---
title: "Sintax Error in Microchip Header File? - .c and .s ext files"
url: "/forum/topic/117/"
archiveKind: "topic"
---
# Sintax Error in Microchip Header File? - .c and .s ext files

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p332">
<header><strong>malife</strong><time datetime="2008-05-07 19:46 UTC">2008-05-07 19:46 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I am trying to implement the software emulation EEPROM as described in Microchip's App Note AN1095 <a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1824&amp;appnote=en530593">http://www.microchip.com/stellent/idcpl ... e=en530593</a>. This is what I am doing:<br>
<br>
<br>
<br>
I downloaded the code and renamed the C, S and H files to DEE.c, DEE.s and DEE.h respectively. Then I added those to the Simulink model via Simulation -&gt; Configuration Parameters -&gt; Custom Code. I place the S and C files in Source Files and the H file in Header File. I am still not doing anything with the model except flashing an LED and trying to compile. When I compile I get this error:<br>
<br>
<br>
<pre><code>---------------------------------------------------
Embedded Coder for dsPIC V0.96b2(17-Mar-2008) for Matlab R2007a.
Licence Accorded to Mariano I. Lizarraga - University of California Santa Cruz
<wbr>
<wbr>
informations available at  archive.kerhuel.eu 
<wbr>
.
### Processing Template Makefile: C:\Mariano\MATLAB\dsPICBlock\dspic\dspic_pic30_gcc.tmf
### Wrapping unrecognized make command (angle brackets added)
###    &lt;C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake&gt;
### in default batch file
### SPIMasterTest.mk which is generated from C:\Mariano\MATLAB\dsPICBlock\dspic\dspic_pic30_gcc.tmf is up to date
### Building SPIMasterTest: .\SPIMasterTest.bat
<wbr>
C:\Mariano\AP\Simulink\SPIMasterTest_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007a  
<wbr>
C:\Mariano\AP\Simulink\SPIMasterTest_dspic\sources&gt;C:\PROGRA~1\MATLAB\R2007a\rtw\bin\win32\gmake -f SPIMasterTest.mk  GENERATE_REPORT=1 ADD_MDL_NAME_TO_GLOBALS=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
pic30-gcc  -c -mcpu=33FJ256MC710 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007a/simulink/include -IC:\PROGRA~1\MATLAB\R2007a/extern/include -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007a/rtw/c/src/ext_mode/common -IC:\Mariano\AP\Simulink\SPIMasterTest_dspic\sources -IC:\Mariano\AP\Simulink -IC:\Mariano\AP\Simulink\C_Code -IC:\PROGRA~1\MATLAB\R2007a\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    SPIMasterTest_main.c 
Microchip MPLAB C30 License Manager Version v3_02 (Build Date Nov  9 2007). 
Copyright (c) 2005 Microchip Technology Inc. All rights reserved. 
The MPLAB C30 license has expired. 
pic30-coff-cc1.exe: warning: Options have been disabled due to expired license 
In file included from c:/program files/microchip/mplab c30/bin/../support/h/p33fxxxx.h:122, 
                 from SPIMasterTest_private.h:32, 
                 from SPIMasterTest_main.c:28: 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7618: error: syntax error before numeric constant 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7620: error: syntax error before ':' token 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7621: error: syntax error before ':' token 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7622: error: syntax error before ':' token 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7630: error: syntax error before '}' token 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7632: error: syntax error before 'NVMCONbits' 
c:/program files/microchip/mplab c30/bin/../support/h/p33FJ256MC710.h:7632: error: sfr attribute requires extern storage class 
gmake: *** [SPIMasterTest_main.o] Error 0xff 
### Real-Time Workshop build procedure for model: 'SPIMasterTest' aborted due to an error.</code></pre><br>
<br>
Now, for a minute I contemplated the fact that the Header File could have a syntax error, I checked it and it does not. Also, I then compiled the downloaded MPLab  project that comes with the App Note without any complaints.<br>
<br>
<br>
<br>
I have attached the Mdl and the C, S and H files. Any help would be greatly appreciated.<br>
<br>
<br>
<br>
Mariano</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/73-DEEMdl.zip">Pièce jointe : DEEMdl.zip</a></p>
</article>

<article class="forum-post" id="p333">
<header><strong>malife</strong><time datetime="2008-05-07 20:15 UTC">2008-05-07 20:15 UTC</time></header>
<h3>Re: Sintax Error in Microchip Header File?</h3>
<div class="forum-post-body">It turns out I found the problem. Actually there were 2 problems. I hope Lubin has a clear explanation for the first one:<br>
<br>
<br>
<br>
1.- H File: The H file SHOULD NOT go in the Simulation-&gt;Config Parameters dialog. You just need to include it in your C file. No clue why.<br>
<br>
<br>
<br>
2.- DEE.C and DEE.S both created a DEE.o object which when linked, broke everything :-S. Yes I know, simple one, sorry :-).<br>
<br>
<br>
<br>
I am posting this to help anybody else in the same boat.<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p334">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-07 20:29 UTC">2008-05-07 20:29 UTC</time></header>
<h3>Re: Sintax Error in Microchip Header File?</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
I converged to the same solution. You were quicker! <br>
<br>
<br>
<br>
Anyway, the model compile without any 'C function Call' block, but when I am trying to access to one function, It is not ok !<br>
<br>
It has maybe to do with the .h file that we do not declare...<br>
<br>
<br>
<pre><code>SPIMasterTest.o(.text+0xe2):C:\prog\Matlab2\RTWdsPIC\Developpements\Forum\Mariano_EEPROM\SPIMasterTest_dspic\sources\SPIMasterTest.c: undefined reference to `GetPagePackSkipped' </code></pre><br>
<br>
I noticed that when we include the .h file, error appears on a specific part of the .h file where we have syntax that I am not used to ... ( : start a 2 lines ?)<br>
<pre><code>__extension__ typedef struct tagNVMCONBITS {
  union {
    struct {
      unsigned NVMOP:4;
      unsigned :2;
      unsigned ERASE:1;
      unsigned :6;
      unsigned WRERR:1;
      unsigned WREN:1;
      unsigned WR:1;
    };
    struct {
      unsigned NVMOP0:1;
      unsigned NVMOP1:1;
      unsigned NVMOP2:1;
      unsigned NVMOP3:1;
    };
  };
} NVMCONBITS;</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/74-Mariano_EEPROM.zip">Pièce jointe : Mariano_EEPROM.zip</a></p>
</article>

<article class="forum-post" id="p335">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-07 20:43 UTC">2008-05-07 20:43 UTC</time></header>
<h3>Re: Sintax Error in Microchip Header File?</h3>
<div class="forum-post-body">I guess I did not choose the right function name to call.<br>
<br>
<br>
<br>
This model compile.<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/75-Mariano_EEPROM2.zip">Pièce jointe : Mariano_EEPROM2.zip</a></p>
</article>

