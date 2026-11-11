---
title: "Not able to install dspic toolbox... Errors"
url: "/forum/topic/293/"
archiveKind: "topic"
---
# Not able to install dspic toolbox... Errors

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p1143">
<header><strong>Sabooh</strong><time datetime="2010-03-31 07:38 UTC">2010-03-31 07:38 UTC</time></header>
<div class="forum-post-body">Hello<br>
<br>
<br>
<br>
I am using <br>
<br>
Matlab 2009a<br>
<br>
MPLAB IDE 8.46<br>
<br>
MPLAB C30 ComboLite_v3_23 (dspic and pic24)<br>
<br>
<br>
<br>
but when i m running <br>
<br>
CompileAllModels.m<br>
<br>
I am getting following error..<br>
<br>
<br>
<pre><code>7x1 struct array with fields:
    name
    date
    bytes
    isdir
    datenum
<wbr>
Warning: File 'Data_Login_Matlab.hex'
not found. 
&gt; In CompileAllModels at 8
  In run at 57
Warning: The following error occurred
processing the System Target File '':
<wbr>
Undefined function or method 'ExecBatch'
for input arguments of type 'char'.
<wbr>
&gt; In stf2target at 61
  In CompileAllModels at 10
  In run at 57
Evaluating callback 'LoadFcn' for Data_Login_Matlab/Master
Callback: clear InternaldsPICBlockset;        
dsPIC_MASTER_callback() ;           
dsPIC_MASTER_callback_InitMask(gcb);
Warning: block_diagram does not have a
parameter named 'GMAKE_PLACE'. 
&gt; In C:\Documents and Settings\Sabooh\My Documents\MATLAB\install_dsPIC_R2009a\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36
  In CompileAllModels at 10
  In run at 57
Warning: Error evaluating 'LoadFcn'
callback of Master block (mask)
'Master'. block_diagram does not have a
parameter named 'GMAKE_PLACE'. 
&gt; In C:\Documents and Settings\Sabooh\My Documents\MATLAB\install_dsPIC_R2009a\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36
  In CompileAllModels at 10
  In run at 57
Warning: The following error occurred
processing the System Target File '':
<wbr>
Undefined function or method 'ExecBatch'
for input arguments of type 'char'.
<wbr>
&gt; In stf2target at 61
  In C:\Documents and Settings\Sabooh\My Documents\MATLAB\install_dsPIC_R2009a\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 42
  In CompileAllModels at 11
  In run at 57
Warning: The following error occurred
processing the System Target File '':
<wbr>
Undefined function or method 'ExecBatch'
for input arguments of type 'char'.
<wbr>
&gt; In C:\Documents and Settings\Sabooh\My Documents\MATLAB\install_dsPIC_R2009a\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 42
  In CompileAllModels at 11
  In run at 57
??? Error using ==&gt;
dsPIC_ConfigureModelFordsPICTarget at 51
Error using ==&gt; dsPIC_ConfigRTWOption at
11
block_diagram does not have a parameter
named 'GMAKE_PLACE'.
<wbr>
Error in ==&gt; CompileAllModels at 11
    dsPIC_ConfigureModelFordsPICTarget();
<wbr>
Error in ==&gt; run at 57
          evalin('caller', [s ';']);
<wbr>
Evaluating callback 'ModelCloseFcn' for Data_Login_Matlab/Master
Callback: clear InternaldsPICBlockset;
&gt;&gt;
</code></pre><br>
<br>
<br>
<br>
Please any body Help me??????????????????????????????</div>
</article>

<article class="forum-post" id="p1144">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-31 11:14 UTC">2010-03-31 11:14 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">Thanks you very much for your post !<br>
<br>
<br>
<br>
This error comes from correction I made in the last blockset version published two days ago.<br>
<br>
it appears from your post that some files are missing in the installer package.<br>
<br>
<br>
<br>
I'll correct it shortly.<br>
<br>
<br>
<br>
I'll post a message once it's done !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1187">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-27 07:47 UTC">2010-04-27 07:47 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I did not post the message, But problem has been solved, please give a try with the latest version (3.2b)  : <a href="/wiki/release-notes/">http://archive.kerhuel.eu/wiki/Release_Notes</a></div>
</article>

<article class="forum-post" id="p1258">
<header><strong>alby.divy</strong><time datetime="2010-06-29 09:46 UTC">2010-06-29 09:46 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">Hi Lubin!I have the same error also with version 3.2b. I'm desperate!<br>
<br>
I'm working with Matlab 2010a. Can this cause problems?<br>
<br>
Help me!<br>
<br>
Thanks<br>
<br>
<br>
<br>
Alb</div>
</article>

<article class="forum-post" id="p1260">
<header><strong>LubinKerhuel</strong><time datetime="2010-06-29 11:11 UTC">2010-06-29 11:11 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
Could you post the entire error message you get (the one within matlab comand windows) ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1261">
<header><strong>alby.divy</strong><time datetime="2010-06-29 17:26 UTC">2010-06-29 17:26 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">Of course! When I compile the examples:<br>
<br>
<br>
<br>
<span style="color:#ff0000">### Successful completion of Real-Time Workshop build procedure for model: Servo_Sinus_x64<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
Warning: File 'dsPIC_32MX460F512L_Explorer16_HyperSampling.hex' not found. <br>
<br>
&gt; In CompileAllModels at 10<br>
<br>
Warning: The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Undefined function or variable "myData".<br>
<br>
 <br>
<br>
&gt; In stf2target at 61<br>
<br>
  In CompileAllModels at 12<br>
<br>
Warning: In instantiating linked block<br>
<br>
'dsPIC_32MX460F512L_Explorer16_HyperSampling/Master' : Invalid setting in Master block<br>
<br>
(mask) 'Master' for parameter 'MCLR' <br>
<br>
&gt; In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9<br>
<br>
  In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In CompileAllModels at 12<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'.<br>
<br>
block_diagram does not have a parameter named 'GMAKE_PLACE'. <br>
<br>
&gt; In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9<br>
<br>
  In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In CompileAllModels at 12<br>
<br>
Warning: block_diagram does not have a parameter named 'GMAKE_PLACE'. <br>
<br>
&gt; In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9<br>
<br>
  In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In CompileAllModels at 12<br>
<br>
Warning: The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Undefined function or variable "myData".<br>
<br>
 <br>
<br>
&gt; In stf2target at 61<br>
<br>
  In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 40<br>
<br>
  In CompileAllModels at 13<br>
<br>
Warning: The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Undefined function or variable "myData".<br>
<br>
 <br>
<br>
&gt; In C:\Users\Alberto Di Vittorio\Documents\MATLAB\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 40<br>
<br>
  In CompileAllModels at 13<br>
<br>
??? Error using ==&gt; dsPIC_ConfigureModelFordsPICTarget at 51<br>
<br>
Error using ==&gt; dsPIC_ConfigRTWOption at 11<br>
<br>
block_diagram does not have a parameter named 'GMAKE_PLACE'.<br>
<br>
<br>
<br>
Error in ==&gt; CompileAllModels at 13<br>
<br>
    dsPIC_ConfigureModelFordsPICTarget();</span><br>
<br>
<br>
<br>
<span style="color:#000000">and when I compile my program "prova2":</span><br>
<br>
<span style="color:#ff0000">-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating prova2.mk from C:\Users\Alberto Di Vittorio\Documents\MATLAB\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building prova2: "C:\PROGRA~1\MATLAB\R2010a\bin\win32\gmake" -f prova2.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0<br>
<br>
Impossibile trovare il percorso specificato. <br>
<br>
### Real-Time Workshop build procedure for model: 'prova2' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found</span></div>
</article>

<article class="forum-post" id="p1262">
<header><strong>alby.divy</strong><time datetime="2010-06-29 17:28 UTC">2010-06-29 17:28 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">I have also ried with Matlab R2009a and with 2 types of compiler, (also the 3.23 (latest) version of 3.30), but the error is always the same!<br>
<br>
Can you help me, Lubin?<br>
<br>
Thanks<br>
<br>
<br>
<br>
Alb</div>
</article>

<article class="forum-post" id="p1265">
<header><strong>Inkspot</strong><time datetime="2010-06-30 07:57 UTC">2010-06-30 07:57 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">I've just spent 3 hours trying to install the dspic toolbox on a machine with R2010a.  I had matlab installed on drive D:, and installed the Microchip tools on D: also.  This won't work for some reason, lots of errors that look like those posted above occur when trying to compile the examples.<br>
<br>
<br>
<br>
Placing the Microchip on the C: drive seems to have cured the errors (at least the examples compile correctly).   I just thought I'd post in case it helps somebody. <br>
<br>
<br>
<br>
Now - I have C32 1.05 and C30 3.23b tools installed - is there any known issues with 3.23b or should I use the last version mentioned in the dsPIC wiki (version 3.12)?</div>
</article>

<article class="forum-post" id="p1266">
<header><strong>Inkspot</strong><time datetime="2010-06-30 08:25 UTC">2010-06-30 08:25 UTC</time></header>
<h3>Re: Not able to install dspic toolbox... Errors</h3>
<div class="forum-post-body">One question, which may be silly (it's a long time since I've used Matlab and it's changed quite a bit).<br>
<br>
<br>
<br>
When I run these examples, there are strings of 'P' and 'T' characters intermingled with the Matlab output in the console window.  Is this to be expected (and if so - why?).</div>
</article>

