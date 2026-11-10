---
title: "Question about SPI"
url: "/forum/topic/114/"
archiveKind: "topic"
---
# Question about SPI

Forum : [dsPIC Peripherals](/forum/#forum-9)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p321">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-30 22:10 UTC">2008-04-30 22:10 UTC</time></header>
<div class="forum-post-body">Hi Michal,<br>
<br>
<br>
<br>
I respond to your mail on the forum.<br>
<br>
<br>
<blockquote>Is this using internal hardware SPI module in dsPIC, or it's using softwarable SPI from blockset</blockquote><br>
It use the hardware SPI peripheral.<br>
<br>
<br>
<blockquote>If I want to use i.e. 6 SPI modules to communicate with 6 peripheral devices, but my PIC has only 2 modules, can I to do it? </blockquote><br>
Yes, Only one module is necessary to communicate with 6 peripherals devices : <br>
<br>
the three lines SCK, SDI and SDO will be common to all devices (this is the bus).<br>
<br>
Each peripheral will also be connected to a fourth line : Chip Select. Peripheral devices with their Chip Select line disable should be in high impedance on the bus.<br>
<br>
<br>
<br>
The illustration shows a typical use of the SPI block.<br>
Note the ordering connection between blocks to force the execution order.<br>
<br>
Digital Write is used to drive the Chip Select line.<br>
<br>
On, this example, we read two different data from the same chip (There is only one Chip Select line: E5)<br>
<br>
Also, note the Nop blocks that allow slowing down the start of transmission on the bus after the Chip Select line is enable. This gives time for the Chip Select line to be stable. It is safe to place the SPI logic inside a subsystem with the subsystem parameters "Treat as atomic" checked. This will force all blocks to be executed without being mixed up by execution of others blocks from the model. <br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/63-SPI_example.png">Pièce jointe : SPI_example.png</a></p>
</article>

