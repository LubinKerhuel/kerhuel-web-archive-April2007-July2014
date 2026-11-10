---
title: "CAN Communication Between two PIC microcontrollers"
url: "/forum/topic/337/"
archiveKind: "topic"
---
# CAN Communication Between two PIC microcontrollers

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1343">
<header><strong>varunvummaneni</strong><time datetime="2010-11-26 20:25 UTC">2010-11-26 20:25 UTC</time></header>
<div class="forum-post-body">Hi Lubin, <br>
<br>
I want to use CAN communication between to dsPICs.<br>
<br>
They are 30f4011 and 30f 4013. My aim is to send joystick signals from 4011 to 4013 using CAN. and receive them at PC using UART from 4013. Can u please suggest me how to configure CAN blocks??</div>
</article>

<article class="forum-post" id="p1359">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 23:07 UTC">2010-11-29 23:07 UTC</time></header>
<h3>Re: CAN Communication Between two PIC microcontrollers</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I did not build an example with CAN communication yet as I was waiting to suport ECAN to build a demo of CAN peripheral communicating with ECAN. Anyway, I attach the two messy model used at testing time. <br>
<br>
I used two 30f4012 dsPIC that communicate throught CAN. I am not sure the two models are in a good shape. The last test I made was I guess to check that one dsPIC could receive the message that it sent. However, modifying just a bit the identifiers reception or emission filters will make you able to make two dsPIC communicating.<br>
<br>
<br>
<br>
Make sure you place the CAN driver chips with the correct pull-up resistor that make the CAN bus workable ! It might be usefull to use a scope for debugging !<br>
<br>
<br>
<br>
Please keep let me know what's happening !</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/356-CAN.mdl">Pièce jointe : CAN.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/357-CAN231.mdl">Pièce jointe : CAN231.mdl</a></p>
</article>

