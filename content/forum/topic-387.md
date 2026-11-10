---
title: "CAN configuration bug"
url: "/forum/topic/387/"
archiveKind: "topic"
---
# CAN configuration bug

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1552">
<header><strong>Bernard Leak</strong><time datetime="2011-04-20 12:33 UTC">2011-04-20 12:33 UTC</time></header>
<div class="forum-post-body">See also my changes to<br>
<br>
<a href="/wiki/dspic-block-can-configuration/">http://www.kerhuel.eu/wiki/Block/CAN_Configuration</a><br>
<br>
These include suggestions for better prompts in the block's masked parameter<br>
<br>
dialogue.<br>
<br>
In particular, note<br>
<br>
    'Progagation' should be 'Propagation'<br>
<br>
    (and 'bits' should be 'quanta').<br>
<br>
<br>
<br>
    'Baud Rate' should be 'Baud Rate Prescaler - 1'<br>
<br>
    I was thoroughly confused by 'Baud Rate'!<br>
<br>
    Note the - 1!  N in this field is the value<br>
<br>
    written to the register, when the oscillator<br>
<br>
    rate is reduced by a scale factor of (N + 1).<br>
<br>
<br>
<br>
    If you don't mind breaking backward compatibility,<br>
<br>
    it would be best to let this parameter be like the<br>
<br>
    segment lengths, set to match the actual<br>
<br>
    ratio used rather than the register setting<br>
<br>
<br>
<br>
Now the important bit:<br>
<br>
The CAN frequency is wrong (on all<br>
<br>
CAN modules I know about, including<br>
<br>
the PIC30f6014a).  You've added<br>
<br>
together the propagation and phase buffer<br>
<br>
segment lengths and added 2: but you<br>
<br>
should only add 1.  Perhaps you counted<br>
<br>
the synchronisation quantum at both<br>
<br>
ends of the bit?  It is 'between<br>
<br>
bits' and should only be counted once<br>
<br>
for each bit in determining the baud<br>
<br>
rate.</div>
</article>

