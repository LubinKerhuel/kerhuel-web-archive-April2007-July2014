---
title: "Rs 232 Gui Interface with PIC 32 starter kit"
url: "/forum/topic/351/"
archiveKind: "topic"
---
# Rs 232 Gui Interface with PIC 32 starter kit

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1444">
<header><strong>chandupotluri</strong><time datetime="2011-01-20 01:35 UTC">2011-01-20 01:35 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I am using PIC 32 statrter kit. I am reading the data from the ADC and want to transmit  through UART to PC. PIC 32 starter kit only has a USB. When I am trying to establish the connection through COM port 3 it is doing it. But I am not able to see any data that is being received. I tried doing all the suggestion you made in forum for a similar problem but was unsucessfull. I am just wondering if there is away to connect the comm ports through the USB. I am also attaching my model as a reference.<br>
<br>
<br>
<br>
Thanks in advance.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/370-trail5freqchangeBandF_analog_uart1.mdl">Pièce jointe : trail5freqchangeBandF_analog_uart1.mdl</a></p>
</article>

<article class="forum-post" id="p1461">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-15 21:33 UTC">2011-02-15 21:33 UTC</time></header>
<h3>Re: Rs 232 Gui Interface with PIC 32 starter kit</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I hardly use this starter kit. As far as I remember, It is not possible to connect to the dsPIC UART from the USB. (I think that USB is connected to a PIC with USB peripheral which may act as a bootloader only).<br>
<br>
<br>
<br>
Try to find an available UART pin on the board. You may then connect the two pin (Rx-Tx) with a <a href="http://www.ftdichip.com/Products/Cables/USBTTLSerial.htm">FTDI cable</a>.<br>
<br>
 <br>
<br>
Lubin</div>
</article>

