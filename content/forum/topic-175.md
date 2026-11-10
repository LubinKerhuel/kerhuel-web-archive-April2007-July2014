---
title: "Speed and current control"
url: "/forum/topic/175/"
archiveKind: "topic"
---
# Speed and current control

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p610">
<header><strong>musa</strong><time datetime="2008-11-13 12:52 UTC">2008-11-13 12:52 UTC</time></header>
<div class="forum-post-body">Lubin, I want to control the speed and current on the dc motor. I'm using PI controller for both current and speed control, but the controller generates the constant duty cycle. please help me I dont know what is the problem</div>
</article>

<article class="forum-post" id="p611">
<header><strong>LubinKerhuel</strong><time datetime="2008-11-14 00:38 UTC">2008-11-14 00:38 UTC</time></header>
<h3>Re: Speed and current control</h3>
<div class="forum-post-body">Hi Musa,WeI have not element to help you. Provide more details ! (electronic, control scheme...)<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p647">
<header><strong>gdiana</strong><time datetime="2008-12-22 14:52 UTC">2008-12-22 14:52 UTC</time></header>
<h3>Re: Speed and current control</h3>
<div class="forum-post-body">Hi Musa and Lubin,<br>
<br>
<br>
<br>
I have done this sucessfully using Lubin's demo software. See the attached Simulink model.<br>
<br>
<br>
<br>
<br>
You must adjust Speed, Current and DC Voltage for your system. The controller gains will depend upon your motor size and machine parameters (Ra,La,Kt,Km,J and B).<br>
<br>
<br>
<br>
Start with current loop first. Positive voltage must give positive current and positive speed.<br>
<br>
<br>
<br>
I have inlcuded some info in the model. The controller may be used as is in the Simulink simulation. The PI controllers have anti-windup. <br>
<br>
<br>
<br>
It would be better to use synchronous sampling, to avoid switching noise in the feedback signals using the PWM block, but this feature is not yet available in Lubin's blockset.<br>
<br>
<br>
<br>
Cheers<br>
<br>
<br>
<br>
<br>
<br>
Greg Diana</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/168-DEMOIO.mdl">Pièce jointe : DEMOIO.mdl</a></p>
</article>

<article class="forum-post" id="p648">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-23 12:55 UTC">2008-12-23 12:55 UTC</time></header>
<h3>Re: Speed and current control</h3>
<div class="forum-post-body">Hi Greg,<br>
<br>
<br>
<br>
Thanks for posting this demo and for making it nice and clear... Would you like to add a short page about this demo in the <a href="/wiki/simulink-embedded-target-for-pic/">Example Category</a> of the website? It would be great to have few more details about the motor used, its simulink model, and few curves of the closed loop response... or whatever you want... Musa could also contribute if he would like too...<br>
<br>
Let me know (You may not have the right to create a new page on this wiki ; I will just create it and let you write...)<br>
<br>
<br>
<br>
Few technical points about the simulink model you posted: <br>
<br>
* Sampling time for all blocks is 10Khz except for delay blocks (1/z) which are at 5Khz. (It is very useful to use sample time colour : <strong>Format ==&gt; SampleTimeDisplay </strong><br>
<br>
* 10Khz is very fast for the calculation to be done using single. You may check using the <a href="/wiki/simulink-embedded-target-for-pic/">Calculus Time Step</a>  block that calculation are done within the 100us. This block will provide you with the calculation time. It's interesting also to get the free time you may have for others tasks... (You could get the numerical value of the Calculus Time Step block directly with the UART or with another PWM output)<br>
<br>
<br>
<br>
More general question about the control scheme:<br>
<br>
It seems that this motor is a big one (from the several amperes current you provide). I guess thus that its dynamics may be quite slow. Coupled with the very fast time step of 100us, I suspect the PWM output to be in fact use as an on/off signal (always saturate to PWMmax or to 0). i.e. it could be interesting to see if it this control scheme works when replacing the PWM output with a threshold followed by a binary Output PIN (Sliding mode).<br>
<br>
<br>
<br>
On a similar subject, a sensorless controller for a tiny motor using Simulink with dsPIC is described in this article:  <a href="http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=4602072">http://ieeexplore.ieee.org/xpl/freeabs_ ... er=4602072</a><br>
<br>
<br>
<br>
Lubin</div>
</article>

