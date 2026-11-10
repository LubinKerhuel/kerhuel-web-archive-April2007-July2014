---
title: "Missing 128ms POR delay"
url: "/forum/topic/216/"
archiveKind: "topic"
---
# Missing 128ms POR delay

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p813">
<header><strong>Bernard Leak</strong><time datetime="2009-04-08 11:44 UTC">2009-04-08 11:44 UTC</time></header>
<div class="forum-post-body">I'm not quite sure which PIC models have this.  It's not well documented.<br>
<br>
The default POR delay (FPWRT in FPOR) seems to be 128ms.  It's given like that<br>
<br>
in the MPLAB GUI (the 'Configuration bits' window), and there is a selector for this<br>
<br>
(FPWRT_PWR128) in *all* of the dsPIC33F header files.  This counts as "default"<br>
<br>
because it's what you get if the FPOR configuration register is unprogrammed<br>
<br>
(all bits set).<br>
<br>
<br>
<br>
However, it's not available in the dsPIC Master block mask, which only allows<br>
<br>
0 and powers of 2 from 1 to 64.<br>
<br>
<br>
<br>
I owe you a success story: while I was failing to write you a testimonial,<br>
<br>
we at add2 have put a product out on the market.  It's a battery simulator for<br>
<br>
(mostly) the car industry.<br>
<br>
<br>
<br>
                                                                  Bernard Leak.</div>
</article>

<article class="forum-post" id="p815">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-09 21:55 UTC">2009-04-09 21:55 UTC</time></header>
<h3>Re: Missing 128ms POR delay</h3>
<div class="forum-post-body">Hi Bernard,<br>
<blockquote><header class="quote-author">Citation : Bernard Leak</header>in *all* of the dsPIC33F header files</blockquote><br>
Ok, I believe you, (did not open all of them). But I added the 128ms to all 33f dspic (will be available in the next version , current is 0.99c).<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Bernard Leak</header>I owe you a success story: while I was failing to write you a testimonial,<br>
<br>
we at add2 have put a product out on the market. It's a battery simulator for<br>
<br>
(mostly) the car industry.</blockquote><br>
I did not get the message here ? <br>
<br>
<br>
<br>
I am still planning to write a testimonial page on the wiki, but I just have to prepare it ! Would you be the first to write on it ?<br>
<br>
Could we get more info about the battery simulator ? I do not know what is it for ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p819">
<header><strong>Bernard Leak</strong><time datetime="2009-04-14 08:23 UTC">2009-04-14 08:23 UTC</time></header>
<h3>Re: Missing 128ms POR delay</h3>
<div class="forum-post-body">Thanks for the update.<br>
<br>
<br>
<br>
I didn't open the files individually - I used grep!<br>
<br>
<br>
<br>
I said I'd see about getting a testimonial for you quite a long time ago.  My managers<br>
<br>
are quite happy to let me do it, though of course they will have to approve any text I<br>
<br>
send you.  I simply haven't had any spare time.<br>
<br>
<br>
<br>
Bernard Leak.</div>
</article>

