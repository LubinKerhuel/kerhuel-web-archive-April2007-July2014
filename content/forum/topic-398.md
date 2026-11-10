---
title: "Microstick"
url: "/forum/topic/398/"
archiveKind: "topic"
---
# Microstick

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1575">
<header><strong>boyce</strong><time datetime="2011-05-15 00:02 UTC">2011-05-15 00:02 UTC</time></header>
<div class="forum-post-body">Has anyone successfully compiled for the Microchip Microstick? <br>
<br>
<br>
<br>
I was hoping I could just bring the generated project into MPLAB, compile it, and upload it to the Microstick (it uses the Start Kits Tool). The code compiles just fine, but when I upload the code I get <br>
<br>
<br>
<br>
"Starter Kit board connected<br>
<br>
Firmware version: 00.00.03<br>
<br>
Programming and verifying...done<br>
<br>
Unable to Enter Debug Mode<br>
<br>
Target removed"<br>
<br>
<br>
<br>
and then it refuses to recognize the board as a Starter Kit.<br>
<br>
<br>
<br>
Anyone else have better luck?<br>
<br>
<br>
<br>
Thanks.</div>
</article>

<article class="forum-post" id="p1576">
<header><strong>LubinKerhuel</strong><time datetime="2011-05-15 15:58 UTC">2011-05-15 15:58 UTC</time></header>
<h3>Re: Microstick</h3>
<div class="forum-post-body">Lee, I just copy the solution you sent by email<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Mail - Lee</header>I found the problem; it was the configuration bits. I had left the previous settings which had an external oscillator. The Microstick only uses an internal oscillator, so in the Master block, I needed to set Oscillator Mode to Internal Fast RC (I also turned off the PLL for now). Apparently, the wrong clock bits throws MPLAB off so that it doesn't recognize the device as a Starter Kit.</blockquote><br>
<br>
Alternatively, you could also add a quartz (or external oscillator) to the kit. This solution is quite easy and gives you the possibility to use a serial bootloader. (And serial connexion also, internal RC is not precise enough. The blockset is not able yet to measure timing for correcting he baud rate)<br>
<br>
<br>
<br>
I attached an early example here, where I tested the new clock switching capabilities.  <br>
<br>
It is now possible to have a bootloader running at a fixed frequency (PLL), and to configure the application with another PLL configuration.<br>
<br>
Note also that a simulink block (from blockset) allows to do clock switching for saving power for example (however, peripheral will not works correctly then)<br>
<br>
All these functions are working, but not documented yet and without example also ;-)<br>
<br>
<br>
<br>
I attached here the firmware of a bootloader based on <a href="http://mrmackey.no-ip.org/elektronik/ds30loader/">ds30</a> using the microstick where I added a external clock running at 4MhZ.<br>
<br>
A simulink model running at a frequency different from the bootloader is also present.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/416-MicroStick_33Fj64MC802.7z">Pièce jointe : MicroStick_33Fj64MC802.7z</a></p>
</article>

