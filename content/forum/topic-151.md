---
title: "Matlab Variables do not Propagate to C-Function Call Block"
url: "/forum/topic/151/"
archiveKind: "topic"
---
# Matlab Variables do not Propagate to C-Function Call Block

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p478">
<header><strong>malife</strong><time datetime="2008-08-22 16:38 UTC">2008-08-22 16:38 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I am currently working on 0.98d so maybe you already fixed that in the latest version (which I hope you'll send it to me when you get back from vacations :-) )<br>
<br>
<br>
<br>
 But the issue is the following. I have a matlab script that initializes different variables most of it related to sizes and locations of signals. For instance I have a MAX_POSSIBLE variable that determines the maximum amount of bytes I can receive between sample times in the interrupt driven UART. If I configure that value using the variable (instead of just the number) in the C-function call dialog, for instance, for the input size. It will not recognize it; furthermore if I try to compile it says that it can not convert "" to an integer. <br>
<br>
<br>
<br>
Hope this is a simple one to fix. Certainly it is not a show-stopper since I can just put the number manually, but it is convenient that if I change something (like baud rate) all the sizes get reconfigured by reading those variables.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p479">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-22 22:29 UTC">2008-08-22 22:29 UTC</time></header>
<h3>Re: Matlab Variables do not Propagate to C-Function Call Block</h3>
<div class="forum-post-body">Ok, Will have a look on that.<br>
<br>
Thanks for the bug report !<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p497">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-02 19:03 UTC">2008-09-02 19:03 UTC</time></header>
<h3>Re: Matlab Variables do not Propagate to C-Function Call Block</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
It seems to be quite complicated to modify the blockset.<br>
<br>
<br>
<br>
Anyway, there may be a way to do what you wants : <br>
<br>
replace : <strong>YoutVariable</strong> by <strong>['[' num2str(YourVariable) ']']</strong> in the dialog box.<br>
<br>
I should work for all blocks. <br>
<br>
<br>
<br>
Lubin</div>
</article>

