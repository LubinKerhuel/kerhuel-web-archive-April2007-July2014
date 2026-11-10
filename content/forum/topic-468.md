---
title: "how to use custom c source code"
url: "/forum/topic/468/"
archiveKind: "topic"
---
# how to use custom c source code

Forum : [General Remark and Questions](/forum/#forum-1)

10 message(s) · archive en lecture seule

<article class="forum-post" id="p1775">
<header><strong>resodad</strong><time datetime="2012-01-05 20:59 UTC">2012-01-05 20:59 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
The help for the c function call block says:<br>
<br>
"The .c file containing the code of the function should be placed in the same directory as the .mdl file. If the c file is in another directory, it must be manually added in the "Simulation Parameters -&gt; Real time workshop -&gt; additional C file" <br>
<br>
Can you please clear this up for me?<br>
<br>
instead of  "Simulation Parameters -&gt; Real time workshop -&gt; additional C file" <br>
<br>
what would be the effect of putting the name of the c file in "Simulation Target &gt; Custom Code &gt; include custom c code in generated &gt; source file?"<br>
<br>
thanks,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1781">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 09:36 UTC">2012-01-12 09:36 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
I couldn't find "Simulation Parameters -&gt; Real time workshop -&gt; additional C file"  on matlab 2011b.<br>
<br>
The help file seems not up to date (or I write something wrong, anyway, I think this comes from an older matlab version...)<br>
<br>
<br>
<br>
The correct place to add the file is the one you provided. Please do not hesitates to update directly the wiki help page when you noticed this kind of remarks.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1789">
<header><strong>resodad</strong><time datetime="2012-01-12 13:39 UTC">2012-01-12 13:39 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
The attached screen image shows the configuration parameters and where I enter the names of the custom c files. Instead of "Simulation Target" they might also go under "Code Generation."  Please verify--do I have it right? Does it work just as well to put the file names under"Code Generation?"  Regards, John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/462-configScreen.jpg">Pièce jointe : configScreen.jpg</a></p>
</article>

<article class="forum-post" id="p1791">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 14:17 UTC">2012-01-12 14:17 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
That's not correct.<br>
<br>
File reference must be included into "Include list of additional". Otherwise, simulink will just add the name on the file within the generated code, that would create an error!<br>
<br>
<br>
<br>
Then, the files should be included into the Code Generation panel. Not the Simulation Target (did not notice this earlier)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1792">
<header><strong>resodad</strong><time datetime="2012-01-12 15:34 UTC">2012-01-12 15:34 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Like this?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/463-configScreen2.jpg">Pièce jointe : configScreen2.jpg</a></p>
</article>

<article class="forum-post" id="p1793">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 16:59 UTC">2012-01-12 16:59 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Correct.<br>
<br>
you might also add the folder where they are in the "include directory" box if the compiler did not find theses files.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1799">
<header><strong>salemimoh</strong><time datetime="2012-01-14 17:30 UTC">2012-01-14 17:30 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Lubin,<br>
<br>
I imagine this does not work with the demo version does it.</div>
</article>

<article class="forum-post" id="p1800">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-14 20:02 UTC">2012-01-14 20:02 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">It works with the demo version or at least it should work ;-)</div>
</article>

<article class="forum-post" id="p1804">
<header><strong>resodad</strong><time datetime="2012-01-16 14:48 UTC">2012-01-16 14:48 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">Lubin,<br>
<blockquote><header class="quote-author">Citation : LubinKerhuel</header>Correct.<br>
<br>
you might also add the folder where they are in the "include directory" box if the compiler did not find theses files.<br>
<br>
<br>
<br>
Lubin</blockquote><br>
Like this? I ask because this produces an error (see my other post about GenericTypeDefs.h)<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/471-configInclude.jpg">Pièce jointe : configInclude.jpg</a></p>
</article>

<article class="forum-post" id="p1811">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-18 20:26 UTC">2012-01-18 20:26 UTC</time></header>
<h3>Re: how to use custom c source code</h3>
<div class="forum-post-body">See the <a href="/forum/topic/432/">other post</a></div>
</article>

