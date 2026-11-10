---
title: "SPI EEPROM Record and Playback on Explorer 16"
url: "/forum/topic/297/"
archiveKind: "topic"
---
# SPI EEPROM Record and Playback on Explorer 16

Forum : [dsPIC Peripherals](/forum/#forum-9)

18 message(s) · archive en lecture seule

<article class="forum-post" id="p1177">
<header><strong>resodad</strong><time datetime="2010-04-23 01:04 UTC">2010-04-23 01:04 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
I would like to record a PWM signals and reproduce ("play back") later. These are radio control signals: 20ms fixed period, high time varies from 0.5 to 2.5 ms. My proposal is to record the high times to EEPROM on board the Explorer 16. This EEPROM is already connected to SPI2. A toggle switch e.g. B2 will control whether I am resording or playing back.<br>
<br>
<br>
<br>
Questions:<br>
<br>
1. Can I use eeprom in this way to record a list of numbers and then go back to the beginning of the list and read them back?<br>
<br>
2. Should I use interrupt SPI block? see the attachment SPIwork1<br>
<br>
2. Maybe I can do this without interrupt, see attachment SPIwork2<br>
<br>
3 simulink gives error:<br>
<br>
Error building Real-Time Workshop target for block diagram 'SPIwork2'. MATLAB error message: The following error occurred processing the System Target File '': SubSystem block does not have a parameter named 'RTWGenSettings'.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/327-SPIwork1.mdl">Pièce jointe : SPIwork1.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/328-SPIwork2.mdl">Pièce jointe : SPIwork2.mdl</a></p>
</article>

<article class="forum-post" id="p1183">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-26 00:56 UTC">2010-04-26 00:56 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>1. Can I use eeprom in this way to record a list of numbers and then go back to the beginning of the list and read them back?</blockquote><br>
Should be Ok.<br>
<br>
<br>
<br>
2)3)4)<br>
<br>
You can't have two interrupt driven SPI blocks, except perhaps very special case (here is not the case). Even it ir was working, this would not be good for what's you are doing (as interrupt SPI block may be executed several times within one time-step).<br>
<br>
<br>
<br>
Thus, you should the other SPI block.<br>
<br>
the model SPIwork2 is compiling on my system.<br>
<br>
<br>
<br>
<br>
<br>
Anyway, I get another error : Play back subsystem need a uint8 to uint16 converter between SPI and OC blocks.<br>
<br>
Idem in Record sybsystem between IC and SPI blocks.<br>
<br>
<br>
<br>
Could you provide details about your error (copy all compiling message, blockset version, matlab version, any useful information to make me able to reproduce the problem)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1189">
<header><strong>resodad</strong><time datetime="2010-04-27 21:12 UTC">2010-04-27 21:12 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback</h3>
<div class="forum-post-body">Thanks Lubin, Your info about interrupts helped me along.<br>
<br>
There were several problems with the previously posted model SPIwork2.<br>
<br>
I simplified to make sure I can do an easy task first.<br>
<br>
<br>
<br>
Easy Task: Measure PWM input using IC2 and immediately duplicate it on OC2.<br>
<br>
This is running--output tracks input perfectly! Well, there is latency, but otherwise perfect.<br>
<br>
See the model ic_to_oc_v2.mdl and the description IC to OC.doc in the first attachment.<br>
<br>
Question: Can I specify which timer to use for a peripheral?<br>
<br>
e.g. I want to can I use timer 3 for both IC2 and OC2.<br>
<br>
Question: Can I specify a 32-bit combined timer 2/3?<br>
<br>
<br>
<br>
Difficult Task: write a stream to EEPROM over SPI<br>
<br>
See attached model SPIwork3.mdl<br>
<br>
I have LED indicators on Explorer16 for record and playback, these work OK<br>
<br>
In record mode the IC2 data looks correct viewed over UART<br>
<br>
In playback mode, UART shows nothing but zeros<br>
<br>
I am  not sure if this is writing to SPI bus:<br>
<br>
The /CS pin on the EEPROM is constantly low, and a clock signal is present, but I do not see any data signals.<br>
<br>
<br>
<br>
As always thanks so much for your expert help.<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/333-SPIwork3.zip">Pièce jointe : SPIwork3.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/332-inputCapture_to_OutputCompare.zip">Pièce jointe : inputCapture_to_OutputCompare.zip</a></p>
</article>

<article class="forum-post" id="p1197">
<header><strong>Ender</strong><time datetime="2010-04-28 18:46 UTC">2010-04-28 18:46 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
In the SPI Config block, you have to enable the output "SDO enable", with the scope check the data on the pin 5 call SI of U5, or on the pin 12 of your Dspic it should be work now...<br>
<br>
If it doesn't work update here another model more simple, with just the enable on D12 and to send a constant on the SPI output. Give us your Mathlab and blockset version please.<br>
<br>
<br>
<br>
Are you building something like a universal remote control ?<br>
<br>
<br>
<br>
Lubin what the utility to disable the SDO ?<br>
<br>
<br>
<br>
Thierry</div>
</article>

<article class="forum-post" id="p1198">
<header><strong>resodad</strong><time datetime="2010-04-28 19:43 UTC">2010-04-28 19:43 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Hello Thierry,<br>
<br>
I will do that. Also, I had a look at 24LC256 data sheet.I see that I have to send EEPROM  WREN and WRITE commands and then address before I write to EEPROM, so I have some work to do before I post.<br>
<br>
Thanks,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1199">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-28 21:53 UTC">2010-04-28 21:53 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Ender</header>Lubin what the utility to disable the SDO ?</blockquote><br>
<br>
Well, if you don't use it ? Isn't there some chip that are not waiting anything before sending data (thus receive on SDI) ? Perhaps to read data on a bus ?<br>
<br>
Anyway, this option is present on microchip microcontrôller, I just give acces to it on the blockset. I never had use of it yet !<br>
<br>
<br>
<br>
Jon, we'll wait your next post...<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1201">
<header><strong>resodad</strong><time datetime="2010-04-28 22:11 UTC">2010-04-28 22:11 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Lubin, Thierry:<br>
<blockquote><header class="quote-author">Citation : Ender</header>Are you building something like a universal remote control ?</blockquote><br>
No, it's not a universal remote; I am trying to record and reproduce radio controlled car signal wave forms.<br>
<blockquote><header class="quote-author">Citation : Ender</header>you have to enable the output "SDO enable"</blockquote><br>
What is  "SDO enable" for?<br>
<br>
Here is my attempt at writing a single value to address 21 on the EEPROM and reading back. It reports only zeros. see attachment.<br>
<br>
Pin 5 of U5 on the Explorer16 DOES show the data. I can see the pattern of the data 1234 decimal, 10011010010 binary, as well as the WREN and WRITE commands and the address on oscilloscope.<br>
<br>
During attempted read operation, read request and address appear on SI pin, but NOTHING on SO pin.<br>
<br>
Matlab is R2009BSP1<br>
<br>
blockset is  Version 3.1a   16-Mar-2010  For Matlab 7.8    R2009a<br>
<br>
Lubin should I upgrade blockset?<br>
<br>
Cheers,<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/335-SPIwriteRead.zip">Pièce jointe : SPIwriteRead.zip</a></p>
</article>

<article class="forum-post" id="p1202">
<header><strong>Ender</strong><time datetime="2010-04-29 01:02 UTC">2010-04-29 01:02 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header><blockquote><header class="quote-author">Citation : Ender</header>Lubin what the utility to disable the SDO ?</blockquote><br>
<br>
Well, if you don't use it ?<br>
<br>
<br>
<br>
Lubin</blockquote><br>
<br>
Ho yeh, I'm silly! :lol: <br>
<br>
I Have used the SPI one time, 8 years ago, and for me it was a big shift register so simple that you better have to loop the data from in to out all the time anyway you have nothing to write when you are reading the register.<br>
<br>
And I never see SPI peripherals using just the enable and clock to return data on their SO, but you right and the PIC could be in slave so just to use his SI to be controled as a sink. Thanks.</div>
</article>

<article class="forum-post" id="p1204">
<header><strong>Ender</strong><time datetime="2010-04-29 03:32 UTC">2010-04-29 03:32 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">John, I didn't try, just take a peek on the datasheet :<br>
<br>
<br>
<br>
The Read and Write instructions have to be on 8 bits, so I guess you have to change all your model to use the 'SPI config' as 8 bits data size.<br>
<br>
<br>
<br>
Doesn't matter but I think you do not need a WRDI at the end of a write sequence.</div>
</article>

<article class="forum-post" id="p1206">
<header><strong>resodad</strong><time datetime="2010-04-29 19:26 UTC">2010-04-29 19:26 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Lubin and all,<br>
<br>
I made that change Thierry--8-bit addresses. Also I made the data 8 bits and the SPI data setting 8 bits instead of 16.<br>
<br>
It is still not working. I will attach scope traces showing /CS, CLOCK, and both DATA lines. These traces look good to me: from bottom to top: /CS, DATA out, DATA in, CLOCK. There is no data out.<br>
<br>
What is wrong?<br>
<br>
<br>
<br>
I will compare to signals produced by working C program (program also atached).<br>
<br>
Question: is there an easy way to handle 16-bit to 2x 8-bit and vice versa? I handled it one way to send UART TX, but am wondering if there is a simpler way.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/338-SPIwriteRead_v2.zip">Pièce jointe : SPIwriteRead_v2.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/339-SPI%20oscilloscope.zip">Pièce jointe : SPI oscilloscope.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/340-SPI%20Master%20EEPROM%20dcPIC.zip">Pièce jointe : SPI Master EEPROM dcPIC.zip</a></p>
</article>

<article class="forum-post" id="p1207">
<header><strong>resodad</strong><time datetime="2010-04-29 19:59 UTC">2010-04-29 19:59 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">OH!<br>
<br>
I changed commands to 8 bits--right<br>
<br>
but also:<br>
<br>
changed address to 8 bits :WRONG!<br>
<br>
<br>
<br>
Stand By<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1209">
<header><strong>resodad</strong><time datetime="2010-04-29 20:26 UTC">2010-04-29 20:26 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Still not working :( <br>
<br>
Latest model attached.<br>
<br>
john</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/341-SPIwriteRead_v3.zip">Pièce jointe : SPIwriteRead_v3.zip</a></p>
</article>

<article class="forum-post" id="p1210">
<header><strong>Ender</strong><time datetime="2010-04-29 22:59 UTC">2010-04-29 22:59 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">I didn't check everything but the principle seem now good for me. Good idea to add the traces 8).<br>
<br>
<br>
<br>
The clock edges are rising while the data are changing too. The memory chip take the data on the rising edge clock no on the state.<br>
<br>
Inside the Lubin SPI config block, it seem for me you can change the clock to be active on a state Low or High state and sample on midle of the data... it should be fall in work...</div>
</article>

<article class="forum-post" id="p1211">
<header><strong>Ender</strong><time datetime="2010-04-29 23:10 UTC">2010-04-29 23:10 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Lubin, :idea: <br>
<br>
<br>
<br>
On future versions, you maybe change the form inside the Configure SPI mask by:<br>
<br>
- the currently 'Sample Phase' by 'clock synchronization' with 'edge' and 'state' as choices.<br>
<br>
- and Clock Active with 'State high or Rising' and 'State Low or Falling' as choices.</div>
</article>

<article class="forum-post" id="p1213">
<header><strong>resodad</strong><time datetime="2010-04-30 15:11 UTC">2010-04-30 15:11 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Thierry thanks for the help.<br>
<br>
Program is working to write then read from EEPROM. See atachments.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/342-Write_Read_EEPROM.zip">Pièce jointe : Write_Read_EEPROM.zip</a></p>
</article>

<article class="forum-post" id="p1214">
<header><strong>Ender</strong><time datetime="2010-04-30 17:43 UTC">2010-04-30 17:43 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">:D <br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>Lubin and all,<br>
<br>
Question: is there an easy way to handle 16-bit to 2x 8-bit and vice versa? I handled it one way to send UART TX, but am wondering if there is a simpler way.</blockquote><br>
<br>
I didn't see which method you are using but I would use the Matlab instruction : 'Bitsliceget' and 'Bitconcat', and all instructions like 'bitshift'  too, which are close of C code equilalent instructions.</div>
</article>

<article class="forum-post" id="p1215">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-30 18:19 UTC">2010-04-30 18:19 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Hi Jon, Thierry<br>
<br>
<br>
<br>
Jon, good to see EEPROM read-write working on Explorer 16. I may place a link to this demo from one of the wiki page if you're Ok (for example on the <a href="/wiki/category/example/">example page</a>)<br>
<br>
<br>
<br>
Thierry,<br>
<br>
With simulink, you can handle conversion 8 to 16 bits using shift blocks and lobgical operator. Even if it is not much practical to do it with theses blocks, it is compiled in a quite pretty way.)<br>
<br>
You may also use the <strong>embedded </strong>matlab function block to make your conversion.<br>
<br>
There are also solutions with the Convert block using the<strong> Store integer (SI)</strong> options (more tricky, but interresting to see how theses blocks works when used with the SI option).<br>
<br>
You may find pretty example from the ECAN peripheral (look under mask) than Bryant mairs has done. you may find a link <a href="/forum/topic/11/#p1022">there</a>to download it.<br>
<br>
<br>
<br>
With matlab script, I have nothing more to propose than instructions you provided. I typically use the (bitand, bitshift...) instructions, or worse : divisions and additions...<br>
<br>
Perhaps you may find better way within the fixed point toolbox.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1216">
<header><strong>resodad</strong><time datetime="2010-05-01 11:07 UTC">2010-05-01 11:07 UTC</time></header>
<h3>Re: SPI EEPROM Record and Playback on Explorer 16</h3>
<div class="forum-post-body">Hi Lubin,<br>
<blockquote><header class="quote-author">Citation : LubinKerhuel</header>place a link to this demo </blockquote><br>
That would be great. Then when I forget  :? how to do it, I can easily find it.<br>
<br>
Cheers,<br>
<br>
John</div>
</article>

