---
title: "Output Compare block"
url: "/forum/topic/64/"
archiveKind: "topic"
---
# Output Compare block

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p124">
<header><strong>deepak223</strong><time datetime="2007-11-18 02:01 UTC">2007-11-18 02:01 UTC</time></header>
<div class="forum-post-body">Lubin, I want to generate a PWM signal using the output compare block.  I looked at the examples provided in the toolbox (Servo_ADC.mdl,Servo_sinus.mdl) but it is entirely clear to me how to set OCxR and PRy registers in dsPIC33f.<br>
<br>
How to define the PWM period and duty cycle in the block.<br>
<br>
<br>
<br>
thanks<br>
<br>
Deepak</div>
</article>

<article class="forum-post" id="p125">
<header><strong>LubinKerhuel</strong><time datetime="2007-11-19 23:26 UTC">2007-11-19 23:26 UTC</time></header>
<div class="forum-post-body">Configure the channel to 'Up - Period' (5)<br>
<br>
The Up input (uint 16) of the block set the Duty Cycle, and the Period input (uint 16) of the block set the period.<br>
<br>
<br>
<br>
You must define the max period you will use in 'Max / Channel'.<br>
<br>
<br>
<br>
One uint 16 variable is automaticaly defined in the matlab workspace : OC?max (where ? is the channel number).<br>
<br>
This variable corresponds to the time of the max period defined for that channel. This value must be used to scale the Duty cycle and the Period.<br>
<br>
<br>
<br>
for example, if you define 'Max / Channel' = 10e-3 (for 10ms)<br>
<br>
Then if you define the Period Input as OC1max, this will produce a period of 10e-3.<br>
<br>
if you define the Period Input as round(OC1max/2), this will produce a period of 5e-3.<br>
<br>
<br>
<br>
The Duty Cycle time is defines in the same way...<br>
<br>
<br>
<br>
Help is available on the web page : <a href="/RTWdsPIC/Blocks/OutputCompare.html">http://archive.kerhuel.eu/RTWdsPIC/Blocks/O ... mpare.html</a></div>
</article>

