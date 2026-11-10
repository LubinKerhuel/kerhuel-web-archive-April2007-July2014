---
title: "Thrust for unmanned two-engine aircraf : Problem with blocks"
url: "/forum/topic/70/"
archiveKind: "topic"
---
# Thrust for unmanned two-engine aircraf : Problem with blocks

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p144">
<header><strong>Phil</strong><time datetime="2007-12-28 20:22 UTC">2007-12-28 20:22 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I encountered some problems with my model while generating the code. I think I made something wrong in the configuration, but could not figure out what it was. Maybe you could help me? <br>
<br>
For better understanding here is waht i want to do: I am building a syncronization for the thrust for an unmanned two-engined aircraft. Therefor I need two inputs (Input Capture) for the engine speed, which will be converted with the 2D look up table (which should normally consist of mor values) (by entering the engine speed and velocity) into thrust of the airscrew. Then I take the difference of the to thrusts and compare it with the difference I want to have (ADC INput1). Then next two blocks are for the PI-Controller. The ADC Input (AN_0) represenst the signal I get from the autopilot for the speed of the aircraft. This signal will be added/subtracted with the signal from the controller and changes the mass flow to the engine (PWM Motor Output).<br>
<br>
<br>
<br>
Here is the error message:<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'dspic_model'. MATLAB error message:<br>
<br>
Error using ==&gt; RTW.genMakefileAndBuild<br>
<br>
Error(s) encountered while building model "dspic_model".<br>
<br>
<br>
<br>
<br>
<br>
And this is what it said before:  (I also uploaded the model)<br>
<br>
<br>
<br>
### Starting Real-Time Workshop build procedure for model: dspic_model<br>
<br>
### Generating code into build directory: D:\My Documents\Studienarbeit Chile\Messungen\dspic_model_dspic\sources<br>
<br>
Number of I/O PINs used : 4<br>
<br>
<span style="color:#0000ff">[...] (removed by Lubin)</span><br>
<br>
dspic_model.c: In function `dspic_model_step': <br>
<br>
dspic_model.c:89: error: `ic2RisingPeriode' undeclared (first use in this function) <br>
<br>
dspic_model.c:89: error: (Each undeclared identifier is reported only once <br>
<br>
dspic_model.c:89: error: for each function it appears in.) <br>
<br>
dspic_model.c:340:1: warning: "config2" redefined <br>
<br>
dspic_model.c:325:1: warning: this is the location of the previous definition <br>
<br>
gmake: *** [dspic_model.o] Error 0xff<br>
<br>
<br>
<br>
<br>
<br>
Thanks for your help<br>
<br>
<br>
<br>
Philipp</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/2-dspic_model.mdl">Pièce jointe : dspic_model.mdl</a></p>
</article>

<article class="forum-post" id="p145">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-28 22:35 UTC">2007-12-28 22:35 UTC</time></header>
<h3>Re: Thrust for unmanned two-engine aircraf : Problem with blocks</h3>
<div class="forum-post-body">Thanks for your message Phil.<br>
<br>
<br>
<br>
The error comes from the multiple use of blocks that should be used only once in a model :<br>
<br>
If you are to use more that one Input Capture port, <strong><span style="color:#0000ff">use only One block IC</span></strong> and configure this block to get many IC ports. <br>
<br>
Same remark for the ADC block,PWM motor block, OC block and others. Only The Digital Write, Read can be present in multiple place in a model. Same for the Rx-Tx blocks and the Tx-for-Matlab-Labview...<br>
<br>
<br>
<br>
Find attach the model with some modifications that compile. I also added few remarks. It would be fine if we could have a look on the final version (when the controller works).<br>
<br>
<br>
Few question remains : why is the PI only controlling the differential trust. Isn't it possible to use 2 PI? ( one for differential and one for common thrust, or more simple : one for each motor).<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/3-Trust_twoEngineAircraft.mdl">Pièce jointe : Trust_twoEngineAircraft.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/5-Trust_twoEngineAircraft.png">Pièce jointe : Trust_twoEngineAircraft.png</a></p>
</article>

