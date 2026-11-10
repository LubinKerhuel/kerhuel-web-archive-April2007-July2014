---
title: "Internal Quartz and PLL"
url: "/forum/topic/308/"
archiveKind: "topic"
---
# Internal Quartz and PLL

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1253">
<header><strong>squall315</strong><time datetime="2010-06-10 18:24 UTC">2010-06-10 18:24 UTC</time></header>
<div class="forum-post-body">Hi Lubin, I already told you but i write it there to give the solution to everyone<br>
<br>
<br>
<br>
If you want to use the internal quartz with a dspic33fj128gp802/804 (maybe you will have the same problem with others micro-controllers but i tested these two), the PLL value is not taken into account which prevents you from choosing the number of instructions you want. <br>
<br>
<br>
<br>
The solution i found is to go into the main source file created when you compile and change  _FOSCSEL( FNOSC_FRC &amp; IESO_OFF &amp; 0xFFFF ) by  _FOSCSEL( FNOSC_FRCPLL &amp; IESO_OFF &amp; 0xFFFF ). <br>
<br>
<br>
<br>
All the others registers to select the different prescalers are correct so you should have the right number of MIPS.</div>
</article>

