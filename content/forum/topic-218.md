---
title: "ADC inputs yet again"
url: "/forum/topic/218/"
archiveKind: "topic"
---
# ADC inputs yet again

Forum : [dsPIC Peripherals](/forum/#forum-9)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p821">
<header><strong>Bernard Leak</strong><time datetime="2009-04-14 14:52 UTC">2009-04-14 14:52 UTC</time></header>
<div class="forum-post-body">It has been some months since I last picked up a new copy of the block-set, and the latest<br>
<br>
version seems to have broken something which once worked.<br>
<br>
<br>
<br>
The default behaviour seems to be to leave all analogue input pins configured for<br>
<br>
analogue input.  Explicitly putting a digital I/O block in a model would set bits in the<br>
<br>
AD[12]PCFG[HL] registers to disable them as analogue inputs.  In the past, I have<br>
<br>
used digital input blocks driving terminator blocks. to ensure that I could use the<br>
<br>
associated pin as a digital I/O pin (in code not visible in the Simulink model diagram).<br>
<br>
This no longer works.<br>
<br>
<br>
<br>
The analogue pins I am using are all in AN16-31 (so they are configured<br>
<br>
in AD1PCFGH).  The list is [ 16 17 18 19 20 22 23 24 25 26 ].<br>
<br>
I am using AN27-AN31 as digital inputs.  Whereas AD1PCFGH used<br>
<br>
to be set (correctly) to 0xF800, it is now left as 0 (the default state<br>
<br>
at start-up).<br>
<br>
<br>
<br>
There has been some change in this area: in fact, I used to see compiler<br>
<br>
warnings about 16-bit shifts on 16-bit quantities.</div>
</article>

<article class="forum-post" id="p827">
<header><strong>Bernard Leak</strong><time datetime="2009-04-16 10:38 UTC">2009-04-16 10:38 UTC</time></header>
<h3>Re: ADC inputs yet again</h3>
<div class="forum-post-body">Here's a tiny illustrative model.  This one shows the problem even though<br>
<br>
there is no ADC input at all!<br>
<br>
<br>
<br>
On this CPU (dsPIC33FJ256GP710) the digital I/O pins given are<br>
<br>
also analogue inputs (numbered as labelled).  At power-on, all the<br>
<br>
analogue input pins are configured as ADC inputs by default,<br>
<br>
represented by 0 bits in the ADxPCFGL and AD1PCFGH registers.<br>
<br>
The generated dummy.c file has all the appropriate details.<br>
<br>
TRISE is (correctly) left with all bits set, so all the pins are inputs.<br>
<br>
However, AD1PCFGH is left with all bits clear, so AN16-AN31<br>
<br>
are configured as analogue inputs only; port read input is disabled,<br>
<br>
so the actual state of the pin isn't read.<br>
<br>
<br>
<br>
AD1PCFGL and AD2PCFGL are explicitly (and redundantly)<br>
<br>
set to their default value of 0.  This guarantees that the<br>
<br>
same problem will also affect AN0-AN15 (it so happens that<br>
<br>
I wasn't using any of these as inputs).</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/232-dummy.mdl">Pièce jointe : dummy.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/233-dummy.c">Pièce jointe : dummy.c</a></p>
</article>

<article class="forum-post" id="p828">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-17 17:14 UTC">2009-04-17 17:14 UTC</time></header>
<h3>Re: ADC inputs yet again</h3>
<div class="forum-post-body">Thanks again for this clear bug description with simulin example.It really helped to track it !<br>
<br>
<br>
<br>
the bug is corrected and the corrected blockset version will be available in the next blockset version (following version 0.99c)<br>
<br>
<br>
<br>
Lubin</div>
</article>

