---
title: "Support more inputs for C-function Call Block"
url: "/forum/topic/470/"
archiveKind: "topic"
---
# Support more inputs for C-function Call Block

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1779">
<header><strong>bmairs</strong><time datetime="2012-01-12 02:37 UTC">2012-01-12 02:37 UTC</time></header>
<div class="forum-post-body">It'd be nice if up to 6 inputs could be supported by the C-function Call Block. Not knowing how the backend works, I can't say whether this is indeed possible, but it'd be nice if it was.</div>
</article>

<article class="forum-post" id="p1785">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 10:03 UTC">2012-01-12 10:03 UTC</time></header>
<h3>Re: Support more inputs for C-function Call Block</h3>
<div class="forum-post-body">I understand that the 3 input limitation might not be practical, however I think that using array probides some possibilities.<br>
<br>
<br>
<br>
Everything is always possible, question of time...<br>
<br>
Is it a show stopper for your project ? <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1798">
<header><strong>bmairs</strong><time datetime="2012-01-13 17:03 UTC">2012-01-13 17:03 UTC</time></header>
<h3>Re: Support more inputs for C-function Call Block</h3>
<div class="forum-post-body">It's not a show-stopper, just an inconvenience. I have a lot of functions that just need to pass 4 variables to the function and it's annoying to have to pack that small amount of data to transmit it to C. There's no way to have the C-function call block allow for an arbitrary number and size of variables?</div>
</article>

<article class="forum-post" id="p1822">
<header><strong>philippe.1</strong><time datetime="2012-02-03 18:32 UTC">2012-02-03 18:32 UTC</time></header>
<h3>Re: Support more inputs for C-function Call Block</h3>
<div class="forum-post-body">Hello bmairs,<br>
<br>
<br>
<br>
Could you tell me how do you do to pass your 4 variables please,<br>
<br>
Thanks.<br>
<br>
Philippe</div>
</article>

<article class="forum-post" id="p1825">
<header><strong>bmairs</strong><time datetime="2012-02-08 19:07 UTC">2012-02-08 19:07 UTC</time></header>
<h3>Re: Support more inputs for C-function Call Block</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : philippe.1</header>Could you tell me how do you do to pass your 4 variables please,</blockquote><br>
<br>
Just pack all of your variables into an array and pass that. If they're different data types pack them all into an array of uint8s, uint16s, or uint32s and unpack them on the C end.</div>
</article>

