---
title: "CAN num in &quot;CAN receive&quot; block"
url: "/forum/topic/219/"
archiveKind: "topic"
---
# CAN num in &quot;CAN receive&quot; block

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p830">
<header><strong>Toro480</strong><time datetime="2009-04-20 18:02 UTC">2009-04-20 18:02 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
in my project I use CAN BUS between 2 dsPIC. The 2 boards are already built with connection on CAN2.<br>
<br>
But when I add a "CAN Receiver block" I can't choice number 2 (only num CAN 1). Is it a bug?<br>
<br>
<br>
<br>
PS : if someone have an example of model which works with CAN blocks, will be possible to share it?<br>
<br>
Thanks for your answers.<br>
<br>
<br>
<br>
Best regards,<br>
<br>
Florent</div>
</article>

<article class="forum-post" id="p831">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-20 22:38 UTC">2009-04-20 22:38 UTC</time></header>
<h3>Re: CAN num in &amp;quot;CAN receive&amp;quot; block</h3>
<div class="forum-post-body">Hello Florent,<br>
<br>
<br>
<br>
I worked on CAN more than one year ago.  (Not ECAN yet !)<br>
<br>
I find the two models I used to develop the CAN blocks. These models were working last year. It was very funny to see on the oscilloscope two CAN trame sent by each dsPIC to cross over. When you see it, you'll find that CAN is a smart system.<br>
<br>
I was wondering to publish a nice example, but I didn't find time for it. I was also wondering to mix an ECAN peripheral with a CAN peripheral. Anyway, If anybody is motivated to publish a nice CAN system on the wiki, it's open !<br>
<br>
<br>
<br>
I hope theses model will help to see how it works. I have not been using CAN since then. I am not sure I could provide lots of information.<br>
<br>
<br>
<br>
Please let me know which dsPIC you are using. There may be an error that makes only the CAN 1 available.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/234-CAN.zip">Pièce jointe : CAN.zip</a></p>
</article>

<article class="forum-post" id="p833">
<header><strong>Toro480</strong><time datetime="2009-04-21 09:44 UTC">2009-04-21 09:44 UTC</time></header>
<h3>Re: CAN num in &amp;quot;CAN receive&amp;quot; block</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
thanks for your answer. I will study these models.<br>
<br>
I use two dsPIC30F6014A. I want to create CAN communication between the two dsPIC.<br>
<br>
The num 1 is not available in CAN Receiver block.<br>
<br>
<br>
<br>
Florent</div>
</article>

