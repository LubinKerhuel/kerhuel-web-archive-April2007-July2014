---
title: "I2C alternative pins"
url: "/forum/topic/309/"
archiveKind: "topic"
---
# I2C alternative pins

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1254">
<header><strong>squall315</strong><time datetime="2010-06-10 18:27 UTC">2010-06-10 18:27 UTC</time></header>
<div class="forum-post-body">Hi Lubin, <br>
<br>
<br>
<br>
If it is possible, it could be helpful to have the possibility to use the alternative pins for the I2C in a future release. <br>
<br>
<br>
<br>
As it is a configuration register, we can't modify it with a S function and the only way is to go into the main source file created when you compile and modify _FPOR ( FPWRT_PWR1 ) by _FPOR (ALTI2C_ON &amp; FPWRT_PWR1 )</div>
</article>

