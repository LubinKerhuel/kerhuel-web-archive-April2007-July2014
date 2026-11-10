---
title: "Slow Compilation Time"
url: "/forum/topic/92/"
archiveKind: "topic"
---
# Slow Compilation Time

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p241">
<header><strong>Masaki</strong><time datetime="2008-02-24 08:48 UTC">2008-02-24 08:48 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
After I get RTW embedded coder, the toolkit starts to work.<br>
<br>
As its name shows, the prototyping speeds gets really fast!!<br>
<br>
<br>
<br>
On the other hand, the compilation speed seems to be so slow.<br>
<br>
It takes about 70 seconds with your exercise program "Sinus PWM".<br>
<br>
What is more intersting is that the incremental comiplation time is the same<br>
<br>
to both cases: after the model is chaned and no changes is made.<br>
<br>
<br>
<br>
Approximate time profiles are:<br>
<br>
 RTW   30 sec<br>
<br>
 "Number of I/O Pins" message (maybe, your program)  20 sec<br>
<br>
 Compiler  20 sec<br>
<br>
 Total  70 sec<br>
<br>
<br>
<br>
The PC I'm using is an old one with 800MHz Celleron on Windows 2000.<br>
<br>
Matlab version is R2007b.<br>
<br>
<br>
<br>
Would you give me some advice to make it faster?</div>
</article>

<article class="forum-post" id="p244">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-25 22:08 UTC">2008-02-25 22:08 UTC</time></header>
<h3>Re: RTW vs. RTW embedded coder</h3>
<div class="forum-post-body">I notice this inconvenient. As I am building more and more complex models, it takes more and more time to get compiled. However, I am usually using a faster computer and it is Ok (lets say 25 sec from the 'click' push button to get the .hex file).<br>
<br>
Compilation time also depend if you ask for an html report or not.<br>
<br>
<br>
<br>
When a block is being compiled, parameters of others blocks are also checked to get sure that the overall is coherent. This process could be speed up, but it's a hard and long task. I admit that it is not my priority right now! I hope that, despite the slow time compilation for huge model, the blockset accelerate your overall development...<br>
<br>
<br>
<br>
Anyway, I will keep you inform whenever I accelerate the compiling process.</div>
</article>

<article class="forum-post" id="p245">
<header><strong>Masaki</strong><time datetime="2008-02-26 00:39 UTC">2008-02-26 00:39 UTC</time></header>
<h3>Re: Slow Compilation Time</h3>
<div class="forum-post-body">Thanks for your reply. <br>
<br>
I understand this is partly RTW problems.<br>
<br>
I'll also try to upgrade my PC.<br>
<br>
<br>
<br>
Another trick you can make is just to speed up parameter tuning process.<br>
<br>
When a user changes a parameter on a model, i.e. a gain or constant, your program<br>
<br>
automatically detects the correspoinding memory location in hex file and changes it.<br>
<br>
<br>
<br>
Download process takes no time, so this will speed up our total development time.<br>
<br>
<br>
<br>
Masaki</div>
</article>

