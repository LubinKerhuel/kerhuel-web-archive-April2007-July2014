---
title: "Teething problems - PIC32"
url: "/forum/topic/142/"
archiveKind: "topic"
---
# Teething problems - PIC32

Forum : [bug reports](/forum/#forum-8)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p438">
<header><strong>gdiana</strong><time datetime="2008-07-05 11:55 UTC">2008-07-05 11:55 UTC</time></header>
<div class="forum-post-body">I am trying to evaluate your "free" blockest using Matlab 2007b and am experiencing some teething problems. I am using the simple Servo_Sinus.mdl to find my feet and get started.<br>
<br>
<br>
<br>
Problem - C32 Compiler: When I build I get the following;<br>
<br>
<br>
<br>
<span style="color:#0000ff"><em><strong>Servo_Sinus_main.c:30: error: unknown value for configuration setting 'FPLLODIV': 'DIV_526' gmake: *** [Servo_Sinus_main.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'Servo_Sinus' aborted due to an error.</strong></em></span><br>
<br>
<br>
<br>
This is what appears in "Servo_Sinus_main.c"<br>
<br>
<span style="color:#ff8000">#pragma config FPLLMUL = MUL_15, FPLLIDIV = DIV_1, FPLLODIV = DIV_526, FWDTEN = OFF<br>
<br>
#pragma config POSCMOD = XT, FNOSC = PRIPLL, FPBDIV = DIV_1</span><br>
<br>
<br>
<br>
This seems to be a simple typo problem and should read <span style="color:#ff0000">'FPLLODIV': 'DIV_256'</span>. <br>
<br>
<br>
<br>
Am I able to fix this? When I made the correction myself (in Servo_Sinus_main.c) and run the Servo_Sinus.bat file all appears to work ok and without error. I get the Servo_Sinus.elf and Servo_Sinus.hex in the example directory after manually running the bat file.<br>
<br>
<br>
<br>
Kind regards<br>
<br>
<br>
<br>
<br>
<br>
Greg Diana</div>
</article>

<article class="forum-post" id="p439">
<header><strong>LubinKerhuel</strong><time datetime="2008-07-07 21:41 UTC">2008-07-07 21:41 UTC</time></header>
<h3>Re: Teething problems</h3>
<div class="forum-post-body">Hello Greg,<br>
<br>
<br>
<br>
I noticed that you also got a problem with the C30 installation. Did you solve the problem? Could you share the solution if there is some trick to apply while installing C30 ?<br>
<br>
Feel free to register and to then edit the "installation page" of the website's wiki.<br>
<br>
<br>
<br>
About the C32, there was a typo error in the software. I just solved it so the problem will be solved in the next blockset release (0.98e). I 'll try to update the website very shortly with this new release. (If you need it shortly, let me know).<br>
<br>
<br>
<br>
Thanks for reporting that bug. (Activating PLL may resolve the bug on your the actual blockset version (0.98d))<br>
<br>
<br>
<br>
Be aware of the fact that PIC32 are curently only experimental and few peripheral are supported right now. (I have a problem with the Output Compare Interrupt and the development process stopped there!)<br>
<br>
<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p440">
<header><strong>gdiana</strong><time datetime="2008-07-08 20:18 UTC">2008-07-08 20:18 UTC</time></header>
<h3>Re: Teething problems</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thank you, much appreciated, there is no particular hurry, and I am sure you have a lot on your plate. I will play around with the dsPIC30 stuff first. Got Servo_Sinus to compile, download and run on the Microchip dsPICDEM 2 demonstration board running with a 40 pin DIL dsPIC30F4011 (<a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=2519&amp;param=en025319&amp;page=wwwdsPICDSCDemo">http://www.microchip.com/stellent/idcpl ... PICDSCDemo</a>). <br>
<br>
I imported to MPLAB (<span style="color:#0000ff"><em><strong>ver 8.10  note ver 8.14 beta now available and works fine too!</strong></em></span>) downloaded and it ran as you said it would.<br>
<br>
<br>
<br>
However I first had to change the NIPS as well as the Oscillator Mode (XT_PLL8) parameters in the dsPIC Master Block, Real Time - Quartz Tab  to conform to the dsPICDEM 2 board setup configuration. Initially it would just not run, with your standard parameter set, until I fathomed out what the problem was. This might be useful to others!<br>
<br>
<br>
<br>
As far as the C30 compiler problem I initially penned down and subsequently removed. This was simply due to a change in the way Microchip have now organised the PIC24 and dsPIC 16 bit C30 Compilers. Previously, I understand, there was only a single / combined C30 compiler for both. However MPLAB (8.10) only installs  the C32 compiler. One has to download and install the C30 compilers from Microchip (student versions) but there are 3 versions namely;<br>
<br>
1 One C30 for the PIC24 MCUs<br>
<br>
2 One C30 for the dsPIC DSCs<br>
<br>
3 A single upgrade for both 1 and 2.<br>
<br>
<br>
<br>
I incorrectly installed the PIC24 C30 compiler (1) and tried to compile Sinus-Servo using a dsPIC device and MATLAB gave a licence error message as I was compiling the wrong device with the wrong compiler. I subsequently installed the dsPIC C30 compiler (2), along with the upgrade (3) and resolved the problem. One of those Read The Manual problems!<br>
<br>
<br>
<br>
Also please note that the PIC24 (1) and dsPIC C30 (2) compilers appear to write to the same directories so that only one may be installed at a time! Weird but apparantly true. Within MPLAB 8.10 there is only a single <span style="color:#ff0000"><em><strong>Microchip C30 Toolsuite</strong></em></span> defined under the Set Language Locations in the Project Menu. <span style="color:#ff0000"><em><strong>This might create problems!</strong></em></span><br>
<br>
<br>
<br>
However I learned some maybe interesting things that others might want to take note of;<br>
<br>
<br>
<br>
1 Installing MPLAB 8.10 does not provide the option to automatically modify the WINDOWS PATH. This has to be done manually. I found I could not just use START-&gt;RUN-&gt;CMD to open a DOS CMD Window and edit and change the path in the autoexec.bat file. When I did this, and ran it, it indeed showed, in the DOS CMD Window, that the DOS PATH had changed, but MATLAB did not pick it up via the WINDOWS PATH! (If I ran !PATH from the MATLAB command line it was unchanged and different from that in the DOS CMD Window). Even exiting and restarting MATLAB <span style="color:#ff0000"><em><strong>DID NOT</strong></em></span> solve the problem. Even rebooting did not work! It sounded similar to the problem that other forum member was experiencing!<br>
<br>
<br>
<br>
2 When installing the dsPIC C30 (2) compiler and upgrade (3) it was noted that the WINDOWS PATH was changed, when selecting this install option, and that MATLAB picked this up immediately.<br>
<br>
<br>
<br>
3 To solve the problem I right clicked on My Computer, clicked on Properties, clicked on the Advanced Tab and then opened the Environment Variables under Startup and Recovery.<br>
<br>
<br>
<br>
Under Systems variables I moved the slider until the Path variable showed and simply double clicked on the Path Variable, allowing me to edit and change the WINDOWS PATH. This I did and simply added (<span style="color:#0000ff"><em><strong>C:\Program Files\Microchip\MPLAB C30\bin;C:\Program Files\Microchip\MPLAB C32\bin</strong></em></span>) to the path and exited. I rebooted to make sure and PRESTO it worked just fine. It appears modifying the path via My Computer is best.<br>
<br>
<br>
<br>
I am sorry if I have been so long winded but I hope this might be of some help to others. I just noticed that you requested a reply on the "installation page". Please forgive but I will modify a little later when I am "fresh".<br>
<br>
<br>
<br>
Kind regards<br>
<br>
<br>
<br>
<br>
<br>
Greg Diana</div>
</article>

<article class="forum-post" id="p441">
<header><strong>LubinKerhuel</strong><time datetime="2008-07-08 21:27 UTC">2008-07-08 21:27 UTC</time></header>
<h3>Re: Teething problems</h3>
<div class="forum-post-body">Hi Greg,<br>
<br>
<br>
<br>
Thanks for all theses information. I noticed theses facts (C32 not added in the windows path when installing with MPLAB, but option is available if installing C32 with its standalone installer.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : gdiana</header><br>
Also please note that the PIC24 (1) and dsPIC C30 (2) compilers appear to write to the same directories so that only one may be installed at a time! Weird but apparantly true. Within MPLAB 8.10 there is only a single Microchip C30 Toolsuite defined under the Set Language Locations in the Project Menu. This might create problems!</blockquote><br>
PIC24 and dsPIC C30 compiler install to the same directories. PIC24 and dsPIC C30 compiler are the same binary software. Libraries are different for the PIC24 and the C30 version. Installing both will add both libraries in different subdirectory thus making you able to compile for either dsPIC 30f or PIC24 chips.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : gdiana</header>you requested a reply on the "installation page"</blockquote><br>
Information is easier found on the wiki than on the forum. That may help many others. A Version Short and Simple to resume all theses information would be great on the wiki ;-)<br>
<br>
If you are willing to add examples for the dsPICDEM2 on the wiki, it could be great. So feel free to ask. (Not sure that you can create new pages on the wiki...)<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p483">
<header><strong>Anonyme</strong><time datetime="2008-08-31 01:15 UTC">2008-08-31 01:15 UTC</time></header>
<h3>Re: Teething problems</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>Hello Greg,<br>
<br>
<br>
<br>
...<br>
<br>
<br>
<br>
Be aware of the fact that PIC32 are curently only experimental and few peripheral are supported right now. (I have a problem with the Output Compare Interrupt and the development process stopped there!)<br>
<br>
<br>
<br>
<br>
<br>
Lubin</blockquote><br>
<br>
Did you ever resolve the Output Compare Interupt problem? I am also having a similar problem in that the Output Compare Interrupt always happens at the beginning of the timer instead of the output Compare register offset.</div>
</article>

<article class="forum-post" id="p484">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-31 12:15 UTC">2008-08-31 12:15 UTC</time></header>
<h3>Re: Teething problems</h3>
<div class="forum-post-body">I did not get back yet on the interrupt problem I had.<br>
<br>
<br>
<br>
so, still stuck. I still hope that someone could help.<br>
<br>
<br>
<br>
Lubin</div>
</article>

