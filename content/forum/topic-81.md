---
title: "Matlab: Error while building model"
url: "/forum/topic/81/"
archiveKind: "topic"
---
# Matlab: Error while building model

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p173">
<header><strong>johan.b</strong><time datetime="2008-01-31 07:50 UTC">2008-01-31 07:50 UTC</time></header>
<div class="forum-post-body">Hello all, <br>
<br>
I discovered this blockset and it seems really interessant for my field of activity. I donwloaded files for Matlab R2007b and I followed the instructions of installation. <br>
<br>
I downloaded the student version of MPLAB C30 and I tried to build my own model: but it was an error during the build:<br>
<br>
<br>
<br>
<strong>Error building Real-Time Workshop target for block diagram 'Servo_ADC'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "Servo_ADC".</strong><br>
<br>
<br>
<br>
 Then I tried to find the source of error ... without success !<br>
<br>
Finally I tried with the sample file Servo_ADC.mdl and I have the same error. <br>
<br>
<br>
<br>
Maybe somebody can help me. You can find below for the detailed description of error. Thanks in advance. <br>
<br>
<br>
<br>
****MATLAB OUTPUT - BEGIN****<br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'.
Error using ==&gt; dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC Real Time workshop
(Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: In instantiating linked block 'Servo_ADC/ADC Input' : Invalid setting
in dsPIC : ADC10 block (mask) 'ADC Input' for parameter 'OutFormatBitspopup'.
&gt; In C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\blocks\dsPIC_PWM_OC_callback.p&gt;dsPIC_PWM_OC_callback at 94
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Number of I/O PINs used : 2
Number of I/O PINs used : 2
### Starting Real-Time Workshop build procedure for model: Servo_ADC
### Generating code into build directory: C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources
Number of I/O PINs used : 2
Number of I/O PINs used : 2
Number of I/O PINs used : 2
Warning: Source 'Servo_ADC/ADC Input' specifies that its sample time (-1) is
back-inherited. You should explicitly specify the sample time of sources. You
can disable this diagnostic by setting the 'Source block specifies -1 sample
time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of
the Configuration Parameters dialog box.
### Invoking Target Language Compiler on Servo_ADC.rtw
	tlc
	-r
	C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources\Servo_ADC.rtw
	C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\dspic\dspic.tlc
	-OC:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources
	-IC:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\dspic
	-IC:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\blocks
	-IC:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources\tlc
	-IC:\MATLAB_R2007b\rtw\c\tlc\mw
	-IC:\MATLAB_R2007b\rtw\c\tlc\lib
	-IC:\MATLAB_R2007b\rtw\c\tlc\blocks
	-IC:\MATLAB_R2007b\rtw\c\tlc\fixpt
	-IC:\MATLAB_R2007b\stateflow\c\tlc
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
	-aGMAKE_PLACE="C:\MATLAB~1\bin\win32\gmake"
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
### Evaluating PostCodeGenCommand specified in the model
<wbr>
Companie =
<wbr>
     ''
<wbr>
<wbr>
<wbr>
----------------------------------------------------
Embedded Coder for dsPIC V0.95b(09-Dec-2007) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
informations available at http://archive.kerhuel.eu/
----------------------------------------------------
.
### Processing Template Makefile: C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\MATLAB~1\bin\win32\gmake&gt;
### in default batch file
### Creating Servo_ADC.mk from C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\dspic\dspic_pic30_gcc.tmf
### Building Servo_ADC: .\Servo_ADC.bat
<wbr>
C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources&gt;set MATLAB=C:\MATLAB_R2007b  
<wbr>
C:\Documents and Settings\Johan.INSPIRON\Mes documents\MATLAB\install_dsPIC_R2007b\examples\Servo_ADC_dspic\sources&gt;C:\MATLAB~1\bin\win32\gmake -f Servo_ADC.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\MATLAB~1/simulink/include -IC:\MATLAB~1/extern/include -IC:\MATLAB~1/rtw/c/src -IC:\MATLAB~1/rtw/c/ert -IC:\MATLAB~1/rtw/c/src/ext_mode/common -IC:\DOCUME~1\JOHAN~1.INS\MESDOC~1\MATLAB\INSTAL~1\examples\SERVO_~1\sources -IC:\DOCUME~1\JOHAN~1.INS\MESDOC~1\MATLAB\INSTAL~1\examples -IC:\MATLAB~1\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    Servo_ADC_data.c 
pic30-gcc  -c -mcpu=30F3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\MATLAB~1/simulink/include 
[color=#0000FF][Removed Part ...][/color]
-IC:\MATLAB~1/extern/include -IC:\MATLAB~1/rtw/c/src -IC:\MATLAB~1/rtw/c/ert -IC:\MATLAB~1/rtw/c/src/ext_mode/common -IC:\DOCUME~1\JOHAN~1.INS\MESDOC~1\MATLAB\INSTAL~1\examples\SERVO_~1\sources -IC:\DOCUME~1\JOHAN~1.INS\MESDOC~1\MATLAB\INSTAL~1\examples -IC:\MATLAB~1\rtw\c\libsrc   -IC:\PROGRA~1\MICROC~1\MPLABC~1\include    C:\MATLAB~1\rtw\c\libsrc/rt_sat_prod_uint8.c 
"### Creating rtwlib.a " 
pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  
"### rtwlib.a Created" 
pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld -o ..\../Servo_ADC.coff  Servo_ADC_data.o Servo_ADC_main.o dsPIC_OutputCompare_Interrupt.o Servo_ADC.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libp30F3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a 
C:\Program Files\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld: No such file or directory 
gmake: *** [..\../Servo_ADC.coff] Error 255 
### Real-Time Workshop build procedure for model: 'Servo_ADC' aborted due to an error.
&gt;&gt; </code></pre><br>
****MATLAB OUTPUT - END****</div>
</article>

<article class="forum-post" id="p174">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-31 08:15 UTC">2008-01-31 08:15 UTC</time></header>
<h3>Re: Matlab: Error while building model</h3>
<div class="forum-post-body">H Johan,<br>
<br>
<br>
<br>
It seems it is the same problem : have a look on the following topic<br>
<br>
<br>
<br>
sumedhk get similar error : a missing gld file was reported. could you try the solution explained on the topic : <a href="/forum/topic/73/">Issues in dsPIC 30f6014 compiling : Missing gld &amp; DCI Periph</a>  :<br>
<br>
<br>
<br>
Ant let me know if  you still get the error.</div>
</article>

<article class="forum-post" id="p175">
<header><strong>johan.b</strong><time datetime="2008-01-31 08:49 UTC">2008-01-31 08:49 UTC</time></header>
<h3>Re: Matlab: Error while building model</h3>
<div class="forum-post-body">Ok and thank you for your answer. I will try this solution on my model and I shall let you know if it works. <br>
<br>
Thanks.</div>
</article>

<article class="forum-post" id="p176">
<header><strong>johan.b</strong><time datetime="2008-01-31 17:29 UTC">2008-01-31 17:29 UTC</time></header>
<h3>Re: Matlab: Error while building model</h3>
<div class="forum-post-body">I've just tried your solution and it seems to work properly. Many thanks !</div>
</article>

