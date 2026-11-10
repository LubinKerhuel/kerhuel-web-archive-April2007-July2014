---
title: "Encoder interfacing with dsPIC33FJ256MC710"
url: "/forum/topic/177/"
archiveKind: "topic"
---
# Encoder interfacing with dsPIC33FJ256MC710

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p614">
<header><strong>giulio</strong><time datetime="2008-11-20 17:15 UTC">2008-11-20 17:15 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I expose the problem:<br>
<br>
I'm working on the Flex (full version) and I have to interface two incremental rotary encoders, both with 2 channels;<br>
<br>
the control I've dveloped is formed by the two encoder signals in input (processed by QEI or other; I never thought about yet)  <br>
<br>
and the torque for the electric motor in output (there are differences using OC or PWMout block?). <br>
<br>
I'm asking to myself where I can place it: in the gpio, one in gpio and the other in QEI, or with an external chip (like hctl2032)? <br>
<br>
for all this solutions I would also need the simulink blocks. I'm not so expert in this field for create the c functions and than the blocks,<br>
<br>
and also for conversions of the type. <br>
<br>
Can I have your help?<br>
<br>
<br>
<br>
thanks<br>
<br>
Giulio</div>
</article>

<article class="forum-post" id="p681">
<header><strong>malife</strong><time datetime="2009-01-11 04:17 UTC">2009-01-11 04:17 UTC</time></header>
<h3>Re: Encoder interfacing with dsPIC33FJ256MC710</h3>
<div class="forum-post-body">Hello Giulio,<br>
<br>
 It seems like your problem is a bit more related to design rather than the blockset itself. If you need to read more than one QEI channel, than there is not much you can do with a dsPIC. You can try using the input capture, but be aware that you have to write your own logic to determine the phase and the speed (besides you need an aditional one if you want to use the index from the encoder). QEI is a relatively new module in the dsPICs make sure you look at the Microchip websited they have a "tips and tricks" document specifically related to doing that with interrupts and the input capture module (which is fully soported by Lubin's blockset).<br>
<br>
<br>
<br>
Regarding PWM, yes, PWM engine is much more efficient than the OC. The PWM uses no timer and it is better suited for motor control.<br>
<br>
<br>
<br>
Hope this helps<br>
<br>
<br>
<br>
Mariano</div>
</article>

