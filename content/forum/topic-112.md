---
title: "CAN module with dspic33fj256gp710 or pic24fj128ga010"
url: "/forum/topic/112/"
archiveKind: "topic"
---
# CAN module with dspic33fj256gp710 or pic24fj128ga010

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p315">
<header><strong>mhiernaux</strong><time datetime="2008-04-28 19:25 UTC">2008-04-28 19:25 UTC</time></header>
<div class="forum-post-body">Hi everyone,<br>
<br>
<br>
<br>
I've tried using the CAN block with the dspic33fj256gp710 and it says error, no CAN peripheral on 33fj256gp710. <br>
<br>
<br>
<br>
Does anyone know how to activate the module/bypass the error ? Because the pic does indeed have 2 can modules.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Martin</div>
</article>

<article class="forum-post" id="p316">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-28 20:07 UTC">2008-04-28 20:07 UTC</time></header>
<h3>Re: CAN module with dspic33fj256gp710 or pic24fj128ga010</h3>
<div class="forum-post-body">Hi Martin,<br>
<br>
<br>
<br>
33f pic family endowed with a CAN module have the ECAN peripheral implemented.<br>
<br>
As mentionned in the release note, ECAN is not support yet. Only te CAN peripheral is supported so far.<br>
<br>
ECAN peripheral is on the road map...<br>
<br>
The fastest and easiest way to implement the ECAN driver is to use the "C call function block" from the blockset and to write your own c driver for the ECAN peripheral.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p318">
<header><strong>mhiernaux</strong><time datetime="2008-04-29 06:06 UTC">2008-04-29 06:06 UTC</time></header>
<h3>Re: CAN module with dspic33fj256gp710 or pic24fj128ga010</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks a lot for your answer. I'll use the C call.<br>
<br>
<br>
<br>
Keep up the good work !<br>
<br>
Martin</div>
</article>

<article class="forum-post" id="p344">
<header><strong>malife</strong><time datetime="2008-05-13 00:18 UTC">2008-05-13 00:18 UTC</time></header>
<h3>Re: CAN module with dspic33fj256gp710 or pic24fj128ga010</h3>
<div class="forum-post-body">Hello Martin,<br>
<br>
 In case you've gotten ECAN to work using C function calls would you mind posting about your results and maybe your model/code? In that way we can all take advantage of what is being done while Lubin catches up :-). <br>
<br>
<br>
<br>
You can read about the QEI (<a href="/forum/topic/100/">viewtopic.php?f=5&amp;t=100&amp;start=0&amp;st=0&amp;sk=t&amp;sd=a</a>) and EEPROM Emulation (<a href="/forum/topic/117/">viewtopic.php?f=6&amp;t=117#p334</a>) that I posted in case you find yourself in need of it.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

