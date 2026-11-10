---
title: "Installation failure on matlab 6.5"
url: "/forum/topic/130/"
archiveKind: "topic"
---
# Installation failure on matlab 6.5

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p394">
<header><strong>Anonyme</strong><time datetime="2008-05-27 18:13 UTC">2008-05-27 18:13 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I've tryed to install the dsPIC toolboxe :<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;&gt;&gt; install_dsPIC_R2006a
-------------------------
  INSTALLATION RTWdsPIC
-------------------------
  Reading the archiv 
  Checksum test passed (12C36605504AC)
  RTWdsPIC version none 
  RTWdsPIC time stamp 21-May-2008 21:14:35
  Importing the archiv 100% |******************************|
  Toolbox folder is C:\MATLAB6p5\toolbox\MPLAB
  Make directory C:\MATLAB6p5\toolbox\MPLAB\blocks
  Make directory C:\MATLAB6p5\toolbox\MPLAB\dspic
  Make directory C:\MATLAB6p5\toolbox\MPLAB\examples
----------------------------
       ERROR OCCURED 
    during installation
----------------------------
Undefined function or variable 'savepath'.
No error in the installation I/O process.
   errorcode is 97.7
----------------------------</code></pre><br>
<br>
I used all versions of install_dsPIC_R200x.x, its's the same result. I use matlab 6.5.<br>
<br>
<br>
<br>
What could be the problem ?<br>
<br>
<br>
<br>
Thanks in advance</div>
</article>

<article class="forum-post" id="p395">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-27 19:56 UTC">2008-05-27 19:56 UTC</time></header>
<h3>Re: Installation failure on matlab 6.5</h3>
<div class="forum-post-body">Hi Pick,<br>
<br>
<br>
<br>
The blockset support matlab, starting from version 2006a, i.e. Matlab V7.2 (january 2006)<br>
<br>
It is not gonna to work on earlier matlab version.<br>
<br>
<br>
<br>
Lubin</div>
</article>

