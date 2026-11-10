---
title: "Generated MPLAB projects don't allow debugging"
url: "/forum/topic/370/"
archiveKind: "topic"
---
# Generated MPLAB projects don't allow debugging

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1505">
<header><strong>bmairs</strong><time datetime="2011-03-09 18:57 UTC">2011-03-09 18:57 UTC</time></header>
<div class="forum-post-body">The MPLAB projects that are generated on compilation don't set up the compilation within MPLAB to allow for debugging and stepping through the code. This is generally what I want to do when I go to use MPLAB. I've found that changing the following options allow for code step-through and variable watching:<br>
<br>
Project-&gt;Build options-&gt;Project under the MPLAB LINK30 tab, Diagnostics category select "Generate map file"<br>
<br>
Project-&gt;Build options-&gt;Project under the MPLAB C30 tab, General category select "Generate debugging information"<br>
<br>
<br>
<br>
Would it make sense for these options to be set by default in the generated MPLAB projects?</div>
</article>

<article class="forum-post" id="p1507">
<header><strong>bmairs</strong><time datetime="2011-03-09 19:20 UTC">2011-03-09 19:20 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t allow debugging</h3>
<div class="forum-post-body">If I change just those two settings I mentioned above, then the .mcp file TOOL_SETTINGS section looks as follows:<br>
<blockquote><br>
[TOOL_SETTINGS]<br>
<br>
TS{7D9C6ECE-785D-44CB-BA22-17BF2E119622}=<br>
<br>
TS{25AC22BD-2378-4FDB-BFB6-7345A15512D3}=<strong>-g</strong> -O3 -fschedule-insns -fschedule-insns2<br>
<br>
TS{7DAC9A1D-4C45-45D6-B25A-D117C74E8F5A}=<strong>-Map="$(BINDIR_)$(TARGETBASE).map"</strong> --report-mem -o"$(BINDIR_)$(TARGETBASE).$(TARGETSUFFIX)"<br>
<br>
TS{509E5861-1E2A-483B-8B6B-CA8DB7F2DD78}=</blockquote><br>
<br>
The bold parts are the only things that've changed.</div>
</article>

<article class="forum-post" id="p1511">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-12 23:18 UTC">2011-03-12 23:18 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t allow debugging</h3>
<div class="forum-post-body">Thanks Bryant,<br>
<br>
<br>
<br>
This will be taken into account in the next release (after 3.4c).<br>
<br>
<br>
<br>
Lubin</div>
</article>

