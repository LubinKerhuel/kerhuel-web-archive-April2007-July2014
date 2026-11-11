---
title: "Some help needed : Error while compiling"
url: "/forum/topic/88/"
archiveKind: "topic"
---
# Some help needed : Error while compiling

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p219">
<header><strong>barryforever</strong><time datetime="2008-02-17 14:55 UTC">2008-02-17 14:55 UTC</time></header>
<div class="forum-post-body">I tried doing some program and it dint go all that easy showed me error every time .<br>
<br>
I even tried your sinusoidal signal servo control it showed me error<br>
<br>
I use a R2007b with all required toolboxes <br>
<br>
The first error i get when put dspic master into a new model areai get the following warning in matlab workspace<br>
<br>
<br>
<pre><code>Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using
==&gt; dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time workshop.
&gt; In load_system at 52
  In libbrowse&gt;i_LoadSys at 142
  In libbrowse&gt;LoadLibrary at 121
  In libbrowse at 24
TimeStep was undefined and is set to : 0.001</code></pre><br>
<br>
Then i put the simulink configuration in the model.<br>
<br>
<br>
<br>
I used a digital input and a digital write output ..<br>
<br>
which means that what ever i give in port b 1 i should be able to get port b 2 right ?<br>
<br>
then i compiled things in with generate code only as worshop parameter and it compiled without error.<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;Warning: The dialog of 'mika/Master' is being closed because a mask
parameter has been changed.
&gt; In C:\toolbox\blocks\dsPIC_Set_Dialog_PopUp_Param.p&gt;dsPIC_Set_Dialog_PopUp_Param at 57
  In C:\toolbox\blocks\dsPIC_MASTER_callback_InitMask.p&gt;dsPIC_MASTER_callback_InitMask at 225
Number of I/O PINs used : 2
Number of I/O PINs used : 2
Number of I/O PINs used : 2
### Starting Real-Time Workshop build procedure for model: mika
### Generating code into build directory: C:\Documents and Settings\Barry\My Documents\MATLAB\mouline\mika_dspic\sources
Warning: Source 'mika/Digital Input' specifies that its sample time (-1) is
back-inherited. You should explicitly specify the sample time of sources.
You can disable this diagnostic by setting the 'Source block specifies -1
sample time' diagnostic to 'none' in the Sample Time group on the
Diagnostics pane of the Configuration Parameters dialog box.
### Invoking Target Language Compiler on mika.rtw
	tlc
	-r
	C:\Documents and Settings\Barry\My Documents\MATLAB\mouline\mika_dspic\sources\mika.rtw
	C:\toolbox\dspic\dspic.tlc
	-OC:\Documents and Settings\Barry\My Documents\MATLAB\mouline\mika_dspic\sources
	-IC:\toolbox\dspic
	-IC:\toolbox\blocks
	-IC:\Documents and Settings\Barry\My Documents\MATLAB\mouline\mika_dspic\sources\tlc
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
	-aGenCodeOnly=1
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
	-aOPTIM_GCC="-mcpu=30F6011 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\gld\p30f6011.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F6011-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="30f6011"
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
...........
### Writing main
### Writing header file mika_types.h
.
### Writing header file mika.h
### Writing source file mika.c
### Writing header file mika_private.h
.
### Writing header file autobuild.h
### Writing source file mika_main.c
.
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
Embedded Coder for dsPIC V0.96b(13-Feb-2008) for Matlab R2007b.
Licence Accorded to Demonstration Version - 
<wbr>
<wbr>
informations available at  archive.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\toolbox\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;
### in default batch file
### Creating mika.mk from C:\toolbox\dspic\dspic_pic30_gcc.tmf
### Successful completion of Real-Time Workshop build procedure for model: mika
</code></pre><br>
<br>
<br>
<br>
Now what do i do with the bat file created there is no hex file generation in the folder.<br>
<br>
I tried using MPLAB to make the required files<br>
<br>
it also gave me error :<br>
<br>
<br>
<pre><code>Opening Matlab session and model 'C:\Documents and Settings\Barry\My Documents\MATLAB\mouline\mika.mdl'
Please wait...
<wbr>
Warning: Error evaluating 'LoadFcn'
callback of Master block (mask) 'Master'.
Error using ==&gt; dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to
dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time
workshop.
&gt; In &lt;a href="error:C:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m,14,1"&gt;MplabOpenModel at 14&lt;/a&gt;
<wbr>
</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/21-mouline.zip">Pièce jointe : mouline.zip</a></p>
</article>

<article class="forum-post" id="p220">
<header><strong>micman2</strong><time datetime="2008-02-17 19:39 UTC">2008-02-17 19:39 UTC</time></header>
<h3>Re: Some help needed : Error while compiling</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
i teset the code and not have problem:<br>
<br>
<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt;<br>
<br>
dsPIC_ConfigRTWOption at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration<br>
<br>
Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 148<br>
<br>
  In uiopen at 196<br>
<br>
Number of I/O PINs used : 2<br>
<br>
Number of I/O PINs used : 2<br>
<br>
### Starting Real-Time Workshop build procedure for model: mika<br>
<br>
### Generating code into build directory: C:\Documents and Settings\Michele\Desktop\Nuova cartella\mouline\mika_dspic\sources<br>
<br>
Number of I/O PINs used : 2<br>
<br>
Warning: Source 'mika/Digital Input' specifies that its sample time (-1) is back-inherited. You should<br>
<br>
explicitly specify the sample time of sources. You can disable this diagnostic by setting the 'Source<br>
<br>
block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the Diagnostics pane of<br>
<br>
the Configuration Parameters dialog box.<br>
<br>
### Invoking Target Language Compiler on mika.rtw<br>
<br>
	tlc<br>
<br>
	-r<br>
<br>
	C:\Documents and Settings\Michele\Desktop\Nuova cartella\mouline\mika_dspic\sources\mika.rtw<br>
<br>
	C:\MyToolBox\dspic\dspic.tlc<br>
<br>
	-OC:\Documents and Settings\Michele\Desktop\Nuova cartella\mouline\mika_dspic\sources<br>
<br>
	-IC:\MyToolBox\dspic<br>
<br>
	-IC:\MyToolBox\blocks<br>
<br>
	-IC:\Documents and Settings\Michele\Desktop\Nuova cartella\mouline\mika_dspic\sources\tlc<br>
<br>
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\mw<br>
<br>
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\lib<br>
<br>
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\blocks<br>
<br>
	-IC:\Programmi\MATLAB\R2007b\rtw\c\tlc\fixpt<br>
<br>
	-IC:\Programmi\MATLAB\R2007b\stateflow\c\tlc<br>
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
	-aGenCodeOnly=1<br>
<br>
	-aRTWVerbose=1<br>
<br>
	-aIncludeHyperlinkInReport=0<br>
<br>
	-aLaunchReport=0<br>
<br>
	-aGenerateTraceInfo=0<br>
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
	-aIncDataTypeInIds=0<br>
<br>
	-aInsertBlockDesc=0<br>
<br>
	-aSimulinkBlockComments=1<br>
<br>
	-aInlinedPrmAccess="Literals"<br>
<br>
	-aTargetFcnLib="ansi_tfl_table_tmw.mat"<br>
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
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake"<br>
<br>
	-aOPTIM_GCC="-mcpu=30F6011 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"<br>
<br>
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\gld\p30f6011.gld"<br>
<br>
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libp30F6011-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"<br>
<br>
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"<br>
<br>
	-aPIC_REF="30f6011"<br>
<br>
	-aGenerateTraceInfo=0<br>
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
...........<br>
<br>
### Writing main<br>
<br>
### Writing header file mika_types.h<br>
<br>
.<br>
<br>
### Writing header file mika.h<br>
<br>
### Writing source file mika.c<br>
<br>
### Writing header file mika_private.h<br>
<br>
.<br>
<br>
### Writing header file autobuild.h<br>
<br>
### Writing source file mika_main.c<br>
<br>
.<br>
<br>
### TLC code generation complete.<br>
<br>
### Creating project marker file: rtw_proj.tmw<br>
<br>
### Evaluating PostCodeGenCommand specified in the model<br>
<br>
<br>
<br>
Companie =<br>
<br>
<br>
<br>
     ''<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
----------------------------------------------------<br>
<br>
Embedded Coder for dsPIC V0.96b(13-Feb-2008) for Matlab R2007b.<br>
<br>
Licence Accorded to Demonstration Version - <br>
<br>
<br>
<br>
<br>
<br>
informations available at  <a href="/">http://archive.kerhuel.eu</a> <br>
<br>
<br>
<br>
.<br>
<br>
### Processing Template Makefile: C:\MyToolBox\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Wrapping unrecognized make command (angle brackets added)<br>
<br>
###    &lt;C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake&gt;<br>
<br>
### in default batch file<br>
<br>
### Creating mika.mk from C:\MyToolBox\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Successful completion of Real-Time Workshop build procedure for model: mika<br>
<br>
&gt;&gt;</div>
</article>

<article class="forum-post" id="p221">
<header><strong>barryforever</strong><time datetime="2008-02-18 12:50 UTC">2008-02-18 12:50 UTC</time></header>
<h3>Re: Some help needed : Error while compiling</h3>
<div class="forum-post-body">in RTW it get compiled very well but what about the hex file generation while getting compiled<br>
<br>
I dont see any..<br>
<br>
<br>
<br>
I tried compiling using mplab by connecting to matlab i received a error ..</div>
</article>

<article class="forum-post" id="p226">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-18 19:47 UTC">2008-02-18 19:47 UTC</time></header>
<h3>Re: Some help needed : Error while compiling</h3>
<div class="forum-post-body">I suggest to compile from simulink (matlab)<br>
<br>
<br>
<br>
to get your .hex file, uncheck the "generate code only", see post : <a href="/forum/topic/89/">viewtopic.php?f=1&amp;t=89#p225</a></div>
</article>

