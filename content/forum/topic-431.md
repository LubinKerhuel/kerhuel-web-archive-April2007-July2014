---
title: "install_ds_PICR20XX.m effor"
url: "/forum/topic/431/"
archiveKind: "topic"
---
# install_ds_PICR20XX.m effor

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1650">
<header><strong>clay.mcvay</strong><time datetime="2011-08-12 21:12 UTC">2011-08-12 21:12 UTC</time></header>
<div class="forum-post-body">Lubin,<br>
<br>
<br>
<br>
Hi, my name is Clay McVay.  I'm teaching the same course that John Rogers taught last semester.  We upgraded MATLAB over the summer to 2011a and I'm unable to get the blockset to work.  When I run install_ds_PICR2011a.m or the paid version titled install_dsPIC_R2010b.m I get the following error message in my Command Window:<br>
<br>
<br>
<br>
-------------------------<br>
<br>
  INSTALLATION RTWdsPIC<br>
<br>
-------------------------<br>
<br>
  Reading the archiv <br>
<br>
  Checksum test passed (2A9BBB5164A79)<br>
<br>
  RTWdsPIC version none <br>
<br>
  RTWdsPIC time stamp 25-Jul-2011 22:26:12<br>
<br>
  Importing the archiv 100% |******************************|<br>
<br>
  Toolbox folder is C:\Program Files\MATLAB\R2011a\LKblockset<br>
<br>
addpath 'C:\Program Files\MATLAB\R2011a\LKblockset' <br>
<br>
  Make directory C:\Program Files\MATLAB\R2011a\LKblockset\blocks<br>
<br>
<span style="color:#ff0000">??? Error using ==&gt; fprintf<br>
<br>
Invalid file identifier.  Use fopen to generate a valid file identifier.<br>
<br>
<br>
<br>
Error in ==&gt; install_dsPIC_R2011a at 311<br>
<br>
      fprintf(fid,'%s\n','This script is under development and your assistance<br>
<br>
      is');</span> <br>
<br>
 <br>
<br>
Any thoughts?  One last question.  Will our paid 2010b blockset version work in MATLAB 2011a?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Clay</div>
</article>

<article class="forum-post" id="p1651">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-12 21:20 UTC">2011-08-12 21:20 UTC</time></header>
<h3>Re: install_ds_PICR20XX.m effor</h3>
<div class="forum-post-body">It seems there is a bug in the installer.<br>
<br>
I will have a look on it.<br>
<blockquote><header class="quote-author">Citation : clay.mcvay</header><br>
Any thoughts? One last question. Will our paid 2010b blockset version work in MATLAB 2011a?</blockquote>it should work.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1652">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-12 21:41 UTC">2011-08-12 21:41 UTC</time></header>
<h3>Re: install_ds_PICR20XX.m effor</h3>
<div class="forum-post-body">Hi Clay,<br>
<br>
<br>
<br>
I am not able to reproduce the problem using the website blockset version (with checksum 2A9BBB5164A79 tagged with 25-Jul-2011 22:26:12).<br>
<br>
<br>
<br>
Could you try to install the blockset in another place than within the matalb directory ?<br>
<br>
Do you have right restriction with your computer ?<br>
<br>
Which windows version are you using ? are you on 64 bits or 32 bits Matlab (and windows)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p3482">
<header><strong>louis314</strong><time datetime="2014-03-27 08:26 UTC">2014-03-27 08:26 UTC</time></header>
<h3>Re: install_ds_PICR20XX.m effor</h3>
<div class="forum-post-body">I had the same problem. Running MATLAB as administrator was a solution for me.</div>
</article>

