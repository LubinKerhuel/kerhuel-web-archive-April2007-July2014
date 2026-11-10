---
title: "Timeout for Input Capture Block"
url: "/forum/topic/240/"
archiveKind: "topic"
---
# Timeout for Input Capture Block

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p917">
<header><strong>bmairs</strong><time datetime="2009-07-27 19:16 UTC">2009-07-27 19:16 UTC</time></header>
<div class="forum-post-body">Currently the input capture block holds its output values if the input signals remains constant as there are no rising or falling edges to trigger an update of the values. In working with radio controlled electronics, a lost connection means that the PWM signal input is now ground. It would be nice if you could specify a timeout duration in the block where the value would be reset to 0 if no events happened. This would make it easy to implement a failsafe for your vehicle when using radio controlled equipment.</div>
</article>

<article class="forum-post" id="p930">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 10:35 UTC">2009-07-30 10:35 UTC</time></header>
<h3>Re: Timeout for Input Capture Block</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
Thanks for the suggestion. Here is the solution I am using (see attached file : figure and model)<br>
<br>
<br>
<br>
Model time step is 1ms.<br>
<br>
The RC PWM signal arrived with a period of 20ms.<br>
<br>
Thus, The resetable integrator is set to 0 each time one pulse arrived.<br>
<br>
It increment 1 each ms. If there is no RC connection break, its value should never goes above 20ms. (we take a security and set the value at 49)<br>
<br>
While the integrator has a value below 49, I considere that the RC signal is OK. otherwise, I place the system in protection (with the final switch)<br>
<br>
<br>
<br>
My original design also takes into account the value of the duty cycle that should go astray [1 2] ms limits. I removed it to make the system more clear.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/260-RC_protect.png">Pièce jointe : RC_protect.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/259-RC_protect.mdl">Pièce jointe : RC_protect.mdl</a></p>
</article>

<article class="forum-post" id="p933">
<header><strong>bmairs</strong><time datetime="2009-07-30 18:02 UTC">2009-07-30 18:02 UTC</time></header>
<h3>Re: Timeout for Input Capture Block</h3>
<div class="forum-post-body">You model works exactly how the custom C code I wrote works, it's just nicer because it's all contained within Simulink.<br>
<br>
<br>
<br>
My argument for this being built into the block is because I would expect a 0 to come out of the block for the uptime if the signal went to DC. Would it be possible to integrate the extra blocks you added to get this to work into the input capture block itself? Then the input capture block would take an extra parameter, how long the timeout should be. That would make it much easier to work with PWM signals I think.</div>
</article>

<article class="forum-post" id="p935">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 19:45 UTC">2009-07-30 19:45 UTC</time></header>
<h3>Re: Timeout for Input Capture Block</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : bmairs</header>Would it be possible to integrate the extra blocks you added to get this to work into the input capture block itself?</blockquote><br>
The strategy is to give user the <strong>more flexiblity</strong>. Thus, any "high level" function that could be done <strong>efficiently</strong> with simulink should be done this way. I mean, there will be no difference in the final C code between the two version.<br>
<br>
I think that adding a specific function (only RC system has that)  like this one to the block would add confusion on the use of the block.<br>
<br>
Realizing the function with simulink allow more flexibility, for example, you may imagine that if you loose only one RC receiver channel, you will block all system and not just that channel...<br>
<br>
<br>
<br>
However, A library could be done with high the high level function you propose. You can imagine have the subsystem with the IC block and the protection logic and add a <strong>mask</strong> to the subsystem to set-up parameters and make it like a <strong>super IC block</strong> !  If you wish to publish such library, you are encourage to do it and provide the link (or publish it directly here) !<br>
<br>
<br>
<br>
Lubin</div>
</article>

