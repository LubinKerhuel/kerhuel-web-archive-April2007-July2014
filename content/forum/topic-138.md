---
title: "maximum speed on PIC32?"
url: "/forum/topic/138/"
archiveKind: "topic"
---
# maximum speed on PIC32?

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p415">
<header><strong>lead_innovation</strong><time datetime="2008-06-11 09:42 UTC">2008-06-11 09:42 UTC</time></header>
<div class="forum-post-body">dear sir!<br>
<br>
    first thank you for trial version : Simulink embedded coder for dspic/pic24/pic32.  :D <br>
<br>
    when i try to use Pic32 master block. i don't know "maximum speed on Pic32" (number milion instruction percent second)<br>
<br>
    the Xtal i use is 72Mhz.<br>
<br>
    thank again for best solution DSP on dspic.</div>
</article>

<article class="forum-post" id="p420">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-11 23:23 UTC">2008-06-11 23:23 UTC</time></header>
<h3>Re: maximum speed on PIC32?</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
The C32 has a lot of multipliers or diviser factor allowing to configure the chip so as to get the desired MIPS.<br>
<br>
On the master block, you have to :<br>
<br>
- Set correctly the quartz mounted on your board. (<strong>Quartz or External Clock Frequency</strong>)<br>
<br>
- Set the desired MIPS (<strong>Desired Instruction Per Seconds</strong>)<br>
<br>
The blockset automatically compute all parameters so as to be as close as possible to the desired MIPS. The real MIPS achieved is showed in <strong>Number Instructions per Seconds</strong></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/91-dsPIC_Master_C32.png">Pièce jointe : dsPIC_Master_C32.png</a></p>
</article>

<article class="forum-post" id="p424">
<header><strong>lead_innovation</strong><time datetime="2008-06-14 03:22 UTC">2008-06-14 03:22 UTC</time></header>
<h3>Re: maximum speed on PIC32?</h3>
<div class="forum-post-body">Thanks for reply! <br>
<br>
<br>
<br>
      i attachment a image. maximum Quartz is 72Mhz in PIC32MX360 =&gt; it excute on 1080 MIPS? (very fast with microcontroller!) that true?</div>
</article>

<article class="forum-post" id="p425">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-14 08:41 UTC">2008-06-14 08:41 UTC</time></header>
<h3>Re: maximum speed on PIC32?</h3>
<div class="forum-post-body">Hi Stefano,<br>
<br>
<br>
<br>
I do not see any image inside your last post.<br>
<br>
<br>
<br>
From the microchip doc : <br>
<br>
The external quartz you can use with a PIC32 chip must be within the [3.5  40]MHz range.<br>
<br>
If you use an External Clock, it must be within the [0 72]Mhz range.<br>
<br>
<br>
<br>
You can use PLL multiplier to speed up internally the clock.<br>
<br>
I do not know that is the max speed that can be obtained with a PIC32. It is probably not 1080MIPS (that is 1 Ghz : too fast !)<br>
<br>
<br>
<br>
I attach a very simple example running the PIC32 starter kit. The PIC32 starter kit has an external Quartz of 8Mhz. In the example, I use PLL and get a 1 Mips speed. However, I could get a wide range of speed by modifying the <strong>Desired Instruction Per Seconds</strong>.<br>
<br>
<br>
All peripheral are not yet supported on the PIC32 family.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/92-PIC32_StarterKit_demo.mdl">Pièce jointe : PIC32_StarterKit_demo.mdl</a></p>
</article>

<article class="forum-post" id="p427">
<header><strong>lead_innovation</strong><time datetime="2008-06-17 13:52 UTC">2008-06-17 13:52 UTC</time></header>
<h3>Re: maximum speed on PIC32?</h3>
<div class="forum-post-body">dear sir!<br>
<br>
      i think i found answer for my question. the maximum on pic32 is 72MIPS on CPU and 32MIPS on peripheral(that i read manual C32). but i'm not sure.</div>
</article>

