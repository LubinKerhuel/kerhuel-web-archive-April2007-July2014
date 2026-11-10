---
title: "Correct use of UART peripheral"
url: "/forum/topic/354/"
archiveKind: "topic"
---
# Correct use of UART peripheral

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1454">
<header><strong>BenUL</strong><time datetime="2011-02-01 16:25 UTC">2011-02-01 16:25 UTC</time></header>
<div class="forum-post-body">Hello<br>
<br>
I am a university student very new to programming. I am trying to interact with the SRF02 sonar rangefinder for use as an altimeter on a UAV, and currently using the UART to communicate with it, through a dsPIC30F4013. (I am aware that it supports I2C also, but the unit is currently wired for serial connections) I simply want to send two bytes of information, firstly the address of the sonar, then a command to do the ranging, which this unit does all in one. However I am unsure of the correct proceedure for doing so, at the moment I am sending  constants to the UART TX block only. Any help with this would be greatly appreciated.<br>
<br>
<br>
<br>
Ben</div>
</article>

<article class="forum-post" id="p1848">
<header><strong>Saeed</strong><time datetime="2012-03-06 00:26 UTC">2012-03-06 00:26 UTC</time></header>
<h3>Re: Correct use of UART peripheral</h3>
<div class="forum-post-body">Flex Board Blinking LED example among the presented examples of the wikki may help you through this.</div>
</article>

