---
title: "SPI - IMU &quot;2&quot;"
url: "/forum/topic/278/"
archiveKind: "topic"
---
# SPI - IMU &quot;2&quot;

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1095">
<header><strong>Bobes</strong><time datetime="2010-02-27 22:48 UTC">2010-02-27 22:48 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
I am trying to use SPI: I have ADIS16405. I have tried scheme used in IMU, but I do not exactly understand what are the inputs?  I guess they are addresses, but how to get to those numbers? (I am looking at the IMU_dsPIC_30f4012_TestElectronics.mdl)<br>
<br>
I do not think that my problem is wiring, when I reset ADIS, I receive 2^16, otherwise its always zero, in some cases I have got 17.<br>
<br>
<br>
<br>
"trame" is frame in french?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/293-ADIS16400_16405.pdf">Pièce jointe : ADIS16400_16405.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/294-Vejlupek_CAR4_dsPIC33_ACU44_SPI_R01.mdl">Pièce jointe : Vejlupek_CAR4_dsPIC33_ACU44_SPI_R01.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/295-Vejlupek_CAR4_dsPIC33_ACU44_SPI_R02.mdl">Pièce jointe : Vejlupek_CAR4_dsPIC33_ACU44_SPI_R02.mdl</a></p>
</article>

<article class="forum-post" id="p1096">
<header><strong>Bobes</strong><time datetime="2010-02-27 23:28 UTC">2010-02-27 23:28 UTC</time></header>
<h3>Re: SPI - IMU &amp;quot;2&amp;quot;</h3>
<div class="forum-post-body">update: i have changed back to the interrupt driven SPI bloc, and I am getting some data, just not on all channels and also they seems to be mixed. ie I am getting something that is reacting on my screwdriver (magnetic) but the readout is on accY<br>
<br>
will work more, just in case someone see some ovious error that I am missing, please let me know .)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/296-Vejlupek_CAR4_dsPIC33_ACU44_SPI_R02.mdl">Pièce jointe : Vejlupek_CAR4_dsPIC33_ACU44_SPI_R02.mdl</a></p>
</article>

<article class="forum-post" id="p1140">
<header><strong>Bobes</strong><time datetime="2010-03-19 20:34 UTC">2010-03-19 20:34 UTC</time></header>
<h3>Re: SPI - IMU &amp;quot;2&amp;quot;</h3>
<div class="forum-post-body">ok, uff, found the problem! its in the data-sheet, or I am an an-alphabet... I believe that AD have a bug in their data-sheet.<br>
<br>
they have addresses for X-Z gyro X-Z accelerometer X-Z magnetometer like this: 0400 0600 0800 0A00 0C00 0E00 1000 1200 1400<br>
<br>
But I am running it and finally reading data that make sense like this: 0400 0500 0600 0700 0800 0900 0A00 0B00 0C00 (or one less, I am not sure right now, I have the model at school)</div>
</article>

