#!/usr/bin/env python3
"""Build the Kerhuel.eu wiki/forum archive directly from the saved SQL dump.

No PHP runtime, web server, or MySQL import is used. The SQL is read-only;
Pandoc translates current MediaWiki wikitext and Python renders phpBB BBCode.
"""
from __future__ import annotations
import argparse
import datetime as dt
import gzip
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit, parse_qs

PROJECT = Path(__file__).resolve().parents[1]
WEBSITES = PROJECT.parent
DEFAULT_SITE = WEBSITES / 'www.kerhuel.eu'
DEFAULT_DUMP = DEFAULT_SITE / 'SQL' / 'mysql168.kerhuelforum.2019-03-25-09h30.gz'
SAFE_LINK_SCHEME = {'http', 'https', 'mailto'}
ACTIVE_EXTENSIONS = {'.html', '.htm', '.js', '.mjs', '.php', '.svg'}
TEXT_EXTENSIONS = {'.txt', '.m', '.c', '.h', '.log', '.csv', '.md', '.ini', '.xml', '.bat', '.cfg',
                   '.s', '.asm', '.inc', '.mdl', '.tmf', '.lst', '.map', '.def', '.cpp', '.py', '.htm', '.html'}
PICLIST_TOKEN = 'KERHUELPICLISTTOKEN'
MAX_GIT_FILE = 95 * 1024 * 1024  # leave headroom below GitHub's 100 MiB hard limit


def eprint(*args):
    print(*args, file=sys.stderr)


def sql_unescape(value: str):
    if value.strip().upper() == 'NULL':
        return None
    if not value.startswith("'"):
        return value.strip()
    out, i = [], 1
    escapes = {'0': '\0', 'b': '\b', 'n': '\n', 'r': '\r', 't': '\t',
               'Z': '\x1a', "'": "'", '"': '"', '\\': '\\'}
    while i < len(value):
        c = value[i]
        if c == "'":
            # MySQL's doubled quote form is accepted as well as backslash quotes.
            if i + 1 < len(value) and value[i + 1] == "'":
                out.append("'"); i += 2; continue
            break
        if c == '\\' and i + 1 < len(value):
            out.append(escapes.get(value[i + 1], value[i + 1])); i += 2
        else:
            out.append(c); i += 1
    return ''.join(out)


def parse_sql_tuples(payload: str):
    """Yield row lists from a mysqldump VALUES clause, including escaped strings."""
    i, n = 0, len(payload)
    while i < n:
        while i < n and payload[i] not in "('": i += 1
        if i >= n: break
        if payload[i] != '(': i += 1; continue
        i += 1
        fields, token = [], []
        quoted = False
        while i < n:
            c = payload[i]
            if quoted:
                token.append(c)
                if c == '\\' and i + 1 < n:
                    token.append(payload[i + 1]); i += 2; continue
                if c == "'":
                    if i + 1 < n and payload[i + 1] == "'":
                        token.append(payload[i + 1]); i += 2; continue
                    quoted = False
                i += 1; continue
            if c == "'": quoted = True; token.append(c); i += 1; continue
            if c == ',':
                fields.append(sql_unescape(''.join(token).strip())); token = []; i += 1; continue
            if c == ')':
                fields.append(sql_unescape(''.join(token).strip())); i += 1; break
            token.append(c); i += 1
        yield fields


class SQLDump:
    TABLES = {
        'mwiki_page', 'mwiki_revision', 'mwiki_slots', 'mwiki_content', 'mwiki_text',
        'mwiki_categorylinks', 'mwiki_image',
        'phpbb3_forums', 'phpbb3_topics', 'phpbb3_posts', 'phpbb3_attachments',
        'phpbb3_users',
    }
    def __init__(self, path: Path):
        self.path = path
        self.columns: dict[str, list[str]] = {}
        self.rows: dict[str, list[dict]] = {t: [] for t in self.TABLES}

    def read(self):
        opener = gzip.open if self.path.suffix.lower() == '.gz' else open
        create_table = None
        pending = ''
        with opener(self.path, 'rt', encoding='utf-8', errors='replace', newline='') as stream:
            for line in stream:
                cm = re.match(r'CREATE TABLE `([^`]+)`\s*\(', line)
                if cm:
                    create_table = cm.group(1)
                    if create_table in self.TABLES: self.columns[create_table] = []
                    continue
                if create_table:
                    if line.startswith(') ENGINE') or line.startswith(') TYPE'):
                        create_table = None; continue
                    fm = re.match(r'\s+`([^`]+)`\s', line)
                    if fm and create_table in self.TABLES:
                        self.columns[create_table].append(fm.group(1))
                    continue
                if pending:
                    pending += line
                    if ';' not in line: continue
                    line, pending = pending, ''
                im = re.match(r'INSERT INTO `([^`]+)` VALUES\s*(.*);\s*$', line)
                if not im:
                    if line.startswith('INSERT INTO ') and line.count(';') == 0:
                        pending = line
                    continue
                table = im.group(1)
                if table not in self.TABLES: continue
                cols = self.columns.get(table, [])
                for vals in parse_sql_tuples(im.group(2)):
                    if len(vals) != len(cols):
                        raise ValueError(f'{table}: expected {len(cols)} columns, parsed {len(vals)}')
                    self.rows[table].append(dict(zip(cols, vals)))
        missing = [t for t in self.TABLES if t not in self.columns]
        if missing: raise ValueError('Tables absent from SQL dump: ' + ', '.join(sorted(missing)))
        return self


def safe_str(value):
    return '' if value is None else str(value)


def mediawiki_data(db: SQLDump):
    text_rows = {}
    for r in db.rows['mwiki_text']:
        text_rows[str(r.get('old_id'))] = (safe_str(r.get('old_text')), safe_str(r.get('old_flags')))
    content = {str(r.get('content_id')): safe_str(r.get('content_address')) for r in db.rows['mwiki_content']}
    revisions = {str(r.get('rev_id')): r for r in db.rows['mwiki_revision']}
    slots_by_revision = {}
    for r in db.rows['mwiki_slots']:
        # The main content slot has slot_role_id=1 in this MediaWiki 1.33 dump.
        if str(r.get('slot_role_id')) == '1': slots_by_revision[str(r.get('slot_revision_id'))] = r
    current, by_title = [], {}
    for page in db.rows['mwiki_page']:
        if str(page.get('page_namespace')) != '0': continue
        rev = revisions.get(str(page.get('page_latest')))
        if not rev: continue
        slot = slots_by_revision.get(str(rev.get('rev_id')))
        if not slot: continue
        address = content.get(str(slot.get('slot_content_id')), '')
        mt = re.fullmatch(r'tt:(\d+)', address)
        if not mt: continue
        text, flags = text_rows.get(mt.group(1), ('', ''))
        if 'gzip' in flags.lower():
            # No gzip-flagged rows are expected in this dump; fail visibly rather than
            # silently emitting binary/garbled content if the source changes.
            raise ValueError(f"Compressed MediaWiki text row {mt.group(1)} requires explicit decoder")
        title = safe_str(page.get('page_title'))
        is_redirect = str(page.get('page_is_redirect')) == '1' or bool(re.match(r'^\s*#redirect\b', text, re.I))
        entry = {'id': int(page['page_id']), 'title': title, 'text': text,
                 'date': safe_str(rev.get('rev_timestamp')), 'redirect': is_redirect,
                 'page_len': int(page.get('page_len') or 0)}
        current.append(entry); by_title[title.replace('_', ' ').casefold()] = entry
    return current, by_title


def forum_data(db: SQLDump):
    forums = {int(r['forum_id']): r for r in db.rows['phpbb3_forums']}
    users = {int(r['user_id']): safe_str(r.get('username')) for r in db.rows['phpbb3_users']}
    attachments, attach_by_id = [], {}
    for r in db.rows['phpbb3_attachments']:
        try: aid = int(r['attach_id'])
        except (ValueError, TypeError): continue
        item = {'id': aid, 'post_id': int(r.get('post_msg_id') or 0),
                'topic_id': int(r.get('topic_id') or 0),
                'physical': safe_str(r.get('physical_filename')),
                'name': safe_str(r.get('real_filename')),
                'orphan': str(r.get('is_orphan') or '0') == '1',
                'size': int(r.get('filesize') or 0)}
        attachments.append(item); attach_by_id[aid] = item
    posts = {}
    for r in db.rows['phpbb3_posts']:
        if str(r.get('post_approved') or '1') != '1': continue
        try: pid = int(r['post_id']); tid = int(r['topic_id'])
        except (ValueError, TypeError): continue
        posts.setdefault(tid, []).append({
            'id': pid, 'topic_id': tid, 'forum_id': int(r.get('forum_id') or 0),
            'author': users.get(int(r.get('poster_id') or 0), safe_str(r.get('post_username')) or 'Membre'),
            'date': int(r.get('post_time') or 0), 'subject': safe_str(r.get('post_subject')),
            'text': safe_str(r.get('post_text')), 'has_attachment': str(r.get('post_attachment') or '0') == '1',
        })
    topics = []
    for r in db.rows['phpbb3_topics']:
        if str(r.get('topic_approved') or '1') != '1': continue
        try: tid = int(r['topic_id'])
        except (ValueError, TypeError): continue
        topic_posts = sorted(posts.get(tid, []), key=lambda p: (p['date'], p['id']))
        if not topic_posts: continue
        topics.append({'id': tid, 'forum_id': int(r.get('forum_id') or 0),
                       'title': safe_str(r.get('topic_title')) or 'Sujet sans titre', 'posts': topic_posts})
    return forums, topics, attachments, attach_by_id


def fix_nested_anchors(markup):
    """Drop the outer <a> whenever another <a> opens inside it (forum posts contain such pairs)."""
    out, stack, pos = [], [], 0  # stack entries: [index of open tag in out, dropped]
    for m in re.finditer(r'<a\b[^>]*>|</a\s*>', markup, flags=re.I):
        out.append(markup[pos:m.start()]); pos = m.end()
        tok = m.group(0)
        if tok[:2].lower() == '<a':
            if stack:
                stack[-1][1] = True
                out[stack[-1][0]] = ''
            stack.append([len(out), False])
            out.append(tok)
        elif stack:
            _, dropped = stack.pop()
            out.append('' if dropped else '</a>')
    out.append(markup[pos:])
    return ''.join(out)


MATH_RE = re.compile(r'\$\$.+?\$\$|\$[^$\n]+\$', re.S)


def mathml_markdown(md, warnings):
    """Replace each TeX formula ($...$ or $$...$$) by native MathML, converted by Pandoc in ONE
    batch (one formula per paragraph, so the n-th <math> of the output belongs to the n-th formula).
    Browsers render MathML natively: no JavaScript, no KaTeX fonts. On any mismatch the Markdown is
    returned unchanged and a warning is recorded."""
    found = list(MATH_RE.finditer(md))
    if not found:
        return md
    src = '\n\n'.join(m.group(0) for m in found) + '\n'
    proc = subprocess.run(['pandoc', '--from=markdown+tex_math_dollars', '--to=html5', '--mathml', '--wrap=none'],
                          input=src, capture_output=True, text=True, encoding='utf-8')
    maths = re.findall(r'<math\b.*?</math>', proc.stdout, re.S)
    if proc.returncode != 0 or len(maths) != len(found):
        warnings.append(f'MathML conversion skipped ({len(found)} formulas, {len(maths)} converted, rc={proc.returncode})')
        return md
    maths = [re.sub(r'\s+xmlns="[^"]+"', '', x) for x in maths]
    it = iter(maths)
    return MATH_RE.sub(lambda _m: next(it), md)


def join_raw_html_blocks(markup):
    """Forum post HTML must stay one raw HTML block: a blank line ends it (even inside <pre>),
    and then Markdown turns text such as '### ...' or lines followed by '----' into headings.
    Outside <pre>, blank lines are removed; inside <pre>, each blank line becomes an invisible
    <wbr> so the printed line structure is unchanged."""
    def fix_article(m):
        parts = re.split(r'(<pre\b.*?</pre>)', m.group(0), flags=re.S | re.I)
        return ''.join(re.sub(r'(?m)^[ \t]*$', '<wbr>', p) if i % 2 else re.sub(r'(?m)^[ \t]*\n', '', p)
                       for i, p in enumerate(parts))
    return re.sub(r'<article\b.*?</article>', fix_article, markup, flags=re.S | re.I)


def normalized_title(title):
    return safe_str(title).replace('_', ' ').strip()


# Old MediaWiki URLs are not indexed any more, so the archive uses one simple rule:
# every wiki page gets a unique ASCII slug (lowercase, dash-separated). Files, links
# and navigation all go through wiki_url(), so they can never disagree.
WIKI_SLUGS = {}  # casefolded title -> unique slug, filled by assign_wiki_slugs()


def slug_for(title):
    t = unicodedata.normalize('NFKD', normalized_title(title)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-') or 'page'


def assign_wiki_slugs(titles):
    used = set()
    for title in sorted(set(titles), key=str):
        key = normalized_title(title).casefold()
        if key in WIKI_SLUGS: continue
        base, n = slug_for(title), 1
        slug = base
        while slug in used:
            n += 1
            slug = f'{base}-{n}'
        used.add(slug)
        WIKI_SLUGS[key] = slug


def wiki_url(title):
    slug = WIKI_SLUGS.get(normalized_title(title).casefold()) or slug_for(title)
    return '/wiki/' + slug + '/'


def safe_filename(name):
    name = Path(name.replace('\\', '/')).name
    name = re.sub(r'[^\w.() -]+', '_', name, flags=re.UNICODE).strip(' .')
    return name or 'file'


def html_attr(s):
    return html.escape(safe_str(s), quote=True)


def yaml_quote(s):
    return json.dumps(safe_str(s), ensure_ascii=False)


def slugify(s):
    s = unquote(s).replace('_', ' ').strip().lower()
    s = re.sub(r'[^\w\- ]+', '', s, flags=re.UNICODE)
    return re.sub(r'\s+', '-', s).strip('-') or 'section'


class SiteBuilder:
    def __init__(self, root: Path, dump: Path, db: SQLDump, site_root: Path):
        self.root, self.dump, self.db, self.site_root = root, dump, db, site_root
        self.report = {'source_dump': dump.name, 'source_sha256': self.sha256(dump),
                       'wiki_pages_exported': 0, 'wiki_redirects_omitted': 0,
                       'wiki_links_rewritten': 0, 'wiki_links_unresolved': [],
                       'images_copied': 0, 'images_missing': [],
                       'forum_topics_exported': 0, 'forum_posts_exported': 0,
                       'attachments_copied': 0, 'attachments_missing': [],
                       'legacy_files_copied': 0, 'large_files_not_copied': [],
                       'unsafe_attachments_renamed': [], 'redacted_emails': 0,
                       'redacted_ipv4': 0, 'warnings': []}
        self.articles, self.by_title = mediawiki_data(db)
        self.redirect_targets = self._redirect_map()
        self.canonical_titles = {}
        for a in self.articles:
            self.canonical_titles[a['title'].replace('_', ' ').casefold()] = self._resolve_redirect(a['title'])
        self.forums, self.topics, self.attachments, self.attach_by_id = forum_data(db)
        self.topic_by_id = {t['id']: t for t in self.topics}
        self.post_to_topic = {p['id']: t['id'] for t in self.topics for p in t['posts']}
        self.category_urls = {safe_str(r.get('cl_to')).casefold(): '/wiki/category/' + slugify(safe_str(r.get('cl_to'))) + '/'
                              for r in db.rows['mwiki_categorylinks'] if r.get('cl_to')}
        self.attachment_urls = {}
        self.image_sources = {}
        self.legacy_urls = {}
        self.images_index = None
        self.asset_report_items = []

    @staticmethod
    def sha256(path):
        h = hashlib.sha256()
        with open(path, 'rb') as f:
            for block in iter(lambda: f.read(1024 * 1024), b''): h.update(block)
        return h.hexdigest()

    def _redirect_map(self):
        found = {}
        for a in self.articles:
            m = re.match(r'^\s*#redirect\s*\[\[([^\]|#]+)', a['text'], re.I)
            if m: found[a['title'].replace('_', ' ').casefold()] = normalized_title(m.group(1))
        return found

    def _resolve_redirect(self, title, seen=None):
        key = normalized_title(title).casefold()
        seen = set() if seen is None else seen
        if key in seen: return normalized_title(title)
        seen.add(key)
        target = self.redirect_targets.get(key)
        if target: return self._resolve_redirect(target, seen)
        return normalized_title(title)

    def setup_dirs(self):
        # Clear generated trees only; keep authored layouts, styles, vendor files and CNAME.
        for p in ['content/wiki', 'content/forum', 'content/categories', 'static/images',
                  'static/forum/attachments', 'static/legacy', 'static/RTWdsPIC', 'reports']:
            path = self.root / p
            if path.exists(): shutil.rmtree(path)
            path.mkdir(parents=True, exist_ok=True)
        stale = self.root / 'content/archive-assets.md'
        if stale.exists(): stale.unlink()

    def index_images(self):
        base = self.site_root / 'w' / 'images'
        idx = {}
        for path in base.rglob('*'):
            if not path.is_file() or 'thumb' in {x.lower() for x in path.parts}: continue
            if path.name.startswith('.'): continue
            idx.setdefault(path.name.casefold(), []).append(path)
        self.images_index = idx

    def copy_image(self, filename):
        filename = unquote(filename).strip()
        if not filename: return None
        base = Path(filename).name
        candidates = [base, base.replace(' ', '_'), base.replace('_', ' ')]
        choices = []
        for candidate in candidates:
            choices = self.images_index.get(candidate.casefold(), [])
            if choices: break
        if not choices:
            self.report['images_missing'].append(base); return None
        # MediaWiki filenames are unique. Prefer the root/original over generated thumbs.
        source = sorted(choices, key=lambda p: (len(p.parts), p.as_posix().lower()))[0]
        outname = safe_filename(source.name)
        dest = self.root / 'static' / 'images' / outname
        if dest.exists() and self.sha256(dest) != self.sha256(source):
            stem, suffix = dest.stem, dest.suffix
            outname = f'{stem}-{hashlib.sha1(str(source).encode()).hexdigest()[:8]}{suffix}'
            dest = self.root / 'static' / 'images' / outname
        if not dest.exists(): shutil.copy2(source, dest); self.report['images_copied'] += 1
        url = '/images/' + quote(outname, safe='-_.()')
        self.image_sources[base.casefold()] = url
        self.image_sources[source.name.casefold()] = url
        return url

    def copy_attachment(self, aid):
        item = self.attach_by_id.get(int(aid))
        if not item or item['orphan']:
            return None
        src = self.site_root / 'forum' / 'files' / item['physical']
        if not src.is_file():
            self.report['attachments_missing'].append(int(aid)); return None
        name = safe_filename(item['name'])
        if Path(name).suffix.lower() in ACTIVE_EXTENSIONS:
            name += '.txt'
            self.report['unsafe_attachments_renamed'].append(int(aid))
        rel = f'{aid}-{name}'
        dest = self.root / 'static' / 'forum' / 'attachments' / rel
        if not dest.exists():
            if Path(name).suffix.lower() in TEXT_EXTENSIONS:
                # Forum text attachments often contain e-mail addresses (logs, config dumps).
                # latin-1 round-trip is lossless (byte-exact outside the masked e-mails); utf-8 'replace' would corrupt legacy cp1252 bytes.
                dest.write_bytes(self.redact_emails(src.read_bytes().decode('latin-1')).encode('latin-1'))
            else:
                shutil.copy2(src, dest)
            self.report['attachments_copied'] += 1
        url = '/forum/attachments/' + quote(rel, safe='-_.()')
        self.attachment_urls[int(aid)] = url
        return url

    def copy_legacy_file(self, relpath):
        relpath = unquote(relpath).lstrip('/')
        if relpath.startswith('RTWdsPIC/') and (self.site_root / relpath).is_file():
            # Already published by copy_legacy_tree() at the same path.
            return '/' + quote(relpath, safe='/-_.()')
        # Never copy server configuration, SQL dumps, PHP source, hidden metadata, or git dirs.
        if any(part.startswith('.') or part.lower() in {'.git', 'config', 'cache'} for part in Path(relpath).parts):
            return None
        if Path(relpath).suffix.lower() in {'.php', '.sql', '.gz', '.zip', '.bak'} and relpath.startswith(('forum/', 'w/', 'w_old/')):
            return None
        src = (self.site_root / relpath).resolve()
        try: src.relative_to(self.site_root.resolve())
        except ValueError: return None
        if not src.is_file(): return None
        size = src.stat().st_size
        if size > MAX_GIT_FILE:
            if not any(x['path'] == relpath for x in self.report['large_files_not_copied']):
                self.report['large_files_not_copied'].append({'path': relpath, 'size': size})
            return None
        dest = self.root / 'static' / 'legacy' / relpath
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists(): shutil.copy2(src, dest); self.report['legacy_files_copied'] += 1
        return '/legacy/' + quote(relpath, safe='/-_.()')

    def rewrite_url(self, raw_url):
        raw_url = html.unescape(raw_url).strip().replace('&amp;', '&')
        try: u = urlsplit(raw_url)
        except ValueError: return None
        host = (u.hostname or '').lower()
        if host not in {'kerhuel.eu', 'www.kerhuel.eu', 'kerhuel.fr', 'www.kerhuel.fr'}:
            return None
        path = u.path or '/'
        if '&kerhuelforum_mwiki__session=' in path:
            path = path.split('&kerhuelforum_mwiki__session=', 1)[0]
        if path in {'/', '/index.html'}:
            return '/'
        # Pandoc's MediaWiki reader appends a link label to some external URL
        # filenames (e.g. `.html_Report`). Trim only a recognized label suffix.
        for ext in ('.html', '.htm', '.hex', '.pdf', '.zip', '.txt', '.png', '.jpg'):
            marker = ext + '_'
            at = path.lower().find(marker)
            if at >= 0:
                path = path[:at + len(ext)]
                break
        q = parse_qs(u.query)
        if path.endswith('/forum/viewtopic.php') or path.endswith('/viewtopic.php'):
            tid = (q.get('t') or [None])[0]
            pid = (q.get('p') or [None])[0]
            if pid and pid.isdigit() and int(pid) in self.post_to_topic:
                dest = f"/forum/topic/{self.post_to_topic[int(pid)]}/#p{pid}"
                self.report['wiki_links_rewritten'] += 1; return dest
            if tid and tid.isdigit() and int(tid) in self.topic_by_id:
                self.report['wiki_links_rewritten'] += 1; return f'/forum/topic/{tid}/'
            return '/forum/'
        if path.endswith('/forum/viewforum.php') or path.endswith('/viewforum.php'):
            fid = (q.get('f') or [None])[0]
            self.report['wiki_links_rewritten'] += 1
            return f'/forum/#forum-{fid}' if fid else '/forum/'
        if path.endswith('/forum/download/file.php') or path.endswith('/download/file.php'):
            aid = (q.get('id') or [None])[0]
            dest = self.copy_attachment(int(aid)) if aid and aid.isdigit() else None
            if dest: self.report['wiki_links_rewritten'] += 1; return dest
            return '/forum/'
        if path.startswith('/forum'):
            self.report['wiki_links_rewritten'] += 1; return '/forum/'
        if path.endswith('/wiki/index.php') or path.endswith('/w/index.php'):
            title = (q.get('title') or [None])[0]
            if title:
                target = self.resolve_wiki_title(title)
                if target: self.report['wiki_links_rewritten'] += 1; return target
            return '/wiki/'
        if path.startswith('/wiki/'):
            target = self.resolve_wiki_title(path[len('/wiki/'):])
            if target: self.report['wiki_links_rewritten'] += 1; return target
        rel = path.lstrip('/')
        local = self.copy_legacy_file(rel)
        if local:
            self.report['wiki_links_rewritten'] += 1
            return local + (('#' + u.fragment) if u.fragment else '')
        too_large = (self.site_root / rel).resolve()
        if too_large.is_file() and too_large.stat().st_size > MAX_GIT_FILE:
            self.report['wiki_links_rewritten'] += 1
            return '/archive-assets/#large-file-' + slugify(Path(rel).name)
        if path.startswith(('/w/images/', '/images/')):
            name = Path(path).name.casefold()
            target = self.image_sources.get(name)
            if target: self.report['wiki_links_rewritten'] += 1; return target
        return None

    def resolve_wiki_title(self, raw, source_title=None):
        raw = unquote(raw).replace('_', ' ').strip()
        if raw.startswith('/') and source_title:
            raw = normalized_title(source_title).rstrip('/') + raw
        raw = raw.lstrip(':')
        if raw.casefold().startswith(('media:', 'file:', 'image:')):
            filename = raw.split(':', 1)[1]
            return self.copy_image(filename)
        if '#' in raw:
            title, frag = raw.split('#', 1)
            suffix = '#' + slugify(frag)
        else: title, suffix = raw, ''
        if ':' in title and title.split(':', 1)[0].casefold() == 'category':
            c = title.split(':', 1)[1]
            return self.category_urls.get(c.casefold(), '/wiki/categories/') + suffix
        canonical = self._resolve_redirect(title)
        if canonical.casefold() not in self.by_title:
            return None
        return wiki_url(canonical) + suffix

    def _piclist_html(self, wikitext):
        """Chip matrix {{PicList}}: nested MediaWiki tables, converted to HTML by Pandoc.

        Pandoc's Markdown writer cannot represent these nested tables, so the page gets a
        token that is swapped for this HTML after conversion."""
        wikitext = wikitext.replace("''''''", '')
        proc = subprocess.run(['pandoc', '--from=mediawiki', '--to=html5', '--wrap=none'],
                              input=wikitext, text=True, encoding='utf-8', errors='replace', capture_output=True)
        if proc.returncode:
            self.report['warnings'].append('PicList conversion failed: ' + proc.stderr[:200])
            return ''
        h = re.sub(r'<a href="Category:[^"]*"[^>]*>.*?</a>', '', proc.stdout, flags=re.S)
        h = re.sub(r'<hr\s*/?>', '', h)
        def fix_anchor(m):
            target = self.resolve_wiki_title(html.unescape(m.group(1)))
            return f'<a href="{target}">{m.group(2)}</a>' if target else m.group(2)
        h = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', fix_anchor, h, flags=re.S)
        h = re.sub(r'<td([^>]*)><p><strong>([^<]+)</strong></p></td>', r'<th scope="col"\1>\2</th>', h)
        return '<div class="chip-matrix">' + ' '.join(h.split()) + '</div>'

    def _expand_templates(self, text):
        # The live articles use four simple metadata templates and one static chip table.
        constants = {'blocksetversion': '3.7e', 'blocksetdate': '10 sep 2012', 'blocksetnbrchips': '100'}
        piclist = None
        for p in self.db.rows['mwiki_page']:
            if int(p.get('page_namespace') or -1) != 10 or safe_str(p.get('page_title')).casefold() != 'piclist': continue
            rev = next((r for r in self.db.rows['mwiki_revision'] if str(r.get('rev_id')) == str(p.get('page_latest'))), None)
            if not rev: continue
            slot = next((s for s in self.db.rows['mwiki_slots'] if str(s.get('slot_revision_id')) == str(rev.get('rev_id')) and str(s.get('slot_role_id')) == '1'), None)
            if not slot: continue
            con = next((c for c in self.db.rows['mwiki_content'] if str(c.get('content_id')) == str(slot.get('slot_content_id'))), None)
            mt = re.fullmatch(r'tt:(\d+)', safe_str(con.get('content_address'))) if con else None
            row = next((r for r in self.db.rows['mwiki_text'] if mt and str(r.get('old_id')) == mt.group(1)), None)
            if row: piclist = safe_str(row.get('old_text')).replace('{{table}}', '')
            break
        def replace_template(m):
            if getattr(self, 'piclist_html', None) is None and piclist is not None:
                self.piclist_html = self._piclist_html(piclist)
            name = m.group(1).strip().replace('_', ' ').casefold()
            if name in constants: return constants[name]
            if name == 'piclist' and piclist is not None:
                return '\n\n' + PICLIST_TOKEN + '\n\n'
            if name.startswith('#evt:'):
                args = m.group(0)
                vid = re.search(r'\|\s*id\s*=\s*([^|}]+)', args, re.I)
                service = re.search(r'service\s*=\s*([^|}]+)', args, re.I)
                if vid:
                    svc = safe_str(service.group(1) if service else 'youtube').strip().lower()
                    ident = safe_str(vid.group(1)).strip()
                    host = 'vimeo.com' if 'vimeo' in svc else 'www.youtube.com/watch?v='
                    href = f'https://{host}{ident}' if 'vimeo' in svc else f'https://{host}{ident}'
                    return f'[Video archivé]({href})'
                return '[Vidéo archivée]'
            if name.startswith('#widget:') or name in {'only in print', 'hide in print'}:
                return ''
            # Do not publish unresolved parser functions/template implementation text.
            self.report['warnings'].append('Unexpanded template: ' + m.group(0)[:100])
            return ''
        # Repeated passes expand simple nested calls. Protect triple-brace parameters.
        for _ in range(5):
            newer = re.sub(r'\{\{(?!\{)([^{}]*)\}\}', replace_template, text)
            if newer == text: break
            text = newer
        return text

    def _preprocess_mediawiki_images(self, text):
        image_re = re.compile(r'\[\[(?:Image|File):(.+?)\]\]', re.I | re.S)
        def replace(m):
            fields = m.group(1).split('|')
            filename = fields[0].strip()
            options = [x.strip() for x in fields[1:]]
            width = ''
            caption = []
            for option in options:
                if re.fullmatch(r'\d+px', option, re.I): width = option[:-2]
                elif option.casefold() in {'thumb','tumb','thumbnail','frame','frameless','right','rght','left','center','none','border'}: continue
                elif option.startswith(('link=','alt=','class=','page=')): continue
                elif option: caption.append(option)
            url = self.copy_image(filename)
            if not url: return f'<span class="missing-image">[image manquante : {html.escape(filename)}]</span>'
            alt = caption[-1] if caption else filename
            alt = re.sub(r'\[https?://[^\s\]]+\s+([^\]]+)\]', r'\1', alt)
            alt = re.sub(r'\[\[[^|\]]+\|([^\]]+)\]\]', r'\1', alt)
            alt = alt.replace("'''", '').replace("''", '')
            size = f' width="{int(width)}"' if width.isdigit() and int(width) <= 1200 else ''
            cap = f'<figcaption>{html.escape(alt)}</figcaption>' if caption else ''
            return f'<figure class="wiki-figure"><img loading="lazy" src="{html_attr(url)}" alt="{html_attr(alt)}"{size}>{cap}</figure>'
        return image_re.sub(replace, text)

    def _pandoc_markdown(self, title, text):
        text = self._expand_templates(text)
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        text = self._preprocess_mediawiki_images(text)
        # Repair the one known missing bracket in the old Output Compare link if present.
        text = re.sub(r'(\[\[[^\]]+\|[^\]]+)\](\s+or\s+\[\[)', r'\1]]\2', text)
        cmd = ['pandoc', '--from=mediawiki', '--to=markdown+tex_math_dollars', '--wrap=none']
        proc = subprocess.run(cmd, input=text, text=True, encoding='utf-8', errors='replace',
                              capture_output=True, cwd=self.root)
        if proc.returncode:
            self.report['warnings'].append(f'Pandoc failed for {title}: {proc.stderr[:300]}')
            return '<!-- Conversion failed; source is available in the private backup. -->\n'
        md = proc.stdout
        md = md.replace(PICLIST_TOKEN, getattr(self, 'piclist_html', '') or '')
        # Pandoc wraps raw HTML as `<tag ...>`{=html}; goldmark would show it as code. Unwrap it.
        md = re.sub(r'`(<[^`\n]+>)`\{=html\}', r'\1', md)
        if proc.stderr.strip():
            self.report['warnings'].append(f'Pandoc warning for {title}: {proc.stderr.strip()[:300]}')
        # Rewrite Pandoc's .wikilink attributes to our stable archive URL structure.
        linkpat = re.compile(r'\[(?P<label>[^\]]*)\]\((?P<target>[^\s)]+)(?:\s+"[^"]*")?\)\{\.wikilink\}')
        def link_repl(m):
            target, label = m.group('target'), m.group('label')
            if urlsplit(target).scheme.lower() in {'http', 'https'}:
                return f'[{label}]({target})'
            mapped = self.resolve_wiki_title(target, source_title=title)
            if mapped:
                self.report['wiki_links_rewritten'] += 1
                return f'[{label}]({mapped})'
            self.report['wiki_links_unresolved'].append({'source': title, 'target': target})
            return label
        md = linkpat.sub(link_repl, md)
        # Rewrite plain external URLs pointing back into the former site.
        def old_url_repl(m):
            target = m.group(1)
            mapped = self.rewrite_url(target)
            return '](' + mapped + ')' if mapped else '](' + target + ')'
        md = re.sub(r'\]\((https?://[^\s)]+)\)', old_url_repl, md)
        def autolink_repl(m):
            target = m.group(1)
            mapped = self.rewrite_url(target)
            return '<' + (mapped or target) + '>'
        md = re.sub(r'<(https?://[^>\s]+)>', autolink_repl, md)
        # Rewrite image paths emitted either as Markdown or HTML by Pandoc.
        def img_repl(m):
            alt, dest, rest = m.group(1), m.group(2), m.group(3) or ''
            mapped = self.image_sources.get(Path(unquote(dest)).name.casefold())
            if not mapped: mapped = self.copy_image(Path(unquote(dest)).name)
            if mapped: return f'![{alt}]({mapped}{rest})'
            return f'![{alt}](/archive-assets/)'
        md = re.sub(r'!\[([^\]]*)\]\(([^\s)]+)([^)]*)\)', img_repl, md)
        def html_img(m):
            tag = m.group(0)
            sm = re.search(r'\bsrc=["\']([^"\']+)', tag, re.I)
            if not sm: return tag
            mapped = self.image_sources.get(Path(unquote(sm.group(1))).name.casefold()) or self.copy_image(Path(unquote(sm.group(1))).name)
            if not mapped: return '<span class="missing-image">[image indisponible]</span>'
            return tag[:sm.start(1)] + mapped + tag[sm.end(1):]
        md = re.sub(r'<img\b[^>]*>', html_img, md, flags=re.I)
        # Remove MediaWiki category directives from prose; category membership is
        # rebuilt from mwiki_categorylinks in Hugo's category index.
        md = re.sub(r'\[\[Category:[^\]]+\]\]', '', md, flags=re.I)
        # Avoid raw/active markup from an imported page.
        md = re.sub(r'<script\b[^>]*>.*?</script\s*>', '', md, flags=re.I | re.S)
        md = re.sub(r'<iframe\b[^>]*>.*?</iframe\s*>', '[contenu embarqué retiré]', md, flags=re.I | re.S)
        md = re.sub(r'\son\w+\s*=\s*(["\']).*?\1', '', md, flags=re.I | re.S)
        md = re.sub(r'javascript:', '', md, flags=re.I)
        return md.strip() + '\n'

    def _bbcode_tree(self, text):
        token = re.compile(r'\[(/?)\s*([a-z*]+)(?:\s*=\s*([^\]]*))?\]', re.I)
        root = {'tag': None, 'arg': None, 'children': []}; stack = [root]
        pos = 0
        while True:
            m = token.search(text, pos)
            if not m:
                stack[-1]['children'].append(text[pos:]); break
            if m.start() > pos: stack[-1]['children'].append(text[pos:m.start()])
            closing, tag, arg = bool(m.group(1)), m.group(2).lower(), m.group(3)
            if tag == 'code' and not closing:
                end = re.search(r'\[/code\s*\]', text[m.end():], re.I)
                if end:
                    raw = text[m.end():m.end()+end.start()]
                    stack[-1]['children'].append({'tag': 'code', 'arg': arg, 'children': [raw]})
                    pos = m.end() + end.end(); continue
            if tag == '*' and not closing:
                if stack[-1].get('tag') == 'li': stack.pop()
                node = {'tag': 'li', 'arg': arg, 'children': []}; stack[-1]['children'].append(node); stack.append(node)
            elif closing:
                for k in range(len(stack)-1, 0, -1):
                    if stack[k].get('tag') == tag:
                        stack = stack[:k]; break
                else:
                    stack[-1]['children'].append(m.group(0))
            elif tag in {'b','i','u','s','strike','sub','sup','url','email','img','quote','list','color','size','align','font','attachment','hr','*'}:
                if tag == 'hr': stack[-1]['children'].append({'tag':'hr','arg':arg,'children':[]})
                else:
                    node = {'tag': tag, 'arg': arg, 'children': []}; stack[-1]['children'].append(node); stack.append(node)
            else:
                stack[-1]['children'].append(m.group(0))
            pos = m.end()
        return root

    def redact_text(self, text):
        text, n_email = re.subn(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '[adresse e-mail retirée]', text)
        text, n_ip = re.subn(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])', '[adresse IP retirée]', text)
        self.report['redacted_emails'] += n_email; self.report['redacted_ipv4'] += n_ip
        return text

    def redact_emails(self, text):
        text, n = re.subn(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '[adresse e-mail retirée]', text)
        self.report['redacted_emails'] += n
        return text

    def legacy_page_text(self, src):
        text = self.redact_emails(src.read_bytes().decode('utf-8', errors='replace'))
        # Old pages link to ../wiki/<Title>; point them at the new wiki when the page exists.
        def repl(m):
            target = self.resolve_wiki_title(m.group(2))
            return f'{m.group(1)}="{target}' if target else m.group(0)
        return re.sub(r'(href|src)="(?:\.\./)+wiki/([^"#?]*)', repl, text)

    def copy_legacy_tree(self):
        """Publish the old RTWdsPIC static mirror at /RTWdsPIC/ with the same paths."""
        for name in ('Img', 'Resume'):  # root-level assets used by ../Img/... links of the old pages
            tree = self.site_root / name
            if not tree.is_dir(): continue
            for src in tree.rglob('*'):
                if not src.is_file(): continue
                dest = self.root / 'static' / name / src.relative_to(tree)
                dest.parent.mkdir(parents=True, exist_ok=True)
                if src.suffix.lower() in {'.html', '.htm', '.txt'}:
                    dest.write_text(self.redact_emails(src.read_bytes().decode('utf-8', errors='replace')), encoding='utf-8')
                else:
                    shutil.copy2(src, dest)
        fav = self.site_root / 'favicon.ico'
        if fav.is_file():
            (self.root / 'static').mkdir(parents=True, exist_ok=True)
            shutil.copy2(fav, self.root / 'static' / 'favicon.ico')
        src_root = self.site_root / 'RTWdsPIC'
        if not src_root.is_dir(): return
        for src in sorted(src_root.rglob('*')):
            if not src.is_file(): continue
            rel = src.relative_to(src_root)
            if any(p.startswith('.') or p.lower() in {'.git', 'cache', 'config'} for p in rel.parts): continue
            if src.suffix.lower() in {'.php', '.sql', '.gz', '.zip', '.bak'} and False: continue
            size = src.stat().st_size
            if size > MAX_GIT_FILE:
                self.report['large_files_not_copied'].append({'path': 'RTWdsPIC/' + rel.as_posix(), 'size': size})
                continue
            dest = self.root / 'static' / 'RTWdsPIC' / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src.suffix.lower() in {'.html', '.htm', '.txt'}:
                dest.write_text(self.legacy_page_text(src), encoding='utf-8')
            else:
                shutil.copy2(src, dest)
            self.report['legacy_files_copied'] += 1

    def old_site_url(self, url):
        mapped = self.rewrite_url(url)
        if mapped: return mapped
        u = urlsplit(url)
        if (u.hostname or '').lower() in {'kerhuel.eu', 'www.kerhuel.eu', 'kerhuel.fr', 'www.kerhuel.fr'}:
            return '/archive-assets/'
        return None

    def render_text(self, text):
        # Protect URLs before redacting email/IP literals, so an IP-based link remains
        # syntactically valid while standalone personal addresses are removed.
        text = html.unescape(text)
        urls = []
        def hold(m):
            raw = m.group(0); tail = ''
            while raw and raw[-1] in '.,!?;:)': tail = raw[-1] + tail; raw = raw[:-1]
            token = f'\x00URL{len(urls)}\x00'; urls.append((raw, tail)); return token
        text = re.sub(r'https?://[^\s<>"\']+', hold, text)
        text = self.redact_text(text)
        pieces = re.split(r'(\x00URL\d+\x00)', text)
        out = []
        for part in pieces:
            um = re.fullmatch(r'\x00URL(\d+)\x00', part)
            if um:
                raw, tail = urls[int(um.group(1))]
                href = self.old_site_url(raw)
                if not href:
                    scheme = urlsplit(raw).scheme.lower()
                    href = raw if scheme in SAFE_LINK_SCHEME else None
                label = html.escape(raw, quote=False)
                out.append(f'<a href="{html_attr(href)}" rel="nofollow">{label}</a>{html.escape(tail)}' if href else label + html.escape(tail))
            else:
                out.append(html.escape(part, quote=False).replace('\r\n','\n').replace('\r','\n').replace('\n','<br>\n'))
        return ''.join(out)

    def render_bbnode(self, node):
        if isinstance(node, str): return self.render_text(node)
        tag, arg, children = node.get('tag'), safe_str(node.get('arg')), node.get('children', [])
        if tag == 'code':
            raw = self.redact_text(html.unescape(''.join(str(x) for x in children)))
            return '<pre><code>' + html.escape(raw, quote=False) + '</code></pre>'
        child = ''.join(self.render_bbnode(c) for c in children)
        if tag == 'b': return '<strong>' + child + '</strong>'
        if tag == 'i': return '<em>' + child + '</em>'
        if tag == 'u': return '<span class="underline">' + child + '</span>'
        if tag in {'s','strike'}: return '<del>' + child + '</del>'
        if tag == 'sub': return '<sub>' + child + '</sub>'
        if tag == 'sup': return '<sup>' + child + '</sup>'
        if tag == 'hr': return '<hr>'
        if tag == 'li': return '<li>' + child + '</li>'
        if tag == 'list':
            ordered = arg.strip() not in {'', '1', 'a', 'A', 'i', 'I'} and arg.strip().isdigit()
            return ('<ol>' if ordered else '<ul>') + child + ('</ol>' if ordered else '</ul>')
        if tag == 'quote':
            author = self.redact_text(arg.split(',',1)[0].strip().strip('"\''))
            label = f'<header class="quote-author">Citation : {html.escape(author)}</header>' if author else ''
            return '<blockquote>' + label + child + '</blockquote>'
        if tag == 'url':
            if not arg.strip() and '<a ' in child:
                return child
            # Plain URL labels are auto-linked while rendering their text nodes; unwrap
            # that inner anchor before adding the BBCode URL's authoritative target.
            child = re.sub(r'<a\b[^>]*>(.*?)</a>', r'\1', child, flags=re.I | re.S)
            target = arg.strip() or re.sub(r'<[^>]+>', '', child).strip()
            mapped = self.old_site_url(target)
            u = urlsplit(target)
            href = mapped or (target if u.scheme in SAFE_LINK_SCHEME else None)
            return f'<a href="{html_attr(href)}">{child or html.escape(target)}</a>' if href else child
        if tag == 'email':
            self.report['redacted_emails'] += 1
            return '[adresse e-mail retirée]'
        if tag == 'img':
            target = arg.strip() or re.sub(r'<[^>]+>', '', child).strip()
            mapped = self.old_site_url(target)
            if mapped and mapped.startswith(('/images/', '/legacy/', '/RTWdsPIC/')):
                return f'<img loading="lazy" src="{html_attr(mapped)}" alt="Image du forum">'
            return f'<a href="{html_attr(mapped or target)}">Image externe (non intégrée)</a>'
        if tag == 'attachment':
            m = re.search(r'\d+', arg)
            aid = int(m.group(0)) if m else None
            url = self.copy_attachment(aid) if aid else None
            if not url: return '[pièce jointe non disponible]'
            name = (self.attach_by_id.get(aid) or {}).get('name', '')
            if Path(name).suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}:
                # Inline image attachment: show it in the post, as phpBB does.
                return f'<img loading="lazy" src="{html_attr(url)}" alt="{html_attr(name)}">'
            return f'<a class="attachment" href="{html_attr(url)}" download>{child or "Télécharger la pièce jointe"}</a>'
        if tag == 'color':
            color = arg.strip().lower()
            if re.fullmatch(r'#[0-9a-f]{3,8}|[a-z]{1,20}', color): return f'<span style="color:{color}">{child}</span>'
            return child
        if tag == 'size': return '<span class="forum-size">' + child + '</span>'
        if tag == 'align':
            align = arg.strip().lower()
            return f'<div class="align-{align}">{child}</div>' if align in {'left','right','center','justify'} else child
        if tag == 'font': return child
        return child

    def normalize_phpbb_post(self, text):
        # phpBB's saved post_text uses an XML-like rich-text representation: <r>/<t>
        # wrappers, <s>/<e> markers containing BBCode, and <URL>/<QUOTE>/<CODE> tags.
        # Convert that representation back to ordinary BBCode before the small renderer.
        raw_codes = []
        code_re = re.compile(r'<CODE\b[^>]*>\s*<s>.*?</s>(.*?)<e>.*?</e>\s*</CODE>', re.I | re.S)
        def hold_code(m):
            token = f'__PHPBB_RAW_CODE_{len(raw_codes)}__'
            raw_codes.append(m.group(1)); return token
        text = code_re.sub(hold_code, text)
        text = html.unescape(text)
        text = re.sub(r'<ATTACHMENT\b[^>]*>.*?</ATTACHMENT>', '', text, flags=re.I | re.S)
        def url_wrapper(m):
            attrs, inner = m.group(1), m.group(2)
            hm = re.search(r'\burl\s*=\s*"([^"]+)"', attrs, re.I)
            href = hm.group(1) if hm else ''
            lm = re.search(r'<LINK_TEXT\b[^>]*\btext\s*=\s*"([^"]*)"[^>]*>', inner, re.I)
            label = lm.group(1) if lm else inner
            label = re.sub(r'<s>.*?</s>|<e>.*?</e>', '', label, flags=re.I | re.S)
            label = re.sub(r'<[^>]+>', '', label).strip()
            return f'[url={href}]{label or href}[/url]' if href else label
        text = re.sub(r'<URL\b([^>]*)>(.*?)</URL>', url_wrapper, text, flags=re.I | re.S)
        def img_wrapper(m):
            attrs, inner = m.group(1), m.group(2)
            hm = re.search(r'\bsrc\s*=\s*"([^"]+)"', attrs, re.I)
            href = hm.group(1) if hm else ''
            um = re.search(r'<URL\b([^>]*)>', inner, re.I)
            if um:
                am = re.search(r'\burl\s*=\s*"([^"]+)"', um.group(1), re.I)
                if am: href = am.group(1)
            return f'[img]{href}[/img]' if href else ''
        text = re.sub(r'<IMG\b([^>]*)>(.*?)</IMG>', img_wrapper, text, flags=re.I | re.S)
        text = re.sub(r'<EMAIL\b[^>]*>.*?</EMAIL>', '[email][adresse e-mail retirée][/email]', text, flags=re.I | re.S)
        def anchor_wrapper(m):
            href = html.unescape(m.group(1)); label = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            return f'[url={href}]{label or href}[/url]'
        text = re.sub(r'<a\b[^>]*\bhref\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>', anchor_wrapper, text, flags=re.I | re.S)
        text = re.sub(r'<s\s*>(.*?)</s\s*>', r'\1', text, flags=re.I | re.S)
        text = re.sub(r'<e\s*>(.*?)</e\s*>', r'\1', text, flags=re.I | re.S)
        text = re.sub(r'<br\s*/?>', '\n', text, flags=re.I)
        text = re.sub(r'</?p\b[^>]*>', '\n\n', text, flags=re.I)
        # Formatting wrapper tags have their real BBCode in the <s>/<e> markers.
        text = re.sub(r'</?(?:r|t|b|i|u|s|quote|code|color|url|link_text|img|email|attachment)\b[^>]*>', '', text, flags=re.I)
        # Remaining legacy XML tags are presentation metadata, not user content.
        text = re.sub(r'</?[A-Z][A-Z0-9_]*(?:\s+[^>]*)?\s*/?>', '', text)
        for i, code in enumerate(raw_codes):
            text = text.replace(f'__PHPBB_RAW_CODE_{i}__', '[code]' + code + '[/code]')
        return text

    def render_bbcode(self, text):
        text = self.normalize_phpbb_post(text)
        tree = self._bbcode_tree(text)
        return ''.join(self.render_bbnode(c) for c in tree['children'])

    def frontmatter(self, title, url, kind='page', extra=None):
        fields = ['---', 'title: ' + yaml_quote(title), 'url: ' + yaml_quote(url),
                  'archiveKind: ' + yaml_quote(kind), '---', '']
        if extra: fields[1:1] = [f'{k}: {yaml_quote(v)}' for k,v in extra.items()]
        return '\n'.join(fields)

    def page_latest_text(self, page_id):
        page = next((x for x in self.db.rows['mwiki_page'] if str(x.get('page_id')) == str(page_id)), None)
        if not page: return ''
        rev = next((x for x in self.db.rows['mwiki_revision'] if str(x.get('rev_id')) == str(page.get('page_latest'))), None)
        slot = next((x for x in self.db.rows['mwiki_slots'] if rev and str(x.get('slot_revision_id')) == str(rev['rev_id']) and str(x.get('slot_role_id')) == '1'), None)
        con = next((x for x in self.db.rows['mwiki_content'] if slot and str(x.get('content_id')) == str(slot.get('slot_content_id'))), None)
        mt = re.fullmatch(r'tt:(\d+)', safe_str(con.get('content_address'))) if con else None
        row = next((x for x in self.db.rows['mwiki_text'] if mt and str(x.get('old_id')) == mt.group(1)), None)
        return safe_str(row.get('old_text')) if row else ''

    def build_wiki_nav(self):
        """Left-hand wiki menu: the sections of MediaWiki:Sidebar (page id 2), then every
        exported page that the sidebar does not list (under 'Other pages')."""
        def clean(label):
            label = label.replace('{{blocksetVersion}}', '3.7e')
            return re.sub(r'\{\{[^}]*\}\}', '', label).replace('_', ' ').strip()
        sections, cur, linked = [], None, set()
        for raw in self.page_latest_text(2).splitlines():
            line = raw.strip()
            if line.startswith('**'):
                if cur is None: continue
                target, _, label = line.lstrip('*').strip().partition('|')
                target = target.strip().replace('DsPIC_DsPIC_', 'DsPIC_')  # typo in the original sidebar
                if target.casefold() == 'mainpage': target = 'Main_Page'  # MediaWiki alias of the main page
                external = bool(re.match(r'https?://', target))
                url = (self.rewrite_url(target) or target) if external else self.resolve_wiki_title(target)
                if not url:
                    self.report['warnings'].append('Sidebar entry not exported: ' + target)
                elif not external:
                    linked.add(url)
                cur['items'].append({'label': clean(label or target), 'url': url, 'external': external})
            elif line.startswith('*'):
                cur = {'title': clean(line.lstrip('*')), 'items': []}
                sections.append(cur)
        others = [{'label': clean(t), 'url': wiki_url(t), 'external': False}
                  for t in self.exported_titles if wiki_url(t) not in linked]
        if others:
            sections.append({'title': 'Other pages', 'items': sorted(others, key=lambda i: i['label'].casefold())})
        out = self.root / 'data' / 'wiki_nav.json'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({'sections': sections}, ensure_ascii=False, indent=1), encoding='utf-8')
        self.report['wiki_nav_sections'] = len(sections)
        self.report['wiki_nav_other_pages'] = len(others)

    def build_wiki(self):
        self.index_images()
        assign_wiki_slugs([a['title'] for a in self.articles])
        # Copy images mentioned in main-namespace article wikitext before translating.
        for a in self.articles:
            if a['title'].casefold().startswith('sandbox'): continue
            text = re.sub(r'<!--.*?-->', '', a['text'], flags=re.S)
            for m in re.finditer(r'\[\[(?:Image|File):([^|\]]+)', text, re.I): self.copy_image(m.group(1))
        self.exported_titles = []
        # Build category membership from the SQL relation table.
        page_by_id = {a['id']: a for a in self.articles}
        categories = {}
        for row in self.db.rows['mwiki_categorylinks']:
            try: pid = int(row['cl_from'])
            except (ValueError, TypeError): continue
            if pid in page_by_id:
                categories.setdefault(safe_str(row.get('cl_to')), set()).add(page_by_id[pid]['title'])
        for a in self.articles:
            if a['title'].casefold().startswith('sandbox'):
                self.report['wiki_redirects_omitted'] += 1; continue
            if a['redirect']:
                self.report['wiki_redirects_omitted'] += 1; continue
            md = self._pandoc_markdown(a['title'], a['text'])
            url = wiki_url(a['title'])
            out = self.root / 'content' / 'wiki' / f'page-{a["id"]}.md'
            try:
                lastmod = dt.datetime.strptime(a['date'], '%Y%m%d%H%M%S').replace(tzinfo=dt.timezone.utc).isoformat().replace('+00:00', 'Z')
            except (ValueError, TypeError):
                lastmod = '2019-03-25T00:00:00Z'
            body = mathml_markdown(self.redact_emails(md), self.report['warnings'])
            out.write_text(self.frontmatter(normalized_title(a['title']), url, extra={'source': 'MediaWiki snapshot 2019-03-25', 'lastmod': lastmod}) + body, encoding='utf-8')
            self.report['wiki_pages_exported'] += 1
            self.exported_titles.append(a['title'])
        # Rewrite titles in redirection chains in all destinations; index contains only real articles.
        lines = ['# Articles du wiki', '', 'Archive du wiki MediaWiki — dernière sauvegarde locale : 25 mars 2019.', '', '']
        for a in sorted(self.articles, key=lambda x: x['title'].casefold()):
            if a['redirect'] or a['title'].casefold().startswith('sandbox'): continue
            lines.append(f'- [{a["title"]}]({wiki_url(a["title"])})')
        (self.root / 'content/wiki/_index.md').write_text(self.frontmatter('Wiki', '/wiki/', kind='section') + '\n'.join(lines) + '\n', encoding='utf-8')
        category_lines = ['# Catégories', '', 'Index des catégories conservées dans l’export.', '']
        for name, members in sorted(categories.items(), key=lambda x:x[0].casefold()):
            slug = slugify(name)
            shown = normalized_title(name)
            curl = '/wiki/category/' + slug + '/'
            cat_file = self.root / 'content/categories' / (slug + '.md')
            body = [f'# {shown}', ''] + [f'- [{normalized_title(t)}]({wiki_url(t)})' for t in sorted(members, key=str.casefold)]
            cat_file.write_text(self.frontmatter(shown, curl, kind='category') + '\n'.join(body) + '\n', encoding='utf-8')
            category_lines.append(f'- [{shown}]({curl}) ({len(members)} pages)')
        (self.root / 'content/wiki/categories.md').write_text(self.frontmatter('Catégories', '/wiki/categories/', kind='page') + '\n'.join(category_lines) + '\n', encoding='utf-8')
        # Update our index of categories for link conversion.
        self.category_urls = {name.casefold(): '/wiki/category/' + slugify(name) + '/' for name in categories}

    def build_forum(self):
        attach_by_post = {}
        for a in self.attachments:
            if a['orphan']: continue
            attach_by_post.setdefault(a['post_id'], []).append(a)
        by_forum = {}
        forum_body = ['# Forum en lecture seule', '',
                      'Archive phpBB issue de la sauvegarde locale du 25 mars 2019. Les derniers messages sauvegardés datent de juillet 2014.',
                      '', 'Aucun compte, adresse e-mail de compte, mot de passe, adresse IP de connexion ni message privé n’est publié.', '']
        for topic in self.topics:
            turl = f"/forum/topic/{topic['id']}/"
            by_forum.setdefault(topic['forum_id'], []).append(topic)
            body = [f'# {topic["title"]}', '', f'Forum : [{safe_str(self.forums.get(topic["forum_id"],{}).get("forum_name","Forum"))}](/forum/#forum-{topic["forum_id"]})', '',
                    f'{len(topic["posts"])} message(s) · archive en lecture seule', '']
            for post in topic['posts']:
                when = dt.datetime.fromtimestamp(post['date'], dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
                author = post['author'] or 'Membre'
                if '@' in author: author = 'Membre'
                if author.lower() in {'anonymous', 'anonyme'}: author = 'Anonyme'
                body.append(f'<article class="forum-post" id="p{post["id"]}">')
                body.append(f'<header><strong>{html.escape(author)}</strong><time datetime="{when}">{when}</time></header>')
                if post['subject'] and post['subject'].strip().casefold() != topic['title'].strip().casefold():
                    body.append(f'<h3>{html.escape(post["subject"])}</h3>')
                body.append('<div class="forum-post-body">' + self.render_bbcode(post['text']) + '</div>')
                attached_ids = set()
                for m in re.finditer(r'\[attachment\s*=\s*(\d+)\]', post['text'], re.I): attached_ids.add(int(m.group(1)))
                for att in attach_by_post.get(post['id'], []):
                    if att['id'] in attached_ids: continue
                    url = self.copy_attachment(att['id'])
                    if url: body.append(f'<p class="attachment-line"><a class="attachment" download href="{html_attr(url)}">Pièce jointe : {html.escape(att["name"])}</a></p>')
                body.append('</article>\n')
            md = join_raw_html_blocks(fix_nested_anchors('\n'.join(body)))
            out = self.root / 'content/forum' / f'topic-{topic["id"]}.md'
            out.write_text(self.frontmatter(topic['title'], turl, kind='topic') + md + '\n', encoding='utf-8')
            self.report['forum_posts_exported'] += len(topic['posts'])
        for fid, forum in sorted(self.forums.items(), key=lambda x:safe_str(x[1].get('forum_name')).casefold()):
            if not by_forum.get(fid): continue
            name = safe_str(forum.get('forum_name')) or f'Forum {fid}'
            forum_body.extend([f'<h2 id="forum-{fid}">{html.escape(name)}</h2>', ''])
            for topic in sorted(by_forum[fid], key=lambda t:t['title'].casefold()):
                forum_body.append(f'- [{topic["title"]}](/forum/topic/{topic["id"]}/) — {len(topic["posts"])} messages')
            forum_body.append('')
        (self.root / 'content/forum/_index.md').write_text(self.frontmatter('Forum', '/forum/', kind='section') + '\n'.join(forum_body) + '\n', encoding='utf-8')
        self.report['forum_topics_exported'] = len(self.topics)

    def build_local_files(self):
        # Scan all article wikitext and public forum post text for old first-party URLs;
        # copy ordinary referenced files and leave oversized files in a review list.
        sources = [a['text'] for a in self.articles if not a['redirect'] and not a['title'].casefold().startswith('sandbox')]
        sources += [p['text'] for t in self.topics for p in t['posts']]
        urls = set()
        for text in sources:
            for m in re.finditer(r'https?://(?:www\.)?kerhuel\.(?:eu|fr)/[^\s<>\]"\']+', text, re.I):
                urls.add(m.group(0).rstrip('.,;:)'))
        for url in sorted(urls):
            self.rewrite_url(url)
        if self.report['large_files_not_copied']:
            lines = ['# Fichiers non inclus dans le dépôt', '',
                     'Certains fichiers dépassent la limite pratique/technique d’un dépôt GitHub. Ils ne sont pas intégrés au site statique ; ajouter les originaux comme assets de GitHub Releases puis mettre à jour les liens avant publication.', '']
            for item in self.report['large_files_not_copied']:
                lines.append(f'- <span id="large-file-{slugify(Path(item["path"]).name)}"></span>`{item["path"]}` — {item["size"]:,} octets')
            (self.root / 'content/archive-assets.md').write_text(self.frontmatter('Fichiers volumineux', '/archive-assets/', kind='page') + '\n'.join(lines) + '\n', encoding='utf-8')

    def build_home(self):
        text = '''# Kerhuel.eu — archives du wiki et du forum

Cette archive statique regroupe les articles du wiki technique et les discussions publiques du forum phpBB. Elle ne permet pas de se connecter, publier ou modifier du contenu.

- [Parcourir le wiki](/wiki/)
- [Parcourir le forum](/forum/)
- [Voir les catégories du wiki](/wiki/categories/)

## État des archives

- Wiki : dernière sauvegarde locale du **25 mars 2019**.
- Forum : dernier message présent dans la sauvegarde du **24 juillet 2014**.
- Les pièces jointes et fichiers de taille compatible avec GitHub sont conservés lorsqu’ils sont référencés.
- Les pages sont figées ; les informations techniques et les téléchargements anciens peuvent être obsolètes.

Les liens internes du wiki et du forum sont convertis vers les pages de cette archive. Certains liens dynamiques de l’ancien site ne sont pas reproductibles.
'''
        (self.root / 'content/_index.md').write_text(self.frontmatter('Kerhuel.eu — archive', '/', kind='home') + text, encoding='utf-8')

    def write_report(self):
        report_dir = self.root / 'reports'; report_dir.mkdir(exist_ok=True)
        obj = dict(self.report)
        obj['source_dump_size'] = self.dump.stat().st_size
        obj['forum_source_posts'] = len(self.db.rows['phpbb3_posts'])
        obj['forum_source_topics'] = len(self.db.rows['phpbb3_topics'])
        obj['wiki_source_pages_ns0'] = sum(1 for p in self.db.rows['mwiki_page'] if str(p.get('page_namespace')) == '0')
        (report_dir / 'build-report.json').write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
        lines = ['# Rapport de génération', '',
                 f'- Dump utilisé : `{self.dump.name}`', f'- SHA-256 du dump : `{obj["source_sha256"]}`',
                 f'- Pages wiki exportées : {obj["wiki_pages_exported"]}; redirects MediaWiki non générés : {obj["wiki_redirects_omitted"]}',
                 f'- Sujets forum exportés : {obj["forum_topics_exported"]}; messages : {obj["forum_posts_exported"]}',
                 f'- Images wiki copiées : {obj["images_copied"]}; manquantes : {len(obj["images_missing"])}',
                 f'- Pièces jointes copiées : {obj["attachments_copied"]}; manquantes : {len(obj["attachments_missing"])}',
                 f'- Fichiers locaux classiques copiés : {obj["legacy_files_copied"]}',
                 f'- E-mails masqués dans les messages : {obj["redacted_emails"]}; IPv4 masquées : {obj["redacted_ipv4"]}', '',
                 '## Vérifications à effectuer avant publication',
                 '- Contrôler les liens non résolus et les images/pièces jointes manquantes dans `build-report.json`.',
                 '- Comparer le nombre de sujets avec les captures Web Archive (le dump local contient 454 sujets).',
                 '- Contrôler les fichiers volumineux absents et les modèles/vidéos signalés.',
                 '- Ne pas ajouter de dump SQL, de `config.php`, de base utilisateurs ou de fichier d’identifiants au dépôt.', '']
        lines += ['## Liens wiki non résolus', '']
        unique = sorted({(x['source'],x['target']) for x in self.report['wiki_links_unresolved']})
        lines += [f'- `{src}` → `{target}`' for src,target in unique[:500]] or ['Aucun.']
        if len(unique) > 500: lines.append(f'- … {len(unique)-500} autres (voir JSON).')
        lines += ['', '## Images manquantes', '']
        lines += [f'- `{x}`' for x in sorted(set(self.report['images_missing']))] or ['Aucune.']
        lines += ['', '## Pièces jointes manquantes', '']
        lines += [f'- ID `{x}`' for x in sorted(set(self.report['attachments_missing']))] or ['Aucune.']
        lines += ['', '## Fichiers > limite GitHub non copiés', '']
        lines += [f'- `{x["path"]}` ({x["size"]:,} octets)' for x in self.report['large_files_not_copied']] or ['Aucun.']
        lines += ['', '## Avertissements', '']
        lines += [f'- {x}' for x in self.report['warnings'][:200]] or ['Aucun.']
        (report_dir / 'build-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    def build(self):
        self.setup_dirs()
        self.build_wiki()
        self.build_wiki_nav()
        self.build_forum()
        self.copy_legacy_tree()
        self.build_local_files()
        self.build_home()
        self.write_report()
        return self.report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sql', type=Path, default=DEFAULT_DUMP, help='MySQL dump (.gz or plain SQL)')
    parser.add_argument('--site-root', type=Path, default=DEFAULT_SITE, help='Saved www.kerhuel.eu tree')
    parser.add_argument('--output', type=Path, default=PROJECT, help='Hugo project directory')
    args = parser.parse_args()
    dump, site, output = args.sql.resolve(), args.site_root.resolve(), args.output.resolve()
    if not dump.is_file(): parser.error(f'SQL dump not found: {dump}')
    if not (site / 'w' / 'images').is_dir(): parser.error(f'MediaWiki images directory not found: {site / "w/images"}')
    if not (site / 'forum' / 'files').is_dir(): parser.error(f'phpBB attachments directory not found: {site / "forum/files"}')
    if not shutil.which('pandoc'):
        parser.error('Pandoc 3.x is required on PATH; no PHP/MySQL is required.')
    print(f'Reading saved SQL: {dump.name}')
    db = SQLDump(dump).read()
    print('SQL rows:', {k: len(v) for k,v in db.rows.items() if v})
    builder = SiteBuilder(output, dump, db, site)
    report = builder.build()
    print(json.dumps({k:report[k] for k in ['wiki_pages_exported','wiki_redirects_omitted','wiki_links_rewritten','forum_topics_exported','forum_posts_exported','images_copied','attachments_copied','legacy_files_copied']}, indent=2))
    print(f'Report: {output / "reports" / "build-report.md"}')

if __name__ == '__main__': main()
