---
title: "'CompileAllModels' Error"
url: "/forum/topic/306/"
archiveKind: "topic"
---
# 'CompileAllModels' Error

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1247">
<header><strong>edlaurence</strong><time datetime="2010-06-06 19:37 UTC">2010-06-06 19:37 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I've just installed MPLAB C32 compiler and your latest (3.2b) blockset for Matlab 2009a.  It seems to install correctly although I have problems as soon as I run the suggested check using the 'CompileAllModels.m' script.  The output is as follows:<br>
<br>
<br>
<pre><code>&gt;&gt; CompileAllModels.m
Warning: File 'Data_Login_Matlab.hex' not found. 
&gt; In CompileAllModels at 11
Warning: The following error occurred processing the
System Target File '':
<wbr>
Undefined function or variable "myData".
<wbr>
&gt; In stf2target at 61
  In C:\dsPIC_Toolbox\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 42
  In CompileAllModels at 14
Warning: The following error occurred processing the
System Target File '':
<wbr>
Undefined function or variable "myData".
<wbr>
&gt; In C:\dsPIC_Toolbox\blocks\dsPIC_ConfigureModelFordsPICTarget.p&gt;dsPIC_ConfigureModelFordsPICTarget at 42
  In CompileAllModels at 14
??? Error using ==&gt; dsPIC_ConfigureModelFordsPICTarget
at 51
Error using ==&gt; dsPIC_ConfigRTWOption at 11
block_diagram does not have a parameter named
'GMAKE_PLACE'.
<wbr>
Error in ==&gt; CompileAllModels at 14
    dsPIC_ConfigureModelFordsPICTarget();</code></pre><br>
<br>
I get a similar problem when trying to open block such as 'Configure Model' and 'Master' with reference to the GMAKE_PLACE fault.<br>
<br>
<br>
<br>
It's probably a rookie mistake but I'd really appreciate your help as I think the blockset is going to be hugely useful!  :D <br>
<br>
<br>
<br>
Many thanks!<br>
<br>
<br>
<br>
Ed</div>
</article>

<article class="forum-post" id="p1249">
<header><strong>edlaurence</strong><time datetime="2010-06-07 10:59 UTC">2010-06-07 10:59 UTC</time></header>
<h3>Re: &#x27;CompileAllModels&#x27; Error</h3>
<div class="forum-post-body">Hi again,<br>
<br>
<br>
<br>
Looks like I've fixed the problem by installing C30 as well as C32.  It makes sense that this would cause issues when running the 'CompileAllModels' script but didn't expect GMAKE_PLACE errors when just trying to add blocks and configure for PIC32...?<br>
<br>
<br>
<br>
Cheers!<br>
<br>
<br>
<br>
Ed</div>
</article>

<article class="forum-post" id="p1250">
<header><strong>LubinKerhuel</strong><time datetime="2010-06-08 17:51 UTC">2010-06-08 17:51 UTC</time></header>
<h3>Re: &#x27;CompileAllModels&#x27; Error</h3>
<div class="forum-post-body">Anyway, thanks for reporting it !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1259">
<header><strong>alby.divy</strong><time datetime="2010-06-29 10:47 UTC">2010-06-29 10:47 UTC</time></header>
<h3>Re: &#x27;CompileAllModels&#x27; Error</h3>
<div class="forum-post-body">I've the same error! I don't understand how you have debugged it!<br>
<br>
Can you help me?<br>
<br>
Thanks!<br>
<br>
<br>
<br>
Alb</div>
</article>

<article class="forum-post" id="p1270">
<header><strong>edlaurence</strong><time datetime="2010-07-11 19:44 UTC">2010-07-11 19:44 UTC</time></header>
<h3>Re: &#x27;CompileAllModels&#x27; Error</h3>
<div class="forum-post-body">Hi Alb,<br>
<br>
<br>
<br>
Just make sure you have the correct MPLAB compiler installed for your application.  If you plan to run the 'CompileAllModels' script please be aware that you're compiling models for a few different targets which in themselves require different compilers (either C30 or C32).  They can both be downloaded from the Microchip website.<br>
<br>
<br>
<br>
Hope that helps,<br>
<br>
<br>
<br>
Ed</div>
</article>

