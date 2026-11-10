---
title: "Heap can't be configured for MPLAB"
url: "/forum/topic/479/"
archiveKind: "topic"
---
# Heap can't be configured for MPLAB

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1826">
<header><strong>bmairs</strong><time datetime="2012-02-08 19:22 UTC">2012-02-08 19:22 UTC</time></header>
<div class="forum-post-body">If you specify a heap size for your project in Simulink under Code Generation-&gt;DsPIC options-&gt;LDFLAGS then this same setting won't apply to the generated MPLAB 8 project and you'll need to manually specify a heap size. This means that the default project created by your blockset when a heap is specified doesn't compile.</div>
</article>

<article class="forum-post" id="p1884">
<header><strong>LubinKerhuel</strong><time datetime="2012-04-27 00:34 UTC">2012-04-27 00:34 UTC</time></header>
<h3>Re: Heap can&#x27;t be configured for MPLAB</h3>
<div class="forum-post-body">Hello Bryant,<br>
<br>
<br>
<br>
The compiler's parameters are not reported to the MPLAB project.<br>
<br>
Thus you are completly true this is a problem.<br>
<br>
<br>
<br>
Thanks for your remark.<br>
<br>
<br>
<br>
Lubin</div>
</article>

