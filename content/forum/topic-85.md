---
title: "Question about I2C"
url: "/forum/topic/85/"
archiveKind: "topic"
---
# Question about I2C

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p216">
<header><strong>johan.b</strong><time datetime="2008-02-15 07:49 UTC">2008-02-15 07:49 UTC</time></header>
<div class="forum-post-body">Good morning all, <br>
<br>
<br>
<br>
I have tried to use the I2C Master for my application and I have some questions concerning it. <br>
<br>
My dspic reads I2C data, but the sequence of data changes as a function of the operating mode. <br>
<br>
<br>
<br>
The state machine has 6 modes and these modes are identified by numbers: 1,2,3,4,5 and 6 <br>
<br>
<br>
<br>
In practice I have 2 sequences: <br>
<br>
<br>
<br>
- The 1st for the operating mode numbers 2, 4 and 6. The dspic must read 12 words in these modes.<br>
<br>
- The 2nd for the operating mode numbers 1, 3 and 5. The dspic must read 18 words in these modes. <br>
<br>
 <br>
<br>
At present, I have no available simulink model and I don't see how to manage this with the I2C master. <br>
<br>
<br>
<br>
Maybe that anybody can help me ? Thank you in advance.<br>
<br>
<br>
<br>
Johan</div>
</article>

<article class="forum-post" id="p227">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-18 22:10 UTC">2008-02-18 22:10 UTC</time></header>
<h3>Re: Question about I2C</h3>
<div class="forum-post-body">Hi Johan,<br>
<br>
<br>
<br>
On the example I have build, I read only <br>
<br>
- 4 data for states 1 ; 3 and 5<br>
<br>
- 2 data for states 2 ; 3 and 6<br>
<br>
But you can easily adapt it to read 18 and 12 data.<br>
<br>
<br>
<br>
I use an Enabled Subsystem to choose wether I am reading 4 or 2 data.<br>
<br>
<br>
The model : <br>
<br>
I use a bus to gather the data. When reading only 2 data, I place 0 into into the unfilled data.<br>
<br>
Using a bus with a constant width of 4 is up to you. You could use the I2C data in a different way.<br>
<br>
<br>
The merge block output the most recent data (refere to simulink help)<br>
<br>
<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/25-Enable_Subsystem.png">Pièce jointe : Enable_Subsystem.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/26-Model_General.png">Pièce jointe : Model_General.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/27-FSM_1_3_5.png">Pièce jointe : FSM_1_3_5.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/28-FSM_2_4_6.png">Pièce jointe : FSM_2_4_6.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/29-I2C_MultipleSequence_FinitStateMachine.mdl">Pièce jointe : I2C_MultipleSequence_FinitStateMachine.mdl</a></p>
</article>

<article class="forum-post" id="p238">
<header><strong>johan.b</strong><time datetime="2008-02-21 08:25 UTC">2008-02-21 08:25 UTC</time></header>
<h3>Re: Question about I2C</h3>
<div class="forum-post-body">Hello Lubin and thank you for your answer. <br>
<br>
I will test your model and adapt it to my need.<br>
<br>
Thank you.<br>
<br>
Johan</div>
</article>

