---
title: "build error in GenericTypeDefs.h"
url: "/forum/topic/432/"
archiveKind: "topic"
---
# build error in GenericTypeDefs.h

Forum : [bug reports](/forum/#forum-8)

14 message(s) · archive en lecture seule

<article class="forum-post" id="p1658">
<header><strong>resodad</strong><time datetime="2011-08-17 17:36 UTC">2011-08-17 17:36 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Is this a bug?<br>
<br>
the attached model generates this error when generating code:<br>
<pre><code>..\../GenericTypeDefs.h:64:22: error: expected identifier before '(' token </code></pre><br>
<br>
and the offending line of GenericTypeDefs.h is:<br>
<pre><code>typedef enum _BOOL { FALSE = 0, TRUE } BOOL;    /* Undefined size */</code></pre><br>
which looks OK.<br>
<br>
<br>
<br>
I am using C32 V2.00 compiler<br>
<br>
<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/433-SD_Datalogger.mdl">Pièce jointe : SD_Datalogger.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/434-Matlab%20warnings%20upon%20opening%20model.txt">Pièce jointe : Matlab warnings upon opening model.txt</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/435-Matlab%20output%20from%20build.txt">Pièce jointe : Matlab output from build.txt</a></p>
</article>

<article class="forum-post" id="p1659">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-17 20:03 UTC">2011-08-17 20:03 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
The problem appears for 24fj chips : see forum post <a href="/forum/topic/325/#p1299">here</a> <br>
<br>
It has been corrected for 24Fj chips : the dsPIC blockset now generate its own GenericTypeDefs.h file.<br>
<br>
I will do the same correction for 32f Chips.<br>
<br>
<br>
<br>
The workaround is just to modify the file GenericTypeDefs.h like : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt; // typedef enum _BOOL { FALSE = 0, TRUE } BOOL;    /* Undefined size */
 typedef enum _BIT { CLEAR = 0, SET } BIT;
</code></pre><br>
It should fix the problem. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1661">
<header><strong>resodad</strong><time datetime="2011-08-18 11:48 UTC">2011-08-18 11:48 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Thanks Lubin, I already tried that; now the error is "chased" to a new line of a different header file that depends on BOOL:<br>
<pre><code>In file included from ..\../CustomSD.c:8:0: 
..\../FSIO.h:272:5: error: expected specifier-qualifier-list before 'BOOL' 
gmake: *** [CustomSD.o] Error 1 
### Real-Time Workshop build procedure for model: 'SD_Datalogger' aborted due to an error.</code></pre><br>
John</div>
</article>

<article class="forum-post" id="p1662">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-18 13:19 UTC">2011-08-18 13:19 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">I did not use code where the BOOL type were required.<br>
<br>
Thus I have no solution for that. There might be more usefull information on Microchip forum for this.<br>
<br>
<br>
<br>
Anyway, I would be glad to get the final word. It is weird that this BOOL enumeration does not work. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1663">
<header><strong>resodad</strong><time datetime="2011-08-18 17:01 UTC">2011-08-18 17:01 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Lubin,  Microchip tech support looked into it but could not find the problem. John</div>
</article>

<article class="forum-post" id="p1664">
<header><strong>resodad</strong><time datetime="2011-08-18 17:49 UTC">2011-08-18 17:49 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Lubin, maybe this is a clue? I tried replacing<br>
<pre><code>typedef enum _BOOL { FALSE = 0, TRUE } BOOL;    /* Undefined size */</code></pre><br>
with<br>
<pre><code>typedef enum _BOOL { NO_FALSE = 0, YES_TRUE } BOOL;</code></pre><br>
and the result was:<br>
<pre><code>sources/SD_Datalogger.c: In function 'SD_Datalogger_initialize':
sources/SD_Datalogger.c:195:19: error: 'T1_INT_PRIOR_0' undeclared (first use in this function)</code></pre><br>
etc. I t looks like it got past the GenericTypeDefs and FSIO headers. Was it getting stuck on key words FALSE and TRUE?<br>
<br>
Now it's not finding the timer configuration variables...<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1665">
<header><strong>resodad</strong><time datetime="2011-08-19 11:59 UTC">2011-08-19 11:59 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Lubin,<br>
<br>
Are my files being executed out of order?<br>
<br>
<br>
<br>
see this post on a microchip forum where there was a duplicate #define FALSE:<br>
<br>
<a href="http://www.microchip.com/forums/m522926.aspx">http://www.microchip.com/forums/m522926.aspx</a><br>
<br>
John</div>
</article>

<article class="forum-post" id="p1666">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-19 12:45 UTC">2011-08-19 12:45 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
The best might be to modify the generated code within MPLAB X until it's working. Thus trying the microchip forum's solution with MPLAB and the generated code. Then finding a trick to make it works from simulink straight.<br>
<br>
It's difficult to help you more on this.<br>
<br>
However, could you post the c source code for the SD : CustomSD.c etc... I guess this is microchip's template ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1667">
<header><strong>resodad</strong><time datetime="2011-08-19 16:47 UTC">2011-08-19 16:47 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Lubin,  No, there is no solution on microchip forum for this. The post I referred to had duplicate definitions, and that is not my case.<br>
<br>
CustomSD.c is written by my colleague here to manage file init/open/close/write commands:<br>
<pre><code>#include &lt;p32xxxx.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "FSconfig.h"
#include "HardwareProfile.h"
#include "GenericTypeDefs.h"
#include "FSIO.h"
<wbr>
#define NumRetries 10
<wbr>
FSFILE * filePtr;
<wbr>
<wbr>
unsigned char FS_init_loop(void){
    unsigned char i;
    for (i=0; i &lt; NumRetries; i++){
    if(FSfinit()==0)  return 1;
    return 0;    
    }
}
<wbr>
unsigned char FSopen(char *u1){
    filePtr = FSfopen( u1,FS_WRITE);
    if (filePtr != NULL) {
        return 1;
    }
    else return 0;  
}
<wbr>
void FSclose(void){
    FSfclose(filePtr);
}
<wbr>
unsigned char FSprint(unsigned int u1){
    char y1;
    y1 = FSfprintf(filePtr, "AN0= %u%c%c", u1, 0x0D, 0x0A);
    if (y1 &gt; 0){
        return 1;
    }
    else return 0;
}
</code></pre></div>
</article>

<article class="forum-post" id="p1726">
<header><strong>resodad</strong><time datetime="2011-10-11 14:57 UTC">2011-10-11 14:57 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Lubin and all:<br>
<br>
I have found a clue about this problem. please note:<br>
<br>
1. attachment SD_Datalogger2.mdl contains NO CUSTOM CODE.<br>
<br>
There is no build error when the MATLAB working folder is set correctly to the same location when the .mdl file is saved.<br>
<br>
HOWEVER, the same file produces the GenericTypeDefs error if the MATLAB working folder is set one folder above.<br>
<br>
<br>
<br>
2. attachment SD_Datalogger3.mdl does contain CUSTOM CODE. That is the only difference. Custom code is incorporated via &gt;Simulation&gt;Configuration Parameters&gt;Code Generation&gt;Custom Code&gt; Include Directories and ...&gt;Source Files.<br>
<br>
This file produces the GenericTypeDefs error even if the MATLAB working folder is set correctly.<br>
<br>
Please see if you can duplicate this.<br>
<br>
<br>
<br>
I suspect the paths of the included files are the source of the trouble.<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/447-SD_Datalogger2.mdl">Pièce jointe : SD_Datalogger2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/448-SD_Datalogger3.mdl">Pièce jointe : SD_Datalogger3.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/449-CustomSD.c">Pièce jointe : CustomSD.c</a></p>
</article>

<article class="forum-post" id="p1741">
<header><strong>resodad</strong><time datetime="2011-11-22 14:49 UTC">2011-11-22 14:49 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Hi Lubin and all,<br>
<br>
I am still very stuck on this problem.  Please confirm that you can duplicate the problem (#2 above).<br>
<br>
the error is:<br>
<br>
"<br>
<br>
...GenericTypeDefs.h:65:22: error: expected identifier before '(' token <br>
<br>
"<br>
<br>
But there is nothing wrong with the code in this file. It is Microchip sourced and proven.<br>
<br>
<br>
<br>
Do I have all the source files and header files in the right locations?<br>
<br>
Am I missing a file?<br>
<br>
Do I have a duplicate definition?<br>
<br>
<br>
<br>
I have tried different arrangements of included source code and include directories.<br>
<br>
<br>
<br>
I have tried this using several versions of Microchip compilers and MPLAB and different versions of Matlab.<br>
<br>
Currently I am using <br>
<br>
MATLAB R2011a<br>
<br>
MPLAB IDE v8.76<br>
<br>
C32 compiler v2.01<br>
<br>
and<br>
<br>
Embedded Coder for dsPIC V3.7(08-Oct-2011)<br>
<br>
<br>
<br>
I am attaching everything.<br>
<br>
<br>
<br>
Can you please help?<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/452-myFolder.zip">Pièce jointe : myFolder.zip</a></p>
</article>

<article class="forum-post" id="p1774">
<header><strong>resodad</strong><time datetime="2012-01-05 19:57 UTC">2012-01-05 19:57 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Microchip Tech Support says:<br>
<br>
"<br>
<br>
I think the issue is that you are including the GenericTypeDefs after rtwtypes.h, and there the FALSE and TRUE are defined.\<br>
<br>
So FALSE is replaced with (0U), so the parsing fails.<br>
<br>
You should try to include the timer.h before the rest of your own files.<br>
<br>
"<br>
<br>
<br>
<br>
I tried following this suggestion, but I'm not sure I'm doing it right. All my attempts resulted in errors.<br>
<br>
<br>
<br>
I moved the c file names to:<br>
<br>
Simulation &gt; Configuration Parameters &gt; Simulation Target &gt; Custom Code &gt; Source File (under Include Custom c code in generated:)<br>
<br>
and moved the include directories to this page as well, and the simple model (turn on LED) compiled without error, but a more complicated model (data log to SD card) had the same GenericTypeDefs.h error.<br>
<br>
<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1807">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-17 11:02 UTC">2012-01-17 11:02 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Hello John,<br>
<br>
<br>
<br>
I could not spend too much time on this specific problem.<br>
<br>
Interfacing with other driver might be difficult.<br>
<br>
However, here is my finding:<br>
<br>
<br>
<br>
You copied two files :<br>
<br>
GenericTypeDefs.h<br>
<br>
timer.h<br>
<br>
in the Include folder that you include that are already included within the compiling process. Including theses files creates an error. (Are theses the correct ones ? )<br>
<br>
<br>
<br>
I still get an error, but I think compiling process goes slightly better :<br>
<pre><code>### Writing main
--- Multi Rate &amp; Single Tasking implementation
.
### Writing header file SD_Datalogger5.h
.
### Writing header file SD_Datalogger5_types.h
### Writing header file rtwtypes.h
.
### Writing source file SD_Datalogger5.c
### Writing header file SD_Datalogger5_private.h
.
### Writing source file SD_Datalogger5_data.c
### Writing header file autobuild.h
.
### Writing source file SD_Datalogger5_main.c
### TLC code generation complete.
### Creating HTML report file SD_Datalogger5_codegen_rpt.html
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
Check updates and new informations at :  archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\M91449\Perso\RTWdsPIC\dspic\pic32_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating SD_Datalogger5.mk from C:\M91449\Perso\RTWdsPIC\dspic\pic32_gcc.tmf
### Building SD_Datalogger5: "C:\PROGRA~1\MATLAB\R2011A~1\bin\win64\gmake" -f SD_Datalogger5.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    ..\../CustomSD.c 
..\../CustomSD.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    C:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1/FSIO.c 
C:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1/FSIO.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    C:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1/SD-SPI.c 
C:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1/SD-SPI.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    SD_Datalogger5_data.c 
SD_Datalogger5_data.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    SD_Datalogger5_main.c 
SD_Datalogger5_main.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2011A~1/simulink/include -IC:\PROGRA~1\MATLAB\R2011A~1/extern/include -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2011A~1/rtw/c/src/ext_mode/common -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\SD_Datalogger5_dspic\sources -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\Microchip\Include -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\MDDFIL~1 -IC:\M91449\Perso\RTWdsPIC\Developpements\Forum\resodad_john\myFolder\SDtroubleshooting\..\MICROC~1\Include\MDDFIL~1   -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include -IC:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include\PERIPH~1    SD_Datalogger5.c 
SD_Datalogger5.c:1:0: warning: Compiler option (forward propagate) ignored due to lite-mode limitations 
" ================================================================" 
"*** Embedded Target for dsPIC by Lubin KERHUEL - http://archive.kerhuel.eu" 
" | Licence Accorded to &amp;&amp;               Licence Name          &amp;&amp;|" 
" |                     &amp;&amp;               Mailcontact           &amp;&amp;|"	     
" |          Companie : &amp;&amp;               Companie              &amp;&amp;|"  
" |                     &amp;&amp;               CompanieAddress1      &amp;&amp;|" 
" |                     &amp;&amp;               CompanieAddress2      &amp;&amp;|" 		 
" |                     &amp;&amp;               CompanieAddress3      &amp;&amp;|" 
" |                     &amp;&amp;               CompanieAddress4      &amp;&amp;|"		 		 
" | Financial Service : &amp;&amp;               BuyerName             &amp;&amp;|" 
" | Contact             &amp;&amp;               MailBuyer             &amp;&amp;|" 
" |                     &amp;&amp;               BuyerAddress1         &amp;&amp;|" 
" |                     &amp;&amp;               BuyerAddress2         &amp;&amp;|" 
" |                     &amp;&amp;               BuyerAddress3         &amp;&amp;|" 
" |                     &amp;&amp;               BuyerAddress4         &amp;&amp;|" 
" | Version &amp;&amp;Version&amp;&amp;                       &amp;&amp;  Date       &amp;&amp;  |" 
" | For Matlab &amp;&amp; VerMatlab &amp;&amp; &amp;&amp; Release &amp;&amp;                     |" 
" ================================================================"		  
''pic32-gcc   -t --report-mem -cref  -mprocessor=32MX460F512L -o ..\../SD_Datalogger5.elf  CustomSD.o FSIO.o SD-SPI.o SD_Datalogger5_data.o SD_Datalogger5_main.o SD_Datalogger5.o      C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libm.a C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libm.a 
c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1/../../../../pic32mx/bin/ld.exe: mode elf32pic32mx 
c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1/../../../../pic32mx/lib/crt0.o 
CustomSD.o 
FSIO.o 
SD-SPI.o 
SD_Datalogger5_data.o 
SD_Datalogger5_main.o 
SD_Datalogger5.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)memset.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)strcpy.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)strlen.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)general-exception.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)ctype.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)ctypef.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)strncpy.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)default-general-exception-handler.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)default-bootstrap-exception-handler.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)default-on-reset.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)default-on-bootstrap.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libc.a)default-nmi-handler.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a)int_enable_mv_int_lib.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a)spi_getc_spi2_lib_legacy.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a)spi_open_spi2_lib_legacy.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a)spi_brg_tbl_lib_legacy.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libmchp_peripheral_32MX460F512L.a)int_enable_interrupts_lib.o 
(C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\lib\speed\libm.a)fp32.o 
(c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1\libgcc.a)_udivdi3.o 
(c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1\libgcc.a)_umoddi3.o 
processor.o (c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1/../../../../pic32mx/lib/./proc/32MX460F512L\processor.oCustomSD.o: In function `FS_init_loop': 
CustomSD.c:(.text+0x8): undefined reference to `FSfinit' 
c:/program files (x86)/microchip/mplabc32/v2.01/bin/../lib/gcc/pic32mx/4.5.1/../../../../pic32mx/bin/ld.exe: link errors found, deleting executable `..\../SD_Datalogger5.elf) 
' 
collect2: ld returned 1 exit status 
gmake: *** [..\../SD_Datalogger5.elf] Error 1 
### Build procedure for model: 'SD_Datalogger5' aborted due to an error.
&gt;&gt; </code></pre><br>
Zip file with few changes is attached.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/472-myFolder.zip">Pièce jointe : myFolder.zip</a></p>
</article>

<article class="forum-post" id="p1821">
<header><strong>philippe.1</strong><time datetime="2012-01-27 19:36 UTC">2012-01-27 19:36 UTC</time></header>
<h3>Re: build error in GenericTypeDefs.h</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I don't know if this can help but I had a quick view on the code and I haven't been able to find the FSfinit function in the Microchip application note AN1045 (<a href="http://ww1.microchip.com/downloads/en/AppNotes/01045b.pdf">http://ww1.microchip.com/downloads/en/A ... 01045b.pdf</a>) but I guess this function initialize the card so maybe you should try to replace in teh CustomSD c file at line 18 the FSfinit by FSInit. In my case the code is compiling in both Simulink and in MPlab.<br>
<br>
<br>
<br>
Regards.<br>
<br>
<br>
<br>
Philippe</div>
</article>

