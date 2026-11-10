---
title: "fuzzy logic controlller"
url: "/forum/topic/440/"
archiveKind: "topic"
---
# fuzzy logic controlller

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1699">
<header><strong>ricaldo2431</strong><time datetime="2011-09-14 22:24 UTC">2011-09-14 22:24 UTC</time></header>
<div class="forum-post-body">Dear Lubin:<br>
<br>
<br>
<br>
We are designing a fuzzy logic controller (Mandani) using matlab and simulink dspic tool and the idea is to implement it into a dsPIC33fj128mc802.<br>
<br>
<br>
<br>
At the compilation process we obtain an error message.<br>
<br>
<br>
<br>
Can you please help me to fix this problem please.<br>
<br>
<br>
<br>
I send you the files of my controller. Thank you.<br>
<br>
<br>
<br>
Sincerely,<br>
<br>
<br>
<br>
Ricardo</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/441-FUZZY.rar">Pièce jointe : FUZZY.rar</a></p>
</article>

<article class="forum-post" id="p1700">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-17 17:24 UTC">2011-09-17 17:24 UTC</time></header>
<h3>Re: fuzzy logic controlller</h3>
<div class="forum-post-body">Hi Ricardo,<br>
<br>
<br>
<br>
I could not open the fuzzy-logic block of yoru model as I do not have the Fuzzy-Logic Toolbox.<br>
<br>
Anyway, The model seems fine otherwise.<br>
<br>
<br>
<br>
Usually, theses fuzzy-logic blocks use a lot of memory as they implement huge look-up table for sigmoide function or similar.<br>
<br>
Could you copy-past the error you get ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1702">
<header><strong>ricaldo2431</strong><time datetime="2011-09-19 20:06 UTC">2011-09-19 20:06 UTC</time></header>
<h3>Re: fuzzy logic controlller</h3>
<div class="forum-post-body">Hi lubin,<br>
<br>
<br>
<br>
thank you for your response.<br>
<br>
<br>
<br>
In fact actually my project do not show any error, now it generate the dspic code, but when I try to program the system, it does not nothing.<br>
<br>
<br>
<br>
I check the memory usage and its ok, so is not a memory problem.<br>
<br>
<br>
<br>
I thank you your help.<br>
<br>
<br>
<br>
<br>
<br>
Ricardo</div>
</article>

<article class="forum-post" id="p1733">
<header><strong>carotti</strong><time datetime="2011-10-29 16:52 UTC">2011-10-29 16:52 UTC</time></header>
<h3>Re: fuzzy logic controlller</h3>
<div class="forum-post-body">Hi Ricardo,<br>
<br>
I was curious about your post so had a quick look.  I notice that you have 1ms sample time (relatively fast) but are only running the processor at 2.00 MIPS.  Perhaps the processor is unable to complete the task within the 1ms period.  Crank up the MIPS by a factor of 10 and you may see a result?<br>
<br>
Dave.</div>
</article>

