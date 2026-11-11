---
title: "Build error"
url: "/forum/topic/160/"
archiveKind: "topic"
---
# Build error

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p524">
<header><strong>barryforever</strong><time datetime="2008-09-22 06:43 UTC">2008-09-22 06:43 UTC</time></header>
<div class="forum-post-body">I get this error when trying to build the block..<br>
<br>
can you tell me what i have to do..<br>
<br>
Im running a Matlab r2008a and Mplab8.01 <br>
<br>
running a c30 compliler student version 2.05<br>
<pre><code>C30 Compiler found
P
T
C30 Compiler found
C30 Compiler found
Model configured...
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
Number of I/O PINs used : 1
T
P
Number of I/O PINs used : 1
T
C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: let
### Generating code into build directory: C:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources
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
Warning: Output port 1 of 'let/Digital Output Write' is not connected.
### Invoking Target Language Compiler on let.rtw
	tlc
	-r
	C:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources\let.rtw
	C:\Documents and Settings\Barry\My Documents\MATLAB\dspic\dspic.tlc
	-OC:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources
	-IC:\Documents and Settings\Barry\My Documents\MATLAB\dspic
	-IC:\Documents and Settings\Barry\My Documents\MATLAB\blocks
	-IC:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources\tlc
	-ID:\MATLAB\R2008a\rtw\c\tlc\mw
	-ID:\MATLAB\R2008a\rtw\c\tlc\lib
	-ID:\MATLAB\R2008a\rtw\c\tlc\blocks
	-ID:\MATLAB\R2008a\rtw\c\tlc\fixpt
	-ID:\MATLAB\R2008a\stateflow\c\tlc
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
	-aGMAKE_PLACE="D:\MATLAB\R2008a\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2 -fno-short-double"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4013.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4013-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="30f4013"
	-aGCCPATH=""
	-aGenerateTraceInfo=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
.....
### Initial pass through model to cache user defined code
### Caching model source code
............
### Writing main
### Writing header file let_types.h
.
### Writing header file let.h
### Writing source file let.c
.
### Writing header file let_private.h
### Writing source file let_data.c
### Writing header file autobuild.h
.
### Writing source file let_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V0.98fe(16-Sep-2008) for Matlab R2008a.
<wbr>
<wbr>
Licence Accorded to  Demo
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://www.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRENE : 503 920 456
<wbr>
 Facturation to :    
<wbr>
                     WEBSITE : http://www.kerhuel.eu
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  http://www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Documents and Settings\Barry\My Documents\MATLAB\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;D:\MATLAB\R2008a\bin\win32\gmake&gt;
### in default batch file
### Creating let.mk from C:\Documents and Settings\Barry\My Documents\MATLAB\dspic\dspic_pic30_gcc.tmf
### Building let: .\let.bat
<wbr>
C:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources&gt;set MATLAB=D:\MATLAB\R2008a  
<wbr>
C:\Documents and Settings\Barry\My Documents\MATLAB\let_dspic\sources&gt;D:\MATLAB\R2008a\bin\win32\gmake -f let.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2008a/simulink/include -ID:\MATLAB\R2008a/extern/include -ID:\MATLAB\R2008a/rtw/c/src -ID:\MATLAB\R2008a/rtw/c/ert -ID:\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB\LET_DS~1\sources -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB -ID:\MATLAB\R2008a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    let_data.c 
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2008a/simulink/include -ID:\MATLAB\R2008a/extern/include -ID:\MATLAB\R2008a/rtw/c/src -ID:\MATLAB\R2008a/rtw/c/ert -ID:\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB\LET_DS~1\sources -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB -ID:\MATLAB\R2008a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    let_main.c 
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2008a/simulink/include -ID:\MATLAB\R2008a/extern/include -ID:\MATLAB\R2008a/rtw/c/src -ID:\MATLAB\R2008a/rtw/c/ert -ID:\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB\LET_DS~1\sources -IC:\DOCUME~1\Barry\MYDOCU~1\MATLAB -ID:\MATLAB\R2008a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    let.c 
''pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4013.gld -o ..\../let.coff  let_data.o let_main.o let.o      C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4013-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Program Files\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4013.gld: No such file or directory 
gmake: *** [..\../let.coff] Error 255 
### Real-Time Workshop build procedure for model: 'let' aborted due to an error.
C30 Compiler found
C30 Compiler found</code></pre></div>
</article>

<article class="forum-post" id="p525">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-22 21:54 UTC">2008-09-22 21:54 UTC</time></header>
<h3>Re: Build error</h3>
<div class="forum-post-body">You must update your C30 compiler to version (3.10b or 3.11b) (student version is also Ok)<br>
<br>
See requirements <a href="/wiki/download/">http://www.kerhuel.eu/wiki/Download#Requirement</a><br>
<br>
<br>
<br>
Lubin</div>
</article>

