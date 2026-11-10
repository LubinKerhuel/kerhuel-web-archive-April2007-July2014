---
title: "UART RX interrupt always included with config block"
url: "/forum/topic/323/"
archiveKind: "topic"
---
# UART RX interrupt always included with config block

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1296">
<header><strong>bmairs</strong><time datetime="2010-09-14 18:13 UTC">2010-09-14 18:13 UTC</time></header>
<div class="forum-post-body">I'm looking to use the configuration block of the UART along with my own custom code for the receive and transmit interrupts. Currently the transmit interrupt is only compiled if you've added the UART TX block. This is not the case with the UART RX block, as the interrupt handler is always compiled in even if the block isn't included.</div>
</article>

<article class="forum-post" id="p1519">
<header><strong>bmairs</strong><time datetime="2011-03-27 20:44 UTC">2011-03-27 20:44 UTC</time></header>
<h3>Re: UART RX interrupt always included with config block</h3>
<div class="forum-post-body">Is this something you intend to fix? I notice that it hasn't been fixed for the 3.4cb version and it's actually worse as both interrupts are included when you only have the UART initialization block. I think it'd be very useful for people who don't want to do the initialization by hand but want to handle everything else with their own custom code, such as myself.</div>
</article>

