---
title: "100% beginners"
url: "/forum/topic/113/"
archiveKind: "topic"
---
# 100% beginners

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p319">
<header><strong>Anonyme</strong><time datetime="2008-04-29 18:18 UTC">2008-04-29 18:18 UTC</time></header>
<div class="forum-post-body">Where do I find examples for total beginners?</div>
</article>

<article class="forum-post" id="p325">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-05 22:37 UTC">2008-05-05 22:37 UTC</time></header>
<h3>Re: 100% beginners</h3>
<div class="forum-post-body">- On the website : <a href="/archive-assets/">http://archive.kerhuel.eu/RTWdsPIC</a><br>
<br>
- The blockset contains few examples.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1068">
<header><strong>listedunlisted</strong><time datetime="2010-02-02 23:46 UTC">2010-02-02 23:46 UTC</time></header>
<h3>Re: 100% beginners</h3>
<div class="forum-post-body">This is my first quote. So please go easy on me. I really need your help fellows.<br>
<br>
<br>
<br>
I just found out about the thing where Simulink can be used to download the code on the PIC microcontroller without using C or any programming language.<br>
<br>
<br>
<br>
Now, I have Matlab R2007B. First of all my main question is can someone please explain in simple steps how to download a Simulink blockset on the Micro Controller and what wires and software is required to do so. I saw the videos on your website. I have downloaded the Install_dsPIC_R2007b for my Matlab. But this is a script file. How do I move forward about downloading the file for Simulink. I really need help with this. I have a project coming up in a few weeks and I need to start working on it.<br>
<br>
<br>
<br>
Can anyone please explain simple steps in using Simulink with PIC microcontroller and what do I need?</div>
</article>

<article class="forum-post" id="p1070">
<header><strong>Bobes</strong><time datetime="2010-02-03 13:40 UTC">2010-02-03 13:40 UTC</time></header>
<h3>Re: 100% beginners</h3>
<div class="forum-post-body">1/ install the block-set (put it in some DIR like C:/Program Files/Matlab/Addons/Kerhuel toolbox - do not install it under Matlab/toolbox!) - In simulink you should see the block-set as Embedded Target for microchip (or something like that)<br>
<br>
2/ create project - or better start with some example, you have to configure simulink for your target (PIC), there are blocks for this.<br>
<br>
3/ when it is ready, click on "Incremental build" its next to run button. - this if everything is OK will create hex file<br>
<br>
4/ you need some tool to upload HEX file, there are many tools to do that, ie ICD 2, ICD 3 from Microchip, but there are many cheaper ways. use google for that.</div>
</article>

<article class="forum-post" id="p1085">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-11 17:26 UTC">2010-02-11 17:26 UTC</time></header>
<h3>Re: 100% beginners</h3>
<div class="forum-post-body">Hello<br>
<blockquote><header class="quote-author">Citation : listedunlisted</header>I have downloaded the Install_dsPIC_R2007b for my Matlab. But this is a script file. How do I move forward</blockquote><br>
* open matlab<br>
<br>
* run the script file : eigher you type its name, or you right click on the script file and click "run"<br>
<br>
This will install the blockset... at that place !<br>
<br>
<br>
<br>
I guess bobes provide the way to go forward.<br>
<br>
<br>
<br>
Lubin</div>
</article>

