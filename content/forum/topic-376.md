---
title: "Support for dsPIC33xxGSxx series"
url: "/forum/topic/376/"
archiveKind: "topic"
---
# Support for dsPIC33xxGSxx series

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1524">
<header><strong>Andrew</strong><time datetime="2011-03-29 18:16 UTC">2011-03-29 18:16 UTC</time></header>
<div class="forum-post-body">Hi ,<br>
<br>
<br>
<br>
I saw the supporting list of chip, but didn't see the dsPIC33xxGSxx series. Will it be supported in the future? I have to use<br>
<br>
it in my project because it has an important feature that the phase shift between differenct PWM channels is adjustable. This <br>
<br>
feature is vital is phase-shift-dc-converter and some kind of pwm modulation in BLDC. I really hope it will be supported. Thanks!</div>
</article>

<article class="forum-post" id="p1526">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-30 21:25 UTC">2011-03-30 21:25 UTC</time></header>
<h3>Re: Support for dsPIC33xxGSxx series</h3>
<div class="forum-post-body">Hi Andrew,<br>
<br>
<br>
<br>
Theses chips are not currently supported.<br>
<br>
I could just add their definition into the blockset ant let you make your own PWM driver usitn the C function call block.<br>
<br>
However, an analysis should be done to check which peripheral are identical to others dsPIC, which are differents.<br>
<br>
idem for the clock, and PLL configuration. <br>
<br>
Could you help to speed up the process ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1698">
<header><strong>Michael_hdz</strong><time datetime="2011-09-13 11:34 UTC">2011-09-13 11:34 UTC</time></header>
<h3>Re: Support for dsPIC33xxGSxx series</h3>
<div class="forum-post-body">Dear Lubin<br>
<br>
<br>
<br>
For me will be useful if you could add their definition, I have a proyect and I only using the ADC and the PWM Fault comparation from DAC are vital for me.<br>
<br>
<br>
<br>
Thanks</div>
</article>

