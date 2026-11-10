---
title: "C Call function - Vector Input"
url: "/forum/topic/478/"
archiveKind: "topic"
---
# C Call function - Vector Input

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1824">
<header><strong>philippe.1</strong><time datetime="2012-02-06 18:10 UTC">2012-02-06 18:10 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am trying to write a data vector on a SD card by calling a C function.<br>
<br>
I have been writing this but it's not dealing with the array:<br>
<br>
<br>
<br>
unsigned char sd_write(unsigned int Input){<br>
<br>
char y1;<br>
<br>
y1 = FSfprintf(datafile, "%u%c%c",Input, 0x0D, 0x0A);<br>
<br>
}<br>
<br>
<br>
<br>
Could you tell me the right syntax to deal with the array please?<br>
<br>
Thanks<br>
<br>
Philippe</div>
</article>

