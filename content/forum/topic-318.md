---
title: "I2C on PIC32"
url: "/forum/topic/318/"
archiveKind: "topic"
---
# I2C on PIC32

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1284">
<header><strong>edlaurence</strong><time datetime="2010-08-02 11:34 UTC">2010-08-02 11:34 UTC</time></header>
<div class="forum-post-body">Hi again Lubin,<br>
<br>
<br>
<br>
Looks like my last thread got hijacked so here it is again....<br>
<br>
<br>
<br>
I'm having some problems building a model to communicate between a PIC32 (32MX360F256L) and a Bosch accelerometer (BMA180) using an I2C bus for a heli autopilot application. Looking through the posts on the forum I think this problem was found by another user earlier this year and seems to fall over at the following point during the build..<br>
<br>
<br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:1: warning: Compiler option ignored due to lite-mode limitations <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c: In function `dsPIC_32MX360F256L_AccelI2C_step': <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:48: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:55: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:58: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:68: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:71: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:78: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:81: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:93: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:96: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:103: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:106: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:118: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:121: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:128: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:131: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:142: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:145: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:162: error: union has no member named `MI2C1IF' <br>
<br>
dsPIC_32MX360F256L_AccelI2C.c:165: error: union has no member named `MI2C1IF' <br>
<br>
gmake: *** [dsPIC_32MX360F256L_AccelI2C.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'dsPIC_32MX360F256L_AccelI2C' aborted due to an error.<br>
<br>
C32 Compiler found<br>
<br>
C32 Compiler found<br>
<br>
C32 Compiler found<br>
<br>
<br>
<br>
<br>
<br>
I saw that you intended to take a look at the I2C blockset for PIC32F and was wondering if you had managed to make any progress on this issue? If you need any info from me please let me know.<br>
<br>
<br>
<br>
Many thanks,<br>
<br>
<br>
<br>
Ed Laurence</div>
</article>

<article class="forum-post" id="p1871">
<header><strong>resodad</strong><time datetime="2012-04-03 20:21 UTC">2012-04-03 20:21 UTC</time></header>
<h3>Re: I2C on PIC32</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I've got the same problem.<br>
<br>
John<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/499-i2cBuildError.txt">Pièce jointe : i2cBuildError.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/500-I2C_test_simple2.mdl">Pièce jointe : I2C_test_simple2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/501-desktopFig.jpg">Pièce jointe : desktopFig.jpg</a></p>
</article>

<article class="forum-post" id="p1872">
<header><strong>resodad</strong><time datetime="2012-04-04 13:24 UTC">2012-04-04 13:24 UTC</time></header>
<h3>Re: I2C on PIC32</h3>
<div class="forum-post-body">All,<br>
<br>
This belongs in the BUG REPORTS forum.<br>
<br>
I will re-post there.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1971">
<header><strong>adina728</strong><time datetime="2012-12-24 04:51 UTC">2012-12-24 04:51 UTC</time></header>
<h3>Re: I2C on PIC32</h3>
<div class="forum-post-body">Nice Post...Thanks for the info</div>
</article>

