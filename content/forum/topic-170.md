---
title: "Simulink access"
url: "/forum/topic/170/"
archiveKind: "topic"
---
# Simulink access

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p594">
<header><strong>lelis</strong><time datetime="2008-10-30 08:14 UTC">2008-10-30 08:14 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
l would like to congratulate you your excellent job. You documentation, examples and Wiki implementation is clear and well made. <br>
<br>
I’ve just installed yesterday your new version of blocs-set. The installation has been corrected but the new dsPIC blocs are no “accessible” in the Simulink window. <br>
<br>
There is message after installation:<br>
<br>
Installation of Real Time Embedded Coder for dsPIC is finished!<br>
<br>
  - Checking that C30 PIC24 and/or dsPIC are installed on your system :<br>
<br>
&gt;&gt;!pic30-lm<br>
<br>
Microchip MPLAB C30 License Manager Version v3.00 (Build Date Feb 28 2007). <br>
<br>
Copyright (c) 2005 Microchip Technology Inc. All rights reserved. <br>
<br>
This demo-version license has 37 days remaining after today. <br>
<br>
  - checking that C32 PIC32 is also installed on your system :<br>
<br>
&gt;&gt;!pic32-gcc -v<br>
<br>
'pic32-gcc' is not recognized as an internal or external command, <br>
<br>
operable program or batch file. <br>
<br>
 - go to  <a href="/">archive.kerhuel.eu</a>  to check installation procedure<br>
<br>
 - YOU MUST INSTALL THE INDEPENDANT VERSION OF THE C30 COMPILER AVAILABLE ON THE  MICROCHIP WEBSITE <br>
<br>
 The C30 version included in the MPLAB distribution (v8.10) will produce a error like "gld file not found"<br>
<br>
 - Check installation : start the script CompileAllModels in the examples directory. <br>
<br>
It will compile all the model contained in the example directory (for dsPIC and PIC24 ;<br>
<br>
 make sure you install both compiler : for dsPIC and PIC24)  <br>
<br>
I’m using Student version of C30 and R2008 version 7.6 of Matlab.<br>
<br>
<br>
<br>
Thanks for your help.<br>
<br>
Lelis</div>
</article>

<article class="forum-post" id="p595">
<header><strong>lelis</strong><time datetime="2008-10-30 08:20 UTC">2008-10-30 08:20 UTC</time></header>
<h3>Re: Simulink access</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
There is also additional warmomg:<br>
<br>
<br>
<br>
<span style="color:#8080ff">Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt;<br>
<br>
dsPIC_ConfigRTWOption at 100<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;<br>
<br>
Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 153<br>
<br>
  In uiopen at 196[/i]</span><br>
<br>
<br>
<br>
Thanks<br>
<br>
<br>
<br>
lelis</div>
</article>

<article class="forum-post" id="p596">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-30 09:31 UTC">2008-10-30 09:31 UTC</time></header>
<h3>Re: Simulink access</h3>
<div class="forum-post-body">Hi Lelis,<br>
<br>
<br>
<br>
I do not see the problem. (coule not reproduce it)<br>
<br>
check that you did not install the blockset inside the Matlab directory (it may cause problems)<br>
<br>
Check the matlab path. The blockset'sroot directory, block subdirectory and dspic subdirectory must have been added to the matlab path.<br>
<br>
<br>
<br>
Lubin</div>
</article>

