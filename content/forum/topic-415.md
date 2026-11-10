---
title: "OC minimum to maximum range"
url: "/forum/topic/415/"
archiveKind: "topic"
---
# OC minimum to maximum range

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1607">
<header><strong>resodad</strong><time datetime="2011-06-16 20:03 UTC">2011-06-16 20:03 UTC</time></header>
<div class="forum-post-body">Hello Lubin and all,<br>
<br>
I would like to produce a 1kHz PWM signal that varies in duty cycle from 0 to 100% in 10% steps.<br>
<br>
Please see attached simulink file. <br>
<br>
I control the duty cycle by counting presses of a button from 0 to 10.<br>
<br>
OC produces the correct signal except at 100%.<br>
<br>
At 100%, the wave form is high for 995 microseconds and the frequency drops to 380 Hz.<br>
<br>
What's wrong?<br>
<br>
Regards,<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/425-Pushbutton_to_PWMv2.mdl">Pièce jointe : Pushbutton_to_PWMv2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/426-Push_to_PWM.jpg">Pièce jointe : Push_to_PWM.jpg</a></p>
</article>

<article class="forum-post" id="p1608">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-17 06:39 UTC">2011-06-17 06:39 UTC</time></header>
<h3>Re: OC minimum to maximum range</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : resodad</header>At 100%, the wave form is high for 995 microseconds and the frequency drops to 380 Hz.</blockquote><br>
<strong>OC block</strong> compute a signal using interrupt and change during the interrupt values for the next event to appears... Thus very fast event such as 1% or 99% might not work properly. (due to software handling)<br>
<br>
Anyway, for 100% and 0% typical value, I thought added tricky code to make theses special value owrking. Perhaps that it does not work with PIC32. (mainly tested with 16 bits pic). <br>
<br>
<br>
<br>
Anyway, could you give a try replacing the <a href="/wiki/dspic-block-output-compare/">OC block</a> with the <a href="/wiki/dspic-block-output-compare-hw/">OC_HW</a> block ?<br>
<br>
<br>
<br>
Thus, I'll try to have a closer look on your question, but it is difficult for me to do it before the end of next week. I apologize for the delay...<br>
<br>
Lubin</div>
</article>

