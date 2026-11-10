---
title: "UART on Explore16"
url: "/forum/topic/276/"
archiveKind: "topic"
---
# UART on Explore16

Forum : [General Remark and Questions](/forum/#forum-1)

12 message(s) · archive en lecture seule

<article class="forum-post" id="p1079">
<header><strong>resodad</strong><time datetime="2010-02-09 17:58 UTC">2010-02-09 17:58 UTC</time></header>
<div class="forum-post-body">Hello, I am trying to use UART2. It is very simple: send sequence 0, 1, 2, 3...15 repeating to UART2 at 9600/8/1/none/none.<br>
<br>
Result:<br>
<br>
Terminal program on computer --cursor jumps from position to position, but no text or numbers.<br>
<br>
I am generating code through MPLAB.<br>
<br>
versions:<br>
<br>
Windows vista<br>
<br>
MPLAB  v8.36<br>
<br>
C30 v3.20<br>
<br>
MATLAB r2009a<br>
<br>
no build errors<br>
<br>
I will attach model and source code<br>
<br>
Thanks,<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/291-UARTtest2.zip">Pièce jointe : UARTtest2.zip</a></p>
</article>

<article class="forum-post" id="p1080">
<header><strong>Bobes</strong><time datetime="2010-02-10 12:15 UTC">2010-02-10 12:15 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">than it is probably working right<br>
<br>
look at the ASCII table <a href="http://www.asciitable.com/">http://www.asciitable.com/</a><br>
<br>
<br>
<br>
hyperterminal is "translating" to ascii</div>
</article>

<article class="forum-post" id="p1081">
<header><strong>resodad</strong><time datetime="2010-02-10 17:26 UTC">2010-02-10 17:26 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">YES! THANKS Bobes<br>
<br>
of course you are correct. I changed the input to [0:255} and now have the entire ASCII set<br>
<br>
Cheers,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1088">
<header><strong>resodad</strong><time datetime="2010-02-25 23:51 UTC">2010-02-25 23:51 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">Lubin, I have a new problem on this effort: When I run the program it will very quickly halt:<br>
<br>
Running...<br>
<br>
Target halted<br>
<br>
I am not aware of changing anything. If I attempt to import all source files into MPLAB and rebuild, I get:<br>
<br>
Link step failed.<br>
<br>
.<br>
<br>
.<br>
<br>
.<br>
<br>
BUILD FAILED</div>
</article>

<article class="forum-post" id="p1091">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-26 16:07 UTC">2010-02-26 16:07 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
- check that your programmer (ICD2 ?) is not in debug mode while loading the program.<br>
<br>
(it shouldn't as you compiled inside matalb and not directly into mplab).<br>
<br>
<br>
<br>
- check your hardware, specificaly the quartz signal ; do you use a pin MCLR, if so, is it tight to "1" properly. running time is it always the same or does it changes from one try to another ?<br>
<br>
<br>
<br>
last things, trap error could be caused by division by 0 or so, check that point.</div>
</article>

<article class="forum-post" id="p1092">
<header><strong>resodad</strong><time datetime="2010-02-26 19:49 UTC">2010-02-26 19:49 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">I am new to MPLAB; I'm not sure what to do. So far I have used the ICD3 only in degugger mode.  I am thinking the procedure is build the model directly in matlab, add the .hex file to the MPLAB project and then in MPLAB:<br>
<br>
programmer &gt; select programmer &gt; ICD3<br>
<br>
programmer &gt; program<br>
<br>
and the program will start running. <br>
<br>
This is what I am trying and there is no output from the dsPIC<br>
<br>
<br>
<br>
I am not using MCLR<br>
<br>
I  is not a divide by zero problem.<br>
<br>
<br>
<br>
This program was working earlier.</div>
</article>

<article class="forum-post" id="p1094">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-26 21:36 UTC">2010-02-26 21:36 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : resodad</header>programmer &gt; select programmer &gt; ICD3<br>
<br>
programmer &gt; program</blockquote><br>
between theses two step, load the .hex file, or the .coff file (I guess that's already done)<br>
<br>
<br>
<br>
Two more ideas : <br>
<br>
<br>
<br>
- Check the dsPIC configuration bits programmation : MPLAB can use either the configuration that is in the .hex/.coff file, or the configuration bytes defined in the MPLAB interface. It must be set to use the .hex/.coff information, or you must configure theses bytes carefully in MPLAB.<br>
<br>
<br>
<br>
- MPLAB has a release signal (connected to MCLR) that (sometimes) allows to start/stop the program.</div>
</article>

<article class="forum-post" id="p1097">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-01 21:54 UTC">2010-03-01 21:54 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">One more remarks : Do not compile anything within MPLAB. Just load the hex file : <br>
<br>
<br>
<br>
In the case you use the blockset, you import the .hex (or .coff) binary file into MPLAB and you must directly program without compiling within the MPLAB interface. Otherwise, you compile the current project that does not correspond to code generated by Simulink.<br>
<br>
Thus, order is :<br>
<br>
--&gt; Select chip in MPLAB<br>
<br>
--&gt; Select programmer<br>
<br>
--&gt; Load your Hex/coff file generated within Matlab/Simulink into MPLAB<br>
<br>
--&gt; Check dspic configuration bits settings (see post up)<br>
<br>
--&gt; load the program into the chip through ICD2 / ICD3 / Real ice or equivalent<br>
<br>
--&gt; press "release" button if necessary. Sometimes it is necessary to disconnect the cable.<br>
<br>
<br>
<br>
You cannot do debugging with this method as the project with c files and so is not configured within MPLAB.<br>
<br>
<br>
<br>
Another method is to configure a new project, importing c files and library from the simulink's model subdirectory. Then compile the project as a usual project. With this last solution, you can debug using mplab tools.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1098">
<header><strong>resodad</strong><time datetime="2010-03-02 20:10 UTC">2010-03-02 20:10 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">Thanks, I still have no output from dsPIC<br>
<br>
Attached is an image of my configuration bits, and the latest simulink model. I cannot find a configuration bit regarding MCLR. I don't know how to set / clear. I am not sure what you mean by "release button;" I assume you mean Programmer menu &gt; release from reset?  Does this make the program run?<br>
<br>
<br>
<br>
MCLR pin (pin 13 of dsPIC33FJ256GP710) measures 3 volts with voltmeter.<br>
<br>
<br>
<br>
See warnings 1 and 2 from Matlab upon opening model file below. I got these at different times opening the simulink model:<br>
<br>
<br>
<pre><code>warning 1:
C30 Compiler found
Warning: dsPICdrivers.mdl, line 47: block_diagram does not have a parameter named
'CovForceBlockReductionOff'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time workshop. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System
Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
Warning: In instantiating linked block 'UARTtest4/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
PT&gt;&gt;</code></pre><br>
<br>
<br>
<pre><code>warning 2:
&gt;&gt; clear all
C30 Compiler found
Warning: In instantiating linked block 'UARTtest4/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'. 
  In general\private\openmdl at 13
  In open at 154
  In uiopen at 196
PTPTPTPNumber of I/O PINs used : 6
TPTTPTPT&gt;&gt;</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/298-UARTtest4.zip">Pièce jointe : UARTtest4.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/299-shot_20100303000123-641.png">Pièce jointe : shot_20100303000123-641.png</a></p>
</article>

<article class="forum-post" id="p1099">
<header><strong>LubinKerhuel</strong><time datetime="2010-03-02 23:42 UTC">2010-03-02 23:42 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">Good news, as I think I found the problem and solution is very simple.<br>
<br>
Few elements first <br>
<blockquote><header class="quote-author">Citation : resodad</header>See warnings 1 and 2 from Matlab upon opening model file below. I got these at different times opening the simulink model</blockquote><br>
I can't get a ride of them yet but theses warning are not a problem.<br>
<br>
<br>
<br>
If you get at the end of compilation <br>
<pre><code>*** Created executable: ..\../UARTtest4.coff
''pic30-bin2hex ..\../UARTtest4.coff  
*** Created executable: ..\../UARTtest4.hex
### Successful completion of Real-Time Workshop build procedure for model: UARTtest4
C30 Compiler found
C30 Compiler found
PTPTPNumber of I/O PINs used : 6</code></pre><br>
it's Ok.<br>
<br>
<br>
<br>
I check model's logic, it's all fine. (Port A should work), you may replace <em>the Repeating Sequence Stair</em> block with a simple 8 bit counter.<br>
<br>
<br>
<br>
The problem is in MPLAB :<br>
<br>
In the picture you present here, <strong>the .hex file is not loaded correctly as you added the file to a project and this is not the way to do</strong>.  <br>
<br>
You can see in the config bits that is presented on the screenshot that for example the oscillator mode (FNOSC) is set to <strong>Internal Fast RC</strong>. It should be set instead to primary oscillator w/PLL as demanded on the simulink file. (Configuration bits set in code checkbox is set correctly here.)<br>
<br>
<br>
<br>
<strong>From MPLAB</strong>,<br>
<br>
- First close any open project (<strong>Project ==&gt; Close</strong>) (it is not necessary, but it will make things more clear)<br>
<br>
- Select programmer (ICD2, and the set configurations bits set in code checkbox) etc...<br>
<br>
- <strong> Load the .hex file</strong> : (<strong>File ==&gt; Import, no add into project or other way</strong> ) You may see the checksum below the menu to change. <strong>&lt;== This is the Solution that will solve the problem</strong><br>
<br>
- you may check that the .hex file is properly imported throws the configurations bits, for example check the Oscillator mode (FNOSC), should be set automatically to primary oscillator w/PLL.<br>
<br>
- <strong>program </strong> as usual, without compiling anything within MPLAB ; that's it !<br>
<br>
<br>
<br>
Note that you must Import again the .hex file each time the simulink model is compiled in Matlab, in order to program the last binary result into the dsPIC.<br>
<br>
<br>
<br>
Please, feel free to edit the wiki at the place where it would have helped you. It seems be missing right now!<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1100">
<header><strong>resodad</strong><time datetime="2010-03-03 16:55 UTC">2010-03-03 16:55 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">Excellent work Lubin, thank you much.<br>
<br>
This project is working now on Explorer16 with sdPIC33FJ256GP710. I was adding the file to a MPLAB Project instead of importing.<br>
<br>
One minor problem: The simulink source "repeating sequence stair" does not work as I expect now, but it's not a big deal since the source "limited counter" set to 127 is working. Do you have any ideas about this?<br>
<br>
I have also duplicated the project on Evidence Flex which I wil post separately.</div>
</article>

<article class="forum-post" id="p1101">
<header><strong>resodad</strong><time datetime="2010-03-03 22:15 UTC">2010-03-03 22:15 UTC</time></header>
<h3>Re: UART on Explore16</h3>
<div class="forum-post-body">I am attaching an example for the Flex board</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/300-Serial%20Communications%20with%20Microchip%20dsPIC33.pdf">Pièce jointe : Serial Communications with Microchip dsPIC33.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/301-UART7.zip">Pièce jointe : UART7.zip</a></p>
</article>

