---
title: "slow matlab"
url: "/forum/topic/329/"
archiveKind: "topic"
---
# slow matlab

Forum : [bug reports](/forum/#forum-8)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1304">
<header><strong>sztibi82</strong><time datetime="2010-10-06 16:10 UTC">2010-10-06 16:10 UTC</time></header>
<div class="forum-post-body">i try to evaluate the free version of 2008A.<br>
<br>
<br>
<br>
Since i installed the dspi/pic blockset, the Simulink goes very slow. For a simple operation like see what is in the contiunous blockset, it takes 5-10 minutes to open.</div>
</article>

<article class="forum-post" id="p1305">
<header><strong>LubinKerhuel</strong><time datetime="2010-10-07 11:07 UTC">2010-10-07 11:07 UTC</time></header>
<h3>Re: slow matlab</h3>
<div class="forum-post-body">Simulink takes some times to read the blockset; however, it should not take more than 10 sec.<br>
<br>
Could you describe your configuration ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1307">
<header><strong>sztibi82</strong><time datetime="2010-10-07 13:23 UTC">2010-10-07 13:23 UTC</time></header>
<h3>Re: slow matlab</h3>
<div class="forum-post-body">I have an <br>
<br>
AMD Athlon XP 2500+<br>
<br>
1.84 GHz, with 1G ram<br>
<br>
<br>
<br>
<br>
<br>
I am using Matlab 2008a on windows XP SP2.<br>
<br>
<br>
<br>
<br>
<br>
Matlab runs fine. I can even start simulink very fast.<br>
<br>
When i create a new simulink project, computer almost freezes, the processor gets 100% usage. <br>
<br>
If a simulink model and the simulink blockset browser are both open the computer freezes, works very slow.<br>
<br>
If i close one of windoes (simulink blockest browser or model)computer gets fast again.<br>
<br>
<br>
<br>
When matlab is so slow i try to close with end task i get the following message:"Cannot close the model 'untitled1' while processing a callback."<br>
<br>
<br>
<br>
If you have more questions, pls don't hesitate to write in the forum.</div>
</article>

<article class="forum-post" id="p1311">
<header><strong>LubinKerhuel</strong><time datetime="2010-10-11 21:22 UTC">2010-10-11 21:22 UTC</time></header>
<h3>Re: slow matlab</h3>
<div class="forum-post-body">Thanks for the description.<br>
<br>
<br>
<br>
This seems not normal, I do not have this behavior (2Ghz ram however, but should not change that much !).<br>
<br>
<br>
<br>
Do you have virtual serial port, like bluetooth or so on ?<br>
<br>
If you cancel (ctrl-c), can you get the script name that slow downs the computer ? (i.e. which is the script that loop infinitly or likely)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1312">
<header><strong>sztibi82</strong><time datetime="2010-10-14 10:14 UTC">2010-10-14 10:14 UTC</time></header>
<h3>Re: slow matlab</h3>
<div class="forum-post-body">I have something similar for the PIC32 kit. It runs on USB but i think it emulates a virtual serial port.<br>
<br>
<br>
<br>
Sadly i don't get any script when i press ctrl+c</div>
</article>

<article class="forum-post" id="p1370">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 22:33 UTC">2010-11-30 22:33 UTC</time></header>
<h3>Re: slow matlab</h3>
<div class="forum-post-body">Hey, did you solve the problem ?<br>
<br>
A new blockset version is available, could you let me know if you still get the problem with this new one ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

