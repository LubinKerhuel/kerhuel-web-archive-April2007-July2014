---
title: "Link Error: Could not allocate data memory"
url: "/forum/topic/349/"
archiveKind: "topic"
---
# Link Error: Could not allocate data memory

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1438">
<header><strong>coolj</strong><time datetime="2011-01-12 00:02 UTC">2011-01-12 00:02 UTC</time></header>
<div class="forum-post-body"><span style="color:#0000bf">xxxxxx.o: Link Error: Could not allocate section .nbss, size = 64 bytes, attributes = bss near <br>
<br>
 Link Error: Could not allocate data memory</span><br>
<br>
Link step failed.<br>
<br>
<br>
<br>
If you're trying to compile source files in MPLAB (for debugging purposes) that compile fine in Matlab, but run into the error above, try enabling "Large data model" under Build Options -&gt; Project -&gt; MPLAB C30 -&gt; Memory Model<br>
<br>
<br>
<br>
Hope that helps!<br>
<br>
<br>
<br>
Justin<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/368-large_data_model.gif">Pièce jointe : large_data_model.gif</a></p>
</article>

