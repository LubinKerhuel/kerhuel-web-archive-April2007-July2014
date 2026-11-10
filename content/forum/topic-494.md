---
title: "Error in SPWM Motor PWM Output"
url: "/forum/topic/494/"
archiveKind: "topic"
---
# Error in SPWM Motor PWM Output

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1876">
<header><strong>kanchibhotla14</strong><time datetime="2012-04-09 17:40 UTC">2012-04-09 17:40 UTC</time></header>
<div class="forum-post-body">Hello Sir,<br>
<br>
I want to generate the SPWM and simple PWM to GPIOs ... SPWM of fundamental frequency 50Hz and Switching frequency 5kHz .....but when we build and run the program i am getting the switching frequency is of around 63Hz and fundamental frequency 2Hz ....simple PWM is of least frequency...<br>
<br>
Ts = 2e-6 and Fixed step size is of 2e-6 (in solver) and MIPS 20e6 (in master).....even the fixed step size (in solver) is every time is resetting to 0.01..... I am attaching the simulation file...can you check and please tell me how to get the my required pwm frequency and spwm....even i tried with rate transition box but no use...</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/507-PWM.mdl">Pièce jointe : PWM.mdl</a></p>
</article>

<article class="forum-post" id="p1879">
<header><strong>LubinKerhuel</strong><time datetime="2012-04-27 00:13 UTC">2012-04-27 00:13 UTC</time></header>
<h3>Re: Error in SPWM Motor PWM Output</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
You will not generate a PWM efficiently using digital output blocks.<br>
<br>
Use the PWM like block, or Output Compare block.<br>
<br>
<br>
<br>
You might find some examples on the website or within blockset example folder.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1984">
<header><strong>pakerjon</strong><time datetime="2013-02-21 05:59 UTC">2013-02-21 05:59 UTC</time></header>
<h3>Re: Error in SPWM Motor PWM Output</h3>
<div class="forum-post-body">Thanks <strong>LubinKerhuel</strong> for giving the correction &amp; new idea...<br>
<br>
<br>
<br>
 :)  8)</div>
</article>

<article class="forum-post" id="p3476">
<header><strong>Casper</strong><time datetime="2013-12-09 11:25 UTC">2013-12-09 11:25 UTC</time></header>
<h3>Re: Error in SPWM Motor PWM Output</h3>
<div class="forum-post-body">Thanks for making me understand about the exact issue. I was not aware about not to generate a PWM efficiently using digital output blocks. I usually use the PWM for the output blocks. Now on wards I will make use of the Output Compare block. <br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
--------------------------------<br>
<br>
Ellery<br>
<br>
<a href="http://www.windowsonlinesupportnow.com">Windows online support now</a></div>
</article>

