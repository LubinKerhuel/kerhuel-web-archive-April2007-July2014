---
title: "undefined reference to `sbrk'"
url: "/forum/topic/150/"
archiveKind: "topic"
---
# undefined reference to `sbrk'

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p476">
<header><strong>malife</strong><time datetime="2008-08-21 21:21 UTC">2008-08-21 21:21 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I've spent much of the day today trying to debug this error with no luck:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;C:\PROGRA~1\MICROC~1\MPLABC~1\lib\libc-coff.a(xgetmem.o)(.libc+0x4):/home/guymc/build/3.10/build_20080424/src/standardc/sxl/xgetmem.c: undefined reference to `sbrk' 
C:\Program Files\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../GPSRead.coff' 
gmake: *** [..\../GPSRead.coff] Error 0xff 
### Real-Time Workshop build procedure for model: 'GPSRead' aborted due to an error.
</code></pre><br>
<br>
The strange thing is that it happens once the memory usage map has been printed, that is almost at the end.<br>
<br>
<br>
<br>
Any idea what the problem might be?<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p477">
<header><strong>malife</strong><time datetime="2008-08-22 16:32 UTC">2008-08-22 16:32 UTC</time></header>
<h3>Re: undefined reference to `sbrk&#x27;</h3>
<div class="forum-post-body">I finally solved this issue. It turns out that malloc and memcpy use sbrk which for some reason it is not compiled into the coff. Anyways, I found in the periphereal library documentation that microchip provides the source for sbrk with the standard C30 instalation, so I just added the source to the Simulink project and then it compiled fine. <br>
<br>
<br>
<br>
Hope this helps anyone with similar problems</div>
</article>

