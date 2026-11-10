---
title: "ADC, QEI and PWM on dsPIC30f4012 problem"
url: "/forum/topic/189/"
archiveKind: "topic"
---
# ADC, QEI and PWM on dsPIC30f4012 problem

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p685">
<header><strong>Simon_says</strong><time datetime="2009-01-13 01:49 UTC">2009-01-13 01:49 UTC</time></header>
<div class="forum-post-body">Hello Lubin and Mariano!<br>
<br>
 I am still learning how to use the pheriperals  of the dsPIC. I was implementing the following model in order to use the PWM, the ADC and the QEI at the same time. The PWM generates just a signal with a constant period and constant duty cycle. The QEI, reads the position of the motor shaft and turns on a led when the count of the PSTCNT is &lt;1 or &gt; 44000 counts, otherwise the led is off. Last, the ADC reads a voltage input and turns on /off a led when the input voltage is at a certain level. When I use only one peripheral, the model runs fine in the dsPIC; However, in the model attached there is no problem with the PWM and the QEI but the ADC won´t respond  as it suppossed to. I noticed that when I configure the QEI something affects the ADC and it do not work properly... Can you help me? Could you please take a look at the model? Thanks a lot!<br>
<br>
 By the way, I am using the function and the model proposed by Mariano to run the QEI....<br>
<br>
Regards.<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/179-QEI_ADC3.mdl">Pièce jointe : QEI_ADC3.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/180-myQEI.c">Pièce jointe : myQEI.c</a></p>
</article>

<article class="forum-post" id="p686">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-13 21:52 UTC">2009-01-13 21:52 UTC</time></header>
<h3>Re: ADC, QEI and PWM on dsPIC30f4012 problem</h3>
<div class="forum-post-body">The configuration of the QEI peripheral in the C function file should not interfere with others peripheral:<br>
<br>
<br>
<br>
in myQEI.c , the line <br>
<br>
<span style="color:#0000ff">  ADPCFG = 0xFFFF;                      //ADPCFG | 0x0030;       // Disable the A/D pins 4 and 5</span><br>
<br>
Disable ADC from pin 0 to xx. Thus, ADC 0 will not be used properly!<br>
<br>
It should be like the comment: <br>
<br>
<span style="color:#0000ff">  ADPCFG =ADPCFG | 0x0030;       // Disable the A/D pins 4 and 5</span><br>
<br>
<br>
<br>
if it still do not work, report it. There may be few tricks to remove completely the pin configuration done inside the QEI c file!<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p687">
<header><strong>Simon_says</strong><time datetime="2009-01-14 00:11 UTC">2009-01-14 00:11 UTC</time></header>
<h3>Re: ADC, QEI and PWM on dsPIC30f4012 problem</h3>
<div class="forum-post-body">That was the solution!!!  Great! Thanks a lot. I will continue experimenting and learning...<br>
<br>
Thanks a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
</article>

<article class="forum-post" id="p688">
<header><strong>malife</strong><time datetime="2009-01-14 23:48 UTC">2009-01-14 23:48 UTC</time></header>
<h3>Re: ADC, QEI and PWM on dsPIC30f4012 problem</h3>
<div class="forum-post-body">Thanks Lubin,<br>
<br>
 Yes, that is correct. Glad it worked<br>
<br>
<br>
<br>
Cheers<br>
<br>
Mariano</div>
</article>

