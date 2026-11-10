---
title: "Compilation error. Please help."
url: "/forum/topic/223/"
archiveKind: "topic"
---
# Compilation error. Please help.

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p847">
<header><strong>gksinghal</strong><time datetime="2009-05-07 20:46 UTC">2009-05-07 20:46 UTC</time></header>
<div class="forum-post-body">Hello, <br>
<br>
<br>
<br>
I am using Matlab 2008b, C30 COMPILER, DSPic 30f2012. I have all required toolboxes installed. I run into error when I try to compile the simulink blocks. The simulink block has the dsPIC Master block, UART config block and Tx block. <br>
<br>
<br>
<br>
Thanks in advance<br>
<br>
<br>
<br>
Girish<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
### Loading TLC function libraries<br>
<br>
<br>
<br>
.....<br>
<br>
### Initial pass through model to cache user defined code<br>
<br>
### Caching model source code<br>
<br>
Error: File: C:\LOCAL\Motor Control\Simulink\Blocksets\blocks\dsPIC_MASTER.tlc Line: 106 Column: 62<br>
<br>
The specified index (2) was out of the range 0 - 1<br>
<br>
Error: File: C:\LOCAL\Motor Control\Simulink\Blocksets\blocks\dsPIC_MASTER.tlc Line: 106 Column: 62<br>
<br>
The specified index (3) was out of the range 0 - 1<br>
<br>
Error: File: C:\LOCAL\Motor Control\Simulink\Blocksets\blocks\dsPIC_MASTER.tlc Line: 106 Column: 62<br>
<br>
The specified index (4) was out of the range 0 - 1<br>
<br>
Error: File: C:\LOCAL\Motor Control\Simulink\Blocksets\blocks\dsPIC_MASTER.tlc Line: 106 Column: 62<br>
<br>
The specified index (5) was out of the range 0 - 1<br>
<br>
### Real-Time Workshop build procedure for model: 'project1' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found</div>
</article>

<article class="forum-post" id="p848">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-07 21:26 UTC">2009-05-07 21:26 UTC</time></header>
<h3>Re: Compilation error. Please help.</h3>
<div class="forum-post-body">Dear Girish,<br>
<br>
<br>
<br>
I will probably not be available for the next three day.<br>
<br>
Anyway, could you try to compile one of the example in the example repertory ?<br>
<br>
<br>
<br>
On your model, Check that you selected one microcontroller in the Master block configuration<br>
<br>
<br>
<br>
Then, if you still get in trouble, could you post your model on this forum ? I'll try to look at that.<br>
<br>
<br>
<br>
Lubin</div>
</article>

