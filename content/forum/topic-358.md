---
title: "error compilation"
url: "/forum/topic/358/"
archiveKind: "topic"
---
# error compilation

Forum : [bug reports](/forum/#forum-8)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1468">
<header><strong>ELMAY</strong><time datetime="2011-02-18 01:22 UTC">2011-02-18 01:22 UTC</time></header>
<div class="forum-post-body">bonjour<br>
<br>
je test un model .mdl    pwm    mais il apparait une erreur<br>
<br>
<br>
<br>
svp est ce que vous pouvez m`aider<br>
<br>
merci d*avance</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/381-pwm.mdl">Pièce jointe : pwm.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/382-Doc1.docx">Pièce jointe : Doc1.docx</a></p>
</article>

<article class="forum-post" id="p1469">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-18 09:12 UTC">2011-02-18 09:12 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Hi Elmay,<br>
<br>
<br>
<br>
Unexpected problem, easily solved however !<br>
<br>
<br>
<br>
It happens that your model name pwm.mdl generates C code files with the same name (i.e. <strong>pwm.c </strong>and <strong>pwm.h</strong>). But the model must include another files which is <strong>pwm.h</strong> from the microchip library. Here, the generated file <strong>pwm.h</strong> shadows the microchip library file <strong>pwm.h</strong>.<br>
<br>
<br>
<br>
Workaround: <br>
<br>
Rename your simulink file into pwm_test.mdl for example. Compilation is then Ok.<br>
<br>
<br>
<br>
Others ticks : a model time step of 1/100000 which is 1us is pretty fast for the microcontroller ! You should try with a 1ms or 250us time step for example ! This time step has no effects on the max PWM frequency you can achieved.<br>
<br>
<br>
<br>
I am also not certain that PWM blocks is configured as you expected it.<br>
<br>
Here, the period id set to (1000/PWM*0.41943) with PWM = 65534 thus you'll get a period of 6.4ms and duty cycle (500/1000 = 50%) of 3.2ms.<br>
<br>
<br>
<br>
Please try to copy/past from the matlab workspace the errors you obtain using the forum Code function. Try to add to the model you posted a screenshot of it. It may help other users and I may respond faster.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1471">
<header><strong>ELMAY</strong><time datetime="2011-02-21 10:09 UTC">2011-02-21 10:09 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I make changes on this model but still error appears<br>
<br>
thank you</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/384-pwm_test.mdl">Pièce jointe : pwm_test.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/385-matlab%20workspace%20%20errors.doc">Pièce jointe : matlab workspace  errors.doc</a></p>
</article>

<article class="forum-post" id="p1472">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-21 11:51 UTC">2011-02-21 11:51 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Working version attached.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : LubinKerhuel</header>Please try to copy/past from the matlab workspace the errors you obtain using the forum Code function. Try to add to the model you posted a screenshot of it. It may help other users and I may respond faster.</blockquote><br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/386-pwm_test.mdl">Pièce jointe : pwm_test.mdl</a></p>
</article>

<article class="forum-post" id="p1477">
<header><strong>ELMAY</strong><time datetime="2011-02-23 10:26 UTC">2011-02-23 10:26 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body"><pre><code>Model configured...
### Starting Real-Time Workshop build procedure for model: pwm_test
### Generating code into build directory: D:\Documents and Settings\ELMAY\Bureau\pwm_test_dspic\sources
PTPTPNumber of I/O PINs used : 0
TPNumber of I/O PINs used : 0
TTPTPTTTWarning: Could not find an exact (case-sensitive) match for 'dsPIC_PWM_Motor_callback_InitMask'.
D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks\dsPIC_PWM_motor_callback_InitMask.p is a
case-insensitive match and will be used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
TPTPNumber of I/O PINs used : 0
TPTTPTPTT### Invoking Target Language Compiler on pwm_test.rtw
	tlc
	-r
	D:\Documents and Settings\ELMAY\Bureau\pwm_test_dspic\sources\pwm_test.rtw
	D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic.tlc
	-OD:\Documents and Settings\ELMAY\Bureau\pwm_test_dspic\sources
	-ID:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic
	-ID:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\blocks
	-ID:\Documents and Settings\ELMAY\Bureau\pwm_test_dspic\sources\tlc
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\mw
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\lib
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\blocks
	-ID:\Program Files\MATLAB\R2009b\rtw\c\tlc\fixpt
	-ID:\Program Files\MATLAB\R2009b\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=1
	-aInlineParameters=0
	-aLocalBlockOutputs=0
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=1
	-aZeroExternalMemoryAtStartup=1
	-aInitFltsAndDblsToZero=1
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
	-aTargetFcnLib="ansi_tfl_tmw.mat"
	-aGenFloatMathFcnCalls="ANSI_C"
	-aIsPILTarget=0
	-aIncludeMdlTerminateFcn=0
	-aCombineOutputUpdateFcns=1
	-aSuppressErrorStatus=0
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
	-aExtMode=1
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
	-aOPTIM_GCC="-mcpu=30f3010 -O3 -fschedule-insns -fschedule-insns2 -merrata=exch -mlarge-data"
	-aLDFLAGS=" -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref"
	-aLDPICTYPE=" -Xlinker --script=D:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f3010.gld"
	-aLDLIBPIC=" D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a"
	-aPIC_INCLUDES=" -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include"
	-aPIC_REF="30f3010"
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
...................
### Writing main
.
### Writing header file pwm_test_types.h
### Writing header file pwm_test.h
.
### Writing source file pwm_test.c
### Writing header file pwm_test_private.h
### Writing source file pwm_test_data.c
.
### Writing header file autobuild.h
### Writing source file pwm_test_main.c
### TLC code generation complete.
### Generating TLC interface API.
.
### Creating data type transition file pwm_test_dt.h
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
                     WEBSITE : http://archive.kerhuel.eu/wiki
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
Check updates and new informations at :  archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating pwm_test.mk from D:\Documents and Settings\ELMAY\Mes documents\Downloads\DSPIC_DOC\dspic\dspic\dspic_pic30_gcc.tmf
### Building pwm_test: "D:\PROGRA~1\MATLAB\R2009b\bin\win32\gmake" -f pwm_test.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=30f3010 -O3 -fschedule-insns -fschedule-insns2 -merrata=exch -mlarge-data	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\pwm_test_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau -ID:\DOCUME~1\ELMAY\Bureau\Simulink_PWM   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    pwm_test_data.c 
''pic30-gcc  -c -mcpu=30f3010 -O3 -fschedule-insns -fschedule-insns2 -merrata=exch -mlarge-data	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\pwm_test_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau -ID:\DOCUME~1\ELMAY\Bureau\Simulink_PWM   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    pwm_test_main.c 
''pic30-gcc  -c -mcpu=30f3010 -O3 -fschedule-insns -fschedule-insns2 -merrata=exch -mlarge-data	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2009b/simulink/include -ID:\PROGRA~1\MATLAB\R2009b/extern/include -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2009b/rtw/c/src/ext_mode/common -ID:\DOCUME~1\ELMAY\Bureau\pwm_test_dspic\sources -ID:\DOCUME~1\ELMAY\Bureau -ID:\DOCUME~1\ELMAY\Bureau\Simulink_PWM   -I D:\PROGRA~1\MICROC~1\mplabc30\v3.25\include    pwm_test.c 
''pic30-gcc   -mcpu=30f3010  pwm_test_data.o pwm_test_main.o pwm_test.o      D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a -o ..\../pwm_test.cof -Xlinker --script=D:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f3010.gld -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref 
d:\program files\microchip\mplabc30\v3.25\bin\bin\..\bin/pic30-coff-ld.exe: mode pic30_coff 
pwm_test_data.o 
pwm_test_main.o 
pwm_test.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)crt0_standard.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)data_init_standard.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a)ConfigIntTimer1.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a)SetDCMCPWM.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a)ConfigIntMCPWM.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3010-coff.a)OpenMCPWM.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)memset.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)puts.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)fputc.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)stdclean.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)fseek.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)fflush.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)flsbuf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)fclose.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)buf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)tfiles.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)errno.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fne.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)addsf3.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)mulsf3.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fgtge.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)floatsisf.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fcompare.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack2.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)futil.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fpack.o 
(D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)lseek.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)write.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)close.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)remove.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)sbrk.o 
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-[img][code]</code></pre>[/img]coff.a)c30_uart.o <br>
<br>
(d:/program files/microchip/mplabc30/v3.25/bin/bin/../../lib\libpic30-coff.a)brk.o <br>
<br>
stdclean.o: Link Error: Could not allocate section .bss, size = 1026 bytes, attributes = bss  <br>
<br>
 Link Error: Could not allocate data memory <br>
<br>
gmake: *** [..\../pwm_test.cof] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'pwm_test' aborted due to an error.</div>
</article>

<article class="forum-post" id="p1478">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-23 11:09 UTC">2011-02-23 11:09 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Could you test with the model I uploaded on the forum ?</div>
</article>

