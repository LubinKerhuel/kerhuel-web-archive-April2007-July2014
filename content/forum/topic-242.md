---
title: "Duty cycle of OC(HW)"
url: "/forum/topic/242/"
archiveKind: "topic"
---
# Duty cycle of OC(HW)

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p926">
<header><strong>Quan</strong><time datetime="2009-07-30 03:50 UTC">2009-07-30 03:50 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am making a sampling using the OC(HW) and ADC.<br>
<br>
In the dialog of OC(HW), we can set the period for the PWM output.<br>
<br>
However, I am not clear about setting the duty cycle.<br>
<br>
Could you explain exactly what the set and reset mean in the block?<br>
<br>
Thanks in advance.<br>
<br>
<br>
<br>
Quan</div>
</article>

<article class="forum-post" id="p931">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 11:31 UTC">2009-07-30 11:31 UTC</time></header>
<h3>Re: Duty cycle of OC(HW)</h3>
<div class="forum-post-body">Could you please have a look on the block's page : <a href="/wiki/dspic-block-output-compare-hw/">http://www.kerhuel.eu/wiki/Block/Output_Compare_HW</a><br>
<br>
<br>
<br>
Unfortunatly, I will not have time to draw something (that would make it clearer)<br>
<br>
<br>
<br>
If there are unclear point, please let me know.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p932">
<header><strong>Quan</strong><time datetime="2009-07-30 13:46 UTC">2009-07-30 13:46 UTC</time></header>
<h3>Re: Duty cycle of OC(HW)</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Sorry for bothering you again. <br>
<br>
I have read the block page many times, still I cannot get what I want.<br>
<br>
Attached is a graph got from the example of Hyper Sampling.<br>
<br>
Could you explain how the duty cycle is decided and why there is a "+" between the set and reset inputs?<br>
<br>
Thanks very much.<br>
<br>
<br>
<br>
Quan</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/261-HyperSampling.PNG">Pièce jointe : HyperSampling.PNG</a></p>
</article>

<article class="forum-post" id="p934">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 18:16 UTC">2009-07-30 18:16 UTC</time></header>
<h3>Re: Duty cycle of OC(HW)</h3>
<div class="forum-post-body">Hi Quan,<br>
<br>
<br>
<br>
I respond quicky, sorry if there are imprecision.<br>
<br>
<br>
<br>
OC works with a counter. For a given periode (set within the block) the counter will count from 0 to a number, let say it is 1000 here, this number is given in OCmax (it depends on your quartz).<br>
<br>
<br>
<br>
- The ADC starts conversion when the counter is reset, ie, goes from 1000 to 0.<br>
<br>
- The OC output is set to 1 when the counter reach the Tset value.<br>
<br>
- The OC output is set to 0 when the counter reach the Treset value.<br>
<br>
<br>
<br>
For example, <br>
<br>
- if Tset value 250 and Treset value is 350, you will get a PWM duty cycle of 10% on the OC output. ADC will starts conversion while the OC output is 0<br>
<br>
- if Tset value 950 and Treset value is 50, you will also get a PWM duty cycle of 10% on the OC output. ADC will starts conversion while the OC output is 1<br>
<br>
<br>
<br>
Please feel free to add any usefull explanation on the Wiki page about OC(HW)<br>
<br>
<a href="/wiki/dspic-block-output-compare-hw/">http://www.kerhuel.eu/wiki/Block/Output_Compare_HW</a></div>
</article>

<article class="forum-post" id="p936">
<header><strong>Quan</strong><time datetime="2009-07-31 02:47 UTC">2009-07-31 02:47 UTC</time></header>
<h3>Re: Duty cycle of OC(HW)</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for your patient explanation.<br>
<br>
I will add some detailed explanation for OC(HW).<br>
<br>
<br>
<br>
Quan</div>
</article>

