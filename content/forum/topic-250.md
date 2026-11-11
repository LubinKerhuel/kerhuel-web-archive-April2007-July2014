---
title: "PWM motor output error"
url: "/forum/topic/250/"
archiveKind: "topic"
---
# PWM motor output error

Forum : [General Remark and Questions](/forum/#forum-1)

17 message(s) · archive en lecture seule

<article class="forum-post" id="p974">
<header><strong>jirka</strong><time datetime="2009-10-27 06:23 UTC">2009-10-27 06:23 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I have a problem with setting of processor type dsPIC30f6015. I can't set PWM motor output. I don't know how this problem removes. I placed print screen of this error at attachment. Then I would like asking you a possibility to set-up of dead time on PWM. I don't find this options in setting of PWM motor output block. I used R2008a version of Matlab. Thanks for your help.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/272-errors_PWM_motor_block.PNG">Pièce jointe : errors_PWM_motor_block.PNG</a></p>
</article>

<article class="forum-post" id="p975">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-27 10:08 UTC">2009-10-27 10:08 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Jirka,<br>
<br>
<br>
<br>
Thanks for the screen shoot.<br>
<br>
This seems to be a bug from the blockset since the error message talk about <em>PWM motor 2</em> peripheral, but the PWM motor dialog is set on<em> PWM motor 1</em> !<br>
<br>
<br>
<br>
Thus, I'll try to look at this soon. Could you upload your simulink .mdl file, It will help to track that bug.<br>
<br>
<br>
<br>
For the dead time, I did not implemented it yet as I usually use this block just for generating PWM, not for motor control. I will try to have a look within few weeks. If you have any suggestion on how you want to have it implemented (as a constant set in the dialog box (best I think), as a block input ?)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p976">
<header><strong>jirka</strong><time datetime="2009-10-27 13:15 UTC">2009-10-27 13:15 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
 <br>
<br>
Thanks for answer. I upload the mdl file as you required.<br>
<br>
<br>
<br>
For the dead time, I don't have special requirement. I think that it implement as constant set in the dialog box is good.<br>
<br>
<br>
<br>
Jirka</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/273-dspic30f6015.mdl">Pièce jointe : dspic30f6015.mdl</a></p>
</article>

<article class="forum-post" id="p977">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-27 22:28 UTC">2009-10-27 22:28 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Jirka,<br>
<br>
<br>
<br>
I compiled successfully this model on my system without doing anything particular.<br>
<br>
<br>
<br>
Could you try to download the latest blockset version and test it again ?<br>
<br>
<br>
<br>
Let me know if you still get the error.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p978">
<header><strong>jirka</strong><time datetime="2009-10-29 07:57 UTC">2009-10-29 07:57 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I reinstall blockset for dspic and now it is all right. Thank you for help.<br>
<br>
<br>
<br>
Now I waiting only on setting of deat time so I can try to control BLDC motor. Could you give know when you'll have complete setting for dead time?<br>
<br>
Once again thank you for everything.<br>
<br>
<br>
<br>
Jirka</div>
</article>

<article class="forum-post" id="p1001">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-17 14:11 UTC">2009-11-17 14:11 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Jirka<br>
<br>
<br>
<br>
I implemented the Dead time on the PWM motor peripheral.<br>
<br>
Please test the new blockset version and let me know if the way it is implemented is usefull for BLDC motor control.<br>
<br>
download link : <a href="/wiki/download/">http://archive.kerhuel.eu/wiki/Download</a><br>
<br>
<br>
<br>
It would be great to get an example of BLDC control using this blockst. Would it be possible to post a model here, or even better, on the wiki ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1004">
<header><strong>jirka</strong><time datetime="2009-11-22 17:44 UTC">2009-11-22 17:44 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
thanks for the deat time, but I'm very busy now.I will try to have a look within few weeks.<br>
<br>
<br>
<br>
Jirka</div>
</article>

<article class="forum-post" id="p1734">
<header><strong>william_yan</strong><time datetime="2011-11-03 09:39 UTC">2011-11-03 09:39 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : jirka</header>Hi Lubin,<br>
<br>
I have a problem with setting of processor type dsPIC30f6015. I can't set PWM motor output. I don't know how this problem removes. I placed print screen of this error at attachment. Then I would like asking you a possibility to set-up of dead time on PWM. I don't find this options in setting of PWM motor output block. I used R2008a version of Matlab. Thanks for your help.</blockquote><br>
hi lubin...<br>
<br>
<br>
<br>
i have a smilar project with the above but  i got another error showing this erro for PWM.. please advice me .. i really need help ..i did attach the error screem shot and the .mdl fine for your red.. hope u will help me :))<br>
<br>
<br>
<br>
regards<br>
<br>
William</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/450-error.JPG">Pièce jointe : error.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/451-FYP_pwm_model.mdl">Pièce jointe : FYP_pwm_model.mdl</a></p>
</article>

<article class="forum-post" id="p1735">
<header><strong>william_yan</strong><time datetime="2011-11-03 09:43 UTC">2011-11-03 09:43 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">i will be using with dsPIC33fJ64MC802 and microstick .</div>
</article>

<article class="forum-post" id="p1863">
<header><strong>akwer</strong><time datetime="2012-03-16 14:16 UTC">2012-03-16 14:16 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I have a bug with PWM block set.<br>
<br>
I use dsPIC Toolbox for Matlab R2011b.<br>
<br>
I created new folder "blocks2"and put it in a file "dsPIC_PWM_motor_callback_InitMask.p".<br>
<br>
The "dsPIC_PWM_motor_callback_InitMask.p" is copy "dsPIC_PWM_Motor_callback_InitMask.p" from folder "blocks".<br>
<br>
Then I added the path to the Matlab search Path.<br>
<br>
It solved the my problem. Compilation was successful.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/495-1.png">Pièce jointe : 1.png</a></p>
</article>

<article class="forum-post" id="p1881">
<header><strong>LubinKerhuel</strong><time datetime="2012-04-27 00:22 UTC">2012-04-27 00:22 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Akwer,<br>
<br>
<br>
<br>
Matlab is now case sensitive. <br>
<br>
I corrected few problem caused by this change.<br>
<br>
<br>
<br>
You might be using an old blockset version. Please update and let me know if the problem is still there.<br>
<br>
<br>
<br>
The file dsPIC_PWM_Motor_callback_InitMask.p has M of Motor upper case in latest blockset release.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1972">
<header><strong>nasrullah</strong><time datetime="2012-12-26 01:50 UTC">2012-12-26 01:50 UTC</time></header>
<h3>PWM on 32MX460F512L</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
It is true that there is no PWM motor peripheral available on chip 32MX460F512L?</div>
</article>

<article class="forum-post" id="p1991">
<header><strong>ruxania</strong><time datetime="2013-03-28 03:44 UTC">2013-03-28 03:44 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">I'm only a freshmen without any knowledge in building stuff. I want to build a motor in which can vibrate at a given frequency. It will be helpful if the materials are cheap to get. I was looking at an electromagnetic linear motor but i cant find one in which i can buy.<br>
<br>
______________________<br>
<br>
<a href="http://www.RecipeInstant.com">healthy dinner recipes</a> ~ <a href="http://cookingway.com/">simple recipes for dinner</a> ~ <a href="http://cookingway.com/">low fat recipes</a></div>
</article>

<article class="forum-post" id="p2014">
<header><strong>chiclothe</strong><time datetime="2013-09-06 06:29 UTC">2013-09-06 06:29 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Thanks for the screen shoot.</div>
</article>

<article class="forum-post" id="p2016">
<header><strong>cheaproomd</strong><time datetime="2013-09-09 05:51 UTC">2013-09-09 05:51 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Thus, I'll try to look at this soon. Could you upload your simulink .mdl file, It will help to track that bug.</div>
</article>

<article class="forum-post" id="p2027">
<header><strong>cheaproomd</strong><time datetime="2013-09-25 06:11 UTC">2013-09-25 06:11 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Thanks for the screen shoot.</div>
</article>

<article class="forum-post" id="p2028">
<header><strong>cheaproomd</strong><time datetime="2013-09-30 03:50 UTC">2013-09-30 03:50 UTC</time></header>
<h3>Re: PWM motor output error</h3>
<div class="forum-post-body">Thanks for the screen shoot.</div>
</article>

