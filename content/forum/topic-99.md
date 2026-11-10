---
title: "Dspic and ICD2 problem"
url: "/forum/topic/99/"
archiveKind: "topic"
---
# Dspic and ICD2 problem

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p265">
<header><strong>barryforever</strong><time datetime="2008-03-13 16:12 UTC">2008-03-13 16:12 UTC</time></header>
<div class="forum-post-body">I knw this is not the right place to discuss but Im desperate to find answer .<br>
<br>
I have got ICD2 and Dspic30f3011 and problem is that whenever I connect the Chip to ICD2<br>
<br>
it gives me INVALID TARGET DEVICE no matter how i connect . I searched for answers dint find one which solved the problem.<br>
<br>
I hear that these chips can be only programmed only placed in circuit ..<br>
<br>
any help would be appreciated</div>
</article>

<article class="forum-post" id="p270">
<header><strong>malife</strong><time datetime="2008-03-20 23:39 UTC">2008-03-20 23:39 UTC</time></header>
<h3>Re: Dspic and ICD2 problem</h3>
<div class="forum-post-body">go to MPLAB Menu Configure-&gt;Select Device and make sure you have the correct device. That should take care of it.<br>
<br>
<br>
<br>
Hope this helps<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p272">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-21 00:47 UTC">2008-03-21 00:47 UTC</time></header>
<h3>Re: Dspic and ICD2 problem</h3>
<div class="forum-post-body">You could also check that the your chip is correctly powered.<br>
<br>
<br>
<br>
If the chip is not powered, the return code is either FF or 0 and will give a "wrong" chip ID.<br>
<br>
Btw, I'm not an ICD2 expert ! (use a bootloader like tinybld, much faster and easier)<br>
<br>
<br>
<br>
Lubin</div>
</article>

