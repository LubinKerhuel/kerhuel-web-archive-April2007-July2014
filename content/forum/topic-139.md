---
title: "Using 2 UART"
url: "/forum/topic/139/"
archiveKind: "topic"
---
# Using 2 UART

Forum : [dsPIC Peripherals](/forum/#forum-9)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p417">
<header><strong>Stefano</strong><time datetime="2008-06-11 12:26 UTC">2008-06-11 12:26 UTC</time></header>
<div class="forum-post-body">Hi, I need to use two UARTs to communicate with the serial port of a pc and with the serial port of a DC motor controller. For this purpose I'm using a dsPIC30F3011 which has one UART1, one UART1 Alternative and one UART2. Unfortunately I'm having this problems: <br>
<br>
<br>
<br>
1) In the dsPIC toolbox the dsPIC30f3011 has only one UART1 (and one UART1 Alternative), I think that this is a bug. To enable also the UART2 I have modified the  property “nuart” in the item number 15 of the file "dspicliste.mat" substituting the existing value with the new value [1 2]. In this way I can select UART1 and UART2 in the dsPICtoolbox... is it correct?<br>
<br>
<br>
<br>
2) everything works fine if I use only one UART (1 or 2), but if I try to use two UARTs, using two "UART configuration" blocks, the compile process generates this error<br>
<br>
&lt;&lt;<br>
<br>
dsPIC_UART2_Interrupt.c: In function '_U2TXInterrupt': <br>
<br>
dsPIC_UART2_Interrupt.c:19: warning:  PSV model not specified for '_U2TXInterrupt'; <br>
<br>
   assuming 'auto_psv' this may affect latency <br>
<br>
dsPIC_UART2_Interrupt.c: In function '_U2RXInterrupt': <br>
<br>
dsPIC_UART2_Interrupt.c:31: warning:  PSV model not specified for '_U2RXInterrupt'; <br>
<br>
   assuming 'auto_psv' this may affect latency <br>
<br>
pic30-gcc  -c -mcpu=30f3011 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -Ic:\MyToolbox\blocks\Test_2_RS232_dspic\sources -Ic:\MyToolbox\blocks -IC:\Users\stefano\Desktop\CONTRO~3\example -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    Test_2_RS232.c <br>
<br>
Test_2_RS232.c: In function 'Test_2_RS232_step1': <br>
<br>
Test_2_RS232.c:111: error: 'RxPtrHaut_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:111: error: (Each undeclared identifier is reported only once <br>
<br>
Test_2_RS232.c:111: error: for each function it appears in.) <br>
<br>
Test_2_RS232.c:111: error: 'RxPtrBas_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:112: error: 'RxTab_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:113: error: 'Rx_BUFF_SIZE_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c: In function 'Test_2_RS232_initialize': <br>
<br>
Test_2_RS232.c:271: error: 'TxPtrHaut_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:272: error: 'TxPtrBas_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:273: error: 'RxPtrHaut_Uart1' undeclared (first use in this function) <br>
<br>
Test_2_RS232.c:274: error: 'RxPtrBas_Uart1' undeclared (first use in this function) <br>
<br>
gmake: *** [Test_2_RS232.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'Test_2_RS232' aborted due to an error.<br>
<br>
&gt;&gt;<br>
<br>
I get the same error even if I try to use another dsPIC with two UARTS (without modifying the file "dspicliste.mat").<br>
<br>
<br>
<br>
Can you tell me if it is possible to enable two serial communications within the same dsPIC and how to do it?<br>
<br>
<br>
<br>
Tank you<br>
<br>
<br>
<br>
PS: I've attached to this post the file that I'm using to perform the tests...</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/90-Test_2_RS232.mdl">Pièce jointe : Test_2_RS232.mdl</a></p>
</article>

<article class="forum-post" id="p421">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-11 23:26 UTC">2008-06-11 23:26 UTC</time></header>
<h3>Re: Using 2 UART</h3>
<div class="forum-post-body">Hi Stefano,<br>
<br>
<br>
<br>
Thanks for reporting this bug. It should be corrected now.<br>
<br>
Please, have a look on the experimental version of the blockset on the <a href="/RTWdsPIC/ReleaseNotes.html">Release Note</a> Page (Bottom).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p422">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-12 07:56 UTC">2008-06-12 07:56 UTC</time></header>
<h3>Re: Using 2 UART</h3>
<div class="forum-post-body">Hi Stefano,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Stefano</header>the file "dspicliste.mat" substituting the existing value with the new value [1 2]</blockquote><br>
This solution is correct in this very specific case. However, in most case, it will not work since severals entry have to be coherent so as to generate a correct C code. The entry has been corrected in the last version of the blockset (0.98c).</div>
</article>

<article class="forum-post" id="p423">
<header><strong>Stefano</strong><time datetime="2008-06-12 21:18 UTC">2008-06-12 21:18 UTC</time></header>
<h3>Re: Using 2 UART</h3>
<div class="forum-post-body">Thanks Lubin for the fast new release… I will try it as soon as I come back to my office…</div>
</article>

