---
title: "erreur"
url: "/forum/topic/258/"
archiveKind: "topic"
---
# erreur

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1013">
<header><strong>enim</strong><time datetime="2009-12-22 10:30 UTC">2009-12-22 10:30 UTC</time></header>
<div class="forum-post-body">bonjour monsieur <br>
<br>
quand j'essaye d'executer le programme servo_ADC il engendre l'erreur suivante: build genmake1138<br>
<br>
voila une copie de mon erreur sur matlab<br>
<br>
merci pour votre comprhénsion<br>
<br>
<br>
<br>
<span style="color:#ff4080"><span style="color:#ff4080"><strong>C30 Compiler found<br>
<br>
Warning: dsPICdrivers.mdl, line 48: block_diagram does not have a parameter named<br>
<br>
'CovForceBlockReductionOff'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 153<br>
<br>
  In uiopen at 196<br>
<br>
Warning: dsPICdrivers.mdl, line 54: block_diagram does not have a parameter named<br>
<br>
'CovExternalEMLEnable'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 153<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt;<br>
<br>
dsPIC_ConfigRTWOption at 107<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;<br>
<br>
Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In C:\Documents and Settings\Administrateur\Bureau\install dspic\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 153<br>
<br>
  In uiopen at 196<br>
<br>
Warning: In instantiating linked block 'Servo_ADC_filter/ADC Input' : Invalid setting in dsPIC :<br>
<br>
ADC10 block (mask) 'ADC Input' for parameter 'OutFormatBitspopup'.<br>
<br>
&gt; In C:\Documents and Settings\Administrateur\Bureau\install dspic\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 153<br>
<br>
  In uiopen at 196<br>
<br>
PTC30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
### Starting Real-Time Workshop build procedure for model: Servo_ADC_filter<br>
<br>
### Generating code into build directory: C:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources<br>
<br>
PPNumber of I/O PINs used : 4<br>
<br>
TPTPTTPNumber of I/O PINs used : 4<br>
<br>
TPNumber of I/O PINs used : 4<br>
<br>
TTTPTPTPTTPNumber of I/O PINs used : 4<br>
<br>
TPTWarning: Source 'Servo_ADC_filter/ADC Input' specifies that its sample time (-1) is<br>
<br>
back-inherited. You should explicitly specify the sample time of sources. You can disable this<br>
<br>
diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the<br>
<br>
Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box.<br>
<br>
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be<br>
<br>
represented exactly using the run-time data type. A small quantization error has occurred. You<br>
<br>
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This<br>
<br>
originated from 'Servo_ADC_filter/Constant1'.<br>
<br>
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be<br>
<br>
represented exactly using the run-time data type. A small quantization error has occurred. You<br>
<br>
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This<br>
<br>
originated from 'Servo_ADC_filter/Gain'.<br>
<br>
### Invoking Target Language Compiler on Servo_ADC_filter.rtw<br>
<br>
	tlc<br>
<br>
	-r<br>
<br>
	C:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources\Servo_ADC_filter.rtw<br>
<br>
	C:\Documents and Settings\Administrateur\Bureau\install dspic\dspic\dspic.tlc<br>
<br>
	-OC:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\install dspic\dspic<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\install dspic\blocks<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources\tlc<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\mw<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\lib<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\blocks<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\fixpt<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\stateflow\c\tlc<br>
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
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake"<br>
<br>
	-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"<br>
<br>
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f3012.gld"<br>
<br>
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\dsPIC30F\libp30f3012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"<br>
<br>
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"<br>
<br>
	-aPIC_REF="30f3012"<br>
<br>
	-aGCCPATH=""<br>
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
.....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
.<br>
<br>
### Caching model source code<br>
<br>
...............<br>
<br>
### Writing main<br>
<br>
### Writing header file Servo_ADC_filter_types.h<br>
<br>
.<br>
<br>
### Writing header file Servo_ADC_filter.h<br>
<br>
### Writing source file Servo_ADC_filter.c<br>
<br>
.<br>
<br>
### Writing header file Servo_ADC_filter_private.h<br>
<br>
### Writing source file Servo_ADC_filter_data.c<br>
<br>
### Writing header file autobuild.h<br>
<br>
.<br>
<br>
### Writing source file Servo_ADC_filter_main.c<br>
<br>
### TLC code generation complete.<br>
<br>
### Evaluating PostCodeGenCommand specified in the model<br>
<br>
<br>
<br>
     ----------------------------------------------------<br>
<br>
     ----------------------------------------------------<br>
<br>
Embedded Coder for dsPIC V3.1(17-Nov-2009) for Matlab R2009a.<br>
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
                     WEBSITE : <a href="/archive-assets/">http://archive.kerhuel.eu/wiki</a><br>
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
Check updates and new informations at :  <a href="/">archive.kerhuel.eu</a> <br>
<br>
     ----------------------------------------------------<br>
<br>
<br>
<br>
.<br>
<br>
### Processing Template Makefile: C:\Documents and Settings\Administrateur\Bureau\install dspic\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Servo_ADC_filter.mk which is generated from C:\Documents and Settings\Administrateur\Bureau\install dspic\dspic\dspic_pic30_gcc.tmf is up to date<br>
<br>
### Building Servo_ADC_filter: .\Servo_ADC_filter.bat<br>
<br>
 <br>
<br>
C:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2008a  <br>
<br>
 <br>
<br>
C:\Documents and Settings\Administrateur\Bureau\examples\Servo_ADC_filter_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2006a\rtw\bin\win32\gmake" -f Servo_ADC_filter.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
Le chemin d'accŠs sp‚cifi‚ est introuvable. <br>
<br>
### Real-Time Workshop build procedure for model</strong>: 'Servo_ADC_filter' aborted due to an error.</span></span></div>
</article>

<article class="forum-post" id="p1014">
<header><strong>LubinKerhuel</strong><time datetime="2009-12-22 11:37 UTC">2009-12-22 11:37 UTC</time></header>
<h3>Re: erreur</h3>
<div class="forum-post-body">essayer de cliquer, avant de compiler sur un block jaune qui permet de configurer le modèle, et corrige les chemins d'accés aux fichiers/compilateurs...</div>
</article>

<article class="forum-post" id="p1016">
<header><strong>enim</strong><time datetime="2009-12-22 15:24 UTC">2009-12-22 15:24 UTC</time></header>
<h3>Re: erreur</h3>
<div class="forum-post-body">bonjour j'ai changé et voila ce qu'il m'ecrit:<br>
<br>
pouvez vous m'aider SVP<br>
<br>
<br>
<br>
<br>
<br>
<span style="color:#ff40bf">### Starting Real-Time Workshop build procedure for model: Servo_ADC_filter<br>
<br>
### Generating code into build directory: C:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources<br>
<br>
PNumber of I/O PINs used : 4<br>
<br>
TTPNumber of I/O PINs used : 4<br>
<br>
TPNumber of I/O PINs used : 4<br>
<br>
TPNumber of I/O PINs used : 4<br>
<br>
TTPTPTWarning: Source 'Servo_ADC_filter/ADC Input' specifies that its sample time (-1) is back-inherited. You should explicitly specify the sample time of<br>
<br>
sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to 'none' in the Sample Time group on the<br>
<br>
Diagnostics pane of the Configuration Parameters dialog box.<br>
<br>
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using the run-time data type. A small<br>
<br>
quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated from<br>
<br>
'Servo_ADC_filter/Constant1'.<br>
<br>
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the run-time data type. A small<br>
<br>
quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated from<br>
<br>
'Servo_ADC_filter/Gain'.<br>
<br>
### Invoking Target Language Compiler on Servo_ADC_filter.rtw<br>
<br>
	tlc<br>
<br>
	-r<br>
<br>
	C:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources\Servo_ADC_filter.rtw<br>
<br>
	C:\Documents and Settings\Administrateur\Bureau\dspic\dspic.tlc<br>
<br>
	-OC:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\dspic<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\blocks<br>
<br>
	-IC:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources\tlc<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\mw<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\lib<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\blocks<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\rtw\c\tlc\fixpt<br>
<br>
	-IC:\Program Files\MATLAB\R2008a\stateflow\c\tlc<br>
<br>
	-aEnforceIntegerDowncast=0<br>
<br>
	-aFoldNonRolledExpr=1<br>
<br>
	-aInlineInvariantSignals=1<br>
<br>
	-aInlineParameters=1<br>
<br>
	-aLocalBlockOutputs=1<br>
<br>
	-aRollThreshold=5<br>
<br>
	-aZeroInternalMemoryAtStartup=0<br>
<br>
	-aZeroExternalMemoryAtStartup=0<br>
<br>
	-aInitFltsAndDblsToZero=0<br>
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
	-aGMAKE_PLACE="C:\Program Files\MATLAB\R2008a\bin\win32\gmake"<br>
<br>
	-aOPTIM_GCC="-mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2"<br>
<br>
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"<br>
<br>
	-aLDPICTYPE="C:\Program Files\Microchip\MPLAB C30\support\dsPIC30F\gld\p30f3012.gld"<br>
<br>
	-aLDLIBPIC="C:\Program Files\Microchip\MPLAB C30\lib\libpic30-coff.a  C:\Program Files\Microchip\MPLAB C30\lib\libp30f3012-coff.a C:\Program Files\Microchip\MPLAB C30\lib\libc-coff.a C:\Program Files\Microchip\MPLAB C30\lib\libm-coff.a"<br>
<br>
	-aPIC_INCLUDES="C:\Program Files\Microchip\MPLAB C30\include"<br>
<br>
	-aPIC_REF="30f3012"<br>
<br>
	-aGCCPATH="'C:\Program Files\Microchip\MPLAB C30\bin\\'"<br>
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
.....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
.<br>
<br>
### Caching model source code<br>
<br>
..............<br>
<br>
### Writing code interface description file codeInfo.mat<br>
<br>
<br>
<br>
### Writing main<br>
<br>
.<br>
<br>
### Writing header file Servo_ADC_filter_types.h<br>
<br>
### Writing header file Servo_ADC_filter.h<br>
<br>
### Writing source file Servo_ADC_filter.c<br>
<br>
.<br>
<br>
### Writing header file Servo_ADC_filter_private.h<br>
<br>
### Writing header file autobuild.h<br>
<br>
.<br>
<br>
### Writing source file Servo_ADC_filter_main.c<br>
<br>
### TLC code generation complete.<br>
<br>
### Evaluating PostCodeGenCommand specified in the model<br>
<br>
<br>
<br>
     ----------------------------------------------------<br>
<br>
     ----------------------------------------------------<br>
<br>
Embedded Coder for dsPIC V3.0b(02-Oct-2009) for Matlab R2008a.<br>
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
                     WEBSITE : <a href="/archive-assets/">http://archive.kerhuel.eu/wiki</a><br>
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
Check updates and new informations at :  <a href="/">archive.kerhuel.eu</a> <br>
<br>
     ----------------------------------------------------<br>
<br>
<br>
<br>
.<br>
<br>
### Processing Template Makefile: C:\Documents and Settings\Administrateur\Bureau\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Creating Servo_ADC_filter.mk from C:\Documents and Settings\Administrateur\Bureau\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building Servo_ADC_filter: .\Servo_ADC_filter.bat<br>
<br>
 <br>
<br>
C:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2008a  <br>
<br>
 <br>
<br>
C:\Documents and Settings\Administrateur\Bureau\Servo_ADC_filter_dspic\sources&gt;"C:\Program Files\MATLAB\R2008a\bin\win32\gmake" -f Servo_ADC_filter.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
C:\Program Files\Microchip\MPLAB C30\bin\\pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2008a/simulink/include -IC:\PROGRA~1\MATLAB\R2008a/extern/include -IC:\PROGRA~1\MATLAB\R2008a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\DOCUME~1\ADMINI~1\Bureau\SERVO_~1\sources -IC:\DOCUME~1\ADMINI~1\Bureau -IC:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc   C:\Program Files\Microchip\MPLAB C30\include    Servo_ADC_filter_main.c <br>
<br>
pic30-coff-gcc: C:\Program: No such file or directory <br>
<br>
pic30-coff-gcc: Files\Microchip\MPLAB: No such file or directory <br>
<br>
pic30-coff-gcc: C30\include: No such file or directory <br>
<br>
gmake: *** [Servo_ADC_filter_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'Servo_ADC_filter' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found</span></div>
</article>

