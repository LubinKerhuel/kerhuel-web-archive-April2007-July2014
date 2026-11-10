---
title: "frequency mismatching"
url: "/forum/topic/256/"
archiveKind: "topic"
---
# frequency mismatching

Forum : [dsPIC Peripherals](/forum/#forum-9)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1006">
<header><strong>Deepthi</strong><time datetime="2009-11-27 03:41 UTC">2009-11-27 03:41 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
           Your blockset is amazing and i am using the trial version of Matlab_09a .My problem is that i am not getting the frequency of square pulse correctly once i download the hex file to dsPIC.The frequency in the model is correct,problem is with the hardware.I am using dsPIC30f3011.I am using a 20mHz crystal oscillator as clock.What can be the problem?<br>
<br>
<br>
<br>
Thank you<br>
<br>
<br>
<br>
Deepthi.</div>
</article>

<article class="forum-post" id="p1007">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-27 09:24 UTC">2009-11-27 09:24 UTC</time></header>
<h3>Re: frequency mismatching</h3>
<div class="forum-post-body">Hi Deepthi,<br>
<br>
<br>
<br>
Please upload the model you made (adding screenshoot is even better). this will help to identify the problem.<br>
<br>
<br>
<br>
On 30f chip, the real MIPS is the frequency of the quartz <strong>divided by 4</strong>, and then multiplied with the choosen PLL (1 if no PLL) . See help <a href="/wiki/dspic-block-master/">http://www.kerhuel.eu/wiki/Block/Master</a><br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1008">
<header><strong>Deepthi</strong><time datetime="2009-12-09 16:12 UTC">2009-12-09 16:12 UTC</time></header>
<h3>Re: frequency mismatching</h3>
<div class="forum-post-body">Hi Lubin<br>
<br>
<br>
<br>
         Sorry for the late reply.Actually i tried with correct MIPS,but i am still having the same problem.I am attaching the model with this post.Please help me out!<br>
<br>
<br>
<br>
Deepthi</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/281-square4.mdl">Pièce jointe : square4.mdl</a></p>
</article>

<article class="forum-post" id="p1009">
<header><strong>LubinKerhuel</strong><time datetime="2009-12-09 17:03 UTC">2009-12-09 17:03 UTC</time></header>
<h3>Re: frequency mismatching</h3>
<div class="forum-post-body">Hi Deepthi,<br>
<br>
<br>
<br>
Do you get a slower frequency ? could you describe, what are you seeing on your scope ?<br>
<br>
<br>
<br>
I do not see obvious errors on the model configuration<br>
<br>
<strong>BUT</strong><br>
<br>
you selected a time step of 0.00001 which is 100Khz. That's very fast and perhaps the dspic cannot execute the mode that fast ! It may append that each time step will takes about 15us instead of 10us.<br>
<br>
You can check if real time constraint with the <strong>busy flag port</strong> and the <strong>overload flag port</strong> in the master block. You could also have more precision using the <strong> <a href="/wiki/dspic-block-calculus-time-step/">Time Step block</a></strong> <br>
<br>
<br>
<br>
To correct the problem quickly, 3 solutions : <br>
<br>
- <strong>reduce the time step of your model</strong> (use for example .001 for 1Khz)<br>
<br>
- increase the dsPIC <strong>MIPS </strong>with a pll <br>
<br>
- generate a PWM pulse using <strong>Output Compare</strong> of <strong>PWM motor block</strong> (if available on this dsPIC) (however, with this solution, you should check anyway that real time constraints are OK otherwise your algorithm'll will not be correct : for example filter frequency cut will not be the one expected...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1010">
<header><strong>Deepthi</strong><time datetime="2009-12-10 03:25 UTC">2009-12-10 03:25 UTC</time></header>
<h3>Re: frequency mismatching</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
               Thanks for the reply.I will try out as you said and reply to you as soon as possible.But when i tried to make the fixed step size as 1ms.Its showing the error that the "period must be an integer multiple of the fixed step size".What can be the reson for this??<br>
<br>
<br>
<br>
Deepthi</div>
</article>

<article class="forum-post" id="p1011">
<header><strong>LubinKerhuel</strong><time datetime="2009-12-10 08:42 UTC">2009-12-10 08:42 UTC</time></header>
<h3>Re: frequency mismatching</h3>
<div class="forum-post-body">This error means that a block is configured to run with a sampling rate that is either faster, or not an integer multiple of the the model sampling rage.<br>
<br>
<br>
<br>
In your model, the block Convert is defined with a sampling rate of 0.0001s. I would advise to set this block to -1 to get it working at the same sampling rate as the Pulse Generator connected to it.<br>
<br>
<br>
<br>
This "wrong" sampling rate could also be the cause of the bad result you get when the model was configured with a sampling rate of 0.00001s.<br>
<br>
Please have a look on model time-step and sampling rate topics in simulink help page, you will find many usefull information here that should be better than any of my explanations... <br>
<br>
<br>
<br>
Lubin</div>
</article>

