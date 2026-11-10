---
title: "Rx Input Multiplexed?"
url: "/forum/topic/131/"
archiveKind: "topic"
---
# Rx Input Multiplexed?

Forum : [dsPIC Peripherals](/forum/#forum-9)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p400">
<header><strong>NigmaTech</strong><time datetime="2008-05-28 22:35 UTC">2008-05-28 22:35 UTC</time></header>
<div class="forum-post-body">Hi!<br>
<br>
<br>
<br>
I;m thinking about controling duty cycle of PWM's in my dsPIC using a joystick connected to computer. I'm trying to use yaw, pitch, roll axis and throttle from "joystick" block in "Virtual Reality Toolbox", data should be transfered via RS-232. Is that possible to make it using your blockset Lubin?</div>
</article>

<article class="forum-post" id="p401">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-28 23:21 UTC">2008-05-28 23:21 UTC</time></header>
<h3>Re: Rx Input Multiplexed?</h3>
<div class="forum-post-body">Hi NigmaTech,<br>
<br>
<br>
<br>
All required dsPIC peripheral for this application are suported by the blockset. The blockset will help to build in no time the software for the dsPIC.<br>
<br>
<br>
<br>
You will have two Simulink model : <br>
<br>
- model onboard the dsPIC<br>
<br>
- model for the user interface running on your PC<br>
<br>
<br>
<br>
You have to create your own "high level protocol" to send data from the PC to the PIC throw UART.<br>
<br>
<br>
<br>
On the model onboard the dsPIC, use the UART Rx block to receive data. Once information from UART is decoded, the PWM will be sent throw either one of the peripheral able to generate a PWM signal (PWM Motor, Output Compare)<br>
<br>
<br>
<br>
For the user interface, The hard part is to send data to the UART port from Simulink. I saw once a block able to do it (not a Mathworks block !)<br>
<br>
<br>
<br>
Btw, For this kind of application, I would recommend to use Labview to build the Graphical User Interface. (I built such a system few years ago, see <a href="http://lubink.free.fr/projelectro/Autopilote_2005/Autopilote_2005_fr.html">http://lubink.free.fr/projelectro/Autop ... 05_fr.html</a> (french) )<br>
<br>
Matlab can do it, but it is more difficult and the result is not as user friencly as with labview.</div>
</article>

<article class="forum-post" id="p428">
<header><strong>NigmaTech</strong><time datetime="2008-06-19 12:06 UTC">2008-06-19 12:06 UTC</time></header>
<h3>Re: Rx Input Multiplexed?</h3>
<div class="forum-post-body">Could I request You for an example of Simulink model for transmitting data from PC to dsPIC? I need something simple to transmit data via at least one channel, i.e. thrust from joystick via Simulink to dsPIC using RS-232. Probably I should to use xPC blockset but I don't know how  :cry:</div>
</article>

<article class="forum-post" id="p429">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-19 20:31 UTC">2008-06-19 20:31 UTC</time></header>
<h3>Re: Rx Input Multiplexed?</h3>
<div class="forum-post-body">I am not sure xPC is the solution: As far as I know, Virtual reality blockset will not work on xPC Target.<br>
<br>
The solution may be to find (on the web) the Simulink block that is able to send data throw Serial port. It is the hard part! <br>
<br>
Otherwise, you can write your own block function for simulink and use the command line instructions to send data (from simulink) through UART.<br>
<br>
<br>
<br>
From the PIC, Serial port Rx block is very easy to use and should not be a problem.</div>
</article>

<article class="forum-post" id="p442">
<header><strong>NigmaTech</strong><time datetime="2008-07-19 09:40 UTC">2008-07-19 09:40 UTC</time></header>
<h3>Re: Rx Input Multiplexed?</h3>
<div class="forum-post-body">Could You make an example of Interface in LabView available? Something to sending data, receiving and presenting on grapf diagram. I've got evaluate version of LabView 8.5. I have never used it before  :(</div>
</article>

<article class="forum-post" id="p443">
<header><strong>LubinKerhuel</strong><time datetime="2008-07-27 22:35 UTC">2008-07-27 22:35 UTC</time></header>
<h3>Re: Rx Input Multiplexed?</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I will not have time to do it soon.<br>
<br>
I have to clean up the existing labview files I have.<br>
<br>
<br>
<br>
I attach an old project where labview was used to watch the variables (like the matlab interface rs232gui) and to send new configuration parameters.<br>
<br>
This was for a plane. Few screenshoot are available on my french website : <a href="http://lubink.free.fr/projelectro/Autopilote_2005/Autopilote_2005_fr.html">http://lubink.free.fr/projelectro/Autop ... 05_fr.html</a><br>
<br>
Data transmission from the PIC use the protocole implemented in the dsPIC block "Tx for Matlab Labview"<br>
<br>
<br>
<br>
All labview files of this project are in the .rar file attached. It is provided as is !<br>
<br>
It may be quite messy in its present form.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/97-Labview.rar">Pièce jointe : Labview.rar</a></p>
</article>

