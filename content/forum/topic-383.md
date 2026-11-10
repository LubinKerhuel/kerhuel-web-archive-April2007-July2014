---
title: "Simulink to dspic"
url: "/forum/topic/383/"
archiveKind: "topic"
---
# Simulink to dspic

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1547">
<header><strong>ELMAY</strong><time datetime="2011-04-15 13:27 UTC">2011-04-15 13:27 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
This is a model of a PWM rectifier in simulink I want to translate Blokset / MATLAB to program a dsPIC 30F4011 to Implement<br>
<br>
But when I reflected I do not find  output to the terminal dsPIC knowing that  input is a sine wave and ferquence 50 hz<br>
<br>
Can you help me about this problem?<br>
<br>
<br>
<br>
thanks<br>
<br>
<br>
<br>
Elmay</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/405-model_PWM.mdl">Pièce jointe : model_PWM.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/404-model_PWM_dspic.mdl">Pièce jointe : model_PWM_dspic.mdl</a></p>
</article>

<article class="forum-post" id="p1558">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-26 17:35 UTC">2011-04-26 17:35 UTC</time></header>
<h3>Re: Simulink to dspic</h3>
<div class="forum-post-body">Hi Elmay,<br>
<br>
<br>
<br>
I do not understand what your model is supposed to do.<br>
<br>
The input capture Up signal connected to a boolean data type conversion will provide you 1 until the Up period of the input signal is not 0.<br>
<br>
you might use the rising edge detection of this block. In the input capture block, you might set the "Change Detected on" option to 1 for rising edge (see block dialog box).<br>
<br>
<br>
<br>
You might also use only one block PWM_motor. Select three channels output. (output channel will be [1 2 3] )<br>
<br>
<br>
<br>
Lubin</div>
</article>

