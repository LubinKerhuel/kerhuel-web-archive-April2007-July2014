---
title: "Some help needed reg  data conversion for this model"
url: "/forum/topic/96/"
archiveKind: "topic"
---
# Some help needed reg  data conversion for this model

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p258">
<header><strong>barryforever</strong><time datetime="2008-03-06 11:17 UTC">2008-03-06 11:17 UTC</time></header>
<div class="forum-post-body">Hello<br>
<br>
Im a Student doing my undergraduation in Instrumentation and Control Engineering .Im recently developing a smart sensor using your toolbox.<br>
<br>
I did build a simple smart sensor but it failed to compile it gave me the following error .<br>
<br>
<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'smart_sensor'. MATLAB error message:
Error using ==&gt; rtwgen
--&gt; Error reported by S-function 'dsPIC_UART_TX_Labview_Matlab' in 'smart_sensor/TX Output Multiplexed for Matlab // Labview':
Invalid input or output port data type.
--&gt; An error occurred while propagating data type 'double' from 'smart_sensor/Add', output port 1.</code></pre><br>
<br>
Can you debug the model and give me the corrected simulink model ..<br>
<br>
please also tell me what is the error that i did .<br>
<br>
i have attached the model to this thread</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/34-smart_sensor.mdl">Pièce jointe : smart_sensor.mdl</a></p>
</article>

<article class="forum-post" id="p259">
<header><strong>barryforever</strong><time datetime="2008-03-06 15:07 UTC">2008-03-06 15:07 UTC</time></header>
<h3>Re: Some help needed reg  data conversion for this model</h3>
<div class="forum-post-body">why did you ask me to change the switch box ? is there any specific reasons for it</div>
</article>

<article class="forum-post" id="p262">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-07 00:19 UTC">2008-03-07 00:19 UTC</time></header>
<h3>Re: Some help needed reg  data conversion for this model</h3>
<div class="forum-post-body">Barry,<br>
<br>
<br>
<br>
I did not understand what the purpose of the model you posted is.<br>
<br>
However, I corrected few tricks. But I guess that it will not do the job you are expecting.<br>
<br>
<br>
<br>
I posted a second model to use for simulation. I replaced the ADC block by a sinus generator block. It makes you able to simulates the "program" execution if a sinus signal (between 0V and +Vcc) was connected to the ADC input of the dsPIC.<br>
<br>
<br>
<br>
I suggest to modify this model until you get the expected the correct behavior.<br>
<br>
Once simulation is OK, just cut-past this model into the mdl file used to program the dsPIC. Few tricks could be necessary to make it compiling. <br>
<br>
(For advanced user, it is possible to use a unique mdl file for both simulation and code generation using the "Environment Controller" block that you can find in the standard simulink library)<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : barryforever</header>why did you ask me to change the switch box ? </blockquote><br>
Isn't it  more simple ?<br>
<br>
C code generated is also more simple thus more efficient.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/35-smart_sensor.mdl">Pièce jointe : smart_sensor.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/36-smart_sensor_Simulation.mdl">Pièce jointe : smart_sensor_Simulation.mdl</a></p>
</article>

