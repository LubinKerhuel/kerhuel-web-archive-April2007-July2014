---
title: "PWM output"
url: "/forum/topic/129/"
archiveKind: "topic"
---
# PWM output

Forum : [General Remark and Questions](/forum/#forum-1)

8 message(s) · archive en lecture seule

<article class="forum-post" id="p391">
<header><strong>Anonyme</strong><time datetime="2008-05-26 18:52 UTC">2008-05-26 18:52 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I'm working in a small project for my university. I'm trying to generate the code for the 30f2010. I'm in a preliminary process. I try to use the PWM exit control a chopper, with the duty cicle and period as variables.<br>
<br>
<br>
<br>
I've tried with the OC compare block, and also with the PWM motor output block, but i don't success. Can you help me? I've read all the forum and seen all the examples, but I'm blocked at this position.<br>
<br>
<br>
<br>
At this moment I can't do a print screen, I hope tomorrow I could do.<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p392">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-27 07:10 UTC">2008-05-27 07:10 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">Hi Defe,<br>
<br>
<br>
<br>
Could you upload your Simulink model file  ? or a screenshoot as you like...</div>
</article>

<article class="forum-post" id="p393">
<header><strong>Anonyme</strong><time datetime="2008-05-27 13:01 UTC">2008-05-27 13:01 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
here's a pic of the model. Ocmax is the period and Ocmax/3 is the duty cycle. Is anything wrong? <br>
<br>
<br>
<br>
The PWM output has only one input. Can I use this block and how?<br>
<br>
<br>
<br>
My objetive is have a PWM output which variables are the duty cycle and period.<br>
<br>
<br>
<br>
Thanks</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/87-model.jpg">Pièce jointe : model.jpg</a></p>
</article>

<article class="forum-post" id="p396">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-27 20:03 UTC">2008-05-27 20:03 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">Hi Defe,<br>
<br>
<br>
<br>
This model should work. You should get a duty cycle of 1/3. If it doesn't, try forcing the sampling rate of the constant to .001 for example.<br>
<br>
<br>
<br>
Using the OC block, you will be able to get a PWM signal with variable duty cycle and period. You just have to care about scaling theses two values with regards to OC?max.<br>
<br>
<br>
<br>
The PWM Motor block has only one entry for duty cycle. Thus, it is not possible to get a variable period with this block. The period is fixed in the dialog box parameters.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1133">
<header><strong>jmednick</strong><time datetime="2010-03-12 20:03 UTC">2010-03-12 20:03 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">So wait, you can't change the duty cycle of the PWM wave?<br>
<br>
<br>
<br>
EDIT:  Never mind, I need to learn to read</div>
</article>

<article class="forum-post" id="p1134">
<header><strong>jmednick</strong><time datetime="2010-03-12 20:14 UTC">2010-03-12 20:14 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">What I am asking is how can I change the duty cycle in the PWM block?</div>
</article>

<article class="forum-post" id="p1135">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-12 21:53 UTC">2010-03-12 21:53 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">On OC block, duty cycle is set for example throw the OCx_Up. Period is set throw period. But theses input can be change into OCx_Up and OCx_Down in the dialog box.</div>
</article>

<article class="forum-post" id="p1219">
<header><strong>skumar</strong><time datetime="2010-05-04 07:25 UTC">2010-05-04 07:25 UTC</time></header>
<h3>Re: PWM output</h3>
<div class="forum-post-body">hie sir..<br>
<br>
<br>
<br>
i am a undergraduate student.. i am doing a project where i want to control the output voltage of the BOOST converter.. <br>
<br>
the controller i am using is PI control.. i am giving the error voltage to the PI controller.. this controller will give a signal and i am comparing that signal with a ramp wave which which give the pulse to switch on the MOSFET... i tested that circuit in matlab simulink and it is  working also..but for implemeting that with DSPIC toolbox what i have to change..<br>
<br>
i am very new to this microcontroller....i tried for many days but i am unable to move furture..<br>
<br>
<br>
<br>
waiting for u r reply..</div>
</article>

