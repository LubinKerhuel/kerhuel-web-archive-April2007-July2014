---
title: "PWM simultaneous switching problem"
url: "/forum/topic/570/"
archiveKind: "topic"
---
# PWM simultaneous switching problem

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1983">
<header><strong>welf</strong><time datetime="2013-02-13 16:34 UTC">2013-02-13 16:34 UTC</time></header>
<div class="forum-post-body">I previously had no problem running the motor PWM block in "2 quadrant" mode, i.e. PWM only of the high side switches. I would now  like to operate in "4 quadrant" mode, with simultaneous PWM  of both the high and low side switches (but not using complementary switching).<br>
<br>
<br>
<br>
I cannot find a way to enable both high and low switches for PWM without having complementary output enabled (which I do not want).<br>
<br>
<br>
<br>
I know that this is possible because if I manually edit the following line in the code it works fine:<br>
<br>
<br>
<br>
#define config2                        (0xffff &amp; PWM1_PEN1L &amp; PWM1_MOD1_IND &amp; PWM1_PDIS1H &amp; PWM1_PEN2L &amp; PWM1_MOD2_IND &amp; PWM1_PDIS2H &amp; PWM1_PEN3L &amp; PWM1_MOD3_IND &amp; PWM1_PDIS3H)<br>
<br>
<br>
<br>
Removing the  PWM1_PDISxH parts allows me to achieve what I want.<br>
<br>
<br>
<br>
Is this a bug?</div>
</article>

