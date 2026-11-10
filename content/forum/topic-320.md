---
title: "bad installation"
url: "/forum/topic/320/"
archiveKind: "topic"
---
# bad installation

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1286">
<header><strong>jirobai</strong><time datetime="2010-08-13 19:54 UTC">2010-08-13 19:54 UTC</time></header>
<div class="forum-post-body">Hi<br>
<br>
i have installed on my pc windows 7 and matlab 2010a.<br>
<br>
when i run install_dsPIC_R2010a, to install the dsPIC blocksets the installation is OK but the procedure don't ask me where install it.<br>
<br>
and when i close matlab and i restart it i must reinstall the package.<br>
<br>
I'm very tired to do it. i don't know what i do to solve this problem.<br>
<br>
<br>
<br>
Thank in advance.<br>
<br>
jirobai</div>
</article>

<article class="forum-post" id="p1287">
<header><strong>LubinKerhuel</strong><time datetime="2010-08-15 08:33 UTC">2010-08-15 08:33 UTC</time></header>
<h3>Re: bad installation</h3>
<div class="forum-post-body">Hey Jirobai,<br>
<br>
<br>
<br>
The blockset install itself at the place where you launch it.<br>
<br>
The installer then add 3 directory into the matlab path.<br>
<br>
<br>
<br>
Thus, Copy first the installer to the place you want to install the blockset.<br>
<br>
Then, launch it from there.<br>
<br>
<br>
<br>
Note that installing the blockset within the matlab (sub)-folder usually cause many problems.<br>
<br>
Thus prefere install it at some place like "program file" or into your matlab working directory.<br>
<br>
<br>
<br>
You could check that matlab get the 3 new directory into its path.<br>
<br>
Some matlab version, or configuration, may not save this new path provided the the user do not has the right to do so (I did not see this case yet however...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

