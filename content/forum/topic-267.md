---
title: "PIC32. Problems with I2C."
url: "/forum/topic/267/"
archiveKind: "topic"
---
# PIC32. Problems with I2C.

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1046">
<header><strong>uwlu</strong><time datetime="2010-01-24 18:37 UTC">2010-01-24 18:37 UTC</time></header>
<div class="forum-post-body">My hard- and software: PIC32MX360F512L 80MHz, matlab 2008a.<br>
<br>
<br>
<br>
Hi Lubin,<br>
<br>
I'm trying to communicate with a HMC5843 sensor. It's a I2C device. For this task I have built a very simple model. I want to use I2C 1 with 400 kHz. The reload value for the BRG can be calculated or taken from the table according the PIC32MX Family Reference Manual, Section 24(DS61116D) p.32. I take the I2CxBRG value for 40 MHz PBCLK from the table 24-1. It is 0x030 or 48 in decimal. I put then this value into the I2C Master Block and get Fscl = 661.157 kHz. Why? Shouldn't be a value about 400 kHz? It's my first problem. The next problem occurs if I try to compilate the model. I get an error message like:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1138<br>
<br>
<br>
<br>
and in Command Window<br>
<br>
<br>
<br>
magnet_field_sensor.c: In function `magnet_field_sensor_step': <br>
<br>
magnet_field_sensor.c:48: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:55: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:58: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:67: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:70: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:79: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:82: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:91: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:94: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:104: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:111: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:114: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:124: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:127: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:134: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:137: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:148: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:151: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:170: error: union has no member named `MI2C1IF' <br>
<br>
magnet_field_sensor.c:173: error: union has no member named `MI2C1IF' <br>
<br>
gmake: *** [magnet_field_sensor.o] Error 1 <br>
<br>
<br>
<br>
Could you please give me an advise what I'm doing wrong?<br>
<br>
<br>
<br>
Regards<br>
<br>
Oliver</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/289-magnet_field_sensor.mdl">Pièce jointe : magnet_field_sensor.mdl</a></p>
</article>

<article class="forum-post" id="p1050">
<header><strong>uwlu</strong><time datetime="2010-01-26 14:31 UTC">2010-01-26 14:31 UTC</time></header>
<h3>Re: PIC32. Problems with I2C.</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Did you overlook my post? I'm still waiting for your help.<br>
<br>
<br>
<br>
Regards<br>
<br>
Oliver</div>
</article>

<article class="forum-post" id="p1051">
<header><strong>Bobes</strong><time datetime="2010-01-26 22:02 UTC">2010-01-26 22:02 UTC</time></header>
<h3>Re: PIC32. Problems with I2C.</h3>
<div class="forum-post-body">I dont think I can help you, but you should probably also post your c-file.<br>
<br>
Kind regards Josef</div>
</article>

<article class="forum-post" id="p1054">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-27 00:32 UTC">2010-01-27 00:32 UTC</time></header>
<h3>Re: PIC32. Problems with I2C.</h3>
<div class="forum-post-body">Hi Olivier,<br>
<br>
<br>
<br>
I should do some more test on I2C with PIC32. I have no project using this target yet and errors may remains.<br>
<br>
I'll try to have a look on it, but I may not be able to do it in the next two or three weeks.<br>
<br>
<br>
<br>
Lubin</div>
</article>

