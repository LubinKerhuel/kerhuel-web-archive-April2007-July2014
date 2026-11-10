---
title: "can i make real time speech processing and dsc starter kit"
url: "/forum/topic/339/"
archiveKind: "topic"
---
# can i make real time speech processing and dsc starter kit

Forum : [General Remark and Questions](/forum/#forum-1)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1371">
<header><strong>angelita</strong><time datetime="2010-12-01 15:56 UTC">2010-12-01 15:56 UTC</time></header>
<div class="forum-post-body">hi i want to know if i can make a real time speech processing (without recording the sound) using matlab simulink<br>
<br>
and if the MPLAB Starter Kit for dsPIC DSCs is supported bu simulink<br>
<br>
<br>
<br>
if yes..would you give me some examples application program or stuff like that</div>
</article>

<article class="forum-post" id="p1374">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-01 19:18 UTC">2010-12-01 19:18 UTC</time></header>
<h3>Re: can i make real time speech processing and dsc starter k</h3>
<div class="forum-post-body">Hi, <br>
<br>
<br>
<br>
It's possible to do real time sound processing with matlab simulink. The signal processing blockset has a microphone block and a speaker block allowing doing this. There are also few toolbox that may accelerate real time processing on your computer (windows target ?).<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : angelita</header>MPLAB Starter Kit for dsPIC DSCs is supported bu simulink</blockquote><br>
It only depends which microcontroller is in the Starter Kit you are using. Which one is it ?<br>
<br>
<br>
<br>
I have not done yet real time speech processing using dsPIC. It should be feasible using simulink and the dsPIC blockset provided the dsPIC is running fast enough. I typically used a processing sampling rate (i.e. time step) of 2Khz (i.e. 0.5ms) to implement automatic control laws. Thus, sampling sound at at least 8KHz should be Ok. Anyway, take care of the time consumed by the algorithm (monitor the real time consumption with the "time step" block)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1377">
<header><strong>angelita</strong><time datetime="2010-12-02 05:12 UTC">2010-12-02 05:12 UTC</time></header>
<h3>Re: can i make real time speech processing and dsc starter k</h3>
<div class="forum-post-body">i mean the whole kit <br>
<br>
i want to control this project with usb interface so i want to use the pic18 in the kit <br>
<br>
and the dspic33 for the audio  processing (noise and echo ellimination )<br>
<br>
is that possible ??</div>
</article>

<article class="forum-post" id="p1378">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-02 11:44 UTC">2010-12-02 11:44 UTC</time></header>
<h3>Re: can i make real time speech processing and dsc starter k</h3>
<div class="forum-post-body">I guess pic18 serve only for programming the main dsPIC 33.<br>
<br>
Thus, you will not be able to use USB interface for your own program.<br>
<br>
 If you have few input/output on the board for sound, it should  be Ok.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1676">
<header><strong>golesorkh</strong><time datetime="2011-08-30 10:31 UTC">2011-08-30 10:31 UTC</time></header>
<h3>Re: can i make real time speech processing and dsc starter k</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header> There are also few toolbox that may accelerate real time processing on your computer (windows target ?).</blockquote><br>
<br>
<br>
<br>
hi;<br>
<br>
may i ask what are these toolboxes that can accelerate realtime processing? u mean realtime windows target? <br>
<br>
actually i have used microphone and speaker, i connected them directly/ with a delay block. but sound transmision has delay of at least 1 sec. would u give me a detailed help on how to use this windows target.</div>
</article>

<article class="forum-post" id="p1677">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-30 11:54 UTC">2011-08-30 11:54 UTC</time></header>
<h3>Re: can i make real time speech processing and dsc starter k</h3>
<div class="forum-post-body">I am not up to date with real time processing of audio data with simulink on PC. I could provide the following inputs:<br>
<br>
<br>
<br>
- Simulink Microphone block might create a buffer and provide the following block with a fixed size buffer. This will create a first delay in processing.<br>
<br>
- sound cards drivers usually creates also delay. You might find specialized driver that should reduced sound delay. Their name is <a href="http://www.asio4all.com/">ASIO4ALL</a>. However, for best results, your sound cards should be compatible "ASIO".<br>
<br>
<br>
<br>
Lubin</div>
</article>

