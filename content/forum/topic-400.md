---
title: "UART2, UART alternativ et I2C in the same time"
url: "/forum/topic/400/"
archiveKind: "topic"
---
# UART2, UART alternativ et I2C in the same time

Forum : [dsPIC Peripherals](/forum/#forum-9)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1579">
<header><strong>Amandine Randuineau</strong><time datetime="2011-05-17 07:33 UTC">2011-05-17 07:33 UTC</time></header>
<div class="forum-post-body">Dear Mister Kerhuel,<br>
<br>
For 4 months, I am working with mister Bateman in the Military Air School of Salon de Provence. I would like create an embedded system to control an UAV.<br>
<br>
To do this, I made a program to decode a serial frame from a receiver, one to decode a serial frame from a inertial measure unit and one to control 6 engines with the I2C. One by one, each program is working. When I tried to bring the program together, it was working but the sending frequency of the number 102 in the alternativ UART wasn't the one that I wanted. In fact, to obtain the IMU's informations I have to send to its the letter f (102 in ascii code).<br>
<br>
I am working with a dsPIC 30f4013.<br>
<br>
I would like to know if you have already seen this problem using the UART 2, the UART alternativ and the I2C in the same time and if you could help me please.<br>
<br>
I send you my simulink program.<br>
<br>
Yours sincerely.<br>
<br>
Amandine Randuineau</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/417-commoteur.mdl">Pièce jointe : commoteur.mdl</a></p>
</article>

<article class="forum-post" id="p1583">
<header><strong>LubinKerhuel</strong><time datetime="2011-05-19 08:43 UTC">2011-05-19 08:43 UTC</time></header>
<h3>Re: UART2, UART alternativ et I2C in the same time</h3>
<div class="forum-post-body">Hi Amandine,<br>
<br>
<br>
<br>
For the UART problem,<br>
<br>
could you try :<br>
<br>
<br>
<br>
- Simulation ==&gt; Configuration parameters ==&gt; Optimisation : Check inline parameters (code will be more efficient)<br>
<br>
- UART 1 Config ==&gt; Tx Tab ==&gt; Interrupt configuration : Do not use interrupt (not required here as you sent 1 data every  15ms and the UART baud rate is much higher than this.)<br>
<br>
You may also uncheck suppport for inf time, nan value, imaginary number...<br>
<br>
<br>
<br>
Decoding UART should be done only when data are received. Thus for each UART (UART 1 and UART 2) the <strong>receive output flag</strong> should activate a subsystem which compute the decoding.<br>
<br>
<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1591">
<header><strong>ismaeelbit</strong><time datetime="2011-05-30 06:09 UTC">2011-05-30 06:09 UTC</time></header>
<h3>Re: UART2, UART alternativ et I2C in the same time</h3>
<div class="forum-post-body">Hi Amandine,<br>
<br>
I am working also on UAV embedded system and I will like to ask if you are using GPS and how you are able to use the Lubin blockset to acquire the gps data via serial port.<br>
<br>
<br>
<br>
Thanks</div>
</article>

