---
title: "explorer16 demo still working?"
url: "/forum/topic/352/"
archiveKind: "topic"
---
# explorer16 demo still working?

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1446">
<header><strong>coolj</strong><time datetime="2011-01-21 05:18 UTC">2011-01-21 05:18 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I was having some troubles with my own model, so I decided to revert back to the dsPIC_33f_Explorer16.mdl that you provide to make sure everything on my explorer 16 board was still working well.<br>
<br>
<br>
<br>
The model compiled fine, but I got strange output when adjusting the potentiometer - it seems like the two filtered values are not being converted to the right type or something.  <br>
<br>
<br>
<br>
I reverted back to 3.4 of the blockset (instead of 3.4b), but the same thing happened.  I'm pretty sure it was okay on v3.3, but I don't have that version so I can't verify.<br>
<br>
<br>
<br>
Are you seeing this on your side?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Justin<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/375-explorer_16_issue.gif">Pièce jointe : explorer_16_issue.gif</a></p>
</article>

<article class="forum-post" id="p1447">
<header><strong>coolj</strong><time datetime="2011-01-21 05:25 UTC">2011-01-21 05:25 UTC</time></header>
<h3>Re: explorer16 demo still working?</h3>
<div class="forum-post-body">Confirmed:  the two filter outputs need to be set to uint16...then everything works!<br>
<br>
<br>
<br>
-Justin</div>
</article>

<article class="forum-post" id="p1463">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-15 21:55 UTC">2011-02-15 21:55 UTC</time></header>
<h3>Re: explorer16 demo still working?</h3>
<div class="forum-post-body">Thanks for the problem report.<br>
<br>
<br>
<br>
I corrected the example and next blockset version will be Ok (thus, above 3.4b).<br>
<br>
Don't know what's happend as I did not modify anything also !<br>
<br>
<br>
<br>
Nice curve  :) <br>
<br>
Lubin</div>
</article>

