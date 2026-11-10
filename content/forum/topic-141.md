---
title: "LED blink - Real time and Quartz Configuration"
url: "/forum/topic/141/"
archiveKind: "topic"
---
# LED blink - Real time and Quartz Configuration

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p433">
<header><strong>carbon9</strong><time datetime="2008-06-29 07:01 UTC">2008-06-29 07:01 UTC</time></header>
<div class="forum-post-body">Hi all,<br>
<br>
<br>
<br>
First of all thanks to L. Kerhuel for this very useful blockset. I've installed it succesfully referencing to the animation on the web site. Also, I applied the sinusoidal motor driving example. The blockset compiles succesfully.<br>
<br>
<br>
<br>
So, going one step further, I tried to compile a new project. The aim is simple: <br>
<br>
<br>
<br>
1. Blink a LED connected to Port F.2 infinitely using a pulse on Simulink<br>
<br>
2. Drive a LED on Port D.2 if Port B.2 is made logic 1. <br>
<br>
<br>
<br>
The copy of my simulink file is attached to this message.<br>
<br>
<br>
<br>
I've sucessfully compiled the project and generated .hex file. I'm using BigdsPIC board with 30F6014A from Mikroe, I've downloaded the hex file on the board using Mikroe's download program. The program works. <br>
<br>
<br>
<br>
1. The LED on F.2 blinks with a period of about 0.4 sec<br>
<br>
2.  The LED on D.2 is ON if B.1 is made logic 1. <br>
<br>
<br>
<br>
But, my question is: I want to blink the LED on F.2 with 2 sec period. What can I adjust to make the period to 2 sec with 50% duty cycle?<br>
<br>
<br>
<br>
Regards</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/95-LEDblink.mdl">Pièce jointe : LEDblink.mdl</a></p>
</article>

<article class="forum-post" id="p434">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-29 10:30 UTC">2008-06-29 10:30 UTC</time></header>
<h3>Re: LED blink example question</h3>
<div class="forum-post-body">Hi carbon9,<br>
<br>
<br>
<br>
Few comments about the model: <br>
<br>
<br>
<br>
A simulation of the model shows that the led should be blinking at a rate of 1Hz (duty cycle of 0.5s).<br>
<br>
You do not get 1Hz because your quartz configuration (master block dialog box) may not be configured correctly (i.e. information provided to the simulink model are not conform to the material information).<br>
<br>
From your model configuration, the Quartz of the board should is : 2.5*4 = 10Mhz. This may be false.<br>
<br>
(See help of the Master Block on the website. I just updated it)<br>
<br>
<br>
<br>
I post a model with few comments: <br>
<br>
<br>
<br>
- Configure appropriate Quartz in Master block!<br>
<br>
- Use Color Sample time from the Format menu<br>
<br>
- Replace Pulse generator with a counter with a rate of 1 Hz (run simulation with simulink to check results)<br>
<br>
- Set Digital Input with a sampling rate of 1ms to get a more reactive result (base time step of the model, menu Simulation / Configuration Parameters / Solver)<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/96-LEDblink_v02.mdl">Pièce jointe : LEDblink_v02.mdl</a></p>
</article>

<article class="forum-post" id="p435">
<header><strong>carbon9</strong><time datetime="2008-07-01 05:39 UTC">2008-07-01 05:39 UTC</time></header>
<h3>Re: LED blink example question</h3>
<div class="forum-post-body">Thank you very much for your comments.<br>
<br>
<br>
<br>
Another question is: can we drive an LCD using the Simulink blockset?<br>
<br>
<br>
<br>
Regards</div>
</article>

<article class="forum-post" id="p436">
<header><strong>LubinKerhuel</strong><time datetime="2008-07-01 06:22 UTC">2008-07-01 06:22 UTC</time></header>
<h3>Re: LED blink example question</h3>
<div class="forum-post-body">It is probably possible to drive an LCD. What is the interface of the LCD ?<br>
<br>
If you have to create a complexe sequential logic, you could also use stateflow.<br>
<br>
<br>
<br>
In the worst case, use the "C Call function block" to write the driver for the LCD.<br>
<br>
( only available in the registred version of the blockset)</div>
</article>

<article class="forum-post" id="p437">
<header><strong>carbon9</strong><time datetime="2008-07-01 17:46 UTC">2008-07-01 17:46 UTC</time></header>
<h3>Re: LED blink - Real time and Quartz Configuration</h3>
<div class="forum-post-body">Thanks for the replies. I'll try and if works, will post on this forum.<br>
<br>
<br>
<br>
Regards</div>
</article>

