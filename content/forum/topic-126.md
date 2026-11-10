---
title: "Compiling error p**.gld:9: syntax error - solved"
url: "/forum/topic/126/"
archiveKind: "topic"
---
# Compiling error p**.gld:9: syntax error - solved

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p382">
<header><strong>Anonyme</strong><time datetime="2008-05-23 08:45 UTC">2008-05-23 08:45 UTC</time></header>
<div class="forum-post-body">Dear All,<br>
<br>
I was trying to compile the example models (in this case Data_Login_Matlab.m) for several pic's, and got errors during compilation.<br>
<br>
I have ML R2008a, and<br>
<br>
"MPLAB® C Compiler for PIC24 MCUs and dsPIC DSCs, v3.10 (B), 9 May 2008"<br>
<br>
<br>
<br>
The error message in the matlab command window was:<br>
<br>
c:\program files\microchip\pic30_tools\bin\pic30-coff-ld.exe:C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC33F\gld\p33fJ256GP710.gld:9: syntax error <br>
<br>
gmake: *** [..\../dsPIC_33f_Explorer16.coff] Error 255 <br>
<br>
<br>
<br>
The solution was - thank You again, Mr. Kerhuel - to remove (or comment, as shown below) line 9 of the .gld file:<br>
<br>
/*<br>
<br>
** OPTIONAL(-lp33FJ256GP710)<br>
<br>
*/<br>
<br>
<br>
<br>
Best regards:<br>
<br>
David</div>
</article>

