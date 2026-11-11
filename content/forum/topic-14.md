---
title: "error while opening Master Block or compiling model"
url: "/forum/topic/14/"
archiveKind: "topic"
---
# error while opening Master Block or compiling model

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p19">
<header><strong>arci</strong><time datetime="2007-04-19 22:50 UTC">2007-04-19 22:50 UTC</time></header>
<div class="forum-post-body">I downloaded your dspic library for simulink/matlab, but it generates error msg sometimes,"error:evaluating "OpenFcn" callback of masterblock .......named 'LDPICTYPE' ". My simulink file contains only dspic master block and when double click this block, error occured.<br>
<br>
<br>
<br>
<br>
<br>
arci</div>
</article>

<article class="forum-post" id="p20">
<header><strong>LubinKerhuel</strong><time datetime="2007-04-19 23:39 UTC">2007-04-19 23:39 UTC</time></header>
<div class="forum-post-body">Hi Arci,<br>
<br>
<br>
<br>
You are not using the last version of the toolbox. <br>
<br>
<br>
<br>
I noticed this problem and the new version would give a more comprehensive error message :<br>
<br>
<br>
<br>
<span style="color:darkblue">Error evaluating 'OpenFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 24<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.</span><br>
<br>
<br>
<br>
When you get this message ( or the one you obtain with the older toolbox described in the previous post)<br>
<br>
<br>
<br>
You MUST go to the <br>
<br>
<span style="color:red">Simulation </span>menu, then<br>
<br>
<span style="color:red">Configuration Parameters</span>, and go to the <br>
<br>
<span style="color:red">Real Time Workshop</span> menu and Set the <br>
<br>
<span style="color:red">System Target File</span> to <span style="color:red">dsPIC</span> (It must be in the list)<br>
<br>
<br>
<br>
<br>
<br>
Please, have a look on the first part of the "Sinus PWM" animation where I build a small diagram for dsPIC from scratch : <a href="/RTWdsPIC/examples/SinusPWM.html">http://archive.kerhuel.eu/RTWdsPIC/examples/SinusPWM.html</a><br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p223">
<header><strong>barryforever</strong><time datetime="2008-02-18 15:35 UTC">2008-02-18 15:35 UTC</time></header>
<h3>Re: error while opening Master Block or compiling model</h3>
<div class="forum-post-body">I receive the same error when i try compiling using mplab c30 using the mplab matlab tool <br>
<br>
This is what i get <pre><code>&lt;i&gt;
&lt;/i&gt;Opening Matlab session and model 'C:\Documents and Settings\Barry\My Documents\MATLAB\idid\deport.mdl'
Please wait...
<wbr>
Warning: Error evaluating 'LoadFcn' callback of
Master block (mask) 'Master'. Error using ==&gt;
dsPIC_ConfigRTWOption at 34
The *System Target File must be defined to dsPIC
Real Time workshop (Simulation ==&gt; Configuration
Parameters ==&gt; Real Time workshop.
&gt; In &lt;a href="error:C:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m,14,1"&gt;MplabOpenModel at 14&lt;/a&gt;
Warning: In instantiating linked block
'deport/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR'.
&gt; In &lt;a href="error:C:\Program Files\Microchip\MPLAB IDE\Tools\Matlab\MplabOpenModel.m,14,1"&gt;MplabOpenModel at 14&lt;/a&gt;
<wbr>
</code></pre><br>
<br>
I use MATLAB R2007b and MPLAB 8 and your toolbox 18.02.08</div>
</article>

<article class="forum-post" id="p224">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-18 19:15 UTC">2008-02-18 19:15 UTC</time></header>
<h3>Re: error while opening Master Block or compiling model</h3>
<div class="forum-post-body">The blockset is not compatible yet with the MPLAB plugging that open and "import" the C code generated into MPLAB.<br>
<br>
<br>
<br>
I recommend compiling the mdl schematic into a .hex file from simulink. You can import C code using the "custom C function block" (only on the registered version of the blockset). <br>
<br>
<br>
<br>
If you want to import the C code generated into a MPLAB project, use the procedure described <a href="/RTWdsPIC/examples/ImportSimulinkMPLAB.html">here</a>.</div>
</article>

