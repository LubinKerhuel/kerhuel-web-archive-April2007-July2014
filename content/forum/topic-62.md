---
title: "C function call"
url: "/forum/topic/62/"
archiveKind: "topic"
---
# C function call

Forum : [dsPIC Peripherals](/forum/#forum-9)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p120">
<header><strong>kevin1025</strong><time datetime="2007-10-08 02:43 UTC">2007-10-08 02:43 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
I have a problem about "C funtion call".I don't know how to add the .c file.Can you explain more?<br>
<br>
Thanks.</div>
</article>

<article class="forum-post" id="p122">
<header><strong>LubinKerhuel</strong><time datetime="2007-10-10 20:24 UTC">2007-10-10 20:24 UTC</time></header>
<div class="forum-post-body">My advice is to place the c file in the same directory as your mdl file.<br>
<br>
<br>
<br>
You must add the C file in <br>
<br>
Simulation &gt;&gt; Configuration Parameters &gt;&gt; Custom Code &gt;&gt; include directory &gt;&gt; type the directory of your mdl file.<br>
<br>
<br>
<br>
and<br>
<br>
<br>
<br>
Simulation &gt;&gt; Configuration Parameters &gt;&gt; Custom Code &gt;&gt; Sources files &gt;&gt; type the filename : something.c<br>
<br>
<br>
<br>
I will post an example soon.<br>
<br>
<br>
<br>
Note however that this block is not functionnal in the evaluation version of the toolbox.</div>
</article>

<article class="forum-post" id="p370">
<header><strong>jebobrow</strong><time datetime="2008-05-19 02:27 UTC">2008-05-19 02:27 UTC</time></header>
<h3>Re: C function call</h3>
<div class="forum-post-body">I can't make the c function call work.  Did you ever make further instructions or an example on this?<br>
<br>
<br>
<br>
I made the two changes you suggested in this thread: 1) added the source code name to the configuration parameters, and I put it in the same directory that my mdl file is 2) I tried to add the path to the include directories, but it did not seem to like what I put in there. It was "C:\Documents and Settings\Jim\My Documents\PicMicro\InvertedPendulum_3030" but matlab complained about that.  It did not complain as much when I removed that, but I get the error below<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
pic30-coff-cc1.exe: warning: Options have been disabled due to expired license <br>
<br>
test2.c:31: error: syntax error before '.' token <br>
<br>
gmake: *** [test2.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'test2' aborted due to an error.</div>
</article>

<article class="forum-post" id="p371">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-19 17:15 UTC">2008-05-19 17:15 UTC</time></header>
<h3>Re: C function call</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
Up to now, some bugs were reported about the C call function<br>
<br>
<br>
<br>
One bug appears when using C Function Call with one input and No output.<br>
<br>
Most of these bugs are now fixed and will be released very soon in the next version (0.98)<br>
<br>
Anyway, it may greatly help if you could upload on the forum a simple example (mdl + c files).<br>
<br>
<br>
<br>
If the c file is in your model directory, you do not need to add the path of the c file.<br>
<br>
Note anyway that any path you provide must be in the format "8.3" (old dos format with ~1 or ~x at the end of long directory name.<br>
<br>
The matlab instruction rtw_alt_pathname('C:\Program files\zzz\...') convert a long name to its 8.3 name.<br>
<br>
(but you should not need that)<br>
<br>
<br>
<br>
Few thread about C function Call and with some examples: <br>
<br>
<br>
<br>
<a href="/forum/topic/100/#p266">Implementing the C Function Call</a><br>
<br>
<a href="/forum/topic/122/">Passing a Vector to the C-Function Call block</a><br>
<br>
<a href="/forum/topic/107/">C Function Call error for output size != 1</a><br>
<br>
<a href="/forum/topic/101/">How much RAM area can a program use?</a><br>
<br>
<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p383">
<header><strong>jebobrow</strong><time datetime="2008-05-23 16:23 UTC">2008-05-23 16:23 UTC</time></header>
<h3>Re: C function call</h3>
<div class="forum-post-body">Your QEI example solved my problem.  I put my source code file name in the wrong box in the "custom code" configuration paramters.  I had originally placed it in "Include custom c code in generated" instead of "Include list of addional" where it worked fine.  Strange.</div>
</article>

