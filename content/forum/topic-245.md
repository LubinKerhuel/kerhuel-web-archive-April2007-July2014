---
title: "Sample time C-function Call"
url: "/forum/topic/245/"
archiveKind: "topic"
---
# Sample time C-function Call

Forum : [General Remark and Questions](/forum/#forum-1)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p946">
<header><strong>catia</strong><time datetime="2009-09-10 01:48 UTC">2009-09-10 01:48 UTC</time></header>
<div class="forum-post-body">Hi Lubin, <br>
<br>
<br>
<br>
I currently use the C function call blockset as initialization, I would like to know what i have to put for the sample time for this blockset to be called only once. I have tried with 'inf' but it seems to call this blockset at every cycle.<br>
<br>
<br>
<br>
Cathia</div>
</article>

<article class="forum-post" id="p947">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-10 09:51 UTC">2009-09-10 09:51 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Hi Cathia,<br>
<br>
<br>
<br>
C function call is only working on registred version of the blockset.<br>
<br>
Thus, check that you have a registred version (are you working in ASU team that use a registred version ?)<br>
<br>
Else, you may be using the blockset build (or copied !) by Microchip.<br>
<br>
<br>
<br>
Anyway, inf time should activate the block only once at initialization. Else, you could use a triggered subsystem and place the c call function block inside this subsystem. (There are few examples like that on the forum).<br>
<br>
<br>
<br>
It may help to get the mdl file. Could you post it ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p948">
<header><strong>catia</strong><time datetime="2009-09-10 22:24 UTC">2009-09-10 22:24 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Hi Lubin, <br>
<br>
<br>
<br>
I am working in an ASU laboratory. So i must have the right version. Maybe i made a mistaske somewhere else, that would be why i have the impression to initialize at every cycle.<br>
<br>
<br>
<br>
Cathia</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/262-ecan2essai.mdl">Pièce jointe : ecan2essai.mdl</a></p>
</article>

<article class="forum-post" id="p949">
<header><strong>LubinKerhuel</strong><time datetime="2009-09-11 07:23 UTC">2009-09-11 07:23 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Hi Cathia,<br>
<br>
<br>
<br>
Could not compile to test (no c files attached).<br>
<br>
However, you could try this : <br>
<br>
<br>
<br>
in Simulation ==&gt; Configuration Parameters ==&gt; Optimization (left) ==&gt; Check box <strong>Inline parameters</strong>.<br>
<br>
<br>
<br>
Tips : You may have a better view of what's happening with :  Format ==&gt; <em>Sample Time Display</em> ==&gt; Color <br>
<br>
(update then the diagram, with or without the Optimization checked).<br>
<br>
<br>
<br>
This should works fine, however, if you prefere, you might use triggered subsystem with a step or so on... (browse the forum for examples)<br>
<br>
<br>
<br>
Let me know...<br>
<br>
<br>
<br>
another Tip : Simulink has binary shift blocks and you should rather use them instead of the Embedded MATLAB Function (which probably makes theses calculation with double data type ? this should be checked )<br>
<br>
<br>
<br>
If you are working on the ECAN peripheral (as your model's name suggest), it may be very useful to post results provided you have the rights to do so...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1449">
<header><strong>coolj</strong><time datetime="2011-01-21 17:10 UTC">2011-01-21 17:10 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I had a similar issue with version 3.4b of your blockset.  My inf time functions that were supposed to run only once were being called every time step.<br>
<br>
<br>
<br>
Once I enabled Simulation -&gt; Configuration -&gt; Optimization -&gt; Inline parameters, the inf-time initialization C functions were correctly called only once.<br>
<br>
<br>
<br>
Might want to add to the documentation, along with "inf" allowing for "run once".</div>
</article>

<article class="forum-post" id="p1451">
<header><strong>coolj</strong><time datetime="2011-01-24 02:34 UTC">2011-01-24 02:34 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Here is some background for inline parameters needing to be enabled to prevent inf-time functions from being called every time step.<br>
<br>
<br>
<br>
<a href="http://www.kxcad.net/cae_MATLAB/toolbox/simulink/ug/f7-9753.html">http://www.kxcad.net/cae_MATLAB/toolbox ... -9753.html</a><br>
<br>
<br>
<br>
inf<br>
<br>
<br>
<br>
The meaning of this sample time depends on whether the active model configuration's inline parameters optimization (see Inline parameters) is enabled.<br>
<br>
<br>
<br>
If the inline parameters optimization is enabled, inf signifies that the block's output can never change (see Constant Sample Time). This speeds up simulation and the generated code by <span class="underline">eliminating the need to recompute the block's output at each time step</span>. If the inline parameters optimization is disabled or the block with inf sample time drives an output port of a conditionally executed subsystem, Simulink treats inf as -1, i.e., as inherited sample time. This allows you to tune the block's parameters during simulation.</div>
</article>

<article class="forum-post" id="p1494">
<header><strong>jannypan</strong><time datetime="2011-03-05 06:07 UTC">2011-03-05 06:07 UTC</time></header>
<h3>Re: Sample time C-function Call</h3>
<div class="forum-post-body">Anyway, inf time should activate the block only once at initialization. Else, you could use a triggered subsystem and place the c call function block inside this subsystem. (There are few examples like that on the forum).</div>
</article>

