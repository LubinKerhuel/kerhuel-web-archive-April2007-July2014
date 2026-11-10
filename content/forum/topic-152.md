---
title: "ADC Input block - solved"
url: "/forum/topic/152/"
archiveKind: "topic"
---
# ADC Input block - solved

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p480">
<header><strong>Bernard Leak</strong><time datetime="2008-08-26 09:04 UTC">2008-08-26 09:04 UTC</time></header>
<div class="forum-post-body">M. Kerhuel,<br>
<br>
                   there is still a problem with the ADC Input block.<br>
<br>
<br>
<br>
For dsPIC33FJ256GP710, it gives the permitted<br>
<br>
analogue input pins as 0-21 and 24-33, instead of<br>
<br>
0-31 (which is certainly correct)<br>
<br>
<br>
<br>
It is as though 22 and 23 were entered as 32 and 33, and the list was<br>
<br>
then sorted into order.  Typing 22 produces a dialogue<br>
<br>
box:<br>
<br>
<br>
<br>
   RTW for PIC 16 MCU error<br>
<br>
   Subscript indices must either be real positive indices or logicals.<br>
<br>
<br>
<br>
Checking the nearest convenient data-sheet,<br>
<br>
Microchip's 70286A (covering dsPIC33FJXXXGPX06/X08/X10)<br>
<br>
whenever AN21 is present AN22 and AN23 are also present:<br>
<br>
that is, on<br>
<br>
<br>
<br>
  dsPIC33FJ{64,128}GP708<br>
<br>
  dsPIC33FJ{64,128}GP310<br>
<br>
  dsPIC33FJ256GP510<br>
<br>
  dsPIC33FJ{64,128,256}GP710<br>
<br>
<br>
<br>
all but the GP708 versions continue with<br>
<br>
pins AN24 - AN31: the GP708 stops with AN23.<br>
<br>
<br>
<br>
On the other hand, I don't actually get any input on AN22, even<br>
<br>
when I modify AD1CSSH to set the bit I want.  I don't yet<br>
<br>
understand this, and it might be relevant if I did.  It is possible<br>
<br>
that this is a problem with the hardware (or my understanding<br>
<br>
of it), but I thought I should mention it.<br>
<br>
<br>
<br>
Bernard Leak</div>
</article>

<article class="forum-post" id="p482">
<header><strong>Bernard Leak</strong><time datetime="2008-08-28 16:06 UTC">2008-08-28 16:06 UTC</time></header>
<h3>Re: ADC Input block</h3>
<div class="forum-post-body">Dear List,<br>
<br>
                   I am using version 0.98fb of the dsPIC block-set,<br>
<br>
dated 21st August 2008, for MatLab R2006b.<br>
<br>
<br>
<br>
The list picRef.AN is wrong: it contains spurious<br>
<br>
NaNs at indices 23 and 24 (1-based: 22 and 23 if 0-based)<br>
<br>
which cause AN22 and AN23 to "vanish", and all<br>
<br>
higher-numbered analogue pins to be numbered<br>
<br>
too high by 2.  This also smashes the generation of<br>
<br>
ADPCFG in dsPIC_PortSetting.m .<br>
<br>
<br>
<br>
Bernard Leak</div>
</article>

<article class="forum-post" id="p485">
<header><strong>malife</strong><time datetime="2008-08-31 17:45 UTC">2008-08-31 17:45 UTC</time></header>
<h3>Re: ADC Input block</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I would also add to Bernard's post on the ADC the following bug:<br>
<br>
<br>
<br>
I have AN channels 0-16 except for AN2 which is SPI1 SSL in 33FJ256MC710. So in the AN dialog box I have:<br>
<br>
<br>
<pre><code>[0 1 3 4 5 6 7 8 9 10 11 12 13 15 16]</code></pre><br>
<br>
Just for the sake of completeness I have a digital output block set with infinite sample time (so it just happens once) to high.<br>
<br>
<br>
<br>
But regardless of that the generated code is as follows:<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;/* Configuration ADCHS */
  AD1PCFGL = (0&amp; 65535);
  AD2PCFGL = (0&amp; 65535);
  AD1PCFGH = ((0 &gt;&gt; 16) &amp; 65535);
<wbr>
  /* blocks with infinite sample periods */
<wbr>
  /* S-Function "dsPIC_Digital_OutputWrite" Block: &lt;Root&gt;/Drive SSL High */
  LATBbits.LATB2 = TRUE;
</code></pre><br>
<br>
Which clearly ignores the fact that the ADxPCFGx bit 2 must be set to 1, in order to make B2 a digital pin. No show-stopper now that I know what the problem is but took me quite some time to figure out what was wrong :-).<br>
<br>
<br>
<br>
Thanks, and I hope this gets corrected in the next version.</div>
</article>

<article class="forum-post" id="p494">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-01 20:50 UTC">2008-09-01 20:50 UTC</time></header>
<h3>Re: ADC Input block - bug to solve</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Bernard Leak</header>there is still a problem with the ADC Input block.<br>
<br>
<br>
<br>
Bernard, For dsPIC33FJ256GP710, it gives the permitted<br>
<br>
analogue input pins as 0-21 and 24-33, instead of<br>
<br>
0-31 (which is certainly correct)</blockquote><br>
<br>
Thanks Bernard for this bug report. The definition (inside the blockset) for the dsPIC33FJxxxGP710 family has an error that may cause problems for ADC pins above 21. It is now corrected in the version 0.98fc of the blockset.<br>
<br>
<br>
<br>
----<br>
<br>
Malife,<br>
<br>
I find a bug that may affect all PIC or dsPIC on the ADC block that may cause the trouble described.<br>
<br>
The correction added in the version 0.98fc should solve it.<br>
<br>
This bug has also been reported by Peter but by email.<br>
<br>
<br>
<br>
<br>
<br>
Thanks for theses bug descriptions.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p500">
<header><strong>Bernard Leak</strong><time datetime="2008-09-03 13:49 UTC">2008-09-03 13:49 UTC</time></header>
<h3>Re: ADC Input block - solved</h3>
<div class="forum-post-body">Thanks: all my problems with the ADC block are now with the hardware!</div>
</article>

