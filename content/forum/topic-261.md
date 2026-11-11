---
title: "pwm 2+2"
url: "/forum/topic/261/"
archiveKind: "topic"
---
# pwm 2+2

Forum : [dsPIC Peripherals](/forum/#forum-9)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1018">
<header><strong>Bobes</strong><time datetime="2009-12-28 21:36 UTC">2009-12-28 21:36 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
this is more of a PIC specialist question:<br>
<br>
I am using dsPIC33fj128mc802, and I need to generate 4 PWM signals:<br>
<br>
to drive 2 DC brushed motors (same frequency around 10 kHz but independent duty cycle)<br>
<br>
and 2 "modeller" servos (same frequency 50Hz but independent duty cycle)<br>
<br>
<br>
<br>
my question is: is it possible to generate 2 PWM on one PWM module each with different frequency?<br>
<br>
I have tried it out, but I have got error from the compiler (I do not have my DevKit with me right now, so HW testing is not possible at the moment).<br>
<br>
<br>
<br>
Please excuse me, I am quite a beginner...<br>
<br>
I will appreciate any help and/or advices<br>
<br>
Thanks<br>
<br>
Kind regards<br>
<br>
Josef<br>
<br>
<br>
<br>
UPDATE: I have tried removing second servo PWM (removed PWM2_motor block) and it was compiled without an error (having on PWM1_motor block 3 channels with 2 different frequencies) On one hand this may mean that it can be done, but on the other: I am more confused: why it does not work?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/283-Vejlupek_CAR4_dsPIC33_AxleControl.mdl">Pièce jointe : Vejlupek_CAR4_dsPIC33_AxleControl.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/285-Vejlupek_CAR4_dsPIC33_AxleControl_bckup_R091228_R02.mdl">Pièce jointe : Vejlupek_CAR4_dsPIC33_AxleControl_bckup_R091228_R02.mdl</a></p>
</article>

<article class="forum-post" id="p1030">
<header><strong>Bobes</strong><time datetime="2010-01-19 11:37 UTC">2010-01-19 11:37 UTC</time></header>
<h3>Re: pwm 2+2</h3>
<div class="forum-post-body">update: it is not possible to run one PWM module with two different frequencies.  :(</div>
</article>

<article class="forum-post" id="p1031">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-19 12:12 UTC">2010-01-19 12:12 UTC</time></header>
<h3>Re: pwm 2+2</h3>
<div class="forum-post-body">Hi Josef,<br>
<br>
<br>
<br>
It may not be possible to get two different PWM period from one "PWM motor" peripheral. However, you may use an Output Compare block that is capable to generate PWM signals with different periods.<br>
<br>
<br>
<br>
I just updated the PWM  help page <a href="/wiki/dspic-block-pwm-motor-output/">http://archive.kerhuel.eu/wiki/Block/PWM_Mo ... ut#Periode</a><br>
<br>
Please feel free to complete wiki help page for others usefull informations.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1032">
<header><strong>Bobes</strong><time datetime="2010-01-19 12:31 UTC">2010-01-19 12:31 UTC</time></header>
<h3>Re: pwm 2+2</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
yes... I have reached this conclusion as well.<br>
<br>
<br>
<br>
However I have now something else: I was trying to set the period externally, but I was asked for uint16. Is this correct?<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p1034">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-19 12:59 UTC">2010-01-19 12:59 UTC</time></header>
<h3>Re: pwm 2+2</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Bobes</header><br>
However I have now something else: I was trying to set the period externally, but I was asked for uint16. Is this correct?</blockquote><br>
Yes, That is correct.<br>
<br>
Input value must be :<br>
<br>
 <br>
<br>
requestedTime (in s) *  { PWMmax (variable defined in the workspace) / Periode set in the block (in s) }<br>
<br>
<br>
<br>
You'll get a large value that you may round off. See the many example for more details.<br>
<br>
<br>
<br>
Lubin</div>
</article>

