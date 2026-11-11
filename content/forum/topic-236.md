---
title: "Error in Compiling Model from demo"
url: "/forum/topic/236/"
archiveKind: "topic"
---
# Error in Compiling Model from demo

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p901">
<header><strong>chad</strong><time datetime="2009-07-22 04:18 UTC">2009-07-22 04:18 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I am trying to compile my first model from your demo <a href="/wiki/animation-compiling-your-first-model/">http://archive.kerhuel.eu/wiki/Animation_Co ... irst_model</a>    and keep getting the error:<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'chad'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "chad".<br>
<br>
<br>
<pre><code>C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
### Starting Real-Time Workshop build procedure for model: chad
### Generating code into build directory: C:\Users\Chad\Documents\MATLAB\chad_dspic\sources
PNumber of I/O PINs used : 1
TT### Invoking Target Language Compiler on chad.rtw
	tlc
	-r
	C:\Users\Chad\Documents\MATLAB\chad_dspic\sources\chad.rtw
	C:\Users\Chad\Desktop\install_dsPIC_R2007b\dspic\dspic.tlc
	-OC:\Users\Chad\Documents\MATLAB\chad_dspic\sources
	-IC:\Users\Chad\Desktop\install_dsPIC_R2007b\dspic
	-IC:\Users\Chad\Desktop\install_dsPIC_R2007b\blocks
	-IC:\Users\Chad\Documents\MATLAB\chad_dspic\sources\tlc
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
	-aOPTIM_GCC="-mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\PIC24F\gld\p24fJ128GA010.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\PIC24F\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="24fJ128GA010"
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
.............
### Writing main
.
### Writing header file chad_types.h
### Writing header file chad.h
### Writing source file chad.c
.
### Writing header file chad_private.h
### Writing source file chad_data.c
.
### Writing header file autobuild.h
### Writing source file chad_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V0.99g(08-Jul-2009) for Matlab R2007b.
<wbr>
<wbr>
Licence Accorded to  Demonstration Version
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://archive.kerhuel.eu
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
Check updates and new informations at :  archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Users\Chad\Desktop\install_dsPIC_R2007b\dspic\dspic_pic30_gcc.tmf
### chad.mk which is generated from C:\Users\Chad\Desktop\install_dsPIC_R2007b\dspic\dspic_pic30_gcc.tmf is up to date
### Building chad: .\chad.bat
<wbr>
C:\Users\Chad\Documents\MATLAB\chad_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  
<wbr>
C:\Users\Chad\Documents\MATLAB\chad_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f chad.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Users\Chad\Documents\MATLAB\chad_dspic\sources -IC:\Users\Chad\Documents\MATLAB -IC:\Users\Chad\Desktop -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    chad_data.c 
In file included from c:/program files/microchip/mplab c30/bin/bin/../../support/peripheral_24F/timer.h:35, 
                 from chad_private.h:47, 
                 from chad_data.c:28: 
c:/program files/microchip/mplab c30/bin/bin/../../support/peripheral_24F/GenericTypeDefs.h:53: error: syntax error before '(' token 
gmake: *** [chad_data.o] Error 255 
### Real-Time Workshop build procedure for model: 'chad' aborted due to an error.
C30 Compiler found
C30 Compiler found</code></pre><br>
<br>
I checked I am using the latest version C30 v3.12.  I am using MATLAB 2007b.  Why can't it compile without error?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Chad</div>
</article>

<article class="forum-post" id="p902">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-22 07:27 UTC">2009-07-22 07:27 UTC</time></header>
<h3>Re: Error in Compiling Model from demo</h3>
<div class="forum-post-body">Hello Chad,<br>
<br>
<br>
<br>
Does the models in the example folder compile ?<br>
<br>
Could you upload the model you tried to compile ?  (it seems it is not an example)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p904">
<header><strong>chad</strong><time datetime="2009-07-25 02:26 UTC">2009-07-25 02:26 UTC</time></header>
<h3>Re: Error in Compiling Model from demo</h3>
<div class="forum-post-body">Curiously, dsPIC_33f_Explorer16.mdl gave pathing error because it was looking for a Matlab &gt; R2009a folder, while I have R2007b.  I got it working by creating a R2009a folder and copying and pasting folders from the R2007b folder into it.  <br>
<br>
<br>
<br>
The chad.mdl I made from the tutorial still wont compile though, so I uploaded it here.  The Matlab messages might mean a syntax error in a header file.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/253-chad.mdl">Pièce jointe : chad.mdl</a></p>
</article>

<article class="forum-post" id="p911">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-26 17:38 UTC">2009-07-26 17:38 UTC</time></header>
<h3>Re: Error in Compiling Model from demo</h3>
<div class="forum-post-body">Hi Chad,<br>
<br>
<br>
<br>
This model compiles just fine with matlab 2007b.<br>
<br>
I attached the obtained .hex file.<br>
<br>
<br>
<br>
Anyway, if you have path error, you may add the yellow block "Configure Model for dsPIC" in the Simulink Configuration subblocks of the dsPIC blockset and click on it. This block check and configure if necessary the differents paths.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/254-chad.hex">Pièce jointe : chad.hex</a></p>
</article>

