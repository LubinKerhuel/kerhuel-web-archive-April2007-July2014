---
title: "I2C problem on UDB4 board"
url: "/forum/topic/476/"
archiveKind: "topic"
---
# I2C problem on UDB4 board

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1820">
<header><strong>alpert</strong><time datetime="2012-01-25 18:35 UTC">2012-01-25 18:35 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
I'm using the Sparkfun's UDB4 board.<br>
<br>
I've tried to make his I2c to work and I bump into something strange. <br>
<br>
<br>
<br>
[ Before i'll continue, just for the protocol, I have already tested the I2C block on GlounPilot's board (dsPIC33fj256jMC710) and it worked fine ] .<br>
<br>
<br>
<br>
So, here is the problem:<br>
<br>
This board have 2 port of I2C. One suppose to be used by the EEPROM and the other is free to connect. Both ports are connected to PULL-UP resistors on the board.<br>
<br>
I've made a simple model which use I2C_2 and sends a constant number to a constant address every 0.1 sec. here is the model:<br>
<br>
<br>
After that, I have touched with a scope on I2C_1 (mark as (1) on the picture) and I2C_2 and i found out that they both show the same signal (its a bad signal, but i'll keep this problem for the next topic).<br>
<br>
<br>
<br>
After that i changed th model to I2C_1 and no signal appear on both ports (i have tried to touch directly on the PULL-UP).<br>
<br>
<br>
<br>
Here is a picture of the board, i marked the I2C_1 and I2C_2 and the PULL-UP resistors:<br>
<br>
<br>
Lubin, can you please test it on your board?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Alpert</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/480-ex10_I2C.mdl">Pièce jointe : ex10_I2C.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/481-I2C.jpg">Pièce jointe : I2C.jpg</a></p>
</article>

<article class="forum-post" id="p1828">
<header><strong>alpert</strong><time datetime="2012-02-09 15:31 UTC">2012-02-09 15:31 UTC</time></header>
<h3>Re: I2C problem on UDB4 board</h3>
<div class="forum-post-body">OK. Problem solved after clicking on "Erase flash device" in MPLAB. <br>
<br>
Mybe the problem has occur because the MPLAB's programer set to "Allow PICkit 3 to select memories and ranges" and from some reason it didn't update all the registers (Lubin, is it a possible explanation?) <br>
<br>
<br>
<br>
Now there is another problem with the I2C, but i will start a new topic for it.</div>
</article>

