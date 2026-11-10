---
title: "I2C - alternative pin"
url: "/forum/topic/265/"
archiveKind: "topic"
---
# I2C - alternative pin

Forum : [dsPIC Peripherals](/forum/#forum-9)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1033">
<header><strong>Bobes</strong><time datetime="2010-01-19 12:52 UTC">2010-01-19 12:52 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
I am using dsPIC33FJ128MC804. I was wandering if there is setting on I2C block, that would allow me to switch to alternative pin-out (It is not re-mappable, but you have two pairs of pins to select from.. at least that is how I understand it)<br>
<br>
I would rather use ASDA1 and ASCL1 (pin 42 and 43), than SDA1 and SCL1 (pin 44 and 1).<br>
<br>
Is there some easy (tick box) way, or should I do that via c-function?<br>
<br>
Thanks<br>
<br>
Kind regards<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1035">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-19 13:03 UTC">2010-01-19 13:03 UTC</time></header>
<h3>Re: I2C - alternative pin</h3>
<div class="forum-post-body">This option has not been implemented yet.<br>
<br>
<br>
<br>
I may have a look at it as it sound pretty easy to do.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1036">
<header><strong>Bobes</strong><time datetime="2010-01-19 13:07 UTC">2010-01-19 13:07 UTC</time></header>
<h3>Re: I2C - alternative pin</h3>
<div class="forum-post-body">ok, would be great.<br>
<br>
as for PIC I am using - Register Settings: BitField: ALTI2C, Register: FPOR, 1 = SDA1/SCL1, 0 = ASDA1/ASCL1</div>
</article>

