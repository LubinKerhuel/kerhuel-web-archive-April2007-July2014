---
title: "PIC32 SPI"
url: "/forum/topic/345/"
archiveKind: "topic"
---
# PIC32 SPI

Forum : [General Remark and Questions](/forum/#forum-1)

8 message(s) · archive en lecture seule

<article class="forum-post" id="p1430">
<header><strong>konsgn</strong><time datetime="2011-01-05 15:01 UTC">2011-01-05 15:01 UTC</time></header>
<div class="forum-post-body">Greetings,<br>
<br>
<br>
<br>
I was wondering what the progress was on getting SPI functionality for the PIC32MX line? <br>
<br>
What about using the C function call to call working C32 compiler code that would handle the SPI communication?<br>
<br>
Are there any workarounds for getting SPI working?<br>
<br>
<br>
<br>
Thank you,<br>
<br>
Konsgn</div>
</article>

<article class="forum-post" id="p1439">
<header><strong>resodad</strong><time datetime="2011-01-12 16:33 UTC">2011-01-12 16:33 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
I am working with Konsgn to implement a SD card data logger on Cerebot 32MX4 (PIC32MX460F512L). I ran Microchip's example C program "MDD File System-SD Card" successfully. The setup uses SPI to read / write.<br>
<br>
<br>
<br>
Now to port to Simulink. We would like to have a Simulink block to write data over SPI to the SD card. <br>
<br>
<br>
<br>
I saw the QEI C-function block example on the forum.<br>
<br>
Would it be possible for Konsgn and me to write a c-function block to do SPI? <br>
<br>
Is there a better way?<br>
<br>
<br>
<br>
Would you consider developing and publishing the block? <br>
<br>
<br>
<br>
Cheers,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1440">
<header><strong>matgraci</strong><time datetime="2011-01-18 09:15 UTC">2011-01-18 09:15 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Hi.<br>
<br>
<br>
<br>
Does this mean that SPI functionality is not supported for PIC32 uCs with those blocksets?! I can't remember reading this anywhere when buying those blocksets for my PIC32MX360F512l uC!  :?: <br>
<br>
I noticed that when i insert the SPI Configuration Block that the Fsck can't be counted or something like that. Never figured that this blockset is not supported for that uC. I even noticed that I couldn't compile when using SPI2 even though SPI2 port is available on my uC.</div>
</article>

<article class="forum-post" id="p1441">
<header><strong>matgraci</strong><time datetime="2011-01-18 22:16 UTC">2011-01-18 22:16 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">I just wrote C function that is supposed to write data to SPI port. There is one more function that sets SPI configuration. I set my model so that config function is called only once. <br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;void configSPI() {
	static int first_pass = 1;
	int rData;
	if (first_pass) {
		first_pass = 0;
		IEC0CLR=0x03800000; // disable all interrupts
		SPI1CON = 0; // Stops and resets the SPI1.
		rData=SPI1BUF; // clears the receive buffer
		IFS0CLR=0x03800000; // clear any existing event
		IPC5CLR=0x1f000000; // clear the priority
		IPC5SET=0x0d000000; // Set IPL=3, Subpriority 1
		IEC0SET=0x03800000; // Enable RX, TX and Error interrupts
		SPI1BRG=0x1; // use FPB/4 clock frequency
		SPI1STATCLR=0x40; // clear the Overflow
		SPI1CON=0x8220; // SPI ON, 8 bits transfer, SMP=1, Master mode
		// from now on, the device is ready to transmit and receive data
	}
}
void sendSPI(char a) {
	IFS0CLR=0x03800000; // clear any existing event
	//rData=SPI1BUF; // clears the receive buffer
	SPI1BUF=a; // transmit an A character
}
void setport(){
	static int i=1;
        TRISD = 0;
	LATD = i;
	i = (i+1)%2;
}
</code></pre><br>
<br>
This works fine (since I manage to send and receive some data to my other uC), but the problem is that function for writing to SPI port is called only once, even thought it should be called every 0.5s. I added other C function that lights one LED every 0.5s. I put that LED function and sendSPI function in one enabled subsystem and set all SampleTime-s to -1. So if everything is alright then LED should blink every 0.5s and some data should be sent over SPI port every 0.5s. I'v done that only for debugging. But it didn't happen. LED lighted only once and only one char was transferred over SPI port. <br>
<br>
<br>
<br>
When I commented this line<br>
<pre><code>SPI1BUF=a</code></pre><br>
then LED started to blink. Why is that so?! Does anyone have any idea?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/369-dsPIC_32MX360F512L_Proba.mdl">Pièce jointe : dsPIC_32MX360F512L_Proba.mdl</a></p>
</article>

<article class="forum-post" id="p1450">
<header><strong>resodad</strong><time datetime="2011-01-23 15:19 UTC">2011-01-23 15:19 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Hi matgraci,<br>
<br>
<br>
<br>
Thanks for posting, I am trying your model. I am new to this... where did you save your c code? what did you name it? how did you connect it to the model?<br>
<br>
This is what I tried: Saved your code as SPIcode.c in the build directory, and entered the name SPIcode.c in the list of additional source files on the custom code page of the Real-Time Workshop page. The build produces a generic error.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : matgraci</header>Hi.<br>
<br>
<br>
<br>
Does this mean that SPI functionality is not supported for PIC32 uCs with those blocksets?! I can't remember reading this anywhere when buying those blocksets for my PIC32MX360F512l uC!  :?: <br>
</blockquote><br>
<br>
See the note: " * PIC 32F<br>
<br>
    SPI function not suported yet;" under the list of supported chips on page: <a href="/wiki/simulink-embedded-target-for-pic/">http://archive.kerhuel.eu/wiki/Simulink_-_E ... et_for_PIC</a>.</div>
</article>

<article class="forum-post" id="p1452">
<header><strong>matgraci</strong><time datetime="2011-01-24 13:19 UTC">2011-01-24 13:19 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Sorry, but i can't include the whole c file that I used because it contains some of the data and other things that I can't share with all of you. I think that you can't compile it because you did not include "pic32mxxx.h" in your .c file, or whatever is the the name of the file that contains names of all of the registers used for addressing ports and other peripherals.<br>
<br>
<br>
<br>
Regarding my problem... When i changed from SPI1 to SPI2 some things started to work, just that I was not able to receive any data, only to send.</div>
</article>

<article class="forum-post" id="p1559">
<header><strong>konsgn</strong><time datetime="2011-04-27 20:01 UTC">2011-04-27 20:01 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
  I've been working a lot on getting SD card capability for logging data in Simulink. I have placed all the relevant headers and C files provided by Microchips Application Solution MDD file system in the working directory of the model. I have also removed any nested folders.<br>
<br>
<br>
<br>
 The problem I have noticed is that within the code provided by Microchip, they make use of delays that are often over 1ms long. Since we are running on a 1ms timestep on the PIC32MX460F512L, I would like to keep this timestep the same, but temporarily change the running of certain subfunctions to free-running mode.  Would this be possible or should I be looking to modify the Delays?<br>
<br>
<br>
<br>
I have posted a .zip with all the relevant files in case that helps.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/409-SD%20Datalogging.zip">Pièce jointe : SD Datalogging.zip</a></p>
</article>

<article class="forum-post" id="p1571">
<header><strong>resodad</strong><time datetime="2011-05-11 14:07 UTC">2011-05-11 14:07 UTC</time></header>
<h3>Re: PIC32 SPI</h3>
<div class="forum-post-body">Lubin and all,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : konsgn</header><br>
  I've been working a lot on getting SD card capability for logging data ...<br>
<br>
I have posted a .zip with all the relevant files in case that helps.</blockquote><br>
please comment on the method konsgn uses to write to an SD card. Is there a better way?<br>
<br>
John</div>
</article>

