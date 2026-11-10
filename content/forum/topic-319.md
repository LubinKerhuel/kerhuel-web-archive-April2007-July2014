---
title: "PIC32 Bootloader memory offset"
url: "/forum/topic/319/"
archiveKind: "topic"
---
# PIC32 Bootloader memory offset

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1285">
<header><strong>mlove</strong><time datetime="2010-08-12 09:14 UTC">2010-08-12 09:14 UTC</time></header>
<div class="forum-post-body">Hi There,<br>
<br>
I was wanting to use the PIC32 Bootloader to upload code for en embedded application. Use of the bootloader requires that the start vector for the application sofware has a memory offset added to the code and uses a custom set of *.ld files and bootloader memory file. Is there a way to edit the blockset /dspic target in order to add this ofset into the build sequence? Also, how could the scripts be modified to pull in the other custom files required?<br>
<br>
<br>
<br>
Thanks<br>
<br>
Matthew Love</div>
</article>

<article class="forum-post" id="p1288">
<header><strong>mlove</strong><time datetime="2010-08-16 09:52 UTC">2010-08-16 09:52 UTC</time></header>
<h3>Re: PIC32 Bootloader memory offset</h3>
<div class="forum-post-body">Hi all, It was just a matter of changing the procdefs.ld file for the device being used and then the target generates the correct application code for use with the MC bootloader.<br>
<br>
<br>
<br>
Matthew</div>
</article>

