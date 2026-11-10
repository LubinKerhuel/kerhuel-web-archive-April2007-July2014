---
title: "64-Bit Compatibility"
url: "/forum/topic/271/"
archiveKind: "topic"
---
# 64-Bit Compatibility

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1062">
<header><strong>aboehler</strong><time datetime="2010-01-28 18:06 UTC">2010-01-28 18:06 UTC</time></header>
<div class="forum-post-body">Lubin,<br>
<br>
<br>
<br>
As promised here the post of my email from yesterday:<br>
<br>
<br>
<br>
<br>
<br>
"Dear Lubin,<br>
<br>
<br>
<br>
Thanks again for your recent support on your blockset!<br>
<br>
<br>
<br>
I have a different question concerning 64-bit systems. Do you have any experience if your blockset runs on 64-bit? I'm working on a 64-bit machine now. I have installed MATLAB, the C30 compiler v3.11b and the latest blockset version you sent us (0.99h). When I compile I get an error message from MATLAB saying<br>
<br>
<br>
<br>
"Error using ==&gt; set_param<br>
<br>
--&gt; Error in S-function 'dsPIC_33f_..../xyz':<br>
<br>
S-Function 'dsPIC_xyz' does not exist."<br>
<br>
<br>
<br>
I get similar errors for every dsPIC block in the Simulink model.<br>
<br>
<br>
<br>
I did some online searching and now believe that it is because the S-Function files were compiled in 32-bit (*.mexw32) but would need to be in 64-bit (*.mexw64). Does that make sense to you? Or do you know of anybody getting it to work on 64-bit? Is there a simple workaround, e.g. convert the *.mexw32 to *.mexw64?<br>
<br>
<br>
<br>
Thanks so much for your help!<br>
<br>
<br>
<br>
Alex"</div>
</article>

<article class="forum-post" id="p1084">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-11 17:22 UTC">2010-02-11 17:22 UTC</time></header>
<h3>Re: 64-Bit Compatibility</h3>
<div class="forum-post-body">Hi Alex,<br>
<br>
<br>
<br>
The blockset is not yet compatible with 64 bits matlab.<br>
<br>
The problem comes from the mexw32 files that only works on matlab 32 bits.<br>
<br>
<br>
<br>
I will try to switch soon on 64 bits system to adapt the blockset.<br>
<br>
<br>
<br>
The workaround for the moment is to install a matlab 32 bits on your 64 bits system. It works well.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1192">
<header><strong>Ender</strong><time datetime="2010-04-28 05:24 UTC">2010-04-28 05:24 UTC</time></header>
<h3>Re: 64-Bit Compatibility</h3>
<div class="forum-post-body">We'll try later the blockset in 64 bits OS, but right now, I'm using the licence on my older 32bit computer with Matlab2010a and Alex is busy.<br>
<br>
But thanks for all the updates done in 32, 64 bits and Matlab 2010a, all provide in the same week Lubin<br>
<br>
<br>
<br>
Thierry</div>
</article>

