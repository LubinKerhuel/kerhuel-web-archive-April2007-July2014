---
title: "GUI in Matlab2010a with virtual Com port problem"
url: "/forum/topic/295/"
archiveKind: "topic"
---
# GUI in Matlab2010a with virtual Com port problem

Forum : [General Remark and Questions](/forum/#forum-1)

8 message(s) · archive en lecture seule

<article class="forum-post" id="p1170">
<header><strong>Ender</strong><time datetime="2010-04-21 20:25 UTC">2010-04-21 20:25 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I'm using a Bluetooth bridge for monitoring for 2 years now.<br>
<br>
With other Matlab version there was no issue to start the connection; but with Matlab2010 impossible to have a correct answer by using the 'Connexion' button in the GUI.<br>
<br>
<br>
<br>
When I use my own Labview GUI the 'Com' port is linked and the monitoring still works fine.<br>
<br>
Sure I don't have problem with the classic wired RS232, in Matlab2010 too.<br>
<br>
I test with different Bluetooth devices on different computer.<br>
<br>
So maybe, the latency or the something is different in this new Matlab version and it doesn't work anymore with the virtual serial port.<br>
<br>
<br>
<br>
Lubin:<br>
<br>
Are you still using the GUI with wireless link, like before on your flying projects?<br>
<br>
Is it a Bluetooth link ?<br>
<br>
Could you test the GUI with matlab2010 and a virtual com port ?<br>
<br>
<br>
<br>
This is not hurry for me, it's just to advice other user using virtual serial Com port before to update Matlab.<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p1172">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-21 23:56 UTC">2010-04-21 23:56 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">I did not test yet bluetooth virtual COM port with matlab 2010a.<br>
<br>
Are you using a mablab 32 or 64 bits ? <br>
<br>
<br>
<br>
I think that matlab serial connections rely on java. Thus, you may try updating java version (see matlab help to change matlab java)<br>
<br>
<br>
<br>
Anyway, from my former experiment (planes and robots with bootloader), bluetooth virtual COM port using software bluetooth stack is working, but is sometime tricky.<br>
<br>
<br>
<br>
To obtain a more comfortable bluetooth connection, you may use on the PC side an hardware bluetooth2serial adapter, (like <a href="http://www.free2move.se/index.php?type=view&amp;pk=22">free2move</a>) and if no serial ports are available on the PC, using a ftdi serial2usb adapter.<br>
<br>
Thus, you need 1 bluetooth and one serial adapter on the PC side like <a href="http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=71&amp;op=catalogue-product_info-null&amp;prodCategoryID=47">FTDI adapter</a>.<br>
<br>
This is more expensive than a bluetooth donble, but will avoid using a software bluetooth stack.<br>
<br>
<br>
<br>
What parts are you using (just for information)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1175">
<header><strong>Ender</strong><time datetime="2010-04-22 22:41 UTC">2010-04-22 22:41 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">I'm using a Free2move F2M03GLA SPP on the Dspic, and different computers and Bluetooth modules; include USB modules or free2move F2M03GLA HCI, for 4 years now on different microcontroller and for 2 years with the DSPsic and your GUI.<br>
<br>
<br>
<br>
Yes, because the RS232 works fine, I'm sure your idea to use a USB to RS232 + RS232 to Bluetooth works, but It's not comfortable. I'll use my Labview GUI for right now, thanks.<br>
<br>
  <br>
<br>
I didn't know Matlab use Java for it, It was a good idea so I updated java 6 from update 17 to 20, and I still get the same messages, it can't open the port :  <br>
<pre><code>[size=85][color=#FF0040]Connecting... May take few seconds...
??? Error using ==&gt; serial.fopen at 72
Cannot connect to the COM10 port. Possible reasons are another
application is connected to the port or the port does not exist.
<wbr>
Error in ==&gt; C:\Users\Thierry\Documents\MATLAB\XXX_Dspic\blocks\rs232gui.p&gt;pushConnexion_Callback at 122
<wbr>
<wbr>
Error in ==&gt; gui_mainfcn at 96
        feval(varargin{:});
<wbr>
Error in ==&gt; C:\Users\Thierry\Documents\MATLAB\XXX_Dspic\blocks\rs232gui.p&gt;rs232gui at 43
<wbr>
<wbr>
??? Error while evaluating uicontrol Callback
<wbr>
&gt;&gt; [/color][/size]</code></pre><br>
<br>
Another think, Matlab 2010a, is more case sensitive for the character then the precedent version. I had to change some of my code like from "False" to "false" for Boolean type, because the uppercase made a issue. <br>
<br>
And I got some warning about this too, I thing one was about the GUI but I can't cause it again, example :<br>
<blockquote>Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.<br>
<br>
C:\Users\Thierry\Documents\MATLAB\XXX_Dspic\dspic\execBatch.p is a case-insensitive match and will be<br>
<br>
used instead.<br>
<br>
You can improve the performance of your code by using exact<br>
<br>
name matches and we therefore recommend that you update your<br>
<br>
usage accordingly. Alternatively, you can disable this warning using<br>
<br>
warning('off','MATLAB:dispatcher:InexactCaseMatch').<br>
<br>
This warning will become an error in future releases. </blockquote></div>
</article>

<article class="forum-post" id="p1176">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-22 23:07 UTC">2010-04-22 23:07 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">There is a trick with matlab to make matlab use another java version:<br>
<br>
See: <a href="http://www.mathworks.com/access/helpdesk/help/techdoc/matlab_external/f98533.html#f122031">this mathworks page</a><br>
<br>
<br>
<br>
Anyway, I doubt that using another java version will solve the problem.<br>
<br>
<br>
<br>
Are you decoding frames from the <a href="/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/">Tx_Output_Multiplexed_For_Matlab-Labview</a> block with Labview?<br>
<br>
<br>
<br>
I did Labview decoding blocks a about 5 years ago. It was working pretty well, the Labview interface is much better to view real time data. I can provide theses Labview model if it can help. <br>
<br>
Anyway, protocol used by the <a href="/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/">Tx_Output_Multiplexed_For_Matlab-Labview</a> block is described (in french) on this <a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">website</a> (not updated anymore).</div>
</article>

<article class="forum-post" id="p1178">
<header><strong>Ender</strong><time datetime="2010-04-23 15:01 UTC">2010-04-23 15:01 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">Yes, I’m using the Tx_Output_Multiplexed_For_Matlab-Labview block with Labview. I never try the other block to send data with the UART. This  code is 2 years old when I start with your tool, I thought the protocol was too basic, my idea was too write another one with checksum and  time mark , or to try to win few bits in the transmission because the free2move Bluetooth is limited at 300Kb/s and I was interested to use just 2.5 bytes, to send 1 Uint16 rather than 3 bytes. But I have worked on something else and I never improve this code. I preferred to use your GUI.<br>
<br>
<br>
<br>
 Yes, I’m interested by your Labview code to compare your syncronisation code with mine please.<br>
<br>
<br>
<br>
I used two ways , nothing was perfect:<br>
<br>
The synchronization on the 05 header was done just one time when I start, when I try to re-synchronize on the fly, the code was not efficient enough. The code was looking for redundancy at the header mark  and if it was doing while the display was update, it got latency and lost bytes because the display had to work with too munch dots.<br>
<br>
I have tried another way too, by writing the data directly in a files or memory. With a little shift to display then after decimating the value to get a fast display with less accuracy. This work well and I added functions to save/read  and to export the data in mat file. But I got a problem of memory busy in Labview when I try to record too much time by this way. (I was interested to record 20min :wink: ) I didn’t find the way to release enough memory even though  I write the file on the hard drive by segment and try to keep just small table in memory.</div>
</article>

<article class="forum-post" id="p1182">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-26 00:34 UTC">2010-04-26 00:34 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">I uploaded my "old" labview schema on the wiki :<br>
<br>
bottom of page : <a href="/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/">http://www.kerhuel.eu/wiki/Block/Tx_Out ... ab-Labview</a> <br>
<br>
<br>
<br>
Tell me if you can't open it. I did it using an old labview (like 6 or 6.5). Old labview models are sometimes difficult to convert to newer labview version.<br>
<br>
I may find more recent copy of it.<br>
<br>
(I have no currently labview installed there)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1191">
<header><strong>Ender</strong><time datetime="2010-04-28 01:51 UTC">2010-04-28 01:51 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">I'm using Labview 8.5 (so 2007 or 2008 release I think) and it didn't display advices or anything when it was opening, everything seem fine.</div>
</article>

<article class="forum-post" id="p1313">
<header><strong>Vladimir</strong><time datetime="2010-10-26 22:18 UTC">2010-10-26 22:18 UTC</time></header>
<h3>Re: GUI in Matlab2010a with virtual Com port problem</h3>
<div class="forum-post-body">I have a problem with Tx-MatLab Block, I can't read the port, in the MatLab command window appears this error:<br>
<br>
<br>
<br>
??? Attempted to access s_control_pos(1); index<br>
<br>
out of bounds because numel(s_control_pos)=0.<br>
<br>
Error in ==&gt; C:\Documents and Settings\Vladi\My<br>
<br>
Documents\MATLAB\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc<br>
<br>
at 78<br>
<br>
Error in ==&gt; C:\Documents and Settings\Vladi\My<br>
<br>
Documents\MATLAB\blocks\rs232gui.p&gt;pushStart_Callback<br>
<br>
at 271<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
Error in ==&gt; C:\Documents and Settings\Vladi\My<br>
<br>
Documents\MATLAB\blocks\rs232gui.p&gt;rs232gui at 43 <br>
<br>
??? Error while evaluating uicontrol Callback</div>
</article>

