---
title: "Problem using PWM_motor - Solved"
url: "/forum/topic/163/"
archiveKind: "topic"
---
# Problem using PWM_motor - Solved

Forum : [General Remark and Questions](/forum/#forum-1)

10 message(s) · archive en lecture seule

<article class="forum-post" id="p547">
<header><strong>murali</strong><time datetime="2008-10-04 13:48 UTC">2008-10-04 13:48 UTC</time></header>
<div class="forum-post-body">hi!<br>
<br>
 I am trying to use one of the PWM channels of dsPIC,but while generating the c-code..it is giving the following error:<br>
<br>
<br>
<br>
PWM.c: In function 'PWM_initialize': <br>
<br>
PWM.c:61: error: 'PWM_INT_DIS' undeclared (first use in this function) <br>
<br>
PWM.c:61: error: (Each undeclared identifier is reported only once <br>
<br>
PWM.c:61: error: for each function it appears in.) <br>
<br>
PWM.c:61: error: 'PWM_FLTA_DIS_INT' undeclared (first use in this function) <br>
<br>
PWM.c:61: error: 'PWM_INT_PR1' undeclared (first use in this function) <br>
<br>
PWM.c:61: error: 'PWM_FLTA_INT_PR0' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_EN' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_OP_SCALE1' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_IPCLK_SCALE4' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_MOD_FREE' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PEN1L' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_MOD1_IND' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PDIS1H' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PDIS2L' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PDIS2H' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PDIS3L' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_PDIS3H' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_SEVOPS1' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_OSYNC_TCY' undeclared (first use in this function) <br>
<br>
PWM.c:66: error: 'PWM_UEN' undeclared (first use in this function) <br>
<br>
<br>
<br>
<a href="http://murali.8051.googlepages.com/123.jpg">Image externe (non intégrée)</a></div>
</article>

<article class="forum-post" id="p548">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-04 18:52 UTC">2008-10-04 18:52 UTC</time></header>
<h3>Re: Problem using PWM_motor</h3>
<div class="forum-post-body">Thanks for the bug report.<br>
<br>
<br>
<br>
I sucessfully reproduced it on the blockset version 0.98fe.<br>
<br>
<br>
<br>
Workaround : open at least once the PWM dialog blox and close it before compiling. It seems that some parameters are not updated until the block is opened at least once.<br>
<br>
<br>
<br>
Bug will be solved in the next release version.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p549">
<header><strong>murali</strong><time datetime="2008-10-04 19:09 UTC">2008-10-04 19:09 UTC</time></header>
<h3>Re: Problem using PWM_motor</h3>
<div class="forum-post-body">hi!<br>
<br>
 since i need it urgently, can you please send me the corrected blockset.</div>
</article>

<article class="forum-post" id="p550">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-04 19:35 UTC">2008-10-04 19:35 UTC</time></header>
<h3>Re: Problem using PWM_motor</h3>
<div class="forum-post-body">Hi Murali,<br>
<br>
<br>
<br>
Note that with the current version, you will be able to compile your model. You just need to open the PWM block once before compiling!!<br>
<br>
<br>
<br>
Anyway, I can provide you with the version being developed. <br>
<br>
Which matlab version are you using?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p551">
<header><strong>murali</strong><time datetime="2008-10-04 19:44 UTC">2008-10-04 19:44 UTC</time></header>
<h3>Re: Problem using PWM_motor</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
  I tried that,infact i have changed the period also before compiling ,but the same errors are appearing ..<br>
<br>
I am using r2008a..It would be great if you can provide me the corrected version.<br>
<br>
Thank you</div>
</article>

<article class="forum-post" id="p585">
<header><strong>gladiac</strong><time datetime="2008-10-23 10:54 UTC">2008-10-23 10:54 UTC</time></header>
<h3>Re: Problem using PWM_motor - Solved</h3>
<div class="forum-post-body">Hi Lubin<br>
<br>
<br>
<br>
It seems I have a similar problem.Once  I add the PWM bolckset to simulink model, the 'master' block couldn't be opened. The pic attached shows the error info. Also same error appears during compiling.<br>
<br>
<br>
<br>
cheers</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/128-New%20Picture.jpg">Pièce jointe : New Picture.jpg</a></p>
</article>

<article class="forum-post" id="p588">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-23 23:11 UTC">2008-10-23 23:11 UTC</time></header>
<h3>Re: Problem using PWM_motor - Solved</h3>
<div class="forum-post-body">Correction will be available in the next version of the blockset. It will be released within few days (3 to 10 days from now)</div>
</article>

<article class="forum-post" id="p597">
<header><strong>gladiac</strong><time datetime="2008-10-30 12:22 UTC">2008-10-30 12:22 UTC</time></header>
<h3>Re: Problem using PWM_motor - Solved</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I have upgraded to V0.99a for R2007b and R2006a, but the problem still exist, the picture shows the error info for R2007b</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/135-New%20Picture.jpg">Pièce jointe : New Picture.jpg</a></p>
</article>

<article class="forum-post" id="p598">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-30 12:34 UTC">2008-10-30 12:34 UTC</time></header>
<h3>Re: Problem using PWM_motor - Solved</h3>
<div class="forum-post-body">Hi Gladiac,<br>
<br>
<br>
<br>
I check the dsPIC you are using 30f6014, it has no PWM motor peripheral ! I will try to update the error message to make it more clear.<br>
<br>
<br>
<br>
You can generate PWM signal using the Output Compare block. 30f6014 has 8 OC channels capable to generate a PWM signal.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p599">
<header><strong>gladiac</strong><time datetime="2008-10-30 22:42 UTC">2008-10-30 22:42 UTC</time></header>
<h3>Re: Problem using PWM_motor - Solved</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks! The problem seems to be caused by myself. I just muddled up your 'PWM blockset' with the PWM mode of OC module. So your 'PWM blockset' works for MCPWM module. Thanks again for your help.</div>
</article>

