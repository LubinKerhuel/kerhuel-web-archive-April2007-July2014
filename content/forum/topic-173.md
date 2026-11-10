---
title: "Matlab 64 bits - Starter Kit for dsPIC"
url: "/forum/topic/173/"
archiveKind: "topic"
---
# Matlab 64 bits - Starter Kit for dsPIC

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p607">
<header><strong>Ckouna</strong><time datetime="2008-11-07 15:39 UTC">2008-11-07 15:39 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I'm a student in Troyes and I'd like to know if your toolbox works with the new Starter kit from Microchip.<br>
<br>
<br>
<br>
The Debugger is a PIC : 18F67J50 and the DSPic is a 33FJ256GP506. It's designed only for audio applications with a mic/line in jack, and a speaker out jack.<br>
<br>
<br>
<br>
I don't know many things about dsPIC but I have a project at the university with a teacher, to create a simple filtering application with this Starter Kit or the Explorer 16 board.<br>
<br>
<br>
<br>
I think you speak french, but I'll try keeping typing english as it might increase my knowledges of technical english.<br>
<br>
<br>
<br>
EDIT : Does the toolbox work with R2008a 64bits ? I can't even compile the example for the Explorer 16.</div>
</article>

<article class="forum-post" id="p613">
<header><strong>Ckouna</strong><time datetime="2008-11-20 15:41 UTC">2008-11-20 15:41 UTC</time></header>
<h3>Re: Starter Kit for dsPIC</h3>
<div class="forum-post-body">Heres the error I get when I try to compile the dsPIC_33f_Explorer16 example program :<br>
<br>
<br>
<br>
I clik on the incremental build after the yellow block.<br>
<br>
<br>
<br>
Error using ==&gt; tlc c at 133<br>
<br>
Error evaluating IntiFCn callback of Master block ... Error using dsPIC_PortSetting at 416<br>
<br>
Error in S-function dsPic ... S-Function 'dsPIC_MASTER' does not exist<br>
<br>
<br>
<br>
If anyone knows what's wrong with how I'm doing things ... Help would be great .</div>
</article>

<article class="forum-post" id="p615">
<header><strong>LubinKerhuel</strong><time datetime="2008-11-24 18:16 UTC">2008-11-24 18:16 UTC</time></header>
<h3>Re: Starter Kit for dsPIC</h3>
<div class="forum-post-body">Hi Ckouna,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ckouna</header>EDIT : Does the toolbox work with R2008a 64bits ? I can't even compile the example for the Explorer 16.</blockquote><br>
The blockset has not been tested on 64 bits matlab. It seems that matlab 64 bits cannot execute 32 bits mex files. <br>
<br>
<br>
<br>
Thus, install a 32 bits matalb on your 64bit Winows and it will work properly.<br>
<br>
<br>
<br>
How many are interrested by a 64 bits version of the blockset  ? Let me know !</div>
</article>

<article class="forum-post" id="p618">
<header><strong>Ckouna</strong><time datetime="2008-11-28 13:30 UTC">2008-11-28 13:30 UTC</time></header>
<h3>Re: Starter Kit for dsPIC</h3>
<div class="forum-post-body">Thanks for the quick answer, I'm not sure I have the choice to install it in 32 bit but I'll try that.</div>
</article>

