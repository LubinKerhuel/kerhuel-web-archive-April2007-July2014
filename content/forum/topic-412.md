---
title: "ADC block sets configures all pins to the ADC"
url: "/forum/topic/412/"
archiveKind: "topic"
---
# ADC block sets configures all pins to the ADC

Forum : [bug reports](/forum/#forum-8)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p1600">
<header><strong>bmairs</strong><time datetime="2011-06-08 23:44 UTC">2011-06-08 23:44 UTC</time></header>
<div class="forum-post-body">If I have the ADC block within my model and build it I see the following configuration bits:<br>
<pre><code>  AD1PCFGL = (0U);
  AD2PCFGL = (0U);
  AD1PCFGH = ((0U) &amp; 65535);
<wbr>
  /* S-Function "dsPIC_ADC" initialization Block: &lt;Root&gt;/ADC Input */
  /* Initialise ADC converter */
  /* 0 mean each 1 conversion */
#define NoSamplesADC                   0
#define ADCSval                        12
#define SAMCval                        (1 &lt;&lt; 8)
#define OutFormatBitsval               (0 &lt;&lt; 8)
#define VoltRef                        (0 &lt;&lt; 13)
<wbr>
  /* Use internal counter Trigger, continuous simulatenous sampling */
  AD1CON1 = 0x0004 | (7 &lt;&lt; 5) | (0 &lt;&lt; 10)| OutFormatBitsval;
  AD1CON2 = 0x0400 | (NoSamplesADC &lt;&lt; 2) | VoltRef;
  AD1CSSL = (1 &amp; 65535);
  AD1CON3 = (ADCSval | SAMCval) &amp; 0xff7f;
  AD1CHS0 = 0x0000;
  IPC2 = (IPC2 | (6 &lt;&lt; 12));           /*Interrupt Priority : 6*/
  _AD1IF = 0;
<wbr>
  /* We set _ADIE = 1 in the main file if necessary*/
  /* Clear Off Any Interrupt Due To Configuration */
  /* Turn on ADC Module */
  AD1CON1bits.ADON= 1;</code></pre><br>
<br>
The first 3 lines configure the AN pins to be used by the ADC or to by used as GPIO pins or be used for other peripherals. Why are these all being set to 0? Especially why is AD2 being configured as ADC inputs? Looking at the AD1CSSL only pin AN0 is actually being read, so why are the other pins being configured? Really I would expect only expect AD1PCFGH and AD1PCFGL set to 0xFFFF and 0xFFFE respectively in order to enable just AN0.<br>
<br>
<br>
<br>
I'm using the Explorer 16 board with the dsPIC33fJ256GP710 onboard and was trying to diagnose why most of my AN* pins were sitting at 3.7V (at least pins AN0-AN4, AN8-10) which is when I ran into this. I know that RB15 is at least one of the pins causing this increased voltage as it's connected to the LCD on the e16 board. But this isn't the real issue as none of this should be a problem if the pins are correctly configured.</div>
</article>

<article class="forum-post" id="p1601">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-09 16:04 UTC">2011-06-09 16:04 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
I'll respond from what I remember:<br>
<br>
Pin at startup are all configured to use ADC. You must change the default configuration if you want a digital I/O. ADC configuration for unused pin might be better (maybe, due to their high impedence)<br>
<br>
Thus, this is how the blockset does also: If one pin is used as a digital one, its corresponding ADC configuration is removed, but only on this pin. Thus all others PIN is still configure to ADC peripheral.<br>
<br>
<br>
<br>
This is why most unused PIN are still configured as an ADC input.<br>
<br>
<br>
<br>
Please let me know if this behavior is causing trouble. Would you prefer to have unused pin configured a digital input? Is there any reason for this ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1602">
<header><strong>bmairs</strong><time datetime="2011-06-09 16:22 UTC">2011-06-09 16:22 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">Yes I believe the default status for a pin should be for it to be a Digital I/O, which really just means NOT being used as an ADC pin. If I don't select an ANx pin to read from, why should it set that pin to be an ADC pin? Was there a reason for this design originally?<br>
<br>
<br>
<br>
I believe that if a pin is set to be used by the ADC, it can't be used by any other peripheral. So if I manually configure any of the other pins through my own custom code with a C-function block, that pin may be configured by your ADC block anyways and then I wouldn't be able to use it. That's clearly a conflict that shouldn't happen.</div>
</article>

<article class="forum-post" id="p1628">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-27 22:53 UTC">2011-06-27 22:53 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : bmairs</header>Was there a reason for this design originally?</blockquote>High impedance and low current leakage I guess ?<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : bmairs</header>That's clearly a conflict that shouldn't happen</blockquote>That make sens. What about adding a block just to be able to configure unused pin as either a digital input or ouptut ? Thus, you might then configure any peripheral you wwish without modifying either TRIS nor ADC config registers.</div>
</article>

<article class="forum-post" id="p1637">
<header><strong>bmairs</strong><time datetime="2011-07-11 19:13 UTC">2011-07-11 19:13 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>That makes sense. What about adding a block just to be able to configure unused pin as either a digital input or ouptut ? Thus, you might then configure any peripheral you wish without modifying either TRIS nor ADC config registers.</blockquote><br>
<br>
Yeah, I believe that's how it should be. So this would mean that the ADxPCFGx registers should default to all 1s with only pins needing the ADC input to be set to a 0. I also don't think that the registers need to be configured unless you're specifically mapping the pins to be 0. My code should only need to set bit 0 in AD1PCFGL to 0, so I don't think it needs to configure the other two registers, AD2PCFGL and AD1PCFGH.</div>
</article>

<article class="forum-post" id="p1642">
<header><strong>bmairs</strong><time datetime="2011-07-20 00:09 UTC">2011-07-20 00:09 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">So here's an additional model that exposes the problem also. In this model I am merely attempting to read the temperature value from the TC1047 chip that is onboard the Explorer16. If I use your ADC code, I get values that are almost exactly 1V higher than they should should. I should note that I also have nothing else besides the PICkit2 connected while performing these tests. Removing this, however, did not affect my readings. If I fix the ADCHS configuration section to the following, then everything works as expected.<br>
<pre><code>AD1PCFGL = 0xFFEF;
AD2PCFGL = 0xFFFF;
AD1PCFGH = 0xFFFF;</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/429-temp.mdl">Pièce jointe : temp.mdl</a></p>
</article>

<article class="forum-post" id="p1660">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-18 01:17 UTC">2011-08-18 01:17 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
I tested your model reading the temperature on my Explorer 16 board endowed with a 33fj256GP710 PIM module.<br>
<br>
<br>
<br>
I'll use degree °C  instead of fahrenheit<br>
<br>
Thus your formulae : ((ADC * 3.3/1023-0.5)/.01)*9/5+32<br>
<br>
turn into<br>
<br>
( ADC * 3.3/1023*100 ) - 50<br>
<br>
I get here a correct reading of the temperature : 30.8°C (it's warm here today). I get about 1°C difference with TX35DTH-IT (home temperature measurement system). Thus result seems correct.<br>
<br>
<br>
<br>
Looking at raw ADC converted value, I read on the dsPIC ADC 254 that should correspond to 254*3.3/1023 = 0.82V<br>
<br>
Measurement with my <a href="http://www.jpoutillage.com/descriptif/730250.html">voltmetre</a> between board GND and TC1047 sensor gives 0.84V. Thus results seems correct.<br>
<br>
<br>
<br>
blockset code for ADCHS register is:<br>
<pre><code>  AD1PCFGL = (0U);
  AD2PCFGL = (0U);
  AD1PCFGH = ((128U) &amp; 65535);</code></pre><br>
All pin configured as ADC input (high impedance, no pull-up) except AN7 which output a blinking led.<br>
<br>
<br>
<br>
I tested the configuration you propose:<br>
<pre><code>AD1PCFGL = 0xFFEF;
AD2PCFGL = 0xFFFF;
AD1PCFGH = 0xFFFF;</code></pre><br>
pin RB4 is properly configured as ADC input throuth bit 4 of AD1PCFGL.<br>
<br>
<br>
<br>
On the Explorer 16 board, I get same results (corrects).<br>
<br>
<br>
<br>
I've been using Explorer 16 with Real ICE connected all time and with a serial cable connecting also Explorer 16 to the PC at all time.<br>
<br>
<br>
<br>
The results you get seems weird. Could you provide more details about your material ? Have you been able to test on differents chips / board ? are you using a 33fj256GP710<strong>a</strong> chip ? (I only have one board and one chip)<br>
<br>
<br>
<br>
I am still convinced that unused pin should remains configured as ADC input for power consumption purpose (as is the default configuration). I would be pleased to get your feedback on this.<br>
<br>
Anyway, I will try to add a block to make you able to force specific pin as being digital input or output for your C function call functions.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/436-temp.mdl">Pièce jointe : temp.mdl</a></p>
</article>

<article class="forum-post" id="p1681">
<header><strong>bmairs</strong><time datetime="2011-09-06 18:03 UTC">2011-09-06 18:03 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">So regarding the weird voltages I'm seeing, that's most like a board issue, but I'm not willing to debug that right now.<br>
<br>
<br>
<br>
So I've reread Section 16: Analog-to-Digital Converter of the dsPIC manual and it does appear that the pins should default to ADC input so that the digital input buffers can be disabled to save power.<br>
<br>
<br>
<br>
You mention adding an additional block that can specify each ADC pin as an input or output. I'm not certain that's actually necessary given that my situation is very unique. I do know that one of my labmates was trying to do some work with a quadrature encoder library. This entailed him having to create an init function that specifically set those pins. I don't really see that being a problem though as he already needed to have an init function for the rest of the code.<br>
<br>
<br>
<br>
So considering everything, I think this issue can just be closed.</div>
</article>

<article class="forum-post" id="p1682">
<header><strong>LubinKerhuel</strong><time datetime="2011-09-06 20:48 UTC">2011-09-06 20:48 UTC</time></header>
<h3>Re: ADC block sets configures all pins to the ADC</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
I did not give feedback yet, however changes are already done, (will be published in version following v3.6).<br>
<br>
I added in the C function Call the Pins Configuration tab which allows to set up any pin which might be used in the C function as a digital I/O or an analog Input.<br>
<br>
<br>
<br>
If for any reason you want to set few pins as input/output without using C function call, you might still use this C function call block, without defining any function call...<br>
<br>
<br>
<br>
Hoping it will help for your design ;-)<br>
<br>
<br>
<br>
Lubin</div>
</article>

