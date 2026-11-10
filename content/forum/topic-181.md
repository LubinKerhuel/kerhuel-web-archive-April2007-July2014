---
title: "Did anyone implement a controller in dsPIC by this toolbox?"
url: "/forum/topic/181/"
archiveKind: "topic"
---
# Did anyone implement a controller in dsPIC by this toolbox?

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

16 message(s) · archive en lecture seule

<article class="forum-post" id="p626">
<header><strong>gladiac</strong><time datetime="2008-12-08 13:41 UTC">2008-12-08 13:41 UTC</time></header>
<div class="forum-post-body">Did anyone implement a controller in dsPIC by this toolbox? I was trying some times but still got some problems. I use dsPIC30f6014A device. If I use 'transfer function' block of Simulink simply or create a 'direct form' model for controllers, they don't work in practice. <br>
<br>
Only when I use a simple P, PI or 1st order model, the controller works just OK in practice. Also error tracking is not good in this situation. <br>
<br>
For all models, sample time was specified. The 'signal type' was setup as 'double precision', because there was a big number range from reference input to controller output in my case. I'm not sure above modelling and setups are exactly correct. Did anyone have related experiences? And Mr. Lubin, do you have any advice for implementing controller by your toolbox? Thanks for all!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/150-direct%20form.jpg">Pièce jointe : direct form.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/151-discrete%20TF.jpg">Pièce jointe : discrete TF.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/152-one.jpg">Pièce jointe : one.jpg</a></p>
</article>

<article class="forum-post" id="p627">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-08 14:11 UTC">2008-12-08 14:11 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hello,<br>
<br>
Thanks for the images.<br>
<br>
<br>
<br>
I made many controllers (PID or state space model) that work.<br>
<br>
<br>
<br>
Try to: <br>
<br>
- show sample time of each block (use sample time color).<br>
<br>
- Check that 1/Z works at the right sample time (should be -1 for inherited or you simulink sample time value) default value is 1 (for 1 second) and is a cause of error!<br>
<br>
<br>
<br>
- Also, note that double are implemented as single in the dsPIC except if you add the block "Compiler Configuration" from the dsPIC blockset and check the box to implement Double in 64bits instead of 32. (But I do not think that is the error, and I would advise to keep 32 bits)<br>
<br>
<br>
<br>
If it did not solved the problem, could you upload the simulink files for theses model? <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p628">
<header><strong>gladiac</strong><time datetime="2008-12-08 15:55 UTC">2008-12-08 15:55 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I think I have done the same setup for my models. It's better to upload the model, but always errors occur  when I upload a .mdl<br>
<br>
file. Anyway, I have sent the model to you by [adresse e-mail retirée], please take a look if possible.<br>
<br>
<br>
<br>
cheers,<br>
<br>
<br>
<br>
gladiac</div>
</article>

<article class="forum-post" id="p629">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-08 19:49 UTC">2008-12-08 19:49 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Gladiac,<br>
<br>
<br>
<br>
I did not see obvious error the simulink file you sent.<br>
<br>
But I could perhaps help anyway. First of all, I will not check the controller stability and so on... I supposed that it is Ok.<br>
<br>
<br>
<br>
I have two remarks:<br>
<br>
First, on the use of data type double: despite it is easier to use than fixed point calculation, strange behavior may appears when <strong>calculation </strong>involving both <strong>very large value with very low value appears</strong>.  <br>
<br>
<br>
<br>
Then, a second remark: the PID implemented has no reset or saturation limits (or anti windup) on the 'I' term. As soon as the controller is switch off (See switch on the model), I supposed that the integrator reach a very high value. Cf to remark 1, you may get into trouble then.<br>
<br>
<br>
<br>
If your electronic board has an UART that you can connect to your PC, I would suggest using the Tx-Matlab block to see what happen on several variables at the same time.  (Convert value into int16 data type before sending through UART. <br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/158-Block_UART_Tx_Output_Multiplexed_MatlabLabview_1_.png">Pièce jointe : Block_UART_Tx_Output_Multiplexed_MatlabLabview[1].png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/159-controller.mdl">Pièce jointe : controller.mdl</a></p>
</article>

<article class="forum-post" id="p632">
<header><strong>gladiac</strong><time datetime="2008-12-08 20:01 UTC">2008-12-08 20:01 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Thank you very much, Lubin! I will try it tomorrow and let you know the result.</div>
</article>

<article class="forum-post" id="p635">
<header><strong>gladiac</strong><time datetime="2008-12-12 14:26 UTC">2008-12-12 14:26 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I have tried the dsPIC again. First, my controller worked OK on dSPACE before.So the cotnroller should be OK. Second,if I remove the 'saturation' block in model, output signal looks fine on oscilloscope. But on real testing,  behaviour is still bad.  I'm sitll checking problem include the hardware.<br>
<br>
<br>
<br>
cheers,<br>
<br>
gladiac</div>
</article>

<article class="forum-post" id="p677">
<header><strong>gladiac</strong><time datetime="2009-01-08 16:47 UTC">2009-01-08 16:47 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
The low order controller works OK  when using the update version toolbox.The high order one doesn't work. Still trying.</div>
</article>

<article class="forum-post" id="p715">
<header><strong>gladiac</strong><time datetime="2009-01-29 16:38 UTC">2009-01-29 16:38 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
Unfortunately, my dsPIC was broken two weeks ago and the new one just come a few days ago. So the problem has been delayed for a long time. Now I use the 'zpk(zeros-poles-gain)' block to implement the high order controller, and that works OK in real testing. Also I tried the 'state-space' block, it performaned like the general 'tf' blcok which doesn't work. Do you have any idea for that phenomenon and What's the difference between 'zpk','ss'and 'tf' block in implementation?    <br>
<br>
<br>
<br>
Cheers,<br>
<br>
<br>
<br>
Gladiac</div>
</article>

<article class="forum-post" id="p716">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-01 14:17 UTC">2009-02-01 14:17 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Gladiac<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : gladiac</header>What's the difference between 'zpk','ss'and 'tf' block in implementation? </blockquote><br>
<br>
I did not compared the C implementation of theses block yet. That would be interresting. Could you upload a model with your corrector as starting point to  compare ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p719">
<header><strong>gladiac</strong><time datetime="2009-02-02 15:35 UTC">2009-02-02 15:35 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
The file attached is the model of the controller. I put three different blocks with same one controller in it. <br>
<br>
<br>
<br>
Cheers<br>
<br>
Gladiac</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/195-controller.mdl">Pièce jointe : controller.mdl</a></p>
</article>

<article class="forum-post" id="p752">
<header><strong>malife</strong><time datetime="2009-02-11 19:11 UTC">2009-02-11 19:11 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 This seems to be quite an interesting comparison, would you post your results if/when you have them to see which is more efficient?<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p754">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-11 20:09 UTC">2009-02-11 20:09 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hello Gladiac, Mariano,<br>
<br>
<br>
<br>
I'am quite overloaded (Working on both the next blockset version and my PhD ...) forgot this thread. Sorry about that.<br>
<br>
Thanks Gladiac for the last model you posted. I'll try to have a look next week. (it is not urgent for anybody? )<br>
<br>
I'll report results If it is not already done by someone.<br>
<br>
As an interresting subject, that could be a case study to add in the wiki pages...<br>
<br>
<br>
<br>
Cheers<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p755">
<header><strong>Tchangov</strong><time datetime="2009-02-12 17:58 UTC">2009-02-12 17:58 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">The controller model presented has problem with the Gain 3; It must be negative...<br>
<br>
Gain 3 and Gain 2 MUST be negative...<br>
<br>
...and do not try any positive feedback design in your systems unlesss you are designing Variable Structure System Design...<br>
<br>
Todor</div>
</article>

<article class="forum-post" id="p756">
<header><strong>Tchangov</strong><time datetime="2009-02-12 18:08 UTC">2009-02-12 18:08 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">This Gain -koefficient in the first intrgrator feed back must be negative.<br>
<br>
...in both the Plant and the controller.<br>
<br>
The controller presented is not performing PI.<br>
<br>
If the Gain is negative then we have a first order filter responce added to Proportional K...<br>
<br>
Ones you have negative gain ofcourse. <br>
<br>
Then you will have an "I" component to "P", which will be working for 0.63 of the Time Cte for this First order structure. And no MORE...<br>
<br>
<br>
<br>
After that - in study State...this 1 Order will add extra proportional actuating...<br>
<br>
You will miss the "I" Integral component in PI...therefore, a big Static Error (studyState...Tracking...error.) will never be compensated to be ZERO.<br>
<br>
Back to Simulink...<br>
<br>
Lubin is right about using Integrators...always limit them...and be ready to reset the Initial Conditions !!!!!<br>
<br>
Happy Simulating,<br>
<br>
Todor</div>
</article>

<article class="forum-post" id="p759">
<header><strong>Tchangov</strong><time datetime="2009-02-12 22:23 UTC">2009-02-12 22:23 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Tchangov</header><br>
I have just derived the controller: It present a Proportional Derivative dynamics.  <br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
This Gain -koefficient in the first intrgrator feed back must be negative.<br>
<br>
...in both the Plant and the controller.<br>
<br>
The controller presented is not performing PI.<br>
<br>
If the Gain is negative then we have a first order filter responce added to Proportional K...<br>
<br>
Ones you have negative gain ofcourse. <br>
<br>
Then you will have an "I" component to "P", which will be working for 0.63 of the Time Cte for this First order structure. And no MORE...<br>
<br>
<br>
<br>
After that - in study State...this 1 Order will add extra proportional actuating...<br>
<br>
You will miss the "I" Integral component in PI...therefore, a big Static Error (studyState...Tracking...error.) will never be compensated to be ZERO.<br>
<br>
Back to Simulink...<br>
<br>
Lubin is right about using Integrators...always limit them...and be ready to reset the Initial Conditions !!!!!<br>
<br>
Happy Simulating,<br>
<br>
Todor</blockquote></div>
</article>

<article class="forum-post" id="p764">
<header><strong>gladiac</strong><time datetime="2009-02-23 16:42 UTC">2009-02-23 16:42 UTC</time></header>
<h3>Re: Did anyone implement a controller in dsPIC by this toolbox?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Thanks for your continuing attention.<br>
<br>
And Todor,<br>
<br>
Your explanation is right. But I don't think it will cause the problem, feedback loop of 'direct form' still can be negative. As 'sign' can be changed straight in 'gain' block. Actually, I put the negative cofficients in 'gain' blocks directly. The problem for the model first uploaded is not the compensator. The reason is my hardware is not supported by Lubin's blockset initially, when Lubin upgrade the blockset for me, the problem was solved. The controller with dsPIC woked fine in real machine testing.<br>
<br>
<br>
<br>
Cheers<br>
<br>
Gladiac</div>
</article>

