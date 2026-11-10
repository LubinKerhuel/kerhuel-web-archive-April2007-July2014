---
title: "dsPIC Master error"
url: "/forum/topic/437/"
archiveKind: "topic"
---
# dsPIC Master error

Forum : [General Remark and Questions](/forum/#forum-1)

13 message(s) · archive en lecture seule

<article class="forum-post" id="p1683">
<header><strong>whatthehack</strong><time datetime="2011-09-08 16:15 UTC">2011-09-08 16:15 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I'm using Matlab 2007b with Windows7 64. The Installation seemed to be ok. But when I want to choose the Master I always get the Matlab error message:<br>
<br>
<br>
<br>
Error evaluating 'OpenFcn' callback of Master block (mask) 'Master'. Index exceeds matrix dimensions.<br>
<br>
<br>
<br>
I would be glad if someone could tell me what's going wrong.</div>
</article>

<article class="forum-post" id="p1685">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-09 07:11 UTC">2011-09-09 07:11 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">Which blockset version are you working with ?<br>
<br>
Can you compile the files in example directory ? (there is a m script to compile them all at once !)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1687">
<header><strong>whatthehack</strong><time datetime="2011-09-09 08:45 UTC">2011-09-09 08:45 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">I installed it with: install_dsPIC_R2007b.<br>
<br>
<br>
<br>
The example all result in the same error after some warnings. I post it for the first example at the end.<br>
<br>
<br>
<br>
In the examples I can open the "Master Block" and change it. If I copy the "Master Block" into my model, it seems to work. But no compilation.<br>
<br>
<br>
<br>
Peter<br>
<br>
<br>
<br>
K&gt;&gt; <br>
<br>
Warning: 'slprj' is a directory.  Use rmdir to delete directories.<br>
<br>
&gt; In CompileAllModels at 4<br>
<br>
Warning: File 'Data_Login_Matlab.hex' not found.<br>
<br>
&gt; In CompileAllModels at 27<br>
<br>
***** Solver Mode change from Auto to SingleTasking (this mode allows single rate and multirate). See help to get the difference with the MultiTasking mode which is now supported by the blockset *****<br>
<br>
Old gmake exist, but newly GMAKE set at : C:\PROGRA~2\MATLAB\R2007b\bin\win32\gmake<br>
<br>
PNumber of I/O PINs used : 2<br>
<br>
TModel configured...<br>
<br>
sources files not found. MPLAB project file not created.<br>
<br>
K&gt;&gt; <br>
<br>
<br>
<br>
and the important error:<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'Data_Login_Matlab'. MATLAB error message:<br>
<br>
Error using ==&gt; make_rtw<br>
<br>
Too many output arguments.</div>
</article>

<article class="forum-post" id="p1688">
<header><strong>whatthehack</strong><time datetime="2011-09-09 09:18 UTC">2011-09-09 09:18 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">Additionally:<br>
<br>
<br>
<br>
For all the dsPIC33 I tried, I get: No CAN peripheral on ...<br>
<br>
<br>
<br>
For dsPIC30 it works.</div>
</article>

<article class="forum-post" id="p1689">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-09 10:01 UTC">2011-09-09 10:01 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : whatthehack</header>In the examples I can open the "Master Block" and change it. If I copy the "Master Block" into my model, it seems to work. But no compilation.</blockquote><br>
<br>
You need to set the Code Generation target : simulink configuration, pannel Code Generation, set it to dsPIC or pic32...<br>
<br>
a yellow block is capable of configuring the siumlink model automatically if you add it to your model.<br>
<br>
<br>
<pre><code>K&gt;&gt;
Warning: 'slprj' is a directory. Use rmdir to delete directories.
&gt; In CompileAllModels at 4
Warning: File 'Data_Login_Matlab.hex' not found.
&gt; In CompileAllModels at 27
***** Solver Mode change from Auto to SingleTasking (this mode allows single rate and multirate). See help to get the difference with the MultiTasking mode which is now supported by the blockset *****
Old gmake exist, but newly GMAKE set at : C:\PROGRA~2\MATLAB\R2007b\bin\win32\gmake
PNumber of I/O PINs used : 2
TModel configured...
sources files not found. MPLAB project file not created.
K&gt;&gt; </code></pre><br>
Could you compile without debug mode (K&gt;&gt; mean debug I guess ?)  and print out the complete error message ?<br>
<br>
It's difficult to make out what's happening there.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1690">
<header><strong>whatthehack</strong><time datetime="2011-09-09 15:30 UTC">2011-09-09 15:30 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body"><blockquote>You need to set the Code Generation target : simulink configuration, pannel Code Generation, set it to dsPIC or pic32...<br>
<br>
a yellow block is capable of configuring the siumlink model automatically if you add it to your model.</blockquote><br>
<br>
In all cases there was set dspic.tlc.<br>
<br>
<br>
<br>
I tried the same with Matlab2007b(32bit) and Matlab2010b (64bit), both on windows7 (64bit). During opening of the model I get a lot of warnings, see: <br>
<br>
In both cases during incremental build for the example Data_Login_Matlab a new info-window opens with an error message:<br>
<br>
<br>
<br>
2007b:<br>
<br>
<span style="color:#0000ff">Error building Real-Time Workshop target for block diagram 'Data_Login_Matlab'. MATLAB error message:<br>
<br>
Error using ==&gt; make_rtw<br>
<br>
Too many output arguments.</span><br>
<br>
<br>
<br>
2010b:<br>
<br>
<span style="color:#0000ff">Real-Time Workshop Embedded Coder is not licensed or not installed. The current target is: C:\Program Files\MATLAB\toolbox\dspic\dspic\dspic.tlc</span><br>
<br>
<br>
<br>
And in both cases for dspic33fj128gp802 (or other pic33) I get no CAN</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/437-dsPIC2007b.txt">Pièce jointe : dsPIC2007b.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/438-dsPIC2010b.txt">Pièce jointe : dsPIC2010b.txt</a></p>
</article>

<article class="forum-post" id="p1691">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-09 15:51 UTC">2011-09-09 15:51 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">don't pay attention to warning message at model opening.<br>
<br>
<br>
<br>
I do not understand the message you obtain on matlab 2007b.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : whatthehack</header>Real-Time Workshop Embedded Coder is not licensed or not installed. The current target is: C:\Program Files\MATLAB\toolbox\dspic\dspic\dspic.tlc</blockquote>You need to have Embedded Coder installed on matlab to have the dsPIC blockset work. dsPIC blockset works on top of RTW Embedded Coder.<br>
<br>
<br>
<br>
Maybe, you do not have also Embedded Coder on matlab 2007b ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1692">
<header><strong>whatthehack</strong><time datetime="2011-09-09 16:09 UTC">2011-09-09 16:09 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body"><blockquote>Real-Time Workshop Embedded Coder is not licensed or not installed. The current target is: C:\Program Files\MATLAB\toolbox\dspic\dspic\dspic.tlc</blockquote><br>
<br>
is the error message with 2010b.<br>
<br>
<br>
<br>
I have the RTW coder for both versions<br>
<blockquote>Real-Time Workshop                                    Version 7.0        (R2007b)<br>
</blockquote><br>
<blockquote>Real-Time Workshop                                    Version 7.6        (R2010b)<br>
</blockquote><br>
<br>
My dSpace-System works fine with both versions</div>
</article>

<article class="forum-post" id="p1693">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-09 16:13 UTC">2011-09-09 16:13 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">There is <br>
<br>
Real Time Workshop and <br>
<br>
Real Time Workshop Embedded Coder (renamed Embedded Coder on last matlab version)<br>
<br>
<br>
<br>
RTW EC works on top of RTW. In other word, you need them both.<br>
<br>
Do you have RTW Embedded Coder ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1695">
<header><strong>whatthehack</strong><time datetime="2011-09-10 11:14 UTC">2011-09-10 11:14 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I have to apologize. I didn't check this :( . For what reason ever the embedded coder was not installed. Now it is!<br>
<br>
<br>
<br>
Now principally everything works fine but in the examples Data_Login_Matlab, Servo_ADC, Servo_Sinus I get the following error:<br>
<br>
<br>
<br>
<span style="color:#0000ff">Servo_ADC_main.c:34: error: syntax error before numeric constant <br>
<br>
Servo_ADC_main.c: In function '_FICD': <br>
<br>
Servo_ADC_main.c:36: error: syntax error before '{' token <br>
<br>
gmake: *** [Servo_ADC_main.o] Error 255 </span><br>
<br>
<br>
<br>
And very important for me too: How do I get the CAN-Interface with an 33fj128gp802?<br>
<br>
<br>
<br>
Thanks a lot<br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p1696">
<header><strong>whatthehack</strong><time datetime="2011-09-11 09:44 UTC">2011-09-11 09:44 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">Well, I think I found the reason for the compiler error. It seems that from mplabc30 v3.25 to v3.30 the name of FICD changed to ICD (but only for dsp30f3xxx up to 6xxx :?: ).<br>
<br>
<br>
<br>
Remains 1 problem for me at the moment: no CAN for my dsp33.</div>
</article>

<article class="forum-post" id="p1766">
<header><strong>LubinKerhuel</strong><time datetime="2011-12-19 12:46 UTC">2011-12-19 12:46 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">This is correct.<br>
<br>
<br>
<br>
ICD will turn back to FICD in next Microchip compiler (v3.31) comming soon.<br>
<br>
Thus I do not correct this problem for now.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1780">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 09:23 UTC">2012-01-12 09:23 UTC</time></header>
<h3>Re: dsPIC Master error</h3>
<div class="forum-post-body">Compiler C30 v3.31 is released.<br>
<br>
Blockset were updated accordingly. Download latest <a href="/wiki/download/">blockset version (3.7c)</a> with the <a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1406&amp;dDocName=en010065">C30 compiler v3.31</a>.<br>
<br>
<br>
<br>
Everything should be Ok now.<br>
<br>
Lubin</div>
</article>

