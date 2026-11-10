---
title: "genMakefileAndBuild"
url: "/forum/topic/74/"
archiveKind: "topic"
---
# genMakefileAndBuild

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

13 message(s) · archive en lecture seule

<article class="forum-post" id="p154">
<header><strong>Membre</strong><time datetime="2008-01-19 17:04 UTC">2008-01-19 17:04 UTC</time></header>
<div class="forum-post-body">Encounter error msg below when compile/build even with simple block. Please advice<br>
<br>
<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'try3'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "try3". :(</div>
</article>

<article class="forum-post" id="p155">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-19 18:09 UTC">2008-01-19 18:09 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi, could you upload on the forum the simulink file that generate that error ?</div>
</article>

<article class="forum-post" id="p156">
<header><strong>Membre</strong><time datetime="2008-01-20 06:36 UTC">2008-01-20 06:36 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Thanks for the reply. Me actually trying "my first example" as illustrated in example.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/6-try3.mdl">Pièce jointe : try3.mdl</a></p>
</article>

<article class="forum-post" id="p157">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-20 23:06 UTC">2008-01-20 23:06 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi Aunanshi<br>
<br>
<br>
<br>
The mdl file 'try3.mdl' compile successfully on my system. Could you provide more details on the error : Which matlab version are you using, Is real time workshop and Real Time Workshop Embedded Coder installed on your system,  Which version of the C30 compiler are you using ; Is this the complete error message ? In which directory is it installed ... <br>
<br>
<br>
<br>
Also, you could browse this forum; some topics are about the installation of the blockset. If you do not find a solution, please ask again.</div>
</article>

<article class="forum-post" id="p160">
<header><strong>Membre</strong><time datetime="2008-01-22 02:10 UTC">2008-01-22 02:10 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">C:\Program Files\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f3012.gld: No such file or directory <br>
<br>
gmake: *** [..\../try3.coff] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'try3' aborted due to an error.<br>
<br>
<br>
<br>
error msg as above.<br>
<br>
<br>
<br>
me using matlab 7.5.0 (R2007b)<br>
<br>
MPLAB_C30_v3_02-studentEdition   &lt;== could this be the problem, if yes where can get usable version(Free or trial version) ? <br>
<br>
<br>
<br>
I also saw forum posted by Mr.Peter. You replying "The toolbox must not be installed in the matlab directory or subdirectory. Make sure you did not install the toolbox inside the matlab directory or sudirectory ! "  which toolbox are you refering to? <br>
<br>
<br>
<br>
Regards,<br>
<br>
Nanshi</div>
</article>

<article class="forum-post" id="p161">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-22 09:06 UTC">2008-01-22 09:06 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi Nanshi,<br>
<blockquote><header class="quote-author">Citation : [adresse e-mail retirée]</header>MPLAB_C30_v3_02-studentEdition &lt;== could this be the problem, if yes where can get usable version (Free or trial version) ? </blockquote><br>
This is not the problem: the student version of the C30_V3_02 work with the dsPIC blockset !<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : [adresse e-mail retirée]</header>I also saw forum posted by Mr.Peter. You replying "The toolbox must not be installed in the matlab directory or subdirectory. Make sure you did not install the toolbox inside the matlab directory or subdirectory !" which toolbox are you refering to? </blockquote><br>
I am refering to the dsPIC blockset only. The one you download from this website.<br>
<br>
<br>
<br>
sumedhk get similar error : a missing gld file was reported. could you try the solution explained on the topic : <a href="/forum/topic/73/">Issues in dsPIC 30f6014 compiling : Missing gld &amp; DCI Periph</a>  :<br>
<blockquote><header class="quote-author">Citation : Lubin Kerhuel</header>rtw_alt_pathname('C:\Program Files\Microchip\MPLAB C30\support\gld')<br>
<br>
If you do not get C:\PROGRA~1\MICROC~1\MPLABC~1, you will have to change the short path in Simulink :<br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; DsPIC options </blockquote><br>
<br>
Let me know then...</div>
</article>

<article class="forum-post" id="p163">
<header><strong>Membre</strong><time datetime="2008-01-26 06:20 UTC">2008-01-26 06:20 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi Lubin, <br>
<br>
Compile successful after changed MPLABC~1 to MPLABC~2, all 6 of them from <br>
<br>
        Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; DsPIC options<br>
<br>
<br>
<br>
Thanks a lot!!!<br>
<br>
<br>
<br>
Regards,<br>
<br>
nanshi</div>
</article>

<article class="forum-post" id="p1237">
<header><strong>bassplayer142</strong><time datetime="2010-05-11 19:38 UTC">2010-05-11 19:38 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">I am having the same problem but the previous fix is not working.  I'm using the 2007b matlab and have rtw and rtw embedded installed.  I get the error as follows<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'try1'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "try1".<br>
<br>
<br>
<br>
It may be important to note that I am running win7 64-bit but I am working with a 32-bit matlab.  It is also important to note that my matlab is installed in c:/program files (x86)/... The following is the paths that I have where the problem may lie.  Thank you for any help.  I also don't know why there is four different path directories for the 5th path (ldlibpic)<br>
<br>
<br>
<br>
(this order below) Gmake file/optimisation/ldflags/ldpictype/ldlibpic/picincludes/picref/compiler path<br>
<br>
<br>
<br>
C:\PROGRA~2\MATLAB\R2007b\bin\win32\gmake<br>
<br>
<br>
<br>
-mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2<br>
<br>
<br>
<br>
-t --report-mem -Map ../untitled.map --heap 0  -cref<br>
<br>
<br>
<br>
  -T C:\PROGRA~2\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4011.gld<br>
<br>
<br>
<br>
  C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libp30f4011-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a<br>
<br>
<br>
<br>
  -I C:\PROGRA~2\MICROC~1\MPLABC~2\include<br>
<br>
<br>
<br>
30f4011<br>
<br>
''<br>
<br>
<br>
<br>
<br>
<br>
thanks for any help!</div>
</article>

<article class="forum-post" id="p1238">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-11 23:33 UTC">2010-05-11 23:33 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
try to place the yellow block 'configuration of the model' from the dsPIC library on your model and dbl click on it. It may solve few problems. (anyway, this block will be improved in the next blockset version, not published yet)<br>
<br>
 If problem is not solved,<br>
<br>
<br>
<br>
Check all your path. Copy-past repertory with ~1 in a file browser to see if that directory exist. If not, try to replace ~1 by ~2 and so on until you find the correct directory. <br>
<br>
<br>
<br>
It should not be a problem to use matlab 32bits on windows 64 bits. I successfully tested this configuration.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1239">
<header><strong>bassplayer142</strong><time datetime="2010-05-12 02:59 UTC">2010-05-12 02:59 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">I tried the things you said to no avail.  First off whenever I make changes and try them, when I go back to the dsPIC path options, they are all defaulted back to their original paths.  Secondly, I checked them and only one is path is broken as seen below.<br>
<br>
<br>
<br>
  -T C:\PROGRA~2\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f4011.gld<br>
<br>
<br>
<br>
should infact be <br>
<br>
<br>
<br>
  -T C:\PROGRA~2\MICROC~1\MPLABC~2\support/gld\p30f4011.gld<br>
<br>
<br>
<br>
I checked with another users comment and tried this command also<br>
<br>
<br>
<br>
rtw_alt_pathname('C:\PROGRA~2\MICROC~1\MPLABC~2\support\gld\')<br>
<br>
<br>
<br>
but in the command window it said this which leads me to believe that is not the problem.  It also says this below when I double click the configure model button.<br>
<br>
<br>
<br>
C30 Compiler found<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4011-coff.a<br>
<br>
      --&gt; corrected : find in C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libp30f4011-coff.a<br>
<br>
Model configured...<br>
<br>
<br>
<br>
<br>
<br>
Thanks a lot though for the quick reply<br>
<br>
<br>
<br>
edit:  I should also note that I only need the hex file which I will then upload to the pickit2.  Just wondering if that may simplify the process by getting rid of the c code files.</div>
</article>

<article class="forum-post" id="p1240">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-12 19:54 UTC">2010-05-12 19:54 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : bassplayer142</header>C30 Compiler found<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f4011-coff.a<br>
<br>
--&gt; corrected : find in C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libp30f4011-coff.a<br>
<br>
Model configured...</blockquote><br>
<br>
Current version (V3.2b) has a problem here : the path is not updated properly and the error comes back. I'll send an updated verision by email for testing. Let me know if that's Ok.</div>
</article>

<article class="forum-post" id="p1241">
<header><strong>bassplayer142</strong><time datetime="2010-05-12 22:13 UTC">2010-05-12 22:13 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Unfortunately it still gives the same error.  Although the path problem you talked about did disappear.  This is what the end of the command prompt says when it errors out.<br>
<br>
<br>
<br>
### Processing Template Makefile: C:\Program Files (x86)\MATLAB\dspic\dspic_pic30_gcc.tmf<br>
<br>
-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating try1.mk from C:\Program Files (x86)\MATLAB\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building try1: "C:\PROGRA~2\MATLAB\R2007b\bin\win32\gmake" -f try1.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0<br>
<br>
''pic30-gcc  -c -mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~2\MATLAB\R2007b/simulink/include -IC:\PROGRA~2\MATLAB\R2007b/extern/include -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\PROGRA~2\MATLAB\R2007b\try1_dspic\sources -IC:\PROGRA~2\MATLAB\R2007b -IC:\Users\chris\Desktop -IC:\PROGRA~2\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    try1_data.c <br>
<br>
''pic30-gcc  -c -mcpu=30f4011 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~2\MATLAB\R2007b/simulink/include -IC:\PROGRA~2\MATLAB\R2007b/extern/include -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~2\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\PROGRA~2\MATLAB\R2007b\try1_dspic\sources -IC:\PROGRA~2\MATLAB\R2007b -IC:\Users\chris\Desktop -IC:\PROGRA~2\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    try1_main.c <br>
<br>
try1_main.c: In function '_FICD': <br>
<br>
try1_main.c:41: error: syntax error before '{' token <br>
<br>
gmake: *** [try1_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'try1' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
<br>
<br>
<br>
<br>
I have also attached the model I was using.  thanks!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/344-try1.mdl">Pièce jointe : try1.mdl</a></p>
</article>

<article class="forum-post" id="p1242">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-13 11:23 UTC">2010-05-13 11:23 UTC</time></header>
<h3>Re: genMakefileAndBuild</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I could not reproduce that bug. <br>
<br>
Thus, it may be your version of the C30 compiler. Which version are you using ? Could you update it with the latest version from the microchip website ?</div>
</article>

