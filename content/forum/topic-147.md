---
title: "ADC: some problems (revisited)"
url: "/forum/topic/147/"
archiveKind: "topic"
---
# ADC: some problems (revisited)

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p465">
<header><strong>Bernard Leak</strong><time datetime="2008-08-15 16:18 UTC">2008-08-15 16:18 UTC</time></header>
<div class="forum-post-body">A previous post of mine seems to have vanished!  In any case, it was out-of-date.<br>
<br>
My company (add2) paid on 1st May for an unlimited version of the dsPIC block-set.<br>
<br>
The current release notes suggest that changes to the ADC Input block have removed<br>
<br>
several problems I had seen.  I'm eager to try it .. but how do I actually get updated<br>
<br>
versions of the unlimited block-set?<br>
<br>
<br>
<br>
In brief, my problems were...<br>
<br>
(a) The restriction to ADC1  (this may still be there, and is not good for my employer)<br>
<br>
(b) ADC1BUF1 ADC1BUF2 ... were being used in the generated code, but only<br>
<br>
     ADC1BUF0 was declared in the Microchip header file.  This seems to have been repaired<br>
<br>
    in V0.98b.<br>
<br>
(c) The list of analogue pins available to the ADC was wrong (and generated<br>
<br>
     strange errors).  Specifically, AN22 and AN23 seem to have been<br>
<br>
     given as AN32 and AN33 in the list (for dsPIC33FJ128GP710, as it<br>
<br>
    happens).  This seems to have been repaired in V0.98d.<br>
<br>
<br>
<br>
... and thanks for giving us time offsets as well as rates in V0.95b!<br>
<br>
<br>
<br>
Bernard.</div>
</article>

<article class="forum-post" id="p466">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-16 07:53 UTC">2008-08-16 07:53 UTC</time></header>
<h3>Re: ADC: some problems (revisited)</h3>
<div class="forum-post-body">hi Bernard,<br>
<br>
<br>
<br>
I send update on the blockset on simple mail request. (until I find a way to send to everybody the update at once !)<br>
<br>
<br>
<br>
I am currently on vacation until 1st of september, I will see if I can send you an update earlier.<br>
<br>
<br>
<br>
Lubin</div>
</article>

