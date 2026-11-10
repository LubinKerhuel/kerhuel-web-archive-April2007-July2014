---
title: "Creating sinusoidal PWM"
url: "/forum/topic/123/"
archiveKind: "topic"
---
# Creating sinusoidal PWM

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p368">
<header><strong>wam</strong><time datetime="2008-05-18 11:51 UTC">2008-05-18 11:51 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I am kind of new about programming dsPIC and I have limited time to finish my project and I decided to use simulink. I need to generate sinusoidal PWM by comparing sinusoidal reference with triangular waveform and obtain the output from PWM1L pin of the dsPIC30f4011. Can you help me about this?  :?: My PWM frequency will be 4 kHz.</div>
</article>

<article class="forum-post" id="p372">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-19 17:30 UTC">2008-05-19 17:30 UTC</time></header>
<h3>Re: Creating sinusoidal PWM</h3>
<div class="forum-post-body">Hi Wam,<br>
<br>
<br>
<br>
The project seems quite small and could do it with the demo version of the blockset.<br>
<br>
I do not get the meaning of :<br>
<blockquote><header class="quote-author">Citation : wam</header>triangular waveform and obtain the output from PWM1L</blockquote><br>
<br>
You 'd rather start your project and post question about the model you create if you are in trouble.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p373">
<header><strong>wam</strong><time datetime="2008-05-20 04:26 UTC">2008-05-20 04:26 UTC</time></header>
<h3>Re: Creating sinusoidal PWM</h3>
<div class="forum-post-body">Hi LubinKerhuel,<br>
<br>
<br>
<br>
Thanks for the reply. I will use normal sinusoidal PWM scheme. As you know if you want to do that you can feed comparator with sinusoidal and triangular waveform. PWM1L is the pin in dsPIC30F4011 and I want to get the PWM output from that pin.</div>
</article>

<article class="forum-post" id="p397">
<header><strong>wam</strong><time datetime="2008-05-28 02:58 UTC">2008-05-28 02:58 UTC</time></header>
<h3>Re: Creating sinusoidal PWM</h3>
<div class="forum-post-body">Can I get output from motor control PWM pin outputs such as PWM1L. I have to use this because I built my PCB to get PWM output signals from dsPIC. However I am not using motor control modules. I mean instead of getting signal from "OC1" pin, can I get exactly same signal from PWM1L (dsPIC30F4011) pin using your blocks?<br>
<br>
Thank you very much...</div>
</article>

<article class="forum-post" id="p398">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-28 07:09 UTC">2008-05-28 07:09 UTC</time></header>
<h3>Re: Creating sinusoidal PWM</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : wam</header>can I get exactly same signal from PWM1L</blockquote><br>
<br>
Yes,<br>
<br>
However, one difference between PWM motor and OC (Output Compare) block is that the PWM signal period cannot be changed during execution (with the PWM block). Since your period is fixed (Frequency set to 4Khz), It is OK.</div>
</article>

