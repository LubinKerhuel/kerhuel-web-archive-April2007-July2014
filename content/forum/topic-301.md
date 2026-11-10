---
title: "Enable a code Block at 480Hz"
url: "/forum/topic/301/"
archiveKind: "topic"
---
# Enable a code Block at 480Hz

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1203">
<header><strong>jnewmill</strong><time datetime="2010-04-29 01:29 UTC">2010-04-29 01:29 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
 I'm using the dsPIC33FJ256 Explorer board.  I want to enable a block at 480Hz.  I can't use any of the simulation timers or signal generators.  Is there a way to use an on board timer to make an internal 480Hz signal using the block set?  Or do I have to look into the C code?<br>
<br>
<br>
<br>
Best ,<br>
<br>
<br>
<br>
  - Jared</div>
</article>

<article class="forum-post" id="p1205">
<header><strong>Ender</strong><time datetime="2010-04-29 05:11 UTC">2010-04-29 05:11 UTC</time></header>
<h3>Re: Enable a code Block at 480Hz</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
If the goal is a synchronization with another device you better have to use an Input or Output compare or the PWM peripheral. Can you give a better description of your project and the accuracy you want for the frequency? Because there is several solution, included to use an external clock, change or add a quartz etc…<br>
<br>
<br>
<br>
Attached a clumsy solution to get 480Hz with the original Explorer16  <br>
<ul>    One Led blinks at 1Hz, another at 480Hz with an error lower than 0.25%<br>
<br>
    I set the Master at his maximum speed, so 40MIPS<br>
<br>
    In configuration parameter the solver Fixed-step time to 0.00008s, cause it's an integer divider of 40e6<br>
<br>
   The pulse block sample base time is the same 0.00008s than the solver<br>
<br>
   The pulse period is 26 sample time, with 50% of duty cycle so 0.00008 * 26 = 0.00208s =&gt; 480.77 Hz</ul><br>
I didn’t test the code on a target, maybe tomorrow ;) So I can be wrong !</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/336-P480HZ.mdl">Pièce jointe : P480HZ.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/337-P480HZ.hex">Pièce jointe : P480HZ.hex</a></p>
</article>

<article class="forum-post" id="p1226">
<header><strong>resodad</strong><time datetime="2010-05-05 16:06 UTC">2010-05-05 16:06 UTC</time></header>
<h3>Re: Enable a code Block at 480Hz</h3>
<div class="forum-post-body">Hi Jared,<br>
<br>
I think you mean to say you want to enable a block when the frequency of an EXTERNAL signal equals 480Hz. Is that right?<br>
<br>
If so, you might try connecting the signal to an input capture pin. set up the input capture to output period (type [4]) and compare the signal period to a constant ("compare to constant" block) to generate a trigger signal.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1231">
<header><strong>Ender</strong><time datetime="2010-05-06 16:55 UTC">2010-05-06 16:55 UTC</time></header>
<h3>Re: Enable a code Block at 480Hz</h3>
<div class="forum-post-body">It just tried to measure the 8th Harmonic of a USA power line. But because he doesn't know how ........<br>
<br>
R.I.P Jared  :mrgreen:</div>
</article>

