---
title: "&quot;link errors found&quot;"
url: "/forum/topic/484/"
archiveKind: "topic"
---
# &quot;link errors found&quot;

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1846">
<header><strong>epsilon84</strong><time datetime="2012-03-05 21:29 UTC">2012-03-05 21:29 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
Slashes in the path ,as you see, are different. I think thats why the compiler has the link error. How can i handle this problem. <br>
<br>
<br>
<br>
c:\program files\microchip\mplab c30\bin\bin\..\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../analog_read.cof'<br>
<br>
<br>
<br>
==Emre==</div>
</article>

<article class="forum-post" id="p1885">
<header><strong>LubinKerhuel</strong><time datetime="2012-04-27 00:37 UTC">2012-04-27 00:37 UTC</time></header>
<h3>Re: &amp;quot;link errors found&amp;quot;</h3>
<div class="forum-post-body">Hi Emre,<br>
<br>
<br>
<br>
Usually, / and \ would not be a problem for the Microchip C30 compiler.<br>
<br>
Is si notmal you compiler path has two bin folders ? <br>
<br>
c:\program files\microchip\mplab c30\bin\bin/pic30-coff-ld.exe<br>
<br>
<br>
<br>
That might cause the link error ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1887">
<header><strong>epsilon84</strong><time datetime="2012-05-03 17:17 UTC">2012-05-03 17:17 UTC</time></header>
<h3>Re: &amp;quot;link errors found&amp;quot;</h3>
<div class="forum-post-body">Hello Mr. Lubin,<br>
<br>
<br>
<br>
You are right. I copy the files in the second bin folder to first bin folder. Now it works fine. Thanks a lot. <br>
<br>
<br>
<br>
==Emre==</div>
</article>

