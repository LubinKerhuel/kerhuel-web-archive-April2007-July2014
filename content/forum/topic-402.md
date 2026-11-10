---
title: "processor specific configuration settings"
url: "/forum/topic/402/"
archiveKind: "topic"
---
# processor specific configuration settings

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1581">
<header><strong>ssw</strong><time datetime="2011-05-18 01:20 UTC">2011-05-18 01:20 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I'm working on a project to support a File IO to a thumb drive (for the PIC32MX795F512L) with the help of the dsPIC Blockset.<br>
<br>
Therefore I implemented some C code and call this one with the "C Function Call" Block.<br>
<br>
This C code uses the USB stack of the Microchips libraries. The generated code from MATLAB isn't working correctly.<br>
<br>
I used the generated MPLAB project file to adjust the project.<br>
<br>
To get it working, I have to set the heap size in the MPLAB project. I think, this can be done in MATLAB by adding<br>
<br>
--defsym=_min_heap_size=8192 to the LDFLAGS in the DsPIC options. So this is just a problem with a linker option and should not be the problem.<br>
<br>
<br>
<br>
But, I have to edit the code of the generated file "*_main.c" and have to add some other processor specific configuration settings.<br>
<br>
MATLAB is generating the follwing settings:<br>
<br>
<br>
<br>
#pragma config FPLLMUL = MUL_15, FPLLIDIV = DIV_1, FPLLODIV = DIV_256, FWDTEN = OFF<br>
<br>
#pragma config POSCMOD = XT, FNOSC = PRIPLL, FPBDIV = DIV_1<br>
<br>
<br>
<br>
If I replace these settings by:<br>
<br>
<br>
<br>
#pragma config UPLLEN = ON, FPLLMUL = MUL_20, UPLLIDIV = DIV_2, FPLLIDIV = DIV_2, FPLLODIV = DIV_1<br>
<br>
#pragma config FPBDIV = DIV_1, FWDTEN = OFF, WDTPS = PS1, FCKSM = CSDCMD, OSCIOFNC = OFF, POSCMOD = HS<br>
<br>
#pragma config IESO = OFF, FSOSCEN = OFF, FNOSC = PRIPLL, CP = OFF, BWP = OFF, PWP = OFF<br>
<br>
#pragma config ICESEL = ICS_PGx2, DEBUG = OFF<br>
<br>
<br>
<br>
So, my question is: Is there a way to manipulate this processor specific configuration settings in MATLAB?<br>
<br>
<br>
<br>
Hopefully you are able to help me.<br>
<br>
Best regards,<br>
<br>
ssw</div>
</article>

