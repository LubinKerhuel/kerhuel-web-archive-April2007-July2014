---
title: "c 30 compiler problems with missing files"
url: "/forum/topic/560/"
archiveKind: "topic"
---
# c 30 compiler problems with missing files

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1964">
<header><strong>david.v</strong><time datetime="2012-11-26 21:25 UTC">2012-11-26 21:25 UTC</time></header>
<div class="forum-post-body">hi there,<br>
<br>
<br>
<br>
i'm  starting my bsc project with a ubd3 board<br>
<br>
while compiling i got lots of masseges like:<br>
<br>
<br>
<br>
pic30-coff-gcc.exe: C:\PROGRA~2\Microchip\MPLAB: No such file or directory <br>
<br>
pic30-coff-gcc.exe: C:\PROGRA~2\Microchip\MPLAB: No such file or directory <br>
<br>
pic30-coff-gcc.exe: C30\include: No such file or directory <br>
<br>
gmake: *** [Stab_UDB4_GPS_corect_distance_2_data.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'Stab_UDB4_GPS_corect_distance_2' aborted due to an error.<br>
<br>
--dir C:/PROGRA~2/Microchip/MPLAB not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/libpic30-coff.a not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/dsPIC33F/libp33fJ256GP710A-coff.a not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/libc-coff.a not found and not added to the MPLAB project.<br>
<br>
<br>
<br>
OR<br>
<br>
<br>
<br>
file not found : C:\PROGRA~2\Microchip\MPLAB<br>
<br>
file not found : C:\PROGRA~2\Microchip\MPLAB<br>
<br>
file not found : C:\PROGRA~2\Microchip\MPLAB<br>
<br>
file not found : C30\lib\libm-coff.a<br>
<br>
      --&gt; corrected : find in C:\PROGRA~2\Microchip\MPLAB C30\lib\libm-coff.a<br>
<br>
directory not found : C:\Program Files (x86)\Microchip\MPLAB C30\include<br>
<br>
<br>
<br>
OR<br>
<br>
<br>
<br>
### Processing Template Makefile: C:\Users\David\Desktop\PROject\DSpic_david\dspic\dspic_pic30_gcc.tmf<br>
<br>
-- Bypassing matlab internal LCC configuration --<br>
<br>
### Creating Stab_UDB4_GPS_corect_distance_2.mk from C:\Users\David\Desktop\PROject\DSpic_david\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Successful completion of Real-Time Workshop code generation for model: Stab_UDB4_GPS_corect_distance_2<br>
<br>
***  You could open project created and (re)compile it :<br>
<br>
   	  ==&gt; MPLAB 8: Within Matlab, right-click Stab_UDB4_GPS_corect_distance_2.mcp -&gt; open outside Matlab.<br>
<br>
   	  ==&gt; MPLAB X: Start MPLAB X, open the project folder C:\Users\David\Desktop\PROject\DSpic_david\Stab_UDB4_GPS_corect_distance_2_dspic<br>
<br>
--dir C:/PROGRA~2/Microchip/MPLAB not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/libpic30-coff.a not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/dsPIC33F/libp33fJ256GP710A-coff.a not found and not added to the MPLAB project.<br>
<br>
--file C30/lib/libc-coff.a not found and not added to the MPLAB project.<br>
<br>
<br>
<br>
<br>
<br>
i'm using r2010b , c30 v3.31 mplab 8.86<br>
<br>
how can i confure the blockset to find this files?<br>
<br>
<br>
<br>
thanks a head ,<br>
<br>
david.</div>
</article>

