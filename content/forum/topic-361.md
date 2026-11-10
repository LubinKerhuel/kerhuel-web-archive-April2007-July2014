---
title: "Improve duplicate ports warning"
url: "/forum/topic/361/"
archiveKind: "topic"
---
# Improve duplicate ports warning

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1474">
<header><strong>bmairs</strong><time datetime="2011-02-22 19:23 UTC">2011-02-22 19:23 UTC</time></header>
<div class="forum-post-body">When I'm compiling my model, I get the following:<br>
<pre><code>Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= --- 
&gt; In E:\Documents and Settings\Bryant Mairs\My Documents\MATLAB\blocks\dsPIC_PortSetting.p&gt;setTypePort at 525
  In E:\Documents and Settings\Bryant Mairs\My Documents\MATLAB\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 349
  In E:\Documents and Settings\Bryant Mairs\My Documents\MATLAB\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196</code></pre><br>
<br>
I get this error 5 separate times, yet I can't find in my model where this port is used multiple times. This warning and compilation both don't give me any hint as to what's causing this conflict either. Would it be possible to improve these warning so that they say what block was being evaluated when the duplicate port use was found? It would also be nice is during compilation a list of all used ports and which ones they were could be output instead of just how many pins are used.</div>
</article>

<article class="forum-post" id="p1475">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-22 22:44 UTC">2011-02-22 22:44 UTC</time></header>
<h3>Re: Improve duplicate ports warning</h3>
<div class="forum-post-body">Hi Bryan,<br>
<br>
<br>
<br>
Thanks for looking closely at the generated warning. Few guys does it I guess. <br>
<br>
I will try to take into account your remarks about telling which peripheral use which port. There might be necessary to do few internal changes to do so. The best would then be to create a sketch diagram of the dsPIC with used ports with corresponding peripheral; however that's a piece of work to do... I might think to do it in txt form...<br>
<br>
<br>
<br>
About your PORT A0. Does the Master block use A0 for a busy flag or an overflow flag?<br>
<br>
Feel free to update your model so as I try to find also! It may be a blockset bug also!<br>
<br>
<br>
<br>
I've been working recently on CAN peripheral as you may see on the wiki <a href="/wiki/can-communication-between-two-dspic/">example page</a>  (first draft). I'll then work on the ECAN You provide me. I am still very late in that project. <br>
<br>
<br>
<br>
Thanks for your suggestions.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1491">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-01 22:44 UTC">2011-03-01 22:44 UTC</time></header>
<h3>Re: Improve duplicate ports warning</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : bmairs</header>Would it be possible to improve these warning so that they say what block was being evaluated when the duplicate port use was found? It would also be nice is during compilation a list of all used ports and which ones they were could be output instead of just how many pins are used</blockquote><br>
All is done in version 3.4c.<br>
<br>
The new block <a href="/wiki/dspic-block-ports-info/">Ports Info</a> provide information about pin used.<br>
<br>
<br>
<br>
I hope these changes will fulfill  your needs.<br>
<br>
<br>
<br>
Lubin</div>
</article>

