---
title: "PTsources files not found. MPLAB project file not created."
url: "/forum/topic/442/"
archiveKind: "topic"
---
# PTsources files not found. MPLAB project file not created.

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1703">
<header><strong>abrixy</strong><time datetime="2011-09-19 20:58 UTC">2011-09-19 20:58 UTC</time></header>
<div class="forum-post-body">I  my name is Sandra from Belgium<br>
<br>
<br>
<br>
I would like to test the Blockset with the Explorer 16 board and a DSpic33.<br>
<br>
<br>
<br>
But I already made 2 install one, on XP and on Vista<br>
<br>
<br>
<br>
and i always have the same problem it seems not see the compiler but they are both installed :<br>
<br>
<br>
<br>
&gt;&gt;!pic30-lm<br>
<br>
Microchip MPLAB C30 License Manager Version v3_25 (Build Date Oct 11 2010). <br>
<br>
Copyright (c) 2008 Microchip Technology Inc. All rights reserved. <br>
<br>
Academic license for MPLAB C for 16-bit devices, <br>
<br>
   does not expire. <br>
<br>
This demo-version license for MPLAB C for dsPIC devices, <br>
<br>
   has expired. <br>
<br>
<br>
<br>
When I launch compilation the command window give me this message :<br>
<br>
<br>
<br>
PTsources files not found. MPLAB project file not created.<br>
<br>
sources files not found. MPLAB project file not created.<br>
<br>
<br>
<br>
and i get a error in the pop-up window<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'dsPIC_33f_Explorer16'. MATLAB error message:<br>
<br>
Error using ==&gt; make_rtw<br>
<br>
Too many output arguments.<br>
<br>
<br>
<br>
My configuration is MATLAB7.50(R2007B) so i used this script to install : install_dsPIC_R2007b.m<br>
<br>
<br>
<br>
I tried to install with and without administrator rights on vista + a test on XP<br>
<br>
Nothing seems to work<br>
<br>
it just create me a slprj directory but no .HEX<br>
<br>
I'm used to  generate c code for simulink but i have no experience to compile it into MATLAB<br>
<br>
<br>
<br>
Thanks  Sandra</div>
</article>

<article class="forum-post" id="p1709">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-21 06:34 UTC">2011-09-21 06:34 UTC</time></header>
<h3>Re: PTsources files not found. MPLAB project file not create</h3>
<div class="forum-post-body">Hi Sandra,<br>
<br>
<br>
<br>
Could you post the complete message you get when compilint (all lines written at matlat command windows).<br>
<br>
Are you compiling a model from the example directory or is it your own model ? if so, please upload it on the forum.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1713">
<header><strong>abrixy</strong><time datetime="2011-09-21 14:21 UTC">2011-09-21 14:21 UTC</time></header>
<h3>Re: PTsources files not found. MPLAB project file not create</h3>
<div class="forum-post-body">Hi, <br>
<br>
<br>
<br>
there is not much info on the console when compiling<br>
<br>
<br>
<br>
&gt;&gt; sources files not found. MPLAB project file not created.<br>
<br>
<br>
<br>
+ the error window :<br>
<br>
<em><br>
<br>
Error building Real-Time Workshop target for block diagram 'dsPIC_33f_Explorer16'. MATLAB error message:<br>
<br>
Error using ==&gt; make_rtw<br>
<br>
Too many output arguments.</em><br>
<br>
<br>
<br>
I do open an compile an example model for explorer 16. "dsPIC_33f_Explorer16" <br>
<br>
<br>
<br>
<strong>this is the console log when i open the model.:<br>
<br>
</strong><br>
<pre><code>&gt;&gt;
<wbr>
Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
D:\work\dspic\execBatch.p is a case-insensitive match and will be used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactMatch').
&gt; In C:\Program Files\MATLAB\R2007b\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 73
  In C:\Program Files\MATLAB\R2007b\toolbox\rtw\rtw\rtwprivate.p&gt;rtwprivate at 12
  In C:\Program Files\MATLAB\R2007b\toolbox\rtw\rtw\stf4target.p&gt;stf4target at 35
  In C:\Program Files\MATLAB\R2007b\toolbox\rtw\rtw\stf2target.p&gt;stf2target at 61
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 50: block_diagram does not have a parameter named
'CovForceBlockReductionOff'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 55: block_diagram does not have a parameter named
'CovModelRefEnable'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: dsPICdrivers.mdl, line 56: block_diagram does not have a parameter named
'CovExternalEMLEnable'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target
&gt; In D:\work\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation
==&gt; Configuration Parameters ==&gt; Real Time workshop
&gt; In D:\work\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 408
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
PWarning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and
UART Tx.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 124
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and
Output Compare.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 182
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and PWM
Output Compare.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 199
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and
ADC.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 281
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and
Change Notification.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 311
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and SPI
In.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 331
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and SPI
Out.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 333
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and SPI
Clock Output.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 350
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and CAN
Bus.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 399
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and CAN
Bus.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 400
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and I2C
Bus.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 462
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: --- =========&gt;  PORT A0 is used by at least two peripheral :  UART Rx and I2C
Bus.
&gt; In D:\work\blocks\dsPIC_PortSetting.p&gt;setTypePort at 638
  In D:\work\blocks\dsPIC_PortSetting.p&gt;dsPIC_PortSetting at 463
  In D:\work\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 89
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
TLibrary detected, Fixed Step artificially set to 1ms
Warning: In instantiating linked block 'dsPIC_33f_Explorer16/Master' : Invalid setting
in Master block (mask) 'Master' for parameter 'MCLR'.
&gt; In D:\work\blocks\dsPIC_ADC_callback_InitMask.p&gt;dsPIC_ADC_callback_InitMask at 9
  In D:\work\blocks\dsPIC_UART_Rx_Tx_Matlab_InitMask.p&gt;dsPIC_UART_Rx_Tx_Matlab_InitMask at 9
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
***** Solver Mode change from Auto to SingleTasking (this mode allows single rate and multirate). See help to get the difference with the MultiTasking mode which is now supported by the blockset *****
new GMAKE path : C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\support\PIC24F\gld\p24fJ96GA010.gld
      --&gt; corrected : find in --script=C:\PROGRA~1\MICROC~1\mplabc30\v3.25\support\PIC24F\gld\p24fJ96GA010.gld
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libpic30-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\PIC24F\libpPIC24Fxxx-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\PIC24F\libpPIC24Fxxx-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libc-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libc-coff.a
file not found : C:\PROGRA~2\MICROC~1\mplabc30\v3.25\lib\libm-coff.a
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\lib\libm-coff.a
directory not found : C:\Program Files\Microchip\mplabc30\v3.25\include
      --&gt; corrected : find in C:\PROGRA~1\MICROC~1\mplabc30\v3.25\include
 </code></pre><br>
<br>
3 test have been performed now on .<br>
<br>
Vista / XP / and Win7 by my collegue<br>
<br>
<br>
<br>
they all gives the same error.<br>
<br>
<br>
<br>
<br>
<br>
It's a pitty because your modules seems to be a really nice approach for prototyping.<br>
<br>
<br>
<br>
Thanks<br>
<br>
Sandra</div>
</article>

<article class="forum-post" id="p1714">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-21 17:20 UTC">2011-09-21 17:20 UTC</time></header>
<h3>Re: PTsources files not found. MPLAB project file not create</h3>
<div class="forum-post-body">Could you post the model on the forum ? (or by email is it's not to be published)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1715">
<header><strong>abrixy</strong><time datetime="2011-09-22 10:04 UTC">2011-09-22 10:04 UTC</time></header>
<h3>Re: PTsources files not found. MPLAB project file not create</h3>
<div class="forum-post-body">It's the example model i downloaded from your website in the zip from the R2007b block-set.<br>
<br>
<br>
<br>
I didn't make any change to it <br>
<br>
<br>
<br>
As I have a explore 16 board I wanted to test on it .<br>
<br>
<br>
<br>
Thanks<br>
<br>
Sandra</div>
</article>

