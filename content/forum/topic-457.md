---
title: "MPLAB 8.x project not generated properly during compile"
url: "/forum/topic/457/"
archiveKind: "topic"
---
# MPLAB 8.x project not generated properly during compile

Forum : [bug reports](/forum/#forum-8)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p1737">
<header><strong>bmairs</strong><time datetime="2011-11-07 19:25 UTC">2011-11-07 19:25 UTC</time></header>
<div class="forum-post-body">I'm compiling a project and the MPLAB 8.x project isn't being properly generated. I'm seeing the following at the end of code generation:<br>
<pre><code>"    ---33fJ256GP710---" 
"*** Created "executable": ..\../code_gen.cof"	 
''pic30-bin2hex ..\../code_gen.cof  
"*** Converted code_gen.cof to code_gen.hex"	 
. 
"***  MPLAB: file -&gt; import, choose code_gen.hex. Configure -&gt; Configuration Bits : Verify !" 
"       Download into the chip and run."		 
### Successful completion of Real-Time Workshop build procedure for model: code_gen
***  You could open project created and (re)compile it :
   	  ==&gt; MPLAB 8: Within Matlab, right-click code_gen.mcp -&gt; open outside Matlab.
   	  ==&gt; MPLAB X: Start MPLAB X, then open the project folder C:\Users\Bryant\Projects\Autoboat\Code\basic_model\code_gen_dspic
The path '\circBuffer.c' does not exist
<wbr>
Warning : MPLAB project not created due to internal error</code></pre><br>
<br>
My project does include a variety of external C files, though none have the path '\circBuffer.c':<br>
<pre><code>clib/conversions.c
clib/nmea0183.c
clib/nmea2000.c
clib/ecanSensors.c
clib/gps.c
clib/revo.c
clib/commProtocol.c
clib/uart1.c
clib/uart2.c
clib/DEE.c
clib/DEES.s
clib/misc.c
../../../ECAN_dspic/circBuffer.c
../../../ECAN_dspic/ecanFunctions.c</code></pre><br>
<br>
I've also played with location of circBuffer.c within the list of files to include and it made no difference whether it was at the head of the list or towards the bottom.<br>
<br>
<br>
<br>
I have also tried opening the MPLAB X project, but it looks like it doesn't delete them before regeneration, so it isn't generating new MPLAB X projects either.</div>
</article>

<article class="forum-post" id="p1748">
<header><strong>LubinKerhuel</strong><time datetime="2011-12-05 10:26 UTC">2011-12-05 10:26 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">Hello Bryant,<br>
<br>
<br>
<br>
I tested a tiny model with two c files declared as follow: (Code Generation - Custom Code - additional Source files):<br>
<pre><code>..\..\CFunctionCall\MyCFunction.c
test/myfunction2.c</code></pre><br>
I could not reproduce the problem.<br>
<br>
<br>
<br>
Which blockset version do you currently have ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1749">
<header><strong>bmairs</strong><time datetime="2011-12-06 21:45 UTC">2011-12-06 21:45 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">I have version 3.66b. I'm also seeing compilation work for some other projects that I have, so it seems specific to this one.</div>
</article>

<article class="forum-post" id="p1750">
<header><strong>LubinKerhuel</strong><time datetime="2011-12-06 21:57 UTC">2011-12-06 21:57 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">I might test compiling your project on my system if that's not too huge.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1755">
<header><strong>bmairs</strong><time datetime="2011-12-10 00:36 UTC">2011-12-10 00:36 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">You'll need to add the two non-Autoboat directories to the matlab path. The actual model is in \Autoboat\Code\basic_model.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/454-Projects.zip">Pièce jointe : Projects.zip</a></p>
</article>

<article class="forum-post" id="p1776">
<header><strong>resodad</strong><time datetime="2012-01-10 12:33 UTC">2012-01-10 12:33 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">Bryant,<br>
<br>
I get this error:<br>
<br>
"<br>
<br>
The following error occurred processing the System Target File '':<br>
<br>
Undefined function or variable "version".<br>
<br>
"<br>
<br>
when I build.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1778">
<header><strong>bmairs</strong><time datetime="2012-01-12 02:36 UTC">2012-01-12 02:36 UTC</time></header>
<h3>Re: MPLAB 8.x project not generated properly during compile</h3>
<div class="forum-post-body">This was fixed for me in the new 3.7b release.</div>
</article>

