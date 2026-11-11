---
title: "Error"
url: "/forum/topic/235/"
archiveKind: "topic"
---
# Error

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p891">
<header><strong>tnguyen</strong><time datetime="2009-07-12 21:40 UTC">2009-07-12 21:40 UTC</time></header>
<div class="forum-post-body">Hi.<br>
<br>
<br>
<br>
I am trying to compile the dsPIC_33f_Explorer16, but I run into an error.  I am not sure how to solve this problem. <br>
<br>
Any help is much appreciated. <br>
<br>
<br>
<br>
Thanks,<br>
<br>
Tina<br>
<br>
<br>
<br>
<br>
<br>
I get this message error:<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'dsPIC_33f_Explorer16'. MATLAB error message:<br>
<br>
Error using ==&gt; RTW.genMakefileAndBuild<br>
<br>
Error(s) encountered while building model "dsPIC_33f_Explorer16".<br>
<br>
<br>
<br>
I get the following message:<br>
<br>
<br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.
&gt; In load_system at 44
  In libbrowse&gt;i_LoadSys at 135
  In libbrowse&gt;LoadLibrary at 114
  In libbrowse at 24
C30 Compiler found
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'MCLR'.
&gt; In C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9
  In C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36
  In general\private\openmdl at 13
  In open at 141
  In uiopen at 181
PTPNumber of I/O PINs used : 6
TPTPTPTTPTPTC30 Compiler found
C30 Compiler found
Model configured...
C30 Compiler found
C30 Compiler found
<wbr>
### Starting Real-Time Workshop build procedure for model: dsPIC_33f_Explorer16
C30 Compiler found
### Generating code into build directory: C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources
PNumber of I/O PINs used : 6
TWarning: Source 'dsPIC_33f_Explorer16/Digital Input' specifies that its sample time (-1) is back-inherited. You should explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box.
Warning: Parameter precision loss occurred for 'Value'. The value you specifed cannot be represented exactly using the parameter's run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated from 'dsPIC_33f_Explorer16/Compare To Constant/Constant'.
### Invoking Target Language Compiler on dsPIC_33f_Explorer16.rtw
	tlc
	-r
	C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources\dsPIC_33f_Explorer16.rtw
	C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic.tlc
	-OC:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources
	-IC:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic
	-IC:\Program Files\MATLAB\R2006a\install_dspic_r2006a\blocks
	-IC:\Program Files\MATLAB\R2006a\toolbox\simulink\fixedandfloat\tlc_c
	-IC:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2006a\stateflow\c\tlc
	-aEnforceIntegerDowncast=0
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=1
	-aInlineParameters=1
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aGenerateReport=1
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=1
	-aLaunchReport=1
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
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=33fJ256GP710 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~3\support\dsPIC33F\gld\p33fJ256GP710.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~3\lib\dsPIC33F\libp33fJ256GP710-coff.a C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~3\include"
	-aPIC_REF="33fJ256GP710"
	-aGCCPATH=""
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
....
### Initial pass through model to cache user defined code
..
### Caching model source code
........................
### Writing main
### Writing header file dsPIC_33f_Explorer16_types.h
.
### Writing header file dsPIC_33f_Explorer16.h
### Writing source file dsPIC_33f_Explorer16.c
### Writing header file dsPIC_33f_Explorer16_private.h
.
### Writing header file autobuild.h
### Writing source file dsPIC_33f_Explorer16_main.c
### TLC code generation complete.
### Creating HTML report file dsPIC_33f_Explorer16_codegen_rpt.html
.### Creating project marker file: rtw_proj.tmw
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V0.99g(08-Jul-2009) for Matlab R2006a.
<wbr>
<wbr>
Licence Accorded to  Demonstration Version
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://www.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
 Facturation to :    
<wbr>
                     Montee du chateau
                     Rue de l arene
                     13260 Cassis
                     FRANCE
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic_pic30_gcc.tmf
### Creating dsPIC_33f_Explorer16.mk from C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic_pic30_gcc.tmf
### Building dsPIC_33f_Explorer16: .\dsPIC_33f_Explorer16.bat
<wbr>
C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2006a  
<wbr>
C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake" -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 ADD_MDL_NAME_TO_GLOBALS=1  
pic30-gcc  -c -mcpu=33fJ256GP710 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2006a/simulink/include -IC:\PROGRA~1\MATLAB\R2006a/extern/include -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/src/ext_mode/common -IC:\PROGRA~1\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources -IC:\PROGRA~1\MATLAB\R2006a\work -IC:\PROGRA~1\MATLAB\R2006a\INSTAL~1\examples -IC:\PROGRA~1\MATLAB\R2006a\work -IC:\PROGRA~1\MATLAB\R2006a\work\DSPIC_~1\sources -IC:\PROGRA~1\MATLAB\R2006a\rtw\c\libsrc -IC:\PROGRA~1\MATLAB\R2006a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~3\include    dsPIC_33f_Explorer16_main.c 
dsPIC_33f_Explorer16_main.c: In function '_FICD': 
dsPIC_33f_Explorer16_main.c:39: error: syntax error before '{' token 
dsPIC_33f_Explorer16_main.c:45: error: syntax error before 'dsPIC_33f_Explorer16_SetEventsForThisBaseStep' 
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 0xff 
C30 Compiler found
C30 Compiler found</code></pre></div>
</article>

<article class="forum-post" id="p892">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-13 10:19 UTC">2009-07-13 10:19 UTC</time></header>
<h3>Re: Error</h3>
<div class="forum-post-body">Hi Tina,<br>
<br>
<br>
<br>
Thanks for description of the error. I could not reproduce it, using Matlab 2006a and pic30-gcc V3.12 (type at matlab prompt   &gt;&gt; !pic30-gcc -v ) and model provided in the example directory dsPIC dsPIC_33f_Explorer16.mdl as is.<br>
<br>
<br>
<br>
I attach the correct C code file generated on my system. This file seems to cause the problem on your system. <br>
<br>
Could you my generated C code file with yours ? Perhaps you changed a parameter in the master block and this change generate the error. In this case, could you send your model file so I can see and correct the bug ?<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/247-dsPIC_33f_Explorer16_main.c">Pièce jointe : dsPIC_33f_Explorer16_main.c</a></p>
</article>

<article class="forum-post" id="p894">
<header><strong>tnguyen</strong><time datetime="2009-07-13 21:09 UTC">2009-07-13 21:09 UTC</time></header>
<h3>Re: Error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for the quick response back.<br>
<br>
<br>
<br>
When typing in !pic30-gcc -v in the matlab prompt I obtain this message:<br>
 <pre><code>PT&gt;&gt; !pic30-gcc -v
Using built-in specs. 
Target: pic30-coff 
Configured with: ../../src/gcc-4.0.2/gcc-4.0.2//configure --target=pic30-coff --program-prefix=pic30-coff- --enable-languages=c --host=mingw32 --build=i386-pc-cygwin 
Thread model: single 
gcc version 4.0.3 (dsPIC30, Microchip v3.00) Build date: Feb 28 2007 
Microchip Language Tool Shell Version v3.00 (Build date: Feb 28 2007). 
Copyright (c) 2006 Microchip Technology Inc. All rights reserved</code></pre><br>
<br>
I also attached the model I am using.<br>
<br>
<br>
<br>
In addition, I replaced my main C code file with your main C code file and I obtained the same error.  Was I suppose to do it another way?<br>
<pre><code>PNumber of I/O PINs used : 6
TPTPTPTTPTPTPTPNumber of I/O PINs used : 6
TPTPTTPTPTC30 Compiler found
C30 Compiler found
<wbr>
### Starting Real-Time Workshop build procedure for model: dsPIC_33f_Explorer16
C30 Compiler found
### Generating code into build directory: C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources
PTWarning: Source 'dsPIC_33f_Explorer16/Digital Input' specifies that its sample time (-1) is back-inherited. You should explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box.
Warning: Parameter precision loss occurred for 'Value'. The value you specifed cannot be represented exactly using the parameter's run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated from 'dsPIC_33f_Explorer16/Compare To Constant/Constant'.
### Invoking Target Language Compiler on dsPIC_33f_Explorer16.rtw
	tlc
	-r
	C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources\dsPIC_33f_Explorer16.rtw
	C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic.tlc
	-OC:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources
	-IC:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic
	-IC:\Program Files\MATLAB\R2006a\install_dspic_r2006a\blocks
	-IC:\Program Files\MATLAB\R2006a\toolbox\simulink\fixedandfloat\tlc_c
	-IC:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2006a\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2006a\stateflow\c\tlc
	-aEnforceIntegerDowncast=0
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=1
	-aInlineParameters=1
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aGenerateReport=1
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=1
	-aLaunchReport=1
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
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=33fJ256GP710 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~3\support\dsPIC33F\gld\p33fJ256GP710.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~3\lib\dsPIC33F\libp33fJ256GP710-coff.a C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~3\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~3\include"
	-aPIC_REF="33fJ256GP710"
	-aGCCPATH=""
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
....
### Initial pass through model to cache user defined code
..
### Caching model source code
........................
### Writing main
### Writing header file dsPIC_33f_Explorer16_types.h
.
### Writing header file dsPIC_33f_Explorer16.h
### Writing source file dsPIC_33f_Explorer16.c
### Writing header file dsPIC_33f_Explorer16_private.h
.
### Writing header file autobuild.h
### Writing source file dsPIC_33f_Explorer16_main.c
### TLC code generation complete.
### Creating HTML report file dsPIC_33f_Explorer16_codegen_rpt.html
.### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V0.99g(08-Jul-2009) for Matlab R2006a.
<wbr>
<wbr>
Licence Accorded to  Demonstration Version
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://www.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
 Facturation to :    
<wbr>
                     Montee du chateau
                     Rue de l arene
                     13260 Cassis
                     FRANCE
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic_pic30_gcc.tmf
### dsPIC_33f_Explorer16.mk which is generated from C:\Program Files\MATLAB\R2006a\install_dspic_r2006a\dspic\dspic_pic30_gcc.tmf is up to date
### Building dsPIC_33f_Explorer16: .\dsPIC_33f_Explorer16.bat
<wbr>
C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2006a  
<wbr>
C:\Program Files\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake" -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 ADD_MDL_NAME_TO_GLOBALS=1  
pic30-gcc  -c -mcpu=33fJ256GP710 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2006a/simulink/include -IC:\PROGRA~1\MATLAB\R2006a/extern/include -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2006a/rtw/c/src/ext_mode/common -IC:\PROGRA~1\MATLAB\R2006a\work\dsPIC_33f_Explorer16_dspic\sources -IC:\PROGRA~1\MATLAB\R2006a\work -IC:\PROGRA~1\MATLAB\R2006a\INSTAL~1\examples -IC:\PROGRA~1\MATLAB\R2006a\work -IC:\PROGRA~1\MATLAB\R2006a\work\DSPIC_~1\sources -IC:\PROGRA~1\MATLAB\R2006a\rtw\c\libsrc -IC:\PROGRA~1\MATLAB\R2006a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~3\include    dsPIC_33f_Explorer16_main.c 
dsPIC_33f_Explorer16_main.c: In function '_FICD': 
dsPIC_33f_Explorer16_main.c:39: error: syntax error before '{' token 
dsPIC_33f_Explorer16_main.c:45: error: syntax error before 'dsPIC_33f_Explorer16_SetEventsForThisBaseStep' 
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 0xff 
C30 Compiler found
C30 Compiler found</code></pre><br>
<br>
Thanks for the help!<br>
<br>
<br>
<br>
-Tina</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/249-dsPIC_33f_Explorer16.mdl">Pièce jointe : dsPIC_33f_Explorer16.mdl</a></p>
</article>

<article class="forum-post" id="p896">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-13 21:52 UTC">2009-07-13 21:52 UTC</time></header>
<h3>Re: Error</h3>
<div class="forum-post-body">Dear Tina,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : tnguyen</header><br>
In addition, I replaced my main C code file with your main C code file and I obtained the same error.  Was I suppose to do it another way?<br>
</blockquote><br>
This is no worth as the C code file you replace has just been replaced by the one generated by RTW Embedded Coder (i.e. Simulink). You could replace C code file IF you import all files generated in MPLAB and compile the project from MPLAB (see example on the wiki)<br>
<br>
Anyway, you may compare theses C files (using tools like winmerge). Btw, It seems that the problem comes from the compiler : <br>
<br>
<br>
<br>
Current version of C30 supported is 3.11. I get the following :<br>
<pre><code>&gt;&gt; !pic30-gcc -v
Using built-in specs. 
Target: pic30-coff 
Configured with: /home/build/builds/build_20080716/src/gcc-4.0.2/gcc-4.0.2/configure --target=pic30-coff --host=i386-mingw32 --build=i386-pc-linux --program-prefix=pic30-coff- --enable-languages=c 
Thread model: single 
gcc version 4.0.3 (dsPIC30, Microchip v3_11) Build date: Jul 16 2008 
Microchip Language Tool Shell Version v3_11 (Build date: Jul 16 2008). 
Copyright (c) 2006 Microchip Technology Inc. All rights reserved </code></pre><br>
Could you download the latest version of C30 ? I try to maintain compatibility only with the most recent compiler. Version of the C30 for student can be downloaded from the microchip website. Optimization of the generated code is limited to 30 days with theses versions, anyway, code is still working without theses optimisation. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p897">
<header><strong>tnguyen</strong><time datetime="2009-07-13 23:11 UTC">2009-07-13 23:11 UTC</time></header>
<h3>Re: Error</h3>
<div class="forum-post-body">Thanks so much!  It was the outdated C30 compiler. Thanks again.<br>
<br>
<br>
<br>
-Tina</div>
</article>

