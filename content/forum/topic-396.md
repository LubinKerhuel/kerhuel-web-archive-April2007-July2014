---
title: "Interfacing with an VN100 (INS/AHRS SENSOR)"
url: "/forum/topic/396/"
archiveKind: "topic"
---
# Interfacing with an VN100 (INS/AHRS SENSOR)

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1570">
<header><strong>ismaeelbit</strong><time datetime="2011-05-11 04:44 UTC">2011-05-11 04:44 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
Am working on Interfacing an INS/AHRS sensor with PIC24FJ126GA010 ON EXPLORER 16 board using SPI. The datasheet of the sensor is hereby attached. <br>
<br>
I already examined your example with respect to ADIS16100 rate gyro, I am trying to follow this example to communicate with this sensor but I dont know how you get the read command input to SPI and how to apply same to this sensor.<br>
<br>
<br>
<br>
I really need your assistance on this sensor.<br>
<br>
Thanks</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/412-UM001.pdf">Pièce jointe : UM001.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/413-developmental%20board%20VN100.pdf">Pièce jointe : developmental board VN100.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/414-UM003.pdf">Pièce jointe : UM003.pdf</a></p>
</article>

<article class="forum-post" id="p1603">
<header><strong>ismaeelbit</strong><time datetime="2011-06-13 11:05 UTC">2011-06-13 11:05 UTC</time></header>
<h3>Re: Interfacing with an VN100 (INS/AHRS SENSOR)</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I was able to compile a model for interfacing with an IMU sensor VN100 after series of debugging of the c-programme been used. However, when program the chip, it does not work.<br>
<br>
No error in compiling<br>
<pre><code>### Starting Real-Time Workshop build procedure for model: UAV_VN1002b
### Generating code into build directory: D:\EMBEDDED WORKS\BUILD CODES\UAV_VN1002b_dspic\sources
Warning: The file containing block diagram 'sensorMCUSlugsMKII' is shadowed by a file of the same name
higher on the MATLAB path. This can cause unexpected behaviour.  For more information see "Avoiding
Problems with Shadowed Files" in the Simulink documentation.
PT### Invoking Target Language Compiler on UAV_VN1002b.rtw
	tlc
	-r
	D:\EMBEDDED WORKS\BUILD CODES\UAV_VN1002b_dspic\sources\UAV_VN1002b.rtw
	C:\Documents and Settings\Admin\My Documents\MATLAB\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic\dspic.tlc
	-OD:\EMBEDDED WORKS\BUILD CODES\UAV_VN1002b_dspic\sources
	-IC:\Documents and Settings\Admin\My Documents\MATLAB\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic
	-IC:\Documents and Settings\Admin\My Documents\MATLAB\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\blocks
	-ID:\EMBEDDED WORKS\BUILD CODES\UAV_VN1002b_dspic\sources\tlc
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\mw
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\lib
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\blocks
	-IC:\Program Files\MATLAB\R2007b\rtw\c\tlc\fixpt
	-IC:\Program Files\MATLAB\R2007b\stateflow\c\tlc
	-aEnforceIntegerDowncast=1
	-aFoldNonRolledExpr=1
	-aInlineInvariantSignals=0
	-aInlineParameters=1
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
	-aGMAKE_PLACE="C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake"
	-aOPTIM_GCC="-mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2"
	-aLDFLAGS=" -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref"
	-aLDPICTYPE=" -Xlinker --script=C:\PROGRA~1\MICROC~1\MPLABC~2\support\PIC24F\gld\p24fJ128GA010.gld"
	-aLDLIBPIC=" C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\PIC24F\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a"
	-aPIC_INCLUDES=" -I C:\PROGRA~1\MICROC~1\MPLABC~2\include"
	-aPIC_REF="24fJ128GA010"
	-aGCCPATH=""
	-aGenerateTraceInfo=0
	-p10000
<wbr>
<wbr>
### Loading TLC function libraries
<wbr>
....
Warning:  The data type "ufix1" uses a word size that is not available on the intended target.  
    Fixed-point signals using this data type will be put inside a larger word.  When used, 
extra software will be generated to force this larger word to emulate a smaller
word.  This emulation is helpful when your prototype target and your final
production target are not the same.  If the smaller word size does NOT exist
on the final production target, then consider increasing the word size to
one that is supported.
<wbr>
.
### Initial pass through model to cache user defined code
.
### Caching model source code
...............
### Writing main
--- Multi Rate &amp; Single Tasking implementation
### Writing header file UAV_VN1002b_types.h
.
### Writing header file UAV_VN1002b.h
### Writing source file UAV_VN1002b.c
.
### Writing header file UAV_VN1002b_private.h
### Writing header file autobuild.h
### Writing source file UAV_VN1002b_main.c
.
### TLC code generation complete.
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.5b(29-May-2011) for Matlab R2007b.
<wbr>
<wbr>
Licence Accorded to  Ismaeel Tijani
                     [adresse e-mail retirée]
                     Faculty of Engineering
                     Intelligent Mechatronics Research Unit (IMRU)
                     Mechatronics Engineering Department
                     Faculty of Engineering,IIUM,KUALA LUMPUR
                     50728,MALAYSIA
<wbr>
 Facturation to :    Shahril Pawanchee
                     [adresse e-mail retirée]
                     Managing Director
                     WNF Resources Sdn Bhd
                     Kuala Lumpur, MALAYSIA
                     Tel: +603 6187 3179 Fax: +603 4147 3179
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  http://www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Documents and Settings\Admin\My Documents\MATLAB\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### UAV_VN1002b.mk which is generated from C:\Documents and Settings\Admin\My Documents\MATLAB\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic\dspic_pic30_gcc.tmf is up to date
### Building UAV_VN1002b: "C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f UAV_VN1002b.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\EMBEDD~1\BUILDC~1\UAV_VN~2\sources -ID:\EMBEDD~1\BUILDC~1 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    UAV_VN1002b_main.c 
''pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\EMBEDD~1\BUILDC~1\UAV_VN~2\sources -ID:\EMBEDD~1\BUILDC~1 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_Multiplexed_out_UART2.c 
''pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\EMBEDD~1\BUILDC~1\UAV_VN~2\sources -ID:\EMBEDD~1\BUILDC~1 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_UART2_Interrupt.c 
''pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\EMBEDD~1\BUILDC~1\UAV_VN~2\sources -ID:\EMBEDD~1\BUILDC~1 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    UAV_VN1002b.c 
" ================================================================" 
"*** Embedded Target for dsPIC by Lubin KERHUEL - http://www.kerhuel.eu" 
" | Licence Accorded to Ismaeel Tijani                           |" 
" |                     [adresse e-mail retirée]                     |"	     
" |          Companie : Faculty of Engineering                   |"  
" |                     Intelligent Mechatronics Research Unit (IMRU)|" 
" |                     Mechatronics Engineering Department      |" 		 
" |                     Faculty of Engineering,IIUM,KUALA LUMPUR |" 
" |                     50728,MALAYSIA                           |"		 		 
" | Financial Service : Shahril Pawanchee                        |" 
" | Contact             [adresse e-mail retirée]                     |" 
" |                     Managing Director                        |" 
" |                     WNF Resources Sdn Bhd                    |" 
" |                     Kuala Lumpur, MALAYSIA                   |" 
" |                     Tel: +603 6187 3179 Fax: +603 4147 3179  |" 
" | Version 3.5b                              29-May-2011        |" 
" | For Matlab 7.5             R2007b                            |" 
" ================================================================"	 
''pic30-gcc   -mcpu=24fJ128GA010  UAV_VN1002b_main.o VN100.o VN_lib.o VN_math.o VN_user.o dsPIC_Multiplexed_out_UART2.o dsPIC_UART2_Interrupt.o imu.o UAV_VN1002b.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\PIC24F\libpPIC24Fxxx-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a -o ..\../UAV_VN1002b.cof -Xlinker --script=C:\PROGRA~1\MICROC~1\MPLABC~2\support\PIC24F\gld\p24fJ128GA010.gld -Xlinker -t -Xlinker --report-mem -Xlinker -Map=../untitled.map -Xlinker --heap=0 -Xlinker -cref	  
c:\program files\microchip\mplab c30\bin\bin\..\bin/pic30-coff-ld.exe: mode pic30_coff 
UAV_VN1002b_main.o 
VN100.o 
VN_lib.o 
VN_math.o 
VN_user.o 
dsPIC_Multiplexed_out_UART2.o 
dsPIC_UART2_Interrupt.o 
imu.o 
UAV_VN1002b.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)delay32.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\PIC24F\libpPIC24Fxxx-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sqrtf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sinf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)cosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)atan2f.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)acosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)asinf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)tanf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)futil.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)errno.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sincosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)atanf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)asinacosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixsfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodrem.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x155fc] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x200               0x858           0xc84  (3204) 
.text                        0xa58              0x1cee          0x2b65  (11109) 
.dinit                      0x2746               0x13a           0x1d7  (471) 
.text                       0x2880               0x2b8           0x414  (1044) 
.isr                        0x2b38                 0x2             0x3  (3) 
<wbr>
                     Total program memory used (bytes):         0x3dd7  (15831) 12% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x2000] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.ndata                       0x800                   0           0x178  (376) 
.nbss                        0x978                   0            0xb4  (180) 
.ndata                       0xa2c                   0             0xc  (12) 
.nbss                        0xa38                   0             0x2  (2) 
<wbr>
                        Total data memory used (bytes):          0x23a  (570) 6% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                        0xa3a                              0x1dc6  (7622) 
<wbr>
                        Maximum dynamic memory (bytes):         0x1dc6  (7622) 
<wbr>
"    ---24fJ128GA010---" 
"*** Created "executable": ..\../UAV_VN1002b.cof"	 
''pic30-bin2hex ..\../UAV_VN1002b.cof  
"*** Converted UAV_VN1002b.cof to UAV_VN1002b.hex"	 
. 
"***   MPLAB: file -&gt; import, choose UAV_VN1002b.hex. Configure -&gt; Configuration Bits : Verify ! Download into the chip and run."		 
"***   Alternatively, (re-)compile the MPLAB project : Within Matlab, right-click UAV_VN1002b.mcp -&gt; open outside Matlab will open the MPLAB project. Compile, modify..."	 
### Successful completion of Real-Time Workshop build procedure for model: UAV_VN1002b</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/423-UAV_VN1002b.mdl">Pièce jointe : UAV_VN1002b.mdl</a></p>
</article>

<article class="forum-post" id="p1623">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-27 22:24 UTC">2011-06-27 22:24 UTC</time></header>
<h3>Re: Interfacing with an VN100 (INS/AHRS SENSOR)</h3>
<div class="forum-post-body">Hi Ismaeel,<br>
<br>
<br>
<br>
As I understand, you are willing to use the SPI drivers provided by Vector Nav to accec to the VN-100 variables.<br>
<br>
If I were you, I would use directly the dsPIC drivers. Including C files from others should just be more complicated, thus provided the required driver already exist and that its limitation is Ok with your application, just use it.<br>
<br>
<br>
<br>
The interresting document is UM001.pdf. page 13. provide an example of the sequence to send to the VN-100.<br>
<br>
for example, repeating sequence 01 08 00 00 00 00 00 00 will allows to get the computed Yaw,Pitch,Roll. (Do remember to set the Chip Select line properly.)<br>
<br>
This should be quite similar to what has been done with the ADIS16100 rate gyro you mentionned.<br>
<br>
<br>
<br>
Thus, first things is to check that SPI bus is working by having the VN-100 SPI output line to respond. Then, find the best sequence to be send to the VN-100 to get the data you want. Provided that sequence will be repeated, you might use the SPI block based on interrupt which will be even more efficient. (however, in a debuging step, prefere using the "standard" SPI block.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1633">
<header><strong>ismaeelbit</strong><time datetime="2011-07-01 04:50 UTC">2011-07-01 04:50 UTC</time></header>
<h3>Re: Interfacing with an VN100 (INS/AHRS SENSOR)</h3>
<div class="forum-post-body">Thanks for this reply. I have thougth of using SPI block directly, but my problem is that I am yet to figure out how best to send the series of bytes command to the SPI  using the blocksets, and also how to read out the response hex. data.<br>
<br>
<br>
<br>
In the example of the gyro sensor, you only send one byte of command to spi. If you have an idea or example on how to set-up the spi using the block sets to send the data I will be grateful to have it.<br>
<br>
<br>
<br>
I am working on cascading the SPI like you did for one Rx UART example! I may try that latter and update you in the mean time.</div>
</article>

<article class="forum-post" id="p1680">
<header><strong>resodad</strong><time datetime="2011-09-06 11:33 UTC">2011-09-06 11:33 UTC</time></header>
<h3>Re: Interfacing with an VN100 (INS/AHRS SENSOR)</h3>
<div class="forum-post-body">Ismaeel, <br>
<br>
I used SPI to read / write to EEPROM. It is somewhat different from your need, but some of the work may help you along. See my post:<br>
<br>
SPI EEPROM Record and Playback on Explorer 16<br>
<br>
Regards,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1740">
<header><strong>ismaeelbit</strong><time datetime="2011-11-19 08:02 UTC">2011-11-19 08:02 UTC</time></header>
<h3>Re: Interfacing with an VN100 (INS/AHRS SENSOR)</h3>
<div class="forum-post-body">Thanks John, I already got this sensor interfaced and working fine now.<br>
<br>
<br>
<br>
<br>
<br>
Hope to make my experience available once I get some free time</div>
</article>

