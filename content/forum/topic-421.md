---
title: "Importing a MATLAB code from the workspace?"
url: "/forum/topic/421/"
archiveKind: "topic"
---
# Importing a MATLAB code from the workspace?

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1631">
<header><strong>flash87</strong><time datetime="2011-06-28 11:12 UTC">2011-06-28 11:12 UTC</time></header>
<div class="forum-post-body">Hi Kerhuel,<br>
<br>
Can u please me tell me how can I import a code that i have written in MATLAB  from the workspace to your dsPIC blockset, so that when compiled it generates a hex file which can be further imported to the dsPIC.Please provide me some inputs on this as my project deadline is fastly approaching.<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p1632">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-28 18:14 UTC">2011-06-28 18:14 UTC</time></header>
<h3>Re: Importing a MATLAB code from the workspace?</h3>
<div class="forum-post-body">Simulink has a block that allows to embed matlab code.<br>
<br>
Note however that embeded code might react differently from your matlab function on high level function like svd or eig. The order of the eigen value return does not follows the same rules when comparing  between code execution in embedded matlab block and standard matlab script.<br>
<br>
Note also that generated code is not that efficient (However, it seems that this has progressed in the Matlab latest version : 2011a). You will also loose possibility to fine tune your algorithm with fixed point.<br>
<br>
<br>
<br>
This beeing said, I would not recommend to just copy-past a matlab script within simulink so as to get embedded code. Developing algorithm directly within simulink should provide much better results.<br>
<br>
The embedded matlab code should only be used for very simple operation that might be difficult to describe using simulink.<br>
<br>
<br>
<br>
Lubin</div>
</article>

