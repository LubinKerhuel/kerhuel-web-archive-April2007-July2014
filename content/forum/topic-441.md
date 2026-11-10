---
title: "RS232 DATA TRANSFER"
url: "/forum/topic/441/"
archiveKind: "topic"
---
# RS232 DATA TRANSFER

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1701">
<header><strong>ismaeelbit</strong><time datetime="2011-09-18 09:03 UTC">2011-09-18 09:03 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Please, I need your advice on rs232 data transfer:<br>
<br>
1. using your rs232 gui, how can I increase the data port above the maximum 16 lines supported now? I need to port extra 6 lines<br>
<br>
<br>
<br>
2. any example on building custom gui with matlab/labview?<br>
<br>
<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p1723">
<header><strong>LubinKerhuel</strong><time datetime="2011-10-07 23:58 UTC">2011-10-07 23:58 UTC</time></header>
<h3>Re: RS232 DATA TRANSFER</h3>
<div class="forum-post-body">Ismael,<br>
<br>
<br>
<br>
All my bad for the very long delay.<br>
<br>
Here is one of my old model where I logged IMU data from a RC airplane (through High range BlueTooth).<br>
<br>
<br>
<br>
Data from IMU sensor were logged at 1Khz I remember while RC receiver set point (refreshed at 50Hz) were sent at much lower frequency.<br>
<br>
<br>
<br>
Some data are packed and some are multiplexed. The "Rx-Tx for Matlab-Labview" protocol is not used here. But it's pretty straight to build your own protocole with simple simulink blocks and to decode it throuth a m script.<br>
<br>
<br>
<br>
I provide here both Simulink model (complete with sensor etc...) and the m script for decoding recorded .txt file (raw data from BlueTooth Virtual UART). You might use rs232gui to log data or any other tools (realterm is pretty nice and much lighter than matlab for outdoor loging with low power laptop).<br>
<br>
The script also plot rate gyro data and acceleration as well as RC commands. I used theses to idenitfy the gliders dynamic model.<br>
<br>
Actually, results from this glider flight were pretty interresting. I hope getting time to publish all that one day.<br>
<br>
<br>
<br>
Anyway, Home this will help you. Let me know<br>
<br>
It is all given as is.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/444-MixerSimple_LogIMU_RawDatas_30f4012.mdl">Pièce jointe : MixerSimple_LogIMU_RawDatas_30f4012.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/445-ExtractData.m">Pièce jointe : ExtractData.m</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/446-Flight003.txt">Pièce jointe : Flight003.txt</a></p>
</article>

<article class="forum-post" id="p1727">
<header><strong>ismaeelbit</strong><time datetime="2011-10-12 04:55 UTC">2011-10-12 04:55 UTC</time></header>
<h3>Re: RS232 DATA TRANSFER</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Am grateful for the information and for sharing your precious effort.<br>
<br>
I will look into the examples and let you know how far this can take me.<br>
<br>
<br>
<br>
Thanks for the support</div>
</article>

