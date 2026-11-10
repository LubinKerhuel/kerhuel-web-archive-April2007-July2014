---
title: "PLL does not seem to work correctly (bug report)"
url: "/forum/topic/54/"
archiveKind: "topic"
---
# PLL does not seem to work correctly (bug report)

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p95">
<header><strong>mlove</strong><time datetime="2007-08-08 14:36 UTC">2007-08-08 14:36 UTC</time></header>
<div class="forum-post-body">When using the Explorer demo with a crystal frequency between 8 and 16 MHz only the base clock functions correctly. When the PLL is ticked a divide by zero error occurs on the matlab command line. The mask shows zero for instructions, and prescaler says NaN. I was trying to get 40MIPS with the 8 MHz crystal which is within the allowable range of "FIN must be chosen to be in the range of 1.6 MHz to 16 MHz" (from data sheet). Could you have a look at this? Maybe I'm using the mask incorrectly?<br>
<br>
<br>
<br>
By the way, Keep up the good work. I have been using rtw and embedded coder for years and this target is very well done   :) <br>
<br>
<br>
<br>
Im using the MC variation of the 33 series any plans to add these devices/ drivers?</div>
</article>

<article class="forum-post" id="p97">
<header><strong>LubinKerhuel</strong><time datetime="2007-08-08 22:40 UTC">2007-08-08 22:40 UTC</time></header>
<div class="forum-post-body">Thanks for the report.<br>
<br>
<br>
<br>
PLL calculation is not yet described properly on the website. But the dialog should be user friendly. Here is a piece of information: <br>
<br>
<br>
<br>
PLL parameters are computed automatically by the blockset. You have to provide only the quartz used and the desired MIPS to reach. The blockset will provide you with the closest solution possible respecting the many constraints of the PLL circuit. <br>
<br>
<br>
<br>
On the version 0.94c, a bug makes the calculation unworkable as it is describe in the post above.<br>
<br>
<br>
<br>
The problem is now resolved on the version 0.94d.<br>
<br>
<br>
<br>
I couldn't test it completely; fell free to report what's going on...<br>
<br>
<br>
<br>
------------<br>
<br>
<br>
<br>
About the MC family, They will be supported in the next toolbox version. See the <a href="/RTWdsPIC/ReleaseNotes.html">Release note</a> page<br>
<br>
<br>
<br>
Lubin</div>
</article>

