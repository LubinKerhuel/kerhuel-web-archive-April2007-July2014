---
title: "Mplab Or Matlab RTW compilation ?"
url: "/forum/topic/89/"
archiveKind: "topic"
---
# Mplab Or Matlab RTW compilation ?

Forum : [General Remark and Questions](/forum/#forum-1)

8 message(s) · archive en lecture seule

<article class="forum-post" id="p222">
<header><strong>barryforever</strong><time datetime="2008-02-18 15:19 UTC">2008-02-18 15:19 UTC</time></header>
<div class="forum-post-body">Hello ..<br>
<br>
I have a simple model and i attached that model to this thread ..<br>
<br>
I have got a sucessful compilation in matlab that is using RTW.<br>
<br>
But when i compile using MPLab tool feature it shows the following error <br>
<br>
I run a Matlab r2007b and mplab v8 and your toolbox (17.02.08)<br>
<br>
it shows the following error in mplab <br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of
Master block (mask) 'Master'. Error using ==&gt;
dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC
Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop.
&gt; In &lt;a href="error:C:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m,14,1"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: In instantiating linked block
'deport/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'.
&gt; In &lt;a href="error:C:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m,14,1"&gt;MplabOpenModel at 14&lt;/a&gt;
</code></pre><br>
<br>
Which one should i use to program my dspic 6011 please tell me</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/22-deport.mdl">Pièce jointe : deport.mdl</a></p>
</article>

<article class="forum-post" id="p225">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-18 19:45 UTC">2008-02-18 19:45 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">The MASTER block set the diagram for a 30f6012 dsPIC (not 6011). <br>
<br>
RA2 do not exist on the dsPIC 30f6012, nor on the dsPIC 6011. I changed RA2 into RB3.<br>
<br>
<br>
<br>
To import the C code generated, you must follow the procedure described <a href="/RTWdsPIC/examples/ImportSimulinkMPLAB.html">here</a>.<br>
<br>
<br>
<br>
To get the .hex file from simulink in a "one click button procedure", you must uncheck "generate code only" <br>
<br>
From Simulink ==&gt; Configuration parameters ==&gt; Real-Time Workshop.<br>
<br>
<br>
I attached the modified model with the .hex file obtained.<br>
<br>
<br>
Note that if you want to import the C code to MPLAB, you should also uncheck "generate code only" in order to compile the required simulink library into an ".a" library binary file which is easier to import into MPLAB.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/23-uncheck_GenerateCodeOnly.png">Pièce jointe : uncheck_GenerateCodeOnly.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/24-deport.zip">Pièce jointe : deport.zip</a></p>
</article>

<article class="forum-post" id="p229">
<header><strong>barryforever</strong><time datetime="2008-02-19 00:51 UTC">2008-02-19 00:51 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">i tried compiling in simulink as you said but i was stopped due to error...<br>
<br>
I did your sinus PWM tutorial this is what i get<br>
<pre><code>&gt; In C:\Documents and Settings\Zion\My Documents\MATLAB\blocks\dsPIC_Set_Dialog_PopUp_Param.p&gt;dsPIC_Set_Dialog_PopUp_Param at 57
  In C:\Documents and Settings\Zion\My Documents\MATLAB\blocks\dsPIC_MASTER_callback_InitMask.p&gt;dsPIC_MASTER_callback_InitMask at 225
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
### Starting Real-Time Workshop build procedure for model: mouline
### Generating code into build directory: C:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
### Invoking Target Language Compiler on mouline.rtw
	tlc
	-r
	C:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources\mouline.rtw
	C:\Documents and Settings\Zion\My Documents\MATLAB\dspic\dspic.tlc
	-OC:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources
	-IC:\Documents and Settings\Zion\My Documents\MATLAB\dspic
	-IC:\Documents and Settings\Zion\My Documents\MATLAB\blocks
	-IC:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2007b\stateflow\c\tlc
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
....
### Initial pass through model to cache user defined code
.
### Caching model source code
.............
### Writing main
.
### Writing header file mouline_types.h
### Writing header file mouline.h
### Writing source file mouline.c
.
### Writing header file mouline_private.h
### Writing source file mouline_data.c
.
### Writing header file autobuild.h
### Writing source file mouline_main.c
### TLC code generation complete.
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
### Processing Template Makefile: C:\Documents and Settings\Zion\My Documents\MATLAB\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating mouline.mk from C:\Documents and Settings\Zion\My Documents\MATLAB\dspic\dspic_pic30_gcc.tmf
### Building mouline: .\mouline.bat
<wbr>
C:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\Documents and Settings\Zion\My Documents\MATLAB\mouline_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f mouline.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB\MOULIN~1\sources -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB\dsp -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_OutputCompare_Interrupt.c 
process_begin: CreateProcess(NULL, pic30-gcc -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB\MOULIN~1\sources -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB -IC:\DOCUME~1\Zion\MYDOCU~1\MATLAB\dsp -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc -I C:\PROGRA~1\MICROC~1\MPLABC~2\include dsPIC_OutputCompare_Interrupt.c, ...) failed. 
make (e=2): The system cannot find the file specified.  
gmake: *** [dsPIC_OutputCompare_Interrupt.o] Error 2 
### Real-Time Workshop build procedure for model: 'mouline' aborted due to an error.</code></pre><br>
<br>
There is a error in simulink<br>
<br>
<br>
<pre><code>Error building Real Time Workshop target for block diagram mouline Matlab errror Message :
Error using ==&gt;genMakeFileandBuild at 1070
errors encountered in  while building model mouline
</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/31-mouline.mdl">Pièce jointe : mouline.mdl</a></p>
</article>

<article class="forum-post" id="p230">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-19 08:15 UTC">2008-02-19 08:15 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">Is the C30 compiler (from microchip) installed on your system ?</div>
</article>

<article class="forum-post" id="p231">
<header><strong>barryforever</strong><time datetime="2008-02-19 12:19 UTC">2008-02-19 12:19 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">yes<br>
<br>
i did install it before the usage of your toolbox</div>
</article>

<article class="forum-post" id="p232">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-19 12:26 UTC">2008-02-19 12:26 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">From the error message, it's not very clear if <br>
<br>
- it does not find the compiler<br>
<br>
- it does not find the file dsPIC_OutputCompare_Interrupt.c<br>
<br>
<br>
<br>
could you type <br>
<br>
&gt;&gt; <strong>!pic30-gcc -v</strong><br>
<br>
at the matlab prompt to see if it find the C30 compiler ?<br>
<br>
<br>
<br>
you should get <br>
<pre><code>&gt;&gt; !pic30-gcc -v
Using built-in specs. 
Target: pic30-coff 
Configured with: /home/build/builds/build_20071109/src/gcc-4.0.2/gcc-4.0.2/configure --target=pic30-coff --host=i386-mingw32 --build=i386-pc-linux --program-prefix=pic30-coff- --enable-languages=c 
Thread model: single 
gcc version 4.0.3 (dsPIC30, Microchip v3_02) Build date: Nov  9 2007 
Microchip Language Tool Shell Version v3_02 (Build date: Nov  9 2007). 
Copyright (c) 2006 Microchip Technology Inc. All rights reserved 
&gt;&gt; </code></pre><br>
<br>
Also, try tp double click on the "Configure model for dsPIC Target" block before compiling. (that set up the different path for your computer)</div>
</article>

<article class="forum-post" id="p234">
<header><strong>barryforever</strong><time datetime="2008-02-20 12:38 UTC">2008-02-20 12:38 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">This is what i get <br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error
using ==&gt; dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time workshop.
&gt; In load_system at 52
  In libbrowse&gt;i_LoadSys at 142
  In libbrowse&gt;LoadLibrary at 121
  In libbrowse at 24
&gt;&gt; !pic30-gcc -v
'pic30-gcc' is not recognized as an internal or external command, 
operable program or batch file. 
&gt;&gt; </code></pre></div>
</article>

<article class="forum-post" id="p235">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-20 12:50 UTC">2008-02-20 12:50 UTC</time></header>
<h3>Re: Mplab Or Matlab RTW compilation ?</h3>
<div class="forum-post-body">the C30 compiler is not included into your environment path.<br>
<br>
<br>
<br>
try to re-install the C30 compiler from microchip.<br>
<br>
<br>
<br>
follow the procedure described on <a href="/RTWdsPIC/download.html">this page</a><br>
<br>
<br>
<br>
Beware carrefull : <strong>The path must be included to the environment</strong><br>
<br>
<br>
<br>
Then, try again to type <br>
<br>
&gt;&gt; <span style="color:#0000ff">!pic30-gcc -v</span> <br>
<br>
at the matlab prompt.</div>
</article>

