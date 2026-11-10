---
title: "Using Output Compare"
url: "/forum/topic/312/"
archiveKind: "topic"
---
# Using Output Compare

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1263">
<header><strong>jmednick</strong><time datetime="2010-06-29 20:59 UTC">2010-06-29 20:59 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I just wanted to confirm that I'm using the OC Output Compare block correctly...<br>
<br>
<br>
<br>
First off, it seems like OC1max is a constant that is relevant to the chip.  Is there a way I inherit it from the chip, because just making a constant block called [OC1max] does not work.<br>
<br>
<br>
<br>
Additionally, if I wanted to set up a 50% wave at 2 KHz, then I would need Max / Channel to be set to 0.0005 and up would be (0.00025 / 0.0005 )* OC1max?<br>
<br>
<br>
<br>
What do I set Period to, as it needs an integer input?<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p1264">
<header><strong>LubinKerhuel</strong><time datetime="2010-06-30 07:44 UTC">2010-06-30 07:44 UTC</time></header>
<h3>Re: Using Output Compare</h3>
<div class="forum-post-body">Hello Jared<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jmednick</header>First off, it seems like OC1max is a constant that is relevant to the chip. Is there a way I inherit it from the chip, because just making a constant block called [OC1max] does not work.</blockquote><br>
OC1max is relevant to the internal chip frequency (typically depending on quartz and PLL used).<br>
<br>
the dsPIC blockset evaluate this variable in the MATLAB workspace. Type "who" at matlab prompt to list all variable. Get the variable value typing its name "OC1max" (case sensitive).<br>
<br>
There are two OC blocks :<br>
<br>
<a href="/wiki/dspic-block-output-compare-hw/">OC hardware</a> that create one variable <strong>OCmax</strong>.<br>
<br>
<a href="/wiki/dspic-block-output-compare/">OC</a> that create variables <strong>OC(x)max</strong> with x, corresponding to each channel (1, 2 3 or 4) <br>
<br>
==&gt; use the correct one.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : jmednick</header>Additionally, if I wanted to set up a 50% wave at 2 KHz, then I would need Max / Channel to be set to 0.0005 and up would be (0.00025 / 0.0005 )* OC1max?</blockquote><br>
That's correct. The OC(x)max value should be high enough (otherwise, you will not get a correct precision, workaround would be to increase the chip internal MIPS through quartz or PLL)<br>
<br>
As you must use an integer value, roundoff result : round((0.00025 / 0.0005 )* OC1max).<br>
<br>
Period must be set at OC1max (In your case, period is fixed at OC1max, thus, you can remove the Period input from the block).<br>
<br>
<br>
<br>
Please feel free to edit the wiki pages about OC blocks to make them better.<br>
<br>
<br>
<br>
Lubin</div>
</article>

