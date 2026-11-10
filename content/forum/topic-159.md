---
title: "Fuzzy Logic.."
url: "/forum/topic/159/"
archiveKind: "topic"
---
# Fuzzy Logic..

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p523">
<header><strong>NigmaTech</strong><time datetime="2008-09-21 23:12 UTC">2008-09-21 23:12 UTC</time></header>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
Is that possible to use Fuzzy Logic Toolbox and your blockset together in dsPIC?</div>
</article>

<article class="forum-post" id="p526">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-22 22:14 UTC">2008-09-22 22:14 UTC</time></header>
<h3>Re: Fuzzy Logic..</h3>
<div class="forum-post-body">i NigmaTech,<br>
<br>
<br>
<br>
All blockset compatible with the Real Time Workshop (RTW) Embedded Coder can be used in model for dsPIC.<br>
<br>
Fuzzy Logic Blockset is compatible with the Real Time Workshop (RTW) Embedded Coder thus it will work on dsPIC. (see <a href="http://www.mathworks.com/products/fuzzylogic/description2.html">http://www.mathworks.com/products/fuzzy ... tion2.html</a>)<br>
<br>
<br>
<br>
I did not used it yet. But the fuzzy logic blockset seems to use time consuming function (exponential in sigmoid function and so...)<br>
<br>
Calculation are also done in floating point which is also time consumming.<br>
<br>
Therefore, it will works find, but the calculations may be slow, it now depends on your needs...<br>
<br>
<br>
<br>
<br>
<br>
If you are to use dsPIC efficiently, you may considere to convert the fuzzy logic blocks you will used into fixed point equivalent (use "look under mask" of the block). ... (you could for example use look up table instead of using the exponential floating point function and so on...)<br>
<br>
<br>
<br>
Lubin</div>
</article>

