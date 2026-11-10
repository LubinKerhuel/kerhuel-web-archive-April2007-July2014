---
title: "Pathing Problem in Compilation"
url: "/forum/topic/241/"
archiveKind: "topic"
---
# Pathing Problem in Compilation

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p918">
<header><strong>chad</strong><time datetime="2009-07-27 22:30 UTC">2009-07-27 22:30 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
When I try to compile models such as dsPIC_33f_Explorer16.mdl, I get the 1070 build error due to MATLAB not being able to find the gld file.  For instance, MATLAB will search C:\Program Files\Micro~1\MPLABC~1\...   which goes to C:\Program Files\Microchip\MPLAB C32  instead of C:\Program Files\Microchip\MPLAB C30,  while C:\Program Files\Micro~1\MPLABC~2\... goes to C:\Program Files\Microchip\MPLAB C30.  I was only able to compile after I renamed my MPLAB C32 folder to "MPLAB C30 Copy" and copied and pasted the "MPLAB C30" folder contents into "MPLAB C30 Copy."<br>
<br>
<br>
<br>
Do you know why MATLAB is searching for the wrong # after the '~' during compilation?   Is there a way to tell MATLAB to look in the right folder?  I tried adding the path to MATLAB, and it didn't solve the problem.</div>
</article>

<article class="forum-post" id="p919">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-28 08:50 UTC">2009-07-28 08:50 UTC</time></header>
<h3>Re: Pathing Problem in Compilation</h3>
<div class="forum-post-body">Hi Chad,<br>
<br>
<br>
<br>
Did you tried the "magic" yellow block called something like "<strong>configure Simulink model for dsPIC</strong>" ? add this block to your model, dbl click on it and it usually solved path problems.<br>
<br>
<br>
<br>
Lubin</div>
</article>

