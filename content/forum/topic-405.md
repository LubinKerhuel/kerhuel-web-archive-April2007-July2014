---
title: "S-function and define microcontroleur"
url: "/forum/topic/405/"
archiveKind: "topic"
---
# S-function and define microcontroleur

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1586">
<header><strong>yannick</strong><time datetime="2011-05-26 15:33 UTC">2011-05-26 15:33 UTC</time></header>
<div class="forum-post-body">Hi, <br>
<br>
<br>
<br>
I try to use a S-function which call a header file (.h) thanks to an #include &lt;toto.h&gt;<br>
<br>
<br>
<br>
<br>
<br>
At the beginning of my header toto, there is a condition : If dsPIC XXXXX is defined do ..... just like that :<br>
<br>
<br>
<br>
#if defined(__dsPIC30F__)<br>
<br>
#include &lt;p30fxxxx.h&gt; ....<br>
<br>
<br>
<br>
But when I try to compile, Matlab doesn't get the device I chose in the master block, so of course, my dsPIC is not defined and my program cannot compile.<br>
<br>
<br>
<br>
I would like to know how I could get the data in order to define correctly my dsPIC in my header.<br>
<br>
<br>
<br>
I hope everybody understood what I am trying to explain..<br>
<br>
<br>
<br>
Thank you for your help !<br>
<br>
<br>
<br>
Yannick</div>
</article>

