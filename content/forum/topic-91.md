---
title: "circuit interface between MATLAB and dsPIC?"
url: "/forum/topic/91/"
archiveKind: "topic"
---
# circuit interface between MATLAB and dsPIC?

Forum : [General Remark and Questions](/forum/#forum-1)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p242">
<header><strong>Kiara</strong><time datetime="2008-02-24 16:09 UTC">2008-02-24 16:09 UTC</time></header>
<div class="forum-post-body">hello sir,<br>
<br>
<br>
<br>
I have emailed you before asking about your work and my project (ref : Intan).<br>
<br>
<br>
<br>
I am very very new with dsPIC and I don't know much about dsPIC and would very much appreciate it if you could help me with all my questions, even though it is very basic.<br>
<br>
<br>
<br>
My question is, how do you connect from MATLAB to dsPIC? do you need to have a circuit interface or buffer between them? I am very puzzle to how am I connecting this both together.<br>
<br>
<br>
<br>
Thank you</div>
</article>

<article class="forum-post" id="p243">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-25 21:53 UTC">2008-02-25 21:53 UTC</time></header>
<h3>Re: circuit interface between MATLAB and dsPIC?</h3>
<div class="forum-post-body">Hi Kiara,<br>
<br>
<br>
<br>
Are you talking about <br>
<br>
- a connection to upload the .hex file into the dsPIC ?<br>
<br>
- a connection to get and plot data in real time through UART  and COM port on the computer ? (send data is also possible)</div>
</article>

<article class="forum-post" id="p298">
<header><strong>chukhivuitinh</strong><time datetime="2008-04-23 11:30 UTC">2008-04-23 11:30 UTC</time></header>
<h3>Re: circuit interface between MATLAB and dsPIC?</h3>
<div class="forum-post-body">a connection to upload the .hex file into the dsPIC ? &lt;&lt;&lt; use tiny bootloader with 5 pin MCLR ,VDD ,GND ,TX ,RX wright ?<br>
<br>
a connection to get and plot data in real time through UART and COM port on the computer ? &lt;&lt;&lt; ^_^  :?:  :?:  :?:</div>
</article>

<article class="forum-post" id="p301">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-24 22:15 UTC">2008-04-24 22:15 UTC</time></header>
<h3>Re: circuit interface between MATLAB and dsPIC?</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : chukhivuitinh</header>a connection to upload the .hex file into the dsPIC ? &lt;&lt;&lt; use tiny bootloader with 5 pin MCLR ,VDD ,GND ,TX ,RX right ?</blockquote><br>
<br>
:? More or less true: <br>
<br>
If you use a boot loader (like tinybld ; google it !) you need first to program your chip with the bootloader soft. To do so, you will have to buy a programmer (I2C, real ice or others...), or build yourself a programmer for PIC, many schematic are available on the web, some of them are very simple.<br>
<br>
<br>
<br>
Once the bootloader code is loaded into the chip, you will be able to load a program in the chip using the UART interface:   GND ,Tx, Rx + the chip must be running.<br>
<br>
Programming the chip will not erase the bootloader, check how the used bootloader you use is working...<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : chukhivuitinh</header>a connection to get and plot data in real time through UART and COM port on the computer</blockquote><br>
This will use the same UART interface as the one used by the bootloader : GND ,Tx, Rx + the chip must be running.<br>
<br>
<br>
<br>
Note however that some bootloader may use others interface than the UART.<br>
<br>
<br>
<br>
Important: for the UART interface, you need to translate the signal level: COM port of your PC signals are between +-15 or +-3V. The COM port of the chip is between [0-Vdd] with vdd usually fixed in [3.3V ; 5V]<br>
<br>
The "traditional" electronic part to use is max232, but more recent component is even easier: look at DS276 component from maxim.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1065">
<header><strong>onuruygur</strong><time datetime="2010-02-02 15:58 UTC">2010-02-02 15:58 UTC</time></header>
<h3>Re: circuit interface between MATLAB and dsPIC?</h3>
<div class="forum-post-body"><strong>Hello all,<br>
<br>
<br>
<br>
I am not sure that my question is related with this topic but didn't want to create an improper new subject,<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
I just received my lite FLEX dspic board. I have MPLAB 8.3 installed. I also have bought a ICD2.<br>
<br>
<br>
<br>
I have prepared a .hex file in SIMULINK, imported it to MPLAB. After I connect &amp; installed ICD2 in MPLAB it warned me to upgrade the ICD2 operating system to DSPIC33FJ256MC710 (I had choosed it first from the tools&gt;select device). It succesfully upgraded the operating system.<br>
<br>
<br>
<br>
Here is some strange starts:</strong> :shock: <br>
<br>
<strong>When i click program form the programmer menu it firstly:</strong><br>
<br>
<br>
<br>
"ICDWarn0052 : ICD2 cannot validate a target device..."<br>
<br>
<br>
<br>
<strong>and when i click OK:</strong><br>
<br>
"ICDWarn0064: The requested operation will destroy the Boot segment already defined on the target.  You must explicitly specify that ICD is allowed to do this on the Secure Segment tab of the MPLAB ICD 2 Settings Page. "<br>
<br>
<br>
<br>
<strong>Ok there are settings on secure segment tab but i am not sure about overwriting the boot segment.<br>
<br>
<br>
<br>
Which is the right segment for MPLAB / ICD2 &amp; Lite Flex board programming if you just want to program a blinking led example?<br>
<br>
<br>
<br>
Regards,</strong></div>
</article>

<article class="forum-post" id="p1066">
<header><strong>onuruygur</strong><time datetime="2010-02-02 17:21 UTC">2010-02-02 17:21 UTC</time></header>
<h3>Re: circuit interface between MATLAB and dsPIC?</h3>
<div class="forum-post-body">Ok people i coudn't wait anymore and click FULL PROGRAMMING after i read:<br>
<br>
<br>
<br>
<a href="http://209.85.229.132/search?q=cache:ygVVEASi7cQJ:www.pic16.com/wzcapi/mcd2_new_lise.htm+%22Segment+Programming%22+dspic&amp;cd=2&amp;hl=tr&amp;ct=clnk&amp;gl=tr">http://209.85.229.132/search?q=cache:yg ... clnk&amp;gl=tr</a><br>
<br>
<br>
<br>
RESULT : It works!  My led is now blinking... :lol:<br>
<br>
<br>
<br>
Now i can turn to my control model... <br>
<br>
<br>
<br>
Thnxs,</div>
</article>

