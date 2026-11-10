---
title: "error compilation"
url: "/forum/topic/382/"
archiveKind: "topic"
---
# error compilation

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1545">
<header><strong>ELMAY</strong><time datetime="2011-04-14 14:26 UTC">2011-04-14 14:26 UTC</time></header>
<div class="forum-post-body"><pre><code>### Starting Microchip Embedded Target build procedure for model: Demo30f
### Generating code into build directory: D:\Documents and Settings\ELMAY\Bureau\Demo30f_dspic_ert\src
Warning: The file containing block diagram 'dsPICConfigLib' is shadowed by a file of the same name higher on the MATLAB
path. This can cause unexpected behavior.  For more information see "Avoiding Problems with Shadowed Files" in the
Simulink documentation 
Warning: The file containing block diagram 'dsPICRunTimeLib' is shadowed by a file of the same name higher on the MATLAB
path. This can cause unexpected behavior.  For more information see "Avoiding Problems with Shadowed Files" in the
Simulink documentation 
Warning: The file containing block diagram 'forumkerhueladc_filter_OC' is shadowed by a file of the same name higher on
the MATLAB path. This can cause unexpected behavior.  For more information see "Avoiding Problems with Shadowed Files" in
the Simulink documentation 
Warning: Cannot attach component to a locked object 
Warning: Changing property 'LifeSpan' is not allowed. 
### Invoking Target Language Compiler on Demo30f.rtw
	tlc
	-r
	D:\Documents and Settings\ELMAY\Bureau\Demo30f_dspic_ert\src\Demo30f.rtw
	D:\Documents and Settings\ELMAY\Bureau\dsPIC_Matlab\dspic\dsPIC_stf.tlc
	-OD:\Documents and Settings\ELMAY\Bureau\Demo30f_dspic_ert\src
	-ID:\Documents and Settings\ELMAY\Bureau\dsPIC_Matlab\dspic
	-ID:\Documents and Settings\ELMAY\Bureau\dsPIC_Matlab\dspicblks
	-ID:\Documents and Settings\ELMAY\Bureau\Demo30f_dspic_ert\src\tlc
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
	-aTargetFcnLib="ansi_tfl_table_tmw.mat"
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
	-aPICTYPE="30F4011"
	-aOGCC="-O3 -g -fschedule-insns -fschedule-insns2"
	-aLDFS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aMCPATH="D:\PROGRA~1\MICROC~1\mplabc30\v3.25"
	-aLINKERSCRIPT="D:\Program Files\Microchip\mplabc30\v3.25\support\dsPIC30F\gld\p30F4011.gld"
	-aPICLIB="D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30F4011-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libq-coff.a D:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libq-dsp-coff.a"
	-aPICINCL=" -ID:\PROGRA~1\MICROC~1\mplabc30\v3.25\include -ID:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\h"
	-aProtectedModelReferenceTarget=0
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
.
### Writing header file Demo30f_types.h
### Writing header file Demo30f.h
### Writing source file Demo30f.c
.
### Writing header file Demo30f_private.h
### Writing header file autobuild.h
.
### Writing source file main.c
### Writing source file Interrupts.c
### TLC code generation complete.
### Creating project marker file: rtw_proj.tmw
### Evaluating PostCodeGenCommand specified in the model
.
### Processing Template Makefile: D:\Documents and Settings\ELMAY\Bureau\dsPIC_Matlab\dspic\dsPIC_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating Demo30f.mk from D:\Documents and Settings\ELMAY\Bureau\dsPIC_Matlab\dspic\dsPIC_gcc.tmf
### Building Demo30f: "%MATLAB%\bin\win32\gmake" -f Demo30f.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
Le chemin d'accŠs sp‚cifi‚ est introuvable. 
### Real-Time Workshop build procedure for model: 'Demo30f' aborted due to an error.</code></pre></div>
</article>

<article class="forum-post" id="p1546">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-14 14:58 UTC">2011-04-14 14:58 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Try to add the yellow block that configure automatically the model (it may resolve incorrect path).<br>
<br>
<br>
<br>
It seems you may have to clean up your matlab path.<br>
<br>
Do you have multiple blockset installed ? (like microchip official one, mine or others ?)<br>
<br>
<br>
<br>
Please install latest blockset version. I am not sure you are using the last one.<br>
<br>
<br>
<br>
does the model in the example directory compile ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p3487">
<header><strong>Zemog Zurc</strong><time datetime="2014-07-23 16:09 UTC">2014-07-23 16:09 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Hello Lubin<br>
<br>
<br>
<br>
  I´ve experienced the same problem but in different way because I try to compile a blinking led project using the dsPIC30F4011 but when I compile it an error appears.<br>
<br>
<br>
<br>
My error is:<br>
<br>
<br>
<br>
Blinking_led_main.c:32: error: 'BORV_20' undeclared here (not in a function) <br>
<br>
gmake: *** [Blinking_led_main.o] Error 255 <br>
<br>
<br>
<br>
<br>
<br>
I thing the problem could be the compiler. Mine is C30 v3.31.<br>
<br>
If you have some suggest I will thank you  so much.</div>
</article>

<article class="forum-post" id="p3488">
<header><strong>LubinKerhuel</strong><time datetime="2014-07-24 13:26 UTC">2014-07-24 13:26 UTC</time></header>
<h3>Re: error compilation</h3>
<div class="forum-post-body">Hi Zemog,<br>
<br>
<br>
<br>
I would recommend to use the new blockset we are developping now at Microchip. You might find a free demo version at <a href="http://www.microchip.com/SimulinkBlocks">http://www.microchip.com/SimulinkBlocks</a><br>
<br>
The current version is the V3.30 but a new version with many fixed issues will be release soon.<br>
<br>
<br>
<br>
You might also use the microchip forum for questions about this new Microchip Blockset: <a href="http://www.microchip.com/forums/f192.aspx">http://www.microchip.com/forums/f192.aspx</a><br>
<br>
Do not hesitate to post any issues you might encounter or any new features you would like to have.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Lubin</div>
</article>

