---
title: "Generated MPLAB projects don't properly include source files"
url: "/forum/topic/371/"
archiveKind: "topic"
---
# Generated MPLAB projects don't properly include source files

Forum : [bug reports](/forum/#forum-8)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p1506">
<header><strong>bmairs</strong><time datetime="2011-03-09 19:03 UTC">2011-03-09 19:03 UTC</time></header>
<div class="forum-post-body">In my Simulink projects I've used relative paths to include some source files for compilation, like "..\..\..\..\..\ecan\circBuffer.c". When the MPLAB project is generated it just tacks this relative path onto the absolute path of the current working directory so I have file descriptions that look like "E:\DOCUME~1\BRYANT~1\MYDOCU~1\projects\Autoboat\autoboat\Code\BASIC_~1\tests\..\..\..\..\..\ecan\circBuffer.c". MPLAB does not like paths that look like that and I get file not found errors if I try to open that project file within MPLAB. If I change that above source file to specify "E:\DOCUME~1\BRYANT~1\MYDOCU~1\projects\ecan\circBuffer.c" it naturally works just fine.<br>
<br>
<br>
<br>
Is it possible to evaluate relative paths before specifying those files within the MPLAB project? Just doing that should fix all of these problems.<br>
<br>
<br>
<br>
By the way, I really like this feature of generating MPLAB projects for the source. Makes debugging MUCH easier!</div>
</article>

<article class="forum-post" id="p1510">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-10 16:33 UTC">2011-03-10 16:33 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : bmairs</header>Is it possible to evaluate relative paths before specifying those files within the MPLAB project? Just doing that should fix all of these problems.</blockquote> That should be possible, thanks for your suggestion.<br>
<br>
<br>
<br>
It may be even better to have a relative path for such file witin the MPLAB project.<br>
<br>
Would MPLAB accept path like ".\..\..\..\..\..\ecan\circBuffer.c" ?<br>
<br>
If so, I'll try to make the function smarter... <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1520">
<header><strong>bmairs</strong><time datetime="2011-03-27 21:34 UTC">2011-03-27 21:34 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body">This still doesn't work right. Now it just doesn't include the filepath now. I've attached the project generated upon compilation.<br>
<br>
<br>
<br>
I've also noticed that the dir_inc variable is defined incorrectly. Notice the start that is "code_gen_dspic\sourcescode_gen_dspic\sources;.;;" The include directories aren't been appended correctly, so I'm not sure if this actually mattered, but I did notice it.<br>
<br>
<br>
<br>
The source files I'm including are:<br>
<br>
../../../../ecan/circBuffer.c<br>
<br>
../../../../ecan/ecanFunctions.c<br>
<br>
clib/gps.c<br>
<br>
clib/commProtocol.c<br>
<br>
clib/uart2.c<br>
<br>
clib/DEE.c<br>
<br>
clib/DEES.s<br>
<br>
clib/misc.c</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/396-code_gen.zip">Pièce jointe : code_gen.zip</a></p>
</article>

<article class="forum-post" id="p1521">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-28 06:49 UTC">2011-03-28 06:49 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body">Is this project published on git, like SLUG ? Where could I find a version that should compile ?<br>
<br>
I would like to test on your project so as to find the problem that clearly appears here. (It worked on more simple example I tested so far, even with any change in the directory).<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1525">
<header><strong>bmairs</strong><time datetime="2011-03-30 19:25 UTC">2011-03-30 19:25 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body">The code_gen.mdl file is in my Autoboat repo: <a href="https://github.com/Susurrus/Autoboat">https://github.com/Susurrus/Autoboat</a><br>
<br>
<br>
<br>
It also relies on the ecan library here: <a href="https://github.com/Susurrus/ECAN_dspic">https://github.com/Susurrus/ECAN_dspic</a><br>
<br>
<br>
<br>
I have the projects laid out as follows:<br>
<br>
/projects<br>
<br>
/projects/Autoboat/AUTOBOAT_REPO<br>
<br>
/projects/ECAN_REPO<br>
<br>
<br>
<br>
So the autoboat repo is one level deeper than the ecan repository I have.</div>
</article>

<article class="forum-post" id="p1534">
<header><strong>bmairs</strong><time datetime="2011-04-07 18:47 UTC">2011-04-07 18:47 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body">The MPLAB projects generated upon compilation now properly includes all of my source files and builds a debuggable build without configuring any other options. Pretty awesome!<br>
<br>
<br>
<br>
I see the following warning at the end about a tcpip file not being found. It isn't part of any sources I included in the project. Do you know what's causing this?<br>
<br>
<br>
<blockquote>"***   MPLAB: file -&gt; import, choose code_gen.hex. Configure -&gt; Configuration Bits : Verify ! Download into the chip and run."		 <br>
<br>
"***   Alternatively, (re-)compile the MPLAB project : Within Matlab, right-click code_gen.mcp -&gt; open outside Matlab will open the MPLAB project. Compile, modify..."	 <br>
<br>
### Successful completion of Real-Time Workshop build procedure for model: code_gen<br>
<br>
--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</blockquote></div>
</article>

<article class="forum-post" id="p1535">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-07 21:17 UTC">2011-04-07 21:17 UTC</time></header>
<h3>Re: Generated MPLAB projects don&#x27;t properly include source f</h3>
<div class="forum-post-body">Thanks for testing the early blockset version I sent and for the feedback.<br>
<br>
I will try to published thie version soon to succeed to the v3.4c.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : bmairs</header>--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</blockquote><br>
This indicates that matlab included the directory "C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip" to the search path of the compiler. <br>
<br>
<br>
<br>
This directory contains files to support the so called "external mode" which allows changing tunable variables from the PC while the model is running. This mode is not implemented in the current version of the blockset thus the directory containing theses file is not necessary theses files are not required.<br>
<br>
<br>
<br>
I think that maltab include all directory containing potential useful functions (each blockset directory function...). <br>
<br>
The matlab internal directory structure has change a little bit with newer matlab version. Thus, the directory not found might have been added by an older matlab version to the project, and the newer matlab version did not corrected the include path. <br>
<br>
<br>
<br>
So, just do not pay attention. <br>
<br>
If you wish to remove the message, I would propose to create a new simulink model and copy-past all your model and model parameters. <br>
<br>
<br>
<br>
You might also check that you did not activate the "external mode" in the simulink configuration panel. This mode is useless for the dsPIC blockset as not implemented (yet).<br>
<br>
<br>
<br>
Lubin</div>
</article>

