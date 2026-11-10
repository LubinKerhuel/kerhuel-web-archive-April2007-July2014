---
title: "C Function Call error for output size != 1"
url: "/forum/topic/107/"
archiveKind: "topic"
---
# C Function Call error for output size != 1

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p289">
<header><strong>Anonyme</strong><time datetime="2008-04-10 22:59 UTC">2008-04-10 22:59 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
Wen i specify an output size greater than 1, the C  Call function uses a pointer to an arrya of the output type. However, an extra , was left before. Model will not compile due to the syntax error.<br>
<br>
<br>
<br>
For example , I created a function callde GetQEI that returns 3 int32. In the declaation of the function prototype in  "model_NAME"_private.h as:<br>
<br>
<br>
<br>
 extern void GetQEI(,int32_T* y1);<br>
<br>
<br>
<br>
I hope you can fix the error and send the p code and the TLC files.<br>
<br>
<br>
<br>
A work around is to open de _private.h file and erase de ,. Then call de "model_NAME.bat" with the ! changing  the current directory in the sources directory, so it can be compiled.<br>
<br>
<br>
<br>
Saludos.<br>
<br>
A. Soria<br>
<br>
[adresse e-mail retirée]</div>
</article>

<article class="forum-post" id="p317">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-28 21:41 UTC">2008-04-28 21:41 UTC</time></header>
<h3>Re: C Function Call error for output size != 1</h3>
<div class="forum-post-body">Thanks for repporting that bug.<br>
<br>
<br>
<br>
It is now corrected and will be available in the next release (next to V0.97)<br>
<br>
<br>
<br>
Lubin</div>
</article>

