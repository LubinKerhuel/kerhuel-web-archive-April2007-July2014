---
title: "PIC32"
url: "/forum/topic/214/"
archiveKind: "topic"
---
# PIC32

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p808">
<header><strong>jorge.pelizzoni</strong><time datetime="2009-04-06 15:15 UTC">2009-04-06 15:15 UTC</time></header>
<div class="forum-post-body">Dear all,<br>
<br>
<br>
<br>
Why is that that PIC32 seems to be the least supported chip both by Kerhuel's blockset and Microchip's? (By the way, is Microchip's blockset based on his?)<br>
<br>
Is PIC32 likely to receive better coverage soon and leave the "experimental" status?<br>
<br>
<br>
<br>
Thanks in advance. Cheers,<br>
<br>
<br>
<br>
Jorge.</div>
</article>

<article class="forum-post" id="p826">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-15 19:07 UTC">2009-04-15 19:07 UTC</time></header>
<h3>Re: PIC32</h3>
<div class="forum-post-body">Hi Jeorge,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jorge.pelizzoni</header>Is PIC32 likely to receive better coverage soon and leave the "experimental" status?</blockquote><br>
As soon as you guys will use it in your projects, it will leave the experimental status. It is still experimental for me since I do not use theses chip in my projects yet. Not but reported yet, but is there anybody using it ? <br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jorge.pelizzoni</header>is Microchip's blockset based on his</blockquote><br>
Could not answer this question; you should post the question on microchip’s forum. It’s true that I was asked few technical questions by the microchip’s Indian development team few years ago. <br>
<br>
<br>
<br>
I’ve been developing the blockset for more than three years now. I release a first version in march 2007. Microchip released its blockset in late 2008, about September or October, that is one year and a half after my first release.<br>
<br>
Microchip also had the same good ideas to create a NOP block and to add a "C function Call" block which are two very specific blocks. I think that I still have few more ideas since I am using my blockset to build complex automatic systems. For example ideas for tools to check that real time constraint are respected. I am not sure that microchip’s blockset embedded a visualisation system allowing seeing or logging variables evolution in the matlab environment.<br>
<br>
<br>
<br>
Provided someone tested Microchip blockset, it would be appreciated to get a comparative review.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p876">
<header><strong>malife</strong><time datetime="2009-06-28 23:31 UTC">2009-06-28 23:31 UTC</time></header>
<h3>Re: PIC32</h3>
<div class="forum-post-body">I've looked at both and actually tested but of them and I have to say Lubin's is much better than Microchip's. For instance the C function call that they implement you can only pass scalars (i.e. no vectors) which is essentially useless. Also all of their blocks are polled-based instead of interrupt driven, which if  you are playing in a classroom it might be OK but if you are doing some serious development is also useless.<br>
<br>
<br>
<br>
 We decided to stay with Lubin's blocks for this reason and also for the continuous support. Usually issues that we've had (bugs) have been resolved within 48 hours. Try getting that from Microchip. Don't get me wrong I love the brand and I think there are many things they are doing very well, but their Simulink blockset is not one of them.<br>
<br>
<br>
<br>
Regarding the PIC32 I can not tell, I've only used the dsPIC.<br>
<br>
<br>
<br>
Hope this helps.</div>
</article>

