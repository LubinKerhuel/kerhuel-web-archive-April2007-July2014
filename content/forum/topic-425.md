---
title: "Multiple blocks of ADC doesn't trigger error"
url: "/forum/topic/425/"
archiveKind: "topic"
---
# Multiple blocks of ADC doesn't trigger error

Forum : [bug reports](/forum/#forum-8)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1644">
<header><strong>bmairs</strong><time datetime="2011-07-24 19:45 UTC">2011-07-24 19:45 UTC</time></header>
<div class="forum-post-body">According to another post of yours you say the following:<br>
<blockquote>The error comes from the multiple use of blocks that should be used only once in a model :<br>
<br>
If you are to use more that one Input Capture port, use only One block IC and configure this block to get many IC ports.<br>
<br>
Same remark for the ADC block,PWM motor block, OC block and others. Only The Digital Write, Read can be present in multiple place in a model. Same for the Rx-Tx blocks and the Tx-for-Matlab-Labview...<br>
<br>
<br>
<br>
Find attach the model with some modifications that compile. I also added few remarks. It would be fine if we could have a look on the final version (when the controller works).</blockquote><br>
<br>
Can you both add this information to the help document for every block as well as make the blocks trigger an error at some point during compilation or model building that informs the user that there can only be one block of that type? I just tried to use two separate ADC blocks and had it not work even though it compiled fine. I had to search your forums for the above quote and only then did I learn that you couldn't have multiple blocks for the ADC as I haven't seen it mentioned anywhere else in the documentation for your blockset.</div>
</article>

