---
title: "Can not add anything to my schematic"
url: "/forum/topic/353/"
archiveKind: "topic"
---
# Can not add anything to my schematic

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1448">
<header><strong>squall315</strong><time datetime="2011-01-21 09:37 UTC">2011-01-21 09:37 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I'm using a Programmable Gain Array to amplify 6 channels at the same time connected to a dspic 33fj128gp802. As I want a 2kHz refresh rate on each channel, I'm working at 12kHz and this PGA is controlled by SPI. When I do that, my program is working fine and the Calculus Time Step gives me 1200 for T and 3333 for PR1 as I work at 40MIPS. <br>
<br>
<br>
<br>
After that, when I try to add anything to my schematic, even things really simple like an inverter on my blinking led, my program is not working anymore at all. <br>
<br>
I tried to compare the codes generated when it is working and when it is not but nothing changed in the configuration registers. <br>
<br>
<br>
<br>
When it is working, the blinking led frequency and the SPI clock are correct. The weird thing is when I compile my working program at 2kHz instead of 12kHz, it gives me 4000 for T whereas the difference in the number of instructions should not be so different. <br>
<br>
<br>
<br>
So, as I have really no idea of what is going on, do you have any idea? Is it possible that my dsPic is used at 100% but the calculus time step block is giving me false values ? <br>
<br>
<br>
<br>
Thanks, <br>
<br>
<br>
<br>
Fabien</div>
</article>

<article class="forum-post" id="p1462">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-15 21:49 UTC">2011-02-15 21:49 UTC</time></header>
<h3>Re: Can not add anything to my schematic</h3>
<div class="forum-post-body">Hi fabien,<br>
<br>
<br>
<br>
Weird problem! Not sure to get it all ; it might be helpful to post the model so as to get more insight.<br>
<br>
<br>
<br>
Anyway, you might try to use the Busy flag port (see <a href="/wiki/dspic-block-master/">Master block</a>) and a scope to check what's really going on.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1483">
<header><strong>squall315</strong><time datetime="2011-02-24 15:33 UTC">2011-02-24 15:33 UTC</time></header>
<h3>Re: Can not add anything to my schematic</h3>
<div class="forum-post-body">Hi Lubin, <br>
<br>
<br>
<br>
The busy flag is never coming back to 0 which is what I thought. The weird thing is my  SPI clock and blinking LED frequency are correct and the value indicated by T of the Calculus Time Step block must be incorrect as I end up with a 30% occupation. <br>
<br>
<br>
<br>
The goal of that experience was to know if I could work with that frequency so I have my answer but I don't understand how adding something to the schematic can make my program not work at all and not make it slower. And I think we can not take into account the T value if the microcontroller is always occupied. <br>
<br>
<br>
<br>
Fabien</div>
</article>

