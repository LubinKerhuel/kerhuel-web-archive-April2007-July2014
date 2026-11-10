---
title: "Possible Bug in ADC in 33FJ256MC710"
url: "/forum/topic/132/"
archiveKind: "topic"
---
# Possible Bug in ADC in 33FJ256MC710

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p402">
<header><strong>malife</strong><time datetime="2008-05-29 00:12 UTC">2008-05-29 00:12 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I am trying to use the 12-bit ADC block in the 33FJ256MC710, I drop the block and select channels 0-7 and I get the following error when I compile:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;SPIMasterNoDMA.c:167: error: 'ADC1BUF1' undeclared (first use in this function) 
SPIMasterNoDMA.c:167: error: (Each undeclared identifier is reported only once 
SPIMasterNoDMA.c:167: error: for each function it appears in.) 
SPIMasterNoDMA.c:168: error: 'ADC1BUF2' undeclared (first use in this function) 
SPIMasterNoDMA.c:169: error: 'ADC1BUF3' undeclared (first use in this function) 
SPIMasterNoDMA.c:170: error: 'ADC1BUF4' undeclared (first use in this function) 
SPIMasterNoDMA.c:171: error: 'ADC1BUF5' undeclared (first use in this function) 
SPIMasterNoDMA.c:172: error: 'ADC1BUF6' undeclared (first use in this function) 
SPIMasterNoDMA.c:173: error: 'ADC1BUF7' undeclared (first use in this function)
</code></pre><br>
<br>
Could you please advise what am I doing wrong?<br>
<br>
<br>
<br>
Thanks<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p403">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-29 07:14 UTC">2008-05-29 07:14 UTC</time></header>
<h3>Re: Possible Bug in ADC in 33FJ256MC710</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
This is a bug ! Thanks for reporting.<br>
<br>
<br>
<br>
A quick glance at the doc of the 33F256MC710 : I find only one buffer register for the ADC of this PIC. It seems that DMA data transfert must be used if you are doing more than one ADC conversion.<br>
<br>
<br>
<br>
I have idea to workaround that problem. <br>
<br>
<br>
<br>
I guess that I am getting into DMA to make it works !<br>
<br>
<br>
<br>
I try to look at it next week.<br>
<br>
<br>
<br>
Lubin</div>
</article>

