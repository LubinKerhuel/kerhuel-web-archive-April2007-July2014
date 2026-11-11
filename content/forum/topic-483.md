---
title: "Error(s) encountered while building model &quot;ADC6&quot;"
url: "/forum/topic/483/"
archiveKind: "topic"
---
# Error(s) encountered while building model &quot;ADC6&quot;

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1843">
<header><strong>nammta</strong><time datetime="2012-03-05 09:47 UTC">2012-03-05 09:47 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
This is my first attempt to get started with the block set. <br>
<br>
<br>
<br>
I'm running Matlab R2010.a 32bit and installed the C30 compiler as well as the blockset. That worked out fine.<br>
<br>
<br>
<pre><code>### Real-Time Workshop build procedure for model: 'CAN_a_30f4012' aborted due to an error.
***** Solver Mode change from Auto to SingleTasking (this mode allows single rate and multirate). See help to get the difference with the MultiTasking mode which is now supported by the blockset *****
new GMAKE path : E:\MATLAB\bin\win32\gmake
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f3012.gld
      --&gt; corrected : find in --script=C:\PROGRA~1\MICROC~1\mplabc30\v3.30\support\dsPIC30F\gld\p30f3012.gld
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.30\lib\libpic30-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f3012-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.30\lib\dsPIC30F\libp30f3012-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libc-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.30\lib\libc-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libm-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.30\lib\libm-coff.a
directory not found : C:\Program Files\Microchip\mplabc30\v3.30\include
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.30\include
PTModel configured...
Target definition is different from that in the model. Updating target according to the new definition.  The following parameters were updated: 
	ModelReferenceCompliant
### Starting Real-Time Workshop build procedure for model: Servo_ADC
### Generating code into build directory: C:\Documents and Settings\minhnam\Desktop\install_dsPIC_R2010a\Servo_ADC_dspic\sources
PTPTPNumber of I/O PINs used : 2
TPTTPTPNumber of I/O PINs used : 2
TTTTTPTPNumber of I/O PINs used : 2
TPNumber of I/O PINs used : 2
TTPTPTTTPTPNumber of I/O PINs used : 2
TPNumber of I/O PINs used : 2
TTPTPTTTPNumber of I/O PINs used : 2
TPNumber of I/O PINs used : 2
TPNumber of I/O PINs used : 2
TTPTPTTWarning: Source 'Servo_ADC/ADC Input' specifies that its sample time (-1) is back-inherited. You should explicitly specify the
sample time of sources. You can disable this diagnostic by setting the 'Source block specifies -1 sample time' diagnostic to
'none' in the Sample Time group on the Diagnostics pane of the Configuration Parameters dialog box. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using the run-time
data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'Servo_ADC/Constant1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the run-time
data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'Servo_ADC/Gain'. 
### Invoking Target Language Compiler on Servo_ADC.rtw
### Using System Target File: C:\Documents and Settings\minhnam\Desktop\install_dsPIC_R2010a\dspic\dspic.tlc
### Loading TLC function libraries
.....
### Initial pass through model to cache user defined code
..
### Caching model source code
.................
### Writing main
--- Multi Rate &amp; Single Tasking implementation
.
### Writing header file Servo_ADC.h
### Writing header file Servo_ADC_types.h
.
### Writing header file rtwtypes.h
### Writing source file Servo_ADC.c
### Writing header file Servo_ADC_private.h
.
### Writing source file Servo_ADC_data.c
### Writing header file autobuild.h
.
### Writing source file Servo_ADC_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.7c(09-Jan-2012) for Matlab R2010a.
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
Check updates and new informations at :  http://archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Documents and Settings\minhnam\Desktop\install_dsPIC_R2010a\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Servo_ADC.mk which is generated from C:\Documents and Settings\minhnam\Desktop\install_dsPIC_R2010a\dspic\dspic_pic30_gcc.tmf is up to date
### Building Servo_ADC: "E:\MATLAB\bin\win32\gmake" -f Servo_ADC.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IE:\MATLAB/simulink/include -IE:\MATLAB/extern/include -IE:\MATLAB/rtw/c/src -IE:\MATLAB/rtw/c/ert -IE:\MATLAB/rtw/c/src/ext_mode/common -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2\Servo_ADC_dspic\sources -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2 -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2\examples   -I C:\PROGRA~1\MICROC~1\mplabc30\v3.30\include    Servo_ADC_data.c 
''pic30-gcc  -c -mcpu=30f3012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IE:\MATLAB/simulink/include -IE:\MATLAB/extern/include -IE:\MATLAB/rtw/c/src -IE:\MATLAB/rtw/c/ert -IE:\MATLAB/rtw/c/src/ext_mode/common -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2\Servo_ADC_dspic\sources -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2 -IC:\DOCUME~1\minhnam\Desktop\INSTAL~2\examples   -I C:\PROGRA~1\MICROC~1\mplabc30\v3.30\include    Servo_ADC_main.c 
Servo_ADC_main.c:34: error: syntax error before numeric constant 
Servo_ADC_main.c: In function '_FICD': 
Servo_ADC_main.c:36: error: syntax error before '{' token 
gmake: *** [Servo_ADC_main.o] Error 255 
### Real-Time Workshop build procedure for model: 'Servo_ADC' aborted due to an error.</code></pre></div>
</article>

<article class="forum-post" id="p1844">
<header><strong>LubinKerhuel</strong><time datetime="2012-03-05 10:01 UTC">2012-03-05 10:01 UTC</time></header>
<h3>Re: Error(s) encountered while building model &amp;quot;ADC6&amp;quot;</h3>
<div class="forum-post-body">The _FICD register were renamed to _ICD is some compilers version (3.25, 3.30).<br>
<br>
<br>
<br>
Latest compiler version set this register name to _FICD.<br>
<br>
Please <a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1406&amp;dDocName=en010065">download latest C30 compiler</a> (3.31) and perhaps remove others compilers version to make sure the blockset will choose automatically the latest one.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1845">
<header><strong>nammta</strong><time datetime="2012-03-05 15:57 UTC">2012-03-05 15:57 UTC</time></header>
<h3>Re: Error(s) encountered while building model &amp;quot;ADC6&amp;quot;</h3>
<div class="forum-post-body">Thanks for the fast answer!!<br>
<br>
 :D  :D  :D</div>
</article>

<article class="forum-post" id="p1869">
<header><strong>nammta</strong><time datetime="2012-03-29 16:09 UTC">2012-03-29 16:09 UTC</time></header>
<h3>Re: Error(s) encountered while building model &amp;quot;ADC6&amp;quot;</h3>
<div class="forum-post-body">how fix this ?<br>
<blockquote>Error: File: C:\Documents and Settings\minhnam\Desktop\Vidu\USB6_dspic\sources\tlc\dsPIC_main.tlc Line: 27 Column: 12<br>
<br>
Attempt to call a non-function value: FcnMultiTaskingMain<br>
<br>
Error: File: C:\Documents and Settings\minhnam\Desktop\Vidu\USB6_dspic\sources\tlc\dsPIC_main.tlc Line: 27 Column: 31<br>
<br>
Values of NULL type cannot be expanded</blockquote></div>
</article>

