---
title: "CAN block on 33fj256MC710 target"
url: "/forum/topic/374/"
archiveKind: "topic"
---
# CAN block on 33fj256MC710 target

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1516">
<header><strong>ambersil</strong><time datetime="2011-03-24 21:34 UTC">2011-03-24 21:34 UTC</time></header>
<div class="forum-post-body">I'm evaluating the 3.4c blocket (Matlab 2010a) on a 33fj256mc710 target.  When I place te CAN configuration block on a model it states "No CAN Peripheral on 33fj256MC710'", which doesn't seem to be correct.  Any ideas?</div>
</article>

<article class="forum-post" id="p1517">
<header><strong>ambersil</strong><time datetime="2011-03-24 21:53 UTC">2011-03-24 21:53 UTC</time></header>
<h3>Re: CAN block on 33fj256MC710 target</h3>
<div class="forum-post-body">Ah - I see that the blockset doesn't support ECAN - only CAN.<br>
<br>
<br>
<br>
Reading the forum it looks as if ECAN was on the roadmap back in 2008, but still hasn't made it into the blockset.</div>
</article>

<article class="forum-post" id="p1518">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-25 23:00 UTC">2011-03-25 23:00 UTC</time></header>
<h3>Re: CAN block on 33fj256MC710 target</h3>
<div class="forum-post-body">The slug team provide me with all the sources to do quickly the ECAN module. However, I still haven't done it yet, even if I started few month ago.<br>
<br>
Anyway, you might use ECAN peripheral using the C call function and the c sources code provided by the slug team (you should fine on the forum a git repository with theses sources, or a post from Bryant Mairs (bmairs) )<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1527">
<header><strong>ambersil</strong><time datetime="2011-03-30 22:45 UTC">2011-03-30 22:45 UTC</time></header>
<h3>Re: CAN block on 33fj256MC710 target</h3>
<div class="forum-post-body">Thanks for the pointer Lubin, I'm sure the SLUGS code will be a great help.</div>
</article>

<article class="forum-post" id="p1528">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-30 23:21 UTC">2011-03-30 23:21 UTC</time></header>
<h3>Re: CAN block on 33fj256MC710 target</h3>
<div class="forum-post-body">See post <a href="/forum/topic/371/#p1525">http://archive.kerhuel.eu/forum/viewtopic.p ... 1525#p1525</a> for link to a git repository with ECAN projects from Bryant Mairs.</div>
</article>

