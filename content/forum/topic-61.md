---
title: "Errors on testing the first examples in 0.94eb version..."
url: "/forum/topic/61/"
archiveKind: "topic"
---
# Errors on testing the first examples in 0.94eb version...

Forum : [bug reports](/forum/#forum-8)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p112">
<header><strong>just4you</strong><time datetime="2007-09-28 02:03 UTC">2007-09-28 02:03 UTC</time></header>
<div class="forum-post-body">Lubin, I've test the new version (0.94eb)<br>
<br>
<br>
<br>
1. character problems are fixed.<br>
<br>
   : Installation in korean windows and recognition in MATLAB 2007a are good.<br>
<br>
<br>
<br>
2. I've test some blocks.<br>
<br>
   - test a digital i/o block with my board, then works good.<br>
<br>
   - first example shows a error message.<br>
<br>
     the followings are the grabbed in my computer.<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'test_01'. MATLAB error message:
Error using ==&gt; RTW.genMakefileAndBuild at 967
Error(s) encountered while building model "test_01".
<wbr>
<wbr>
<wbr>
<wbr>
<wbr>
<wbr>
<wbr>
### Starting Real-Time Workshop build procedure for model: test_01
### Generating code into build directory: E:\Work\MATLAB\Test\test_01_dspic\sources
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
Number of I/O PINs used : 5
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
Number of I/O PINs used : 5
<wbr>
PLLPOST =
<wbr>
     0
<wbr>
<wbr>
PLLDIV =
<wbr>
    30
<wbr>
<wbr>
PLLPRE =
<wbr>
     0
<wbr>
<wbr>
fcyObtained =
<wbr>
    40000000
<wbr>
### Invoking Target Language Compiler on test_01.rtw
	tlc
	-r
	E:\Work\MATLAB\Test\test_01_dspic\sources\test_01.rtw
	E:\Work\MATLAB\dsPIC_RTW\dspic\dspic.tlc
	-OE:\Work\MATLAB\Test\test_01_dspic\sources
	-IE:\Work\MATLAB\dsPIC_RTW\dspic
	-IE:\Work\MATLAB\dsPIC_RTW\blocks
	-IE:\Work\MATLAB\Test\test_01_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2007a\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=0
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=1
	-aZeroExternalMemoryAtStartup=1
	-aInitFltsAndDblsToZero=1
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
	-aOPTIM_GCC="-mcpu=33FJ128GP706 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p33fj128gp706.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp33FJ128GP706-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-IC:\PROGRA~1\MICROC~1\MPLABC~1\include"
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
....
### Initial pass through model to cache user defined code
.
### Caching model source code
..............
### Writing main
.
### Writing header file test_01_types.h
### Writing header file test_01.h
.
### Writing source file test_01.c
### Writing header file test_01_private.h
### Writing source file test_01_data.c
.
### Writing header file autobuild.h
### Writing source file test_01_main.c
### TLC code generation complete.
### Creating HTML report file test_01_codegen_rpt.html
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
Embedded Coder for dsPIC V0.94eb(26-Sep-2007) for Matlab R2007a.
Licence Accorded to Demonstration Version - 
informations available at http://www.kerhuel.eu/
----------------------------------------------------
.
### Processing Template Makefile: E:\Work\MATLAB\dsPIC_RTW\dspic\dspic_pic30_gcc.tmf
### Creating test_01.mk from E:\Work\MATLAB\dsPIC_RTW\dspic\dspic_pic30_gcc.tmf
### Building test_01: .\test_01.bat
<wbr>
E:\Work\MATLAB\Test\test_01_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007a  
<wbr>
E:\Work\MATLAB\Test\test_01_dspic\sources&gt;"C:\Program Files\MATLAB\R2007a\rtw\bin\win32\gmake" -f test_01.mk  GENERATE_REPORT=1 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=33FJ128GP706 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\test_01_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    dsPIC_OutputCompare_Interrupt.c 
dsPIC_OutputCompare_Interrupt.c: In function '_OC1Interrupt': 
dsPIC_OutputCompare_Interrupt.c:7: warning:  PSV model not specified for '_OC1Interrupt'; 
   assuming 'auto_psv' this may affect latency 
pic30-gcc  -c -mcpu=33FJ128GP706 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\test_01_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    test_01_data.c 
pic30-gcc  -c -mcpu=33FJ128GP706 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\test_01_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    test_01_main.c 
test_01_main.c: In function 'main': 
test_01_main.c:64: warning: 'return' with a value, in function returning void 
test_01_main.c:51: warning: return type of 'main' is not 'int' 
pic30-gcc  -c -mcpu=33FJ128GP706 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\test_01_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    test_01.c 
test_01.c: In function 'test_01_initialize': 
test_01.c:127: warning: right shift count &gt;= width of type 
test_01.c:133: error: 'OC_TIMER4_SRC' undeclared (first use in this function) 
test_01.c:133: error: (Each undeclared identifier is reported only once 
test_01.c:133: error: for each function it appears in.) 
gmake: *** [test_01.o] Error 0xff 
### Real-Time Workshop build procedure for model: 'test_01' aborted due to an error.</code></pre></div>
</article>

<article class="forum-post" id="p113">
<header><strong>just4you</strong><time datetime="2007-09-28 02:23 UTC">2007-09-28 02:23 UTC</time></header>
<h3>Servo Sinus compilation results...</h3>
<div class="forum-post-body">Contrast with my model, the servos sinus examples in the packages compiled well.<br>
<br>
<br>
<br>
My target is 33FJ128GP706.<br>
<br>
<br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.
&gt; In general\private\openmdl at 13
  In open at 146
  In uiopen at 196
Warning: In instantiating linked block 'Servo_Sinus/Output Compare' : Output Capture Peripheral block (mask) does not have a parameter named 'NPORTS'.
&gt; In general\private\openmdl at 13
  In open at 146
  In uiopen at 196
### Starting Real-Time Workshop build procedure for model: Servo_Sinus
### Generating code into build directory: E:\Work\MATLAB\Test\Servo_Sinus_dspic\sources
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
Number of I/O PINs used : 1
### Invoking Target Language Compiler on Servo_Sinus.rtw
	tlc
	-r
	E:\Work\MATLAB\Test\Servo_Sinus_dspic\sources\Servo_Sinus.rtw
	E:\Work\MATLAB\dsPIC_RTW\dspic\dspic.tlc
	-OE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources
	-IE:\Work\MATLAB\dsPIC_RTW\dspic
	-IE:\Work\MATLAB\dsPIC_RTW\blocks
	-IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2007a\stateflow\c\tlc
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
	-aOPTIM_GCC="-mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-IC:\PROGRA~1\MICROC~1\MPLABC~1\include"
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
### Writing header file Servo_Sinus_types.h
.
### Writing header file Servo_Sinus.h
### Writing source file Servo_Sinus.c
### Writing header file Servo_Sinus_private.h
.
### Writing source file Servo_Sinus_data.c
### Writing header file autobuild.h
.
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
Embedded Coder for dsPIC V0.94eb(26-Sep-2007) for Matlab R2007a.
Licence Accorded to Demonstration Version - 
informations available at http://www.kerhuel.eu/
----------------------------------------------------
.
### Processing Template Makefile: E:\Work\MATLAB\dsPIC_RTW\dspic\dspic_pic30_gcc.tmf
### Creating Servo_Sinus.mk from E:\Work\MATLAB\dsPIC_RTW\dspic\dspic_pic30_gcc.tmf
### Building Servo_Sinus: .\Servo_Sinus.bat
<wbr>
E:\Work\MATLAB\Test\Servo_Sinus_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007a  
<wbr>
E:\Work\MATLAB\Test\Servo_Sinus_dspic\sources&gt;"C:\Program Files\MATLAB\R2007a\rtw\bin\win32\gmake" -f Servo_Sinus.mk  GENERATE_REPORT=0 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_Sinus_data.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_Sinus_main.c 
Servo_Sinus_main.c: In function 'main': 
Servo_Sinus_main.c:59: warning: 'return' with a value, in function returning void 
Servo_Sinus_main.c:49: warning: return type of 'main' is not 'int' 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    dsPIC_OutputCompare_Interrupt.c 
dsPIC_OutputCompare_Interrupt.c: In function '_OC1Interrupt': 
dsPIC_OutputCompare_Interrupt.c:7: warning:  PSV model not specified for '_OC1Interrupt'; 
   assuming 'auto_psv' this may affect latency 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_Sinus.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubcc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubcc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubrc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubrc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubrr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_backsubrr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_enab.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubcc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubcc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubcr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubcr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubrc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubrc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubrr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_forwardsubrr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_hypot.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_hypot32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_i32zcfcn.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look1d.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look1d32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look2d32_general.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look2d32_normal.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look2d_general.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look2d_normal.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_look32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_lu_cplx.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_lu_cplx_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_lu_real.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_lu_real_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivcc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivcc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivcr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivcr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivrc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivrc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivrr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matdivrr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandinccc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandinccc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandinccr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandinccr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandincrc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandincrc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandincrr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultandincrr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultcc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultcc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultcr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultcr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultrc_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultrc_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultrr_dbl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_matmultrr_sgl.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_nrand.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_int16.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_int32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_int8.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_uint16.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_uint32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_div_uint8.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_int16.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_int32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_int8.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_uint16.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_uint32.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_sat_prod_uint8.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_urand.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IE:\Work\MATLAB\Test\Servo_Sinus_dspic\sources -IE:\Work\MATLAB\Test -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc/rt_zcfcn.c 
"### Creating rtwlib.a "  
pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_hypot.o rt_hypot32.o rt_i32zcfcn.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_nrand.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o rt_urand.o rt_zcfcn.o  
"### rtwlib.a Created"  
pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld -o ..\../Servo_Sinus.coff  Servo_Sinus_data.o Servo_Sinus_main.o dsPIC_OutputCompare_Interrupt.o Servo_Sinus.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a 
C:\Program Files\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: mode pic30_coff 
Servo_Sinus_data.o 
Servo_Sinus_main.o 
dsPIC_OutputCompare_Interrupt.o 
Servo_Sinus.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a)crt1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a)crt0.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a)ConfigIntTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a)OpenTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a)OpenOC1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a)ConfigIntOC1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)sinf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)floorf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)futil.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)sincosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fchop.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)funpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)errno.o 
(C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a)fixsfsi.o 
<wbr>
<wbr>
Program Memory Usage 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.reset                           0                 0x4             0x6  (6) 
.ivt                           0x4                0x7c            0xba  (186) 
.aivt                         0x84                0x7c            0xba  (186) 
.text                        0x100               0x750           0xaf8  (2808) 
.dinit                       0x850                0x2c            0x42  (66) 
.isr                         0x87c                 0x2             0x3  (3) 
__FOSC                    0xf80000                 0x2             0x3  (3) 
__FWDT                    0xf80002                 0x2             0x3  (3) 
__FBORPOR                 0xf80004                 0x2             0x3  (3) 
__FGS                     0xf8000a                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):          0xcc3  (3267) 13% 
<wbr>
<wbr>
Data Memory Usage 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.ndata                       0x800                   0            0x12  (18) 
.nbss                        0x812                   0             0x6  (6) 
.nbss                        0x818                   0             0x4  (4) 
.nbss                        0x81c                   0             0x2  (2) 
.nbss                        0x81e                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):           0x20  (32) 1% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                        0x820                               0x7e0  (2016) 
<wbr>
                        Maximum dynamic memory (bytes):          0x7e0  (2016) 
<wbr>
"*** Created "executable": ..\../Servo_Sinus.coff"  
pic30-coff-bin2hex ..\../Servo_Sinus.coff  
### Successful completion of Real-Time Workshop build procedure for model: Servo_Sinus</code></pre></div>
</article>

<article class="forum-post" id="p115">
<header><strong>LubinKerhuel</strong><time datetime="2007-09-28 07:00 UTC">2007-09-28 07:00 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
Could you provide me with the mdl file that does not compile ?<br>
<br>
<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p116">
<header><strong>LubinKerhuel</strong><time datetime="2007-09-29 12:32 UTC">2007-09-29 12:32 UTC</time></header>
<div class="forum-post-body">I find the bug; While I correct it, you could avoid it by setting the auto configuration of the timer4 and above to off by setting to 0 at :  <br>
<br>
<br>
<br>
dsPIC MASTER block dialog box<br>
<br>
tab : Real Time - Quartz<br>
<br>
Config Timer [2 3 4 ...]<br>
<br>
<br>
<br>
The value should look like this: [-1 -1 0 0 ...] <br>
<br>
The number of zero depends on the number of independent timer of the PIC.</div>
</article>

<article class="forum-post" id="p117">
<header><strong>just4you</strong><time datetime="2007-10-01 00:58 UTC">2007-10-01 00:58 UTC</time></header>
<h3>[-1 -1 0 0] means Timer4 off ?</h3>
<div class="forum-post-body">[-1 -1 0 0] means timer 3, 4 off, is it?<br>
<br>
<br>
<br>
Timer 4 is the source of OC1 block with dsPIC33FJ128GP706.<br>
<br>
hmm.. I think it's not a good configuration.<br>
<br>
<br>
<br>
I'll send my test model file to you by e-mail....<br>
<br>
<br>
<br>
<br>
<br>
P.S &gt;  I hope I can upload a file in the forum site..</div>
</article>

<article class="forum-post" id="p119">
<header><strong>LubinKerhuel</strong><time datetime="2007-10-06 12:31 UTC">2007-10-06 12:31 UTC</time></header>
<h3>OC and IC will not be assigned to Timer 4 or above !</h3>
<div class="forum-post-body">Very nice bug!<br>
<br>
<br>
<br>
Timers are assigned automatically to get the best result (using my criterion!)<br>
<br>
Unfortunately, Input Capture and Output Compare could only be assigned to Timer 2 or to Timer 3.<br>
<br>
The optimization algorithm that set timer's prescaler and assign Timer did not take into account this constraint and sometimes IC or OC peripheral were assigned to a Timer above 3 ( 4 or 5 for example)<br>
<br>
<br>
<br>
With the version 0.95a of the toolbox, <br>
<br>
The bug is corrected! The optimization algorithm takes into account this constraint and IC and OC could only be assigned to Timer 2 or Timer 3!<br>
<br>
<br>
<br>
Download the last version : <br>
<br>
<a href="/RTWdsPIC/download.html">http://www.kerhuel.eu/RTWdsPIC/download.html</a></div>
</article>

<article class="forum-post" id="p138">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-15 13:03 UTC">2007-12-15 13:03 UTC</time></header>
<h3>Re: Errors on testing the first examples in 0.94eb version...</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : just4you</header>P.S &gt; I hope I can upload a file in the forum site..</blockquote><br>
<br>
It is now possible to upload files on the forum !<br>
<br>
 :D</div>
</article>

