# Kerhuel.eu static wiki and forum archive

This is a standalone Hugo project intended to become a Git submodule in the existing `Websites` repository and, after review, a GitHub Pages site for `kerhuel.eu`.

## Data provenance

The most recent **local** database export found is `mysql168.kerhuelforum.2019-03-25-09h30.gz` in the neighbouring `www.kerhuel.eu/SQL` backup. The MediaWiki and phpBB data are read directly from this gzip-compressed SQL file. No PHP process, MySQL server, Docker image, or live OVH database is needed.

The current archive builder exports the latest main-namespace wiki revisions, public approved phpBB topics/posts, referenced MediaWiki images and phpBB attachments. It does **not** export database accounts, passwords, e-mail addresses, IP fields, private messages, PHP configuration, or SQL dumps. It masks email addresses and IPv4 literals found in public forum post text. The original dumps and `forum/config.php` must remain private.

The forum backup contains posts through 2014-07-24. The local database has 454 topic rows; a Web Archive snapshot showed 476 topics, so check `reports/build-report.md` and investigate completeness before publication.

## Rebuild content from local backups

Requirements on the workstation: Python 3.10+, Pandoc 3.x on `PATH`, the saved website tree and the SQL dump. Hugo Extended is used to build/preview the site. No PHP or SQL engine is installed or started.

From this directory:

```powershell
python tools/build_archive.py
hugo --minify
```

When working from another checkout, specify source locations explicitly:

```powershell
python tools/build_archive.py `
  --sql "D:\path\to\mysql168.kerhuelforum.2019-03-25-09h30.gz" `
  --site-root "D:\path\to\www.kerhuel.eu"
```

Generated Markdown is in `content/`; selected media is copied under `static/`. Build diagnostics and unresolved-link lists are in `reports/`. The script can be rerun; generated content is replaced from the current source snapshot. `public/` is Hugo output and is deliberately git-ignored; GitHub Actions builds and deploys it.

## Local preview

```powershell
hugo server --disableFastRender
```

Open the local address printed by Hugo. Wiki TeX formulas are converted at build time by Pandoc into native MathML (no JavaScript, no KaTeX). Browsers render MathML natively; the formula source stays in the MathML annotation.

## GitHub Pages publication (not yet configured remotely)

1. Create the GitHub repository `kerhuel-eu-static-archive` and push this project only after reviewing the generated content/report.
2. Enable GitHub Pages with **GitHub Actions** as the source. The workflow in `.github/workflows/pages.yml` builds with Hugo Extended and deploys `public/`.
3. The generated site includes `static/CNAME` for `kerhuel.eu`. Do not change OVH DNS until the Pages deployment and custom-domain configuration have been checked.
4. Add this repository to the parent `Websites` repository as a submodule only after its GitHub remote exists. The parent currently has other unrelated untracked files; stage only the intended submodule metadata and gitlink.

No commit, push, GitHub repository creation, or OVH/DNS change has been performed by the builder.
