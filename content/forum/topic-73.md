---
title: "Issues in dsPIC 30f6014 compiling : Missing gld &amp; DCI Periph"
url: "/forum/topic/73/"
archiveKind: "topic"
---
# Issues in dsPIC 30f6014 compiling : Missing gld &amp; DCI Periph

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p151">
<header><strong>Anonyme</strong><time datetime="2008-01-17 06:24 UTC">2008-01-17 06:24 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
      I've created a trial model for dsPIC 30f6014 to test the dsPIC embedded target in R2007b. But, I am not being able to compile the model (flash_1.mdl). I am getting the following error:<br>
<br>
C:\Program Files\Microchip\MPLAB C30\bin\pic30-coff-ld.exe: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~1\support\gld\p30f6014.gld: No such file or directory <br>
<br>
gmake: *** [..\../flash_1.coff] Error 255 <br>
<br>
<br>
<br>
It seems that the compiler cannot find the linker file. This, inspite of the fact that I've installed MPLab C30 v3.02 and verified the path for the gld file (p30f6014.gld) - default path (C:\Program Files\Microchip\MPLAB C30\support\gld). I'm not even being able to compile the example models included in the "Embedded target".<br>
<br>
If I try to just take the generated code and try to compile it independently in MPLab, it is throwing error for undefined function (ConfigIntTimer1). <br>
<br>
I've already confirmed that there is no problem with the test model or settings after communicating with Lubin. Still, if anybody wants, I can send the model.<br>
<br>
<br>
<br>
There is another query:<br>
<br>
Is there a way to implement the DCI module in dsPIC 30f6014 using the dsPIC blockset? It would be very helpful if there is.<br>
<br>
I request you to help with your suggestions.<br>
<br>
<br>
<br>
Thanks.<br>
<br>
-sumedhk</div>
</article>

<article class="forum-post" id="p152">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-17 10:50 UTC">2008-01-17 10:50 UTC</time></header>
<h3>Re: Issues in dsPIC 30f6014 compiling : Missing gld &amp;amp; DCI Periph</h3>
<div class="forum-post-body">Hi sumedhk<br>
<br>
<br>
<br>
I use short path name ("compatible 8.3") to invoke the C30 compiler in Matlab.<br>
<br>
Perhaps that the short path name for the directory 'C:\Program Files\Microchip\MPLAB C30\support\gld' is false.<br>
<br>
( for example, it could be <br>
<br>
C:\PROGRA~1\MICROC~1\MPLABC~1 or <br>
<br>
C:\PROGRA~1\MICROC~2\MPLABC~1<br>
<br>
<br>
<br>
You can check by typing at the matlab prompt the command: <br>
<br>
rtw_alt_pathname('C:\Program Files\Microchip\MPLAB C30\support\gld')<br>
<br>
<br>
<br>
If you do not get C:\PROGRA~1\MICROC~1\MPLABC~1, you will have to change the short path in Simulink :  <br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; Real-Time Workshop ==&gt; DsPIC options<br>
<br>
<br>
<br>
Please, repport if this correct the problem. I will then correct this in the next toolbox version.<br>
<br>
<br>
<br>
About DCI, I did not create the block yet. You could use your own code for that peripheral using the Custom C Function block (not available in the evaluation version).<br>
<br>
Could you explain what is DCI for. I did not see yet any electronic component using this protocol.<br>
<br>
<br>
<br>
PS: CAN and I2C blocks will be released soon...<br>
<br>
<br>
<br>
--<br>
<br>
You could not upload the mdl file because you were not registered to the forum. I just modified the forum right and you could now upload file despite the fact that you are not registered. Note however that you will have more possibilities once registered...</div>
</article>

<article class="forum-post" id="p153">
<header><strong>Anonyme</strong><time datetime="2008-01-18 05:52 UTC">2008-01-18 05:52 UTC</time></header>
<h3>Re: Issues in dsPIC 30f6014 compiling : Missing gld &amp;amp; DCI Periph</h3>
<div class="forum-post-body">Done. The model is compiling now. There was a slight correction I had to make - changed MPLABC~1 to MPLABC~2.<br>
<br>
<br>
<br>
Regarding the DCI module... It is used by the DSC to talk with si3000 (voiceband codec). The communication is done using the pins RG15 (COFS), RG13 (SDI) and RG12 (SDO). Writing of code for the same is already underway.<br>
<br>
<br>
<br>
Thanks again.</div>
</article>

