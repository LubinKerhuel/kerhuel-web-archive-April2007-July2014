---
title: "I2C on PIC32"
url: "/forum/topic/314/"
archiveKind: "topic"
---
# I2C on PIC32

Forum : [General Remark and Questions](/forum/#forum-1)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p1269">
<header><strong>edlaurence</strong><time datetime="2010-07-11 19:23 UTC">2010-07-11 19:23 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
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
I saw that you intended to take a look at the I2C blockset for PIC32F and was wondering if you had managed to make any progress on this issue?  If you need any info from me please let me know.<br>
<br>
<br>
<br>
Many thanks,<br>
<br>
<br>
<br>
Ed Laurence</div>
</article>

<article class="forum-post" id="p1271">
<header><strong>jkavitha_john</strong><time datetime="2010-07-19 08:58 UTC">2010-07-19 08:58 UTC</time></header>
<h3>problem with IC7&amp;amp;IC8</h3>
<div class="forum-post-body">Hi Lubin<br>
<br>
<br>
<br>
       I want to read freq by using  Input Capture. Can I use IC7 Capture in demo version?.</div>
</article>

<article class="forum-post" id="p1272">
<header><strong>jkavitha_john</strong><time datetime="2010-07-19 09:03 UTC">2010-07-19 09:03 UTC</time></header>
<h3>time delay of serial port transmission</h3>
<div class="forum-post-body">Hi Lubin<br>
<br>
<br>
<br>
       How can I find the time delay of serial port rs232 data transmission?.<br>
<br>
<br>
<br>
Thanking You<br>
<br>
Kavitha</div>
</article>

<article class="forum-post" id="p1273">
<header><strong>LubinKerhuel</strong><time datetime="2010-07-20 23:08 UTC">2010-07-20 23:08 UTC</time></header>
<h3>Re: problem with IC7&amp;amp;IC8</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : jkavitha_john</header>Hi Lubin<br>
<br>
       I want to read freq by using  Input Capture. Can I use IC7 Capture in demo version?.</blockquote><br>
<br>
it should be Ok if the microcontroller has an IC7 pin. If it does not work, it's a bug, please report !<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jkavitha_john</header>time delay of serial port rs232 data transmission?</blockquote><br>
could you define what is time delay ?<br>
<br>
<br>
<br>
The rs232gui interface allow to do real time visualisation, but is not a true real time system. Delay (added to natural bits transmission delay) can appears due to windows, java, and also from bluetooth or USB if you are using a virtual port com (over bluetooth os USB)</div>
</article>

<article class="forum-post" id="p1274">
<header><strong>jkavitha_john</strong><time datetime="2010-07-21 09:18 UTC">2010-07-21 09:18 UTC</time></header>
<h3>Re: Gui Interface</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
   thanks for ur reply. The IC7 &amp; IC8 blocks are compiled sucessfully without any error report but its not read any values from the input signal . The IC1 &amp; IC2 blocks read the input signal correctly.<br>
<br>
And I have one more doubt, Can I send a single 16 bit data to dsPIC Controller through GUI Interface? Its posibilites or not.<br>
<br>
<br>
<br>
Thanking you,<br>
<br>
Kavitha</div>
</article>

<article class="forum-post" id="p1275">
<header><strong>LubinKerhuel</strong><time datetime="2010-07-21 11:31 UTC">2010-07-21 11:31 UTC</time></header>
<h3>Re: I2C on PIC32</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : jkavitha_john</header>but its not read any values from the input signal </blockquote><br>
thus, there should be a problem. Could you check at generated  C code if you can identify the problem ? otherwise, post your simulink model on the forum, i'll could try to have a look.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jkavitha_john</header>Can I send a single 16 bit data to dsPIC Controller through GUI Interface?</blockquote><br>
GUI interface can only send 8 bits data. Thus, you have to build your own decoder on the embedded system (typically, through a simulink subsystem) to reconstruct a 16 bit data from two or more 8 bits data...</div>
</article>

<article class="forum-post" id="p1278">
<header><strong>jkavitha_john</strong><time datetime="2010-07-24 05:07 UTC">2010-07-24 05:07 UTC</time></header>
<h3>Re: I2C on PIC32</h3>
<div class="forum-post-body">hi Lubin,<br>
<br>
 Here attached the simulink model which I am working for IC7 &amp; IC8.Which is not working. please give solution to this.<br>
<br>
How can I read position from QEI.<br>
<br>
<br>
<br>
Thanks.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/347-dcpos_ol.mdl">Pièce jointe : dcpos_ol.mdl</a></p>
</article>

