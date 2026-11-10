---
title: "Support for CAN Module?"
url: "/forum/topic/11/"
archiveKind: "topic"
---
# Support for CAN Module?

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

35 message(s) · archive en lecture seule

<article class="forum-post" id="p13">
<header><strong>malife</strong><time datetime="2007-04-17 06:25 UTC">2007-04-17 06:25 UTC</time></header>
<div class="forum-post-body">I have to say Wow! Shocked this is a really nice blockset, congratulations!<br>
<br>
<br>
<br>
I have a question: is CAN support in the roadmap?<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p16">
<header><strong>LubinKerhuel</strong><time datetime="2007-04-17 21:28 UTC">2007-04-17 21:28 UTC</time></header>
<div class="forum-post-body">Well,<br>
<br>
<br>
<br>
I do not use CAN bus in my project due to its complex electronics.<br>
<br>
Right now, I do not plan to build the CAN blockset since the documentation is very long and that it will take me quite a lot of time to achieve the user interface for all the options available. <br>
<br>
So, depending how many people ask for it, I will read carefully the CAN chapter. But I guess that most people use SPI or I2C bus for small distance communication with fixed ground reference voltage.<br>
<br>
<br>
<br>
Note that the "C function" block is there for you to implement unsupported peripheral (also, for recycling your "old fashion C written" algorithm you are proud of ! )<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p96">
<header><strong>mlove</strong><time datetime="2007-08-08 14:42 UTC">2007-08-08 14:42 UTC</time></header>
<h3>Most projects I do also use CAN</h3>
<div class="forum-post-body">Its worth developing the CAN driver blocks as its is widely used. SPI and I2C are ok for on board devices like A/D etc, but CAN is far superior for noisy enviroments and long cable runs.</div>
</article>

<article class="forum-post" id="p98">
<header><strong>p.erasmus</strong><time datetime="2007-08-11 18:06 UTC">2007-08-11 18:06 UTC</time></header>
<h3>CAN Drivers</h3>
<div class="forum-post-body">Hello Lubin<br>
<br>
<br>
<br>
I would also like to see some CAN modules as CAN is widely used and will be in  the industrie for some years to come.<br>
<br>
I work with CAN intensivly and have a CAN test bench with a couple off CAN nodes on a Bus .<br>
<br>
If it would help you I can help you in testing and running the code generated from the toolbox in realtime for you or supply you with the CAN basics which you may need .<br>
<br>
This is just a offer that could help us to generate the modules for the toolbox.<br>
<br>
<br>
<br>
Best Regards <br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p233">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-19 22:59 UTC">2008-02-19 22:59 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">CAN peripheral is available on current version of the dsPIC blockset. I will write the doccumentation soon.<br>
<br>
ECAN is not available yet. Is anybody interrested by ECAN ?</div>
</article>

<article class="forum-post" id="p481">
<header><strong>Bernard Leak</strong><time datetime="2008-08-26 11:21 UTC">2008-08-26 11:21 UTC</time></header>
<h3>Yes, ECAN, please!</h3>
<div class="forum-post-body">We are very interested indeed in getting an ECAN block working.<br>
<br>
We are using PIC variants which have ECAN but not CAN, and<br>
<br>
that's what we will be offering our customers.<br>
<br>
   Our customers are certainly using CAN (as do we), often with<br>
<br>
the MathWorks CANdb support), and we want to be able to offer<br>
<br>
them CAN in their own models with the fullest possible<br>
<br>
interoperability with (e.g.) CANdb support in MathWorks.<br>
<br>
This will greatly encourage them to become dsPIC block-set<br>
<br>
customers themselves! <br>
<br>
<br>
<br>
Bernard Leak.</div>
</article>

<article class="forum-post" id="p486">
<header><strong>malife</strong><time datetime="2008-09-01 02:30 UTC">2008-09-01 02:30 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Yes I second that. ECAN Please :-)!!</div>
</article>

<article class="forum-post" id="p750">
<header><strong>Ender</strong><time datetime="2009-02-11 18:06 UTC">2009-02-11 18:06 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">One more Lumbin, Thanks. :D</div>
</article>

<article class="forum-post" id="p900">
<header><strong>gladiac</strong><time datetime="2009-07-15 22:13 UTC">2009-07-15 22:13 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Very interested in ECAN. Hope it will come soon.Thanks Lubin!</div>
</article>

<article class="forum-post" id="p916">
<header><strong>bmairs</strong><time datetime="2009-07-27 19:00 UTC">2009-07-27 19:00 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I would also like to vote for supporting ECAN. I have the 33f with ECAN and would like to be able to use it as a block.<br>
<br>
<br>
<br>
It seems like a few different people are looking for this, are you thinking about developing an ECAN block?</div>
</article>

<article class="forum-post" id="p929">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 10:08 UTC">2009-07-30 10:08 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
ECAN has lots of possibility and it is still difficult to start to work on it.<br>
<br>
It's even more difficult now because I'm writing my PhD report and have some change planned in my private life (getting married soon).<br>
<br>
<br>
<br>
Btw, if anyone has knowledge on ECAN and Simulink, I would be happy to discuss about the best way to implement it. How to make ECAN blocks that could provide all ECAN functions (like respond to a specific message...) <br>
<br>
Would it be better to have as many ECAN blocks that there are different functions, of only a few (like CAN blocks)<br>
<br>
<br>
<br>
Any suggestions are welcome.<br>
<br>
I will start to works on it as soon as I can get enough free time.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1022">
<header><strong>bmairs</strong><time datetime="2010-01-11 18:41 UTC">2010-01-11 18:41 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I have currently started work on an ECAN library and corresponding blockset. It would be great to get your input on this, Lubin. The current codebase is available here: <a href="https://github.com/Susurrus/ECAN_dspic">https://github.com/Susurrus/ECAN_dspic</a></div>
</article>

<article class="forum-post" id="p1023">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-12 11:53 UTC">2010-01-12 11:53 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hello, <br>
<br>
<br>
<br>
thanks for sharing this work. <br>
<br>
It would be very interresting to get an ECAN module compatible with the blockset.<br>
<br>
I try to have a close look within few weeks (2 or 3) and provide my comments. <br>
<br>
<br>
<br>
anyway, I wasn't able to clone the git repository, is it open access ? (I get the last zip file of the project)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1024">
<header><strong>bmairs</strong><time datetime="2010-01-12 20:20 UTC">2010-01-12 20:20 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I've fixed the repo. Should be publicly clonable. I'll try and add more documentation to it within the week to clear up some things.</div>
</article>

<article class="forum-post" id="p1073">
<header><strong>bmairs</strong><time datetime="2010-02-06 23:51 UTC">2010-02-06 23:51 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I just wanted to update this thread briefly.<br>
<br>
<br>
<br>
I'm currently stuck on an Embedded MATLAB block issue where it doesn't want to respect an infinite sampling time. After that is fixed, there blockset should be close to if not fully functional.</div>
</article>

<article class="forum-post" id="p1074">
<header><strong>Bobes</strong><time datetime="2010-02-07 20:12 UTC">2010-02-07 20:12 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hello<br>
<br>
that is great news, I am really looking forward to that as I will need ECAN soon to implement in my project (I am now waiting for some parts delivery, and PCB to be made) so in few weeks if not days I will be able to test. In case you need some help testing or so, I hope I will be able to help.<br>
<br>
Thanks a lot<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1083">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-11 16:33 UTC">2010-02-11 16:33 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I didn't get time yet to have a close look into the code.<br>
<br>
(I just moved on 1st February, new job and whatever, but no yet internet home, thus, I am not really in right now )<br>
<br>
<br>
<br>
Anyway, I will try to do it.<br>
<br>
If I can help to find a workaround on the sampling time problem, let me know<br>
<br>
Also, if some part of code needs to be included into the core code of the blockset to works fine, let me know also...<br>
<br>
I just must be careful to maintain compatibility with others peripheral (potential problem may appear with DMA...)</div>
</article>

<article class="forum-post" id="p1139">
<header><strong>Bobes</strong><time datetime="2010-03-19 20:28 UTC">2010-03-19 20:28 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hello,<br>
<br>
are there any news? I have run in some problems with communication (UART is not enough :) ). I would like to try ECAN. Should I try using your code (or try to make mine), or should I wait?<br>
<br>
Thanks<br>
<br>
Kind regards<br>
<br>
Josef<br>
<br>
(sorry for me being inpatient, its just that the project deadline is getting closer)</div>
</article>

<article class="forum-post" id="p1147">
<header><strong>Ender</strong><time datetime="2010-03-31 15:55 UTC">2010-03-31 15:55 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hi,<br>
<br>
What do you mean by UART is not enough ?</div>
</article>

<article class="forum-post" id="p1148">
<header><strong>Bobes</strong><time datetime="2010-03-31 19:13 UTC">2010-03-31 19:13 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">1/ I need to communicate between more than two dsPICs<br>
<br>
2/ I need to send and receive more bytes in one time step (sending is not a problem, but receiving is slightly a problem)</div>
</article>

<article class="forum-post" id="p1151">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-31 22:36 UTC">2010-03-31 22:36 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
Few news from ECAN : Bryant (bmair on the forum) is updating his code for ECAN. This code can be found (see previous post)<br>
<br>
I would advise to use it.<br>
<br>
<br>
<br>
I will do an ECAN block based on his code (with his agreement), anyway, I haven't do it yet (as you may see I just release new blockset supporting matlab 64bits, and working on windows 7 (64 bits) !)<br>
<br>
<br>
<br>
I couldn't give date as I always have to postpone it, but this is in the pipe anyway ! I hope to do it soon !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1152">
<header><strong>Ender</strong><time datetime="2010-04-01 07:09 UTC">2010-04-01 07:09 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Bobes</header>1/ I need to communicate between more than two dsPICs<br>
<br>
2/ I need to send and receive more bytes in one time step (sending is not a problem, but receiving is slightly a problem)</blockquote><br>
<br>
It's very good news from Lubin and Bryant.  :D <br>
<br>
<br>
<br>
But, if your deadline is very short, maybe you better have to build a multipoint with the Uart and some RS422 / RS485 tranceivers.<br>
<br>
If the speed at 921600kbaud/s is enough sure.</div>
</article>

<article class="forum-post" id="p1157">
<header><strong>Bobes</strong><time datetime="2010-04-02 15:12 UTC">2010-04-02 15:12 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">thanks, that is good idea. But I did agree in the beginning of the project to CAN, just did not realize some other things that I have to do, so I am in a bit of stress now :)<br>
<br>
Anyway... I have noticed new toolbox version, thanks for the debugging support! I will start with the ECAN part of my project now, as there is a new uC unit for the BUS. I have less than 2 months now to finish my project and write my diploma work... uff.<br>
<br>
Sorry for the off topic :)<br>
<br>
Thanks once again!</div>
</article>

<article class="forum-post" id="p1158">
<header><strong>Bobes</strong><time datetime="2010-04-03 13:57 UTC">2010-04-03 13:57 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">When I use the "configure ECAN1" block from the "blocks.mdl" I get an error:<br>
<pre><code>The function 'gcb' is not supported by Embedded MATLAB for code generation. See the documentation for eml.extrinsic to learn how you can use this function in simulation.
<wbr>
Function 'Configure ECAN 1/Subsystem5/Embedded MATLAB Function' (#251.109.112), line 4, column 43:
"gcb"</code></pre><br>
There is this:<br>
<pre><code>% Set the MIDE bit
cirxmnsid = bitshift(str2double(get_param(gcb, 'mask_0_rm')),3);
<wbr>
% Set the SID bits
% Split the eid from the sid if necessary
sid = fi(get_param(gcb, 'mask_0'));
eid = 0;
if sid &gt; 2^11-1
    eid = bitshift(sid, -11);
    sid = sis &amp; 2047;
end</code></pre><br>
<br>
The config block from the example is somehow different and I can compile it without error... just there is obviously a difference there...</div>
</article>

<article class="forum-post" id="p1159">
<header><strong>Bobes</strong><time datetime="2010-04-04 22:30 UTC">2010-04-04 22:30 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">somethink strange...<br>
<br>
I am trying to get the ECAN alive (actually I am using just 2.0A)<br>
<br>
when I compile the model in MATLAB, It get stuck after it transmits the message (I have USB-CAN to monitor the bus)<br>
<br>
when I loaded the generated C code into MPLAB and run the debuger mode, or even compiled it in MPLAB, it works as I would expect...<br>
<br>
<br>
<br>
If anyone has any idea where may be the problem.. please let me know<br>
<br>
Thanks!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/316-100403_ECAN_100404.rar">Pièce jointe : 100403_ECAN_100404.rar</a></p>
</article>

<article class="forum-post" id="p1160">
<header><strong>Bobes</strong><time datetime="2010-04-06 20:51 UTC">2010-04-06 20:51 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">new fact:<br>
<br>
I have noticed similar behavior with I2C: my colleague is implementing I2C, He is not using I2C part of the block-set for sending and reading data, but he is using C-call. When we compiled through matlab, there was a problem with reading sequence, but when we used generated c code in MPLAB project, it started working! I do not have the code now on me to post it, but I am starting to think, that the problem may be somewhere in the compilation process, perhaps some argument settings for calling the MPLAB?<br>
<br>
<br>
<br>
One note on block used in Example "Simulink echo": ECAN1 TX<br>
<br>
I think, that the Sample Time has to be set (at least to -1) even when using trigger (I got errors, when I had left it in one value, and used another for some input)</div>
</article>

<article class="forum-post" id="p1161">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-06 21:45 UTC">2010-04-06 21:45 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">You may compare the configuration bits. <br>
<br>
<br>
<br>
What if you compile/run in MPLAB with release mode ?<br>
<br>
I often noticed very weird behavious using MPLAB debugger. Thus, I usually avoid using it.<br>
<br>
<br>
<br>
If more option are required in the blockset for the compilation process, just let me know !<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1162">
<header><strong>Bobes</strong><time datetime="2010-04-06 22:44 UTC">2010-04-06 22:44 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">When I use MPLAB, it works both ways (debug, release)...<br>
<br>
Config Bits:<br>
<br>
There are differences on F80002 and F8000E... not that I do know why, but somehow It does not seem unexpected<br>
<br>
I guess that the problem can be in F80002, as that is the difference between working and not working...<br>
<br>
<br>
<br>
update: I am looking at note 25 - device config:<br>
<br>
F80002 is FSS - Secure Code Segment Configuration Register<br>
<br>
00FF<br>
<br>
FFFF<br>
<br>
<br>
<br>
If I read interpret those values correctly: according to section 25: bit 23-8 are Unimplemented, therefore there should be no difference between 00FF and FFFF hmm.. that is just 16 bits?<br>
<br>
<br>
<br>
as for F8000R - FICD<br>
<br>
FFDF 1111 1111 1101 1111<br>
<br>
FF5F 1111 1111 0101 1111<br>
<br>
5 bit: Jtag off when 0<br>
<br>
7 bit: Reserved, do not use. ?!<br>
<br>
<br>
<br>
<br>
<br>
I am confused :/</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/320-Release_mode.png">Pièce jointe : Release_mode.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/321-Debug_mode.png">Pièce jointe : Debug_mode.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/319-Matlab_direct.png">Pièce jointe : Matlab_direct.png</a></p>
</article>

<article class="forum-post" id="p1163">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-08 19:05 UTC">2010-04-08 19:05 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Let me know how to force first 8 bits of FSS to 0.<br>
<br>
I can't force them adding &amp; 255 into : <br>
<pre><code> _FSS( RSS_NO_RAM &amp; SSS_NO_FLASH &amp; SWRP_WRPROTECT_OFF &amp; 255)</code></pre><br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1164">
<header><strong>Bobes</strong><time datetime="2010-04-10 12:32 UTC">2010-04-10 12:32 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I will try to work that out, but it was done automaticly by MPLAB, when I used It to compile manually.. I did not change anything</div>
</article>

<article class="forum-post" id="p1233">
<header><strong>Bobes</strong><time datetime="2010-05-07 22:48 UTC">2010-05-07 22:48 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">I have some further problems with buffers, I have started using more Rx and Tx blocks, Rx seems fine, but I dont see where to set Rx block for buffer which stores filtered data... Does the filter -&gt; buffer feature work?<br>
<br>
<br>
<br>
on Tx: when I set Tx buffers 1 2 3, and then for three Tx blocks use 1 2 and 3 it sends empty messages (only header, no data), I have all set to one buffer now, and that works, but the messages are not send at the rate they are supposed to. I have no (or couple) errors on the line.<br>
<br>
<br>
<br>
I am using blocks from the example with circ buffer.</div>
</article>

<article class="forum-post" id="p1251">
<header><strong>Bobes</strong><time datetime="2010-06-09 17:00 UTC">2010-06-09 17:00 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Hi I have tried the new version, I have problems with the GCB command which seems not to be implemented in 2009a for embeded matlab. I have tried to work around this (passing the parameter by wire), there is still some small hinch I need to work out (mask = get_param(gcb,sprintf('filter_%d_mask',i)); - this is bit harder, but I am planning to use a vector maybe? not sure yet...). But I have noticed, that it also gave me an error for the "configure ECAN": in the mask, there is no filter_2_* defined only filter_0 and 1. I have added them... but I have to still finish the GCB workaround to see, if it will work. So that is all for now I think...</div>
</article>

<article class="forum-post" id="p1756">
<header><strong>bmairs</strong><time datetime="2011-12-10 00:46 UTC">2011-12-10 00:46 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">So I recently went through and updated my ECAN code. I also actively use these blocks, so it's known to be good. Link is here: <a href="https://github.com/Susurrus/ECAN_dspic">https://github.com/Susurrus/ECAN_dspic</a>. Just add it to your Matlab path as another library and you're good to go.</div>
</article>

<article class="forum-post" id="p1877">
<header><strong>ambersil</strong><time datetime="2012-04-16 20:21 UTC">2012-04-16 20:21 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : bmairs</header>So I recently went through and updated my ECAN code. I also actively use these blocks, so it's known to be good. Link is here: <a href="https://github.com/Susurrus/ECAN_dspic">https://github.com/Susurrus/ECAN_dspic</a>. Just add it to your Matlab path as another library and you're good to go.</blockquote><br>
<br>
Hello,  I'm having a look at you blockset.  I have C30 v3.23 and C32 v1.05 installed, with Matlab 2010a.  Trying your two examples 'out of the box'  I notice that a device which is targeted by the pic30 compiler failes to build because your code uses includes from the pic32 compiler (and vice versa).  Does the toolbox require the new Microchip compiler ( I forget what it's called) which I understand targets all parts?<br>
<br>
<br>
<br>
I'm a bit wary of having to upgrade the microchip tools in case it breaks somthing in Lubin's blockset.  If anyone is using te ECAN code (and the dsPIC blockset) succesfully I would appreciate it if you could list the versions of the tools that you're using.</div>
</article>

<article class="forum-post" id="p1890">
<header><strong>ambersil</strong><time datetime="2012-05-05 22:12 UTC">2012-05-05 22:12 UTC</time></header>
<h3>Re: Support for CAN Module?</h3>
<div class="forum-post-body">Has anyone used bmairs ECAN blockset with a dsPIC33FJ256MC710 device?<br>
<br>
<br>
<br>
I've spent a couple of days trying to transmit over CAN from the PIC with no success.  I can transmit using the microchip code that accompanies AN1249 so I know that the hardware is OK.<br>
<br>
<br>
<br>
I'm not sure if I'm doing something stupid or if there is a problem with bmairs code.  If anyone has succesfully used it I'd appreciate a copy of a simple simulink model (that transmits) that is know to work so that I can see if it works with my setup.</div>
</article>

