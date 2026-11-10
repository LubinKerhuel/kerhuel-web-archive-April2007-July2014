---
title: "Modifying source file TinyBld"
url: "/forum/topic/185/"
archiveKind: "topic"
---
# Modifying source file TinyBld

Forum : [General Remark and Questions](/forum/#forum-1)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p650">
<header><strong>crh</strong><time datetime="2009-01-05 08:11 UTC">2009-01-05 08:11 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Modifying source file TinyBld in relation with the masterblock.<br>
<br>
<br>
<br>
When I try to write the hex file (a simulink model build with Matlab) with TinyBld into a dspic30f4013 I get in the GUI the error: <br>
<br>
<br>
<br>
Connected to \\.\COM3 at 115200<br>
<br>
 Searching for PIC ...Not found, <br>
<br>
 ERROR!<br>
<br>
<br>
<br>
I really do not know the cause of this error. Till now I suppose it is coming from a wrong way of modifying the source file from the bootloader regarding frequencies and/or baud. <br>
<br>
<br>
<br>
I build  the bootloader with the following files in MPLAB:<br>
<br>
tinybld_ds4013.s (source: Tiny website) <br>
<br>
p30f4013.gld (source: latest C30 full version) <br>
<br>
p30f4013.inc (source: latest C30 full version) <br>
<br>
Furthermore, I write the produced hex file with PicKit2 into the dspic30f4013.  No problem so far. Then I try to write the hex file of the simulink model into the pic (with the max232, circuit TinyBld )  and get the error (see above).<br>
<br>
I know, I have to modify the s file: tinybld_ds4013.s with the parameters from the masterblock. I use exact the same parameters as in your website: compile your first model. <br>
<br>
10MHz quartz, no PLL etc.<br>
<br>
I tried several ways but till now without any succes.<br>
<br>
Somewhere in?<br>
<pre><code>;********************************************************************
;	Tiny Bootloader		dsPIC series		Size=100words
;	[adresse e-mail retirée]
;	http://www.etc.ugal.ro/cchiculita/software/picbootloader.htm
;********************************************************************
        .equ __30F4013, 1
        .include "p30f4013.inc"
<wbr>
	;config		__FOSC, CSW_FSCM_OFF &amp; HS;FRC &amp; FRC_PLL4
	; fedcba9876543210
	; 11   FOS   FPR//
;	config		__FOSC, 0xC302	;HS
	;config		__FOSC, 0xC703
;	config          __FWDT, WDT_OFF
;	config          __FBORPOR, PBOR_OFF &amp; MCLR_EN
;	config          __FGS, CODE_PROT_OFF
;check also ATIO (below)
<wbr>
;.equ Fcy, 5000000
;.equ baud, 19200
.equ Fcy, 7372800*4
.equ baud, 115200
.equ IdTypePIC, 0x75        ; 0x75 is also for 4011, 4012
.equ max_flash, 0x8000		;dsPIC max address
<wbr>
        .global __reset
<wbr>
	.section .nbss, "b"
buff:	.space 4
buffer:	.space 128+6
W99:	.space 2
<wbr>
;REGISTRY:
;W0	imediat, param nvmcon
;W1	Receive
;W2	SendL		need?
;W3	count rcv
;W4	memory buffer pointer
;W5	^
;W6	for
;W7	temp
;W8
;W9	Erase/Write Flag
;W10	delay1
;W11	delay2
;W12	EA Write 
;W13	crc
;W14	void(black hole)
;W15	stack
<wbr>
etc..</code></pre><br>
<br>
Regards, Casparus</div>
</article>

<article class="forum-post" id="p651">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-05 23:34 UTC">2009-01-05 23:34 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
Configuration for tinybld is sometimes fastidious.<br>
<br>
It's a long time I have not been doing it...<br>
<br>
<br>
<br>
One good method for debugging is to make the code to send data (using the SendL macro) in an infinite loop and to check with your oscillo :<br>
<br>
- UART Tx pin is alive!<br>
<br>
- With an oscilloscope or HyperTerminal (windows), bit rate is Ok<br>
<br>
<br>
<br>
As far as I remember, common problem comes from :<br>
<br>
- DsPIC configuration (Quartz configuration: check if it is HS, XT and PLL parameters...)<br>
<br>
- check that you use the correct dsPIC configuration set (problem with MPLAB interface...)<br>
<br>
- Check the UART baud ( it may be better to write as a literal value the baud) : <br>
<pre><code>        mov     #12, W0                               ; instead of #(((Fcy/baud) / 16) - 1), W0  
        mov     w0, U1BRG                           ;to 115200 Kbaud #(((7372800/115200) / 16) - 1)</code></pre><br>
<br>
I attached the file I usually use as is : (adapt it for 4013)<br>
<br>
Once configuration is done, bootloader will work forever...</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/170-tinybld_ds.s">Pièce jointe : tinybld_ds.s</a></p>
</article>

<article class="forum-post" id="p652">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-06 08:20 UTC">2009-01-06 08:20 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">I have this .hex file (tinybld software) for dsPIC 4013 :<br>
(Quartz at 10Mhz, no PLL used, UART configuration at 19200)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/172-tinybld_ds30f4013_10MHz_HS_19200.zip">Pièce jointe : tinybld_ds30f4013_10MHz_HS_19200.zip</a></p>
</article>

<article class="forum-post" id="p656">
<header><strong>crh</strong><time datetime="2009-01-07 08:38 UTC">2009-01-07 08:38 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Thank you very much for your provided hex file. <br>
<br>
I assume that this hex file is working well, but still I have a problem to connect with my device with the max232. <br>
<br>
I am so new in microcontrollers, that I even do not know if I wrote the hex file in a correct way to the device. <br>
<br>
Therefor, you can find a  screenprint of the GUI from Pickit2 and a screenprint from the max232 circuit.<br>
<br>
<br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/173-screenpickit_tinybld.gif">Pièce jointe : screenpickit_tinybld.gif</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/174-circuitmax232.gif">Pièce jointe : circuitmax232.gif</a></p>
</article>

<article class="forum-post" id="p657">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 09:13 UTC">2009-01-07 09:13 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">No problems due to Vista with the COM port ?</div>
</article>

<article class="forum-post" id="p668">
<header><strong>crh</strong><time datetime="2009-01-08 06:57 UTC">2009-01-08 06:57 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Yesterday evening I tried to discover if it was a Vista problem and checked it with my old laptop running under Windows XP. But a pity: the same errors.<br>
<br>
Still, I suppose it is more a hardware problem then a software problem. From the other hand, I have checked the circuitry a thousand times. <br>
<br>
For your information, because I am not 100% sure if it is alright:<br>
<br>
I connected: <br>
<br>
pin 11 (TX) of the max232 with pin 28 of the pic (pin layout see image from yesterday) and<br>
<br>
pin 12 (RX) of the max232 with pin 27 of the pic. <br>
<br>
I do not use an external crystal.<br>
<br>
In order to connect the max232 to my computer I use a Serial to USB Cable. But I wonder if I have to change some settings in my computer.<br>
<br>
<br>
<br>
Kind Regards, Casparus</div>
</article>

<article class="forum-post" id="p669">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-08 09:27 UTC">2009-01-08 09:27 UTC</time></header>
<h3>Re: Modifying source file TinyBld</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
I do not see errors on the Rx-Tx connections.<br>
<br>
Using USB to Serial converter is not a problem.<br>
<br>
<br>
<br>
To test your hardware, I would advise to create a simple schematic for you dsPIC with simulink, compile it and load it using your usual programmer (ICD2). You can use the windows HyperTerminal to check that you PC can transmit/receive data with the dsPIC through UART.<br>
<br>
<br>
<br>
Anyway, you may have a serious problem because you do not use quartz: dsPIC Internal RC oscillator is usually not precise enough (and may vary over time) for UART set-up, except if you use the microchip system to auto calibrates the UART (see UART doc, not supported in the blockset).<br>
<br>
Lubin</div>
</article>

