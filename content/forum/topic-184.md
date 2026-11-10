---
title: "Oscillator mode  &amp; MIPS configuration"
url: "/forum/topic/184/"
archiveKind: "topic"
---
# Oscillator mode  &amp; MIPS configuration

Forum : [General Remark and Questions](/forum/#forum-1)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p640">
<header><strong>gladiac</strong><time datetime="2008-12-18 11:55 UTC">2008-12-18 11:55 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
My device is 30f6014A and demo board is dsPICDEM 1.1 of Microchip. The crystal of the board is 7.3728 MHz. So the typical configs are:<br>
<br>
XT mode - 7.3728 MHz /1.8432 MIPS <br>
<br>
XT w/ PLL 4x mode - 29.4912 MHz / 7.3728 MIPS <br>
<br>
XT w/ PLL 8x mode - 58.9824 MHz /14.7456 MIPS <br>
<br>
XT w/ PLL 16x mode - 117.9648 MHz / 29.4912 MIPS <br>
<br>
<br>
<br>
In the following PWM model, <br>
If I set the XT mode/1.8432 MIPS in 'master' block, building of HEX code is OK, but errors occured when HEX code import to MPLAB and also in programming process.<br>
<br>
If I set the XT with PLL mode, building and programming are both OK, but actual output period is not equal to the value which set in the model. <br>
<br>
So is there any problem in configuration? <br>
<br>
<br>
<br>
Thanks,<br>
<br>
Gladiac</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/162-model.jpg">Pièce jointe : model.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/163-error.jpg">Pièce jointe : error.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/164-error1.jpg">Pièce jointe : error1.jpg</a></p>
</article>

<article class="forum-post" id="p642">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-18 12:55 UTC">2008-12-18 12:55 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body">Hi Gladiac,<br>
<br>
<br>
<br>
This look like a bug !<br>
<br>
Could you :<br>
<br>
- Upload the simulink model<br>
<br>
- precise your matlab version<br>
<br>
- Precise your C30 compiler version<br>
<br>
- Precise the MPLAB version<br>
<br>
<br>
<br>
I will have a look.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p643">
<header><strong>gladiac</strong><time datetime="2008-12-18 13:41 UTC">2008-12-18 13:41 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body">OK. This is model, and MATLAB is 2007b,C30 is 3.11B, MPLAB is 8.0.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/165-PWM.mdl">Pièce jointe : PWM.mdl</a></p>
</article>

<article class="forum-post" id="p644">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-18 14:34 UTC">2008-12-18 14:34 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : gladiac</header>If I set the XT mode/1.8432 MIPS in 'master' block, building of HEX code is OK, but errors occured when HEX code import to MPLAB and also in programming process.</blockquote><br>
<br>
I do not get this error with MPLAB 8.10.<br>
<br>
Could you upgrade to this mplab and try ?<br>
<br>
<br>
<br>
You could have a look on the configurations bits once the .hex is loaded in MPLAB. (Configure ==&gt; Configuration bits)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p646">
<header><strong>gladiac</strong><time datetime="2008-12-18 17:56 UTC">2008-12-18 17:56 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I still get the same error. And I have checked the config bits, the oscillator is set incorrect, I set XT mode but it's ECIO w/PLL. I use 30f6014A device, MTALB 2007b, 0.99a toolbox,  C 30 3.11b compiler and MPLAB V8.1.<br>
<br>
<br>
<br>
Thanks.<br>
<br>
gladiac</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/167-1.jpg">Pièce jointe : 1.jpg</a></p>
</article>

<article class="forum-post" id="p653">
<header><strong>gladiac</strong><time datetime="2009-01-06 10:34 UTC">2009-01-06 10:34 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I know the reason. Your toolbox support 30f6014 correctly, may be not for 30f6014A. I found that the setups of config bits are different for 30f6014 and 30f6014A in MPLAB. They are not compatible. So can you add the support of 30f6014A individually? I think this also might be the solution for my problem of the controller design which I mentioned before.Thanks very much. <br>
<br>
<br>
<br>
Cheers,<br>
<br>
Gladiac</div>
</article>

<article class="forum-post" id="p658">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 09:21 UTC">2009-01-07 09:21 UTC</time></header>
<h3>Re: Oscillator mode  &amp;amp; MIPS configuration</h3>
<div class="forum-post-body">The following chips were added :  30f6010 ; 30f6011A ; 30f6012A ; 30f6013A ; 30f6014A. Theses changes will be available in the next release version (0.99b)<br>
<br>
<br>
<br>
It solved this problem.</div>
</article>

