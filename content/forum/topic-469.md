---
title: "problem with simulation time step, mips &amp; measured freq"
url: "/forum/topic/469/"
archiveKind: "topic"
---
# problem with simulation time step, mips &amp; measured freq

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1777">
<header><strong>leonk</strong><time datetime="2012-01-10 23:34 UTC">2012-01-10 23:34 UTC</time></header>
<div class="forum-post-body">Lubin,<br>
<br>
Great Blockset and excelent support!!!<br>
<br>
I've found some differences between the setted and measured freq of a blinking LED. It appears that the freq depends on the MIPS and the simulation time step ts. <br>
<br>
Ive found: <br>
<br>
if ts<del> x MIPS &lt; 0.0053 -&gt; LEDfrec[hz] = 340 x ts <br>
<br>
if ts<del> x MIPS &gt; 0.0053 -&gt; LEDfrec[hz] = 1.8 /MIPS <br>
<br>
<br>
<br>
each time i change ts, i also change the period samples to get 1 hz blinking freq. In the attached model, i measured 1.82 hz <br>
<br>
<br>
<br>
weird? am i misconfigurating the model? im using matlab2010b, dsPIC30f4013, with internal oscillator<br>
<br>
<br>
<br>
Thank you very much,<br>
<br>
<br>
<br>
Leonardo<br>
<br>
<br>
<br>
PS: another doubt: the dspic datasheet says "The user can tune the FRC oscillator within a range of +10.5% (840 kHz) and -12% (960 kHz) in steps of 1.50%" <br>
<br>
-&gt; FRC[MHZ]: 8(nom); 7.04(min); 8.84(max). <br>
<br>
-&gt; ips = fosc/4,<br>
<br>
-&gt; ips = 1.76 a 2.21 mips <br>
<br>
how does the blockset manage to set out of range ips?</del></del></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/461-dspic_pwm.mdl">Pièce jointe : dspic_pwm.mdl</a></p>
</article>

<article class="forum-post" id="p1782">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 09:48 UTC">2012-01-12 09:48 UTC</time></header>
<h3>Re: problem with simulation time step, mips &amp;amp; measured freq</h3>
<div class="forum-post-body">Leonardo,<br>
<br>
<br>
<br>
Thanks for your question.<br>
<br>
I mostly used the chips with an external quartz. I think that the blockset suport for the internal oscillator is pretty weak and I would not provide any garanty...<br>
<br>
<br>
<br>
I joined Microchip to build-up a new blockset. This new blockset will handle differents oscillators in a much better way than it has been done with my custom blockset.<br>
<br>
Thus if you are to use my custom blockset, considere using an external quartz which have been working very well so far (I used them exclusively !).<br>
<br>
Considere switching to the Microchip official blockset in the next comming releases...<br>
<br>
<br>
<br>
Regarding the tuning of the FRC resonator, it is not handled in my custom blockset. This will be handled in the Microchip futur blockset in prep...<br>
<br>
<br>
<br>
Lubin</div>
</article>

