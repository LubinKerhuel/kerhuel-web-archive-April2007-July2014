---
title: "dsPIC33fj256710A programming on explorer 16 board"
url: "/forum/topic/409/"
archiveKind: "topic"
---
# dsPIC33fj256710A programming on explorer 16 board

Forum : [dsPIC Peripherals](/forum/#forum-9)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1595">
<header><strong>flash87</strong><time datetime="2011-06-03 06:49 UTC">2011-06-03 06:49 UTC</time></header>
<div class="forum-post-body">Hello everybody,<br>
<br>
I'm a masters student currently doing a biomedical project. I purchased a dsPIC33fj256GP710A processor to do signal processing for an ECG application. My objective is to do feature extraction for an ecg signal using this board. Can anybody provide me some help regarding this topic as I'm completely new to this topic. I have installed the embedded real time workshop for microchip dsPIC developed by  Mr.Lubin Kerhuel as this simulink blockset generates a hex code directly when the blocks have been simulated in simulink.<br>
<br>
Q1.I'd like to know how exactly can i use this simulink blockset ,signal processing blockset plus the wavelet blockset available in simulink ?<br>
<br>
Can anybody out there provide me an overview as to how i should go about in generating the hex file for the dsPIC pertaining to my ECG application.Also,please tell me which are the blocks  I need to use from the explorer 16 board in tandem with the discrete wavelet transform block.<br>
<br>
Q2.How can we provide the ECG input from the matlab workspace to this new model as an input?<br>
<br>
<br>
<br>
I'm attaching the simulink model with this post.please help me out as the deadline for my project is fastly approaching.<br>
<br>
<br>
<br>
Expecting a quick response from any person out there<br>
<br>
Thanks<br>
<br>
<br>
<br>
Sahajhaksh</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/420-sahaj_dsPIC.jpg">Pièce jointe : sahaj_dsPIC.jpg</a></p>
</article>

<article class="forum-post" id="p1599">
<header><strong>flash87</strong><time datetime="2011-06-08 05:45 UTC">2011-06-08 05:45 UTC</time></header>
<h3>Re: dsPIC33fj256710A programming on explorer 16 board</h3>
<div class="forum-post-body">Hello,<br>
<br>
Anybody out there please reply to my post as quickly as possible,as my project deadline is fastly approaching.</div>
</article>

<article class="forum-post" id="p1630">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-27 23:05 UTC">2011-06-27 23:05 UTC</time></header>
<h3>Re: dsPIC33fj256710A programming on explorer 16 board</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : flash87</header>Q1.I'd like to know how exactly can i use this simulink blockset ,signal processing blockset plus the wavelet blockset available in simulink ?</blockquote> Any blocks supporting the Real Time Embedded coder (This is to say, almost all) will compile for dsPIC.<br>
<br>
However, be aware that power not infinite even with theses dsPIC thus be carefull with high computational algorithms.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : flash87</header>Q2.How can we provide the ECG input from the matlab workspace to this new model as an input?</blockquote><br>
No idea ;-), don't you have ECG amplified sensors to connect to the dsPIC ?<br>
<br>
<br>
<br>
Good luck !<br>
<br>
Lubin</div>
</article>

