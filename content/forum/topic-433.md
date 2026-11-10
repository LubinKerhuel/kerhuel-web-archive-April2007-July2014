---
title: "PTfile not found"
url: "/forum/topic/433/"
archiveKind: "topic"
---
# PTfile not found

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1670">
<header><strong>schloudara</strong><time datetime="2011-08-23 11:51 UTC">2011-08-23 11:51 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
This is my first attempt to get started with the dsblock set. <br>
<br>
<br>
<br>
I'm running Matlab R2010.a 32bit and installed the C30 and C32 compiler as well as the dsblockset. That worked out fine.<br>
<br>
<br>
<br>
Then I wanted to create a new simulink model and draged the blocks "configure model" and "compile for dspic" as well as the "Master block" in a new window. Looking at the worksspace there occured the error:<br>
<br>
<br>
<br>
TimeStep was undefined and is set to : 0.001<br>
<br>
System target file set to dspic.tlc<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
Model configured...<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PNumber of I/O PINs used : 0<br>
<br>
T&gt;&gt; <br>
<br>
<br>
<br>
I want to use the whole thing on a PIC32MX795F512L (USB starter kit II)<br>
<br>
<br>
<br>
Therefore I think I need the C32 Compiler. Can I therefore ignore this error, because it refers to dsPIC30F?<br>
<br>
<br>
<br>
Plz Help, I'm new to this... Thanks so far</div>
</article>

<article class="forum-post" id="p1671">
<header><strong>schloudara</strong><time datetime="2011-08-23 11:59 UTC">2011-08-23 11:59 UTC</time></header>
<h3>Re: PTfile not found</h3>
<div class="forum-post-body">When I select PIC32MX795F512L in the "Master block" new error occure:<br>
<br>
<br>
<br>
Tfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
Tfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PNumber of I/O PINs used : 0<br>
<br>
TTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC30F\libpchoose_dsPIC_Target-coff.a<br>
<br>
PNumber of I/O PINs used : 0<br>
<br>
TTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libp32MX795F512L-coff.a<br>
<br>
directory not found : C:\Program Files (x86)\Microchip\mplabc32\v2.01\pic32mx\include<br>
<br>
      --&gt; corrected : find in C:\PROGRA~2\MICROC~1\mplabc32\v2.01\pic32mx\include<br>
<br>
Warning: The dialog of 'untitled/Master' is being closed because a mask parameter has been changed <br>
<br>
&gt; In C:\Program Files (x86)\DSPIC Blockset\blocks\dsPIC_Set_Dialog_PopUp_Param.p&gt;dsPIC_Set_Dialog_PopUp_Param at 57<br>
<br>
  In C:\Program Files (x86)\DSPIC Blockset\blocks\dsPIC_MASTER_callback_InitMask.p&gt;dsPIC_MASTER_callback_InitMask at 269<br>
<br>
file not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
directory not found : C:\Program Files (x86)\Microchip\MPLAB C30\include<br>
<br>
      --&gt; corrected : find in C:\PROGRA~2\MICROC~1\MPLABC~2\include<br>
<br>
Tfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
PNumber of I/O PINs used : 0<br>
<br>
Tfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTfile not found : C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpchoose_dsPIC_Target-coff.a<br>
<br>
PTT&gt;&gt; <br>
<br>
<br>
<br>
Is this ok?<br>
<br>
<br>
<br>
Greetings</div>
</article>

<article class="forum-post" id="p1672">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-23 12:57 UTC">2011-08-23 12:57 UTC</time></header>
<h3>Re: PTfile not found</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
Choose a dsPIC within the MASTER block. <br>
<br>
Until you select a chip, the default pic usd is called "choose_dsPIC". Obviously compiler definition files for that chip does not exist !<br>
<br>
Anyway, thanks for the bug report, I might try to help user for that.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1673">
<header><strong>schloudara</strong><time datetime="2011-08-23 14:33 UTC">2011-08-23 14:33 UTC</time></header>
<h3>Re: PTfile not found</h3>
<div class="forum-post-body">Thanks for the fast answer!!<br>
<br>
<br>
<br>
However the error, as I wrote before, occured also as I choose the right PIC.<br>
<br>
<br>
<br>
Anyways I just ignored it and wrote a simple program and everything worked out fine.<br>
<br>
<br>
<br>
Big thanks for this blockset, it is very useful!!</div>
</article>

