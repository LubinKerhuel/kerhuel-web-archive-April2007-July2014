---
title: "Simulink interface dspic"
url: "/forum/topic/195/"
archiveKind: "topic"
---
# Simulink interface dspic

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p708">
<header><strong>zheng</strong><time datetime="2009-01-27 13:30 UTC">2009-01-27 13:30 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
 <br>
<br>
Currently I am working on a microcontroller project. I need to transmit real time data from simulink to PIC with RS232. I downloaded "Embedded Target for Microchip dsPIC" toolbox, and added UART configuration, Tx Output, but I failed to send data to pic. I used matlab to send directly and it can work. Is there anything else I should do to get it work?<br>
<br>
Really appresicated if you can help. <br>
<br>
<br>
<br>
Regards<br>
<br>
Zheng jun</div>
</article>

<article class="forum-post" id="p714">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-29 11:21 UTC">2009-01-29 11:21 UTC</time></header>
<h3>Re: Simulink interface dspic</h3>
<div class="forum-post-body">Hi Zheng,<br>
<br>
<br>
<br>
This blockset aims to compile the simulink model for the PIC/dsPIC. i.e. execute the simulink model inside the microcontroller. Thus, the Tx block simulated on a PC platform will have no effect, but once compiled and upload on the microcontroller, it will output data stream on the dsPIC Tx pin.<br>
<br>
Anyway, you could use the graphical interface <a href="/wiki/simulink-embedded-target-for-pic/">RS232gui</a> to send and receive data through rs232 port in your your matalab environment.<br>
<br>
<br>
<br>
Or you may be interested by a blockset written by Leonardo Daga that can send/receive data from the simulink model : see <a href="http://www.mathworks.com/matlabcentral/fileexchange/authors/8294">http://www.mathworks.com/matlabcentral/ ... thors/8294</a><br>
<br>
Unfortunatly, it has not been compiled with a recent matlab version...</div>
</article>

