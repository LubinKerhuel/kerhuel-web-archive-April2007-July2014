---
title: "PIC32MX360F512L and MCP4922"
url: "/forum/topic/467/"
archiveKind: "topic"
---
# PIC32MX360F512L and MCP4922

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1769">
<header><strong>3eenab</strong><time datetime="2011-12-27 11:18 UTC">2011-12-27 11:18 UTC</time></header>
<div class="forum-post-body">hi Lubin<br>
<br>
<br>
<br>
my group have used an example that is in the forum to connect between dsPIC and DAC with some modification as shown:<br>
<br>
<br>
<br>
<a href="http://i1237.photobucket.com/albums/ff473/zajora/blocksetdac-1.jpg">Image externe (non intégrée)</a><br>
<br>
<br>
<br>
using mplab we downloaded the program and run it but no signal is reaching the DAC, when halting the program we found out that it is stucked at loop containing SPI1IF bit:<br>
<br>
<br>
<br>
<a href="http://i1237.photobucket.com/albums/ff473/zajora/pic32dac.jpg">Image externe (non intégrée)</a><br>
<br>
<br>
<br>
the connections between PIC32 and MCP4922:<br>
<br>
<br>
<br>
pin 23 (SS bar) with pin 3 (CS bar)<br>
<br>
pin 55 (SCK1) with pin 5 (SCK)<br>
<br>
pin 53 (SDO1) with pin 4 (SDI)<br>
<br>
<br>
<br>
we checked the MCP4922 with pic18 and it is fine, so we think the problem is the pic32.<br>
<br>
<br>
<br>
<br>
<br>
we changed the constant with a counter, changed the blocks configurations, grouneded the chip select on both sides, send a 3.3V to SS bar but nothing worked.<br>
<br>
<br>
<br>
what should we do now?? we hope you answer soon since the end of the semester is near.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/457-spitest2.mdl">Pièce jointe : spitest2.mdl</a></p>
</article>

<article class="forum-post" id="p1770">
<header><strong>salemimoh</strong><time datetime="2011-12-28 18:21 UTC">2011-12-28 18:21 UTC</time></header>
<h3>Re: PIC32MX360F512L and MCP4922</h3>
<div class="forum-post-body">I think the problem is with the configuration of the SPI of the PIC32 in the blockset itself. though You can configure SPI1 and compile it without error, when fired in the microcontroller it does not produce any result in fact it stops in the place mentioned in the comment. Worse still  if you try to configure SPI2 the compilation produces an error. But if you use exactly the same configuration with DSPIC it not only compile but works perfectly as well. So probably I ask kindly Lubbin if he could look at this problem probably he might find a solution.</div>
</article>

