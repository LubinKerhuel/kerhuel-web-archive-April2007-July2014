---
title: "Know when using interrupt driven UART (Tx or Rx)"
url: "/forum/topic/136/"
archiveKind: "topic"
---
# Know when using interrupt driven UART (Tx or Rx)

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p412">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-05 11:50 UTC">2008-06-05 11:50 UTC</time></header>
<div class="forum-post-body">You may get erratic result when setting in the UART configuration block a buffer with more than 256 bytes. The default is 32.<br>
<br>
<br>
<br>
Workaround: Set the buffer for both RX or Tx to a value<strong> lower or equal to 128 bytes</strong> (may work also with 256 bytes)<br>
<br>
<br>
<br>
This bug will be corrected in the next blockset version (0.98b)</div>
</article>

