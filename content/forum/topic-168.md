---
title: "Exemple QEI without Index, DsPic33FJ256MC710"
url: "/forum/topic/168/"
archiveKind: "topic"
---
# Exemple QEI without Index, DsPic33FJ256MC710

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p586">
<header><strong>Ender</strong><time datetime="2008-10-23 16:53 UTC">2008-10-23 16:53 UTC</time></header>
<div class="forum-post-body">.<br>
<br>
Inspired from the <a href="/forum/topic/100/">Malife topic</a>, I did a <strong>QIE model on the DsPic33FJ256MC710</strong> .<br>
<br>
<br>
<br>
But the intializing function _QEIInt_ run more than one time, in spite of the C call function step time is "inf"  :cry: <br>
<br>
Exemple, If you remove the comment to set available the line :  <br>
<br>
 __ // POSCNT = 0x8000;                // Set Current Position to 8000 does't work, reset and speed effect ???__*<br>
<br>
The counter is set any time at 0x8000<br>
<br>
  <br>
<br>
Could you help me Lunbin  :?:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/129-QEI_MC_Uart115200_8MQ.mdl">Pièce jointe : QEI_MC_Uart115200_8MQ.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/130-QEI_Functions.c">Pièce jointe : QEI_Functions.c</a></p>
</article>

<article class="forum-post" id="p587">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-23 19:04 UTC">2008-10-23 19:04 UTC</time></header>
<h3>Re: Exemple QEI without Index, DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi Ender.<br>
<br>
<br>
<br>
This version should works.<br>
<br>
Only 2 changes in the simulink configuration options : <br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; Optimization ==&gt;<br>
<br>
- Check Inline parameters<br>
<br>
- Then, check Inline Invariant signals<br>
<br>
( This is the exact name with matlab 2008a)<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/131-QEI_MC_Uart115200_8MQ.mdl">Pièce jointe : QEI_MC_Uart115200_8MQ.mdl</a></p>
</article>

<article class="forum-post" id="p589">
<header><strong>Ender</strong><time datetime="2008-10-24 17:01 UTC">2008-10-24 17:01 UTC</time></header>
<h3>Re: Exemple QEI without Index, DsPic33FJ256MC710</h3>
<div class="forum-post-body">Yes, It works, Thanks a lot.</div>
</article>

