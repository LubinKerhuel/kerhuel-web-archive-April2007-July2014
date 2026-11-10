---
title: "OC and Matlab2010a"
url: "/forum/topic/298/"
archiveKind: "topic"
---
# OC and Matlab2010a

Forum : [bug reports](/forum/#forum-8)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1190">
<header><strong>Ender</strong><time datetime="2010-04-28 01:43 UTC">2010-04-28 01:43 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
In Matlab 2010 32bits Vista and the Blockset 2010a V3.2B, I got a new issue never see before with the toolbox 2007 version on the output compares.<br>
<br>
So I tried with OC1 and OC2, in the simplified model attached and first the signal frequency is not very stable, and mostly with the settings:<br>
<br>
<br>
<br>
'Max/channel' at : 2.5e-005 , the pulse signal period is 20ms so 50Hhz rather than 40KHz and 25uS  :? <br>
<br>
<br>
<br>
and for :<br>
<br>
<br>
<br>
'Max/channel' at : 0.001 , the pulse signal period is 1.1ms so close but not good.  :wink:<br>
<br>
<br>
<br>
Any idea ?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/334-Evoly_OC.mdl">Pièce jointe : Evoly_OC.mdl</a></p>
</article>

<article class="forum-post" id="p1196">
<header><strong>Ender</strong><time datetime="2010-04-28 17:22 UTC">2010-04-28 17:22 UTC</time></header>
<h3>Re: OC and Matlab2010a</h3>
<div class="forum-post-body">:idea: I tested something and the problem is linked with the idle mode. When the idle is disable the OC work fine, the frequency are good and stable. So it could be a wake up time issue on the OC interrupt.<br>
<br>
<br>
<br>
<br>
<br>
About consumption :<br>
<br>
<br>
<br>
 :arrow: Lubin, what is for you the good way to use the idle ? Do you advice to not use some peripheral in idle mode for example ? For me the idle put down the core when all calculus are done  and there is still some time before a peripheral interrupt or a base timer restart the loop code. On this way all peripherals have to continue to work and the core wouldn’t  lost anything when it’s wake up… But maybe I’m wrong ?<br>
<br>
 <br>
<br>
:arrow: I’m interested by going in sleep mode too. But something easy I don’t want (for the moment) a wake up on interrupt, WDT or other IC. I just want to go in sleep mode when the battery is low to avoid deep discharge. I think to use the C call function to go in sleep mode when the battery level in under a threshold so the wake up will be on a reset (new battery) . Do you have a ready or easier way to do it? I think it’s a common problem for people using rechargeable battery mostly Li-ion and Li-Po. How did you do on your fly project ? What about latter add just a new block to go on sleep mode and no wake up parameter, the instructions seem the same for most Pic</div>
</article>

<article class="forum-post" id="p1212">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-30 08:53 UTC">2010-04-30 08:53 UTC</time></header>
<h3>Re: OC and Matlab2010a</h3>
<div class="forum-post-body">:arrow: This is the way it is supposed to works. Nothing get lost while activating idle mode. However, developing without idle mode is advise, and then test should be done with power save mode (idle activated) activated.<br>
<br>
A specific peripheral (its name is Low Voltage Detection (LVD)) but it is not implemented yet on the blockset.   :( <br>
<br>
The problem that may appears with solution you propose: going into sleep mode using C call: All peripheral are configured to works, or Wake up the core, during the sleep mode. Thus, you will not get a very long sleep. Anyway, if reconfiguring bits in peripheral to make them not workable during sleep, dans also disabling all interrupts, it may be possible to get a deep sleep mode.<br>
<br>
<br>
<br>
<br>
<br>
 :arrow:  For Li-ion or Li-Po power cells, the best practice is to use a small circuit close to the battery that cut off battery power when voltage is lower than a predetermined threshold. Difficulties may appear when motor are driven from theses Li-Po/Li-ion cellules as a current peak may appears at motors start that may activate the cut-off circuit (this one is re-enabled automatically as soon as battery is charged, even for very short time (1s) ) . This way makes battery well protected but you must beware of current drain by rapid motor consign changes (an interesting constraint for control model) . If only electronics is driven, there should be no problems.<br>
<br>
<br>
<br>
During prototyping process, I usually get my Li-Po / Li-ion cells getting fat. Reason is either I draw too much current when cells drives motors. On electronics parts, the drop down of Li-po cells is very fast ad end of charge. Thus, the microcontroller stop working quite suddenly thus, I disconnect my li-po as soon as I see it.<br>
<br>
Of course, that is not the way to do for commercial products…<br>
<br>
<br>
<br>
Lubin</div>
</article>

