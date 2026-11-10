---
title: "Any plans to support new dsPics with 2 QEI ?"
url: "/forum/topic/125/"
archiveKind: "topic"
---
# Any plans to support new dsPics with 2 QEI ?

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p380">
<header><strong>mhiernaux</strong><time datetime="2008-05-22 13:01 UTC">2008-05-22 13:01 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I'm currently working on motor control and I would have loved to use the blockset with the new dsPics like the p33FJ128MC202.<br>
<br>
<br>
<br>
Do you have any plans to include them in the blockset in a near future ? <br>
<br>
<br>
<br>
Thanks,<br>
<br>
Martin</div>
</article>

<article class="forum-post" id="p381">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-22 18:04 UTC">2008-05-22 18:04 UTC</time></header>
<h3>Re: Any plans to support new dsPics with 2 QEI ?</h3>
<div class="forum-post-body">Same question as Mariano,<br>
<br>
<br>
<br>
see : <a href="/forum/topic/110/">viewtopic.php?f=5&amp;t=110#p299</a><br>
<br>
<br>
<br>
I think I will do it. When will you need it ?</div>
</article>

<article class="forum-post" id="p386">
<header><strong>mhiernaux</strong><time datetime="2008-05-25 12:39 UTC">2008-05-25 12:39 UTC</time></header>
<h3>Re: Any plans to support new dsPics with 2 QEI ?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for the reply.<br>
<br>
<br>
<br>
I'll use them as soon as I can because of two reasons : <br>
<br>
<br>
<br>
* It will reduce one of my designs dramatically: I'm developing a robot regulation and right now I'm using 2 pic18f2431 only for their QEI modules. They are connected to the dsPic (33fj256MC710) via SPI and they only transfer the value of their QEI, nothing more :-) The main reason of doing this vs using the QEI of the dsPic and implementing the other in software is to have identical treatment for both QEIs. This temp solution will of course work, but if I can switch to the 802/804 series in the next couple of months, it will be highly appreciated :-)<br>
<br>
<br>
<br>
* As Mariano points out, this series marks the come back of PDIP packages and thus become a much easier choice for all kinds of small projects.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Martin</div>
</article>

