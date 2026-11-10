---
title: "Infinite sampling-time blocks can't chain together"
url: "/forum/topic/365/"
archiveKind: "topic"
---
# Infinite sampling-time blocks can't chain together

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1485">
<header><strong>bmairs</strong><time datetime="2011-02-25 17:42 UTC">2011-02-25 17:42 UTC</time></header>
<div class="forum-post-body">When using infinite sampling times on initialization blocks (remembering to enable inline parameters), these blocks cannot be chained together with the block ordering input/outputs. If you do this, it only calls the final block reducing earlier blocks to zeroes. <br>
<br>
<br>
<br>
A workaround for this is to manually order the blocks using their Priority property under "Block Properties".<br>
<br>
<br>
<br>
Is it possible to fix this issue so that the block ordering inputs/outputs could work in this situation?</div>
</article>

<article class="forum-post" id="p1508">
<header><strong>bmairs</strong><time datetime="2011-03-09 23:56 UTC">2011-03-09 23:56 UTC</time></header>
<h3>Re: Infinite sampling-time blocks can&#x27;t chain together</h3>
<div class="forum-post-body">Lubin, have you gotten a chance to check this problem out? It's made setting up various initialization calls a lot more tedious than it should be.</div>
</article>

<article class="forum-post" id="p1512">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-13 11:28 UTC">2011-03-13 11:28 UTC</time></header>
<h3>Re: Infinite sampling-time blocks can&#x27;t chain together</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
I didn't took into account your first post.<br>
<br>
Anyway, I'll look at this now.<br>
<br>
Would you have a model example to share as it's always faster to start from an example illustrating the problem.<br>
<br>
<br>
<br>
I'll do my own if it's complicated for you<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1513">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-14 13:23 UTC">2011-03-14 13:23 UTC</time></header>
<h3>Re: Infinite sampling-time blocks can&#x27;t chain together</h3>
<div class="forum-post-body">Does your init functions requires input parameters and output results, or is it only a initialisation function without any input/output parameters ?<br>
<br>
If so, there might be a possibility for me to adapt the C function Call block...</div>
</article>

<article class="forum-post" id="p1514">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-15 07:12 UTC">2011-03-15 07:12 UTC</time></header>
<h3>Re: Infinite sampling-time blocks can&#x27;t chain together</h3>
<div class="forum-post-body">Blockset update : C function Call dialog box new parameters.<br>
<br>
You can now define <br>
<br>
- One function for block update (The function that was used by default in the older C function call block)<br>
<br>
- One function for block Init (Call each time block is reseted, at initialisation time and each time the subsystem containing the block is reseted)<br>
<br>
- One function for block Start (call only once for initialisation and reset purpose)<br>
<br>
<br>
<br>
The initialisation should be placed within the Start function that is always call once, even with the "inline parameters option" activated.<br>
<br>
However, theses two added function cannot readdirectly values from block's inport or output value to block's outport.<br>
<br>
<br>
<br>
Lubin</div>
</article>

