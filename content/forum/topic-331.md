---
title: "rs232gui and PIC32 starter kit"
url: "/forum/topic/331/"
archiveKind: "topic"
---
# rs232gui and PIC32 starter kit

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

17 message(s) · archive en lecture seule

<article class="forum-post" id="p1315">
<header><strong>salemimoh</strong><time datetime="2010-11-01 11:27 UTC">2010-11-01 11:27 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I want to download a  matlab application to the PIC32 using PIC32 starter kit. I looked at the rs232gui. It only has the com ports but no USB port, which is used on the starter kit to program the PIC32. Is there a way to how I could get round this problem? What about if I am using the PIC32 I/O expansion board.</div>
</article>

<article class="forum-post" id="p1316">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-01 13:59 UTC">2010-11-01 13:59 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Matlab/Simulink are used for generating the code and compile it into a .hex file.<br>
<br>
Once you have this file, use the microchip MPLAB IDE to load the .hex file and to download it into your target through your own hardware (PIC32 starter kit, or ICD2, ICD3, REAL ICE...)<br>
<br>
<br>
<br>
You may also use a bootloader.<br>
<br>
<br>
<br>
Anyway, Matlab has not the capacity to download your application into your hardware.<br>
<br>
<br>
<br>
rs232gui is used to view variable in real time through an UART interface.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1319">
<header><strong>salemimoh</strong><time datetime="2010-11-05 19:11 UTC">2010-11-05 19:11 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Thank you lubbin.<br>
<br>
I tried to find a way how to downlad the hex file using PIC32 starter kit from MPLAB but I did not find out how to do it. So I tried to import the file into MPLAB using TOOLS then MATLAB/SIMULINK then specify the file name which was opened successfully.<br>
<br>
Then GENERATE CODE which is generated successfully.<br>
<br>
" ================================================================" <br>
<br>
"*** Embedded Target for dsPIC by Lubin KERHUEL - <a href="/">http://www.kerhuel.eu</a>" <br>
<br>
" | Licence Accorded to Demonstration Version                    |" <br>
<br>
" |                     [adresse e-mail retirée]                      |"	     <br>
<br>
" |          Companie : Author : Lubin KERHUEL                   |"  <br>
<br>
" |                     WEBSITE : <a href="/archive-assets/">http://www.kerhuel.eu/wiki</a>     |" <br>
<br>
" |                                                              |" 		 <br>
<br>
" |                     SIRENE : 503 920 456                     |" <br>
<br>
" |                     SIRET : 503 920 456 00012                |"		 		 <br>
<br>
" | Financial Service : Demo                                     |" <br>
<br>
" | Contact             Demo                                     |" <br>
<br>
" |                     Lubin KERHUEL                            |" <br>
<br>
" |                     1, rue Alfred Fredet                     |" <br>
<br>
" |                     38100 Grenoble                           |" <br>
<br>
" |                     FRANCE                                   |" <br>
<br>
" | Version 3.2c                              23-Jul-2010        |" <br>
<br>
" | For Matlab 7.8             R2009a                            |" <br>
<br>
" ================================================================"		  <br>
<br>
"*** Created "executable": ..\../train1.elf"		 <br>
<br>
''pic32-bin2hex ..\../train1.elf  <br>
<br>
"*** Created "executable": ..\../train1.hex"	 <br>
<br>
### Successful completion of Real-Time Workshop build procedure for model: train1<br>
<br>
C32 Compiler found<br>
<br>
C32 Compiler found<br>
<br>
E                                   |" <br>
<br>
" | Version 3.2c                              23-Jul-2010        |" <br>
<br>
" | For Matlab 7.8    <br>
<br>
BUILD EXECUTION COMMAND COMPLETED<br>
<br>
<br>
<br>
<br>
<br>
When I tried to import it using IMPORT GENERATED CODE I get this message:<br>
<br>
<br>
<br>
Error : Accessing generated files information from Matlab. Try regenerating code.<br>
<br>
<br>
<br>
Failed to Import Generated Files. Check the Build Window to know the Status of Build<br>
<br>
<br>
<br>
I tried without success to find out the error but I could not.</div>
</article>

<article class="forum-post" id="p1320">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-05 19:26 UTC">2010-11-05 19:26 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Ok,<br>
<br>
<br>
<br>
1) in MPLAB, select your programmer with the programmer menue.<br>
<br>
2) choose the chip you are using<br>
<br>
3) import with : file==&gt; import<br>
<br>
and choose the .hex file you just generated !<br>
<br>
<br>
<br>
then download it, that's it !<br>
<br>
<br>
<br>
Please, keep an eye on the website as the next release of the blockset will probably have new interresting stuff that will simplify integration with MPLAB.<br>
<br>
(expected within few weeks or days)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1321">
<header><strong>salemimoh</strong><time datetime="2010-11-06 12:41 UTC">2010-11-06 12:41 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Thank you Lubin for your valuable info.</div>
</article>

<article class="forum-post" id="p1322">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-08 23:34 UTC">2010-11-08 23:34 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Latest blockset version (3.3) create the MPLAB project file properly configured. Give it a try !</div>
</article>

<article class="forum-post" id="p1323">
<header><strong>salemimoh</strong><time datetime="2010-11-09 22:23 UTC">2010-11-09 22:23 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Lubbin,<br>
<br>
I have tried the new version 3.3 but it is still giving me the same error message:<br>
<br>
Load Main Project (or) Set Main Project as Active Project<br>
<br>
<br>
<br>
Failed to import Generated Files. Check the Build Window to know the Status of Build. No message was reported in the matlab build window??</div>
</article>

<article class="forum-post" id="p1324">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-10 07:31 UTC">2010-11-10 07:31 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">What is the operation that generate this error ?<br>
<br>
Note that you do not need the MPLAB MATLAB plugin !<br>
<br>
<br>
<br>
first, compile the project with MATLAB. (do not open MATLAB through MPLAB)<br>
<br>
Then, open MPLAB separately !<br>
<br>
<br>
<br>
In matlab, try to compile the example given in the blockset directory that use a C32 pic. <br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1330">
<header><strong>salemimoh</strong><time datetime="2010-11-21 22:01 UTC">2010-11-21 22:01 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I wrote a small program in simulink just as a test, which reads a couple of switches and sends them back to a couple of LEDs. Then I compiled it, and imported it into MPLAB using hex file and it works perfectly. But When I created a MPLAB project and tried to link the bits and pieces as it is shown in the attached file.<br>
<br>
When built, it gives the following errors. It looks though there are few files were not created for some reason. such as timer.h, probably rtlibscr.h library files etc.<br>
<br>
Is that correct or there is another reason?<br>
<br>
<br>
<br>
<br>
<br>
Debug build of project `C:\Program Files\Microchip\MPLAB C32\pic32_mplab.mcp' started.<br>
<br>
Language tool versions: pic32-gcc.exe v1.05, pic32-ld.exe v1.05, pic32-ar.exe v1.05<br>
<br>
Preprocessor symbol `__DEBUG' is defined.<br>
<br>
Target debug platform is `__MPLAB_DEBUGGER_PIC32MXSK=1'.<br>
<br>
Mon Nov 22 00:13:16 2010<br>
<br>
----------------------------------------------------------------------<br>
<br>
Clean: Deleting intermediary and output files.<br>
<br>
Clean: Done.<br>
<br>
Executing: "C:\Program Files\Microchip\MPLAB C32\bin\pic32-gcc.exe" -mprocessor=32MX360F512L -x c -c "C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\test1_main.c" -o"test1_main.o" -MMD -MF"test1_main.d" -D__DEBUG -D__MPLAB_DEBUGGER_PIC32MXSK=1 -g<br>
<br>
In file included from C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\/test1_private.h:33,<br>
<br>
                 from C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\test1_main.c:28:<br>
<br>
C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\/timer.h:42:29: GenericTypeDefs.h: No such file or directory<br>
<br>
In file included from C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\/test1_private.h:33,<br>
<br>
                 from C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\test1_main.c:28:<br>
<br>
C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\/timer.h:66: error: syntax error before "dwCount"<br>
<br>
C:\Documents and Settings\Admin\My Documents\MATLAB\test1_dspic\sources\/timer.h:67: error: syntax error before "ms"<br>
<br>
Halting build on first failure as requested.<br>
<br>
----------------------------------------------------------------------<br>
<br>
Debug build of project `C:\Program Files\Microchip\MPLAB C32\pic32_mplab.mcp' failed.<br>
<br>
Language tool versions: pic32-gcc.exe v1.05, pic32-ld.exe v1.05, pic32-ar.exe v1.05<br>
<br>
Preprocessor symbol `__DEBUG' is defined.<br>
<br>
Target debug platform is `__MPLAB_DEBUGGER_PIC32MXSK=1'.<br>
<br>
Mon Nov 22 00:13:17 2010<br>
<br>
----------------------------------------------------------------------<br>
<br>
BUILD FAILED</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/351-test.doc">Pièce jointe : test.doc</a></p>
</article>

<article class="forum-post" id="p1332">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-21 23:49 UTC">2010-11-21 23:49 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
Did you created by yourself the MPLAB project, or<br>
<br>
did you open the project (.mcp file) created by the latest blockset version ?<br>
<br>
<br>
<br>
The latest blockset version (from v3.3)  creates the MPLAB project file. Thus, project can be opened within MPLAB and recompiled from there if needed.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1333">
<header><strong>salemimoh</strong><time datetime="2010-11-22 19:40 UTC">2010-11-22 19:40 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
Thank you very much for your help.<br>
<br>
Yes I finally got to the final hurdle, where I loaded the application into MPLAB and compiled it successfully as you mentioned then loaded it into the PIC32 and it worked fine. But I have a small problem.  I am trying to follow the program using step by step in the debug mode using the generated machine language (or the un-assembled program if you like) and ir is ok; but I could not trace the C subroutines including the main subroutine; because tracing generated machine language is very tedious and time consuming and is not evident to be followed easily especially in my application where I am implementing relatively long program.<br>
<br>
My question is : is there a way by which we can trace   step by step in the debug mode the C subroutines such as the main subroutine for instance?</div>
</article>

<article class="forum-post" id="p1334">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-22 22:11 UTC">2010-11-22 22:11 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Great that you get it working!<br>
<blockquote><header class="quote-author">Citation : salemimoh</header>My question is : is there a way by which we can trace step by step in the debug mode the C subroutines such as the main subroutine for instance?</blockquote><br>
It's a very long time I have not use the debug trace of MPLAB. Thus, I may not be able to help on that point.<br>
<br>
The only things I know is that there is two ways: <br>
<br>
- Either you use the sim module that will simulate in the PC only the code and you can then check registry values (but not interfere with real signals)<br>
<br>
- Or you use the trace system that makes you able to trace the code in the target (I guess you are talking about this method).<br>
<br>
<br>
<br>
I think that capabilities of the second method depends on the programmer you are using (ICD2, real ice) and of the cable connection you are using with the target.<br>
<br>
Anyway, using breakpoint is usually the way to stop the program where you want to. Removing compiler optimization may help to trace the code. There are also options to generate debug information at compilation time. I have no recent experience to tell how to switch from assembly tracing to C tracing (anyway, I remember doing this few years ago)<br>
<br>
However, it happens that the code run in unexpected ways.<br>
<br>
<br>
<br>
I find myself more time consuming to track bug this way than having the code running in real time and sending debug values through UART.<br>
<br>
<br>
<br>
However, MPLAB has now interesting function. It may be possible to change values of some hard coded variable in hardly real time! I did not test this yet but it might be very useful.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1336">
<header><strong>salemimoh</strong><time datetime="2010-11-23 10:03 UTC">2010-11-23 10:03 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Thank you Lubin,<br>
<br>
I will give it a try and see.</div>
</article>

<article class="forum-post" id="p1348">
<header><strong>salemimoh</strong><time datetime="2010-11-28 19:22 UTC">2010-11-28 19:22 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I am using rs232gui to read data from the PIC32 through its UART. Because I am using LAPTOP where it only has USB connections, the data could only be read through com3 as it is specified on your site.<br>
<br>
Things which I did and the connection was established:<br>
<br>
<br>
<br>
Connecting... May take few seconds...<br>
<br>
Port COM3 successfully open at 115200............OK<br>
<br>
redefinition SerialCOM<br>
<br>
I press PLOT buffer to get the graphic screen. Which it comes through; But When I press start, i do not get any graph.<br>
<br>
My question is: Have you got any idea why is that?</div>
</article>

<article class="forum-post" id="p1349">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-28 21:01 UTC">2010-11-28 21:01 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Hello<br>
<blockquote><header class="quote-author">Citation : salemimoh</header> the data could only be read through com3 as it is specified on your site</blockquote><br>
Could you provide the link ? (I do not remember the whys and wherefores I wrote it)<br>
<br>
<br>
<br>
Anyway, you may test first is the dsPIC is sending data to the PC using an hyperterminal. Most recent windows do not have hyperterminal by default, you may download free version, or alternatively download the pretty good <a href="http://realterm.sourceforge.net/">realterm</a>software (free).<br>
<br>
Check that the PC is receiving data (you should see characters appearing in the term).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1353">
<header><strong>salemimoh</strong><time datetime="2010-11-29 19:14 UTC">2010-11-29 19:14 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I am sure of the link but I think this is the one:<br>
<br>
<a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">http://lubink.free.fr/projelectro/Proto ... ew_FR.html</a><br>
<br>
It says I quote:"Les ports COM disparaissant peu à peu des PC et notamment des portables, on peut utiliser des adaptateurs série=&gt;USB avec leur driver de port série virtuel. Un tel adaptateur a été ici utilisé : le port COM 5 est un port COM virtuel."<br>
<br>
Though it mentions com5, the only com which com which connects with the controller is com3.</div>
</article>

<article class="forum-post" id="p1355">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 20:00 UTC">2010-11-29 20:00 UTC</time></header>
<h3>Re: rs232gui and PIC32 starter kit</h3>
<div class="forum-post-body">That is my old French website (beautiful, but perhaps not accurate enough)<br>
<br>
<br>
<br>
Anyway, when you are using a virtual COM port, for example a USB adaptator, this one can take any number of COM port. It usually remains stable. You have to check your computer config (easiest way is to use the list of hardware peripheral installed on your computer. You can browse them with windows<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : salemimoh</header>Port COM3 successfully open at 115200............OK</blockquote>) <br>
<br>
This does not mean that COM 3 corresponds to your USB adaptator. Thus, you should check that your COM3 correspond to your USB adaptator.<br>
<br>
There is a high probability that this is it !<br>
<br>
<br>
<br>
Then, you may check that your dsPIC is running. try to have make a led blinking to make sure it is running. If it runs properly, you may check that it is blinking at the right frequency (either use a scope, or use a slow blinking frequency like 1 or 2 Hz). <br>
<br>
<br>
<br>
Provided you have a scope, check the Tx line of the microcontroller. It should be changing at pretty high frequency. If you do not have a scope, you can try to send data <strong>continuously </strong>and use a voltmeter. The voltage read should be about half VDD. If you read VDD or 0, something's wrong.<br>
<br>
<br>
<br>
Ok, From the other side, check that your USB adaptator is working. Use real term, connect to your port COM (COM3), short circuit the UART Rx and Tx pins of the USB adaptator and send characters through the terminal. If the character appears on the terminal, they are sent and receive properly. Adaptator should be OK. If you see nothing when you write something within the terminal screen, it means that nothing is received on the Rx pin. Use a scope to check what's happening then...<br>
<br>
<br>
<br>
I hope theses few ideas will help.<br>
<br>
Lubin</div>
</article>

