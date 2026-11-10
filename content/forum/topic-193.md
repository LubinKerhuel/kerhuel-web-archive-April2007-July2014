---
title: "Block Orderring fails for Blocks with infinite sample time"
url: "/forum/topic/193/"
archiveKind: "topic"
---
# Block Orderring fails for Blocks with infinite sample time

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p703">
<header><strong>malife</strong><time datetime="2009-01-21 20:06 UTC">2009-01-21 20:06 UTC</time></header>
<div class="forum-post-body">Hello  Lubin<br>
<br>
 I have several "init"  C- function blocks that I need to execute at a specified order upon booting the dsPIC, if I use the Block ordering option only the last block in the sequence order gets included.  Right now I guess I can work around this by doing just one C-block that calls all in the specified order, so this is not a show stopper, just something for you to consider for the next version.<br>
<br>
<br>
<br>
Here are a couple of screenshots of the model and the  generated code:<br>
<br>
<br>
<br>
Thanks! <br>
<br>
<br>
<br>
Mariano</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/182-Model-1.png">Pièce jointe : Model-1.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/183-Code.png">Pièce jointe : Code.png</a></p>
</article>

<article class="forum-post" id="p704">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-22 01:18 UTC">2009-01-22 01:18 UTC</time></header>
<h3>Re: Block Orderring fails for Blocks with infinite sample time</h3>
<div class="forum-post-body">Hello Mariano,<br>
<br>
<br>
<br>
Thanks for your clear explanation. You find an interesting problem I would never find such a bug by myself ;-)<br>
<br>
<br>
<br>
My explanation is the following: <br>
<br>
<br>
<br>
You checked the Inline parameters (Simulation==&gt;Configuration Parameters==&gt;Optimization) to reduced the RAM memory of the dsPIC.<br>
<br>
<br>
<br>
When a block with infinite sample time (thus, for initialization here) has an input, Simulink try to optimize the code (Inlines parameters). Thus, it computes the scalar (or vector) result for this entry at time 0 because that block will be executed only once at time 0, and directly inject the result to last block with infinite sample time… This is why the blocks attached to a block with infinite time are not executed and thus implemented in the C code!<br>
<br>
<br>
<br>
Therefore, The method I usually use to force the block ordering will cause trouble in such a case. I am not sure there is a solution to make it works differently.<br>
<br>
<br>
<br>
<strong>However</strong>, there is another way to constrain the ordering of the blocks: using the <strong>simulink built in mechanism</strong>. <br>
<br>
Each block has <strong>Priority parameters</strong> (right click on the block ==&gt; Block Properties. <strong>The lower</strong> the priority value, <strong>the sooner</strong> the block executes. If blocks are not inside a loop, this will work 100%. Otherwise, be aware that this added constraint may not be satisfied by simulink…<br>
<br>
 <br>
<br>
<strong>You can see the execution ordering on the model</strong>: Format==&gt;Block Displays ==&gt; Sorted Order<br>
<br>
The number value at the <strong>top-right corner</strong> is the ordering of the blocks. <br>
<br>
I hope the explanation is correct ! I do not have full knowlege about simulink omtimization process yet...<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/184-Simulink_BlockProperty_Priority.png">Pièce jointe : Simulink_BlockProperty_Priority.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/185-SimulinkModel_CFunctionCall_Ordering.png">Pièce jointe : SimulinkModel_CFunctionCall_Ordering.png</a></p>
</article>

<article class="forum-post" id="p705">
<header><strong>malife</strong><time datetime="2009-01-22 01:58 UTC">2009-01-22 01:58 UTC</time></header>
<h3>Re: Block Orderring fails for Blocks with infinite sample time</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 Thanks for such a quick response. This solution works like a charm.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

