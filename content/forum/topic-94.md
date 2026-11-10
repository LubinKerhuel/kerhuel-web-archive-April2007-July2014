---
title: "Encoder interface?"
url: "/forum/topic/94/"
archiveKind: "topic"
---
# Encoder interface?

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p253">
<header><strong>jebobrow</strong><time datetime="2008-02-29 18:09 UTC">2008-02-29 18:09 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
 My students and I could really use an encoder interface to the dsPics.  Do you have any plans to develop this block?  Thank you<br>
<br>
Jim Bobrow</div>
</article>

<article class="forum-post" id="p254">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-01 17:16 UTC">2008-03-01 17:16 UTC</time></header>
<h3>Re: Quadrature Encoder interface? (QEI)</h3>
<div class="forum-post-body">Hi Jim,<br>
<br>
<br>
<br>
I will be honest: the Quadrature Encoder Interface (QEI) Peripheral is not in my road map yet. I did not use it yet and I am not planning to use it in the near future.<br>
<br>
So, I will add it to the blockset if I get some free time to do it, or if many guys ask for it.<br>
<br>
<br>
<br>
Note however that you could write your own driver for the QEI Peripheral and interface this driver with simulink using the "<a href="/RTWdsPIC/Blocks/CFunctionCall.html">C Function Call</a>" block, provided with the registered version of the blockset.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p255">
<header><strong>jebobrow</strong><time datetime="2008-03-02 00:21 UTC">2008-03-02 00:21 UTC</time></header>
<h3>Re: Encoder interface?</h3>
<div class="forum-post-body">Thanks.  We will attempt to use the c function interface for our QEI. Jim</div>
</article>

<article class="forum-post" id="p623">
<header><strong>Simon_says</strong><time datetime="2008-12-04 23:27 UTC">2008-12-04 23:27 UTC</time></header>
<h3>Re: Encoder interface?</h3>
<div class="forum-post-body">Please, add the QEI block!!!!!!!!<br>
<br>
<br>
<br>
 Thanks!</div>
</article>

