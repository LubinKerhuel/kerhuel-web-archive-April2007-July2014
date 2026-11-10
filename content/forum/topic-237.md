---
title: "CAN Configuration"
url: "/forum/topic/237/"
archiveKind: "topic"
---
# CAN Configuration

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p912">
<header><strong>sathishr</strong><time datetime="2009-07-26 20:02 UTC">2009-07-26 20:02 UTC</time></header>
<div class="forum-post-body">I'm trying to setup a dspic 30f4011 w/ CAN.<br>
<br>
<br>
<br>
I can get error frames on the CAN network but can't get the PIC to transmit at 500k.<br>
<br>
<br>
<br>
I'm using a dsPICDEM2 w/ a 8 MHz crystal.  I've configured the bit timing based on the settings suggested by the Intrepidcs Microchip CAN Bit Timing Calculator.  The issue seems to be that the device doesn't match this calculator at all and how you configure the MIPS setting.  <br>
<br>
<br>
<br>
I've configured the oscillator for XT_PLL8 and the MIPS at 16MIPS.  I can't seem to get the correct settings for the CAN channel.  Can someone provide details on what I need to do?<br>
<br>
<br>
<br>
I'm running MPLAB v8.3 w/ Matlab 2007b and the C30 compiler.<br>
<br>
<br>
<br>
Attached should be my model.  What am I setting incorrectly?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/255-test_v2.mdl">Pièce jointe : test_v2.mdl</a></p>
</article>

<article class="forum-post" id="p927">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 09:55 UTC">2009-07-30 09:55 UTC</time></header>
<h3>Re: CAN Configuration</h3>
<div class="forum-post-body">Dear sathishr ,<br>
<br>
<br>
<br>
It's a very long time I made the blocks CAN and I have not been using them since. Anyway, It works well when I tested it.<br>
<br>
<br>
<br>
Anyway,  I do not understand how you can check the received data with this model. You should try for example to send CAN received data to the PC through the UART port. or make a led blinking when a specific data is received. The "Display" blocks have no effect.<br>
<br>
<br>
<br>
Also, you may check if the dsPIC is effectively running at 16 MIPS (using a blinking led for example and checking precisely with a scope). Anyway, If you find any bug in the CAN configuration, please report, I'll correct it.<br>
<br>
<br>
<br>
Lubin</div>
</article>

