---
title: "Confused about calculus time step"
url: "/forum/topic/253/"
archiveKind: "topic"
---
# Confused about calculus time step

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p992">
<header><strong>cjaskolski</strong><time datetime="2009-11-07 05:27 UTC">2009-11-07 05:27 UTC</time></header>
<div class="forum-post-body">I am using calculus time step to try to understand what load the processor is running at. What I have found is odd.<br>
<br>
<br>
<br>
For a simulation time configured as 1E-5, I varied the sample time of an ADC block that was just converted to binary and the LSB used to drive a digital line (model attached). The outputs of the calculus time step block are T and PR1. My PIC is configured at 40MIPS. I was sampling Calculus Time Step at 100Hz and using the TX_Labview_Matlab block for serial output. My results were:<br>
<br>
<br>
<br>
ADC sampling at 10Hz            PR1=400  T=106<br>
<br>
ADC sampling at 1000Hz        PR1=400   T=104<br>
<br>
ADC sampling at 100000Hz    PR1=400    T=82<br>
<br>
<br>
<br>
The PR1 of 400 makes sense (40M/100K=400), but I would have expected that at 100kHz the T would be MUCH MUCH greater than at 10Hz. What am I missing? Is my processor really running at 25% load at 10Hz ADC sampling and 20% load at 100,000Hz?</div>
</article>

<article class="forum-post" id="p993">
<header><strong>cjaskolski</strong><time datetime="2009-11-07 05:36 UTC">2009-11-07 05:36 UTC</time></header>
<h3>Re: Confused about calculus time step</h3>
<div class="forum-post-body">Forgot to attach the model. Here it is. I am using Matlab r2009b.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/278-calculus_timestep_test.mdl">Pièce jointe : calculus_timestep_test.mdl</a></p>
</article>

<article class="forum-post" id="p994">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-07 09:59 UTC">2009-11-07 09:59 UTC</time></header>
<h3>Re: Confused about calculus time step</h3>
<div class="forum-post-body">Hey Corey,<br>
<br>
<br>
<br>
Thanks for this interresting question.<br>
<br>
These measurement are absolutly normal.<br>
<br>
<br>
<br>
- You changed the sampling time of the ADC inside the ADC block.<br>
<br>
- The model time-step was fixed at 100Khz (T = 10us) (quite high). PR1 = 400 : 400 instructions are executed within 10us<br>
<br>
- The 20% or 25% load you measured here correspond to the background task : an average of (106 ,104 ,84) instructions are executed within each 10us time-step. (background code is simpler when blocks are sampled at the same sampling time as the model, explaining the unexpected load decrease while ADC is sampled here at 100kHz.)<br>
<br>
<br>
<br>
The ADC block works with interruptions. The channel AN_4 is sampled "continuously" (via interruption, at 10.1us here) what ever is the ADC block output rate. The  ADC block output undersample these value at the ADC block sampling time. Thus, the model load does not depend on the ADC sampling rate.<br>
<br>
<br>
<br>
What you may want to do is : <br>
<br>
to set the ADC sampling rate to -1 and change it through the model time-step. That would modify PR1 while T remains constant (around 100). The dsPIC % load will decrease as sampling rate decrease. <br>
<br>
<br>
<br>
<br>
<br>
On the experience you made, the very small change you want to see is the time for copying of the LSB of the AN_4 to the A1 digital output (following code). <br>
<pre><code>   98     /* S-Function "ADC" Block: &lt;Root&gt;/ADC Input */
   99     calculus_timestep_test_B.ADCInput = ADC1BUF0;
  100   
  101     /* DataTypeConversion: '&lt;Root&gt;/Data Type Conversion' incorporates:
  102      *  S-Function (sfix_bitop): '&lt;Root&gt;/Bitwise Operator'
  103      */
  104     calculus_timestep_test_B.DataTypeConversion =
  105       ((calculus_timestep_test_B.ADCInput &amp;
  106         calculus_timestep_test_P.BitwiseOperator_BitMask) != 0U);
  107   
  108     /* S-Function "dsPIC_Digital_OutputWrite" Block: &lt;Root&gt;/Digital Output Write1 */
  109     LATAbits.LATA1 = calculus_timestep_test_B.DataTypeConversion;
  110   }
</code></pre><br>
<br>
More precisely, you are not measuring the time of part of code in your two first experiences:<br>
<br>
The Time Step block output the is the time step of the <strong>previous model time step</strong> ! (The current time step which is not finished and cannot be measured yet)<br>
<br>
<br>
<br>
When the model is sampled at 100kHz and ADC to Digital output calculation is executed at 1kHz (100x slower), it may be interresting to compare one step where calculation is done (1kHz) and one step where nothing is done (99 of the steps within 10us)!<br>
<br>
to do so :<br>
<br>
- configure ADC block sampling time to .001 (1kHz)<br>
<br>
- place one Time Step blocks with sampling time set to : [.001 0]<br>
<br>
- place another Time Step blocks with sampling time set to [0.001 .00001]<br>
<br>
(after these two Time Step blocks, you will have to place a transition rate converter to send both values to the Tx_Matlab_Labview block.)<br>
<br>
==&gt; The first Time Step block provides the measure for the time step <strong>prior to</strong> the ADC to A1 calculations<br>
<br>
==&gt; The second Time Step block provides the measure for the time step <strong>with </strong>ADC to A1 calculations<br>
<br>
<br>
<br>
sampling time parameters composed of two figures : [Samplint time    -   Offset]<br>
<br>
<br>
<br>
Let me know if you need any precisions<br>
<br>
It would be interresting to get your feedback or results you received. <br>
<br>
<br>
<br>
Lubin</div>
</article>

