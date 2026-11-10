---
title: "fuzzy in dspic 30f4011"
url: "/forum/topic/164/"
archiveKind: "topic"
---
# fuzzy in dspic 30f4011

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p552">
<header><strong>macroevil</strong><time datetime="2008-10-05 23:22 UTC">2008-10-05 23:22 UTC</time></header>
<div class="forum-post-body">hi ....great job !!!! :D <br>
<br>
<br>
<br>
<br>
<br>
i have a problem....i'm trying to make a control based in fuzzy logic but the compiler says <br>
<br>
<br>
<br>
"Warning:  A terminate function is necessary, however the Real-Time Workshop build process did not generate a terminate function because the 'Terminate function required' check box is cleared."<br>
<br>
<br>
<br>
the fuzzy block is to simple...one input one output......and bisector dezufication....<br>
<br>
<br>
<br>
i dont' know what to do...can you help me.....<br>
<br>
<br>
<br>
..thanks..</div>
</article>

<article class="forum-post" id="p553">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-05 23:28 UTC">2008-10-05 23:28 UTC</time></header>
<h3>Re: fuzzy in dspic 30f4011</h3>
<div class="forum-post-body">Something is wrong in the configuration of you simulink model.<br>
<br>
<br>
<br>
You could try to make a new model model  starting from an example model file in the directory example (then copy-past your blocks).<br>
<br>
If it did not solve the problem, upload your model on the forum.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p554">
<header><strong>macroevil</strong><time datetime="2008-10-05 23:36 UTC">2008-10-05 23:36 UTC</time></header>
<h3>Re: fuzzy in dspic 30f4011</h3>
<div class="forum-post-body">too fast your answer......thanks<br>
<br>
<br>
<br>
the model is to simple...only for test fuzzy in dspic....<br>
<br>
<br>
<br>
There is this model of the attached file..</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/122-prueba_1_adcTors232.mdl">Pièce jointe : prueba_1_adcTors232.mdl</a></p>
</article>

<article class="forum-post" id="p555">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-06 22:05 UTC">2008-10-06 22:05 UTC</time></header>
<h3>Re: fuzzy in dspic 30f4011</h3>
<div class="forum-post-body">I obtain a datatype error. Most (or all) blockset from the fuzzy logic can only take floating point variables.<br>
<br>
<br>
<br>
Btw, I don't think that you will get an efficient using blocks that compute trigonometric or exponential like function... You may replace the buzzy logic blocks with optimized look up table.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p556">
<header><strong>macroevil</strong><time datetime="2008-10-07 02:06 UTC">2008-10-07 02:06 UTC</time></header>
<h3>Re: fuzzy in dspic 30f4011</h3>
<div class="forum-post-body">mr lubin.<br>
<br>
<br>
<br>
thaks..but i still trying make a control with fuzzy in a dspic, it's work but ony in some cases, when i configure the FIS with only one input and one output, and two rules(mamdani method).....<br>
<br>
<br>
<br>
do you have any example using FIS with mamdani metho..???<br>
<br>
<br>
<br>
thanks a lot......this toolbox it's a great job congratulations...!!<br>
<br>
<br>
<br>
att:<br>
<br>
<br>
<br>
César Jiménez</div>
</article>

<article class="forum-post" id="p557">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-07 18:05 UTC">2008-10-07 18:05 UTC</time></header>
<h3>Re: fuzzy in dspic 30f4011</h3>
<div class="forum-post-body">Hi César,<br>
<br>
<br>
<br>
I do not have any example using fuzzy logic or "FIS".</div>
</article>

