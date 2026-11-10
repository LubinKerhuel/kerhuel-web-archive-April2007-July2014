---
title: "compiling error for PIC32 starter kits"
url: "/forum/topic/495/"
archiveKind: "topic"
---
# compiling error for PIC32 starter kits

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1888">
<header><strong>ismaeelbit</strong><time datetime="2012-05-05 07:58 UTC">2012-05-05 07:58 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I am receiving compiling error wrt to "GenericTypeDefs.h:60: error: syntax error before '(' token" while am trying to compile a programme with 2 uart for both PIC32 starter kits and cerebot 32mx<br>
<br>
here is error message:<br>
<br>
<br>
<br>
### Processing Template Makefile: D:\LUBIN BLOCKSETS\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic\pic32_gcc.tmf<br>
<br>
-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating UAV_controllerMCU.mk from D:\LUBIN BLOCKSETS\install_dsPIC_R2007b_PhD_Ismaeel_Tijani_Shahril_Pawanchee_Malaysia (1)\dspic\pic32_gcc.tmf<br>
<br>
### Building UAV_controllerMCU: "C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f UAV_controllerMCU.mk  GENERATE_REPORT=0 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0<br>
<br>
''pic32-gcc  -c -mprocessor=32MX460F512L -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -ID:\EMBEDD~1\UAVDAQ~1\UAV_PI~1\UAV_CO~2\sources -ID:\EMBEDD~1\UAVDAQ~1\UAV_PI~1 -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -IC:\MICROC~1\PIC32S~1\MPLABC~1\pic32mx\include -IC:\MICROC~1\PIC32S~1\MPLABC~1\pic32mx\include\peripheral    UAV_controllerMCU_data.c <br>
<br>
UAV_controllerMCU_data.c:1: warning: Compiler option ignored due to an expired standard-evaluation period <br>
<br>
UAV_controllerMCU_data.c:1: warning: Disable the option or visit <a href="http://www.microchip.com/c32">http://www.microchip.com/c32</a> to purchase a full standard-edition license. <br>
<br>
In file included from C:/MICROC~1/PIC32S~1/MPLABC~1/pic32mx/include/peripheral/uart.h:52, <br>
<br>
                 from UAV_controllerMCU_private.h:40, <br>
<br>
                 from UAV_controllerMCU_data.c:28: <br>
<br>
C:/MICROC~1/PIC32S~1/MPLABC~1/pic32mx/include/GenericTypeDefs.h:60: error: syntax error before '(' token <br>
<br>
gmake: *** [UAV_controllerMCU_data.o] Error 1 <br>
<br>
### Real-Time Workshop build procedure for model: 'UAV_controllerMCU' aborted due <br>
<br>
<br>
<br>
I already tried to follow one of your response here, I comment out line 60 of the .h file, but error is the same.<br>
<br>
<br>
<br>
what could be the problem pls.<br>
<br>
<br>
<br>
thanks</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/508-UAV_controllerMCU_USBkit.mdl">Pièce jointe : UAV_controllerMCU_USBkit.mdl</a></p>
</article>

<article class="forum-post" id="p1889">
<header><strong>ismaeelbit</strong><time datetime="2012-05-05 08:18 UTC">2012-05-05 08:18 UTC</time></header>
<h3>Re: compiling error for PIC32 starter kits</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I removed one of the UART, and use only one 2A, it compiled without error. So the problem is ignited by the use of the two UART 1A and 2A at the same time.<br>
<br>
So, what can you suggest pls as way out.<br>
<br>
<br>
<br>
thanks</div>
</article>

