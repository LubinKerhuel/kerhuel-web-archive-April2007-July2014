---
title: "blocksets do not appear in simulink"
url: "/forum/topic/135/"
archiveKind: "topic"
---
# blocksets do not appear in simulink

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p410">
<header><strong>salemimoh</strong><time datetime="2008-06-03 16:49 UTC">2008-06-03 16:49 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I have just baught a new laptop with windows XP installed. I installed MATLAB R2007B, as well as MPLAB 8.10 and microchip C30 students version. Then I tried to install the block sets into simulink by finding the directory which contains install _dsPIC_R2007b. I excuted it. Then the installation process took place. But when i checked the blocksets into simulink i did not find them. I tried the process many times but without success. Have you got any idea why?</div>
</article>

<article class="forum-post" id="p411">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-03 22:43 UTC">2008-06-03 22:43 UTC</time></header>
<h3>Re: blocksets do not appear in simulink</h3>
<div class="forum-post-body">Hi Salemimoh,<br>
<br>
<br>
<br>
few elements that may help : <br>
<br>
<br>
<br>
- Do not install the blockset in a subdirectory of matlab<br>
<br>
- Check that the blockset has been added to the path of matlab (File ==&gt; Set Path ...)<br>
<br>
   The <strong>root </strong>of the blockset and its two subdirectory <strong>blocks </strong>and <strong>dspic </strong>must be in the path. (automatically done by the installer)<br>
<br>
- play with options path cache option ; restart matlab ... (File ==&gt; Preference ==&gt; General ==&gt; path cache enable/disable etc...)</div>
</article>

<article class="forum-post" id="p1842">
<header><strong>epsilon84</strong><time datetime="2012-03-04 22:48 UTC">2012-03-04 22:48 UTC</time></header>
<h3>Re: blocksets do not appear in simulink</h3>
<div class="forum-post-body">Dear Lubin<br>
<br>
It worked thank you <br>
<br>
<br>
<br>
Emre</div>
</article>

<article class="forum-post" id="p1915">
<header><strong>realbw</strong><time datetime="2012-09-09 13:21 UTC">2012-09-09 13:21 UTC</time></header>
<h3>Re: blocksets do not appear in simulink</h3>
<div class="forum-post-body">thanks to your good work!</div>
</article>

