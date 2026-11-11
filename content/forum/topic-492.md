---
title: "I2C does not build on PIC32"
url: "/forum/topic/492/"
archiveKind: "topic"
---
# I2C does not build on PIC32

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1873">
<header><strong>resodad</strong><time datetime="2012-04-04 13:31 UTC">2012-04-04 13:31 UTC</time></header>
<div class="forum-post-body">Lubin,<br>
<br>
Please look into this. I believe it is a bug.<br>
<br>
There are two other related posts from 2010:<br>
<br>
<a href="/forum/topic/318/">http://www.kerhuel.eu/forum/viewtopic.php?f=1&amp;t=318</a><br>
<br>
and<br>
<br>
<a href="/forum/topic/267/">http://www.kerhuel.eu/forum/viewtopic.php?f=8&amp;t=267</a><br>
<br>
Thanks<br>
<br>
John<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/502-I2C_test_simple2.mdl">Pièce jointe : I2C_test_simple2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/503-i2cBuildError.txt">Pièce jointe : i2cBuildError.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/504-desktopFig.jpg">Pièce jointe : desktopFig.jpg</a></p>
</article>

<article class="forum-post" id="p1878">
<header><strong>resodad</strong><time datetime="2012-04-25 12:37 UTC">2012-04-25 12:37 UTC</time></header>
<h3>Re: I2C does not build on PIC32</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Can you please tell me if this bug is a priority for you?<br>
<br>
If it is not, I will work on the I2C code in C.<br>
<br>
Thanks, John</div>
</article>

<article class="forum-post" id="p1883">
<header><strong>LubinKerhuel</strong><time datetime="2012-04-27 00:31 UTC">2012-04-27 00:31 UTC</time></header>
<h3>Re: I2C does not build on PIC32</h3>
<div class="forum-post-body">Hello John,<br>
<br>
<br>
<br>
As you probably noticed, I am pretty busy theses time.<br>
<br>
It's would be difficult for me spend much time on this question.<br>
<br>
<br>
<br>
However, if the problem is just one bit MI2C1IF whose name changed, I might solve it pretty easily.<br>
<br>
Do you think the problem is limited to this ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1886">
<header><strong>resodad</strong><time datetime="2012-04-27 13:58 UTC">2012-04-27 13:58 UTC</time></header>
<h3>Re: I2C does not build on PIC32</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
My C expert, Konstantin, says:<br>
<br>
"Probably not, although it most likely will not be too much work to fix.<br>
<br>
In the I2CCON register in particular, going from the dsPIC family of microcontrollers to the PIC32, the I2CCON register gets renamed I2CxCON where x is the I2C module number. Also within the I2CCON register itself the I2CEN and I2CSIDL bits get renamed ON and SIDL in the PIC32 hardware."<br>
<br>
John</div>
</article>

