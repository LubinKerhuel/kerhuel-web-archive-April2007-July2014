---
title: "Compiling problem"
url: "/forum/topic/116/"
archiveKind: "topic"
---
# Compiling problem

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

30 message(s) · archive en lecture seule

<article class="forum-post" id="p327">
<header><strong>Anonyme</strong><time datetime="2008-05-06 14:37 UTC">2008-05-06 14:37 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I downloaded the DSPic toolbox for Simulink and I'm having some troubles making it work. I think it has something to do with the generation of the make file.<br>
<br>
<br>
<br>
Here is what is displayed on the Matlab command window when trying to compile the "Servo_Sinus" example:<br>
<br>
<br>
<pre><code>### Starting Real-Time Workshop build procedure for model: Servo_Sinus
### Generating code into build directory: C:\dspic_toolbox\examples\Servo_Sinus_dspic\sources
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
### Invoking Target Language Compiler on Servo_Sinus.rtw
	tlc
	-r
	C:\dspic_toolbox\examples\Servo_Sinus_dspic\sources\Servo_Sinus.rtw
	C:\dspic_toolbox\dspic\dspic.tlc
	-OC:\dspic_toolbox\examples\Servo_Sinus_dspic\sources
	-IC:\dspic_toolbox\dspic
	-IC:\dspic_toolbox\blocks
	-IC:\dspic_toolbox\examples\Servo_Sinus_dspic\sources\tlc
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
	-aTargetFcnLib="ansi_tfl_tmw.mat"
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
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-IC:\PROGRA~1\MICROC~1\MPLABC~1\include"
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
### Writing header file Servo_Sinus_types.h
### Writing header file Servo_Sinus.h
.
### Writing source file Servo_Sinus.c
### Writing header file Servo_Sinus_private.h
### Writing source file Servo_Sinus_data.c
.
### Writing header file autobuild.h
### Writing source file Servo_Sinus_main.c
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
Embedded Coder for dsPIC V0.97(01-Apr-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  http://www.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\dspic_toolbox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating Servo_Sinus.mk from C:\dspic_toolbox\dspic\dspic_pic30_gcc.tmf
### Building Servo_Sinus: .\Servo_Sinus.bat
<wbr>
C:\dspic_toolbox\examples\Servo_Sinus_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\dspic_toolbox\examples\Servo_Sinus_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f Servo_Sinus.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\dspic_toolbox\examples\Servo_Sinus_dspic\sources -IC:\dspic_toolbox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_Sinus_data.c 
process_begin: CreateProcess(NULL, pic30-gcc -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\dspic_toolbox\examples\Servo_Sinus_dspic\sources -IC:\dspic_toolbox\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc -IC:\PROGRA~1\MICROC~1\MPLABC~1\include Servo_Sinus_data.c, ...) failed. 
make (e=2): Le fichier spécifié est introuvable.  
gmake: *** [Servo_Sinus_data.o] Error 2 
### Real-Time Workshop build procedure for model: 'Servo_Sinus' aborted due to an error.
</code></pre><br>
<br>
Here is the message I get in the Error window:<br>
<br>
<br>
<br>
<em>Error building Real-Time Workshop target for block diagram 'Servo_Sinus'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "Servo_Sinus".</em><br>
<br>
<br>
<br>
<br>
<br>
Maybe I missed something in the Configuration Parameters...<br>
<br>
<br>
<br>
I've been trying to make it work for two whole days and I'm out of ideas.<br>
<br>
<br>
<br>
Has anyone had a similar problem?<br>
<br>
<br>
<br>
Thanks in advance for your help.<br>
<br>
<br>
<br>
Julien.</div>
</article>

<article class="forum-post" id="p328">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-06 18:48 UTC">2008-05-06 18:48 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Julien,<br>
<br>
<br>
<br>
Could you provide your matlab version ; matlab installation directory ; <br>
<br>
Could you also check on the forum for similar problems ? (for example, Is the gmake.exe program available from the matlab prompt ? )<br>
<br>
try typing !gmake and see what happen...<br>
<br>
is the C30 compiler installed ? Where is it installed ? etc...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p330">
<header><strong>Julien1138</strong><time datetime="2008-05-06 19:59 UTC">2008-05-06 19:59 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi again,<br>
<br>
<br>
<br>
Thanks for your quick answer.<br>
<br>
<br>
<br>
I'm using Matlab R2007b. It's installed in the <em>C:\Program Files\MATLAB\R2007b</em> directory.<br>
<br>
The C 30 compiler is installed in the <em>C:\Program Files\Microchip\MPLAB</em> C30 directory.<br>
<br>
By the way, the last version of C30 being V3.10, some paths are not correct in the Simulink DSPic options. For example, <em>C:\Program Files\Microchip\MPLAB C30\support\gld</em> becomes <em>C:\Program Files\Microchip\MPLAB C30\support\dsPIC30F\gld</em>. I corrected those but it doesn't fix the problem.<br>
<br>
<br>
<br>
I did a quick research for <em>gmake</em> in the forum but didn't find anything.<br>
<br>
<br>
<br>
Thanks again,<br>
<br>
<br>
<br>
Julien.</div>
</article>

<article class="forum-post" id="p331">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-06 20:41 UTC">2008-05-06 20:41 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">The C30 compiler V3.10 has been released few days ago. I did not test it on the blockset yet. There may be few problems.<br>
<br>
I'll try to look at it soon.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p374">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-20 16:26 UTC">2008-05-20 16:26 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Julien,<br>
<br>
<br>
<br>
The new release (V0.98) of the blockset now support the PIC30 v3.10.<br>
<br>
Therefore, you have to install this version of the compiler (available on the website of Microchip) in order to have the blockset working.<br>
<br>
<br>
<br>
Do not forget to add the block "Configure Model for dsPIC" and to double click on it. The model needs to be reconfigured when upgrading to this version.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p378">
<header><strong>Julien1138</strong><time datetime="2008-05-21 14:02 UTC">2008-05-21 14:02 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I tried the new release of your blockset.<br>
<br>
<br>
<br>
However I still have the same error :<br>
<br>
<br>
<pre><code>### Generating code into build directory: C:\essais_tlc\dspic\Servo_Sinus_dspic\sources
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
### Invoking Target Language Compiler on Servo_Sinus.rtw
	tlc
	-r
	C:\essais_tlc\dspic\Servo_Sinus_dspic\sources\Servo_Sinus.rtw
	C:\dspic_toolbox\dspic\dspic.tlc
	-OC:\essais_tlc\dspic\Servo_Sinus_dspic\sources
	-IC:\dspic_toolbox\dspic
	-IC:\dspic_toolbox\blocks
	-IC:\essais_tlc\dspic\Servo_Sinus_dspic\sources\tlc
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
	-aTargetFcnLib="ansi_tfl_tmw.mat"
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
	-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"
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
### Writing header file Servo_Sinus_types.h
### Writing header file Servo_Sinus.h
.
### Writing source file Servo_Sinus.c
### Writing header file Servo_Sinus_private.h
### Writing source file Servo_Sinus_data.c
.
### Writing header file autobuild.h
### Writing source file Servo_Sinus_main.c
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
Embedded Coder for dsPIC V0.98(21-May-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  www.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\dspic_toolbox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating Servo_Sinus.mk from C:\dspic_toolbox\dspic\dspic_pic30_gcc.tmf
### Building Servo_Sinus: .\Servo_Sinus.bat
<wbr>
C:\essais_tlc\dspic\Servo_Sinus_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\essais_tlc\dspic\Servo_Sinus_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f Servo_Sinus.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\essais_tlc\dspic\Servo_Sinus_dspic\sources -IC:\essais_tlc\dspic -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_Sinus_data.c 
process_begin: CreateProcess(NULL, pic30-gcc -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\essais_tlc\dspic\Servo_Sinus_dspic\sources -IC:\essais_tlc\dspic -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc -I C:\PROGRA~1\MICROC~1\MPLABC~1\include Servo_Sinus_data.c, ...) failed. 
make (e=2): Le fichier spécifié est introuvable.  
gmake: *** [Servo_Sinus_data.o] Error 2 
### Real-Time Workshop build procedure for model: 'Servo_Sinus' aborted due to an error.</code></pre><br>
<br>
I'm going crazy. I can't find any explanation to this error.<br>
<br>
<br>
<br>
when typing "!!C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" or "!gmake" in the Matlab prompt I get the following:<br>
<br>
gmake: *** No targets specified and no makefile found.  Stop.<br>
<br>
<br>
<br>
Is it normal ?<br>
<br>
<br>
<br>
Julien</div>
</article>

<article class="forum-post" id="p379">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-21 16:44 UTC">2008-05-21 16:44 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Julien,<br>
<br>
<br>
<br>
Thanks for your interrest for the blockset.<br>
<br>
<br>
<br>
My understanding is than Matlab could not acces to the PIC30 compiler. The compiler path must be added into the environment variables.<br>
<br>
To check if Matlab find the C30 compiler, you can type at the matlab prompt : <br>
<br>
&gt;&gt; <strong>!pic30-gcc</strong><br>
<br>
The normal response is : <br>
<br>
<strong>pic30-coff-gcc.exe: no input files</strong><br>
<br>
<br>
<br>
If you get a message telling that matlab did not recognize the command, you should re-install the compiler and be carefull to add its path into the system (checkbox to check).<br>
<br>
<br>
<br>
I do not think the problem comes from the blockset since it appears during the compilation process.<br>
<br>
Btw, let us know... even if it is not working !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p444">
<header><strong>NigmaTech</strong><time datetime="2008-08-01 11:54 UTC">2008-08-01 11:54 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">I've got the same problem. When I want to compile Servo_sinus.mdl Matlab displays:<br>
<br>
<br>
<br>
.<br>
<br>
### Processing Template Makefile: D:\Program Files\MATLAB\R2007b\PIC\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Wrapping unrecognized make command (angle brackets added)<br>
<br>
###    &lt;D:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;<br>
<br>
### in default batch file<br>
<br>
### Creating Servo_Sinus.mk from D:\Program Files\MATLAB\R2007b\PIC\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building Servo_Sinus: .\Servo_Sinus.bat<br>
<br>
 <br>
<br>
D:\Program Files\MATLAB\R2007b\PIC\examples\Servo_Sinus_dspic\sources&gt;set MATLAB=D:\Program Files\MATLAB\R2007b  <br>
<br>
 <br>
<br>
D:\Program Files\MATLAB\R2007b\PIC\examples\Servo_Sinus_dspic\sources&gt;D:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f Servo_Sinus.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
pic30-gcc  -c -mcpu=30f6010A -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2007b/simulink/include -ID:\PROGRA~1\MATLAB\R2007b/extern/include -ID:\PROGRA~1\MATLAB\R2007b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\PROGRA~1\MATLAB\R2007b\PIC\examples\Servo_Sinus_dspic\sources -ID:\PROGRA~1\MATLAB\R2007b\PIC\examples -ID:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\Microchip\MPLAB C30\include    Servo_Sinus_data.c <br>
<br>
pic30-coff-gcc.exe: C30\include: No such file or directory <br>
<br>
gmake: *** [Servo_Sinus_data.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'Servo_Sinus' aborted due to an error.<br>
<br>
&gt;&gt; <br>
<br>
<br>
<br>
I'm using C30 3.10b compiler. I've intalled Matlab twice, 4 times dsPIC blockset and 3 times C30 compiler.</div>
</article>

<article class="forum-post" id="p445">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-02 20:15 UTC">2008-08-02 20:15 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi NigmaTech,<br>
<br>
<br>
<br>
Make sure that the bin directory of the C30 compiler is added in the windows path.<br>
<br>
Matlab must find the .exe file present in the C30 repertory because this directory should be in the windows path. It it is not present, you should add it manually !<br>
<br>
<br>
<br>
If too many people get the problem, I will try to modify the blockset to make it easier...<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p446">
<header><strong>NigmaTech</strong><time datetime="2008-08-03 22:02 UTC">2008-08-03 22:02 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Windows path? I don't know what are you talking about. C30 i installed typically on C:\program files\...</div>
</article>

<article class="forum-post" id="p447">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-04 08:32 UTC">2008-08-04 08:32 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">to add the C:\program files\...C30...\bin directory in the path,<br>
<br>
have a look on  <a href="http://www.computerhope.com/issues/ch000549.htm">http://www.computerhope.com/issues/ch000549.htm</a></div>
</article>

<article class="forum-post" id="p448">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-05 10:11 UTC">2008-08-05 10:11 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">The next version of the blockset will be able to find the C30 compiler even if it is not added in the windows path.<br>
<br>
This version will be released next month : september 2008.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p452">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-13 07:46 UTC">2008-08-13 07:46 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
If the directory you are working in has a very long path, you may get error during the compilation.<br>
<br>
The solution is to create a virtual drive with its roots at your directory: <br>
<br>
<br>
<br>
At the matlab prompt, type: <br>
<br>
!subst z: "C:\Documents and Settings\Bernard\Mes documents\MATLAB\Very very long path ... \... \.....\lastDirectoryName"<br>
<br>
<br>
<br>
And now go to the directory z:\ and continue to work as usual.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p490">
<header><strong>arsen</strong><time datetime="2008-09-01 13:56 UTC">2008-09-01 13:56 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">hi lubin,<br>
<br>
i have exactly same problem ;<br>
<br>
and i ve the same output at matlab promt<br>
<br>
following;<br>
<br>
<br>
<pre><code>&gt;&gt; C30 Compiler found
C30 Compiler found
Model configured...
C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: Servo_Sinus
### Generating code into build directory: C:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources
P
T
T
P
Number of I/O PINs used : 1
T
P
Number of I/O PINs used : 1
T
P
T
P
T
P
T
P
T
P
Number of I/O PINs used : 1
T
P
T
P
Number of I/O PINs used : 1
T
P
T
P
T
P
T
### Invoking Target Language Compiler on Servo_Sinus.rtw
tlc
-r
C:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources\Servo_Sinus.rtw
C:\Users\james\Desktop\some_programes\dspic\dspic\dspic.tlc
-OC:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources
-IC:\Users\james\Desktop\some_programes\dspic\dspic
-IC:\Users\james\Desktop\some_programes\dspic\blocks
-IC:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources\tlc
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
-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"
-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0 -cref"
-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f3012.gld"
-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"
-aPIC_REF="30f3012"
-aGCCPATH=""
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
### Writing header file Servo_Sinus_types.h
### Writing header file Servo_Sinus.h
.
### Writing source file Servo_Sinus.c
### Writing header file Servo_Sinus_private.h
### Writing source file Servo_Sinus_data.c
.
### Writing header file autobuild.h
### Writing source file Servo_Sinus_main.c
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
Embedded Coder for dsPIC V0.98f(09-Aug-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at http://www.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\Users\james\Desktop\some_programes\dspic\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
### &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Servo_Sinus.mk which is generated from C:\Users\james\Desktop\some_programes\dspic\dspic\dspic_pic30_gcc.tmf is up to date
### Building Servo_Sinus: .\Servo_Sinus.bat
<wbr>
C:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b 
<wbr>
C:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f Servo_Sinus.mk GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0 
''pic30-gcc -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Users\james\Desktop\some_programes\dspic\examples\Servo_Sinus_dspic\sources -IC:\Users\james\Desktop\some_programes\dspic\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc -I C:\PROGRA~1\MICROC~1\MPLABC~1\include Servo_Sinus_data.c 
Microchip MPLAB C30 License Manager Version v3_11 (Build Date Jul 16 2008). 
Copyright (c) 2008 Microchip Technology Inc. All rights reserved. 
The MPLAB C30 license manager command-line is invalid. 
pic30-coff-cc1.exe: error: License manager failure, please contact your support 
representative or http://support.microchip.com 
gmake: *** [Servo_Sinus_data.o] Error 255 
### Real-Time Workshop build procedure for model: 'Servo_Sinus' aborted due to an error.
C30 Compiler found
C30 Compiler found
</code></pre><br>
i ve read the forum carefully and i did exactly every process<br>
<br>
i ve add the path to windows C:\Program Files\Microchip\MPLAB C30\bin <br>
<br>
and i am using the last version of the boclset 0.98<br>
<br>
since 2 days i am dealing with this problem an i gonna be crazy:))<br>
<br>
please help<br>
<br>
thanx for now<br>
<br>
also i did following command and feedback is true<br>
<br>
!pic30-gcc<br>
<br>
pic30-coff-gcc.exe: no input files <br>
<br>
<br>
<br>
please help wishes <br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p491">
<header><strong>arsen</strong><time datetime="2008-09-01 14:23 UTC">2008-09-01 14:23 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">and i am using matlab  version 2007b</div>
</article>

<article class="forum-post" id="p492">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-01 14:42 UTC">2008-09-01 14:42 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi arsen,<br>
<br>
<br>
<br>
The blockset find the C30 compiler. The problem is out there.<br>
<br>
<br>
<br>
It seems to be a licence problem about the C30 compiler. Are you using a version for student ?<br>
<br>
I did not test yet the version 3.11 of C30 thus I am still using the 3.10.<br>
<br>
<br>
<br>
Did you install the free C30 compiler for student ? <br>
<br>
Can you manage to compile a project with the C30 version you install ?<br>
<br>
<br>
<br>
The question then is :<br>
<br>
Does the free C30 version 3.11 not work as soon as an unsupported optimisation option is used ?<br>
<br>
In that case, I will add the possibility to add/remove compilation options...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p493">
<header><strong>arsen</strong><time datetime="2008-09-01 15:05 UTC">2008-09-01 15:05 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">hi Lubin <br>
<br>
thanx for quick response:)<br>
<br>
 i am using <span style="color:#ff8000">MPLAB_C_dsPICStudent_v3_11</span> that i ve downloaded from '<a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1406&amp;dDocName=en534868">http://www.microchip.com/stellent/idcpl ... e=en534868</a>'<br>
<br>
 and i could not compile any project even an example project servo_sinus<br>
<br>
wishes<br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p495">
<header><strong>arsen</strong><time datetime="2008-09-02 12:14 UTC">2008-09-02 12:14 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">hi lubin <br>
<br>
today ive download c compiler v3.11 again and installed , unfortunately i ve  still got the same prob:((<br>
<br>
wishes<br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p496">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-02 18:05 UTC">2008-09-02 18:05 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">I tested the C30 v3.11(b) version for students and it seems to works properly. (test with matlab 2006a)<br>
<br>
<br>
<br>
could you try to place a block "<strong>Configure Model for dsPIC</strong>" in your model, dbl click on it and then try to compile ?<br>
<br>
<br>
<br>
If you get a problem, try to compile a simple project in the microchip MPLAB IDE. If it does not work, you have an installation problem for the C30 compiler.</div>
</article>

<article class="forum-post" id="p498">
<header><strong>arsen</strong><time datetime="2008-09-03 07:43 UTC">2008-09-03 07:43 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">thanx Lubin i will do ur advise properly by th way i am using matlab 2007b version . and i would like to explain  all the procedure step by step<br>
<br>
my model name is first.mdl<br>
<br>
i have double click on my model in order to open then i ve got following from matlab promt<pre><code>C30 Compiler found
Warning: dsPICdrivers.mdl, line 52: block_diagram does not have a parameter named 'CovModelRefEnable'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt;
dsPIC_ConfigRTWOption at 98
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters
==&gt; Real Time workshop.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196</code></pre><br>
<br>
then as you said i ve placed th block Configure Model for dsPIC and double click on it then <pre><code>P
T
C30 Compiler found
C30 Compiler found
Model configured...</code></pre><br>
 i ve got this from matlab promt<br>
<br>
after that ive started to build the project and <br>
<pre><code>C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: first
### Generating code into build directory: C:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources
P
P
Number of I/O PINs used : 1
T
P
T
P
T
P
Number of I/O PINs used : 1
T
T
T
P
Number of I/O PINs used : 1
T
P
T
P
T
P
T
P
Number of I/O PINs used : 1
T
P
T
P
T
P
T
P
T
P
Number of I/O PINs used : 1
T
P
T
P
T
### Invoking Target Language Compiler on first.rtw
	tlc
	-r
	C:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources\first.rtw
	C:\Users\james\Desktop\some_programes\dspic\dspic\dspic.tlc
	-OC:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources
	-IC:\Users\james\Desktop\some_programes\dspic\dspic
	-IC:\Users\james\Desktop\some_programes\dspic\blocks
	-IC:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources\tlc
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
	-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"
	-aPIC_REF="30f3012"
	-aGCCPATH=""
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
### Writing header file first_types.h
### Writing header file first.h
.
### Writing source file first.c
### Writing header file first_private.h
### Writing source file first_data.c
.
### Writing header file autobuild.h
### Writing source file first_main.c
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
Embedded Coder for dsPIC V0.98f(09-Aug-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  www.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\Users\james\Desktop\some_programes\dspic\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### first.mk which is generated from C:\Users\james\Desktop\some_programes\dspic\dspic\dspic_pic30_gcc.tmf is up to date
### Building first: .\first.bat
<wbr>
C:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake -f first.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC\first_dspic\sources -IC:\Users\james\Desktop\cemal\stateflow\some_samples\metanet\traffic_control\embedded\PIC -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    dsPIC_OutputCompare_Interrupt.c 
Microchip MPLAB C30 License Manager Version v3_11 (Build Date Jul 16 2008). 
Copyright (c) 2008 Microchip Technology Inc. All rights reserved. 
The MPLAB C30 license manager command-line is invalid. 
pic30-coff-cc1.exe: error: License manager failure, please contact your support 
   representative or http://support.microchip.com 
gmake: *** [dsPIC_OutputCompare_Interrupt.o] Error 255 
### Real-Time Workshop build procedure for model: 'first' aborted due to an error.
C30 Compiler found
C30 Compiler found</code></pre><br>
unfortunately i ve got the same error:( i am uploading my project maybe works with ur c30 compiler <br>
<br>
the interesting thing here is i ve tried to compile default examples from folder also did not worked( sinus_servo)<br>
<br>
anyway thank you very much that u spend time on it but beleive me i am getting crazy<br>
<br>
thanx alot again <br>
<br>
wishes <br>
<br>
arsen</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/112-first.mdl">Pièce jointe : first.mdl</a></p>
</article>

<article class="forum-post" id="p499">
<header><strong>arsen</strong><time datetime="2008-09-03 08:08 UTC">2008-09-03 08:08 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">and also i ve found some licence problem s from micro chip forum web site  <a href="http://forum.microchip.com/tm.aspx?m=193512&amp;mpage=1&amp;key=Whats%2Clicense%2Cmanager%2C...%2Cinvalid&amp;#193512">http://forum.microchip.com/tm.aspx?m=19 ... id𯏨</a><br>
<br>
there one user, jasonk, says( at the end of the window)<br>
<br>
'kmougiakos, <br>
<br>
<br>
<br>
Assuming that you are using the student edition, you can disable the "Make warnings into errors (-Werror)" project build option. You are getting a warning that the student edition is now feature limited and that warning is halting the build process because of that option. <br>
<br>
'<br>
<br>
mybe i ve got to do <span style="color:#ffff40">'the student edition, you can disable the "Make warnings into errors (-Werror)" project build optio</span>n'  <br>
<br>
maybe problem is that ? should i do this action if yes , how?<br>
<br>
what do u think Lubin?<br>
<br>
<br>
<br>
wishes arsen</div>
</article>

<article class="forum-post" id="p502">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-03 20:25 UTC">2008-09-03 20:25 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi arsen,<br>
<br>
<br>
<br>
I added the block <strong>Configure Model for dsPIC</strong> and dbl click on it before compiling your model without problems.<br>
<br>
<br>
<br>
You are describing a license problem for the C30 compiler. My guess is that your perhaps updated an older version of C30 and something get wrong. If I were you, I will try to remove the C30 compiler (remove also manually files that may keep in place, and try to clean up the windows registry ; maybe C30 has placed an entry in the registry)<br>
<br>
Anyway, you will certainly find better answer on microchip forum.<br>
<br>
<br>
<br>
If you want to add options at the command line, you can try to do so from simulink :  Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; dsPIC Options<br>
<br>
Be aware however that theses options lines are parsed and modified automatically by the blockset (check that your modifications are keept)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p505">
<header><strong>arsen</strong><time datetime="2008-09-04 12:07 UTC">2008-09-04 12:07 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
thanx alot again because u are spending ur valuable time for that for mee thanx and sorry:)<br>
<br>
any way i will do the procedure that u told me today and i will let u know what happened<br>
<br>
by the way yesterday i ve check the box  generate ony code option under  Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop then i could generate the c code without problem , as  far as i understood as u said the problem is is creating the hex and coff file, any way yesterday i ve mentioned the same problem at microchip forum and added <a href="http://forum.microchip.com/tm.aspx?m=355914">http://forum.microchip.com/tm.aspx?m=355914</a>  <br>
<br>
thanx alot <br>
<br>
( i am using visa home premium edition this could not be a problem or??)<br>
<br>
best wishes<br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p506">
<header><strong>arsen</strong><time datetime="2008-09-04 13:36 UTC">2008-09-04 13:36 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hİİİİİİ Lubin,<br>
<br>
millions times thanx , i ve deleted every registry  entry of microchip and mplab manualyy and reinstall again and works fine super thanx,<br>
<br>
now i can start to design and complee thanx alot since 1 week  i got this problem  and i was neary getting crazy<br>
<br>
wishes <br>
<br>
arsen<br>
<br>
p.s: during the design and compilation may i ask questions when i got problems  in future?:==))</div>
</article>

<article class="forum-post" id="p508">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-04 21:37 UTC">2008-09-04 21:37 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Arsen,<br>
<br>
<br>
<br>
I'm Glad you finally make it!<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : arsen</header>during the design and compilation may i ask questions when i got problems in future?:==))</blockquote><br>
any question related to the dsPIC embedded coder for Simulink are welcome.<br>
<br>
<br>
<br>
Just a remark : when you reply, just click on reply at the bottom. The quote button is not the good way to respond (I just clean up the messages you posted)</div>
</article>

<article class="forum-post" id="p509">
<header><strong>arsen</strong><time datetime="2008-09-05 07:31 UTC">2008-09-05 07:31 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">hi Lubin ,<br>
<br>
i am glad too thanx again i am sure that i am gonna have problems in future <br>
<br>
have a nice day :D  :P  :lol:  8) <br>
<br>
wishes <br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p510">
<header><strong>gdiana</strong><time datetime="2008-09-08 03:55 UTC">2008-09-08 03:55 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body"><span style="color:#4000ff">The MPLAB C30 license manager command-line is invalid. <br>
<br>
pic30-coff-cc1.exe: error: License manager failure, please contact your support <br>
<br>
representative or <a href="http://support.microchip.com">http://support.microchip.com</a> <br>
<br>
gmake: *** [Servo_Sinus_data.o] Error 255</span><br>
<br>
<br>
<br>
Hi,<br>
<br>
<br>
<br>
I has a similar error previously. I found the problem to be the use of the incorrect C30 compiler. Microchip has a separate C30 compiler for both the PIC24 and dsPIC. If one installs the PIC24 and tries to compile for the dsPIC you get the abovementioned error. The same the other way around. Unfortunately, the error message above does not identify which C30 (PIC24 or dsPIC) it is using nor the version.<br>
<br>
<br>
<br>
<em><strong>I have also reported the problem with the compiler paths not automatically being added to the windows path to Microchip. In some cases when one does a manual install of either the PIC24 and dsPIC C30 compilers it does NOT add to the windows path.</strong></em><br>
<br>
<br>
<br>
Lubin I suggest that as part of the installation process you generate a message to remind new users of this potential problem. I know you have added this to your installation guide process but it appears not all people READ IT. Maybe a warning just prior to download and/or just after installation?<br>
<br>
<br>
<br>
Kind regards<br>
<br>
<br>
<br>
<br>
<br>
Greg Diana</div>
</article>

<article class="forum-post" id="p513">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-09 21:40 UTC">2008-09-09 21:40 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Thanks gdiana for the good idea.<br>
<br>
<br>
<br>
I added a message at the end of the installation script.<br>
<br>
It will be available in the next release (following 0.98fc).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p591">
<header><strong>arsen</strong><time datetime="2008-10-28 14:49 UTC">2008-10-28 14:49 UTC</time></header>
<h3>compiler path</h3>
<div class="forum-post-body">hi Lubin :) <br>
<br>
i ve formatted my pc and installed matlab mplab compiler ans 0.98ef again  everything works fine no prob. but since i ve installed mplab under directory d then  i ve installed  compiler c30 also same directory where mplab exists ( D:\Program Files\Microchip\MPLAB C30)<br>
<br>
when i ve tried to open my project following warning appears<br>
<pre><code>= C30 directory not found ============================================
======================================================================
======================================================================
======================================================================
Enter C30 compiler directory (like C:\Program Files\Microchip\MPLAB C30
 (You have to do it twice, copy-past)</code></pre>  <br>
<br>
then i ve done what u wrote there and entered the right path<br>
<pre><code> ----&gt;D:\Program Files\Microchip\MPLAB C30
C30 Compiler found</code></pre><br>
then my model opens correctly fine  but i had to do this prosess all the time whenever i open my model unfortunately. then i ve added the path manually  ( D:\Program Files\Microchip\MPLAB C30) to the  simulation--&gt;configuration parameters--&gt;dspic options--&gt;compiler path by my self  unfortunately  this did not work also so i had to type  the path to the matlab prompt everytime when i would like to open my model.  Do u have any ideas??<br>
<br>
wishes thanx <br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p592">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-28 19:11 UTC">2008-10-28 19:11 UTC</time></header>
<h3>Re: Compiling problem</h3>
<div class="forum-post-body">Hi Arsen,<br>
<br>
<br>
<br>
It is not obvious to correct that.<br>
<br>
Btw, I added the <strong>D:\Program Files\Microchip\MPLAB C30</strong> directory to the search directory and it may solve your problem (look for the version update comming very soon). For others with similar problems, I suggest to make a copy of the <strong>MPLAB C30</strong> directory in the <strong>C:\Program Files\Microchip\</strong> directory ! that makes everything easy !<br>
<br>
<br>
<br>
Lubin</div>
</article>

