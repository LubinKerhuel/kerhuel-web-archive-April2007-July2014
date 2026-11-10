---
title: "Can't run examples"
url: "/forum/topic/563/"
archiveKind: "topic"
---
# Can't run examples

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1967">
<header><strong>fram_22</strong><time datetime="2012-12-11 01:31 UTC">2012-12-11 01:31 UTC</time></header>
<div class="forum-post-body">Hello:<br>
<br>
<br>
<br>
I have just download and installed the  dsPIC blockset. It was installed properly and it is not included on the matlab directory.<br>
<br>
I checked that the matlab folder is set to the dspic blocks folder.<br>
<br>
I am using matlab R2010a on windows 7 64bit.<br>
<br>
However when I try to compile the examples the following error appears:<br>
<br>
<br>
<br>
File I/O error on file 'dspic.tlc'<br>
<br>
Operation that caused an error: open<br>
<br>
<br>
<br>
I am kind of lost here. If someone could explain what does this means and how to workaround that error I would be most thankful.<br>
<br>
<br>
<br>
thank</div>
</article>

<article class="forum-post" id="p1974">
<header><strong>AbuSaleh</strong><time datetime="2012-12-30 12:10 UTC">2012-12-30 12:10 UTC</time></header>
<h3>Re: Can&#x27;t run examples</h3>
<div class="forum-post-body">I had the same problem and I finally solved it. The solution is to copy the blockset m-file to any place other than C: partition. I have copied it to partition E: and chancged the path of Matlab to this location and run the "install_dsPIC_R2012a.m" file inside matlab. Then open the examples folder and run any example and it will work.<br>
<br>
<br>
<br>
<br>
<br>
Ahmed</div>
</article>

<article class="forum-post" id="p1981">
<header><strong>fram_22</strong><time datetime="2013-02-06 17:57 UTC">2013-02-06 17:57 UTC</time></header>
<h3>Re: Can&#x27;t run examples</h3>
<div class="forum-post-body">Thanks for the reply.<br>
<br>
It has worked!<br>
<br>
<br>
<br>
Please forgive me for taking so long to answer. I was distracted by some issues at work.</div>
</article>

