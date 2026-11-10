---
title: "Warning at opening time and can't open dialog in library"
url: "/forum/topic/52/"
archiveKind: "topic"
---
# Warning at opening time and can't open dialog in library

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p87">
<header><strong>northbear</strong><time datetime="2007-07-17 08:24 UTC">2007-07-17 08:24 UTC</time></header>
<div class="forum-post-body">hi,  Lubin<br>
<br>
<br>
<br>
I dowload the "install_dsPIC_R2007a.zip" from your website today, then install it acording to your installing instructions. all is ok.<br>
<br>
 <br>
<br>
but, when dual click the "Embedded Tartget for Microchip dsPIC" from the "Simulink Library Browse", the following warning occurs:<br>
<br>
<br>
<br>
<span style="color:green">Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In load_system at 52<br>
<br>
  In libbrowse&gt;i_LoadSys at 142<br>
<br>
  In libbrowse&gt;LoadLibrary at 121<br>
<br>
  In libbrowse at 24</span><br>
<br>
<br>
<br>
why?<br>
<br>
<br>
<br>
Expect your reply.<br>
<br>
<br>
<br>
and the "dsPIC_33f_Explorer16.mdl" can be open, but the warning is followed:<br>
<br>
<br>
<br>
<span style="color:blue">&gt;&gt; open dsPIC_33f_Explorer16.mdl  <br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'FPBOR'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'MCLR'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'ADC_TYPE12'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'VoltRef'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'OutFormatBits'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'NCHANNEL'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'ANCHANNELS_BITEWISE'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
NbrPortUsed is 6</span><br>
<br>
<br>
<br>
why?</div>
</article>

<article class="forum-post" id="p90">
<header><strong>LubinKerhuel</strong><time datetime="2007-07-21 09:38 UTC">2007-07-21 09:38 UTC</time></header>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : northbear</header>hi,  Lubin<br>
<br>
<br>
<br>
I dowload the "install_dsPIC_R2007a.zip" from your website today, then install it acording to your installing instructions. all is ok.<br>
<br>
 <br>
<br>
but, when dual click the "Embedded Tartget for Microchip dsPIC" from the "Simulink Library Browse", the following warning occurs:<br>
<br>
<br>
<br>
<span style="color:green">Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption at 34<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.<br>
<br>
&gt; In load_system at 52<br>
<br>
  In libbrowse&gt;i_LoadSys at 142<br>
<br>
  In libbrowse&gt;LoadLibrary at 121<br>
<br>
  In libbrowse at 24</span><br>
<br>
<br>
<br>
why?<br>
</blockquote><br>
The blockset dialog box can only be opened when they are placed into a simulink diagram file with the correct parameters set (Fixed Step, and Target File defined as dsPIC)<br>
<br>
(for Simplicity, you could start your new diagram from an example file given.)<br>
<br>
<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : northbear</header><br>
and the "dsPIC_33f_Explorer16.mdl" can be open, but the warning is followed:<br>
<br>
<br>
<br>
<span style="color:blue">&gt;&gt; open dsPIC_33f_Explorer16.mdl  <br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'FPBOR'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting in Master block (mask) 'Master' for parameter 'MCLR'.<br>
<br>
&gt; In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'ADC_TYPE12'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'VoltRef'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'OutFormatBits'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'NCHANNEL'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/ADC Input' : dsPIC : ADC10 block (mask) does not have a parameter named 'ANCHANNELS_BITEWISE'.<br>
<br>
&gt; In F:\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4<br>
<br>
  In F:\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87<br>
<br>
  In general\private\openmdl at 13<br>
<br>
  In open at 146<br>
<br>
NbrPortUsed is 6</span><br>
<br>
<br>
<br>
why?</blockquote><br>
<br>
don't take attention to warning appearing at oppening of a diagram. While oppening diagram, each block are loaded and initialized one after another. However, some blocks need other blocks to be loaded before them. <br>
<br>
<br>
<br>
Note that once the diagram is fully loaded, all blocks are initialized.  These warning should not appear when presing the update button.</div>
</article>

