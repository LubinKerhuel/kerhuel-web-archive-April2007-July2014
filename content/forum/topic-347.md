---
title: "I/O pins allocation"
url: "/forum/topic/347/"
archiveKind: "topic"
---
# I/O pins allocation

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1432">
<header><strong>Nadav_Technion</strong><time datetime="2011-01-08 08:37 UTC">2011-01-08 08:37 UTC</time></header>
<div class="forum-post-body">Hi Lubin<br>
<br>
I'm an undergrad student working on a project which require PWM for a motor using dspic33FJ256GP710A<br>
<br>
<br>
<br>
me and my partner are trying to figure out how we allocate a physical I/O pin to the OC<br>
<br>
<br>
<br>
in other words how do we know which pin will have the desired output function<br>
<br>
thanks<br>
<br>
Nadav</div>
</article>

<article class="forum-post" id="p1433">
<header><strong>LubinKerhuel</strong><time datetime="2011-01-08 22:42 UTC">2011-01-08 22:42 UTC</time></header>
<h3>Re: I/O pins allocation</h3>
<div class="forum-post-body">Hi Nadav,<br>
<br>
<br>
<br>
Not sure to understand your question.<br>
<br>
dspic 33FJ256GP710A does not have PWM motor peripheral. However, you could use Output Compare peripheral. On the <a href="http://ww1.microchip.com/downloads/en/DeviceDoc/70593B.pdf">datasheet</a> on page 17, you can see the dsPIC pin diagram and thus you will be able to locate Output Compare (from OC1 to OC8).<br>
<br>
<br>
<br>
Thus, to use one of these pin, you just need to place either a block <a href="/wiki/dspic-block-output-compare/">Output Compare</a> or <a href="/wiki/dspic-block-output-compare-hw/">Output Compare HW</a>.<br>
<br>
<br>
<br>
As soon as you place a block of a certain peripheral, the corresponding PIN of the dsPIC are configured so as to has the corresponding peripheral function. <br>
<br>
<br>
<br>
Note that on some dsPIC (not on 33FJ256GP710A) has remapable pins capabilities (noted RP pins). This means that you can choose the PIN placement of certain peripheral. This function is done with the blockset through the mapping PIN block.<br>
<br>
<br>
<br>
Lubin</div>
</article>

