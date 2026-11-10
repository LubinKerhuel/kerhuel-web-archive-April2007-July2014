---
title: "installation problems windows 7 64 bits"
url: "/forum/topic/473/"
archiveKind: "topic"
---
# installation problems windows 7 64 bits

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1809">
<header><strong>stephan</strong><time datetime="2012-01-18 14:46 UTC">2012-01-18 14:46 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
We met when you came in Salon de Provence to see M Bateman ,I work with him on oktokopter project.<br>
<br>
We have some installation problems. Our new computers run with windows 7 64 bits, so we installed Matlab 64 bits.<br>
<br>
On a first computer I had little problem but in the end, compilation of examples went to the end. I think that I was not on the right path! <br>
<br>
On a second computer with the same environement and the same conditions some problems come. The installation dsPIC blockset seems ok, but I try to compile examples many error appeared.<br>
<br>
In Matlab Set Path, instalted folder are declared.<br>
<br>
For example, I made a new design on simulink and use only dsPIC MASTER and doulbe-clik on it ,you can see on the picture message error. So somme files can be found ,and even this files are really installed.<br>
<br>
So I don't know how to resolve this kind of problem.<br>
<br>
Would you help use .<br>
<br>
<br>
<br>
Thanks <br>
<br>
<br>
<br>
Stephan</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/475-error%20message.png">Pièce jointe : error message.png</a></p>
</article>

<article class="forum-post" id="p1810">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-18 20:24 UTC">2012-01-18 20:24 UTC</time></header>
<h3>Re: installation problems windows 7 64 bits</h3>
<div class="forum-post-body">Hello Stephan,<br>
<br>
<br>
<br>
Glad to hear from you and Salon de Provence team. Did you add two motors to your hexacopter to get an oktokopter ?<br>
<br>
<br>
<br>
Regarding the problem you mentionned, please make sure that the three blockset folders (root, \dspic and \blocks ) exist in the matlab path.<br>
<br>
You might type &gt;&gt;path rehash to refresh the path cache (or you might try to change path cache setting in matlab preference).<br>
<br>
If the file is in the path, the path cache is refreshed or not activated, I could not provide explanations.<br>
<br>
The first folder of your installation path (install_dsPIC_R2010b_F_B...) seems quite long. Please try to shorten this folder name and adapt the matlab path consequently. <br>
<br>
<br>
<br>
I heard of problems when using windows vista due to user right limitation (IT seems than with Vista, Matlab can't save the path and the blockset folders must be added manually each time matlab is started).<br>
<br>
<br>
<br>
I am myself working with win7 0x64 without problems so far.<br>
<br>
<br>
<br>
Please let me know if you find the problem.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1816">
<header><strong>stephan</strong><time datetime="2012-01-23 08:32 UTC">2012-01-23 08:32 UTC</time></header>
<h3>Re: installation problems windows 7 64 bits</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I spent a week to understand my problem with the installation of dsPIC blockset. I did lots of manipulations in Matlab and windows but in the end the same error appear when I use your blockset.<br>
<br>
<br>
<br>
So in the end The only thing to verifiy was windows !<br>
<br>
<br>
<br>
So as we have some compentent computer scientist in Salon de Provence, I went to see my friend Philippe that propose to me to analyse the process when installing dsPIC blockset.For this he used a microsoft software called "Process monitor"<br>
<br>
<br>
<br>
<a href="http://technet.microsoft.com/fr-fr/sysinternals/bb896645">http://technet.microsoft.com/fr-fr/sysi ... s/bb896645</a><br>
<br>
<br>
<br>
After the use of good filters to isolate Matlab process ,he could see that MSVCR100.dll was missing, and when he looks for MSVCR100.dll in "system32" of windows he can see that it was missing <br>
<br>
<br>
<br>
<br>
So he downloads MSVCR100.dll and past it in "system32"<br>
<br>
<br>
<br>
MSVCR100.dll is a componant used with Visual Studio .<br>
<br>
<br>
<br>
So maybe if some people have this kind of problem ,Philippe thinks that is good to install a package called "vcredist" that install execution componants.<br>
<br>
<br>
<br>
<a href="http://support.microsoft.com/kb/259403/fr">http://support.microsoft.com/kb/259403/fr</a><br>
<br>
<br>
<br>
After this operation all was OK.<br>
<br>
<br>
<br>
So thanks a lot to my friend Philippe.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/477-dll_manquante_matlab.gif">Pièce jointe : dll_manquante_matlab.gif</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/479-ajout_dll_matlab.gif">Pièce jointe : ajout_dll_matlab.gif</a></p>
</article>

<article class="forum-post" id="p1830">
<header><strong>alpert</strong><time datetime="2012-02-10 18:03 UTC">2012-02-10 18:03 UTC</time></header>
<h3>Re: installation problems windows 7 64 bits</h3>
<div class="forum-post-body">Guinness!!!<br>
<br>
I had the same problem. I have tried everything to solve it, but i didn't realize that the problem is not in MATLAB.<br>
<br>
After i download "Microsoft Visual C++ 2010 Redistributable Package (x64)" all the problems have been solved.<br>
<br>
<br>
<br>
this is the link for the latest version for 64bit systems:<br>
<br>
<a href="http://www.microsoft.com/download/en/details.aspx?id=14632">http://www.microsoft.com/download/en/de ... x?id=14632</a><br>
<br>
<br>
<br>
Thank you very mach,<br>
<br>
Alpert</div>
</article>

<article class="forum-post" id="p1980">
<header><strong>marsh12</strong><time datetime="2013-01-24 06:51 UTC">2013-01-24 06:51 UTC</time></header>
<h3>Re: installation problems windows 7 64 bits</h3>
<div class="forum-post-body">i like this topic its good i like it</div>
</article>

