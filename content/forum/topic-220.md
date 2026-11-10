---
title: "Problem with Nop blocks"
url: "/forum/topic/220/"
archiveKind: "topic"
---
# Problem with Nop blocks

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p832">
<header><strong>laurent841</strong><time datetime="2009-04-21 08:16 UTC">2009-04-21 08:16 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I have some problems using Nop blocks. It seems that they aren't taken into account, even if I put values like 4000000 (1 second for my 4.00 MIPS configuration). It works fine when I use the Microchip C funtion Delay instead of Nop blocks, but I would like to use Nop blocks for very small delays.<br>
<br>
<br>
<br>
Does anybody encountered the same problem ?<br>
<br>
<br>
<br>
Thank you in advance,<br>
<br>
<br>
<br>
Laurent</div>
</article>

<article class="forum-post" id="p834">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-21 18:54 UTC">2009-04-21 18:54 UTC</time></header>
<h3>Re: Problem with Nop blocks</h3>
<div class="forum-post-body">Hi Laurent,<br>
<br>
<br>
<br>
The Nop Block must be placed between two others blocks, and connected on the ordering input/output of theses two blocks.<br>
<br>
<br>
<br>
Post the simulink model if you have problems. Anyway, it is not adapted for 1s delay. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p835">
<header><strong>laurent841</strong><time datetime="2009-04-24 13:42 UTC">2009-04-24 13:42 UTC</time></header>
<h3>Re: Problem with Nop blocks</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
In fact I use Nop blocks for SPI communication,in order to respect waiting delays that are imposed. For 4.00 MIPS, when I put a block of 40 Nop (10 µs) between two SPI readings, delays are not taken into account when running the model on my dsPIC33. On the other hand, it does work fine when I use a C function call block that calls the function Delay(int), provided by Mirochip.<br>
<br>
<br>
<br>
I don't understand why Nop blocks are not taken into account by the dsPIC. I join you a part of the model in order to illustrate the use of a Nop block.<br>
<br>
<br>
<br>
Thank you for your help,<br>
<br>
Kind regards,<br>
<br>
<br>
<br>
Laurent</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/235-Nop-block.JPG">Pièce jointe : Nop-block.JPG</a></p>
</article>

<article class="forum-post" id="p844">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-06 22:04 UTC">2009-05-06 22:04 UTC</time></header>
<h3>Re: Problem with Nop blocks</h3>
<div class="forum-post-body">Hi Laurent,<br>
<br>
<br>
<br>
That is strange as I use the nop function and it seems to work.<br>
<br>
Could you post the .mdl file please ?<br>
<br>
Did you loocked in the generated C file ? <br>
<br>
<br>
<br>
Perhaps the compiler optimisation configuration removes nop instruction ?</div>
</article>

