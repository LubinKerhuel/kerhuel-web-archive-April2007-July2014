---
title: "Compilation error using 2 Interrupt driven blocks"
url: "/forum/topic/203/"
archiveKind: "topic"
---
# Compilation error using 2 Interrupt driven blocks

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p762">
<header><strong>MHuy</strong><time datetime="2009-02-18 01:37 UTC">2009-02-18 01:37 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I try to send some information by SPI with two “Interrupt driven” blocks (which work on the same spi).<br>
<br>
The problem is that these blocks can't have different numbers of trame (otherwise it will cause a compilation error). <br>
<br>
<br>
<br>
In the example, the instantiation looks like :<br>
<br>
extern unsigned volatile int SPI1Buffer_Receive[2];<br>
<br>
extern unsigned volatile int SPI1Buffer_Send[2];<br>
<br>
extern unsigned volatile int SPI1InterruptIdx;<br>
<br>
extern unsigned volatile int SPI1Buffer_Receive[1];<br>
<br>
extern unsigned volatile int SPI1Buffer_Send[1];<br>
<br>
…and there is thus an error in the compilation.<br>
<br>
<br>
<br>
A solution would be to have all blocks with the same number of trame. <br>
<br>
However, it will send “0U” for each unconnected signal and there will be a lost  of performance.<br>
<br>
<br>
<br>
Is there another solution?<br>
<br>
<br>
<br>
Michael</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/207-test_2_SPI.mdl">Pièce jointe : test_2_SPI.mdl</a></p>
</article>

<article class="forum-post" id="p798">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-23 21:56 UTC">2009-03-23 21:56 UTC</time></header>
<h3>Re: Compilation error using 2 Interrupt driven blocks</h3>
<div class="forum-post-body">Hi Michael,<br>
<br>
<br>
<br>
As far as I remember, It is not possible to place two interrupt driven SPI block. Even it compilation is Ok, the behaviour will not be Ok. You will not get the requested results.<br>
<br>
<br>
<br>
It is difficult to imagine a solution with a possibility to have two SPI driven block. It may be possible on one SPI driven block to add an entry for each input to activate or inactivate this entry during the next time step. However, that would add complexity for using the block, and I am not sure of the benefits that it would provide.<br>
<br>
<br>
<br>
You may try using non driven SPI blocks. The other solution would be to use the custom C function call and to add your own interrupt code. <br>
<br>
<br>
<br>
If it is a show stopper, could you explain what is it for. It would help to think about one solution...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p807">
<header><strong>MHuy</strong><time datetime="2009-04-06 09:55 UTC">2009-04-06 09:55 UTC</time></header>
<h3>Re: Compilation error using 2 Interrupt driven blocks</h3>
<div class="forum-post-body">I m now using the non driven SPI block and it works perfectly.<br>
<br>
<br>
<br>
Thanks for your help!<br>
<br>
<br>
<br>
Michael</div>
</article>

