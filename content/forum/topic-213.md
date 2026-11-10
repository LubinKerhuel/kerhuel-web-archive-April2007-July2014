---
title: "possible bug using 2 ADC - solved"
url: "/forum/topic/213/"
archiveKind: "topic"
---
# possible bug using 2 ADC - solved

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p806">
<header><strong>MHuy</strong><time datetime="2009-04-06 09:31 UTC">2009-04-06 09:31 UTC</time></header>
<div class="forum-post-body">Hello Lubin, <br>
<br>
<br>
<br>
I try to compile this model but it doesn't work.<br>
<br>
<br>
<br>
It writes the following message in the command window. <br>
<br>
<br>
<pre><code>dsPIC_DMA_Buffers.c:3: error: syntax error before 'ADCBuffChannelDMA' 
dsPIC_DMA_Buffers.c:3: warning: data definition has no type or storage class 
gmake: *** [dsPIC_DMA_Buffers.o] Error 255 </code></pre><br>
<br>
In the file "dsPIC_DMA_Buffers.c", there is no include of "test_ADC_private.h" (NameOfTheModel_private.h) where the variable ADCBuffChannelDMA as the type extern.<br>
<br>
<br>
<pre><code>//dsPIC_DMA_Buffers.c
#include "p33fxxxx.h"
<wbr>
volatile uint16_T ADCBuffChannelDMA[(2)] __attribute__((space(dma),aligned(256)));</code></pre><br>
<br>
<pre><code>//test_ADC_private.h
extern volatile uint16_T ADCBuffChannelDMA[(2)] __attribute__((space(dma),aligned(256)));</code></pre><br>
<br>
Does the compilation error come from that problem? or do you have an other idea?<br>
<br>
<br>
<br>
Thanks for your help!<br>
<br>
<br>
<br>
Michael<br>
<br>
<br>
<br>
PS : I use the dsPIC33FJ128GP802 chip.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/230-test_ADC.mdl">Pièce jointe : test_ADC.mdl</a></p>
</article>

<article class="forum-post" id="p809">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-07 08:32 UTC">2009-04-07 08:32 UTC</time></header>
<h3>Re: possible bug using 2 ADC</h3>
<div class="forum-post-body">Which blockset version are you working with  ? (0.99c ?)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p810">
<header><strong>MHuy</strong><time datetime="2009-04-07 09:32 UTC">2009-04-07 09:32 UTC</time></header>
<h3>Re: possible bug using 2 ADC</h3>
<div class="forum-post-body">I use the 0.99b, is it working with the 0.99c?</div>
</article>

<article class="forum-post" id="p812">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-07 22:54 UTC">2009-04-07 22:54 UTC</time></header>
<h3>Re: possible bug using 2 ADC</h3>
<div class="forum-post-body">I corrected a bug similar to this one just before publishing the 0.99c version.<br>
<br>
I thought that this bug was not present yet in the 0.99b, but it may be the same. <br>
<br>
<br>
<br>
Anyway, could you test your model using the 0.99c version ?<br>
<br>
(Note that the 0.99c version on the website is depicted as 0.99b+ at the matlab command "ver". That is the last bug I found ! not really important...)<br>
<br>
<br>
<br>
Let me know if you still have this bug...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p814">
<header><strong>MHuy</strong><time datetime="2009-04-09 08:56 UTC">2009-04-09 08:56 UTC</time></header>
<h3>Re: possible bug using 2 ADC</h3>
<div class="forum-post-body">There is no more bug with the v0.99c!<br>
<br>
<br>
<br>
Thanks for your help Lubin<br>
<br>
<br>
<br>
Michael</div>
</article>

