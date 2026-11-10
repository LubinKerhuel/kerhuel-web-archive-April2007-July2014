---
title: "dsPIC_PWM_motor.tlc problem"
url: "/forum/topic/498/"
archiveKind: "topic"
---
# dsPIC_PWM_motor.tlc problem

Forum : [bug reports](/forum/#forum-8)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p1893">
<header><strong>Ebap</strong><time datetime="2012-06-06 04:36 UTC">2012-06-06 04:36 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am trying to do a simple program with the dsPIC_PWM_motor block but when I try to generate the code from matlab, it give me this error ''The + operator only works on numeric arguments'' (In the dsPIC_PWM_motor.tlc) I attach the error file, the installation file and the .mdl.  <br>
<br>
<br>
<br>
Matlab 2011a<br>
<br>
C30 compiler V3.3<br>
<br>
Blockset V3.7c</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/510-error.txt">Pièce jointe : error.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/511-installation.txt">Pièce jointe : installation.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/512-baja.mdl">Pièce jointe : baja.mdl</a></p>
</article>

<article class="forum-post" id="p1895">
<header><strong>LubinKerhuel</strong><time datetime="2012-06-10 16:54 UTC">2012-06-10 16:54 UTC</time></header>
<h3>Re: dsPIC_PWM_motor.tlc problem</h3>
<div class="forum-post-body">Thanks for bug report,<br>
<br>
<br>
<br>
Will be fixed in next release.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1907">
<header><strong>welf</strong><time datetime="2012-08-16 20:43 UTC">2012-08-16 20:43 UTC</time></header>
<h3>Re: dsPIC_PWM_motor.tlc problem</h3>
<div class="forum-post-body">I am also affected by this problem. Any progress on a fix or suggestions for a workaround?<br>
<br>
<br>
<br>
Thanks<br>
<br>
<br>
<br>
EDIT: the error does not seem to appear when compiling for certain chips (e.g. 33FJ218MC or 33FJ256MC series), but does for the chip that I am using (33FJ32MC204)</div>
</article>

<article class="forum-post" id="p1908">
<header><strong>welf</strong><time datetime="2012-08-20 12:41 UTC">2012-08-20 12:41 UTC</time></header>
<h3>Re: dsPIC_PWM_motor.tlc problem</h3>
<div class="forum-post-body">Actually I am able to compile the resulting code in MPLAB and run it even though the build (in Matlab) aborts with an error!<br>
<br>
<br>
<br>
The MPLAB project is not created - but I can use a previous project file created without the PWM block in the system.<br>
<br>
The file "dsPIC_OutputCompare_Interrupt.c" is not found but it is replaced with an object file.</div>
</article>

<article class="forum-post" id="p1929">
<header><strong>welf</strong><time datetime="2012-09-17 16:28 UTC">2012-09-17 16:28 UTC</time></header>
<h3>Re: dsPIC_PWM_motor.tlc problem</h3>
<div class="forum-post-body">Fixed in new version!  :)</div>
</article>

<article class="forum-post" id="p1934">
<header><strong>LubinKerhuel</strong><time datetime="2012-09-18 16:05 UTC">2012-09-18 16:05 UTC</time></header>
<h3>Re: dsPIC_PWM_motor.tlc problem</h3>
<div class="forum-post-body">Ok, Thanks for your feedback,<br>
<br>
<br>
<br>
(As I am not very responsive at that time !)<br>
<br>
We're preparing a new blockset suporting newer chips at Microhcip...<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1975">
<header><strong>nasrullah</strong><time datetime="2013-01-01 08:47 UTC">2013-01-01 08:47 UTC</time></header>
<h3>PWM DC Motor</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am trying to do a simple program to active DC motor. But when I try to generate the code from matlab, it give me this error ''Error building Real-Time Workshop target for block diagram 'motor1'. MATLAB error message: Error(s) encountered while building model "motor1".I attach the motor1.mdl below. The motor driver frequency is 40Khz. Thanks.<br>
<br>
<br>
<br>
Matlab 2009a<br>
<br>
MPLAB IDE v8.88 compiler 32 V2.01<br>
<br>
Blockset V3.7e</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/515-motor1.mdl">Pièce jointe : motor1.mdl</a></p>
</article>

