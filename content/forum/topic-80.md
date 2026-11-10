---
title: "How can I open RS232 user interface?"
url: "/forum/topic/80/"
archiveKind: "topic"
---
# How can I open RS232 user interface?

Forum : [General Remark and Questions](/forum/#forum-1)

16 message(s) · archive en lecture seule

<article class="forum-post" id="p171">
<header><strong>surfer</strong><time datetime="2008-01-31 06:45 UTC">2008-01-31 06:45 UTC</time></header>
<div class="forum-post-body">Please tell me if there is someone who can give me a detailed guide to open RS232gui interface, I'm beginner in Matlab simulation.<br>
<br>
I'm trying to find the "Interface Tx-Matlab" and the ",atlab prompt" but no results....<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p172">
<header><strong>LubinKerhuel</strong><time datetime="2008-01-31 07:47 UTC">2008-01-31 07:47 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">To open the RS232gui user interface, either you type at the matlab prompt : <br>
<br>
&gt;&gt; <span style="color:#0000bf">rs232gui</span><br>
<br>
<br>
<br>
or you place the block <br>
<br>
<img loading="lazy" src="/RTWdsPIC/Blocks/Img/InterfaceTxMatlab.png" alt="Image du forum"> <br>
<br>
in you model, and you double click on it to open the interface.</div>
</article>

<article class="forum-post" id="p178">
<header><strong>surfer</strong><time datetime="2008-02-02 12:33 UTC">2008-02-02 12:33 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Thank you "LubinKerhuel" for help!<br>
<br>
I've trayed "rs232gui" under prompt command but it doesn't work!!!<br>
<br>
Look what I've got as comment:<br>
<br>
<br>
<br>
&gt;&gt; rs232gui<br>
<br>
??? Undefined function or variable 'rs232gui'.<br>
<br>
<br>
<br>
please try to help me to find this gui interface.<br>
<br>
Best reguards.</div>
</article>

<article class="forum-post" id="p179">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-02 13:04 UTC">2008-02-02 13:04 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Wen you installed the toolbox, the installer unpacked the two files rs232gui.p and rs232gui.gui in the '/blocks'  directory.<br>
<br>
The blocks directory is also added in the matlab path. (File -&gt; Set Path ...).<br>
<br>
<br>
<br>
Check that theses two files are present in the blocks directory. Try to launch the rs232gui.p file (type rs232gui at the prompt). Since the blocks directory is added in the maltab path, it should be found whatever is your current active directory. If it does not work, try to launch it from the blocks directory.<br>
<br>
<br>
<br>
I do not see any others reason. Does anybody get the same error ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p180">
<header><strong>surfer</strong><time datetime="2008-02-02 13:53 UTC">2008-02-02 13:53 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Hello Lubin, tell me please the toolbox is installed seperatly or auto installed under matlab install? I'm searching the 2 files as you have indicated but I haven't find it!<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p181">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-02 14:04 UTC">2008-02-02 14:04 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body"><blockquote>the toolbox is installed seperatly</blockquote><br>
<br>
download it here : <br>
<br>
<a href="/RTWdsPIC/download.html">http://www.kerhuel.eu/RTWdsPIC/download.html</a></div>
</article>

<article class="forum-post" id="p182">
<header><strong>surfer</strong><time datetime="2008-02-02 14:18 UTC">2008-02-02 14:18 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Sorry this is fo dspic and not an installable software!<br>
<br>
I've found:<br>
<br>
install_dsPIC_R2006a.m<br>
<br>
<br>
<br>
How can I get the installable toolbox?<br>
<br>
<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p183">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-02 15:02 UTC">2008-02-02 15:02 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : surfer</header>install_dsPIC_R2006a.m</blockquote><br>
<br>
This file is the Matlab script that will install the toolbox in the current folder. Launch it at the matlab prompt.</div>
</article>

<article class="forum-post" id="p184">
<header><strong>surfer</strong><time datetime="2008-02-03 10:36 UTC">2008-02-03 10:36 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Hello,<br>
<br>
thank you Lubinm.<br>
<br>
I've succeeded to establish the serial communication link with my serial interface evaluation board based on a PIC16F877. There is response in communication PIC-PC and the buffer is filled with received data, but when I preview the plotted figure nothing is plotted.<br>
<br>
There still some error messages like the followings:<br>
<br>
<br>
<br>
??? Error using ==&gt; unknown<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
Error in ==&gt; RS232_analyzBloc at 117<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; rs232gui&gt;pushStart_Callback at 254<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 75<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; rs232gui at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback.<br>
<br>
<br>
<br>
Please try to help me getting. I just want to get data from srial port and plot it in real time.<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p185">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-03 11:25 UTC">2008-02-03 11:25 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">The rs232gui interface: <br>
<br>
<img loading="lazy" src="/RTWdsPIC/Blocks/Img/InterfaceTxMatlabDialog.png" alt="Image du forum"> <br>
<br>
should be used with the block <br>
<br>
<img loading="lazy" src="/RTWdsPIC/Blocks/Img/TxOutputMultiplexed.png" alt="Image du forum"><br>
<br>
<br>
<br>
The block builds a communication layer to allow plotting up to 16 different data channel coded using either 8, 16 or 32 bits data.<br>
<br>
For details about the communication layer, there is a description on my <a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">french website</a>.<br>
<br>
<br>
<br>
In your case, I guess that you want to plot raw data (without using the communication layer) : uint8.<br>
<br>
==&gt; Push the "donneesBrutes" (ie, "Raw data") button of the interface.</div>
</article>

<article class="forum-post" id="p186">
<header><strong>surfer</strong><time datetime="2008-02-03 13:20 UTC">2008-02-03 13:20 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Thank you Lubin,<br>
<br>
can you help me to make a labview interface the same as you have showed in your frensh website!<br>
<br>
Just us I've told you, getting 16 bit data format and plot it in an appropriate graph.<br>
<br>
The data are a real teperature value sensed from the PIC16F877 to the PC.<br>
<br>
<br>
<br>
I'm so grateful to you.<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p187">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-04 22:48 UTC">2008-02-04 22:48 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Hi Surfer !<br>
<br>
<br>
<br>
I hope to publish the Labview schematic that can decode the data sent by the dsPIC (encoded with the simulink block Tx_Matlab_Labview). I currently do not find time to do it. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p189">
<header><strong>surfer</strong><time datetime="2008-02-05 05:05 UTC">2008-02-05 05:05 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Thanks Lubin  :)  <br>
<br>
Please can you help me to write a program in Matlab, that acquire data from serial port and plot it in real time.<br>
<br>
I thought there is three instuctions to program this task, try to help me please.<br>
<br>
Best regards.</div>
</article>

<article class="forum-post" id="p190">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-05 22:16 UTC">2008-02-05 22:16 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Hi Surfer,<br>
<br>
<br>
<br>
You will find many forums with useful help. The matlab help is also very useful.<br>
<br>
However, from my experiment:<br>
<br>
On matlab, and with some computer (depending on its own hardware)<br>
<br>
Opening serial communication will crash matlab if data are being sent from the other side, while matlab open the serial line<br>
<br>
Also, sometime, it is necessary to send one or two data (char) through the serial before being able to receive any from it.</div>
</article>

<article class="forum-post" id="p191">
<header><strong>surfer</strong><time datetime="2008-02-06 05:27 UTC">2008-02-06 05:27 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">Ok, as I think is not prefered to interface serial port with Matlab! So can I use visual basic?<br>
<br>
Bets Regards</div>
</article>

<article class="forum-post" id="p192">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-06 21:33 UTC">2008-02-06 21:33 UTC</time></header>
<h3>Re: How can I open RS232 user interface?</h3>
<div class="forum-post-body">It's at your convenience...</div>
</article>

