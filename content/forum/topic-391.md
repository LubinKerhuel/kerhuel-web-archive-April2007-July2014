---
title: "Main function not found"
url: "/forum/topic/391/"
archiveKind: "topic"
---
# Main function not found

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1560">
<header><strong>konsgn</strong><time datetime="2011-04-29 13:10 UTC">2011-04-29 13:10 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
   I've been working on a model to write to an LCD display based on the PIC30F6015. I've been able to fix a memory error with an overflow in .bss by removing z^-1 delays in the thousands. However now that the memory error is fixed, I get to the output display from the PIC compiler telling me how much memory is used, followed by a "main" not found error. <br>
<br>
When I load the project in MPLAB, I cannot find the main function in any generated file. <br>
<br>
<br>
<br>
This is a sample output of what I am getting:<br>
<pre><code>" | Version 3.4cb                             11-Apr-2011        |" 
" | For Matlab 7.11            R2010b                            |" 
" ================================================================"	 
''pic30-gcc   -mcpu=30f6015  LCD_commands.o LCD_data.o SPI_cmd.o rtGetInf.o rtGetNaN.o rt_nonfinite.o LCD.o      C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f6015-coff.a C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a -o ..\../LCD.cof -Xlinker --script=C:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\dsPIC30F\gld\p30f6015.gld -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref	  
c:\program files\microchip\mplabc30\v3.25\bin\bin\..\bin/pic30-coff-ld.exe: mode pic30_coff 
LCD_commands.o 
LCD_data.o 
SPI_cmd.o 
rtGetInf.o 
rtGetNaN.o 
rt_nonfinite.o 
LCD.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\dsPIC30F\libp30f6015-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a)memset.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fne.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)floorf.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fpack.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)futil.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fchop.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)funpack.o 
(C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a)errno.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x100, Length = 0x17f00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x100               0x4e4           0x756  (1878) 
.const                       0x5e4               0xb2e          0x10c5  (4293) 
.text                       0x1112               0x450           0x678  (1656) 
.dinit                      0x1562                0x3a            0x57  (87) 
.text                       0x159c                0x46            0x69  (105) 
.isr                        0x15e2                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):         0x1f56  (8022) 5% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x1fa0] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.nbss                        0x800                   0           0x7f6  (2038) 
.ndata                       0xff6                   0            0x20  (32) 
.nbss                       0x1016                   0            0x18  (24) 
.ndata                      0x102e                   0             0x4  (4) 
.nbss                       0x1032                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):          0x834  (2100) 25% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                       0x1034                              0x176c  (5996) 
<wbr>
                        Maximum dynamic memory (bytes):         0x176c  (5996) 
<wbr>
C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a(crt0_standard.o)(.init+0x1a):crt0_standard.s: undefined reference to `main' 
C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a(crt0_standard.o)(.init+0x1c):crt0_standard.s: undefined reference to `main' 
c:\program files\microchip\mplabc30\v3.25\bin\bin\..\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../LCD.cof' 
gmake: *** [..\../LCD.cof] Error 255 </code></pre><br>
<br>
I will be attaching a zip file with the model and related c files.<br>
<br>
<br>
<br>
Also, Is there a better way of getting delays in seconds rather than using the memory intensive z^-1 block<br>
<br>
Thank you,<br>
<br>
Konsgn</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/410-LCD.zip">Pièce jointe : LCD.zip</a></p>
</article>

<article class="forum-post" id="p1572">
<header><strong>konsgn</strong><time datetime="2011-05-12 14:12 UTC">2011-05-12 14:12 UTC</time></header>
<h3>Re: Main function not found</h3>
<div class="forum-post-body">Hi All,<br>
<br>
I got the error fixed. By moving it to a folder located within the subdirectories that also house the dsPIC install, it started working. <br>
<br>
<br>
<br>
I do still have a couple of questions.<br>
<br>
<br>
<br>
1. Why does the z^-1 delay block take up a ridiculous amount of memory? Does it create a variable for every timestep from start to end?<br>
<br>
2. What is the best block to use for a delay in seconds?<br>
<br>
3. Is there a way to format hex float to string in Simulink, or will I have to use a Custom C call to fprintf?<br>
<br>
<br>
<br>
Thank you,<br>
<br>
Konsgn</div>
</article>

