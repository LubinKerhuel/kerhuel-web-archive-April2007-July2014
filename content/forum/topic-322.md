---
title: "C-function block can't inherit input vector dimensions"
url: "/forum/topic/322/"
archiveKind: "topic"
---
# C-function block can't inherit input vector dimensions

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1294">
<header><strong>bmairs</strong><time datetime="2010-09-13 23:03 UTC">2010-09-13 23:03 UTC</time></header>
<div class="forum-post-body">I'm trying to pass the output of the xPC blockset Pack block into the C-function call block. The Pack block doesn't allow inheriting of its output signal dimensions and the C-function call block seems to require its dimensions to be specified. I've tried using -1 as the input vector size, but then the generated code passes a single integer (seemingly randomly generated) to that function when it's called.<br>
<br>
<br>
<br>
I'd like to do this:<br>
<br>
<br>
<br>
Pack Block -&gt; C-Function call<br>
<br>
(pack block outputs unspecified signal whose dimensions are determined when compiled) (the C-function call uses the dimension size passes by the input vector)<br>
<br>
<br>
<br>
In my specific example I have a 28 element vector coming out of the Pack Block. When I pass that to the C-Function call which has -1 specified for the input dimension size the generated function call looks like this: "uart2EnqueueActuatorData(((uint8_T)37U));". It's not only passing it just one element when it should be 28, it seemingly made up some constant to actually pass the function. Very odd.</div>
</article>

