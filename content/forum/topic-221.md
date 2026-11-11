---
title: "problem with filter"
url: "/forum/topic/221/"
archiveKind: "topic"
---
# problem with filter

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p836">
<header><strong>crh</strong><time datetime="2009-05-05 06:00 UTC">2009-05-05 06:00 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
When I put an analog signal on the Ao port of the 30f4013 and I connect an oscilloscope on a low pass filter after the OC pins, everything is working correct. (the frequency on the output is exact the same as the input). See the model in the attachment.<br>
<br>
<strong>At least, with a filter from the expolorer16 model. This filter is working very well.</strong><br>
<br>
But when I design a filter with the FDatool (I tried a lot of designs) the system is not working. (So far as I know I can’t design with the FDatool a filter in the way of a discrete transfer Fcn). <br>
<br>
I use a very simple function generator (XR2206, home made) which I have connected to an anti-alias filter (made from opamps, 5poles, Low Pass). Cut off frequency of this filter: 600Hz=  {(Fs = 1200)/2}  <br>
<br>
I have connected a Schmitt trigger (74HC14) to this analog filter. The output from this 74HC14 is connected with the Ao port of the 30f4013. <br>
<br>
I have connected the OC1 pin of the 30f4013 with a low pass filter (5 poles) of 200Hz.  <br>
<br>
<br>
<br>
Xr2206 – Low Pass filter 600Hz – 74HC14  –   30f4013  –  Low Pass filter 200Hz<br>
<br>
<br>
<br>
As I mentioned in the beginning: when I connect the output from this last filter with an oscilloscope, the frequency is exact the same as the input form the analog function generator  (XR2206).  The discrete transfer Fcn filter is working very well. But any other filter designed with the FDatool is, till now, not working.  <br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/236-forumkerhueladc_filter_OC.mdl">Pièce jointe : forumkerhueladc_filter_OC.mdl</a></p>
</article>

<article class="forum-post" id="p837">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-05 16:06 UTC">2009-05-05 16:06 UTC</time></header>
<h3>Re: problem with filter</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
You are making weird system. It is not very clear why you are using an ADC. What about using an Input Capture block to measure the period of your input signal?<br>
<br>
There may be a problem with the filters you design. You should post a model with a non working filter. <br>
<br>
<br>
<br>
It may help you to do simulation with filters you just design, checking that they are doing the job. Simulink is a very powerful tool for such design. <br>
<br>
You may also use an UART and looking at signals at different steps. Have a look on the video Mariano has done. At the end, it shows how using the UART interface with the graphical user interface: <a href="https://github.com/LubinKerhuel/kerhuel-web-archive-April2007-July2014/releases/download/large-files-v1/dsPicScreencastFromMariano.mov">http://www.kerhuel.eu/download/dsPicScr ... ariano.mov</a><br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p841">
<header><strong>crh</strong><time datetime="2009-05-06 07:19 UTC">2009-05-06 07:19 UTC</time></header>
<h3>Re: problem with filter</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
As you see, I have uploaded some working filters, designed in the FDATool, with their properties in the way I designed them in the FDATool. <br>
<br>
<br>
<br>
I do not fully understand why I cannot use the ADC block. <br>
<br>
<br>
<br>
Anyway, I am intend to study the possibilities of the Input Capture block and start to work with the UART interface with the graphical user interface.<br>
<br>
<br>
<br>
This video tutorial of Mariano is really good and very clear. All compliments! This is what I really miss on the Internet: practical tutorials in combination with your blockset. <br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/238-simforumwithBPfilter.mdl">Pièce jointe : simforumwithBPfilter.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/239-simforumwithLPfilter.mdl">Pièce jointe : simforumwithLPfilter.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/240-properties%20LP%20filter.gif">Pièce jointe : properties LP filter.gif</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/241-properties%20BP%20filter.gif">Pièce jointe : properties BP filter.gif</a></p>
</article>

<article class="forum-post" id="p842">
<header><strong>crh</strong><time datetime="2009-05-06 07:46 UTC">2009-05-06 07:46 UTC</time></header>
<h3>Re: problem with filter</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Please, I am looking for some models with the Input Capture block.<br>
<br>
<br>
<br>
Casparus</div>
</article>

<article class="forum-post" id="p843">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-06 08:06 UTC">2009-05-06 08:06 UTC</time></header>
<h3>Re: problem with filter</h3>
<div class="forum-post-body">Hi Casparus, I will have a look on your filters soon.<br>
<br>
<br>
<br>
Input Capture block is quite similar to the Output Compare block. Despite I am using this block a lot (mostly to capture PWM duty cycle from remote control receiver) Ijust realize that there is no example using this block. <br>
<br>
You must configure inside the block the max periode or time-up/Time-down you are to measure. Then, the max value in ICxmax correspond to this time.<br>
<br>
Please read the <a href="/wiki/simulink-embedded-target-for-pic/">help</a> page about this block. Feel free to complete the page or to ask me to complete for any missing information. <br>
<br>
<br>
<br>
Lubin</div>
</article>

