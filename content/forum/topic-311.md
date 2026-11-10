---
title: "Trying a simple model"
url: "/forum/topic/311/"
archiveKind: "topic"
---
# Trying a simple model

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1256">
<header><strong>Jodoku</strong><time datetime="2010-06-24 21:12 UTC">2010-06-24 21:12 UTC</time></header>
<div class="forum-post-body">I have taken a simple portion from one of the included examples with the blockset to create a blinking LED. I have a dsPIC30f4011 and a dsPICDEM2 board, along with MPLAB ICD 2.  No matter what, I can't get a single LED to light up.  I am very new to this, and I need some direction.  I've attached the simulink model I've been using.  Thank you!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/346-blink_led.mdl">Pièce jointe : blink_led.mdl</a></p>
</article>

<article class="forum-post" id="p1257">
<header><strong>LubinKerhuel</strong><time datetime="2010-06-27 22:42 UTC">2010-06-27 22:42 UTC</time></header>
<h3>Re: Trying a simple model</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
You model is not far from working.<br>
<br>
I think that the problem is the oscillator mode that seems not correct.<br>
<br>
Do you use a quartz. If so, Oscillator mode should be something like XT, XT with Pll or HS. See 30f4011 doc to get further information about oscillator.<br>
<br>
<br>
<br>
Lubin</div>
</article>

