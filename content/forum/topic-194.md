---
title: "trial to run a dsPIC"
url: "/forum/topic/194/"
archiveKind: "topic"
---
# trial to run a dsPIC

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p706">
<header><strong>crh</strong><time datetime="2009-01-22 07:40 UTC">2009-01-22 07:40 UTC</time></header>
<div class="forum-post-body">Bonjour Lubin,<br>
<br>
<br>
<br>
I am trying to run a dsPIC30f4013 for the first time, together with a function generator. In the image attachment you see a screenprint from my scope and the pinlayout of the pic4013.<br>
<br>
When I start my simulink model I get the next intitial warning:<br>
<br>
<br>
<pre><code>Warning: dsPICdrivers.mdl, line 52: block_diagram does not have a parameter named 'CovModelRefEnable'.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption
at 100
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt;
Real Time workshop.
&gt; In general\private\openmdl at 13
  In open at 148
  In uiopen at 196
Warning: In instantiating linked block 'BCfirsttestwithLPfilter/ADC Input' : Invalid setting in dsPIC : ADC10 block
(mask) 'ADC Input' for parameter 'OutFormatBitspopup'.
&gt; In C:\My Toolbox\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 4
  In C:\My Toolbox\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In general\private\openmdl at 13
  In open at 148
  In uiopen at 196.</code></pre><br>
<br>
When I compile the model, I get the warning/error:<br>
<pre><code>''pic30-gcc  -c -mcpu=30f4013 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Users\Casparus\DOCUME~1\MATLAB\Work\WORKFL~1\SIMPLE~1\BCFIRS~1\sources - 
dsPIC_UART1_Interrupt.c: In function '_U1TXInterrupt': 
dsPIC_UART1_Interrupt.c:19: warning:  PSV model not specified for '_U1TXInterrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_UART1_Interrupt.c: In function '_U1RXInterrupt': 
dsPIC_UART1_Interrupt.c:31: warning:  PSV model not specified for '_U1RXInterrupt'; 
   assuming 'auto_psv' this may affect latency
and at the end the message:
*** Version 0.98fe                            16-Sep-2008      " 
"*** For Matlab 7.5             R2007b       " 
"*** Created "executable": ..\../BCfirsttestwithLPfilter.coff"	 
''pic30-bin2hex ..\../BCfirsttestwithLPfilter.coff  
"*** Created "executable": ..\../BCfirsttestwithLPfilter.hex"	 
### Successful completion of Real-Time Workshop build procedure for model: BCfirsttestwithLPfilter</code></pre><br>
<br>
Next, I write the hex file with a Pickit2 in the pic4013. Then I connect the funtion generator with the pic. As you can see in the printscreen of the scope, there is no correlation between the frequency of the generator and the pic4013. The only thing is, when I change the frequency of the generator the frequency of the pic is changing, but it seems to be without  any correlation.<br>
<br>
Please, can you provide me with some helpful hints?<br>
<br>
<br>
<br>
Kind regards,<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/188-BCfirsttestwithLPfilter.mdl">Pièce jointe : BCfirsttestwithLPfilter.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/189-scope_4013.gif">Pièce jointe : scope+4013.gif</a></p>
</article>

<article class="forum-post" id="p707">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-22 20:07 UTC">2009-01-22 20:07 UTC</time></header>
<h3>Re: trial to run a dsPIC</h3>
<div class="forum-post-body">Hello Casparus,<br>
<br>
<br>
<br>
First of all, do not take into account any error message while you open a model.<br>
<br>
Then, compilation finished without error, so it’s seems to be Ok, problems are no there.<br>
<br>
<br>
<br>
As far as I understand, you want to make a digital LP filter at 148Hz. A very first remark is from a theoretical signal processing point of view: The sampling time (model step time) is 1/300s. Thus, all frequency above 150Hz will recopy themselves inside the 0-150Hz band creating aliasing. You should use an analog filter to take out all frequency above 150Hz before the A/D conversion take place. <br>
<br>
<br>
<br>
Anyway, there are few problems with your model:<br>
<br>
<br>
<br>
*30f4013 has a 12 bit ADC. Thus, the first uint8 Data type conversion block after the ADC will certainly saturate.<br>
<br>
<br>
<br>
*about the LP filter: all coefficients are stored in double format (that is a good point because their value look like 0.014552788094050004). Thus the multiplications are done in double. Thus, there is no reason to make the output a uint8 value. The output of the first calculation could vary between 0 and 4 (0.014*255) only. There is a major problem with fixed point calculation here. <br>
<br>
<br>
<br>
*Some coefficient are negative ==&gt; Major problem when result is stored in an unsigned variable.<br>
<br>
<br>
<br>
You may consider using a IIR filter that usually give good filtering results with fewer taps than a FIR filters. (That may allow leaving all calculation in double inside the dsPIC).<br>
<br>
<br>
<br>
I would recommend to do simulation test (start with the file attached). Start using double calculation only ; then, try to use the fixed point tools to make the calculation efficient on the dsPIC.<br>
<br>
<br>
I hope this will help.<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/190-BCfirsttestwithLPfilter_Simulation.mdl">Pièce jointe : BCfirsttestwithLPfilter_Simulation.mdl</a></p>
</article>

<article class="forum-post" id="p727">
<header><strong>crh</strong><time datetime="2009-02-05 07:49 UTC">2009-02-05 07:49 UTC</time></header>
<h3>Re: trial to run a dsPIC</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
In the meantime, I have made a study of the FDAT tool in Simulink.<br>
<br>
I have developed a LP 145Hz filter. According to the attachment it is working.<br>
<br>
From this point on, I developed a model in order to implement it in dsPIC30f4013.  See attachment.  <br>
<br>
With my scope, I get a frequency signal on the U1ATX pin, but it is not equal to the signal of my function generator on pin AN0/Vref.<br>
<br>
<br>
<br>
I developed also the same model with a fixed point filter (based on the original LP filter), but the same problem.<br>
<br>
<br>
<br>
Till now, I spend a lot of time to develop a working filter on a dsPIC. I do not care, because my goal is to learn everything about MCU’s, and this I like very much.  But if you have a very simple model with a filter which I can upload into a pic and can check with a function generator on pin AN0/Vref and a scope on pin U1ATX , I should be very grateful. <br>
<br>
<br>
<br>
Kind regards, Casparus.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/200-LPsimulation.mdl">Pièce jointe : LPsimulation.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/201-LP145floatwithADCUART.mdl">Pièce jointe : LP145floatwithADCUART.mdl</a></p>
</article>

<article class="forum-post" id="p728">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-05 18:49 UTC">2009-02-05 18:49 UTC</time></header>
<h3>Re: trial to run a dsPIC</h3>
<div class="forum-post-body">Hi Casparus,<br>
<blockquote><header class="quote-author">Citation : crh</header>I have developed a LP 145Hz filter</blockquote><br>
* Same problems remains: filtering at 145Hz with a sampling rate at 300Hz is a non sense. (See sampling theory <a href="http://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem">http://en.wikipedia.org/wiki/Nyquist%E2 ... ng_theorem</a>)<br>
<br>
* Output visualisation: your signal is likely to be greater than 255 (ADC output value is within a 10 or 12 bit range and positive only). You should output your signal via a 16 bit variable. I suggest using the <a href="/wiki/simulink-embedded-target-for-pic/">TX_Labview_MATLAB</a> block to send the data, and to see your data on your PC with the <a href="/wiki/simulink-embedded-target-for-pic/">rs232GUI</a> interface that comes with the dsPIC blockset.<br>
<br>
* The designed filter is a FIR with many taps. Calculation are in double, the number or instruction of your dsPIC is not that high (2.5MIPS ?). You should make sure that the dsPIC has time to make the calculation within the defined time step (3.3ms, hopefully that's a large time step). Use the <a href="/wiki/simulink-embedded-target-for-pic/">Overload Flag Port</a> option available on the master block or the <a href="/wiki/simulink-embedded-target-for-pic/">Calculus Time Step block</a><br>
<br>
<br>
<br>
The filter calculation itself may work well (from your simulation). There may be problems at the output level and in the real time calculation.<br>
<br>
<br>
<br>
for a simple example, go to the example directory of the dsPIC blockset and open the model dsPIC_33f_Explorer16.mdl. Two very simple IIR filters <a href="/wiki/simulink-embedded-target-for-pic/">are designed</a> and may be adapted for your microcontroller. Make sure to adapt the time step on your model to use theses filters properly. Otherwise, you may have to change the filters coefficient...<br>
<br>
<br>
<br>
Lots of useful information about <a href="http://en.wikipedia.org/wiki/Category:Digital_signal_processing">digital signal processing</a> is available on Wikipedia.<br>
<br>
<br>
<br>
Lubin</div>
</article>

