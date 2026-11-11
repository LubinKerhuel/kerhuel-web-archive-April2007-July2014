---
title: "error 255 - tcpip not found"
url: "/forum/topic/393/"
archiveKind: "topic"
---
# error 255 - tcpip not found

Forum : [General Remark and Questions](/forum/#forum-1)

10 message(s) · archive en lecture seule

<article class="forum-post" id="p1562">
<header><strong>joanpamo</strong><time datetime="2011-05-03 11:40 UTC">2011-05-03 11:40 UTC</time></header>
<div class="forum-post-body">Hello. Thank you for this great utility.<br>
<br>
<br>
<br>
I have a problem, and I don't know how solve it: when I compile a simple proyect (only with one configuration blockset) the next error occurs: <br>
<br>
<br>
<br>
<em>prueba1_main.c: In function '_FICD': <br>
<br>
prueba1_main.c:36: error: syntax error before '{' token <br>
<br>
gmake: *** [prueba1_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'prueba1' aborted due to an error.<br>
<br>
--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</em><br>
<br>
<br>
<br>
I searched the file <em>tcpip</em> in this directory, but it wasn't there.<br>
<br>
<br>
<br>
Thank you very much again</div>
</article>

<article class="forum-post" id="p1563">
<header><strong>LubinKerhuel</strong><time datetime="2011-05-03 12:06 UTC">2011-05-03 12:06 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : joanpamo</header>--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</blockquote>This is not the bug.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : joanpamo</header>prueba1_main.c: In function '_FICD':<br>
<br>
prueba1_main.c:36: error: syntax error before '{' token </blockquote> This is the bug.<br>
<br>
<br>
<br>
Which PIC/dsPIC did you choosed in the Master block ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1565">
<header><strong>joanpamo</strong><time datetime="2011-05-04 08:21 UTC">2011-05-04 08:21 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">Ok, I choosed <em>dsPIC 30f4013</em>, with the dsPIC master blockset</div>
</article>

<article class="forum-post" id="p1568">
<header><strong>LubinKerhuel</strong><time datetime="2011-05-06 16:43 UTC">2011-05-06 16:43 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">I used extensively the dsPIC30f4013 and it should not have this kind of bug.<br>
<br>
Could you please upload the simulink model you are using on that forum ? (upload attachment at the bottom).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1569">
<header><strong>joanpamo</strong><time datetime="2011-05-07 15:14 UTC">2011-05-07 15:14 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">I'm uploading the simulink model that I use. It's the example that there is on: <a href="/wiki/animation-compiling-your-first-model/">http://archive.kerhuel.eu/wiki/Animation_Co ... irst_model</a>, but it's applied to dsPIC30f4013. All properties of the dsPIC's blockset are default, in order not to get errors.<br>
<br>
<br>
<br>
In the last compilation, I changed from my computer to another that had installed winXP, instead win7 (like first one) And the result was:<br>
<br>
<br>
<br>
<em>***   Alternatively, (re-)compile the MPLAB project : Within Matlab, right-click example1.mcp -&gt; open outside Matlab will open the MPLAB project. Compile, modify..."	 <br>
<br>
### Successful completion of Real-Time Workshop build procedure for model: example1<br>
<br>
--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</em><br>
<br>
<br>
<br>
It still doesn't found <em>tcpip</em>, but there no error.<br>
<br>
<br>
<br>
<br>
<br>
I'm very grateful for your interest. Thank you very much again</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/411-example1.mdl">Pièce jointe : example1.mdl</a></p>
</article>

<article class="forum-post" id="p1831">
<header><strong>jekson</strong><time datetime="2012-02-11 06:31 UTC">2012-02-11 06:31 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">hello LubinKerhuel<br>
<br>
 thanks for the tool.<br>
<br>
I have the same problem joanpamo, this is my error.<br>
<br>
<br>
<br>
### Processing Template Makefile: C:\Users\alex\Documents\MATLAB\dspic\dspic_pic30_gcc.tmf<br>
<br>
-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating dsPIC_33f_Explorer16.mk from C:\Users\alex\Documents\MATLAB\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building dsPIC_33f_Explorer16: "C:\PROGRA~1\MATLAB\R2010a\bin\win32\gmake" -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0<br>
<br>
''pic30-gcc  -c -mcpu=24fJ96GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\alex\dsPIC_33f_Explorer16_dspic\sources -IC:\Users\alex -IC:\Users\alex\Documents\MATLAB\examples   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    dsPIC_33f_Explorer16_main.c <br>
<br>
In file included from c:/program files/microchip/mplab c30/bin/bin/../../support/peripheral_24F/timer.h:35, <br>
<br>
                 from dsPIC_33f_Explorer16_private.h:33, <br>
<br>
                 from dsPIC_33f_Explorer16_main.c:28: <br>
<br>
c:/program files/microchip/mplab c30/bin/bin/../../support/peripheral_24F/GenericTypeDefs.h:53: error: syntax error before '(' token <br>
<br>
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.<br>
<br>
--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.<br>
<br>
&gt;&gt;</div>
</article>

<article class="forum-post" id="p1832">
<header><strong>LubinKerhuel</strong><time datetime="2012-02-12 08:51 UTC">2012-02-12 08:51 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
TCP/Ip not found does not create an error. just a warning, not important.<br>
<br>
<br>
<br>
Your error is there : <br>
<br>
c:/program files/microchip/mplab c30/bin/bin/../../support/peripheral_24F/GenericTypeDefs.h:53: error: syntax error before '(' token<br>
<br>
typically, there are problems with boolean declaration. <br>
<br>
<br>
<br>
I thought the blocket handled this now. if not, you might just edit this .h file and check. commenting few lines usually resolve the problem.<br>
<br>
(there are few indication on this website/forum on that...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1833">
<header><strong>jekson</strong><time datetime="2012-02-12 21:56 UTC">2012-02-12 21:56 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">thanks for your prompt reply, do not take into account the tcpip error, and if I generated the code in mplab, but when compiling I get another problem.<br>
<br>
<br>
<br>
[tercer_fuzzy_dspic\sources\tercer_fuzzy.c: In function 'tercer_fuzzy_step':<br>
<br>
tercer_fuzzy_dspic\sources\tercer_fuzzy.c:121: internal compiler error: in expand_one_stack_var_at, at cfgexpand.c:515<br>
<br>
Please submit a full bug report,<br>
<br>
with preprocessed source if appropriate.]</div>
</article>

<article class="forum-post" id="p1834">
<header><strong>LubinKerhuel</strong><time datetime="2012-02-12 23:13 UTC">2012-02-12 23:13 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">Hello,<br>
<br>
that error should go to Microchip's compiler's team. I might help to reach them if you want.<br>
<br>
<br>
<br>
Anyway, my feeling is that fuzzy logic is not a great for embedded system. It typically required too much memory or to evluate complex math functions...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1835">
<header><strong>jekson</strong><time datetime="2012-02-13 01:43 UTC">2012-02-13 01:43 UTC</time></header>
<h3>Re: error 255 - tcpip not found</h3>
<div class="forum-post-body">I can help correct this problem, which I do, I need to finish this project.<br>
<br>
Thank you. :D</div>
</article>

