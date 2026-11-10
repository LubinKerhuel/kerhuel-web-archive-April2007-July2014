---
title: "Output Compare block - Behaviour at edges values for OC1max"
url: "/forum/topic/93/"
archiveKind: "topic"
---
# Output Compare block - Behaviour at edges values for OC1max

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p246">
<header><strong>Masaki</strong><time datetime="2008-02-26 11:32 UTC">2008-02-26 11:32 UTC</time></header>
<div class="forum-post-body">I'm working on Output Compare block to make a PWM output and came across a strange<br>
<br>
phenomena. <br>
<br>
<br>
<br>
What I did was to connect a potentiometer to AN0 and a oscilloscope to OC1.<br>
<br>
The potentiometer is hooked to +5V and GND. <br>
<br>
I set MaxChannel of OC block to 1e-4, 2e-5,1e-5 to get 10kHz, 50kHz, 100kHz PWM signals. <br>
<br>
Channels Input Type is set to be 10 to get variable Down duration. <br>
<br>
<br>
<br>
When I turn the potentiometer in full swing, the PWM Down period varies between:<br>
<br>
 10kHz   500ns-100us<br>
<br>
 50kHz   500ns-20us <br>
<br>
100kHz   500ns-10us.<br>
<br>
<br>
<br>
OC1max value in each case is:<br>
<br>
 10kHz  3000<br>
<br>
 50kHz   600 <br>
<br>
100kHz  300.<br>
<br>
<br>
<br>
What I think strange is that the pulse duration changes x2000, x400, x200 times. <br>
<br>
These numbers should be the same as OC1max values, as they represent the maximum<br>
<br>
allowable input to Output Capture block. <br>
<br>
<br>
<br>
Why these difference happens? Is there any setting I miss?<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p247">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-26 21:09 UTC">2008-02-26 21:09 UTC</time></header>
<h3>Re: OC1max value in Output Compare block</h3>
<div class="forum-post-body">Hi Masaki,<br>
<br>
<br>
<br>
I upload the file I received by mail.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Masaki</header>What I think strange is that the pulse duration changes x2000, x400, x200 times.<br>
<br>
These numbers should be the same as OC1max values, as they represent the maximum<br>
<br>
Allowable input to Output Capture block. </blockquote><br>
<br>
The pulse duration is the one defined in the block Output Compare dialog box. (If it is not the case, report it because it is a bug.)<br>
<br>
The variable OC1max is a scalar value (uint16) that code for the max duration (max/channel) defined in the Output Compare dialog box.<br>
<br>
This scalar value depends on the max duration (max/channel) set in the dialog box.<br>
<br>
<br>
<br>
Few remarks about this model.<br>
<br>
First, it is very useful to view data types.<br>
<br>
In your case, I guess that after the first multiplication/division block, you get a double, and after the second multiplication block, you get a uint16 ? <br>
<br>
I strongly advice to replace theses two multiplication blocks by one gain block with the value (OC1max/4095).<br>
<br>
The output of this gain block should be a uint16.<br>
<br>
The computation of the multiplication could be set to either uint16, or another more precise data type. <br>
<br>
If you use only uint16 ; depending if OC1max/4095 is near an integer value or not consider using floor(OC1max/4095) to avoid higher result than OC1max. Example: OC1max/4095 = 2.7 ==&gt; would be round to 3 if integer computation is chosen...<br>
<br>
<br>
<br>
If I do not response to your question, please provide more details and upload the model.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/32-testan1.gif">Pièce jointe : testan1.gif</a></p>
</article>

<article class="forum-post" id="p248">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-27 20:54 UTC">2008-02-27 20:54 UTC</time></header>
<h3>Re: OC1max value in Output Compare block</h3>
<div class="forum-post-body">Masaki, I post the information from your mail here.<br>
<br>
<br>
<br>
<br>
<blockquote>In each experiments, I set MaxChannel of OC block to 1e-4, 2e-5,1e-5 to get 10kHz, 50kHz, 100kHz PWM signals.<br>
<br>
Channels Input Type is set to be 10 to get variable Down duration.<br>
<br>
<br>
<br>
What I notice is that the ratio of min and max of Duration isn’t equal to OC1max in each frequency. For example, in case of 100kHz, min duration is 500nsec, max duration is 10usec. The ratio is 20, while OC1max is 300.<br>
<br>
<br>
<br>
Does this make sense?</blockquote><br>
<br>
The Output Compare (OC) peripheral used as PWM output is not completely hardware driven. It means that a minimum time is required between two events : time for code execution. In your case of 33ns Down period (corresponding to 1/300<br>
<br>
* 1/100000) the falling and rising edge are too close to each other. A minimum execution time for instruction being executed between two edges is necessary. In this case, from your data, this minimum time is about 500ns. This correspond to an input value for the OC block of 15. So, 15 is the minimum acceptable value for the Down input block. (the OC block act like as a saturation if you set value lower than 15).<br>
<br>
Note that the same phenomena will appears as your input value get very close from the Periode (setting two edge very close)<br>
<br>
<br>
<br>
If you require such a small down period, considere using a dsPIC with a motor PWM peripheral. The PWM peripheral is hardware driven and will work best on theses "edge" phenomena.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/33-Problem_OutputCompare_fastEvents.png">Pièce jointe : Problem_OutputCompare_fastEvents.png</a></p>
</article>

<article class="forum-post" id="p249">
<header><strong>Masaki</strong><time datetime="2008-02-28 00:13 UTC">2008-02-28 00:13 UTC</time></header>
<h3>Re: Output Compare block - Behaviour at edges values for OC1max</h3>
<div class="forum-post-body">I understand the situation. <br>
<br>
As my CPU is dsPIC30F3013 at Fcy=30MHz, it's supposed to handle PWM signal generation by interrupts.<br>
<br>
As a result, it can only generate edges at every 500ns at its fastest speed.<br>
<br>
<br>
<br>
If I switch my CPU to dsPIC30F4012 with motor control pins, <br>
<br>
does your software support hardware PWM signal generation?</div>
</article>

<article class="forum-post" id="p263">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-08 15:28 UTC">2008-03-08 15:28 UTC</time></header>
<h3>Re: Output Compare block - Behaviour at edges values for OC1max</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Masaki</header>does your software support hardware PWM signal generation?</blockquote><br>
<br>
Yes, hardware PWM signal generation can be done using the "<a href="/RTWdsPIC/Blocks/PWMMotorOutput.html">motor PWM peripheral</a>"<br>
<br>
<br>
<br>
Lubin</div>
</article>

