---
title: "MPLAB Compilation"
url: "/forum/topic/369/"
archiveKind: "topic"
---
# MPLAB Compilation

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1498">
<header><strong>ELMAY</strong><time datetime="2011-03-05 13:12 UTC">2011-03-05 13:12 UTC</time></header>
<div class="forum-post-body">[/img]<span style="color:#ff4000">  hello Sir<br>
<br>
I am a program SIMULINK / BlockSet and it works in MATLAB<br>
<br>
but while running under MPLAB m'apparair following error:<br>
<br>
<span style="color:#bfff40">Failed to import Generated Files. Check the Build Window to know the Status of Build</span></span><br>
<br>
[/b][/size]<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;Opening Matlab session and model 'D:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH.mdl'
Please wait...
Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\execBatch.p is a case-insensitive match and will be used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases.
&gt; In D:\Program Files\MATLAB\R2009b\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 77
  In &lt;a href="matlab: opentoline('D:\Program Files\MATLAB\R2009b\toolbox\rtw\rtw\rtwprivate.m',12,1)"&gt;rtwprivate at 12&lt;/a&gt;
  In &lt;a href="matlab: opentoline('D:\Program Files\MATLAB\R2009b\toolbox\rtw\rtw\stf4target.m',34,1)"&gt;stf4target at 34&lt;/a&gt;
  In &lt;a href="matlab: opentoline('D:\Program Files\MATLAB\R2009b\toolbox\rtw\rtw\stf2target.m',61,1)"&gt;stf2target at 61&lt;/a&gt;
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: GMAKE_PLACE not defined, check tlc target
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 407
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
PWarning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 74
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 132
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 149
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 231
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 261
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 281
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 283
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral  &lt;========= ---
&gt; In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;setTypePort at 521
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 300
  In D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: SubSystem block (mask) does not have a parameter named 'T1CSL'.
&gt; In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. SubSystem block (mask) does not have a parameter named 'T1CSL'.
&gt; In &lt;a href="matlab: opentoline('D:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m',14,1)"&gt;MplabOpenModel at 14&lt;/a&gt;
PTodel at 14&lt;/a&gt;
Warning: SubSystem block (mask) does not
Succesfully Opened The Model
<wbr>
Generating files for Simulink model 'D:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH.mdl'. This may take a few minutes. 
Please wait...### Starting Real-Time Workshop build procedure for model: MPH
### Generating code into build directory: D:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH_dspic\sources
PTPNumber of I/O PINs used : 1
TPTPTTPNumber of I/O PINs used : 1
TPNumber of I/O PINs used : 1
TTTTPTPTPTTPNumber of I/O PINs used : 1
TPTTWarning: Source 'MPH/Subsystem/Sine Wave1' specifies that its sample time (-1) is back-inherited. You should explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box.
### Invoking Target Language Compiler on MPH.rtw
	tlc
	-r
	D:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH_dspic\sources\MPH.rtw
	D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic.tlc
	-OD:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH_dspic\sources
	-ID:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic
	-ID:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks
	-ID:\Documents and Settings\ELMAY\Bureau\DRAFT\MPH_dspic\sources\tlc
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\mw
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\lib
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\blocks
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\fixpt
	-ID:\Program Files\MATLAB\R2009b\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=0
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=1
	-aZeroExternalMemoryAtStartup=1
	-aInitFltsAndDblsToZero=0
	-aForceBlockIOInitOptimize=0
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
	-aIgnoreTestpoints=0
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
	-aGMAKE_PLACE="D:\PROGRA~1\MATLAB\R2009b\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS=" -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref"
	-aLDPICTYPE=" -Xlinker --script=D:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f4013.gld"
	-aLDLIBPIC=" D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f4013-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a"
	-aPIC_INCLUDES=" -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include"
	-aPIC_REF="30f4013"
	-aGCCPATH=""
	-aGenerateTraceInfo=0
	-aIgnoreTestpoints=0
	-aProtectedModelReferenceTarget=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
.....
### Initial pass through model to cache user defined code
.
### Caching model source code
.......................
### Writing main
.
### Writing header file MPH_types.h
### Writing header file MPH.h
.
### Writing source file MPH.c
### Writing header file MPH_private.h
### Writing source file MPH_data.c
.
### Writing header file autobuild.h
### Writing source file MPH_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.4b(14-Jan-2011) for Matlab R2009b.
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
Check updates and new informations at : &lt;a href = "http://archive.kerhuel.eu/wiki/index.php5#3"&gt; www.kerhuel.eu &lt;/a&gt;
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### MPH.mk which is generated from D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic_pic30_gcc.tmf is up to date
### Building MPH: "D:\PROGRA~1\MATLAB\R2009b\bin\win32\gmake" -f MPH.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\DRAFT\MPH_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau\DRAFT   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    MPH_data.c 
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\DRAFT\MPH_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau\DRAFT   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    MPH_main.c 
''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\DRAFT\MPH_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau\DRAFT   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    MPH.c 
''pic30-gcc   -mcpu=30f4013  MPH_data.o MPH_main.o MPH.o      D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f4013-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a -o ..\../MPH.cof -Xlinker --script=D:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f4013.gld -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref 
d:\program files\microchip\mplabc30\v3.25\bin\bin\..\bin/pic30-coff-ld.exe: mode pic30_coff 
MPH_data.o 
MPH_main.o 
MPH.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)crt0_standard.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)data_init_standard.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f4013-coff.a)ConfigIntTimer1.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)floatsisf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)addsf3.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)mulsf3.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)sinf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)cosf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fgtge.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fpack.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack2.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)futil.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)sincosf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fcompare.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)errno.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)feqltle.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fmodf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fixsfsi.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fmodrem.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x100, Length = 0x7f00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x100               0x4d6           0x741  (1857) 
.text                        0x5d6               0x31e           0x4ad  (1197) 
.dinit                       0x8f4                0x68            0x9c  (156) 
.text                        0x95c                0x14            0x1e  (30) 
.isr                         0x970                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):          0xcab  (3243) 6% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x800] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.ndata                       0x800                   0            0x70  (112) 
.nbss                        0x870                   0            0x18  (24) 
.ndata                       0x888                   0             0x2  (2) 
.nbss                        0x88a                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):           0x8c  (140) 6% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                        0x88c                               0x774  (1908) 
<wbr>
                        Maximum dynamic memory (bytes):          0x774  (1908) 
<wbr>
" ================================================================" 
"*** Embedded Target for dsPIC by Lubin KERHUEL - http://www.kerhuel.eu" 
" | Licence Accorded to Demonstration Version                    |" 
" |                     [adresse e-mail retirée]                      |"	     
" |          Companie : Author : Lubin KERHUEL                   |"  
" |                     WEBSITE : http://www.kerhuel.eu/wiki     |" 
" |                                                              |" 		 
" |                     SIRENE : 503 920 456                     |" 
" |                     SIRET : 503 920 456 00012                |"		 		 
" | Financial Service : Demo                                     |" 
" | Contact             Demo                                     |" 
" |                     Lubin KERHUEL                            |" 
" |                     1, rue Alfred Fredet                     |" 
" |                     38100 Grenoble                           |" 
" |                     FRANCE                                   |" 
" | Version 3.4b                              14-Jan-2011        |" 
" | For Matlab 7.9             R2009b                            |" 
" ================================================================"		  
"*** Created "executable": ..\../MPH.cof"	 
''pic30-bin2hex ..\../MPH.cof  
"*** Created "executable": ..\../MPH.hex"	 
. 
"***Ready to be downloaded into 30f4013. (with MPLAB: file -&gt; import, choose MPH.hex)"		 
"***alternative: load the project and re-compile it in MPLAB IDE"	 
### Successful completion of Real-Time Workshop build procedure for model: MPH
 | For Matlab 7.9             R2009b                            |" 
" ================================================================"		  
"*** Created "executable": ..\../MPH.cof"	 
''pic30-bin2hex ..\../MPH.cof  
"*** Created "executable": ..\../MPH.hex"	 
. 
"***Ready to be downloaded into 30f4013. (wi
BUILD EXECUTION COMMAND COMPLETED
<wbr>
<wbr>
Load Main Project (or) Set Main Project as Active Project
<wbr>
Failed to import Generated Files. Check the Build Window to know the Status of Build
</code></pre></div>
</article>

<article class="forum-post" id="p1499">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-05 17:43 UTC">2011-03-05 17:43 UTC</time></header>
<h3>Re: MPLAB Compilation</h3>
<div class="forum-post-body">First, please <a href="/wiki/download/">download</a> the latest blockset version available on the wiki.<br>
<br>
<br>
<br>
Then, do not use the MPLAB Matlab menu.<br>
<br>
Just open your model within matlab, compile it.<br>
<br>
If you want to open the generated C code within MPLAB, just open the mplab project file that is generated within Matlab. (instruction are givens at end of compilation process with the <a href="/wiki/download/">latest blockset version</a> !)<br>
<br>
<br>
<br>
That's it !<br>
<br>
Please let me know if you make it !<br>
<br>
<br>
<br>
Lubin</div>
</article>

