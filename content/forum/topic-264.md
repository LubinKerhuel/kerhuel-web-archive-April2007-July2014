---
title: "Build error in function rt_MatMultAndIncCC_Dbl"
url: "/forum/topic/264/"
archiveKind: "topic"
---
# Build error in function rt_MatMultAndIncCC_Dbl

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

26 message(s) · archive en lecture seule

<article class="forum-post" id="p1025">
<header><strong>roel</strong><time datetime="2010-01-14 23:53 UTC">2010-01-14 23:53 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I was trying to build the example MDLs from your toolbox but got the same error everytime.<br>
<br>
Even when I use an empty MDL with just the master block in I get it.<br>
<br>
<br>
<br>
Here the last part of my screendump describing the problem:<br>
<br>
<br>
<pre><code>### Processing Template Makefile: D:\microchip\MatlabSimulink\dspic\dspic_pic30_gcc.tmf
### Creating untitled.mk from D:\microchip\MatlabSimulink\dspic\dspic_pic30_gcc.tmf
### Building untitled: .\untitled.bat
<wbr>
D:\microchip\MatlabSimulink\projects\1. testbuild\untitled_dspic\sources&gt;set MATLAB=D:\MATLAB\R2007b  
<wbr>
D:\microchip\MatlabSimulink\projects\1. testbuild\untitled_dspic\sources&gt;"D:\MATLAB\R2007b\bin\win32\gmake" -f untitled.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES\UNTITL~1\sources -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\MICROC~1\MPLABC~2\include    untitled_main.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES\UNTITL~1\sources -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\MICROC~1\MPLABC~2\include    untitled.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES\UNTITL~1\sources -ID:\MICROC~1\MATLAB~1\projects\1074C~1.TES -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\MICROC~1\MPLABC~2\include    D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c: In function 'rt_MatMultAndIncCC_Dbl': 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c:54: error: unrecognizable insn: 
(0x00f5a7f8) (insn 233 75 76 6 (set (reg:SF 2 w2 [ A2_val$im ]) 
        (mem/s/j:SF (plus:P16APSV (reg/v/f:P16APSV 14 w14 [orig:57 A2 ] [57]) 
                (const_int 4 [0x4])) [0 &lt;variable&gt;.im+0 S4 A16])) -1 (nil) 
    (nil)) 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c:54: internal compiler error: in extract_insn, at recog.c:2020 
Please submit a full bug report, 
with preprocessed source if appropriate. 
See &lt;URL:http://support.microchip.com&gt; for instructions. 
gmake: *** [rt_matmultandinccc_dbl.o] Error 255 
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.
======================================================================
= C30 directory not found ============================================
======================================================================
======================================================================
======================================================================
Enter C30 compiler directory (like C:\Program Files\Microchip\MPLAB C30
 (You have to do it twice, copy-past)
 ----&gt;C:\Microchipv830\MPLAB C30
C30 Compiler found
C30 Compiler found</code></pre><br>
<br>
Seems that the build proces is missing some standard Simulink RTW information.<br>
<br>
I am using a fresh Matlab R2007b installation + RTW and embedded coder + C30ComboLite_v3_22 + blockset v201<br>
<br>
<br>
<br>
I get the following from my workspace:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;&gt;&gt; !pic30-gcc
pic30-coff-gcc.exe: no input files 
&gt;&gt; !gmake
gmake: *** No targets specified and no makefile found.  Stop. 
&gt;&gt;
 </code></pre><br>
Thanks for your help,<br>
<br>
Roel Leenen<br>
<br>
<br>
<br>
PS: good produkt, good docu, good forum. Really motivates me to get started</div>
</article>

<article class="forum-post" id="p1026">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-15 01:30 UTC">2010-01-15 01:30 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi Roel Leenen,<br>
<br>
<br>
<br>
Thanks for all theses informations.<br>
<br>
I tested recently the blockset with the C30ComboLite_v3_22 compiler version and it works without problems with that compiler.<br>
<br>
<br>
<br>
Could you <br>
<br>
- <strong>upload </strong>the model you attempted to compile on the forum so as to make me able to reproduce the problem.<br>
<br>
- try to compile an example model (using a dsPIC30 or 24 or PIC33, from the example blockset directory) and <strong>report the error</strong> (like what you did with your model)<br>
<br>
<br>
<br>
Thanks for your help<br>
<br>
<br>
<br>
It seems that you did not installed softwares on their standard directory. It should works anyway, but I did not tested all configurations.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1027">
<header><strong>roel</strong><time datetime="2010-01-16 22:24 UTC">2010-01-16 22:24 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Thanks for your fast response. <br>
<br>
<br>
<br>
Here is the answer to your request:<br>
<br>
<br>
<br>
1. upload of my model =&gt; see attachment testbuild.zip<br>
<br>
<br>
<br>
2. I compiled the example model Data_Login_Matlab.mdl and got a similar error message. Below is the Matlab screendump after the build.<br>
<br>
<br>
<pre><code>C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: Data_Login_Matlab
### Generating code into build directory: D:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources
PT### Invoking Target Language Compiler on Data_Login_Matlab.rtw
	tlc
	-r
	D:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources\Data_Login_Matlab.rtw
	D:\microchip\MatlabSimulink\dspic\dspic.tlc
	-OD:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources
	-ID:\microchip\MatlabSimulink\dspic
	-ID:\microchip\MatlabSimulink\blocks
	-ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources\tlc
	-ID:\MATLAB\R2007b\rtw\c\tlc\mw
	-ID:\MATLAB\R2007b\rtw\c\tlc\lib
	-ID:\MATLAB\R2007b\rtw\c\tlc\blocks
	-ID:\MATLAB\R2007b\rtw\c\tlc\fixpt
	-ID:\MATLAB\R2007b\stateflow\c\tlc
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
	-aGMAKE_PLACE="D:\MATLAB\R2007b\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
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
...............
### Writing main
### Writing header file Data_Login_Matlab_types.h
.
### Writing header file Data_Login_Matlab.h
### Writing source file Data_Login_Matlab.c
### Writing header file Data_Login_Matlab_private.h
.
### Writing source file Data_Login_Matlab_data.c
### Writing header file autobuild.h
.
### Writing source file Data_Login_Matlab_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.1(17-Nov-2009) for Matlab R2007b.
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
                     18 avenue Joseph Lieutaud
                     13260 Cassis
                     FRANCE
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  http://www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: D:\microchip\MatlabSimulink\dspic\dspic_pic30_gcc.tmf
### Data_Login_Matlab.mk which is generated from D:\microchip\MatlabSimulink\dspic\dspic_pic30_gcc.tmf is up to date
### Building Data_Login_Matlab: .\Data_Login_Matlab.bat
<wbr>
D:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources&gt;set MATLAB=D:\MATLAB\R2007b  
<wbr>
D:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources&gt;"D:\MATLAB\R2007b\bin\win32\gmake" -f Data_Login_Matlab.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab_data.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab_main.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_Multiplexed_out_UART1.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_UART1_Interrupt.c 
dsPIC_UART1_Interrupt.c: In function '_U1TXInterrupt': 
dsPIC_UART1_Interrupt.c:19: warning:  PSV model not specified for '_U1TXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_UART1_Interrupt.c: In function '_U1RXInterrupt': 
dsPIC_UART1_Interrupt.c:31: warning:  PSV model not specified for '_U1RXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c: In function 'rt_MatMultAndIncCC_Dbl': 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c:54: error: unrecognizable insn: 
(0x00f5b7f8) (insn 233 75 76 6 (set (reg:SF 2 w2 [ A2_val$im ]) 
        (mem/s/j:SF (plus:P16APSV (reg/v/f:P16APSV 14 w14 [orig:57 A2 ] [57]) 
                (const_int 4 [0x4])) [0 &lt;variable&gt;.im+0 S4 A16])) -1 (nil) 
    (nil)) 
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c:54: internal compiler error: in extract_insn, at recog.c:2020 
Please submit a full bug report, 
with preprocessed source if appropriate. 
See &lt;URL:http://support.microchip.com&gt; for instructions. 
gmake: *** [rt_matmultandinccc_dbl.o] Error 255 
### Real-Time Workshop build procedure for model: 'Data_Login_Matlab' abort</code></pre><br>
<br>
Note: before compiling I reinstalled MPLAB and the C30 compiler into their default directory. The only exception is Matlab R2007b<br>
<br>
<br>
<br>
Waiting for your feedback,<br>
<br>
<br>
<br>
Regards,<br>
<br>
Roel</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/287-1.%20testbuild.zip">Pièce jointe : 1. testbuild.zip</a></p>
</article>

<article class="forum-post" id="p1028">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-18 11:10 UTC">2010-01-18 11:10 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi Roel,<br>
<br>
<br>
<br>
I had a look first at the demo example compilation (2 in your previosu message).<br>
<br>
<br>
<br>
I tested the compilation in the same conditions :<br>
<blockquote>Matlab R2007b installation + RTW and embedded coder + C30ComboLite_v3_22 + blockset v201</blockquote><br>
And no problems appears.<br>
<br>
<br>
<br>
It compiled successfully on my computer. The compilation is incremental. Thus, I deleted the directory Data_Login_Matlab_dspic and slprj to make a brend new compilation (you should try to do the same). I get the following output : <br>
<pre><code>C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: Data_Login_Matlab
### Generating code into build directory: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources
PPNumber of I/O PINs used : 2
TPTPTTPNumber of I/O PINs used : 2
TPNumber of I/O PINs used : 2
TT### Invoking Target Language Compiler on Data_Login_Matlab.rtw
	tlc
	-r
	C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources\Data_Login_Matlab.rtw
	C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic.tlc
	-OC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources
	-IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic
	-IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\blocks
	-IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources\tlc
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
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f3012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
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
..............
### Writing main
.
### Writing header file Data_Login_Matlab_types.h
.
### Writing header file Data_Login_Matlab.h
### Writing source file Data_Login_Matlab.c
### Writing header file Data_Login_Matlab_private.h
.
### Writing source file Data_Login_Matlab_data.c
### Writing header file autobuild.h
### Writing source file Data_Login_Matlab_main.c
.
### TLC code generation complete.
### Creating project marker file: rtw_proj.tmw
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V&amp;&amp;Version&amp;&amp;(&amp;&amp;  Date       &amp;&amp;) for Matlab &amp;&amp; Release &amp;&amp;.
<wbr>
<wbr>
Licence Accorded to  &amp;&amp;               Licence Name          &amp;&amp;
                     &amp;&amp;               Mailcontact           &amp;&amp;
                     &amp;&amp;               Companie              &amp;&amp;
                     &amp;&amp;               CompanieAddress1      &amp;&amp;
                     &amp;&amp;               CompanieAddress2      &amp;&amp;
                     &amp;&amp;               CompanieAddress3      &amp;&amp;
                     &amp;&amp;               CompanieAddress4      &amp;&amp;
<wbr>
 Facturation to :    &amp;&amp;               BuyerName             &amp;&amp;
                     &amp;&amp;               MailBuyer             &amp;&amp;
                     &amp;&amp;               BuyerAddress1         &amp;&amp;
                     &amp;&amp;               BuyerAddress2         &amp;&amp;
                     &amp;&amp;               BuyerAddress3         &amp;&amp;
                     &amp;&amp;               BuyerAddress4         &amp;&amp;
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
### Creating Data_Login_Matlab.mk from C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
### Building Data_Login_Matlab: .\Data_Login_Matlab.bat
<wbr>
C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f Data_Login_Matlab.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab_data.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab_main.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_Multiplexed_out_UART1.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_UART1_Interrupt.c 
dsPIC_UART1_Interrupt.c: In function '_U1TXInterrupt': 
dsPIC_UART1_Interrupt.c:19: warning:  PSV model not specified for '_U1TXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_UART1_Interrupt.c: In function '_U1RXInterrupt': 
dsPIC_UART1_Interrupt.c:31: warning:  PSV model not specified for '_U1RXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab.c 
### Creating rtwlib.a 
''pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  
### rtwlib.a Created
''pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f3012.gld -o ..\../Data_Login_Matlab.coff  Data_Login_Matlab_data.o Data_Login_Matlab_main.o dsPIC_Multiplexed_out_UART1.o dsPIC_UART1_Interrupt.o Data_Login_Matlab.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Program Files\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: mode pic30_coff 
Data_Login_Matlab_data.o 
Data_Login_Matlab_main.o 
dsPIC_Multiplexed_out_UART1.o 
dsPIC_UART1_Interrupt.o 
Data_Login_Matlab.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f3012-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floorf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)futil.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fchop.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)errno.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x100, Length = 0x3f00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x100               0x44e           0x675  (1653) 
.text                        0x54e               0x25c           0x38a  (906) 
.dinit                       0x7aa                0x42            0x63  (99) 
.text                        0x7ec                0x14            0x1e  (30) 
.isr                         0x800                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):          0xa83  (2691) 11% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x800] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.nbss                        0x800                   0            0x40  (64) 
.ndata                       0x840                   0            0x18  (24) 
.nbss                        0x858                   0             0xc  (12) 
.ndata                       0x864                   0             0x4  (4) 
.nbss                        0x868                   0             0x2  (2) 
.ndata                       0x86a                   0             0x2  (2) 
.nbss                        0x86c                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):           0x6e  (110) 5% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                        0x86e                               0x792  (1938) 
<wbr>
                        Maximum dynamic memory (bytes):          0x792  (1938) 
<wbr>
 ================================================================
*** Embedded Target for dsPIC by Lubin KERHUEL - http://www.kerhuel.eu
 | Licence Accorded to &amp;&amp;               Licence Name          &amp;&amp;|
 |                     &amp;&amp;               Mailcontact           &amp;&amp;|
 |          Companie : &amp;&amp;               Companie              &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress1      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress2      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress3      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress4      &amp;&amp;|
 | Financial Service : &amp;&amp;               BuyerName             &amp;&amp;|
 | Contact             &amp;&amp;               MailBuyer             &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress1         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress2         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress3         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress4         &amp;&amp;|
 | Version &amp;&amp;Version&amp;&amp;                       &amp;&amp;  Date       &amp;&amp;  |
 | For Matlab &amp;&amp; VerMatlab &amp;&amp; &amp;&amp; Release &amp;&amp;                     |
 ================================================================
*** Created executable: ..\../Data_Login_Matlab.coff
''pic30-bin2hex ..\../Data_Login_Matlab.coff  
*** Created executable: ..\../Data_Login_Matlab.hex
### Successful completion of Real-Time Workshop build procedure for model: Data_Login_Matlab
C30 Compiler found
C30 Compiler found</code></pre><br>
<br>
The difference is there : <br>
<br>
mine : <pre><code>&lt;i&gt;
&lt;/i&gt;''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples\Data_Login_Matlab_dspic\sources -IC:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab.c 
### Creating rtwlib.a 
''pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  
### rtwlib.a Created</code></pre><br>
<br>
yours : <pre><code>''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2    -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    Data_Login_Matlab.c
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2    -O   -I. -I..\.. -ID:\MATLAB\R2007b/simulink/include -ID:\MATLAB\R2007b/extern/include -ID:\MATLAB\R2007b/rtw/c/src -ID:\MATLAB\R2007b/rtw/c/ert -ID:\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\microchip\MatlabSimulink\examples\Data_Login_Matlab_dspic\sources -ID:\microchip\MatlabSimulink\examples -ID:\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c
D:\MATLAB\R2007b\rtw\c\libsrc/rt_matmultandinccc_dbl.c: In function 'rt_MatMultAndIncCC_Dbl':</code></pre><br>
<br>
The problems seems to come from the C30 compiler (however, it works fine for me)<br>
<br>
The C30 compiler could not compile the file rt_matmultandincrr_dbl.c. <br>
<br>
This problem may be due to the incremental compilation porcess. You may try to compile it again, deleting first all files generated by the compiler (slpjr and directory with the model name).<br>
<br>
Does your computer has enough memory to get the C30 compiler working fine ?<br>
<br>
We may compare my rt_matmultandincrr_dbl.c file with yours, but they should be identical (mathworks source file)<br>
<br>
<br>
<br>
Please report if you get anymore insight or results.</div>
</article>

<article class="forum-post" id="p1029">
<header><strong>roel</strong><time datetime="2010-01-18 23:04 UTC">2010-01-18 23:04 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am not an expert, but I am guessing that during my compilation for dsPIC certain Matlab RTW object files are missing. Hence the compiler is starting with the 'default' RTW source file 'rt_MatMultAndIncCC_Dbl'.c. I remember from other experiences that this is a typical one-time only exercise of a compiler, in this case the microchip C30, to generate object files for the dsPIC target out of the RTW source files. In your case it seems that the object files were already compiled (probably when you were using the C30 compiler for the first time) and he finds them in one of your paths. <br>
<br>
<br>
<br>
part of your output: <br>
<br>
### Creating rtwlib.a <br>
<br>
''pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  <br>
<br>
<br>
<br>
<br>
<br>
Could you tell me were these files are located on your system ?<br>
<br>
and could you upload this complete folder with matlab defaults ?<br>
<br>
Maybe by overtaking these files I can overcome my problem.<br>
<br>
<br>
<br>
The ultimate solution would be to force the compiler in some way to generate all the object files out of the source files supplied by matlab. So far I don't know how. Maybe another compiler brand would do the trick.<br>
<br>
<br>
<br>
I will let you know when I have some results.</div>
</article>

<article class="forum-post" id="p1037">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-19 14:51 UTC">2010-01-19 14:51 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi Roel,<br>
<br>
<br>
<br>
I made a mistake in the previous post : I did not delete the directory created during the code generation process containing the compiled matlab library. This library that cause you trouble when compiling with the latest C30 version, only with mablab 2007b. Because the binary file were already compiled in my test, I did not see any error and compilation porcess went Ok.<br>
<br>
<br>
<br>
Thus, very briefly, I get the same error that you get.<br>
<br>
<br>
<br>
<strong>Matlab 2007b + C30ComboLite_v3_22 does not works togethers !</strong><br>
<br>
But more recent Matlab works perfectly with C30ComboLite_v3_22.<br>
<br>
<br>
<br>
I attached the previous C30 version ( <a href="/archive-assets/">MPLAB_C_dsPICStudentv3_11B</a> and <a href="/archive-assets/">MPLAB_C_PIC24Studentv3_11B</a> for student, previously available on the microchip website). Install them booth and try to compile again. Delete first the two directory created by matlab (slpjr and directory created with the same name as the model you compile. )<br>
<br>
<br>
<br>
I am sure it will be easier to change C30 compiler, (or matlab version), rather than copy different library at the right place...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1038">
<header><strong>roel</strong><time datetime="2010-01-20 16:28 UTC">2010-01-20 16:28 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Now it works! After having installed the v3.11 C30 compiler version. Seems to be a backwards compatibility issue in the Microchip compiler.<br>
<br>
<br>
<br>
Thanks a lot,<br>
<br>
<br>
<br>
Regards,<br>
<br>
Roel</div>
</article>

<article class="forum-post" id="p1039">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-20 23:47 UTC">2010-01-20 23:47 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi roel,<br>
<br>
<br>
<br>
thanks for reporting results.<br>
<br>
<br>
<br>
As far as I remember, I think there was another problem with "multirate models" compiled with matlab 2007b. This last bug is due to matlab 2007 code generation error. (I coudl not test it right now but I'll check that next week)<br>
<br>
<br>
<br>
Anyway, I hope you'll enjoy developing signal processing algorithms using theses powerfull automatic code generation system.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1043">
<header><strong>jkavitha_john</strong><time datetime="2010-01-23 08:37 UTC">2010-01-23 08:37 UTC</time></header>
<h3>Build error in RTW.genMakefileAndBuild</h3>
<div class="forum-post-body">Hello,<br>
<br>
        I got an error for generating gmake file.I attached that error with this mail.I am waiting for your reply.<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
### Generating code into build directory: C:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources<br>
<br>
PNumber of I/O PINs used : 1<br>
<br>
TT### Invoking Target Language Compiler on untitled.rtw<br>
<br>
	tlc<br>
<br>
	-r<br>
<br>
	C:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources\untitled.rtw<br>
<br>
	C:\My Toolbox\dspic\dspic.tlc<br>
<br>
	-OC:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources<br>
<br>
	-IC:\My Toolbox\dspic<br>
<br>
	-IC:\My Toolbox\blocks<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources\tlc<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\mw<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\lib<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\blocks<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\fixpt<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\stateflow\c\tlc<br>
<br>
	-aEnforceIntegerDowncast=1<br>
<br>
	-aFoldNonRolledExpr=1<br>
<br>
	-aInlineInvariantSignals=0<br>
<br>
	-aInlineParameters=0<br>
<br>
	-aLocalBlockOutputs=1<br>
<br>
	-aRollThreshold=5<br>
<br>
	-aZeroInternalMemoryAtStartup=1<br>
<br>
	-aZeroExternalMemoryAtStartup=1<br>
<br>
	-aInitFltsAndDblsToZero=1<br>
<br>
	-aGenerateReport=0<br>
<br>
	-aGenCodeOnly=0<br>
<br>
	-aRTWVerbose=1<br>
<br>
	-aIncludeHyperlinkInReport=0<br>
<br>
	-aLaunchReport=0<br>
<br>
	-aForceParamTrailComments=0<br>
<br>
	-aGenerateComments=1<br>
<br>
	-aIgnoreCustomStorageClasses=0<br>
<br>
	-aIncHierarchyInIds=0<br>
<br>
	-aMaxRTWIdLen=31<br>
<br>
	-aShowEliminatedStatements=0<br>
<br>
	-aPrefixModelToSubsysFcnNames=1<br>
<br>
	-aIncDataTypeInIds=0<br>
<br>
	-aInsertBlockDesc=0<br>
<br>
	-aSimulinkBlockComments=1<br>
<br>
	-aInlinedPrmAccess="Literals"<br>
<br>
	-aTargetFcnLib="ansi_tfl_tmw.mat"<br>
<br>
	-aGenFloatMathFcnCalls="ANSI_C"<br>
<br>
	-aIsPILTarget=0<br>
<br>
	-aIncludeMdlTerminateFcn=0<br>
<br>
	-aCombineOutputUpdateFcns=1<br>
<br>
	-aSuppressErrorStatus=1<br>
<br>
	-aERTCustomFileBanners=1<br>
<br>
	-aLogVarNameModifier="rt_"<br>
<br>
	-aGenerateFullHeader=1<br>
<br>
	-aGenerateSampleERTMain=0<br>
<br>
	-aMatFileLogging=0<br>
<br>
	-aMultiInstanceERTCode=0<br>
<br>
	-aPurelyIntegerCode=0<br>
<br>
	-aPortableWordSizes=0<br>
<br>
	-aGenerateErtSFunction=0<br>
<br>
	-aGenerateASAP2=0<br>
<br>
	-aExtMode=0<br>
<br>
	-aExtModeStaticAlloc=0<br>
<br>
	-aExtModeStaticAllocSize=1000000<br>
<br>
	-aExtModeTransport=0<br>
<br>
	-aExtModeTesting=0<br>
<br>
	-aInlinedParameterPlacement="NonHierarchical"<br>
<br>
	-aTargetOS="BareBoardExample"<br>
<br>
	-aMultiInstanceErrorCode="Error"<br>
<br>
	-aRateGroupingCode=1<br>
<br>
	-aRTWCAPISignals=0<br>
<br>
	-aRTWCAPIParams=0<br>
<br>
	-aRootIOStructures=0<br>
<br>
	-aERTCustomFileTemplate="dsPIC_main.tlc"<br>
<br>
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake"<br>
<br>
	-aOPTIM_GCC="-mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"<br>
<br>
	-aLDPICTYPE="-T C:\Program Files\Microchip\MPLAB C30\support\dsPIC30F\gld\p30f4011.gld"<br>
<br>
	-aLDLIBPIC="C:\Program Files\Microchip\MPLAB C30\lib\libpic30-coff.a  C:\Program Files\Microchip\MPLAB C30\lib\libp30f4011-coff.a C:\Program Files\Microchip\MPLAB C30\lib\libc-coff.a C:\Program Files\Microchip\MPLAB C30\lib\libm-coff.a"<br>
<br>
	-aPIC_INCLUDES="-I C:\Program Files\Microchip\MPLAB C30\support\inc"<br>
<br>
	-aPIC_REF="30f4011"<br>
<br>
	-aGCCPATH="C:\Program Files\Microchip\MPLAB C30\bin"<br>
<br>
	-p10000<br>
<br>
<br>
<br>
<br>
<br>
### Loading TLC function libraries<br>
<br>
<br>
<br>
.....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
### Caching model source code<br>
<br>
................<br>
<br>
### Writing main<br>
<br>
.<br>
<br>
### Writing header file untitled_types.h<br>
<br>
### Writing header file untitled.h<br>
<br>
.<br>
<br>
### Writing source file untitled.c<br>
<br>
### Writing header file untitled_private.h<br>
<br>
### Writing source file untitled_data.c<br>
<br>
.<br>
<br>
### Writing header file autobuild.h<br>
<br>
### Writing source file untitled_main.c<br>
<br>
### TLC code generation complete.<br>
<br>
### Creating project marker file: rtw_proj.tmw<br>
<br>
### Evaluating PostCodeGenCommand specified in the model<br>
<br>
<br>
<br>
     ----------------------------------------------------<br>
<br>
     ----------------------------------------------------<br>
<br>
Embedded Coder for dsPIC V3.1(17-Nov-2009) for Matlab R2007a.<br>
<br>
<br>
<br>
<br>
<br>
Licence Accorded to  Demonstration Version<br>
<br>
                     [adresse e-mail retirée]<br>
<br>
                     Author : Lubin KERHUEL<br>
<br>
                     WEBSITE : <a href="/archive-assets/">http://www.kerhuel.eu/wiki</a><br>
<br>
                     <br>
<br>
                     SIRENE : 503 920 456<br>
<br>
                     SIRET : 503 920 456 00012<br>
<br>
<br>
<br>
 Facturation to :    Demo<br>
<br>
                     Demo<br>
<br>
                     Lubin KERHUEL<br>
<br>
                     18 avenue Joseph Lieutaud<br>
<br>
                     13260 Cassis<br>
<br>
                     FRANCE<br>
<br>
<br>
<br>
     ----------------------------------------------------<br>
<br>
Check updates and new informations at :  <a href="/">http://www.kerhuel.eu</a> <br>
<br>
     ----------------------------------------------------<br>
<br>
<br>
<br>
.<br>
<br>
### Processing Template Makefile: C:\My Toolbox\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Creating untitled.mk from C:\My Toolbox\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building untitled: .\untitled.bat<br>
<br>
 <br>
<br>
C:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007a  <br>
<br>
 <br>
<br>
C:\Program Files\MATLAB\R2007a\work\untitled_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake" -f untitled.mk  GENERATE_REPORT=0 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
C:\Program Files\Microchip\MPLAB C30\binpic30-gcc  -c -mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IC:\PROGRA~1\MATLAB\R2007a\work\untitled_dspic\sources -IC:\PROGRA~1\MATLAB\R2007a\work -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -I C:\Program Files\Microchip\MPLAB C30\support\inc    dsPIC_OutputCompare_Interrupt.c <br>
<br>
gmake: command not found: C:\Program <br>
<br>
gmake: *** [dsPIC_OutputCompare_Interrupt.o] Error 0x7f <br>
<br>
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
&gt;&gt;</div>
</article>

<article class="forum-post" id="p1044">
<header><strong>Bobes</strong><time datetime="2010-01-23 09:59 UTC">2010-01-23 09:59 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hello John, may be I can help... I belive I hade same problem:<br>
<br>
Try clicking on the block "Configure Simulink for dsPIC Target", I belive you have somewhere the path in form "C:\Program Files\..." and it should be in the "DOS" format.. like this: "C:\PROGRA~1\..."<br>
<br>
That is I think why is there this message:<br>
<pre><code>gmake: command not found: C:\Program </code></pre><br>
go to Simulation/Configuration parameters ... should look similar like on the attachment, just configured bit differently for your target..</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/288-Clipboard01.jpg">Pièce jointe : Clipboard01.jpg</a></p>
</article>

<article class="forum-post" id="p1045">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-23 23:29 UTC">2010-01-23 23:29 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
Bobes provided a good advice. <br>
<br>
You may also try to click on the yellow block titled something like "configure simulink for dsPIC target". This block automatically check all path and should solve problems. If it did not do the job, I would be interrested to get the parameters of your computer to make this block algorithm even more robust.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1048">
<header><strong>jkavitha_john</strong><time datetime="2010-01-25 11:49 UTC">2010-01-25 11:49 UTC</time></header>
<h3>Re: About Compile Error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
    Thanks for your reply.I am also having another problem,<br>
<br>
    when I compile the program some error has occurred that is,<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
### Starting Real-Time Workshop build procedure for model: untitled<br>
<br>
### Generating code into build directory: C:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources<br>
<br>
PT### Invoking Target Language Compiler on untitled.rtw<br>
<br>
	tlc<br>
<br>
	-r<br>
<br>
	C:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources\untitled.rtw<br>
<br>
	C:\My Toolbox\dspic\dspic.tlc<br>
<br>
	-OC:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources<br>
<br>
	-IC:\My Toolbox\dspic<br>
<br>
	-IC:\My Toolbox\blocks<br>
<br>
	-IC:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources\tlc<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\mw<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\lib<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\blocks<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\fixpt<br>
<br>
	-IC:\Program Files\MATLAB\R2007a\stateflow\c\tlc<br>
<br>
	-aEnforceIntegerDowncast=1<br>
<br>
	-aFoldNonRolledExpr=1<br>
<br>
	-aInlineInvariantSignals=0<br>
<br>
	-aInlineParameters=0<br>
<br>
	-aLocalBlockOutputs=1<br>
<br>
	-aRollThreshold=5<br>
<br>
	-aZeroInternalMemoryAtStartup=1<br>
<br>
	-aZeroExternalMemoryAtStartup=1<br>
<br>
	-aInitFltsAndDblsToZero=1<br>
<br>
	-aGenerateReport=0<br>
<br>
	-aGenCodeOnly=0<br>
<br>
	-aRTWVerbose=1<br>
<br>
	-aIncludeHyperlinkInReport=0<br>
<br>
	-aLaunchReport=0<br>
<br>
	-aForceParamTrailComments=0<br>
<br>
	-aGenerateComments=1<br>
<br>
	-aIgnoreCustomStorageClasses=0<br>
<br>
	-aIncHierarchyInIds=0<br>
<br>
	-aMaxRTWIdLen=31<br>
<br>
	-aShowEliminatedStatements=0<br>
<br>
	-aPrefixModelToSubsysFcnNames=1<br>
<br>
	-aIncDataTypeInIds=0<br>
<br>
	-aInsertBlockDesc=0<br>
<br>
	-aSimulinkBlockComments=1<br>
<br>
	-aInlinedPrmAccess="Literals"<br>
<br>
	-aTargetFcnLib="ansi_tfl_tmw.mat"<br>
<br>
	-aGenFloatMathFcnCalls="ANSI_C"<br>
<br>
	-aIsPILTarget=0<br>
<br>
	-aIncludeMdlTerminateFcn=0<br>
<br>
	-aCombineOutputUpdateFcns=1<br>
<br>
	-aSuppressErrorStatus=1<br>
<br>
	-aERTCustomFileBanners=1<br>
<br>
	-aLogVarNameModifier="rt_"<br>
<br>
	-aGenerateFullHeader=1<br>
<br>
	-aGenerateSampleERTMain=0<br>
<br>
	-aMatFileLogging=0<br>
<br>
	-aMultiInstanceERTCode=0<br>
<br>
	-aPurelyIntegerCode=0<br>
<br>
	-aPortableWordSizes=0<br>
<br>
	-aGenerateErtSFunction=0<br>
<br>
	-aGenerateASAP2=0<br>
<br>
	-aExtMode=0<br>
<br>
	-aExtModeStaticAlloc=0<br>
<br>
	-aExtModeStaticAllocSize=1000000<br>
<br>
	-aExtModeTransport=0<br>
<br>
	-aExtModeTesting=0<br>
<br>
	-aInlinedParameterPlacement="NonHierarchical"<br>
<br>
	-aTargetOS="BareBoardExample"<br>
<br>
	-aMultiInstanceErrorCode="Error"<br>
<br>
	-aRateGroupingCode=1<br>
<br>
	-aRTWCAPISignals=0<br>
<br>
	-aRTWCAPIParams=0<br>
<br>
	-aRootIOStructures=0<br>
<br>
	-aERTCustomFileTemplate="dsPIC_main.tlc"<br>
<br>
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake"<br>
<br>
	-aOPTIM_GCC="-mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"<br>
<br>
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4011.gld"<br>
<br>
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4011-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"<br>
<br>
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"<br>
<br>
	-aPIC_REF="30f4011"<br>
<br>
	-aGCCPATH=""<br>
<br>
	-p10000<br>
<br>
<br>
<br>
<br>
<br>
### Loading TLC function libraries<br>
<br>
<br>
<br>
....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
.<br>
<br>
### Caching model source code<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (4) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (5) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (6) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (7) was out of the range 0 - 3<br>
<br>
...........<br>
<br>
### Writing main<br>
<br>
.<br>
<br>
### Writing header file untitled_types.h<br>
<br>
### Writing header file untitled.h<br>
<br>
.<br>
<br>
### Writing source file untitled.c<br>
<br>
### Writing header file untitled_private.h<br>
<br>
### Writing source file untitled_data.c<br>
<br>
.<br>
<br>
### Writing header file autobuild.h<br>
<br>
### Writing source file untitled_main.c<br>
<br>
### TLC code generation complete.<br>
<br>
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
<br>
<br>
How can I solved it,please help me.</div>
</article>

<article class="forum-post" id="p1049">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-25 17:32 UTC">2010-01-25 17:32 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Thus, installed examples do not compile when you install it newly, but the models you created, that are thus not replaced compile ?<br>
<br>
This is due to path. The examples path are set for my computer. However, theses path error should be corrected with the yellow block "configure simulink for dsPIC"<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1061">
<header><strong>jkavitha_john</strong><time datetime="2010-01-28 08:58 UTC">2010-01-28 08:58 UTC</time></header>
<h3>Re: About Compile Error</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Thanks for your reply.I am also having another problem,<br>
<br>
when I compile the program some error has occurred that is,<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
### Starting Real-Time Workshop build procedure for model: untitled<br>
<br>
### Generating code into build directory: C:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources<br>
<br>
PT### Invoking Target Language Compiler on untitled.rtw<br>
<br>
tlc<br>
<br>
-r<br>
<br>
C:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources\untitled.rtw<br>
<br>
C:\My Toolbox\dspic\dspic.tlc<br>
<br>
-OC:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources<br>
<br>
-IC:\My Toolbox\dspic<br>
<br>
-IC:\My Toolbox\blocks<br>
<br>
-IC:\Documents and Settings\User\Desktop\matlab dspic\programs\led\untitled_dspic\sources\tlc<br>
<br>
-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\mw<br>
<br>
-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\lib<br>
<br>
-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\blocks<br>
<br>
-IC:\Program Files\MATLAB\R2007a\rtw\c\tlc\fixpt<br>
<br>
-IC:\Program Files\MATLAB\R2007a\stateflow\c\tlc<br>
<br>
-aEnforceIntegerDowncast=1<br>
<br>
-aFoldNonRolledExpr=1<br>
<br>
-aInlineInvariantSignals=0<br>
<br>
-aInlineParameters=0<br>
<br>
-aLocalBlockOutputs=1<br>
<br>
-aRollThreshold=5<br>
<br>
-aZeroInternalMemoryAtStartup=1<br>
<br>
-aZeroExternalMemoryAtStartup=1<br>
<br>
-aInitFltsAndDblsToZero=1<br>
<br>
-aGenerateReport=0<br>
<br>
-aGenCodeOnly=0<br>
<br>
-aRTWVerbose=1<br>
<br>
-aIncludeHyperlinkInReport=0<br>
<br>
-aLaunchReport=0<br>
<br>
-aForceParamTrailComments=0<br>
<br>
-aGenerateComments=1<br>
<br>
-aIgnoreCustomStorageClasses=0<br>
<br>
-aIncHierarchyInIds=0<br>
<br>
-aMaxRTWIdLen=31<br>
<br>
-aShowEliminatedStatements=0<br>
<br>
-aPrefixModelToSubsysFcnNames=1<br>
<br>
-aIncDataTypeInIds=0<br>
<br>
-aInsertBlockDesc=0<br>
<br>
-aSimulinkBlockComments=1<br>
<br>
-aInlinedPrmAccess="Literals"<br>
<br>
-aTargetFcnLib="ansi_tfl_tmw.mat"<br>
<br>
-aGenFloatMathFcnCalls="ANSI_C"<br>
<br>
-aIsPILTarget=0<br>
<br>
-aIncludeMdlTerminateFcn=0<br>
<br>
-aCombineOutputUpdateFcns=1<br>
<br>
-aSuppressErrorStatus=1<br>
<br>
-aERTCustomFileBanners=1<br>
<br>
-aLogVarNameModifier="rt_"<br>
<br>
-aGenerateFullHeader=1<br>
<br>
-aGenerateSampleERTMain=0<br>
<br>
-aMatFileLogging=0<br>
<br>
-aMultiInstanceERTCode=0<br>
<br>
-aPurelyIntegerCode=0<br>
<br>
-aPortableWordSizes=0<br>
<br>
-aGenerateErtSFunction=0<br>
<br>
-aGenerateASAP2=0<br>
<br>
-aExtMode=0<br>
<br>
-aExtModeStaticAlloc=0<br>
<br>
-aExtModeStaticAllocSize=1000000<br>
<br>
-aExtModeTransport=0<br>
<br>
-aExtModeTesting=0<br>
<br>
-aInlinedParameterPlacement="NonHierarchical"<br>
<br>
-aTargetOS="BareBoardExample"<br>
<br>
-aMultiInstanceErrorCode="Error"<br>
<br>
-aRateGroupingCode=1<br>
<br>
-aRTWCAPISignals=0<br>
<br>
-aRTWCAPIParams=0<br>
<br>
-aRootIOStructures=0<br>
<br>
-aERTCustomFileTemplate="dsPIC_main.tlc"<br>
<br>
-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake"<br>
<br>
-aOPTIM_GCC="-mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0 -cref"<br>
<br>
-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4011.gld"<br>
<br>
-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4011-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"<br>
<br>
-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"<br>
<br>
-aPIC_REF="30f4011"<br>
<br>
-aGCCPATH=""<br>
<br>
-p10000<br>
<br>
<br>
<br>
<br>
<br>
### Loading TLC function libraries<br>
<br>
<br>
<br>
....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
.<br>
<br>
### Caching model source code<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (4) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (5) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (6) was out of the range 0 - 3<br>
<br>
Error: File: C:\My Toolbox\blocks\dsPIC_MASTER.tlc Line: 113 Column: 62<br>
<br>
The specified index (7) was out of the range 0 - 3<br>
<br>
...........<br>
<br>
### Writing main<br>
<br>
.<br>
<br>
### Writing header file untitled_types.h<br>
<br>
### Writing header file untitled.h<br>
<br>
.<br>
<br>
### Writing source file untitled.c<br>
<br>
### Writing header file untitled_private.h<br>
<br>
### Writing source file untitled_data.c<br>
<br>
.<br>
<br>
### Writing header file autobuild.h<br>
<br>
### Writing source file untitled_main.c<br>
<br>
### TLC code generation complete.<br>
<br>
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
<br>
<br>
How can I solved it,please help me.</div>
</article>

<article class="forum-post" id="p1063">
<header><strong>Bobes</strong><time datetime="2010-01-28 19:29 UTC">2010-01-28 19:29 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">Seems like some timer problem, you should probably post your mdl file here. Without that its quite hard to find the problem. However I have encountered this problem as well, but I do not recall what was the cause.</div>
</article>

<article class="forum-post" id="p1104">
<header><strong>jkavitha_john</strong><time datetime="2010-03-05 05:22 UTC">2010-03-05 05:22 UTC</time></header>
<h3>Re: PWM Motor Output</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I have generated a mdl file with PWM Motor Output. The hex file is generated but the output is not coming.I have attached my mdl file .Please tell me what the reason,the ouput is not coming.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/302-pwm.mdl">Pièce jointe : pwm.mdl</a></p>
</article>

<article class="forum-post" id="p1105">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-05 07:34 UTC">2010-03-05 07:34 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">The model is composed of constants attached to a PWM motor blocks.<br>
<br>
<br>
<br>
Two possible problems : <br>
<br>
first one : const blocks  has a default sampling time set to "inf". This mean that they are typically "executed" only once, and blocks depending only on theses values (here PWM blocks) will inherit this "inf" sampling time. Thus it will be executed only once and that's not very good.<br>
<br>
==&gt; Set const sampling time to .01 for example on at least one (or all) constant connected to the PWM block.<br>
<br>
<br>
<br>
Second one : the Period and the duty cycle are set with the same value of 1000. Thus, the duty cycle will be of 100% inyour case, you won't see anything at the output.<br>
<br>
PWM1 value should be set to a lower value than the Period (set it to 1/2 ==&gt; 500 for example)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1125">
<header><strong>jkavitha_john</strong><time datetime="2010-03-10 06:45 UTC">2010-03-10 06:45 UTC</time></header>
<h3>PWM Output</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
            I had set .01 to the constant value but the ouput is not coming.I attached my mdl file and also the constant properties.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/303-pwm.mdl">Pièce jointe : pwm.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/304-Doc1.doc">Pièce jointe : Doc1.doc</a></p>
</article>

<article class="forum-post" id="p1126">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-10 07:23 UTC">2010-03-10 07:23 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">It should works.<br>
<br>
do you use a scope to check if that's works ? the PWM output is here quite fast : <br>
<br>
<br>
<br>
frequency is : 1/ (4.194303e-001 * 1000 / 65534) = 156Hz.<br>
<br>
If you use a "voltmetre" , you will probably see VDD/2, typically 2.5V.<br>
<br>
<br>
<br>
Anyway, please try to change in the Master block, Time Step reference : <br>
<br>
from FreeRun into Timer1 based as this is more commonly used.<br>
<br>
<br>
<br>
You may check that the dsPIC is running by activating a busy flag port, on the pin you select, in the master block. This busy flag should "flash" at the same frequency as the model : 0.01Hz here. (but as the model's calculation is nothing, it will be very very short and need also a scope to be detected.<br>
<br>
<br>
<br>
<br>
<br>
Please let me know !<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1127">
<header><strong>jkavitha_john</strong><time datetime="2010-03-10 09:27 UTC">2010-03-10 09:27 UTC</time></header>
<h3>Re: PWM Ouput</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
            I have change that settings but the output is not coming.Can u give me the working mdl file,please.</div>
</article>

<article class="forum-post" id="p1129">
<header><strong>jkavitha_john</strong><time datetime="2010-03-11 06:54 UTC">2010-03-11 06:54 UTC</time></header>
<h3>PWM Ouput</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
            Thanks for ur reply,Now its coming.I changed my compiler v2.01 to v3.11.Pwm Output is coming.But I dont know,how can I calculate the freq.please tell me the formula.</div>
</article>

<article class="forum-post" id="p1130">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-11 07:25 UTC">2010-03-11 07:25 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">You should find information here : <a href="/wiki/dspic-block-pwm-motor-output/">http://www.kerhuel.eu/wiki/Block/PWM_Motor_Output</a><br>
<br>
hope it's clear enough as it seem to be tricky when I am reading it today !<br>
<br>
<br>
<br>
feel free to edit the wiki, and let me know for unclear point.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1131">
<header><strong>jkavitha_john</strong><time datetime="2010-03-12 05:23 UTC">2010-03-12 05:23 UTC</time></header>
<h3>PWM Ouput</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
           Thanks for ur reply.I can find the freq calculation.I have one question, real time datas sent from Matlab to dsPIC Controller is it possibe or not.</div>
</article>

<article class="forum-post" id="p1132">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-12 07:29 UTC">2010-03-12 07:29 UTC</time></header>
<h3>Re: Build error in function rt_MatMultAndIncCC_Dbl</h3>
<div class="forum-post-body">It's possible to send data from matlab to the dsPIC throw the rs232gui interface for example. <br>
<br>
However, that will not be real time as Matlab is not realtime !<br>
<br>
Thus, you will be able to send set-point, or to change gain during execution of the dsPIC realtime program, but you will not do a realtime cosimulation including booth a dsPIC and Matlab.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1136">
<header><strong>jkavitha_john</strong><time datetime="2010-03-13 06:54 UTC">2010-03-13 06:54 UTC</time></header>
<h3>PWM Output</h3>
<div class="forum-post-body">Hai Lubin,<br>
<br>
    Thanks for ur reply.Can I find the freq by using blocks only, without any constant value.</div>
</article>

<article class="forum-post" id="p1137">
<header><strong>jkavitha_john</strong><time datetime="2010-03-13 10:58 UTC">2010-03-13 10:58 UTC</time></header>
<h3>PWM Output</h3>
<div class="forum-post-body">Hi,<br>
<br>
    How can I calculate for setting the PWM dead time.</div>
</article>

