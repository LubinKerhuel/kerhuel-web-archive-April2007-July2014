---
title: "error building your model Hypersampling"
url: "/forum/topic/234/"
archiveKind: "topic"
---
# error building your model Hypersampling

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p890">
<header><strong>crh</strong><time datetime="2009-07-12 15:41 UTC">2009-07-12 15:41 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
This is the first time that I try to build a model with a PIC32. Till now without any succes and a lot of errors.<br>
<br>
When I try to build your model hypersampling I get the next error:<br>
<br>
<br>
<br>
In file included from dsPIC_32MX460F512L_Explorer16_HyperSampling_main.c:28: <br>
<br>
dsPIC_32MX460F512L_Explorer16_HyperSampling_private.h:33:19: timer.h: No such file or directory <br>
<br>
dsPIC_32MX460F512L_Explorer16_HyperSampling_private.h:37:24: outcompare.h: No such file or directory <br>
<br>
gmake: *** [dsPIC_32MX460F512L_Explorer16_HyperSampling_main.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'dsPIC_32MX460F512L_Explorer16_HyperSampling' aborted due to an error.<br>
<br>
C32 Compiler found<br>
<br>
<br>
<br>
When I try to build my model I get the next error:<br>
<br>
<br>
<br>
C:\Users\Casparus\Documents\MATLAB\Work Pic32\ADC filter OC HW Pic32\ADC_forumkerhuel_OC_HW_Fs30k_PIC32_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2008b\bin\win32\gmake" -f ADC_forumkerhuel_OC_HW_Fs30k_PIC32.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
C:\\PROGRA~1\\MICROC~1\\MPLABC~1\\bin\\pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2008b/simulink/include -IC:\PROGRA~1\MATLAB\R2008b/extern/include -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src/ext_mode/common -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1\ADC_FO~1\sources -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1   -IC:\PROGRA~1\MICROC~1\MPLABC~1\pic32mx\include  -IC:\PROGRA~1\MICROC~1\MPLABC~1\pic32mx\include\peripheral    ADC_forumkerhuel_OC_HW_Fs30k_PIC32_data.c <br>
<br>
process_begin: CreateProcess(NULL, C:\PROGRA~1\MICROC~1\MPLABC~1\bin\pic32-gcc -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2008b/simulink/include -IC:\PROGRA~1\MATLAB\R2008b/extern/include -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src/ext_mode/common -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1\ADC_FO~1\sources -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1 -IC:\PROGRA~1\MICROC~1\MPLABC~1\pic32mx\include -IC:\PROGRA~1\MICROC~1\MPLABC~1\pic32mx\include\peripheral ADC_forumkerhuel_OC_HW_Fs30k_PIC32_data.c, ...) failed. <br>
<br>
<br>
<br>
make (e=2): Het systeem kan het opgegeven bestand niet vinden.  (in English: the system cannot find the file)<br>
<br>
gmake: *** [ADC_forumkerhuel_OC_HW_Fs30k_PIC32_data.o] Error 2 <br>
<br>
### Real-Time Workshop build procedure for model: 'ADC_forumkerhuel_OC_HW_Fs30k_PIC32' aborted due to an error.<br>
<br>
C32 Compiler found<br>
<br>
<br>
<br>
My idea is that there must be somewhere a fundamental mistake, but I do not know where to look.<br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/245-dsPIC_32MX460F512L_Explorer16_HyperSampling.mdl">Pièce jointe : dsPIC_32MX460F512L_Explorer16_HyperSampling.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/246-ADC_forumkerhuel_OC_HW_Fs30k_PIC32.mdl">Pièce jointe : ADC_forumkerhuel_OC_HW_Fs30k_PIC32.mdl</a></p>
</article>

<article class="forum-post" id="p893">
<header><strong>crh</strong><time datetime="2009-07-13 14:16 UTC">2009-07-13 14:16 UTC</time></header>
<h3>Re: error building your model Hypersampling</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
I solved my problem by re-installing the C30 and C32 compilers again.<br>
<br>
No problems anymore with your model Hypersampling.<br>
<br>
But with the attached model (with any kind of  filter), I get the following message (without a filter no problems):<br>
<br>
<br>
<br>
C:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c\dsppinv/pinv_d_rt.c: In function `MWDSP_PINV_D': <br>
<br>
C:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c\dsppinv/pinv_d_rt.c:66: internal compiler error: Segmentation fault <br>
<br>
Please submit a full bug report, <br>
<br>
with preprocessed source if appropriate. <br>
<br>
See <a href="http://support.microchip.com">http://support.microchip.com</a>&gt; for instructions. <br>
<br>
gmake: *** [pinv_d_rt.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'ADC_forumkerhuel_OC_HW_Fs30k_PIC32' aborted due to an error.<br>
<br>
C32 Compiler found<br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/248-ADC_forumkerhuel_OC_HW_Fs30k_PIC32.mdl">Pièce jointe : ADC_forumkerhuel_OC_HW_Fs30k_PIC32.mdl</a></p>
</article>

<article class="forum-post" id="p895">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-13 21:45 UTC">2009-07-13 21:45 UTC</time></header>
<h3>Re: error building your model Hypersampling</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
I open the model (with matlab 2009a) and compile it without problems.<br>
<br>
I attached the .hex file generated.<br>
<br>
<br>
<br>
I was wondering if the time-step is not to fast. at 30Khz, it would be better to use fixed point filter. You may considere using the busy flag port (see master block options)<br>
<br>
<br>
<br>
It seems that the error you get comes from the C compiler. It's is strange as I am using the same C compiler (I use the last version of C32) : <br>
<pre><code>&gt;&gt; !pic30-gcc -v
gcc version 4.0.3 (dsPIC30, Microchip v3_11) Build date: Jul 16 2008 
Microchip Language Tool Shell Version v3_11 (Build date: Jul 16 2008). </code></pre><br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/250-ADC_forumkerhuel_OC_HW_Fs30k_PIC32.hex">Pièce jointe : ADC_forumkerhuel_OC_HW_Fs30k_PIC32.hex</a></p>
</article>

<article class="forum-post" id="p898">
<header><strong>crh</strong><time datetime="2009-07-14 08:49 UTC">2009-07-14 08:49 UTC</time></header>
<h3>Re: error building your model Hypersampling</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
I followed your advises and tried to eliminate every possible fact that could cause an error. I even re-installed the C32 compiler (and a fixed point fillter).<br>
<br>
But always the same error appears:<br>
<br>
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2008b/simulink/include -IC:\PROGRA~1\MATLAB\R2008b/extern/include -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2008b/rtw/c/src/ext_mode/common -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1\ADCFOR~1\ADC_FO~1\sources -IC:\Users\Casparus\DOCUME~1\MATLAB\WORKPI~1\ADCFIL~1\ADCFOR~1 -IC:\PROGRA~1\MATLAB\R2008b\toolbox\dspblks\include -IC:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c   -IC:\PROGRA~1\MICROC~1\MPLABC~2\pic32mx\include  -IC:\PROGRA~1\MICROC~1\MPLABC~2\pic32mx\include\peripheral    C:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c\dsppinv/pinv_d_rt.c <br>
<br>
C:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c\dsppinv/pinv_d_rt.c: In function `MWDSP_PINV_D': <br>
<br>
C:\PROGRA~1\MATLAB\R2008b\toolbox\rtw\dspblks\c\dsppinv/pinv_d_rt.c:66: internal compiler error: Segmentation fault <br>
<br>
Please submit a full bug report, <br>
<br>
with preprocessed source if appropriate. <br>
<br>
See <a href="http://support.microchip.com">http://support.microchip.com</a>&gt; for instructions. <br>
<br>
gmake: *** [pinv_d_rt.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'ADC_forumkerhuel_OC_HW_Fs3k_PIC32' aborted due to an error.<br>
<br>
C32 Compiler found<br>
<br>
<br>
<br>
I use the latest evaluation C32 V 1.05 and Matlab 2008b.<br>
<br>
Without a filter I can build the model.<br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/251-ADC_forumkerhuel_OC_HW_Fs3k_PIC32.mdl">Pièce jointe : ADC_forumkerhuel_OC_HW_Fs3k_PIC32.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/252-ADC_withoutfilter_OC_HW_Fs3k_PIC32.mdl">Pièce jointe : ADC_withoutfilter_OC_HW_Fs3k_PIC32.mdl</a></p>
</article>

<article class="forum-post" id="p899">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-14 09:04 UTC">2009-07-14 09:04 UTC</time></header>
<h3>Re: error building your model Hypersampling</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
I tested the model with matlab 2008b and I get the same error.<br>
<br>
It seems that matlab 2008b generate code that make the compiler to bug. I do not have solution for that.<br>
<br>
<br>
<br>
As the problem is due to the filter block fdatool, you may easily find a workaround : from the fdatool, generate a simulink subsystem with the filter implemented with simple elements , i.e. addition, delay and gain. This should work.<br>
<br>
<br>
<br>
Lubin</div>
</article>

