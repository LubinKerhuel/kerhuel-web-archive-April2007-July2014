---
title: "Alignment of DMA memory for ADC corrupts"
url: "/forum/topic/566/"
archiveKind: "topic"
---
# Alignment of DMA memory for ADC corrupts

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1970">
<header><strong>bmairs</strong><time datetime="2012-12-17 22:57 UTC">2012-12-17 22:57 UTC</time></header>
<div class="forum-post-body">Using the ADC inputs in a model generated a dsPIC_DMA_Buffers.c file that has the following line:<br>
<pre><code>volatile uint16_T ADCBuffChannelDMA[(2)] __attribute__((space(dma),aligned(256)));</code></pre><br>
<br>
The problem with this is it can cause problems with other DMA uses if those aren't aligned to 256 as well. I can't think of any reason for this being necessary, can it be removed so it doesn't cause these problems?</div>
</article>

