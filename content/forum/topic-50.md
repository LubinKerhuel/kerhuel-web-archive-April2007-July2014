---
title: "Bug, or Matlab needs P4 instruction set, or..."
url: "/forum/topic/50/"
archiveKind: "topic"
---
# Bug, or Matlab needs P4 instruction set, or...

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p71">
<header><strong>andor</strong><time datetime="2007-05-27 15:35 UTC">2007-05-27 15:35 UTC</time></header>
<div class="forum-post-body">I try to describe my problem:<br>
<br>
<br>
<br>
There is an interesting thing I’ve found I think it is a bug (but I don’t know whether Matlab or the toolbox has it). Firstly I tried the toolbox on my computer, I only do the basic things (ex. the demonstration things on your webpage and some more) and it worked (it is a must to change the character encoding with set_param(…), but it’s OK). Next I tried to design a control loop on a laptop but there were some problems even if I tried to build the demonstration example found on your web page. I can only guess that this is because the laptop has a Celeron 1200 MHz processor (Pentium 3 instruction set) and my PC has P4 instruction set (I’m not sure because I haven’t seen the real operation). When I completed set the parameters of the model (time step, solver) I tried to configure the master block (double click), but I got the following error message:<br>
<br>
<br>
<br>
"Error evaluating ‘OpenFcn’ callback of Master block (mask) ‘Untitled/Master’. Error using ==&gt; &lt;a href=”error:C:\MatdsPIC\blocks\dsPIC_MASTER_callback.p,30,1”&gt; dsPIC_MASTER_callback at 30 &lt;/a&gt;<br>
<br>
<br>
<br>
Corrupted package, Remove and Re-install dsPic embedded Target toolbox."<br>
<br>
<br>
<br>
Probably you’ve figured out that the project name was ‘Untitled’, and the installation path was ‘C:\MatdsPIC’.<br>
<br>
<br>
<br>
As far as I know Matlab needs P4 instruction set, but I haven’t met this problem before (and we don’t have P4 laptop).<br>
<br>
I don't understand why, but according to the Marhworks webpage Matlab needs P4 or above:<br>
<br>
<a href="http://www.mathworks.com/support/sysreq/current_release/">http://www.mathworks.com/support/sysreq ... t_release/</a><br>
<br>
but once I've downloaded a Unix installation guide that had specified p3 and above. Strange...<br>
<br>
By the way the laptop has 512 MB memory that meets the requirements, the PC has even more.<br>
<br>
<br>
<br>
I tried to reinstall the toolbox, even I reinstalled Matlab and the toolbox from scratch but the same thing happened. Because the clean installation, The laptop and my PC has the same settings.</div>
</article>

<article class="forum-post" id="p85">
<header><strong>LubinKerhuel</strong><time datetime="2007-06-09 10:50 UTC">2007-06-09 10:50 UTC</time></header>
<div class="forum-post-body">Hi andor,<br>
<br>
<br>
<br>
This is weird. Does anybody encounter the same problem ? I do not think it is in relationship with the processor. Either an unknow bug remains in the toolbox (please, if you get the same error, repport it) neither the toolbox is not properly installed. Try to check the installation : <br>
<br>
<br>
<br>
The installer m file should add the two subdirectory created: <br>
<br>
- *\dspic<br>
<br>
- *\blocks<br>
<br>
In the matlab path.<br>
<br>
--&gt;Check that this has been done correctly: <br>
<br>
in matlab : File ==&gt; set path and check that the theses two directory are present. If they are not, add them...<br>
<br>
<br>
<br>
It still doesn't work: <br>
<br>
Try to refresh the <span style="color:red">matlab path cache</span> if it is enable ; disable the path cache: <br>
<br>
File ==&gt; Preferences ==&gt; in the General Tab...<br>
<br>
<br>
<br>
It still doesn't work?<br>
<br>
<span style="color:red">The toolbox must not be installed in the matlab directory or subdirectory</span>. Make sure you did not install the toolbox inside the matlab directory or sudirectory !<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p86">
<header><strong>andor</strong><time datetime="2007-06-23 04:09 UTC">2007-06-23 04:09 UTC</time></header>
<div class="forum-post-body">Hi!<br>
<br>
<br>
<br>
I tried everything you mentioned but the problem remained...<br>
<br>
<br>
<br>
It is interesting because I configured everything (solver and the dsPIC.tlc)<br>
<br>
<br>
<br>
Here is the log that Matlab gived when I tried to configure the Master block:<br>
<br>
<br>
<br>
<br>
<br>
Warning: Error evaluating 'CopyFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
Warning: The dialog of 'untitled/Master' is being closed because a mask parameter has been changed.<br>
<br>
&gt; In C:\0dsPICMat\blocks\dsPIC_Set_Dialog_PopUp_Param.p&gt;dsPIC_Set_Dialog_PopUp_Param at 57<br>
<br>
  In C:\0dsPICMat\blocks\dsPIC_MASTER_callback_InitMask.p&gt;dsPIC_MASTER_callback_InitMask at 222<br>
<br>
### Starting Real-Time Workshop build procedure for model: untitled<br>
<br>
### Generating code into build directory: C:\Documents and Settings\Andor\Dokumentumok\MATLAB\untitled_dspic\sources<br>
<br>
### Real-Time Workshop build procedure for model: 'untitled' aborted due to an error.<br>
<br>
<br>
<br>
Maybe it is because of the (deleted) older version but I can't get myself trough... Maybe a total PC reinstall would help...<br>
<br>
<br>
<br>
Here is the error message I got after double clicking the master block:<br>
<br>
<a href="http://users.hszk.bme.hu/~ka465/DblClk.bmp">Image externe (non intégrée)</a><br>
<br>
Here is the error message I got after I tried to adjust the paramters by right click -&gt; mask parameters:<br>
<br>
<a href="http://users.hszk.bme.hu/~ka465/Mask.bmp">Image externe (non intégrée)</a><br>
<br>
And I got the configuration block but it's a little bit strange:<br>
<br>
<a href="http://users.hszk.bme.hu/~ka465/Params.bmp">Image externe (non intégrée)</a></div>
</article>

