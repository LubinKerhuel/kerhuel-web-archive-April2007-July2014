---
title: "UART232 Configuration Problem"
url: "/forum/topic/275/"
archiveKind: "topic"
---
# UART232 Configuration Problem

Forum : [General Remark and Questions](/forum/#forum-1)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1075">
<header><strong>onuruygur</strong><time datetime="2010-02-08 18:22 UTC">2010-02-08 18:22 UTC</time></header>
<div class="forum-post-body">Hi all,<br>
<br>
<br>
<br>
I have FLEX Lite board and i have prepared the model given at the attachment. It is a very basic model which blinks the led and sends "A" to serial port.<br>
<br>
<br>
<br>
Here is the problem: Led blinks but UART 1 doesn't send "A" to hyper terminal... <br>
<br>
<br>
<br>
I suprisely discovered that it transmits when ICD2 is in programming progress (all the "A"'s on the hyper terminal are received during the programming proccess from the board when I change the code character is changing). So i think that it is not hardware related. May be a configuration error?<br>
<br>
<br>
<br>
Anybody have idea? Or Anybody who can share me FLEX Board related master configuration?  :roll: <br>
<br>
<br>
<br>
Regards,</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/290-untitled.JPG">Pièce jointe : untitled.JPG</a></p>
</article>

<article class="forum-post" id="p1076">
<header><strong>Bobes</strong><time datetime="2010-02-09 01:46 UTC">2010-02-09 01:46 UTC</time></header>
<h3>Re: UART232 Configuration Problem</h3>
<div class="forum-post-body">Hello, can you be more specific about the connection? Is the UART connected via USB? or ie via MAX3232 and Rx Tx pins?<br>
<br>
I am not really an expert, but I would think it is more likely wiring problem. UART should not be sending anything during programming. <br>
<br>
If you are using UART Rx and Tx, there should not be any signal done by the ICD, as it is connected to one of the PGED/PGEC pairs, and those are not re-mappable with UART. I am not sure how is it with USB, but as you are using UART peripheral it should be still somehow wired.<br>
<br>
Try re-checking the wiring connection. Hope this helps. Good luck.<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1077">
<header><strong>onuruygur</strong><time datetime="2010-02-09 08:04 UTC">2010-02-09 08:04 UTC</time></header>
<h3>Re: UART232 Configuration Problem</h3>
<div class="forum-post-body">Hello Josef,<br>
<br>
<br>
<br>
Thank you for your reply. <br>
<br>
<br>
<br>
Yes, I am using MAX3232 for interfacing UART1 and UART2 for my FLEX board. After your reply, with the given model below I have seperated the prototype board (so there is no max3232) and have a check with a digital oscilloscope on UART 1 TX and UART2 TX (directly at the dspic pins) but there is no meaningful signal out on these pins.  :? <br>
<br>
<br>
<br>
Led blinks but something is wrong with UART....</div>
</article>

<article class="forum-post" id="p1078">
<header><strong>Bobes</strong><time datetime="2010-02-09 14:56 UTC">2010-02-09 14:56 UTC</time></header>
<h3>Re: UART232 Configuration Problem</h3>
<div class="forum-post-body">OK.. i think I may see the problem: have you mapped the peripheral properly? (PIN mapping block?)<br>
<br>
please attach the mdl file</div>
</article>

<article class="forum-post" id="p1082">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-11 16:22 UTC">2010-02-11 16:22 UTC</time></header>
<h3>Re: UART232 Configuration Problem</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I got another explanation : <br>
<br>
<br>
<br>
UART block is <strong>pink </strong>: that mean that block has a sampling time of inf : this block is executed only once at model start.<br>
<br>
<br>
<br>
Solution : sampling time of the <strong>UART block</strong> (different from UART speed) is <strong>inherited </strong>from the constant block. Thus, <br>
<br>
* open the constant block<br>
<br>
* set its sampling time to someghint like .01 (or the sampling time of your model).<br>
<br>
<br>
<br>
it should works properly<br>
<br>
(I think there is no the mapping option on the microchip dspic used on the flex lite board)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1086">
<header><strong>onuruygur</strong><time datetime="2010-02-21 16:53 UTC">2010-02-21 16:53 UTC</time></header>
<h3>Re: UART232 Configuration Problem</h3>
<div class="forum-post-body">Hi and thank you for all,<br>
<br>
<br>
<br>
Yes Lubin you were right (not suprise)   :)  ...<br>
<br>
<br>
<br>
And yes mapping is not an option for FLEX boards.<br>
<br>
<br>
<br>
On my works, what i see is; i am not able to use standart xpc target s-functions such as "FIFO HDRS Read" or basic "ASCII Decode" with DSPIC target. I was using these functions for decoding any sensor on RS232 with xpctarget pc's. I could'nt find a FIFO which converts discrete bytes (as "1", "2"...) to vectors (as "123") received from UART RX block.<br>
<br>
<br>
<br>
What do you advice me for reading a RS232 packet like "A 123 456 789 910 123 456 789 Z" (I am not able to use C Call yet...) <br>
<br>
<br>
<br>
At the end i need:<br>
<br>
DATA1= 123<br>
<br>
DATA2= 456<br>
<br>
DATA3= 789...<br>
<br>
<br>
<br>
Best regards,</div>
</article>

