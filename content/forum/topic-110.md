---
title: "Request Support for DSPIC33FJ64(128)MC802"
url: "/forum/topic/110/"
archiveKind: "topic"
---
# Request Support for DSPIC33FJ64(128)MC802

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

10 message(s) · archive en lecture seule

<article class="forum-post" id="p299">
<header><strong>malife</strong><time datetime="2008-04-24 17:22 UTC">2008-04-24 17:22 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 Microchip has recently started sampling the DSPIC33FJ64MC802 and the DSPIC33FJ128MC802, to become their smallest chips with DMA available (28 pins) and they are conveniently available in PDIP package which makes them easy to prototype. <br>
<br>
<br>
<br>
Would you be so kind to have those chips available in the library? Don't worry about implementing anything of the DMA I will try to do that with the C function call block :-) .<br>
<br>
<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p300">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-24 22:00 UTC">2008-04-24 22:00 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
Thanks for that info. I did not update my dsPIC list from a while now. <br>
<br>
I will have a look soon and will try to get samples from Microchip.<br>
<br>
When are you planning to use theses parts ? (are you waiting for the update of the dsPIC toolbox ?)<br>
<br>
<br>
<br>
Anyway, note that the ECAN peripheral is still not supported. (CAN peripheral is supported on others dsPIC)<br>
<br>
 <br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p305">
<header><strong>malife</strong><time datetime="2008-04-25 14:16 UTC">2008-04-25 14:16 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I will not be using them immediately. Right now I am using the 33F256MC710 which is on the opposite side of the scale (their biggest chip) and is fully supported by your blockset,  but certainly as soon as you support these new parts I will start using them for a side project I am working on. I have requested samples and they should be arriving by the end of next week.<br>
<br>
<br>
<br>
Also, I might be mistaken, but I was under the impression that you can operate any ECAN engine with the standard CAN libraries. I.E. I think you should be able to use any chip with ECAN as if it had CAN, the main differences are only in timing. You can read in Microchip's CAN FAQ about it <a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=2009&amp;param=en001003">http://www.microchip.com/stellent/idcpl ... m=en001003</a> and also the App note AN916 talks about it (<a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1824&amp;appnote=en012161">http://www.microchip.com/stellent/idcpl ... e=en012161</a>)<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p306">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-26 12:37 UTC">2008-04-26 12:37 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : malife</header>ECAN engine with the standard CAN libraries. I.E. I think you should be able to use any chip with ECAN as if it had CAN, the main differences are only in timing</blockquote><br>
<br>
When I looked how I could adapt the C code written for CAN driver to the ECAN driver, it seems that there are many differences. I think that ECAN use DMA only, CAN do not.<br>
<br>
The document you provide explain what are the advantages of ECAN versus CAN. Also, CAN and ECAN module are compatible in the way that you can connect a PIC30f CAN peripheral to a PIC33f ECAN perpheral; they will be able to communicate...<br>
<br>
<br>
<br>
Adapting the CAN block to build a new ECAN block for simulink is still a piece of work. I am willing to do it but I am not able to provide you with a date yet.<br>
<br>
When are you willing to use it ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p312">
<header><strong>malife</strong><time datetime="2008-04-26 16:37 UTC">2008-04-26 16:37 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Thanks Lubin for pointing that out. If I use this small chip (the 28-pin one) most likely I will not be needing ECAN (or CAN) but rather just serial, SPI, ADC, etc... So at least on my side I have no particular hurry for ECAN device support. For the  710 (the big one) CAN(ECAN) willl be a feature that I will provide as an extensibility feature (i.e. periphereals will connect with the main AP via CAN) but I do not foresee using this in at least six months. I would much rather see the SPI go interrupt based (as the serial did, Thanks!! :-) ) although I will be working on my side to try to get DMA to work with SPI using C-function call block.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p340">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-12 21:17 UTC">2008-05-12 21:17 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
I am wondering to do some modification to the SPI module to get an interrupt driven SPI block.<br>
<br>
My ideas are clear now on how I am going to do it.<br>
<br>
It may be usefull to know more precisely how you want to use it in order to check that  my implementation will fit your needs. I may addapt it otherwise...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p342">
<header><strong>malife</strong><time datetime="2008-05-13 00:07 UTC">2008-05-13 00:07 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 That sounds great! I have two dsPICs in a UAV autopilot, one is the sensor MCU and the other is the control, both will exchange information between them using SPI clocked as fast as I can get it to work. One is the master and the other is the slave (obviously :-) ). I am planning on using 4 wires mode, i.e. (SDI, SDO, SCK and SSL).<br>
<br>
<br>
<br>
 Also I've been working today all day in trying to get SPI DMA to work. I've made some progress but are not quite there yet. I will try to set up an example, and as usual as soon as I have it and test it, I will post it here to enrich the examples pool. Also, you should consider setting up a section where users can upload examples :-) because right now they are all over the forum instead of one single location. I think it would help out the new users to figure out the blockset and look at somebody else's work. An will also help seasoned users to see different ways of doing the same thing.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p579">
<header><strong>MHuy</strong><time datetime="2008-10-20 15:39 UTC">2008-10-20 15:39 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hi Lubin, <br>
<br>
<br>
<br>
I would like to know if support for the dsPIC33FJ128MC802/202 will be available soon?<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p580">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-20 22:54 UTC">2008-10-20 22:54 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Hi Mikael,<br>
<br>
<br>
<br>
I get a 33FJ128GP802 from microchip.<br>
<br>
The "Pin mapping" that is present on theses chips  is not supported yet by the blockset. I'll have a look.<br>
<br>
Provided it's simple, it may take few weeks to adapt ; I'll try to do it within two weeks. If it is not done within two weeks, considere that it will not be available before 2 or 3 months.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p593">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-28 19:51 UTC">2008-10-28 19:51 UTC</time></header>
<h3>Re: Request Support for DSPIC33FJ64(128)MC802</h3>
<div class="forum-post-body">Partly Done :<br>
<br>
<br>
<br>
Experimental version is available.<br>
<br>
Go to release note : <a href="/wiki/release-notes/">http://archive.kerhuel.eu/wiki/Release_Note ... 4a30be2655</a><br>
<br>
<br>
<br>
PWM motor do not work on MC familly just added !<br>
<br>
<br>
<br>
Lubin</div>
</article>

