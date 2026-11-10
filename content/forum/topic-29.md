---
title: "probleme - Matlab Version"
url: "/forum/topic/29/"
archiveKind: "topic"
---
# probleme - Matlab Version

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p46">
<header><strong>hamaoui</strong><time datetime="2007-04-28 17:50 UTC">2007-04-28 17:50 UTC</time></header>
<div class="forum-post-body">I have version 7.0.1 of Matlab. I installed your software but it does not work and when I built it, it answered me that :<br>
<br>
"Error while evaluating the 'SelectCallback' in system target <br>
<br>
file 'dspic.tlc'.  Last recorded error message:<br>
<br>
Property 'TargetLang' does not exist."<br>
<br>
<br>
<br>
can you give me a version compatible with my Matlab's version?<br>
<br>
<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p47">
<header><strong>LubinKerhuel</strong><time datetime="2007-04-28 20:10 UTC">2007-04-28 20:10 UTC</time></header>
<div class="forum-post-body">Hi hamaoui,<br>
<br>
<br>
<br>
There is some difference in the Real Time Workshop Embedded Coder Toolbox between Matlab 7.0.1 and Matlab 7.2 (R2006b).  That is why you get this error.<br>
<br>
<br>
<br>
It is quite a hard work to make the toolbox compatible with earlier matlab version. I am not planning to do it.<br>
<br>
<br>
<br>
You should upgrade your matlab to an earlier release. (R2006a, R2006b and R2007a are currently fully supported) <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p250">
<header><strong>Anonyme</strong><time datetime="2008-02-28 13:30 UTC">2008-02-28 13:30 UTC</time></header>
<h3>Re: probleme - Matlab Version</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
why is there no "interface Tx Matlab" block in the dsPIC toolbox for matlab 2007b? Or can i just take the one from 2007a?<br>
<br>
<br>
<br>
<br>
<br>
thanks<br>
<br>
don</div>
</article>

<article class="forum-post" id="p252">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-28 20:22 UTC">2008-02-28 20:22 UTC</time></header>
<h3>Re: probleme - Matlab Version</h3>
<div class="forum-post-body">The block "Interface Tx-Matlab" is available in all the version of the toolbox.<br>
<br>
Anyway, you could also start the user interface of this block by typing "rs232gui" at the matlab prompt.</div>
</article>

