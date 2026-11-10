---
title: "How to configure PLL and maintain correct time"
url: "/forum/topic/338/"
archiveKind: "topic"
---
# How to configure PLL and maintain correct time

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p1352">
<header><strong>coolj</strong><time datetime="2010-11-29 18:42 UTC">2010-11-29 18:42 UTC</time></header>
<div class="forum-post-body">Lubin - great blockset!<br>
<br>
<br>
<br>
I'm currently evaluating if this would work for my current application.<br>
<br>
<br>
<br>
I have the explorer 16 board with your example code up-and-running on it.<br>
<br>
<br>
<br>
However, I am trying to understand how to increase the MIPS of the dspic33fj256gp710 to the max 40 mips without affecting the base time step of the model.<br>
<br>
<br>
<br>
That is, I want to have the fastest processing speed, but maintain accurate real-time time steps.  When I increase the dspic master to 40 MIPS, it clearly affects the time step of the model (the LEDs blink much faster, for example).<br>
<br>
<br>
<br>
Can you help me understand how to increase the model to 40 MIPS and maintain the correct real-time time step?<br>
<br>
<br>
<br>
Much appreciated!<br>
<br>
Justin</div>
</article>

<article class="forum-post" id="p1356">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 20:03 UTC">2010-11-29 20:03 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : coolj</header>When I increase the dspic master to 40 MIPS, it clearly affects the time step of the model (the LEDs blink much faster, for example).</blockquote><br>
<br>
Are you increasing the speed using the MASTER block ?<br>
<br>
Time step should not be affected (make sure you recompile the model. Perhaps try to compile it twice ! (to make sure change are taken into account))<br>
<br>
<br>
<br>
Please report it that's not working ! (bug ?)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1357">
<header><strong>coolj</strong><time datetime="2010-11-29 20:30 UTC">2010-11-29 20:30 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">Thanks for the lightning-fast response, Lubin!<br>
<br>
<br>
<br>
Yes, I increased the speed using the master block "Activate PLL" with MIPS=40000000.  In fact, this is the only thing that I changed from the default example model for the explorer 16 board.  It appears that the time step followed that, as the LEDs look to be blinking approximately 10x faster than before.<br>
<br>
<br>
<br>
R2010b, blockset 3.3.<br>
<br>
<br>
<br>
I tried re-compiling it again as you stated, but it's clear that changes are being implemented as when I uncheck "Activate PLL", the MIPS go down to 4e6 (as expected), and the LEDs blink at the correct rate.<br>
<br>
<br>
<br>
I even tried compiling the project in MPLAB, with the same "fast time step" results.<br>
<br>
<br>
<br>
Is there anything else I should try?</div>
</article>

<article class="forum-post" id="p1358">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 21:47 UTC">2010-11-29 21:47 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">Are you using a bootloader ?<br>
<br>
Bootloader typically do not program config registers where PLL and others parameters are stored.<br>
<br>
<br>
<br>
Otherwise, Could you upload the modified model on the forum ? Something's wrong !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1360">
<header><strong>coolj</strong><time datetime="2010-11-30 06:12 UTC">2010-11-30 06:12 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">No bootloader being used.  I'm programming it directly from ICD3.<br>
<br>
<br>
<br>
I attached the model - it's exactly the same as the explorer 16 demo but with the PLL activated for 40 MIPS (based on the 8 MHz Explorer 16 xtal).</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/354-dsPIC_33f_Explorer16.mdl">Pièce jointe : dsPIC_33f_Explorer16.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/355-dsPIC_33f_Explorer16.hex">Pièce jointe : dsPIC_33f_Explorer16.hex</a></p>
</article>

<article class="forum-post" id="p1361">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 07:41 UTC">2010-11-30 07:41 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">Could you check that, in MPLAB, the configuration bits are also programmed (because there is a checkbox option in MPLAB that force the configuration options bits with the current GUI config...) <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1366">
<header><strong>coolj</strong><time datetime="2010-11-30 18:14 UTC">2010-11-30 18:14 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I believe I have the configuration bits set correctly in MPLAB to read from program code - I attached a screenshot for your verification.<br>
<br>
<br>
<br>
I also attached the exact window showing the updated MIPS / PLL setting.<br>
<br>
<br>
<br>
Justin<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/359-mplab_capture.png">Pièce jointe : mplab_capture.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/360-PLL_settings.png">Pièce jointe : PLL_settings.png</a></p>
</article>

<article class="forum-post" id="p1367">
<header><strong>coolj</strong><time datetime="2010-11-30 19:00 UTC">2010-11-30 19:00 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">RESOLVED.<br>
<br>
<br>
<br>
For some reason, a re-load of Matlab seemed to solve the problem...anyway, it's working great now!<br>
<br>
<br>
<br>
Thanks for your help, Lubin!<br>
<br>
<br>
<br>
Justin</div>
</article>

<article class="forum-post" id="p1369">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 22:31 UTC">2010-11-30 22:31 UTC</time></header>
<h3>Re: How to configure PLL and maintain correct time</h3>
<div class="forum-post-body">Thanks for illustrating what I was talking about the Configuration bits. The picture shows a correct configuration.<br>
<br>
<br>
<br>
Good to see the blockset working now. <br>
<br>
Provided you could reproduce the bug, I would be glad to get the how you did so as to correct that problem !<br>
<br>
<br>
<br>
Lubin</div>
</article>

