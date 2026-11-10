---
title: "Configure Model won't open"
url: "/forum/topic/95/"
archiveKind: "topic"
---
# Configure Model won't open

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p256">
<header><strong>Anonyme</strong><time datetime="2008-03-04 00:43 UTC">2008-03-04 00:43 UTC</time></header>
<div class="forum-post-body">I'm attempting to run one of the example simulink files (the Data_Login_Matlab one)<br>
<br>
I try to double click on "Configure Model for dsPIC Target" and nothing happens, when I try to manually change all the target info to 'dsPIC30F6010A' I still end up missing some.<br>
<br>
<br>
<br>
Any ideas?</div>
</article>

<article class="forum-post" id="p257">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-04 01:51 UTC">2008-03-04 01:51 UTC</time></header>
<h3>Re: Configure Model won&#x27;t open</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : rmiller</header>Configure Model for dsPIC Target</blockquote><br>
This configures some simulink parameters (fixed step solver etc...) but do not change the target.<br>
<br>
<br>
<br>
To change the target to 30f6010A, open the "<a href="/RTWdsPIC/Blocks/Master.html">dsPIC MASTER</a>" block.<br>
<br>
<img loading="lazy" src="/RTWdsPIC/Blocks/Img/Master.png" alt="Image du forum"><br>
<br>
You will find the list of the supported chips (exhaustive list can be found on the <a href="/RTWdsPIC/download.html">download</a> page).<br>
<br>
<br>
<br>
The dialog unexpectedly closed when the target is modified. You have to re-open it to modify others parameters (quartz use...)</div>
</article>

