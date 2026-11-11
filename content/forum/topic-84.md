---
title: "How to change directory?"
url: "/forum/topic/84/"
archiveKind: "topic"
---
# How to change directory?

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

21 message(s) · archive en lecture seule

<article class="forum-post" id="p194">
<header><strong>micman2</strong><time datetime="2008-02-13 08:30 UTC">2008-02-13 08:30 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
I'm new user, How to change directory C:\Program File\Microchip\MPLAB C30   in  C:\Programmi\Microchip\MPLAB C30 ?<br>
<br>
Thanks<br>
<br>
Michele</div>
</article>

<article class="forum-post" id="p195">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-13 12:13 UTC">2008-02-13 12:13 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Hi Michele,<br>
<br>
<br>
<br>
a similar problem with its solution are described here : <a href="/forum/topic/73/">viewtopic.php?f=5&amp;t=73#p152</a><br>
<br>
<br>
<br>
Adapt and try the solution proposed. <br>
<br>
adaptation would be ==&gt; rtw_alt_pathname('C:\Programmi\Microchip\MPLAB C30') <br>
<br>
<br>
<br>
If you still have the problem, please let us know.</div>
</article>

<article class="forum-post" id="p196">
<header><strong>micman2</strong><time datetime="2008-02-13 12:35 UTC">2008-02-13 12:35 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Hi,<br>
<br>
Thanks you for reply.<br>
<br>
<br>
<br>
Send the screen</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/8-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p197">
<header><strong>micman2</strong><time datetime="2008-02-13 12:39 UTC">2008-02-13 12:39 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">after I change "rtw_alt_pathname"</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/9-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p198">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-13 15:58 UTC">2008-02-13 15:58 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">from <a href="/forum/topic/73/">viewtopic.php?f=5&amp;t=73#p152</a> :<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : LubinKerhuel</header>You can check by typing at the matlab prompt the command:<br>
<br>
rtw_alt_pathname('C:\Program Files\Microchip\MPLAB C30')<br>
<br>
<br>
<br>
If you do not get C:\PROGRA~1\MICROC~1\MPLABC~1, you will have to change the short path in Simulink :<br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; DsPIC options</blockquote><br>
<br>
did you correct the parameters in the simulink model : <br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; DsPIC options<br>
<br>
(part 2 of the solution)</div>
</article>

<article class="forum-post" id="p199">
<header><strong>micman2</strong><time datetime="2008-02-13 16:10 UTC">2008-02-13 16:10 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">I see this</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/10-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p200">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-13 17:11 UTC">2008-02-13 17:11 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Something is wrong.<br>
<br>
<br>
<br>
In the Real Time Workshop , you have <br>
<br>
- Comment<br>
<br>
- Symbols<br>
<br>
- Custom Code<br>
<br>
- Debug<br>
<br>
<br>
<br>
You should have <br>
<br>
- Comment<br>
<br>
- Symbols<br>
<br>
- Custom Code<br>
<br>
- Debug<br>
<br>
- DsPIC options<br>
<br>
<br>
<br>
Could you try to select another target than dsPIC.tlc (ert.tlc or any other), click apply, then, choose again dsPIC.tlc, click apply and look at the command windows for any error? Could you report the error you get here?<br>
<br>
Which matlab version are you using?<br>
<br>
<br>
<br>
I will try to find out what's happening as soon as I can...</div>
</article>

<article class="forum-post" id="p201">
<header><strong>micman2</strong><time datetime="2008-02-13 17:33 UTC">2008-02-13 17:33 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Hi,<br>
<br>
The file dspic.tlc is correct but when load there isn't "DsPIC options"</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/11-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p202">
<header><strong>micman2</strong><time datetime="2008-02-13 17:35 UTC">2008-02-13 17:35 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">and I've simulink version :</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/12-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p203">
<header><strong>micman2</strong><time datetime="2008-02-13 17:37 UTC">2008-02-13 17:37 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Matlab version:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/14-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p204">
<header><strong>micman2</strong><time datetime="2008-02-13 17:43 UTC">2008-02-13 17:43 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Error:<br>
<br>
<br>
<br>
Warning: Error using ==&gt; getSTFInfo at 76<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Error using ==&gt; getPathName<br>
<br>
The path 'C:\Program Files\Microchip\MPLAB C30' does not exist<br>
<br>
.<br>
<br>
&gt; In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 148<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption<br>
<br>
at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt;<br>
<br>
Real Time workshop.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 148<br>
<br>
  In uiopen at 196<br>
<br>
Warning: In instantiating linked block 'Servo_ADC/ADC Input' : Invalid setting in dsPIC : ADC10 block (mask) 'ADC<br>
<br>
Input' for parameter 'OutFormatBitspopup'.<br>
<br>
&gt; In C:\MyToolBox\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 148<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption<br>
<br>
at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt;<br>
<br>
Real Time workshop.<br>
<br>
&gt; In C:\MyToolBox\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9<br>
<br>
  In C:\MyToolBox\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 148<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error using ==&gt; getSTFInfo at 76<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Error using ==&gt; getPathName<br>
<br>
The path 'C:\Program Files\Microchip\MPLAB C30' does not exist<br>
<br>
.<br>
<br>
&gt; In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61<br>
<br>
  In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\@RTW\@TargetBrowser\uploadTarget.p&gt;uploadTarget at 20<br>
<br>
  In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\private\targetBrowserCloseCB.p&gt;targetBrowserCloseCB at 9<br>
<br>
  In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\rtwprivate.p&gt;rtwprivate at 12<br>
<br>
Warning: Error using ==&gt; getSTFInfo at 76<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Error using ==&gt; getPathName<br>
<br>
The path 'C:\Program Files\Microchip\MPLAB C30' does not exist<br>
<br>
.<br>
<br>
&gt; In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\@RTW\@TargetBrowser\uploadTarget.p&gt;uploadTarget at 20<br>
<br>
  In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\private\targetBrowserCloseCB.p&gt;targetBrowserCloseCB at 9<br>
<br>
  In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\rtwprivate.p&gt;rtwprivate at 12<br>
<br>
Warning: Error using ==&gt; getSTFInfo at 76<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Error using ==&gt; getPathName<br>
<br>
The path 'C:\Program Files\Microchip\MPLAB C30' does not exist<br>
<br>
.<br>
<br>
&gt; In C:\Programmi\MATLAB\R2007b\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61<br>
<br>
  In simulink\private\configDlgAction at 93<br>
<br>
  In slprivate at 12<br>
<br>
Warning: Error using ==&gt; getSTFInfo at 76<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
<br>
<br>
Error using ==&gt; getPathName<br>
<br>
The path 'C:\Program Files\Microchip\MPLAB C30' does not exist<br>
<br>
.<br>
<br>
&gt; In simulink\private\configDlgAction at 93<br>
<br>
  In slprivate at 12<br>
<br>
&gt;&gt;</div>
</article>

<article class="forum-post" id="p205">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-13 18:23 UTC">2008-02-13 18:23 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">This is a bug !<br>
<br>
<br>
<br>
I'll correct that. Thanks for screenshoot and bug description...</div>
</article>

<article class="forum-post" id="p206">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-13 19:50 UTC">2008-02-13 19:50 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">It's corrected, C30 can now be installed in the directory : C:\Programmi\Microchip\MPLAB C30 or in the directory : C:\Program Files\Microchip\MPLAB C30<br>
<br>
Could you give a try to the new version ? (download it on from website)</div>
</article>

<article class="forum-post" id="p208">
<header><strong>micman2</strong><time datetime="2008-02-14 08:06 UTC">2008-02-14 08:06 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">wow  :D  now work!!! Thank you<br>
<br>
<br>
<br>
<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt;<br>
<br>
dsPIC_ConfigRTWOption at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt;<br>
<br>
Real Time workshop.<br>
<pre><code>&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: In instantiating linked block 'Servo_ADC/ADC Input' : Invalid setting in dsPIC : ADC10 block (mask) 'ADC
Input' for parameter 'OutFormatBitspopup'.
&gt; In C:\MyToolBox\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Number of I/O PINs used : 2
Number of I/O PINs used : 2
### Starting Real-Time Workshop build procedure for model: Servo_ADC
### Generating code into build directory: C:\MyToolBox\examples\Servo_ADC_dspic\sources
Number of I/O PINs used : 2
Number of I/O PINs used : 2
Number of I/O PINs used : 2
Warning: Source 'Servo_ADC/ADC Input' specifies that its sample time (-1) is back-inherited. You should explicitly
specify the sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1
sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters
dialog box.
### Invoking Target Language Compiler on Servo_ADC.rtw
	tlc
	-r
	C:\MyToolBox\examples\Servo_ADC_dspic\sources\Servo_ADC.rtw
	C:\MyToolBox\dspic\dspic.tlc
	-OC:\MyToolBox\examples\Servo_ADC_dspic\sources
	-IC:\MyToolBox\dspic
	-IC:\MyToolBox\blocks
	-IC:\MyToolBox\examples\Servo_ADC_dspic\sources\tlc
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\mw
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\lib
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\blocks
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\fixpt
	-IC:\Programmi\MATLAB\R2007b\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=0
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=1
	-aZeroExternalMemoryAtStartup=1
	-aInitFltsAndDblsToZero=1
	-aGenerateReport=0
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=0
	-aLaunchReport=0
	-aGenerateTraceInfo=0
	-aForceParamTrailComments=0
	-aGenerateComments=1
	-aIgnoreCustomStorageClasses=0
	-aIncHierarchyInIds=0
	-aMaxRTWIdLen=31
	-aShowEliminatedStatements=0
	-aIncDataTypeInIds=0
	-aInsertBlockDesc=0
	-aSimulinkBlockComments=1
	-aInlinedPrmAccess="Literals"
	-aTargetFcnLib="ansi_tfl_table_tmw.mat"
	-aGenFloatMathFcnCalls="ANSI_C"
	-aIsPILTarget=0
	-aIncludeMdlTerminateFcn=0
	-aCombineOutputUpdateFcns=1
	-aSuppressErrorStatus=1
	-aERTCustomFileBanners=1
	-aLogVarNameModifier="rt_"
	-aGenerateFullHeader=1
	-aGenerateSampleERTMain=0
	-aMatFileLogging=0
	-aMultiInstanceERTCode=0
	-aPurelyIntegerCode=0
	-aPortableWordSizes=0
	-aGenerateErtSFunction=0
	-aGenerateASAP2=0
	-aExtMode=0
	-aExtModeStaticAlloc=0
	-aExtModeStaticAllocSize=1000000
	-aExtModeTransport=0
	-aExtModeTesting=0
	-aInlinedParameterPlacement="NonHierarchical"
	-aTargetOS="BareBoardExample"
	-aMultiInstanceErrorCode="Error"
	-aRateGroupingCode=1
	-aRTWCAPISignals=0
	-aRTWCAPIParams=0
	-aRootIOStructures=0
	-aERTCustomFileTemplate="dsPIC_main.tlc"
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="30f3012"
	-aGenerateTraceInfo=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
.....
### Initial pass through model to cache user defined code
### Caching model source code
.............
### Writing main
.
### Writing header file Servo_ADC_types.h
### Writing header file Servo_ADC.h
.
### Writing source file Servo_ADC.c
### Writing header file Servo_ADC_private.h
### Writing source file Servo_ADC_data.c
.
### Writing header file autobuild.h
### Writing source file Servo_ADC_main.c
### TLC code generation complete.
### Creating project marker file: rtw_proj.tmw
### Evaluating PostCodeGenCommand specified in the model
<wbr>
Companie =
<wbr>
     ''
<wbr>
<wbr>
<wbr>
----------------------------------------------------
Embedded Coder for dsPIC V0.96b(13-Feb-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  http://archive.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating Servo_ADC.mk from C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Building Servo_ADC: .\Servo_ADC.bat
<wbr>
C:\MyToolBox\examples\Servo_ADC_dspic\sources&gt;set MATLAB=C:\Programmi\MATLAB\R2007b  
<wbr>
C:\MyToolBox\examples\Servo_ADC_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f Servo_ADC.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Servo_ADC_data.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Servo_ADC_main.c 
Servo_ADC_main.c: In function 'main': 
Servo_ADC_main.c:58: warning: 'return' with a value, in function returning void 
Servo_ADC_main.c:48: warning: return type of 'main' is not 'int' 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_OutputCompare_Interrupt.c 
dsPIC_OutputCompare_Interrupt.c: In function '_OC1Interrupt': 
dsPIC_OutputCompare_Interrupt.c:7: warning:  PSV model not specified for '_OC1Interrupt'; 
   assuming 'auto_psv' this may affect latency 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Servo_ADC.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubcc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubcc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubrc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubrc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubrr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_backsubrr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_enab.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubcc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubcc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubcr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubcr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubrc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubrc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubrr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_forwardsubrr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look1d.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look1d32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look2d32_general.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look2d32_normal.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look2d_general.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look2d_normal.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_look32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_lu_cplx.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_lu_cplx_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_lu_real.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_lu_real_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivcc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivcc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivcr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivcr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivrc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivrc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivrr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matdivrr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandincrc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandincrc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandincrr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandincrr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultcc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultcc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultcr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultcr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultrc_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultrc_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultrr_dbl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_matmultrr_sgl.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_int16.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_int32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_int8.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_uint16.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_uint32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_div_uint8.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_int16.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_int32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_int8.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_uint16.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_uint32.c 
pic30-gcc  -c -mcpu=30F2010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\Servo_ADC_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc/rt_sat_prod_uint8.c 
"### Creating rtwlib.a " 
pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  
"### rtwlib.a Created" 
pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~2\support\gld\p30f2010.gld -o ..\../Servo_ADC.coff  Servo_ADC_data.o Servo_ADC_main.o dsPIC_OutputCompare_Interrupt.o Servo_ADC.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Programmi\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: mode pic30_coff 
Servo_ADC_data.o 
Servo_ADC_main.o 
dsPIC_OutputCompare_Interrupt.o 
Servo_ADC.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a)ConfigIntTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a)OpenTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a)OpenOC1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F2010-coff.a)ConfigIntOC1.o 
<wbr>
<wbr>
Program Memory Usage 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.reset                           0                 0x4             0x6  (6) 
.ivt                           0x4                0x7c            0xba  (186) 
.aivt                         0x84                0x7c            0xba  (186) 
.text                        0x100               0x1d4           0x2be  (702) 
.dinit                       0x2d4                0x1e            0x2d  (45) 
.isr                         0x2f2                 0x2             0x3  (3) 
__FOSC                    0xf80000                 0x2             0x3  (3) 
__FWDT                    0xf80002                 0x2             0x3  (3) 
__FBORPOR                 0xf80004                 0x2             0x3  (3) 
__FGS                     0xf8000a                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):          0x474  (1140) 9% 
<wbr>
<wbr>
Data Memory Usage 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.ndata                       0x800                   0             0x6  (6) 
.nbss                        0x806                   0             0x4  (4) 
.nbss                        0x80a                   0             0x4  (4) 
.nbss                        0x80e                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):           0x10  (16) 3% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                        0x810                               0x1f0  (496) 
<wbr>
                        Maximum dynamic memory (bytes):          0x1f0  (496) 
<wbr>
"*** Embedded Target for dsPIC written by Lubin KERHUEL -  http://archive.kerhuel.eu" 
"*** Licence Accorded to Demonstration Version                                                              " 
"*** Version 0.96b                             13-Feb-2008      " 
"*** For Matlab 7.5             R2007b       " 
"*** Created "executable": ..\../Servo_ADC.coff"	</code></pre> <br>
<br>
pic30-coff-bin2hex ..\../Servo_ADC.coff  <br>
<br>
"*** Created "executable": ..\../Servo_ADC.hex"	 <br>
<br>
### Successful completion of Real-Time Workshop build procedure for model: Servo_ADC<br>
<br>
&gt;&gt;</div>
</article>

<article class="forum-post" id="p209">
<header><strong>micman2</strong><time datetime="2008-02-14 09:08 UTC">2008-02-14 09:08 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">There is a problem, when compiling example "Servo_ADC.mdl"  work very well , but when compiling another example give me error:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/15-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p210">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-14 12:28 UTC">2008-02-14 12:28 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">I can't see the error on the image (it is cut) however, I guess that it says that the linker script ***.gld is missing.<br>
<br>
This script is provided with the C30 compiler. Could you check that you installed it and that it is present in the correct directory?</div>
</article>

<article class="forum-post" id="p211">
<header><strong>micman2</strong><time datetime="2008-02-14 13:02 UTC">2008-02-14 13:02 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Ok resolve it , the problem is :     <br>
<br>
<br>
<br>
Now all the examples are compiled perfectly. <br>
<br>
But I did a test in dsPIC33_f_Explorer16 I changed into "dspic master processor in the box PIC24fj128GA10, make an error "Error ==&gt; genMakefileAndBuild at 1070"</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/16-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p212">
<header><strong>micman2</strong><time datetime="2008-02-14 13:06 UTC">2008-02-14 13:06 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">change processor and the error is:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;----------------------------------------------------
Embedded Coder for dsPIC V0.96b(13-Feb-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  archive.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating dsPIC_33f_Explorer16.mk from C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Building dsPIC_33f_Explorer16: .\dsPIC_33f_Explorer16.bat
<wbr>
C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources&gt;set MATLAB=C:\Programmi\MATLAB\R2007b  
<wbr>
C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=p24FJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_33f_Explorer16_main.c 
pic30-coff-cc1.exe: error: Invalid -mcpu option.  CPU p24FJ128GA010 not recognized. 
<wbr>
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 255 
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask)
'Master' for parameter 'MCLR'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Number of I/O PINs used : 6
Number of I/O PINs used : 6
Number of I/O PINs used : 6
### Starting Real-Time Workshop build procedure for model: dsPIC_33f_Explorer16
### Generating code into build directory: C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources
Number of I/O PINs used : 6
Warning: Source 'dsPIC_33f_Explorer16/Digital Input' specifies that its sample time (-1) is back-inherited. You
should explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source block
specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the
Configuration Parameters dialog box.
### Invoking Target Language Compiler on dsPIC_33f_Explorer16.rtw
	tlc
	-r
	C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources\dsPIC_33f_Explorer16.rtw
	C:\MyToolBox\dspic\dspic.tlc
	-OC:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources
	-IC:\MyToolBox\dspic
	-IC:\MyToolBox\blocks
	-IC:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources\tlc
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\mw
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\lib
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\blocks
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\fixpt
	-IC:\Programmi\MATLAB\R2007b\stateflow\c\tlc
	-aEnforceIntegerDowncast=0
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=1
	-aInlineParameters=1
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=0
	-aZeroExternalMemoryAtStartup=0
	-aInitFltsAndDblsToZero=0
	-aGenerateReport=1
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=1
	-aLaunchReport=1
	-aGenerateTraceInfo=0
	-aForceParamTrailComments=0
	-aGenerateComments=1
	-aIgnoreCustomStorageClasses=0
	-aIncHierarchyInIds=0
	-aMaxRTWIdLen=31
	-aShowEliminatedStatements=0
	-aIncDataTypeInIds=0
	-aInsertBlockDesc=0
	-aSimulinkBlockComments=1
	-aInlinedPrmAccess="Literals"
	-aTargetFcnLib="ansi_tfl_table_tmw.mat"
	-aGenFloatMathFcnCalls="ANSI_C"
	-aIsPILTarget=0
	-aIncludeMdlTerminateFcn=0
	-aCombineOutputUpdateFcns=1
	-aSuppressErrorStatus=1
	-aERTCustomFileBanners=1
	-aLogVarNameModifier="rt_"
	-aGenerateFullHeader=1
	-aGenerateSampleERTMain=0
	-aMatFileLogging=0
	-aMultiInstanceERTCode=0
	-aPurelyIntegerCode=0
	-aPortableWordSizes=0
	-aGenerateErtSFunction=0
	-aGenerateASAP2=0
	-aExtMode=0
	-aExtModeStaticAlloc=0
	-aExtModeStaticAllocSize=1000000
	-aExtModeTransport=0
	-aExtModeTesting=0
	-aInlinedParameterPlacement="NonHierarchical"
	-aTargetOS="BareBoardExample"
	-aMultiInstanceErrorCode="Error"
	-aRateGroupingCode=1
	-aRTWCAPISignals=0
	-aRTWCAPIParams=0
	-aRootIOStructures=0
	-aERTCustomFileTemplate="dsPIC_main.tlc"
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=24FJ128GA010 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\gld\p24fj128ga010.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="24fj128ga010"
	-aGenerateTraceInfo=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
.....
### Initial pass through model to cache user defined code
.
### Caching model source code
.....................
### Writing main
.
### Writing header file dsPIC_33f_Explorer16_types.h
.
### Writing header file dsPIC_33f_Explorer16.h
### Writing source file dsPIC_33f_Explorer16.c
### Writing header file dsPIC_33f_Explorer16_private.h
.
### Writing header file autobuild.h
### Writing source file dsPIC_33f_Explorer16_main.c
### TLC code generation complete.
.
### Creating HTML report file dsPIC_33f_Explorer16_codegen_rpt.html
### Evaluating PostCodeGenCommand specified in the model
<wbr>
Companie =
<wbr>
     ''
<wbr>
<wbr>
<wbr>
----------------------------------------------------
Embedded Coder for dsPIC V0.96b(13-Feb-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  archive.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating dsPIC_33f_Explorer16.mk from C:\MyToolBox\dspic\dspic_pic30_gcc.tmf
### Building dsPIC_33f_Explorer16: .\dsPIC_33f_Explorer16.bat
<wbr>
C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources&gt;set MATLAB=C:\Programmi\MATLAB\R2007b  
<wbr>
C:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=24FJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\MyToolBox\examples\dsPIC_33f_Explorer16_dspic\sources -IC:\MyToolBox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_33f_Explorer16_main.c 
In file included from c:/programmi/microchip/mplab c30/bin/../support/h/peripheral_24F/timer.h:34, 
                 from dsPIC_33f_Explorer16_private.h:33, 
                 from dsPIC_33f_Explorer16_main.c:28: 
c:/programmi/microchip/mplab c30/bin/../support/h/peripheral_24F/Generic.h:56: error: syntax error before '(' token 
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 255 
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.
&gt;&gt; </code></pre></div>
</article>

<article class="forum-post" id="p213">
<header><strong>micman2</strong><time datetime="2008-02-14 13:10 UTC">2008-02-14 13:10 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">PS: excuse me for my screenshoot  and my english  :D<br>
<br>
<br>
<br>
And thank you for your disponibility  :D</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/17-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p214">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-14 15:55 UTC">2008-02-14 15:55 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">There is a know bug for 24fj PIC.<br>
<br>
I do not know why, if anybody has a suggestion.<br>
<br>
<br>
<br>
The solution is described on the release page: <a href="/RTWdsPIC/ReleaseNotes.html">http://archive.kerhuel.eu/RTWdsPIC/ReleaseNotes.html</a><br>
<blockquote>Know bug : before compiling schematic for dsPIC 24f, you must remove the line 56 of Generic.h file which is in<br>
<br>
"C:\Program Files\Microchip\MPLAB C30\support\h\peripheral_24F"<br>
<br>
The line :<br>
<br>
"typedef enum _BOOL { FALSE = 0, TRUE } BOOL;" does not compile !</blockquote></div>
</article>

<article class="forum-post" id="p215">
<header><strong>micman2</strong><time datetime="2008-02-14 16:15 UTC">2008-02-14 16:15 UTC</time></header>
<h3>Re: How to change directory?</h3>
<div class="forum-post-body">Sorry I had not seen, now everything works perfectly thanks   :D  :D  :D</div>
</article>

