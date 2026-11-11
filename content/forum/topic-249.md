---
title: "Communication blockset - bpsk modulation - Error  at 1138"
url: "/forum/topic/249/"
archiveKind: "topic"
---
# Communication blockset - bpsk modulation - Error  at 1138

Forum : [General Remark and Questions](/forum/#forum-1)

14 message(s) · archive en lecture seule

<article class="forum-post" id="p966">
<header><strong>Lizaveta</strong><time datetime="2009-10-19 14:53 UTC">2009-10-19 14:53 UTC</time></header>
<div class="forum-post-body">Hello Lubin!<br>
<br>
I have a problem when matlab generates a с-code from simulink model!<br>
<br>
Compilation begins &amp; after 2 sec it shows an error. :( <br>
<pre><code>### Invoking Target Language Compiler on untitled.rtw
	tlc
	-r
	C:\Users\п\Documents\MATLAB\untitled_dspic\sources\untitled.rtw
	D:\Учеба\МАГИСТРАТУРА\Ветринский\библиотека PIC дляsimulink\dspic\dspic.tlc
	-OC:\Users\п\Documents\MATLAB\untitled_dspic\sources
	-ID:\Учеба\МАГИСТРАТУРА\Ветринский\библиотека PIC дляsimulink\dspic
	-ID:\Program Files\MATLAB\R2008a\toolbox\dspblks\dspmex\tlc_c
	-ID:\Учеба\МАГИСТРАТУРА\Ветринский\библиотека PIC дляsimulink\blocks
	-ID:\Program Files\MATLAB\R2008a\toolbox\commblks\commmex\tlc_c
	-IC:\Users\п\Documents\MATLAB\untitled_dspic\sources\tlc
	-ID:\Program Files\MATLAB\R2008a\rtw\c\tlc\mw
	-ID:\Program Files\MATLAB\R2008a\rtw\c\tlc\lib
	-ID:\Program Files\MATLAB\R2008a\rtw\c\tlc\blocks
	-ID:\Program Files\MATLAB\R2008a\rtw\c\tlc\fixpt
	-ID:\Program Files\MATLAB\R2008a\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=0
	-aLocalBlockOutputs=1
	-aRollThreshold=5
	-aZeroInternalMemoryAtStartup=1
	-aZeroExternalMemoryAtStartup=1
	-aInitFltsAndDblsToZero=1
	-aGenerateReport=0
	-aGenCodeOnly=0
	-aRTWVerbose=1
	-aIncludeHyperlinkInReport=0
	-aLaunchReport=0
	-aGenerateTraceInfo=0
	-aForceParamTrailComments=0
	-aGenerateComments=1
	-aIgnoreCustomStorageClasses=0
	-aIncHierarchyInIds=0
	-aMaxRTWIdLen=31
	-aShowEliminatedStatements=0
	-aIncDataTypeInIds=0
	-aInsertBlockDesc=0
	-aSimulinkBlockComments=1
	-aInlinedPrmAccess="Literals"
	-aTargetFcnLib="ansi_tfl_table_tmw.mat"
	-aGenFloatMathFcnCalls="ANSI_C"
	-aIsPILTarget=0
	-aIncludeMdlTerminateFcn=0
	-aCombineOutputUpdateFcns=1
	-aSuppressErrorStatus=1
	-aERTCustomFileBanners=1
	-aLogVarNameModifier="rt_"
	-aGenerateFullHeader=1
	-aGenerateSampleERTMain=0
	-aMatFileLogging=0
	-aMultiInstanceERTCode=0
	-aPurelyIntegerCode=0
	-aPortableWordSizes=0
	-aGenerateErtSFunction=0
	-aGenerateASAP2=0
	-aExtMode=0
	-aExtModeStaticAlloc=0
	-aExtModeStaticAllocSize=1000000
	-aExtModeTransport=0
	-aExtModeTesting=0
	-aInlinedParameterPlacement="NonHierarchical"
	-aTargetOS="BareBoardExample"
	-aMultiInstanceErrorCode="Error"
	-aRateGroupingCode=1
	-aRTWCAPISignals=0
	-aRTWCAPIParams=0
	-aRootIOStructures=0
	-aERTCustomFileTemplate="dsPIC_main.tlc"
	-aGMAKE_PLACE="D:\PROGRA~1\MATLAB\R2008a\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS="-t --report-mem -Map ../untitled.map --heap 0  -cref"
	-aLDPICTYPE="-T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC30F\gld\p30f2012.gld"
	-aLDLIBPIC="C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\libp30f2012-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES="-I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="30f2012"
	-aGCCPATH="C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\"
	-aGenerateTraceInfo=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
.....
### Initial pass through model to cache user defined code
.
### Caching model source code
................
### Writing main
### Writing header file untitled_types.h
.
### Writing header file untitled.h
### Writing source file untitled.c
.
### Writing header file untitled_private.h
### Writing source file untitled_data.c
### Writing header file autobuild.h
.
### Writing source file untitled_main.c
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.0(26-Sep-2009) for Matlab R2008a.
<wbr>
<wbr>
Licence Accorded to  Demonstration Version
                     [adresse e-mail retirée]
                     Author : Lubin KERHUEL
                     WEBSITE : http://archive.kerhuel.eu/wiki
<wbr>
                     SIRENE : 503 920 456
                     SIRET : 503 920 456 00012
<wbr>
 Facturation to :    Demo
                     Demo
                     Lubin KERHUEL
                     18 avenue Joseph Lieutaud
                     13260 Cassis
                     FRANCE
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  archive.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: D:\Учеба\МАГИСТРАТУРА\Ветринский\библиотека PIC дляsimulink\dspic\dspic_pic30_gcc.tmf
### Creating untitled.mk from D:\Учеба\МАГИСТРАТУРА\Ветринский\библиотека PIC дляsimulink\dspic\dspic_pic30_gcc.tmf
### Building untitled: .\untitled.bat
<wbr>
C:\Users\Ї\Documents\MATLAB\untitled_dspic\sources&gt;set MATLAB=D:\Program Files\MATLAB\R2008a  
<wbr>
C:\Users\Ї\Documents\MATLAB\untitled_dspic\sources&gt;"D:\PROGRA~1\MATLAB\R2008a\bin\win32\gmake" -f untitled.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-gcc  -c -mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2008a/simulink/include -ID:\PROGRA~1\MATLAB\R2008a/extern/include -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\Users\п\Documents\MATLAB\untitled_dspic\sources -IC:\Users\п\Documents\MATLAB -ID:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc -ID:\PROGRA~1\MATLAB\R2008a\toolbox\dspblks\include -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\dspblks\c -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\comm\c\include   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_Multiplexed_out_UART1.c 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-gcc  -c -mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2008a/simulink/include -ID:\PROGRA~1\MATLAB\R2008a/extern/include -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\Users\п\Documents\MATLAB\untitled_dspic\sources -IC:\Users\п\Documents\MATLAB -ID:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc -ID:\PROGRA~1\MATLAB\R2008a\toolbox\dspblks\include -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\dspblks\c -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\comm\c\include   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_UART1_Interrupt.c 
dsPIC_UART1_Interrupt.c: In function '_U1TXInterrupt': 
dsPIC_UART1_Interrupt.c:19: warning:  PSV model not specified for '_U1TXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_UART1_Interrupt.c: In function '_U1RXInterrupt': 
dsPIC_UART1_Interrupt.c:31: warning:  PSV model not specified for '_U1RXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-gcc  -c -mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2008a/simulink/include -ID:\PROGRA~1\MATLAB\R2008a/extern/include -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\Users\п\Documents\MATLAB\untitled_dspic\sources -IC:\Users\п\Documents\MATLAB -ID:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc -ID:\PROGRA~1\MATLAB\R2008a\toolbox\dspblks\include -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\dspblks\c -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\comm\c\include   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    untitled_data.c 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-gcc  -c -mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2008a/simulink/include -ID:\PROGRA~1\MATLAB\R2008a/extern/include -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\Users\п\Documents\MATLAB\untitled_dspic\sources -IC:\Users\п\Documents\MATLAB -ID:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc -ID:\PROGRA~1\MATLAB\R2008a\toolbox\dspblks\include -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\dspblks\c -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\comm\c\include   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    untitled_main.c 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-gcc  -c -mcpu=30f2012 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -ID:\PROGRA~1\MATLAB\R2008a/simulink/include -ID:\PROGRA~1\MATLAB\R2008a/extern/include -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/ert -ID:\PROGRA~1\MATLAB\R2008a/rtw/c/src/ext_mode/common -IC:\Users\п\Documents\MATLAB\untitled_dspic\sources -IC:\Users\п\Documents\MATLAB -ID:\PROGRA~1\MATLAB\R2008a\rtw\c\libsrc -ID:\PROGRA~1\MATLAB\R2008a\toolbox\dspblks\include -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\dspblks\c -ID:\PROGRA~1\MATLAB\R2008a\toolbox\rtw\comm\c\include   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    untitled.c 
untitled.c: In function 'untitled_step': 
untitled.c:145: error: unrecognizable insn: 
(0x018c9eb0) (insn 234 42 44 2 (set (reg:SF 2 w2) 
        (unspec:SF [ 
                (mem:SF (plus:P16APSV (subreg:P16APSV (plus:HI (reg/f:HI 15 w15) 
                                (const_int -36 [0xffffffdc])) 0) 
                        (const_int 24 [0x18])) [0 S4 A16]) 
                (reg:HI 19 PSVPAG) 
            ] 62)) -1 (nil) 
    (nil)) 
untitled.c:145: internal compiler error: in extract_insn, at recog.c:2020 
Please submit a full bug report, 
with preprocessed source if appropriate. 
See &lt;URL:http://support.microchip.com&gt; for instructions. 
gmake: *** [untitled.o] Error 255 
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.</code></pre><br>
And simulink shows the window: <strong>Error building Real-Time Workshop target for block diagram 'untitled'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1138<br>
<br>
Error(s) encountered while building model "untitled".</strong><br>
<br>
Could you help me?<br>
<br>
I don't know, what does it means :?:  :?:  :?:</div>
</article>

<article class="forum-post" id="p967">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-19 15:00 UTC">2009-10-19 15:00 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">The error is there :<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Lizaveta</header>untitled.c:145: error: unrecognizable insn:<br>
<br>
(0x018c9eb0) (insn 234 42 44 2 (set (reg:SF 2 w2)<br>
<br>
        (unspec:SF [<br>
<br>
                (mem:SF (plus:P16APSV (subreg:P16APSV (plus:HI (reg/f:HI 15 w15)<br>
<br>
                                (const_int -36 [0xffffffdc])) 0)<br>
<br>
                        (const_int 24 [0x18])) [0 S4 A16])<br>
<br>
                (reg:HI 19 PSVPAG)<br>
<br>
            ] 62)) -1 (nil)<br>
<br>
    (nil))<br>
<br>
untitled.c:145: internal compiler error: in extract_insn, at recog.c:2020 </blockquote><br>
<br>
It seems to ba an compiler error ? I never see this error before. Could you upload your simulink model and precise which C30 compiler version you are working with ? can you compile model in the blockst example directory ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p968">
<header><strong>Lizaveta</strong><time datetime="2009-10-19 15:35 UTC">2009-10-19 15:35 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">Thank you for answer. If I understand you correctly, it's link for my model  <em><a href="http://rapidshare.com/files/295088629/bpsk.mdl.html">http://rapidshare.com/files/295088629/bpsk.mdl.html</a></em> :oops: <br>
<br>
To tell the truth, I am a beginner in generating c-code frome simulink model.<br>
<br>
I've installed MPLAB C30, MPLAB IDE v8.30.<br>
<br>
I should do the simple model, which contains modalator and demodulator, then generating c-code and after that upload it to MPLAB IDE. :wink:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/269-bpsk.mdl">Pièce jointe : bpsk.mdl</a></p>
</article>

<article class="forum-post" id="p969">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-19 16:14 UTC">2009-10-19 16:14 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">I do not have the communication blockset (with PSK modulation and so on). Thus, I cannot test the model right now. <br>
<br>
<br>
<br>
Perhaps the AWGN channel block is too complicated for the dsPIC your are using. Try several optimisation options in the real time workshop pannel options. (Simulation ==&gt; Real time workshop ==&gt; Optimization ==&gt; inline constant). If it still do not work, try to build theses high end blocks using simple functions. (you may try to look under mask of theses blocks, you may perhaps see how they are made).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p970">
<header><strong>Lizaveta</strong><time datetime="2009-10-19 16:35 UTC">2009-10-19 16:35 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">I've tried 'Simulation ==&gt; Real time workshop ==&gt; Optimization ==&gt; inline constant', but unfortunately it didn't help :( <br>
<br>
<strong>Can i ask, maybe later you'll be able to test it, cause I need it very much.</strong><br>
<br>
Actually i should do only modulator or encoder, but i couldn't do it, cause I had a problem with type of data. Output of modulator is complex signal and input of PIC block should be real. Can you advice me something?!<br>
<br>
I will be waiting for your answer. Thank you very much for your help.</div>
</article>

<article class="forum-post" id="p971">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-19 16:48 UTC">2009-10-19 16:48 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Lizaveta</header>Can i ask, maybe later you'll be able to test it, cause I need it very much</blockquote><br>
I have to find a matlab version with theses blocks available.<br>
<br>
<br>
<br>
Anyway, for the complex signal, there is a simulink block that convert complex signal into real part and imaginary part (theses two values are two reals), you may also convert them into one amplitude and one phase (make sense for communication)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p972">
<header><strong>Lizaveta</strong><time datetime="2009-10-19 17:21 UTC">2009-10-19 17:21 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body"><strong>Thanks! It'll be great, if you find it.<br>
<br>
</strong>I've tried to use such block (complex to real and im), but after it I don't know real or im will be input for PIC block, for example TX Output '<span class="underline">Multiplexed<br>
<br>
for Matlab / Labview'</span></div>
</article>

<article class="forum-post" id="p979">
<header><strong>Lizaveta</strong><time datetime="2009-11-02 16:29 UTC">2009-11-02 16:29 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body"><span class="underline"><em><strong>Hello Lubin! sorry for disturbing you! Can you answer my last messege! :oops: <br>
<br>
Did you try to check my model??????????????</strong></em></span></div>
</article>

<article class="forum-post" id="p980">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-02 19:02 UTC">2009-11-02 19:02 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">Hey Lizaveta,<br>
<br>
<br>
<br>
Sorry for the delay; I compiled successfully your model on matlab 2009b, with Microchip C30 v3_11.<br>
<br>
I get the .hex file without problems. <br>
<br>
<br>
<br>
However, I do not upload it on the forum as it seems to be a compilation test; the model will not do anything interesting. I think you will get always the same output: The output of the ADC is within [0 4096], let say it will hardly not take the 0 value. The BPSK (M-PSK) modulator baseband block will takes the input value as 1, as only two symbols are set (thus output is +1 or -1). As far as I understand, the block output is the phase information that must be used to modulate a signal, typically a sine wave. Adding AWGN noise to this phase information and demodulating directly with this signal seems wired. <br>
<br>
What about generating a real modulation using a PWM output as an analogue output (with RC filter)<br>
<br>
<br>
<br>
Anyway, this model compiled successfully here. Check your c30 version. (Type <strong>!pic30-gcc -v</strong> at the matlab prompt)<br>
<br>
Does examples compile properly (check the example directory of the blockset)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p981">
<header><strong>Lizaveta</strong><time datetime="2009-11-04 19:16 UTC">2009-11-04 19:16 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">Thank you, thank you very much! I am glad to hear that!<br>
<br>
May be you can send me this successful model to me!(I also have matlab 2009b)<br>
<br>
My e-mail <strong>[adresse e-mail retirée]</strong>.<br>
<br>
Please, cause it'll really helps me.<br>
<br>
You were using Compiler C30, weren't you?<br>
<br>
Can I use for compilation MPLAB IDE??<br>
<br>
I'am waiting eor answer.<br>
<br>
Thank you for your help!!!!!!!111111 :!:  :!:  :D</div>
</article>

<article class="forum-post" id="p986">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-04 23:15 UTC">2009-11-04 23:15 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">It's the same model as the one you posted !<br>
<br>
<br>
<br>
anyway, I used C30 directly from simulink (through the blockset)<br>
<br>
You can import all necessary file in MPLAB, but you need to configure the whole project. Do remember to add the required library. It may be better to let matlab to compile all necessary library into one object file that you will add in your mplab project.<br>
<br>
Usually, I do not use MPLAB, except to import the .hex or .coff file to program the target with an ICD2/real ice or equivalent.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/275-bpsk.mdl">Pièce jointe : bpsk.mdl</a></p>
</article>

<article class="forum-post" id="p989">
<header><strong>cjaskolski</strong><time datetime="2009-11-05 01:28 UTC">2009-11-05 01:28 UTC</time></header>
<h3>Re: Error using genMakefileAndBuild at 1138</h3>
<div class="forum-post-body">lizaveta,<br>
<br>
<br>
<br>
Assuming you get this to compile on your end, you should really check the load on the processor using the timing tools in the block set. From experience, using the PSK and AWGN blocks from the Communications blockset AND trying to run these with the double data type conversion at 1000Hz  on your processor (specified at 2.5MIPS in the configuration) is going to totally overwhelm the PIC microcontroller. Taking the double data type conversion out and running this all with fixed point numbers would help, but I would still keep on eye on the load. If you don't want to implement the load checking yourself,  set the "Overload Flag Port" on the dsPIC Master block to a pin and tie an LED to it. If the LED lights up, your algorithm is to much for the PIC.<br>
<br>
<br>
<br>
Corey</div>
</article>

<article class="forum-post" id="p1496">
<header><strong>jannypan</strong><time datetime="2011-03-05 06:10 UTC">2011-03-05 06:10 UTC</time></header>
<h3>Re: Communication blockset - bpsk modulation - Error  at 113</h3>
<div class="forum-post-body">You can import all necessary file in MPLAB, but you need to configure the whole project. Do remember to add the required library. It may be better to let matlab to compile all necessary library into one object file that you will add in your mplab project.</div>
</article>

<article class="forum-post" id="p1743">
<header><strong>yingxuy</strong><time datetime="2011-11-30 02:02 UTC">2011-11-30 02:02 UTC</time></header>
<h3>Re: Communication blockset - bpsk modulation - Error  at 113</h3>
<div class="forum-post-body">You need to configure the entire project. Do remember to add the required libraries. It might be better to let MATLAB Compiler to a target file all the necessary libraries, you will add in your MPLAB project.</div>
</article>

