---
title: "UART on DsPic33FJ256MC710"
url: "/forum/topic/165/"
archiveKind: "topic"
---
# UART on DsPic33FJ256MC710

Forum : [bug reports](/forum/#forum-8)

15 message(s) · archive en lecture seule

<article class="forum-post" id="p559">
<header><strong>Ender</strong><time datetime="2008-10-11 00:35 UTC">2008-10-11 00:35 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
The Simulink design in attachment works with a  DsPic33FJ256<strong>GP</strong>710 but doesn't work with a DsPic33FJ256<strong>MC</strong>710.<br>
<br>
I tried at 9600 baud and 115200 baud.<br>
<br>
<br>
<br>
   Could you peek an eye please?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/124-Source_one_sinus_to_RS_9600_on_MC.mdl">Pièce jointe : Source_one_sinus_to_RS_9600_on_MC.mdl</a></p>
</article>

<article class="forum-post" id="p560">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-11 17:03 UTC">2008-10-11 17:03 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi Ender,<br>
<br>
<br>
<br>
I did not see obvious error.<br>
<br>
The model However, the model send only 100 bytes / seconds with your configuration (time step of the sinus block is 100Hz, time step for the model is 1KHz.<br>
<br>
<br>
<br>
Do you have an electrical signal on the Tx pin of UART 2 ?<br>
<br>
if yes, you should check your quartz configuration.<br>
<br>
<br>
<br>
Otherwise, let me know. <br>
<br>
I successfully tested the DsPic33FJ256MC710 at least on UART 1.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p562">
<header><strong>Ender</strong><time datetime="2008-10-13 19:12 UTC">2008-10-13 19:12 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi Lumbin, thank for this quick answer and sorry I didn't work this WE.<br>
<br>
<br>
<br>
I know for the 100Hz and 1KHz, I tried with many speed and I sent you a version with the simulation/solver/fixed_step time constraint at 1Khz and a block with 100hz. But is there a link between the simulation time step and the Dspic compiler work ?<br>
<br>
<br>
<br>
1__Regardless, the code doesn't work with a block at 1Khz too.<br>
<br>
<br>
<br>
2__I use a Explorer 16 Board with a 40Mhz Oscillator, but I didn't change the capacitors close to the Oscillator (am I need to do?). If I use a C code in Mplab to send a ramp of values with your frame, the GUI display the signal.  So I think the hardware configuration is fine.<br>
<br>
<br>
<br>
3__I ever saw the same problem on a Dspic33FJ256GP on July, when I installed the licensed version of your blockset, I have changed the C compiler version for the 3.11 too. From that time I work with the 3.10b version. But the next week, I installed a new licensed version of MPLAB Dspic C compiler so Maybe there are compliance problems. I’am using:<br>
<br>
  Mathlab 2007b, Dspic Blockset2007B licenced and MPLAB_C_dsPICFullv3_10b Licenced: with these the model work at 1khz, 115200baud on a  Dspic33FJ256GP710 but doesn’t on Dspic33FJ256MC710.<br>
<br>
   I’ll change of version and will see.</div>
</article>

<article class="forum-post" id="p563">
<header><strong>Ender</strong><time datetime="2008-10-13 19:52 UTC">2008-10-13 19:52 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">With  Mathlab 2007b, Dspic Blockset2007B licensed and MPLAB_C_3.11 student, the model 1khz_115200 baud:<br>
<br>
  1___ doesn't work on Dspic33FJ256MC710.<br>
<br>
  2___ And it doesn’t work with a Dspic33FJ256GP710 too of course I changed the target in Master and I compiled the code every time.  <br>
<br>
  3___The Rs232gui receipt few octets but the graph doesn't display.  On the pin 2 of RS232 the signal exists and seems good. With my own Labview RS232 interface, Labview shows a framing error.</div>
</article>

<article class="forum-post" id="p564">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-13 21:50 UTC">2008-10-13 21:50 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi Ender,<br>
<br>
<br>
<br>
I tested the dsPIC_33f_Explorer16.mdl demo (in the demo directory of the blockset) with the explorer16 board equipped with the 33f256GP710 and the original 8Mhz quartz.<br>
<br>
It works successfully (Matlab 2008a, gcc version 4.0.3 (dsPIC30, Microchip v3_11) Build date: Jul 16 2008 student version because my license is out of date)<br>
<br>
<br>
<br>
Could you check that the dsPIC is working at a proper frequency (have an I/O blinking and check its frequency, or use a LED at 1Hz for example)<br>
<br>
If there is a bug, It may be at the configuration of the UART (but as I tested, I do not think so), or it may be a problem dealing with the clock/timer of the dsPIC.  <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p565">
<header><strong>Ender</strong><time datetime="2008-10-13 22:12 UTC">2008-10-13 22:12 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">I checked your idea the led blink at 1.5s = 0.66Hz instead of 1s.<br>
<br>
<br>
<br>
The width of the start bit on the COM is 25µS and the frame is just litle bit more than 700µs at 115200baud<br>
<br>
The widths between to dot are 2.74 ms instead of 1ms.</div>
</article>

<article class="forum-post" id="p566">
<header><strong>Ender</strong><time datetime="2008-10-13 22:36 UTC">2008-10-13 22:36 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Could you build and send to me an .Hex file for 115200baud and an 40Mhz oscillator, please ?</div>
</article>

<article class="forum-post" id="p567">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-13 22:45 UTC">2008-10-13 22:45 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">If led blink at 1.5s, widths between dots should be 1.5m instead of 2.74ms ?<br>
<br>
<br>
<br>
Either there is a bug in the code generated by the blockset.<br>
<br>
Neither the quartz is not at 40Mhz but oscillate at 26.6Mhz. You could try to declare the quartz as a 26.6Mhz quartz in the Master block...<br>
<br>
<br>
<br>
Attached are the two requested .hex file</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/125-dsPIC33f_Explorer16_MC_GP710.zip">Pièce jointe : dsPIC33f_Explorer16_MC_GP710.zip</a></p>
</article>

<article class="forum-post" id="p568">
<header><strong>Ender</strong><time datetime="2008-10-13 22:56 UTC">2008-10-13 22:56 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">I tried with my C code on MPLAB for 115200baud the start width is 8.5µs and the Gui receipt the dots.</div>
</article>

<article class="forum-post" id="p569">
<header><strong>Ender</strong><time datetime="2008-10-13 23:03 UTC">2008-10-13 23:03 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">I declared the quartz as a 26.6Mhz :<br>
<br>
<br>
<br>
Led blink  950mS and  Start bit width 15µS ?</div>
</article>

<article class="forum-post" id="p570">
<header><strong>Ender</strong><time datetime="2008-10-13 23:20 UTC">2008-10-13 23:20 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Thanks for the .Hex file.<br>
<br>
 Same result that me with your dsPIC_33f_Explorer16_GP710.hex file.<br>
<br>
The start bit is 23µS width, instead 8.5µS, so it's also doesn't work in Rs232Gui</div>
</article>

<article class="forum-post" id="p571">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-14 16:43 UTC">2008-10-14 16:43 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
The problem described is weird!<br>
<br>
It is still not clear where it comes from :<br>
<br>
<br>
<br>
- Either there is a bug in the blockset, like an overflow that occurs when using high frequency quartz like 40Mhz quartz<br>
<br>
- Neither there is a hardware problem on your system.<br>
<br>
<br>
<br>
As no PLL are used, a 40Mhz quartz gives a 20MIPS system, it is quite straight ! The time step should be fine and the blinking led should blink at the required frequency! You could also do a test with the busy flag port in the MASTER block and check the time step with a scope.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ender</header>If I use a C code in Mplab to send a ramp of values with your frame, the GUI display the signal. So I think the hardware configuration is fine.</blockquote><br>
In other word, the hardware is Ok!<br>
<br>
<br>
<br>
Could you compare the code you write with the code generated by the blockset ?  (use the simulink report : Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop ==&gt; HTML report)<br>
<br>
The only part to compare is within the main file: timers and UART configuration...<br>
<br>
<br>
<br>
Or send me your "MPLAB" working code that works with your hardware I will have a look.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p572">
<header><strong>Ender</strong><time datetime="2008-10-15 03:54 UTC">2008-10-15 03:54 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">You right Lumbin, I used a example code from Microship which used the PLL.<br>
<br>
There is a hardware problem on the oscillator, some time and more when I use the oscilloscope probe the frequency is correct.<br>
<br>
I'll replace the capacitors by the new ones to be sure of their values and remove/re-solder the quartz.<br>
<br>
<br>
<br>
If I reuse the original 8Mhz quartz, how the blockset will work if the loop time execution is too long to match with the transfer rate request?<br>
<br>
In this case do you use the PLL to increase FCy, the instruction cycle clock, at more than 8Mhz ?<br>
<br>
<br>
<br>
Thanks a lot.</div>
</article>

<article class="forum-post" id="p573">
<header><strong>Ender</strong><time datetime="2008-10-15 04:07 UTC">2008-10-15 04:07 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Okay, I found the answer myself in master block description.<br>
<br>
  <a href="/RTWdsPIC/Blocks/Master.html">http://www.kerhuel.eu/RTWdsPIC/Blocks/Master.html</a></div>
</article>

<article class="forum-post" id="p576">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-15 20:54 UTC">2008-10-15 20:54 UTC</time></header>
<h3>Re: UART on DsPic33FJ256MC710</h3>
<div class="forum-post-body">Hi Ender,<br>
<br>
<br>
<br>
To complete the topic :<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ender</header>how the blockset will work if the loop time execution is too long to match with the transfer rate request?</blockquote>Execution continues (i.e. not like the xPC target system  behaviour where the execution hang up)<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ender</header>In this case do you use the PLL to increase FCy, the instruction cycle clock, at more than 8Mhz ?</blockquote>This is how it works!<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ender</header>Okay, I found the answer myself in master block description.<br>
<br>
<a href="/RTWdsPIC/Blocks/Master.html">http://www.kerhuel.eu/RTWdsPIC/Blocks/Master.html</a></blockquote>This is the old page and will not be updated anymore. Please use this on : <a href="/wiki/dspic-block-master/">http://www.kerhuel.eu/wiki/Block/Master</a><br>
<br>
<br>
<br>
Lubin</div>
</article>

