---
title: "fuzzy logic"
url: "/forum/topic/156/"
archiveKind: "topic"
---
# fuzzy logic

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p514">
<header><strong>salemimoh</strong><time datetime="2008-09-15 08:16 UTC">2008-09-15 08:16 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
 I have tried to simulate a controller of the speed of a motor using fuzzy logic. After developing the model  in MATLAB and transfer it to MPLAB V8.15a and building it.   All went good. But when i fired the program into the DSPIC30F6014 and i tried to run it, it stops. I then run it in step by step using animate, it gave  me the following error message. Is this due of shortage of program memory or what ? If this is the case, is it due to the number of rules implemented in the fuzzier (25 rules which is about the right number of rules to get good control) which makes the program too long so that it could not be accomodated into the programming memory? <br>
<br>
 By the way, i tried to run the program in the MPLAB simulator and it did not work either.<br>
<br>
So could you please advise.<br>
<br>
 <br>
<br>
CORE-E0011: Trap due to unimplemented RAM or PSV memory access, occurred from instruction at 0x000688<br>
<br>
CORE-E0001: Trap due to stack error, occurred from instruction at 0x000688<br>
<br>
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688<br>
<br>
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688<br>
<br>
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688<br>
<br>
CORE-W0008: Software Reset Instruction called at PC=0x002f16</div>
</article>

<article class="forum-post" id="p515">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-15 17:27 UTC">2008-09-15 17:27 UTC</time></header>
<h3>Re: PIC32MX360</h3>
<div class="forum-post-body">Support for PIC 32 device is started.<br>
<br>
An example for the PIC32 starter kit is available here : <a href="/forum/topic/138/#p425">viewtopic.php?f=1&amp;t=138&amp;p=425&amp;hilit=starter#p425</a><br>
<br>
<br>
<br>
I get stuck on a problem relative to interrupt with the Output Compare peripheral. I ave to get back on that problem.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p558">
<header><strong>salemimoh</strong><time datetime="2008-10-10 07:57 UTC">2008-10-10 07:57 UTC</time></header>
<h3>Re: PIC32MX360</h3>
<div class="forum-post-body">Dear Lubbin,<br>
<br>
I am trying to develop a simulink simple model using PIC32, but unfortunately i get the following message:<br>
<br>
[<span style="color:#ff4000">color=#FF4000]process_begin: CreateProcess(NULL, pic30-gcc -c -mcpu=32MX360F512L -O3 -fschedule-insns -fschedule-insns2 -O -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\DOCUME~1\Dell\MYDOCU~1\MATLAB\TEST1_~1\sources -IC:\DOCUME~1\Dell\MYDOCU~1\MATLAB -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc -I C:\PROGRA~1\MICROC~1\MPLABC~2\include dsPIC_OutputCompare_Interrupt.c, ...) failed.</span> <br>
<br>
make (e=2): The system cannot find the file specified.  <br>
<br>
gmake: *** [dsPIC_OutputCompare_Interrupt.o] Error 2 [/color]<br>
<br>
### Real-Time Workshop build procedure for model: 'test1' aborted due to an error.<br>
<br>
How can solve this  dsPIC_OutputCompare_Interrupt.c, ...) failed.  problem.</div>
</article>

<article class="forum-post" id="p561">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-13 18:43 UTC">2008-10-13 18:43 UTC</time></header>
<h3>Re: PIC32MX360</h3>
<div class="forum-post-body">I started the support for PIC32. <br>
<br>
It works for simple peripheral (see example for the PIC 32 KIT)<br>
<br>
<br>
<br>
However, I stopped the development process because of problems with interrupt (in particular with Output compare peripheral)<br>
<br>
I will re-start the investigation later on...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p577">
<header><strong>salemimoh</strong><time datetime="2008-10-15 20:54 UTC">2008-10-15 20:54 UTC</time></header>
<h3>Re: PIC32MX360</h3>
<div class="forum-post-body">that is exactly what the message says</div>
</article>

<article class="forum-post" id="p578">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-15 20:57 UTC">2008-10-15 20:57 UTC</time></header>
<h3>Re: PIC32MX360</h3>
<div class="forum-post-body">Look at this topic : <a href="/forum/topic/142/#p483">viewtopic.php?f=8&amp;t=142&amp;p=483&amp;hilit=PIC32#p483</a></div>
</article>

