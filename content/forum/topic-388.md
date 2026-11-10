---
title: "rs232gui problem"
url: "/forum/topic/388/"
archiveKind: "topic"
---
# rs232gui problem

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1553">
<header><strong>alex</strong><time datetime="2011-04-20 14:45 UTC">2011-04-20 14:45 UTC</time></header>
<div class="forum-post-body">hello ,<br>
<br>
i am  trying  to  use a demo  version  before  the  real  version ,  and  i have  a problem.<br>
<br>
after  building  the same  diagram  from  the presentation  i pass  the  compilation  and  i get a wrong  massage  when i  try  to  connect  to  rs232 gui  in order  to  get  a  graph  of  accelerometers   value.<br>
<br>
(after  connection  i  push  "start"  and  i get  the massage: <br>
<br>
<br>
<br>
&gt;&gt; <br>
<br>
redefinition SerialCOM<br>
<br>
??? Attempted to access s_control_pos(1); index out of bounds because numel(s_control_pos)=0.<br>
<br>
<br>
<br>
Error in ==&gt; C:\Users\alex\AppData\Local\Temp\Rar$DI00.579\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc<br>
<br>
at 78<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; C:\Users\alex\AppData\Local\Temp\Rar$DI00.579\blocks\rs232gui.p&gt;pushStart_Callback at 305<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; C:\Users\alex\AppData\Local\Temp\Rar$DI00.579\blocks\rs232gui.p&gt;rs232gui at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback<br>
<br>
<br>
<br>
what may  be the problem?<br>
<br>
<br>
<br>
&gt;&gt; thank you</div>
</article>

<article class="forum-post" id="p1554">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-20 16:07 UTC">2011-04-20 16:07 UTC</time></header>
<h3>Re: rs232gui problem</h3>
<div class="forum-post-body">Did you use the block <a href="/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/">Tx_Output_Multiplexed_For_Matlab-Labview</a> ?<br>
<br>
<br>
<br>
Is the baud rate right ? (are you using an RC oscillator which have low precision, or a precise quartz ?)<br>
<br>
<br>
<br>
You could try to press "Raw", bottom left of the interface to get the raw value that the PC is receiving. Try to check if data received are Ok or not.<br>
<br>
<br>
<br>
Lubin</div>
</article>

