---
title: "Error 0xff appears while compiling"
url: "/forum/topic/205/"
archiveKind: "topic"
---
# Error 0xff appears while compiling

Forum : [General Remark and Questions](/forum/#forum-1)

8 message(s) · archive en lecture seule

<article class="forum-post" id="p767">
<header><strong>HTL</strong><time datetime="2009-02-25 15:21 UTC">2009-02-25 15:21 UTC</time></header>
<div class="forum-post-body">Hey i want to import a generated c code into a matlab project but i get an error when i want to build the project (model)<br>
<br>
<br>
<br>
I followed every step described on <a href="/RTWdsPIC/examples/ImportSimulinkMPLAB.html">http://archive.kerhuel.eu/RTWdsPIC/examples ... MPLAB.html</a> , also have c32 c30 and c24 compiler installated (was automatically installed with mplab!!)<br>
<br>
<br>
<br>
i hope that someone of u experts out there can help me! big thanks in advance!!<br>
<br>
<br>
<br>
.) I have a log from the building process:<br>
<br>
<br>
<br>
Command Window:<br>
<br>
<br>
<br>
C:\Programme\MATLAB\R2006b\work\suprer_dspic\sources&gt;C:\Programme\MATLAB\R2006b\rtw\bin\win32\gmake -f suprer.mk  GENERATE_REPORT=0 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
C:\\PROGRA~1\\MICROC~1\\MPLABC~1\\bin\\pic30-gcc  -c -mcpu=choose_dsPIC_Target -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\Programme\MATLAB\R2006b/simulink/include -IC:\Programme\MATLAB\R2006b/extern/include -IC:\Programme\MATLAB\R2006b/rtw/c/src -IC:\Programme\MATLAB\R2006b/rtw/c/ert -IC:\Programme\MATLAB\R2006b/rtw/c/src/ext_mode/common -IC:\Programme\MATLAB\R2006b\work\suprer_dspic\sources -IC:\Programme\MATLAB\R2006b\work -IC:\Programme\MATLAB\R2006b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    suprer_main.c <br>
<br>
gmake: *** [suprer_main.o] Error 0xff <br>
<br>
### Real-Time Workshop build procedure for model: 'suprer' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
<br>
<br>
<br>
<br>
Model error:<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'suprer'. MATLAB error message:<br>
<br>
Error using ==&gt; RTW.genMakefileAndBuild<br>
<br>
Error(s) encountered while building model "suprer".</div>
</article>

<article class="forum-post" id="p768">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-26 00:33 UTC">2009-02-26 00:33 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">Hi<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : HTL</header>-mcpu=choose_dsPIC_Target </blockquote><br>
<br>
That mean that you did not selected the target in the Master block !<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : HTL</header><a href="/archive-assets/">http://archive.kerhuel.eu/RTWdsPIC/examples</a> ... MPLAB.html</blockquote><br>
That's may be old pages. Please go to the wiki for more "up to date ;-)" informations.<br>
<br>
Try compiling an example from the example directory ! and then adapt it to your needs...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p771">
<header><strong>HTL</strong><time datetime="2009-03-02 10:21 UTC">2009-03-02 10:21 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">hey thanks for your answer!<br>
<br>
but the target is selected in the master block. see picture below:<br>
<br>
<br>
<br>
<a href="http://img119.imageshack.us/my.php?image=masterblocktarget.jpg">http://img119.imageshack.us/img119/8528 ... get.th.jpg</a><br>
<br>
<br>
<br>
and can u give me the exact link with the up to date information from the wiki?<br>
<br>
<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p772">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-02 12:57 UTC">2009-03-02 12:57 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">Thanks for the picture that help.<br>
<br>
<br>
<br>
The system target file is selected (dspic.tlc) properly: Ok<br>
<br>
<br>
<br>
But you did not select the PIC/dsPIC you are using in the Master block. Thus, dbl click on the master block, and select your target (for the moment, the selected target is 'Choose_dsPIC_Target', as written on the Master block)<br>
<br>
<br>
<br>
To get sure Simulink is properly configured, you may also add the yellow block called configure simulink for dsPIC target and dbl click on it. It will check and correct missing configuration...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p773">
<header><strong>HTL</strong><time datetime="2009-03-03 18:43 UTC">2009-03-03 18:43 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">Hey i added the configure simulink dspic target block but the same error comes!<br>
<br>
<br>
<br>
i also checked the target of the master block its the choose dspic target, if thats not the right one which target do i have to choose?<br>
<br>
<br>
<br>
here the screenshot of the master block:<br>
<br>
<a href="http://img528.imageshack.us/my.php?image=error.jpg">http://img528.imageshack.us/img528/7307/error.th.jpg</a></div>
</article>

<article class="forum-post" id="p774">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-03 18:52 UTC">2009-03-03 18:52 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : HTL</header>if thats not the right one which target do i have to choose?<br>
</blockquote><br>
That's definitly not the right target ! You must choose, within the list,microcontroller your are targetting. it can be a dsPIC30f2010 or any of the given list, but not "choose_dsPIC_Target".<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p776">
<header><strong>HTL</strong><time datetime="2009-03-10 18:47 UTC">2009-03-10 18:47 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">Hey thanks i tried it yesterday but i still get an error:<br>
<br>
Heres a code maybe theres again something wrong with the targets??<br>
<br>
I tried everything, installing matlab again and the other tools but it still doesnt work..heres the error code if u need it and below a screenshot maybe something else is not correctly configured?<br>
<pre><code>Model configured...
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: suprer
C30 Compiler found
### Generating code into build directory: C:\Programme\MATLAB\R2006b\work\suprer_dspic\sources
PTWarning: Source 'suprer/Digital Input' specifies that its sample time (-1) is back-inherited. You should explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box.
### Invoking Target Language Compiler on suprer.rtw
	tlc
	-r
	C:\Programme\MATLAB\R2006b\work\suprer_dspic\sources\suprer.rtw
	C:\Programme\MATLAB\R2006b\work\dspic\dspic.tlc
	-OC:\Programme\MATLAB\R2006b\work\suprer_dspic\sources
	-IC:\Programme\MATLAB\R2006b\work\dspic
	-IC:\Programme\MATLAB\R2006b\work\blocks
	-IC:\Programme\MATLAB\R2006b\work\suprer_dspic\sources\tlc
	-IC:\Programme\MATLAB\R2006b\rtw\c\tlc\mw
	-IC:\Programme\MATLAB\R2006b\rtw\c\tlc\lib
	-IC:\Programme\MATLAB\R2006b\rtw\c\tlc\blocks
	-IC:\Programme\MATLAB\R2006b\rtw\c\tlc\fixpt
	-IC:\Programme\MATLAB\R2006b\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=0
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aGenerateReport=0
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=0
	-aLaunchReport=0
	-aForceParamTrailComments=0
	-aGenerateComments=1
	-aIgnoreCustomStorageClasses=0
	-aIncHierarchyInIds=0
	-aMaxRTWIdLen=31
	-aShowEliminatedStatements=0
	-aPrefixModelToSubsysFcnNames=1
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
	-aGMAKE_PLACE="C:\Programme\MATLAB\R2006b\rtw\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=24fJ128GA006 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\PIC24F\gld\p24fJ128GA006.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\PIC24F\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"
	-aPIC_REF="24fJ128GA006"
	-aGCCPATH=""
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
....
### Initial pass through model to cache user defined code
.
### Caching model source code
..........
### Writing main
.
### Writing header file suprer_types.h
.
### Writing header file suprer.h
### Writing source file suprer.c
### Writing header file suprer_private.h
.
### Writing header file autobuild.h
### Writing source file suprer_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V0.99a(28-Oct-2008) for Matlab R2006b.
<wbr>
<wbr>
Licence Accorded to  Demo
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://archive.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRENE : 503 920 456
<wbr>
 Facturation to :    
<wbr>
                     WEBSITE : http://archive.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Programme\MATLAB\R2006b\work\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\Programme\MATLAB\R2006b\rtw\bin\win32\gmake&gt;
### in default batch file
### suprer.mk which is generated from C:\Programme\MATLAB\R2006b\work\dspic\dspic_pic30_gcc.tmf is up to date
### Building suprer: .\suprer.bat
<wbr>
C:\Programme\MATLAB\R2006b\work\suprer_dspic\sources&gt;set MATLAB=C:\Programme\MATLAB\R2006b  
<wbr>
C:\Programme\MATLAB\R2006b\work\suprer_dspic\sources&gt;C:\Programme\MATLAB\R2006b\rtw\bin\win32\gmake -f suprer.mk  GENERATE_REPORT=0 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=24fJ128GA006 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\Programme\MATLAB\R2006b/simulink/include -IC:\Programme\MATLAB\R2006b/extern/include -IC:\Programme\MATLAB\R2006b/rtw/c/src -IC:\Programme\MATLAB\R2006b/rtw/c/ert -IC:\Programme\MATLAB\R2006b/rtw/c/src/ext_mode/common -IC:\Programme\MATLAB\R2006b\work\suprer_dspic\sources -IC:\Programme\MATLAB\R2006b\work -IC:\Programme\MATLAB\R2006b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    suprer_main.c 
pic30-gcc  -c -mcpu=24fJ128GA006 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\Programme\MATLAB\R2006b/simulink/include -IC:\Programme\MATLAB\R2006b/extern/include -IC:\Programme\MATLAB\R2006b/rtw/c/src -IC:\Programme\MATLAB\R2006b/rtw/c/ert -IC:\Programme\MATLAB\R2006b/rtw/c/src/ext_mode/common -IC:\Programme\MATLAB\R2006b\work\suprer_dspic\sources -IC:\Programme\MATLAB\R2006b\work -IC:\Programme\MATLAB\R2006b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    suprer.c 
pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~1\support\PIC24F\gld\p24fJ128GA006.gld -o ..\../suprer.coff  suprer_main.o suprer.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\PIC24F\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a 
C:\Programme\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~1\support\PIC24F\gld\p24fJ128GA006.gld: No such file or directory 
gmake: *** [..\../suprer.coff] Error 0xff 
### Real-Time Workshop build procedure for model: 'suprer' aborted due to an error.
C30 Compiler found
&gt;&gt; </code></pre><br>
<br>
<a href="http://img145.imageshack.us/my.php?image=sameerror.jpg">http://img145.imageshack.us/img145/9500 ... ror.th.jpg</a><br>
<br>
<br>
<br>
Thanks for your answers u did, hope you can figure out what the problem is!</div>
</article>

<article class="forum-post" id="p777">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-10 22:05 UTC">2009-03-10 22:05 UTC</time></header>
<h3>Re: Error 0xff appears while compiling</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
Simulink configuration is Ok. That a problem about the installation of the Microchip C30 compiler. There is 2 version of this compiler on the microchip website. (As fas as I remember, C30 for Pic24 and C30 for dsPIC30f). Install them booth.<br>
<br>
<br>
<br>
Make sure that this file exist : <br>
<blockquote><header class="quote-author">Citation : HTL</header>C:\PROGRA~1\MICROC~1\MPLABC~1\support\PIC24F\gld\p24fJ128GA006.gld: No such file or directory </blockquote><br>
<br>
It should works properly then !<br>
<br>
<br>
<br>
Lubin</div>
</article>

