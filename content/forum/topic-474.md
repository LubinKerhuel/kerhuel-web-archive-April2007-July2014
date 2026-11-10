---
title: "Interface Tx-Matlab rs232gui block fails in 2011b"
url: "/forum/topic/474/"
archiveKind: "topic"
---
# Interface Tx-Matlab rs232gui block fails in 2011b

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1814">
<header><strong>bmairs</strong><time datetime="2012-01-22 22:37 UTC">2012-01-22 22:37 UTC</time></header>
<div class="forum-post-body">I can't open the Interface Tx-Matlab block in 2011b. The following error occurs:<br>
<blockquote>Error due to multiple causes.<br>
<br>
--&gt; Error evaluating 'OpenFcn' callback of S-Function block (mask) 'power_test/dbl-click to open Graphical interface'.<br>
<br>
--&gt; Cannot find an exact (case-sensitive) match for 'rs232GUI'.<br>
<br>
Do you want: rs232gui <br>
<br>
(in C:\Users\Bryant\Documents\MATLAB\PIC_blockset_m2011b\blocks\rs232gui.p)?</blockquote></div>
</article>

<article class="forum-post" id="p1815">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-22 23:49 UTC">2012-01-22 23:49 UTC</time></header>
<h3>Re: Interface Tx-Matlab rs232gui block fails in 2011b</h3>
<div class="forum-post-body">Thanks Bryant,<br>
<br>
<br>
<br>
I am used to open the GUI interface typing rs232gui at the matlab prompt.<br>
<br>
<br>
<br>
I will correct the block that just call this function when you open it.<br>
<br>
the workaround is to type directly at matlab prompt &gt;&gt; rs232gui.<br>
<br>
<br>
<br>
As you see, matlab 2011 is now case sensitive for function call.<br>
<br>
<br>
<br>
Lubin</div>
</article>

