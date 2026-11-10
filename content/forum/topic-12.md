---
title: "Any Plans to Open Source the Blockset?"
url: "/forum/topic/12/"
archiveKind: "topic"
---
# Any Plans to Open Source the Blockset?

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p14">
<header><strong>malife</strong><time datetime="2007-04-17 06:27 UTC">2007-04-17 06:27 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
The blockset seems really complete and it seems quite amazing what can do, I can only imagine how long it should have taken you to develop this. I was wondering if you have any plans to make the code available so one could code improvements and propose them.<br>
<br>
<br>
<br>
One road for instance would be to develop blocks for the libraries (soft modem, encription, etc..).<br>
<br>
<br>
<br>
I would totally understand if you answer is No, because I guess you want to keep tight control of what and how things get included in the code, but I think the blockset could grow faster if some of the interested are allowed to code Smile<br>
<br>
<br>
<br>
Anyways, Cheers and congrats on the work !<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p17">
<header><strong>LubinKerhuel</strong><time datetime="2007-04-17 21:52 UTC">2007-04-17 21:52 UTC</time></header>
<div class="forum-post-body">Thanks Mariano for your encouraging messages,<br>
<br>
<br>
<br>
Right now, I am not considering open source. <br>
<br>
<br>
<br>
I am just planning to have the low level hardware of dsPIC (30f, 24 and 33) working with user friendly blockset interface. Someone who do not know dsPIC microcontroller should be able to get the peripheral needed for its project working in less that 3 minutes. Then, to develop its project easily with simulink (typically, using the simulink model used for simulation with only small modification)<br>
<br>
<br>
<br>
With the Simulink interface and the Embedded Coder, algorithm achievement (encryption, soft modem or whatever) should be easy, efficient and fast. Algorithms obtained using simulink are easier to improve and to maintain up to date than C language algorithm.<br>
<br>
Is there any constraint to develop theses algorithm in hand written C ?<br>
<br>
<br>
<br>
You could however easily develop a simulink library containing blockset with theses high level algorithms.<br>
<br>
<br>
<br>
Lubin</div>
</article>

