---
title: "Syntax error in compilation"
url: "/forum/topic/244/"
archiveKind: "topic"
---
# Syntax error in compilation

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p944">
<header><strong>Beni</strong><time datetime="2009-08-19 10:24 UTC">2009-08-19 10:24 UTC</time></header>
<div class="forum-post-body">Hi!<br>
<br>
<br>
<br>
I have an compilation error when try to build the examples:<br>
<pre><code>### Invoking Target Language Compiler on ledsample.rtw
	tlc
	-r
	C:\0beni\matlabwork\ledsample_dspic\sources\ledsample.rtw
	C:\0beni\matlabwork\dspic\dspic.tlc
	-OC:\0beni\matlabwork\ledsample_dspic\sources
	-IC:\0beni\matlabwork\dspic
	-IC:\0beni\matlabwork\blocks
	-IC:\0beni\matlabwork\ledsample_dspic\sources\tlc
	-IC:\0beni\Programok\MATLAB\R2006a\rtw\c\tlc\mw
	-IC:\0beni\Programok\MATLAB\R2006a\rtw\c\tlc\lib
	-IC:\0beni\Programok\MATLAB\R2006a\rtw\c\tlc\blocks
	-IC:\0beni\Programok\MATLAB\R2006a\rtw\c\tlc\fixpt
	-IC:\0beni\Programok\MATLAB\R2006a\stateflow\c\tlc
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
	-aForceParamTrailComments=0
	-aGenerateComments=1
	-aIgnoreCustomStorageClasses=1
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
	-aCombineOutputUpdateFcns=0
	-aSuppressErrorStatus=0
	-aERTCustomFileBanners=0
	-aLogVarNameModifier="rt_"
	-aGenerateFullHeader=1
	-aGenerateSampleERTMain=0
	-aMatFileLogging=0
	-aMultiInstanceERTCode=0
	-aPurelyIntegerCode=0
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
	-aGMAKE_PLACE="C:\0beni\Programok\MATLAB\R2006a\rtw\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2 -fno-short-double"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f4013.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~1\lib\dsPIC30F\libp30f4013-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~1\include"
	-aPIC_REF="30f4013"
	-aGCCPATH=""
	-p10000
<wbr>
Error: File: execstring Line: 1 Column: 23
Unterminated string
Error: File: execstring Line: 1 Column: 26
syntax error
C30 Compiler found
C30 Compiler found</code></pre><br>
<br>
I figured out that \ should be \\ and between the " " there should be no whitespace or it's a syntax error..<br>
<br>
-aGMAKE_PLACE="C:\0beni\Programok\MATLAB\R2006a\rtw\bin\win32\gmake"<br>
<br>
-aOPTIM_GCC="-mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2 -fno-short-double"<br>
<br>
<br>
<br>
i use matlab r2006. Where can I set the optim_gcc and the other parameters, or how can i solve that problem?<br>
<br>
regards,<br>
<br>
Beni</div>
</article>

<article class="forum-post" id="p945">
<header><strong>Beni</strong><time datetime="2009-08-19 10:39 UTC">2009-08-19 10:39 UTC</time></header>
<h3>Re: Syntax error in compilation</h3>
<div class="forum-post-body">Hi!<br>
<br>
<br>
<br>
Ok I found the solution:<br>
<br>
<br>
<br>
I have to set at<br>
<br>
Simulation ==&gt; Configuration Parameters.. ==&gt; Real-Time Workshop ==&gt; DsPIC options<br>
<br>
the path variables / to //<br>
<br>
ex.:<br>
<br>
C:\Programs\MATLAB\R2006a\rtw\bin\win32\gmake<br>
<br>
change to:<br>
<br>
C:\\Programs\\MATLAB\\R2006a\\rtw\\bin\\win32\\gmake<br>
<br>
<br>
<br>
and it complies well.<br>
<br>
<br>
<br>
regards,<br>
<br>
Beni</div>
</article>

