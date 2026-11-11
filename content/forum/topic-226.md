---
title: "Input Capture Block and Output Compare block"
url: "/forum/topic/226/"
archiveKind: "topic"
---
# Input Capture Block and Output Compare block

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p858">
<header><strong>val</strong><time datetime="2009-06-03 08:22 UTC">2009-06-03 08:22 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
By accident I found your embedded target for Microchip dsPIC.<br>
<br>
I am a student at the Technical University of Delft in The Netherlands.<br>
<br>
For one of my projects I need to capture a frequency of 500Hz and filter random noise away.<br>
<br>
I consider to use your Input Capture Block and Output Compare block.<br>
<br>
Can you provide me with some models? I have searched for it on your Forum, but I could not find models with the Input Capture Block.<br>
<br>
<br>
<br>
Val</div>
</article>

<article class="forum-post" id="p859">
<header><strong>LubinKerhuel</strong><time datetime="2009-06-03 22:02 UTC">2009-06-03 22:02 UTC</time></header>
<h3>Re: Input Capture Block and Output Compare block</h3>
<div class="forum-post-body">Hi Val,<br>
<br>
<br>
<br>
I hope this is a nice accident !<br>
<br>
<br>
<br>
you will find example about Input Capture block on the example page : <a href="/wiki/category/example/">http://www.kerhuel.eu/wiki/Category:Example</a><br>
<br>
look at the autopilote model, I think it's using IC blocks.<br>
<br>
<br>
<br>
Also, have a look on the IC block help : <a href="/wiki/dspic-block-output-compare/">http://www.kerhuel.eu/wiki/Block/Output_Compare</a><br>
<br>
<br>
<br>
your information is coded in Pulse Width Modulation ?<br>
<br>
<br>
<br>
If you want to filter an analog signal at 500Hz, use the ADC block and configure the simulink time step at 500Hz. Example of such filtering is explain (and one example is in the example directory of the blockset)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p860">
<header><strong>val</strong><time datetime="2009-06-04 07:56 UTC">2009-06-04 07:56 UTC</time></header>
<h3>Re: Input Capture Block and Output Compare block</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thank you very much for the appreciated intention to help me.<br>
<br>
However, I am a little bit confused, because I cannot find the simulink model on the page of the the autopilote model. <br>
<br>
<br>
<br>
You wrote:<br>
<br>
If you want to filter an analog signal at 500Hz, use the ADC block and configure the simulink time step at 500Hz. Example of such filtering is explain (and one example is in the example directory of the blockset)<br>
<br>
<br>
<br>
Please give me the name of the examples. Are you talking about two examples?<br>
<br>
I suppose the time step in the solver must be the same as in the ADC block? And how to set the period in the Output Compare block to get a fine resolution.<br>
<br>
How to configure the time step if I expect an analog signal from 400Hz to 500Hz and I want to filter out a signal of 440Hz with a Notch filter?<br>
<br>
I suppose I have to take into account the Nyquist theorem.<br>
<br>
 <br>
<br>
Val</div>
</article>

<article class="forum-post" id="p861">
<header><strong>LubinKerhuel</strong><time datetime="2009-06-04 17:20 UTC">2009-06-04 17:20 UTC</time></header>
<h3>Re: Input Capture Block and Output Compare block</h3>
<div class="forum-post-body">Hi Val,<br>
<br>
<br>
<br>
I respond very quickly:<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : val</header>I cannot find the simulink model on the page of the the autopilote model</blockquote><br>
Ok, I did not upload it yet. my mistake. Will do it soon.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : val</header>Please give me the name of the examples.</blockquote><br>
<a href="/wiki/explorer-16-board/">http://www.kerhuel.eu/wiki/Explorer_16_Board</a><br>
<br>
<br>
<blockquote><header class="quote-author">Citation : val</header>I suppose the time step in the solver must be the same as in the ADC block?</blockquote><br>
it must be equal or higher. (equal is the easiest solution)<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : val</header>how to set the period in the Output Compare block to get a fine resolution</blockquote><br>
Have a look on the block's help. or a quick glance at the examples.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : val</header>I want to filter out a signal of 440Hz with a Notch filter</blockquote><br>
About nyquist frequency, the question is which frequency are you willing to keep ? and How to keep them untouthced ? <br>
<br>
If you undersample your signal (at a frequency lower than the nyquist frequcney : 880Hz, the 440Hz will be folded into a lower frequency that you can still filter out. (for example if your real 440Hz is folded in 200Hz because of low frequency sampling, you may filter out that 200Hz, but that will also remove the 200Hz of the real signal !). <br>
<br>
You may find smart solution using this principle ! you should Have a look first on the frequency present in the original signal.<br>
<br>
Anyway, if you want to keep it simple, sample at something like 2Khz and filter out the 440Hz with a notch filter.<br>
<br>
<br>
<br>
I'll be absent for two weeks from now (from 5 of june until 20 of june 2009). Thus, I will not be able to provide response for that time. If anybody can give you answers during theses two weeks...<br>
<br>
<br>
<br>
Lubin</div>
</article>

