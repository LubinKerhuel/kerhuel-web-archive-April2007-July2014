---
title: "Support for returning structs from C-Function Call block"
url: "/forum/topic/321/"
archiveKind: "topic"
---
# Support for returning structs from C-Function Call block

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1289">
<header><strong>bmairs</strong><time datetime="2010-08-28 16:59 UTC">2010-08-28 16:59 UTC</time></header>
<div class="forum-post-body">I'm not certain if this is possible, but it would be awesome if you could specify a struct that the c-function call block was returning and then the block would output the data on a bus with the appropriately named signals. Right now it's inconvenient and computationally wasteful to pack a struct into a vector of uints for the c-function call block and to then unpack it in Matlab.</div>
</article>

<article class="forum-post" id="p1292">
<header><strong>LubinKerhuel</strong><time datetime="2010-09-03 17:57 UTC">2010-09-03 17:57 UTC</time></header>
<h3>Re: Support for returning structs from C-Function Call block</h3>
<div class="forum-post-body">This would be for returning values ? (block output)<br>
<br>
<br>
<br>
It may be Ok for the block to parse the C file and to extract some informations, but what to do with ?<br>
<br>
<br>
<br>
Perhaps, it may be possible to declare a structure. The C function output would be a pointer to this sctucture and the block could pase the file and use the structure elements name to provide as many output as the element numbers ?<br>
<br>
however, as the block output will be scalars, simulink would expect their value and not a pointer toward theses elements.<br>
<br>
<br>
<br>
It may thus be necessary to build a converter... that would not be efficient I guess.<br>
<br>
<br>
<br>
If you have any suggestions...<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1293">
<header><strong>bmairs</strong><time datetime="2010-09-13 22:58 UTC">2010-09-13 22:58 UTC</time></header>
<h3>Re: Support for returning structs from C-Function Call block</h3>
<div class="forum-post-body">What I mean is for the C-function blocks to be able to work natively with Simulink Bus objects. This means that they could take them as input or output. I would imagine this could be done because of the support Busses have over various blocks, but I don't know how this all works.<br>
<br>
<br>
<br>
I just know I spend a lot of time packing/unpacking data into uint8 vectors so I can go between C code and Simulink code. That's a lot of additionalcode and computation.</div>
</article>

<article class="forum-post" id="p1813">
<header><strong>bmairs</strong><time datetime="2012-01-19 17:10 UTC">2012-01-19 17:10 UTC</time></header>
<h3>Re: Support for returning structs from C-Function Call block</h3>
<div class="forum-post-body">Is there any possibility for this support to be added? I use busses extensively in my Simulink code and being able to pass them unmodified into the C-function call block would drastically simplify my models.</div>
</article>

