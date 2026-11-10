---
title: "Required Matlab components"
url: "/forum/topic/438/"
archiveKind: "topic"
---
# Required Matlab components

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1684">
<header><strong>resodad</strong><time datetime="2011-09-08 20:25 UTC">2011-09-08 20:25 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Can you please state what components / toolboxes are required to use the blockset?<br>
<br>
e.g. Matlab, Simulink, Simulink Coder (formerly Real Time Workshop), and Embedded Coder...<br>
<br>
did I miss anything?<br>
<br>
Thanks,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1686">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-09 07:18 UTC">2011-09-09 07:18 UTC</time></header>
<h3>Re: Required Matlab components</h3>
<div class="forum-post-body">You listed the minimum required toolboxes. EC (Embeddede Coder) is the most important !<br>
<br>
<br>
<br>
for designing efficient embedded system, the fixed point toolboxes is very useful. <br>
<br>
Stateflow might also be usefull if you are to design FSM.<br>
<br>
<br>
<br>
Then all matlab toolboxes related to your topic (system identification, control toolbox, optimisation...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1717">
<header><strong>resodad</strong><time datetime="2011-10-04 16:43 UTC">2011-10-04 16:43 UTC</time></header>
<h3>Re: Required Matlab components</h3>
<div class="forum-post-body">I see that Matlab coder is required to run embedded coder.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1721">
<header><strong>LubinKerhuel</strong><time datetime="2011-10-07 23:05 UTC">2011-10-07 23:05 UTC</time></header>
<h3>Re: Required Matlab components</h3>
<div class="forum-post-body">Thus EC works on top of Matlab Coder ?<br>
<br>
<br>
<br>
Thanks Mathworks ;-)<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1819">
<header><strong>bmairs</strong><time datetime="2012-01-24 00:03 UTC">2012-01-24 00:03 UTC</time></header>
<h3>Re: Required Matlab components</h3>
<div class="forum-post-body">This kind of explains it: <a href="http://blogs.mathworks.com/seth/2011/04/08/welcome-to-the-coders/">http://blogs.mathworks.com/seth/2011/04 ... he-coders/</a>. But when installing I was required to add Matlab Coder in addition to these like resodad mentioned. Looks like the base requirements are: Matlab, Simulink, Simulink Coder, Embedded Coder, and Matlab Coder.</div>
</article>

