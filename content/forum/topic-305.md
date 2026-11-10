---
title: "Error while compiling &quot;dsPIC_33f_Explorer16.mdl&quot;"
url: "/forum/topic/305/"
archiveKind: "topic"
---
# Error while compiling &quot;dsPIC_33f_Explorer16.mdl&quot;

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1246">
<header><strong>Darlington</strong><time datetime="2010-06-03 08:33 UTC">2010-06-03 08:33 UTC</time></header>
<div class="forum-post-body">Dear Mr Kerhuel,<br>
<br>
<br>
<br>
First of all I would like to thank you for sharing with everyone the work you did. It is very helpful. <br>
<br>
<br>
<br>
I am a beginner with MATLAB/Simulink for dsPIC. So my first try was to compile one of your model, the dsPIC_33f_Explorer16.mdl, with the toolbox you provide. Unfortunately I encountered the following problem while compiling (Error using ==&gt; genMakefileAndBuild at 1070):<br>
<br>
<em><br>
<br>
(...)<br>
<br>
### Processing Template Makefile: C:\Documents and Settings\Simulator\Bureau\Camille\Installations\dspic\dspic_pic30_gcc.tmf<br>
<br>
-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating dsPIC_33f_Explorer16.mk from C:\Documents and Settings\Simulator\Bureau\Camille\Installations\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building dsPIC_33f_Explorer16: "C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0<br>
<br>
''pic30-gcc  -c -mcpu=33fJ256GP710 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\DOCUME~1\SIMULA~2\Bureau\Camille\TESTCA~2\DSPIC_~1\sources -IC:\DOCUME~1\SIMULA~2\Bureau\Camille\TESTCA~2 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_33f_Explorer16_main.c <br>
<br>
<strong>dsPIC_33f_Explorer16_main.c:41: error: syntax error before '&amp;' token <br>
<br>
dsPIC_33f_Explorer16_main.c: In function '_FICD': <br>
<br>
dsPIC_33f_Explorer16_main.c:43: error: syntax error before '{' token <br>
<br>
dsPIC_33f_Explorer16_main.c:50: error: syntax error before 'dsPIC_33f_Explorer16_SetEventsForThisBaseStep' <br>
<br>
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.</strong><br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
&gt;&gt; </em><br>
<br>
<br>
<br>
I tried to check the syntax in the generated code but found nothing wrong.<br>
<br>
I am using MATLAB R2007b. I also tried to compile from MPLAB IDE but the problem is the same.<br>
<br>
I checked my configuration parameters but I probably forgot something.<br>
<br>
<br>
<br>
Could you please let me know if this problem is familiar to you, and if you have any clue to solve it?<br>
<br>
<br>
<br>
Regards.</div>
</article>

<article class="forum-post" id="p1267">
<header><strong>Darlington</strong><time datetime="2010-06-30 13:17 UTC">2010-06-30 13:17 UTC</time></header>
<h3>Re: Error while compiling &amp;quot;dsPIC_33f_Explorer16.mdl&amp;quot;</h3>
<div class="forum-post-body">Hi,<br>
<br>
Do you really have no clue about this error message?<br>
<br>
Thanks.</div>
</article>

