---
title: "problems with toolbox DSPIC"
url: "/forum/topic/246/"
archiveKind: "topic"
---
# problems with toolbox DSPIC

Forum : [bug reports](/forum/#forum-8)

11 message(s) · archive en lecture seule

<article class="forum-post" id="p950">
<header><strong>ATMC</strong><time datetime="2009-09-21 23:37 UTC">2009-09-21 23:37 UTC</time></header>
<div class="forum-post-body">HI<br>
<br>
 I'm trying to use the toolbox ds_PIC_R2009a, and I am not able to open the dsPIC Master block.<br>
<br>
 The message is that appears in command windows the following:<br>
<br>
<br>
<br>
<span style="color:#0040ff">Enter C30 compiler directory (like C:\Program Files\Microchip\MPLAB C30<br>
<br>
 (You have to do it twice, copy-past)<br>
<br>
 ----&gt;C:\Arquivos de programas\Microchip\MPLAB C30<br>
<br>
C30 Compiler found<br>
<br>
Warning: Corrupted package, Remove and Re-install dsPic<br>
<br>
embedded Target toolbox. <br>
<br>
&gt; In C:\Arquivos de programas\Microchip\MPLAB C30\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 154<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master<br>
<br>
block (mask) 'dsPICdrivers/Master'. Corrupted package,<br>
<br>
Remove and Re-install dsPic embedded Target toolbox. <br>
<br>
&gt; In C:\Arquivos de programas\Microchip\MPLAB C30\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 154<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Corrupted package, Remove and Re-install dsPic<br>
<br>
embedded Target toolbox. <br>
<br>
&gt; In C:\Arquivos de programas\Microchip\MPLAB C30\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 154<br>
<br>
  In uiopen at 196<br>
<br>
Warning: Error evaluating 'LoadFcn' callback of Master<br>
<br>
block (mask) 'Data_Login_Matlab/Master'. Corrupted package,<br>
<br>
Remove and Re-install dsPic embedded Target toolbox. <br>
<br>
&gt; In C:\Arquivos de programas\Microchip\MPLAB C30\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p&gt;dsPIC_UART_TX_Labview_Matlab_callback at 36<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 154<br>
<br>
  In uiopen at 196</span><br>
<br>
<br>
<br>
I hope you can help me<br>
<br>
 Kind Regards,<br>
<br>
                Cavalcante</div>
</article>

<article class="forum-post" id="p951">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-22 08:35 UTC">2009-09-22 08:35 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Hi Cavalcante,<br>
<br>
<br>
<br>
did you updated the blockset ? <br>
<br>
<br>
<br>
This error appears if the new blockset find an old file from the old blockset (in the matlab path before the new blockst path), or if a file has been modified (or is corrupted)<br>
<br>
Solution is to delete all files from the blockst installation directory , install the blockset again, and sometime restart matlab.<br>
<br>
<br>
<br>
Anyway, do you have microchip blockset installed on your computer. Both blockset should cohabitate on the same matlab, but I did not tested it further. Please let me know if you solved the problem or not.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p953">
<header><strong>ATMC</strong><time datetime="2009-09-22 20:21 UTC">2009-09-22 20:21 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
 Thanks for your quick response.<br>
<br>
  No, I am not update the block set, and I am trying anytime install de program in differ directories and every time i have  same error. In funcion of the install i think that everything.<br>
<br>
 And i'm not had the microchip blockset diinstal in my PC.<br>
<br>
<br>
<br>
regards<br>
<br>
    Cavalacante</div>
</article>

<article class="forum-post" id="p954">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-22 21:12 UTC">2009-09-22 21:12 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Try to clean up the matlab path <br>
<br>
<br>
<br>
Which matlab version are you using ?<br>
<br>
I should test that !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p955">
<header><strong>ATMC</strong><time datetime="2009-09-23 01:23 UTC">2009-09-23 01:23 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">I will try and follow up the result<br>
<br>
 The version is Matlab2009a<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p956">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-23 08:11 UTC">2009-09-23 08:11 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Please let me know the result, I will have a close look if you still encounter this problem.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p958">
<header><strong>ATMC</strong><time datetime="2009-09-25 01:06 UTC">2009-09-25 01:06 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">yes, the problem persists even cleaning the matlab path, I tried install in other PC with matlab r2009a and I had the same problem.<br>
<br>
 thank you for your attention<br>
<br>
 <br>
<br>
     Cavalcante</div>
</article>

<article class="forum-post" id="p959">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-25 20:24 UTC">2009-09-25 20:24 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Ok, I reproduced the bug, I'll look at it very soon. It may be a new bug that appears in the last blockset update<br>
<br>
I'll post a message when it's repaired (I hope in few days)<br>
<br>
<br>
<br>
Thanks for repporting it !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p961">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-26 17:02 UTC">2009-09-26 17:02 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Bug find and solved.<br>
<br>
<br>
<br>
Please download and try the last blockst version, let me know if it's working as expected !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p962">
<header><strong>ATMC</strong><time datetime="2009-09-26 21:26 UTC">2009-09-26 21:26 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Thank you for your attention. <br>
<br>
In the next two weeks will not be able to get close to the toolbox, but so testing will give you return.<br>
<br>
regards<br>
<br>
 Cavalcante</div>
</article>

<article class="forum-post" id="p973">
<header><strong>ATMC</strong><time datetime="2009-10-19 21:40 UTC">2009-10-19 21:40 UTC</time></header>
<h3>Re: problems with toolbox DSPIC</h3>
<div class="forum-post-body">Sorry about the delay in response, it worked perfectly. <br>
<br>
Thank you for your support.<br>
<br>
<br>
<br>
regards<br>
<br>
    Cavalcante</div>
</article>

