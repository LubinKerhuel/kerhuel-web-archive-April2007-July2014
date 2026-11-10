---
title: "Error loading example"
url: "/forum/topic/315/"
archiveKind: "topic"
---
# Error loading example

Forum : [bug reports](/forum/#forum-8)

18 message(s) · archive en lecture seule

<article class="forum-post" id="p1276">
<header><strong>mickpowell</strong><time datetime="2010-07-21 13:31 UTC">2010-07-21 13:31 UTC</time></header>
<div class="forum-post-body">Using Embedded Target for MICROCHIP dsPIC V3.2b on a Windows XP3 machine and MATLAB R2006b: <br>
<br>
the following is reported in the MATLAB command window: <br>
<br>
<br>
<br>
Warning: Undefined function or method 'exist' for input arguments of type 'cell'.<br>
<br>
&gt; In C:\MATLAB\R2006b\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
Warning: In instantiating linked block 'FlexBoard_Blinking_Led/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'MCLR'.<br>
<br>
&gt; In C:\DSPIC_Lib\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; get_param<br>
<br>
block_diagram does not have a parameter named 'GMAKE_PLACE'.<br>
<br>
&gt; In C:\DSPIC_Lib\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
<br>
<br>
Please advise.</div>
</article>

<article class="forum-post" id="p1277">
<header><strong>LubinKerhuel</strong><time datetime="2010-07-21 19:39 UTC">2010-07-21 19:39 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">it seems to be <strong>only warning</strong> that are cause by the fact that example were created with an order blockset version.<br>
<br>
You just have to not pay attention to them. They should not appears once you'll save the model with your current blockset version.<br>
<br>
<br>
<br>
as soon as you do not get an error (not a warning) , you can go on...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1279">
<header><strong>mickpowell</strong><time datetime="2010-07-26 07:32 UTC">2010-07-26 07:32 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">I have ignored the warnings and saved the example model file.<br>
<br>
On double clicking the 'Master' block in the model, I get the following message in an 'Error' dialogue:<br>
<br>
<br>
<br>
Error evaluating 'Open Fcn' callback of Master block (mask) 'Master.<br>
<br>
Error using ==&gt; get_param<br>
<br>
block_diagram does not have a parameter named 'GMAKE_PLACE'.<br>
<br>
<br>
<br>
Please advise.</div>
</article>

<article class="forum-post" id="p1280">
<header><strong>LubinKerhuel</strong><time datetime="2010-07-26 09:01 UTC">2010-07-26 09:01 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">I uploaded on the website <a href="/wiki/download/">new version (3.2c) of the blockset</a>. Could you test with this last version and report if you still get the problem ?<br>
<br>
Thanks<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1281">
<header><strong>mickpowell</strong><time datetime="2010-07-26 12:12 UTC">2010-07-26 12:12 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">I have installed V3.2c of the blockset for MATLAB R2007a (As this version does not support R2006b which I was using previously).<br>
<br>
The following error(s) are reported when I load the example 'FlexBoard_Blinking_Led.mdl' :<br>
<br>
<br>
<br>
Warning: Error using ==&gt; getSTFInfo.p&gt;getSTFInfo at 47<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Undefined function or method 'exist' for input arguments of type 'cell'.<br>
<br>
&gt; In C:\MATLAB\R2007a\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
Warning: GMAKE_PLACE not defined, check tlc target<br>
<br>
&gt; In C:\DSPIC_Lib\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 359<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In C:\DSPIC_Lib\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6<br>
<br>
  In C:\DSPIC_Lib\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
  In uiopen at 196<br>
<br>
<br>
<br>
When I double click on the 'Master' block the following is displayed on an 'Error' message box:<br>
<br>
<br>
<br>
Error evaluating 'OpenFcn' callback of Master block (mask) 'Master'.<br>
<br>
Error using ==&gt; &lt;ahref="error:C:\DSPIC_Lib\blocks\dsPIC_ConfigRTWOption.p,359,1"&gt;dsPIC_ConfigRTWOption at 359&lt;/a&gt;<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
<br>
<br>
When I check the selected System Target file it is 'dspic.tlc'.<br>
<br>
<br>
<br>
Please advise.</div>
</article>

<article class="forum-post" id="p1291">
<header><strong>LubinKerhuel</strong><time datetime="2010-08-31 20:37 UTC">2010-08-31 20:37 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Dear Mike,<br>
<br>
<br>
<br>
Sorry for the 1 month delay.<br>
<br>
Did you still have the problem ?<br>
<br>
<br>
<br>
I have no obvious idea right now. <br>
<br>
Anyway, could you check that this problem with the latest version (please re-download the blockset that was just updating while you were writting your message (same date)...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1295">
<header><strong>mickpowell</strong><time datetime="2010-09-14 07:53 UTC">2010-09-14 07:53 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">The problem is still as I have described</div>
</article>

<article class="forum-post" id="p1372">
<header><strong>onuruygur</strong><time datetime="2010-12-01 18:24 UTC">2010-12-01 18:24 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : mickpowell</header>The problem is still as I have described</blockquote><br>
<br>
Sorry for complaining but I am totally suffering from the same problem with 2008b. I tried all the dspic related tlc target files but nothing solved. I was used to work on the previous versions which was succesful.<br>
<br>
<br>
<br>
This is the main error when I press play:<br>
<pre><code>The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.</code></pre><br>
<br>
Thnx</div>
</article>

<article class="forum-post" id="p1373">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-01 19:11 UTC">2010-12-01 19:11 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Okay,<br>
<br>
<br>
<br>
Let's see what's happening.<br>
<br>
Can you compile the examples in the demo directory ?<br>
<br>
did you tried to dbclick the yello block that configure and should solve automatically few problems ?<br>
<br>
<br>
<br>
If you started a model from scratch, please upload it on the forum so I can have a look.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1375">
<header><strong>onuruygur</strong><time datetime="2010-12-01 22:08 UTC">2010-12-01 22:08 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I really appreciate your code but for this version might have a problem. Lets see what we have.<br>
<br>
<br>
<br>
I have R2009a at office and try all the steps again and had the same problem again.. :(<br>
<br>
<br>
<br>
MPLAB C Compiler for dsPIC v3.25 Standard-Eval Version    11/15/2010 3:43:44 PM 47769 KB   installed first.<br>
<br>
Download dsPIC Toolbox for Matlab R2009a (Matlab 32 and 64 bits) is installed by install_dsPIC_R2009a<br>
<br>
<br>
<pre><code>  Installation of Real Time Embedded Coder for dsPIC is finished!
<wbr>
 - YOU MUST INSTALL C30 and/or C32 COMPILER AVAILABLE ON THE MICROCHIP WEBSITE.
The C30 version included in the MPLAB distribution (v8.10) will 
 produce a error like "gld file not found"
<wbr>
  - Checking that C30 PIC24 and/or dsPIC are installed on your system :
&gt;&gt;!pic30-lm
Microchip MPLAB C30 License Manager Version v3_25 (Build Date Oct 11 2010). 
Copyright (c) 2008 Microchip Technology Inc. All rights reserved. 
This demo-version license for MPLAB C for 16-bit devices, 
   has 60 days remaining after today. 
<wbr>
- checking that C32 PIC32 is also installed on your system :
&gt;&gt;!pic32-gcc -v
'pic32-gcc' 
<wbr>
 - go to  www.kerhuel.eu  to check installation procedure
 - Check installation : start the script CompileAllModels in the examples directory.
 (copy-past the following) 
cd examples
CompileAllModels
<wbr>
It will compile all the model present in 
the example directory (for dsPIC and PIC24 and PIC32 ;
 make sure you install compiler : for dsPIC and PIC24 and PIC32)</code></pre><br>
<br>
Now I can see the toolbox in the list. It is ok!<br>
<br>
<br>
<br>
Let's open the standard Flex example. &gt;&gt; FlexBoard_Blinking_Led.mdl double click &gt;&gt;<br>
<br>
<br>
<pre><code>Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Documents and Settings\Cat\Desktop\asdqwe\dspic\execBatch.p is a case-insensitive match and will be
used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2009a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 73
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The following error occurred processing the System Target File '':
<wbr>
Undefined function or method 'exist' for input arguments of type 'cell'.
<wbr>
&gt; In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 49: block_diagram does not have a parameter named
'CovForceBlockReductionOff'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: In instantiating linked block 'FlexBoard_Blinking_Led/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196</code></pre><br>
<br>
dbclick on yellow configure block, we observe the data on command screen... &gt;&gt; screen1 below<br>
<br>
<br>
<br>
target is selected as below on RTW: &gt;&gt; screen2 below<br>
<br>
<br>
<br>
when click to play in diagram: &gt;&gt;screen3 below<br>
<br>
<br>
<br>
Very interested to find out a solution. <br>
<br>
<br>
<br>
Thank you very much. <br>
<br>
<br>
<br>
Onur Tarakçıoğlu</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/361-screen1.JPG">Pièce jointe : screen1.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/362-screen2.JPG">Pièce jointe : screen2.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/363-screen3.JPG">Pièce jointe : screen3.JPG</a></p>
</article>

<article class="forum-post" id="p1376">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-02 00:25 UTC">2010-12-02 00:25 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Hi Onur,<br>
<br>
<br>
<br>
Thanks for your report. Please upload directly your image on the forum, it's much more easier to see and open them than through rapidShare.<br>
<br>
<br>
<br>
Anyway, at first, I could not reproduced the bug. However, I saw that you have the Microchp blockset installed. Thus I installed it on my system (v2.10) and I could not compild my example (FlexBoard_Blinking_Led.mdl) anymore. Thus, I re-installed my blockset and it worked properly again. I guess that booth blockest are calling same function name, and the latest blockset installed get the priority in the matlab Path.<br>
<br>
Unfortunately, the problem was not exactly the same as you get. Anyway, there is clearly an incompatibility between booth blockset (I will try to understand what's happening !)<br>
<br>
<br>
<br>
Could you tell me if all the model in the example directory does not compile from your side ? (just launch CompileAllModels.m script)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1379">
<header><strong>onuruygur</strong><time datetime="2010-12-02 17:34 UTC">2010-12-02 17:34 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
Thank you for your keen interest. Pictures are ok. I just started the CompileAllModels.m and the command window is as given below. All the other models give the same error about target file. <br>
<br>
<br>
<pre><code>Warning: File 'Data_Login_Matlab.hex' not found. 
&gt; In CompileAllModels at 10
Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Documents and Settings\Cat\Desktop\asdqwe\dspic\execBatch.p is a case-insensitive match and will be used
instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2009a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 73
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In CompileAllModels at 12
Warning: The following error occurred processing the System Target File '':
<wbr>
Undefined function or method 'exist' for input arguments of type 'cell'.
<wbr>
&gt; In stf2target at 61
  In CompileAllModels at 12
Warning: dsPICdrivers.mdl, line 49: block_diagram does not have a parameter named
'CovForceBlockReductionOff'. 
&gt; In CompileAllModels at 12
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In CompileAllModels at 12
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 52
  In CompileAllModels at 13
??? Error using ==&gt; dsPIC_ConfigureModelFordsPICTarget at 59
Error using ==&gt; dsPIC_ConfigRTWOption at 357
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop
<wbr>
Error in ==&gt; CompileAllModels at 13
    dsPIC_ConfigureModelFordsPICTarget();</code></pre><br>
<br>
<br>
<br>
I reinstall your library. But had the same error. I gonna uninstall the Microchip library somehow...</div>
</article>

<article class="forum-post" id="p1380">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-03 00:04 UTC">2010-12-03 00:04 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Hi Onur and mickpowell<br>
<br>
<br>
<br>
Thanks Onur for uploading your illustration on the forum.<br>
<br>
<br>
<br>
From your message, i appears that there may be a bug in the blockset for some computer configuration.<br>
<br>
As I can't reproduce it, I would ask for your help.<br>
<br>
<br>
<br>
Could you please upload the file testing.p, copy it in the example directory of the blockest.<br>
<br>
The experiment is fairly simple : could you first open one of the model (FlexBoard_Blinking_Led.mdl) and then, launch the script typing testing. (this is a script for matlab 2009a)<br>
<br>
<br>
<br>
Please launch the script at least twice and report all message that may appears.<br>
<br>
"testing.p" is a script very similar to dsPIC_ConfigRTWOption.p from the blockset. This versiou should give me some more insight into the error with from the error message...<br>
<br>
<br>
<br>
Thanks<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1381">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-03 00:10 UTC">2010-12-03 00:10 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Hi Onur and mickpowell<br>
<br>
<br>
<br>
Thanks Onur for uploading your illustration on the forum.<br>
<br>
<br>
<br>
From your message, i appears that there may be a bug in the blockset for some computer configuration.<br>
<br>
As I can't reproduce it, I would ask for your help.<br>
<br>
<br>
<br>
Could you please upload the file testing.p, copy it in the example directory of the blockest.<br>
<br>
The experiment is fairly simple : could you first open one of the model (FlexBoard_Blinking_Led.mdl) and then, launch the script typing &gt;&gt; <strong>testing </strong>at the matlab prompt. (this is a script for matlab 2009a)<br>
<br>
<br>
<br>
Please launch the script at least twice and report all message that will appears.<br>
<br>
"testing.p" is a script very similar to dsPIC_ConfigRTWOption.p from the blockset. This versiou should give me some more insight into the error with from the error message...<br>
<br>
<br>
<br>
Thanks<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/364-testing.p">Pièce jointe : testing.p</a></p>
</article>

<article class="forum-post" id="p1382">
<header><strong>onuruygur</strong><time datetime="2010-12-05 16:09 UTC">2010-12-05 16:09 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Sorry for late response. I ran the testing but a primative error arrises. <br>
<br>
<br>
<br>
Hope that this helps. <br>
<br>
<br>
<pre><code>Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Documents and Settings\Cat\Desktop\asdqwe\dspic\execBatch.p is a case-insensitive match and will be used
instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2009a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 73
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The following error occurred processing the System Target File '':
<wbr>
Undefined function or method 'exist' for input arguments of type 'cell'.
<wbr>
&gt; In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 49: block_diagram does not have a parameter named
'CovForceBlockReductionOff'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: In instantiating linked block 'FlexBoard_Blinking_Led/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_CalculusTimeStep_initMask.p&gt;dsPIC_CalculusTimeStep_initMask at 6
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
&gt;&gt; testing.p
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\examples\testing.p&gt;testing at 45
??? Error using ==&gt; testing at 81
block_diagram does not have a parameter named 'LDPICTYPE'.
<wbr>
&gt;&gt; testing.p
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\examples\testing.p&gt;testing at 45
??? Error using ==&gt; testing at 81
block_diagram does not have a parameter named 'LDPICTYPE'.</code></pre><br>
<br>
After that I have removed the Microchip lib and install your lib again. Still the problem goes on... :roll: <br>
<br>
<br>
<pre><code>---------------------------------------------------
    REMOVING Target for Microchip(TM) dsPIC 2.10  
---------------------------------------------------
  Target for Microchip(TM) dsPIC 2.10 is Installed and ready to use.
-------------------------
  INSTALLATION RTWdsPIC
-------------------------
  Reading the archiv 
  Checksum test passed (18B2AABAED767)
  RTWdsPIC version none 
  RTWdsPIC time stamp 22-Nov-2010 01:00:55
  Importing the archiv 100% |******************************|
  Toolbox folder is C:\Documents and Settings\Cat\Desktop\asdqwe
addpath 'C:\Documents and Settings\Cat\Desktop\asdqwe' 
  Creating Readme.html
  Creating blocks\EmptySFunction.mexw32
  Creating blocks\EmptySFunction.mexw64
  Creating blocks\EmptySFunction.tlc
  Creating blocks\GetDsPICParam.p
  Creating blocks\RS232_analyzBloc.p
  Creating blocks\Set_DialogBoxMask.p
  Creating blocks\combinatoire.p
  Creating blocks\dsPIC_ADC.mexw32
  Creating blocks\dsPIC_ADC.mexw64
  Creating blocks\dsPIC_ADC.tlc
  Creating blocks\dsPIC_ADC_callback.p
  Creating blocks\dsPIC_ADC_callback_InitMask.p
  Creating blocks\dsPIC_ADC_param2mex.p
  Creating blocks\dsPIC_CAN_Config.mexw32
  Creating blocks\dsPIC_CAN_Config.mexw64
  Creating blocks\dsPIC_CAN_Config.tlc
  Creating blocks\dsPIC_CAN_Config_callback.p
  Creating blocks\dsPIC_CAN_Receive.mexw32
  Creating blocks\dsPIC_CAN_Receive.mexw64
  Creating blocks\dsPIC_CAN_Receive.tlc
  Creating blocks\dsPIC_CAN_Receive_callback.p
  Creating blocks\dsPIC_CAN_Transmit.mexw32
  Creating blocks\dsPIC_CAN_Transmit.mexw64
  Creating blocks\dsPIC_CAN_Transmit.tlc
  Creating blocks\dsPIC_CAN_Transmit_callback.p
  Creating blocks\dsPIC_C_function_Call.mexw32
  Creating blocks\dsPIC_C_function_Call.mexw64
  Creating blocks\dsPIC_C_function_Call.tlc
  Creating blocks\dsPIC_C_function_Call_callback.p
  Creating blocks\dsPIC_CalculusTimeStep.mexw32
  Creating blocks\dsPIC_CalculusTimeStep.mexw64
  Creating blocks\dsPIC_CalculusTimeStep.tlc
  Creating blocks\dsPIC_CalculusTimeStep_initMask.p
  Creating blocks\dsPIC_CheckParamSimulation.p
  Creating blocks\dsPIC_Chronograph.mexw32
  Creating blocks\dsPIC_Chronograph.mexw64
  Creating blocks\dsPIC_Chronograph.tlc
  Creating blocks\dsPIC_Chronograph_Callback.p
  Creating blocks\dsPIC_Compile.p
  Creating blocks\dsPIC_ConfigClock32f.p
  Creating blocks\dsPIC_ConfigClock33f.p
  Creating blocks\dsPIC_ConfigRTWOption.p
  Creating blocks\dsPIC_ConfigureModelFordsPICTarget.p
  Creating blocks\dsPIC_Digital_Input.mexw32
  Creating blocks\dsPIC_Digital_Input.mexw64
  Creating blocks\dsPIC_Digital_Input.tlc
  Creating blocks\dsPIC_Digital_Input_callback.p
  Creating blocks\dsPIC_Digital_OutputRead.mexw32
  Creating blocks\dsPIC_Digital_OutputRead.mexw64
  Creating blocks\dsPIC_Digital_OutputRead.tlc
  Creating blocks\dsPIC_Digital_OutputRead_callback.p
  Creating blocks\dsPIC_Digital_OutputWrite.mexw32
  Creating blocks\dsPIC_Digital_OutputWrite.mexw64
  Creating blocks\dsPIC_Digital_OutputWrite.tlc
  Creating blocks\dsPIC_Digital_OutputWrite_callback.p
  Creating blocks\dsPIC_ECAN_Config.mexw32
  Creating blocks\dsPIC_ECAN_Config.mexw64
  Creating blocks\dsPIC_ECAN_Config.tlc
  Creating blocks\dsPIC_EXT_INT_PWM_callback_InitMask.p
  Creating blocks\dsPIC_EXT_INT_PWM_param2mex.p
  Creating blocks\dsPIC_Ext_Interrupt_PWM.mexw32
  Creating blocks\dsPIC_Ext_Interrupt_PWM.mexw64
  Creating blocks\dsPIC_Ext_Interrupt_PWM.tlc
  Creating blocks\dsPIC_Get_Dialog_PopUp_Param.p
  Creating blocks\dsPIC_Get_Dialog_PromptString.p
  Creating blocks\dsPIC_I2C_Master.mexw32
  Creating blocks\dsPIC_I2C_Master.mexw64
  Creating blocks\dsPIC_I2C_Master.tlc
  Creating blocks\dsPIC_I2C_Master_callback.p
  Creating blocks\dsPIC_MASTER.mexw32
  Creating blocks\dsPIC_MASTER.mexw64
  Creating blocks\dsPIC_MASTER.tlc
  Creating blocks\dsPIC_MASTER_callback.p
  Creating blocks\dsPIC_MASTER_callback_InitMask.p
  Creating blocks\dsPIC_Nop.mexw32
  Creating blocks\dsPIC_Nop.mexw64
  Creating blocks\dsPIC_Nop.tlc
  Creating blocks\dsPIC_PIN_Mapping.mexw32
  Creating blocks\dsPIC_PIN_Mapping.mexw64
  Creating blocks\dsPIC_PIN_Mapping.tlc
  Creating blocks\dsPIC_PIN_Mapping_Callback.p
  Creating blocks\dsPIC_PWM_CN.mexw32
  Creating blocks\dsPIC_PWM_CN.mexw64
  Creating blocks\dsPIC_PWM_CN.tlc
  Creating blocks\dsPIC_PWM_CN_CheckDiag.p
  Creating blocks\dsPIC_PWM_CN_callback.p
  Creating blocks\dsPIC_PWM_IC.mexw32
  Creating blocks\dsPIC_PWM_IC.mexw64
  Creating blocks\dsPIC_PWM_IC.tlc
  Creating blocks\dsPIC_PWM_IC_CheckDiag.p
  Creating blocks\dsPIC_PWM_IC_callback.p
  Creating blocks\dsPIC_PWM_Motor_callback.p
  Creating blocks\dsPIC_PWM_OC.mexw32
  Creating blocks\dsPIC_PWM_OC.mexw64
  Creating blocks\dsPIC_PWM_OC.tlc
  Creating blocks\dsPIC_PWM_OC_CheckDiag.p
  Creating blocks\dsPIC_PWM_OC_HW.mexw32
  Creating blocks\dsPIC_PWM_OC_HW.mexw64
  Creating blocks\dsPIC_PWM_OC_HW.tlc
  Creating blocks\dsPIC_PWM_OC_HW_CheckDiag.p
  Creating blocks\dsPIC_PWM_OC_HW_callback.p
  Creating blocks\dsPIC_PWM_OC_HW_callback_InitMask.p
  Creating blocks\dsPIC_PWM_OC_callback.p
  Creating blocks\dsPIC_PWM_OC_callback_InitMask.p
  Creating blocks\dsPIC_PWM_motor.mexw32
  Creating blocks\dsPIC_PWM_motor.mexw64
  Creating blocks\dsPIC_PWM_motor.tlc
  Creating blocks\dsPIC_PWM_motor_callback_InitMask.p
  Creating blocks\dsPIC_PortSetting.p
  Creating blocks\dsPIC_Reset.mexw32
  Creating blocks\dsPIC_Reset.mexw64
  Creating blocks\dsPIC_Reset.tlc
  Creating blocks\dsPIC_SPI_IO.mexw32
  Creating blocks\dsPIC_SPI_IO.mexw64
  Creating blocks\dsPIC_SPI_IO.tlc
  Creating blocks\dsPIC_SPI_IO_Interrupt.mexw32
  Creating blocks\dsPIC_SPI_IO_Interrupt.mexw64
  Creating blocks\dsPIC_SPI_IO_Interrupt.tlc
  Creating blocks\dsPIC_SPI_IO_Interrupt_Callback.p
  Creating blocks\dsPIC_SPI_IO_callback.p
  Creating blocks\dsPIC_SPI_IO_param2mex.p
  Creating blocks\dsPIC_SPI_config.mexw32
  Creating blocks\dsPIC_SPI_config.mexw64
  Creating blocks\dsPIC_SPI_config.tlc
  Creating blocks\dsPIC_SPI_config_callback.p
  Creating blocks\dsPIC_SPI_config_param2mex.p
  Creating blocks\dsPIC_SerialReadSimulink.p
  Creating blocks\dsPIC_Set_Dialog_PopUp_Param.p
  Creating blocks\dsPIC_Set_Dialog_PromptString.p
  Creating blocks\dsPIC_TimerSetting.p
  Creating blocks\dsPIC_UART_RX.mexw32
  Creating blocks\dsPIC_UART_RX.mexw64
  Creating blocks\dsPIC_UART_RX.tlc
  Creating blocks\dsPIC_UART_RX_callback.p
  Creating blocks\dsPIC_UART_RX_param2mex.p
  Creating blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p
  Creating blocks\dsPIC_UART_TX.mexw32
  Creating blocks\dsPIC_UART_TX.mexw64
  Creating blocks\dsPIC_UART_TX.tlc
  Creating blocks\dsPIC_UART_TX_Labview_Matlab.mexw32
  Creating blocks\dsPIC_UART_TX_Labview_Matlab.mexw64
  Creating blocks\dsPIC_UART_TX_Labview_Matlab.tlc
  Creating blocks\dsPIC_UART_TX_Labview_Matlab_callback.p
  Creating blocks\dsPIC_UART_TX_callback.p
  Creating blocks\dsPIC_UART_callback_InitMask.p
  Creating blocks\dsPIC_UART_config.mexw32
  Creating blocks\dsPIC_UART_config.mexw64
  Creating blocks\dsPIC_UART_config.tlc
  Creating blocks\dsPIC_UART_config_callback.p
  Creating blocks\dsPIC_code_template.cgt
  Creating blocks\dsPIC_main.tlc
  Creating blocks\dsPIC_mrmain.tlc
  Creating blocks\dsPIC_srmain.tlc
  Creating blocks\dsPICdrivers.mdl
  Creating blocks\dspicListe.mat
  Creating blocks\fOrderingInOut.p
  Creating blocks\fPin.p
  Creating blocks\fPortRef.p
  Creating blocks\pad.p
  Creating blocks\padr.p
  Creating blocks\rs232gui.fig
  Creating blocks\rs232gui.p
  Creating blocks\slblocks.m
  Creating dspic\Contents.m
  Creating dspic\Contents.p
  Creating dspic\Contents.txt
  Creating dspic\dsPIC_CreateMPLAB.p
  Creating dspic\dspic.tlc
  Creating dspic\dspic_pic30_gcc.tmf
  Creating dspic\dspic_select_callback_handler.p
  Creating dspic\execBatch.p
  Creating dspic\getPath.bat
  Creating dspic\getProgramFilesPath.bat
  Creating dspic\getProgramFilesx86Path.bat
  Creating dspic\info.xml
  Creating dspic\make_CreateMPLAB.p
  Creating dspic\pic32.tlc
  Creating dspic\pic32_gcc.tmf
  Creating dspic\pic32_select_callback_handler.p
  Creating dspic\setup_for_lcc.p
  Creating dspic\sl_customization.p
  Creating examples\CompileAllModels.m
  Creating examples\Data_Login_Matlab.mdl
  Creating examples\FlexBoard_Blinking_Led.mdl
  Creating examples\Servo_ADC.mdl
  Creating examples\Servo_Sinus.mdl
  Creating examples\dsPIC_32MX460F512L_Explorer16_HyperSampling.mdl
  Creating examples\dsPIC_33f_Explorer16.mdl
  Update path...
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.3a(22-Nov-2010) for Matlab R2009a.
<wbr>
<wbr>
Licence Accorded to  Demonstration Version
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://www.kerhuel.eu/wiki
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
 Facturation to :    Demo
                     Demo
                     Lubin KERHUEL
                     1, rue Alfred Fredet
                     38100 Grenoble
                     FRANCE
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
<wbr>
  Installation of Real Time Embedded Coder for dsPIC is finished!
<wbr>
<wbr>
<wbr>
 - YOU MUST INSTALL C30 and/or C32 COMPILER AVAILABLE ON THE MICROCHIP WEBSITE.
The C30 version included in the MPLAB distribution (v8.10) will 
 produce a error like "gld file not found"
<wbr>
<wbr>
  - Checking that C30 PIC24 and/or dsPIC are installed on your system :
&gt;&gt;!pic30-lm
Microchip MPLAB C30 License Manager Version v3_25 (Build Date Oct 11 2010). 
Copyright (c) 2008 Microchip Technology Inc. All rights reserved. 
This demo-version license for MPLAB C for 16-bit devices, 
   has 56 days remaining after today. 
<wbr>
<wbr>
  - checking that C32 PIC32 is also installed on your system :
&gt;&gt;!pic32-gcc -v
'pic32-gcc' i‡ ya da dŸ komut, ‡alŸtrlabilir 
program ya da toplu iŸ dosyas olarak tannmyor. 
<wbr>
<wbr>
 - go to  www.kerhuel.eu  to check installation procedure
<wbr>
 - Check installation : start the script CompileAllModels in the examples directory.
 (copy-past the following) 
cd examples
CompileAllModels
<wbr>
It will compile all the model present in 
the example directory (for dsPIC and PIC24 and PIC32 ;
 make sure you install compiler : for dsPIC and PIC24 and PIC32)
-------------------------
Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Documents and Settings\Cat\Desktop\asdqwe\dspic\execBatch.p is a case-insensitive match and will be
used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2009a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 73
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The following error occurred processing the System Target File '':
<wbr>
Undefined function or method 'exist' for input arguments of type 'cell'.
<wbr>
&gt; In stf2target at 61
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 49: block_diagram does not have a parameter named
'CovForceBlockReductionOff'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: In instantiating linked block 'Servo_ADC/ADC Input' : Invalid setting in dsPIC : ADC10 block
(mask) 'ADC Input' for parameter 'OutFormatBitspopup'. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File must
be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop. 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Documents and Settings\Cat\Desktop\asdqwe\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 52
&gt;&gt; </code></pre><br>
<br>
thx<br>
<br>
<br>
<br>
onur</div>
</article>

<article class="forum-post" id="p1384">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-05 22:06 UTC">2010-12-05 22:06 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Hi Onur, Hi mickpowell,<br>
<br>
<br>
<br>
Thanks for all your remarks that makes me go forward.<br>
<br>
I think I find out the problem. Please give a try to the latest blockset version (3.3b) and let me know if problem is solved.<br>
<br>
<br>
<br>
Thanks<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1385">
<header><strong>onuruygur</strong><time datetime="2010-12-08 21:40 UTC">2010-12-08 21:40 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I want to congr. you since everything is ok with v3.3b!   :)  <br>
<br>
<br>
<br>
See the code below:<br>
<br>
<br>
<pre><code>Warning: In instantiating linked block 'FlexBoard_Blinking_Led/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'. 
new GMAKE path : C:\PROGRA~1\MATLAB\R2009a\bin\win32\gmake
Linker is now called through pic30-gcc as it did not worked anymore using pic30-ar. Linker options have been updated consequently !
Linker is now called through pic30-gcc as it did not worked anymore using pic30-ar. Linker options have been updated consequently !
file not found : C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld
      --&gt; corrected : find in --script=C:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC33F\gld\p33fJ256MC710.gld
file not found : C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a
file not found : C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC33F\libp33fJ256MC710-coff.a
file not found : C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a
file not found : C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a
PNumber of I/O PINs used : 3
TModel configured...
PPTPNumber of I/O PINs used : 3
TPNumber of I/O PINs used : 3
TTPTPTTPTPTPTTPTPTWarning: Source 'FlexBoard_Blinking_Led/Calculus Time Step' specifies that its sample time (-1) is
back-inherited. You should explicitly specify the sample time of sources. You can disable this diagnostic by
setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the
Diagnostics pane of the Configuration Parameters dialog box. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.01. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.01. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.01. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.02. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.02. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.02. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.03. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.03. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.03. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.04. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.04. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.04. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.05. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.05. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.05. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.06. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.06. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.06. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.07000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.07000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.07000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.08. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.08. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.08. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.09. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.09. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.09. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.1. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.1. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.1. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.11. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.11. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.11. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.12. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.12. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.12. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.13. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.13. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.13. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.14. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.14. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.14. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.15. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.15. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.15. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.16. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.16. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.16. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.17. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.17. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.17. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.18. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.18. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.18. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.19. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.19. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.19. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.2. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.2. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.2. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.21. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.21. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.21. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.22. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.22. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.22. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.23. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.23. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.23. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.24. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.24. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.24. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.25. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.25. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.25. 
Warning: Overflow occurred. This originated from 'FlexBoard_Blinking_Led/0.5Hz/Increment Real World/FixPt
Sum1'. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.26. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.26. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.26. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.27. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.27. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.27. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.28. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.28. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.28. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.29. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.29. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.29. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.3. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.3. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.3. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.31. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.31. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.31. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.32. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.32. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.32. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.33. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.33. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.33. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.34. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.34. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.34. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.35. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.35. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.35. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.36. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.36. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.36. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.37. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.37. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.37. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.38. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.38. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.38. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.39. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.39. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.39. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.4. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.4. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.4. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.41. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.41. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.41. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.42. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.42. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.42. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.43. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.43. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.43. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.44. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.44. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.44. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.45. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.45. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.45. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.46. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.46. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.46. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.47. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.47. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.47. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.48. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.48. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.48. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.49. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.49. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.49. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.5. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.5. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.5. 
Warning: Overflow occurred. This originated from 'FlexBoard_Blinking_Led/Switch'. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.51. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.51. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.51. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.52. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.52. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.52. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.53. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.53. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.53. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.54. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.54. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.54. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.55. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.55. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.55. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.5600000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.5600000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.5600000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.5700000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.5700000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.5700000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.58. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.58. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.58. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.59. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.59. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.59. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.6. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.6. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.6. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.61. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.61. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.61. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.62. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.62. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.62. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.63. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.63. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.63. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.64. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.64. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.64. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.65. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.65. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.65. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.66. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.66. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.66. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.67. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.67. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.67. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.6800000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.6800000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.6800000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.6900000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.6900000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.6900000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.7000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.7000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.7000000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.71. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.71. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.71. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.72. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.72. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.72. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.73. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.73. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.73. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.74. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.74. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.74. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.75. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.75. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.75. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.76. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.76. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.76. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.77. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.77. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.77. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.78. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.78. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.78. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.79. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.79. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.79. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.8. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.8. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.8. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.8100000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.8100000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.8100000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.8200000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.8200000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.8200000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.8300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.8300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.8300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.84. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.84. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.84. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.85. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.85. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.85. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.86. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.86. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.86. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.87. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.87. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.87. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.88. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.88. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.88. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.89. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.89. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.89. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.9. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.9. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.9. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.91. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.91. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.91. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.92. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.92. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.92. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.9300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.9300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.9300000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.9400000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.9400000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.9400000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time
0.9500000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time
0.9500000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time
0.9500000000000001. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.96. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.96. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.96. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.97. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.97. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.97. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.98. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.98. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.98. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 0.99. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 0.99. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 0.99. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read4' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory3' before any blocks have written to this memory at time 1. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read1' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory2' before any blocks have written to this memory at time 1. 
Warning: The block 'FlexBoard_Blinking_Led/Data Store Read2' is reading from the data store
'FlexBoard_Blinking_Led/Data Store Memory1' before any blocks have written to this memory at time 1. 
&gt;&gt; </code></pre><br>
<br>
<br>
<br>
Thank you very much!!! :wink:</div>
</article>

<article class="forum-post" id="p1386">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-08 22:08 UTC">2010-12-08 22:08 UTC</time></header>
<h3>Re: Error loading example</h3>
<div class="forum-post-body">Thx Onur for precious help and for your feedback !<br>
<br>
Lubin</div>
</article>

