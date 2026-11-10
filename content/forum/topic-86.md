---
title: "Block ordering ?"
url: "/forum/topic/86/"
archiveKind: "topic"
---
# Block ordering ?

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p217">
<header><strong>johan.b</strong><time datetime="2008-02-15 07:55 UTC">2008-02-15 07:55 UTC</time></header>
<div class="forum-post-body">Hello everybody, <br>
<br>
<br>
<br>
I'm a new user of the dspic blockset and I have a little question concerning the "Block ordering". <br>
<br>
<br>
<br>
What is the role of this feature? I tried to read the online help but I did not concretely see how using this block. <br>
<br>
<br>
<br>
Did you already use this block in your applications ? Can you concretely explain me how it works ? <br>
<br>
<br>
<br>
Thank you in advance.<br>
<br>
<br>
<br>
Johan</div>
</article>

<article class="forum-post" id="p236">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-20 23:19 UTC">2008-02-20 23:19 UTC</time></header>
<h3>Re: Block ordering ?</h3>
<div class="forum-post-body">Hi Johan,<br>
<br>
<br>
<br>
I could not get time to post an example. I try to make the explanation understandable...<br>
<br>
<br>
<br>
If you want to force the execution order of blocks that are not connected, this option allows to add either an input, an output, or both to the block. These virtual connections allow to force the ordering of the blocks.<br>
<br>
<br>
<br>
Note that this method is only available for the block of this blockset. Simulink blockset do not have It. <br>
<br>
However, Simulink allows defining a priority for each blocks, thus giving you another possibility to change the block execution order. This method is not visual and quite hard to use on huge model.</div>
</article>

