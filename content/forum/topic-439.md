---
title: "MPLAB X link post-compilation errors"
url: "/forum/topic/439/"
archiveKind: "topic"
---
# MPLAB X link post-compilation errors

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1694">
<header><strong>bmairs</strong><time datetime="2011-09-09 18:31 UTC">2011-09-09 18:31 UTC</time></header>
<div class="forum-post-body">Clicking the MPLAB X link within MATLAB gives me an error and doesn't launch MPLAB X. The link for launching MPLAB 8, however, is correct.<br>
<br>
<br>
<br>
Here is what I see at the end of compilation along with the errors. After compilation I clicked the MPLAB X link, then the MPLAB 8 link, then the MPLAB X link again, which is what the additional output shows.<br>
<br>
<br>
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
   	  ==&gt; MPLAB X: Start MPLAB X, open the project folder C:\Users\Bryant\Projects\Autoboat\Code\basic_model\code_gen_dspic
???  disp('Starting MPLAB X... 
          |
Error: A MATLAB string constant is not terminated properly.
<wbr>
Starting MPLAB 8...
Starting MPLAB 8...
???  disp('Starting MPLAB X... 
          |
Error: A MATLAB string constant is not terminated properly.
</code></pre></div>
</article>

<article class="forum-post" id="p1697">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-12 18:55 UTC">2011-09-12 18:55 UTC</time></header>
<h3>Re: MPLAB X link post-compilation errors</h3>
<div class="forum-post-body">Thanks for bug report,<br>
<br>
<br>
<br>
bug corrected in version 3.6c. Note however than MPLAB X do not open your project (like MPLAB 8). I do not know yet how  to make this happend...<br>
<br>
<br>
<br>
Lubin</div>
</article>

