---
title: "delay between PWM"
url: "/forum/topic/364/"
archiveKind: "topic"
---
# delay between PWM

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1484">
<header><strong>ELMAY</strong><time datetime="2011-02-25 09:59 UTC">2011-02-25 09:59 UTC</time></header>
<div class="forum-post-body">hi sir<br>
<br>
<br>
<br>
I made this model to generate 3 PWM I compile without errors<br>
<br>
 <br>
<br>
This now I ask the following:<br>
<br>
<br>
<br>
how can there be a delay between these 3 signals?<br>
<br>
<br>
<br>
ELMAY</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/390-commande_IGBT.mdl">Pièce jointe : commande_IGBT.mdl</a></p>
</article>

<article class="forum-post" id="p1486">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-26 19:49 UTC">2011-02-26 19:49 UTC</time></header>
<h3>Re: delay between PWM</h3>
<div class="forum-post-body">Here is your model: <blockquote><header class="quote-author">Citation : ELMAY</header><br>
how can there be a delay between these 3 signals?</blockquote>I do not think there is a robust way to do it.<br>
<br>
Anyway, you may try the <a href="/wiki/dspic-block-output-compare-hw/">Output Compare Hardware (OC (HW))</a> (instead of the Output Compare (<a href="/wiki/dspic-block-output-compare/">OC</a>)) block which I used for <a href="/wiki/pic32-sensorless-speed-controller-for-dc-motor-applied-on-picooz-main-rotor/">picooz motor control</a> or this <a href="/wiki/hyper-sampling/">other example</a> .<br>
<br>
<br>
<br>
With <a href="/wiki/dspic-block-output-compare-hw/">OC (HW)</a> block, mode 16 makes you able to set for each channel the instant at which you want a rising edge and at which instant you want a falling edge. However, due to the way it works, a PWM duty cycle may be false for one period when you are modifying values.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/391-model.PNG">Pièce jointe : model.PNG</a></p>
</article>

