---
title: "send and receive multiple data using GUI"
url: "/forum/topic/477/"
archiveKind: "topic"
---
# send and receive multiple data using GUI

Forum : [General Remark and Questions](/forum/#forum-1)

10 message(s) · archive en lecture seule

<article class="forum-post" id="p1823">
<header><strong>odedyech</strong><time datetime="2012-02-05 13:31 UTC">2012-02-05 13:31 UTC</time></header>
<div class="forum-post-body">Hello lubin,<br>
<br>
<br>
<br>
I am tring to send and receive data thru UART from dsPIC30F4011 to the comp.<br>
<br>
I am using your block "Tx Output Multiplexed For Matlab-Labview" and I was wondering what are the variables I need to insert in order to send data thru this block to the dspic (instead of sending with the send 1 and send 2 buttons), and to split data comming into diffrent channels in the "Tx Output Multplexed for Matlab-Labview" block to different graphs.<br>
<br>
<br>
<br>
Thanks in advance,<br>
<br>
<br>
<br>
Oded</div>
</article>

<article class="forum-post" id="p1840">
<header><strong>Saeed</strong><time datetime="2012-02-29 22:28 UTC">2012-02-29 22:28 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello there,<br>
<br>
Would you please tell me how to build a simulink model where a user-defiend-type data is read from MATLAB workspace into the dsPIC demo board through UART peripheral and rs232 connection?<br>
<br>
And what are the limitations in this regard!?</div>
</article>

<article class="forum-post" id="p1841">
<header><strong>odedyech</strong><time datetime="2012-03-01 07:53 UTC">2012-03-01 07:53 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello Saeed,<br>
<br>
There are a few options for sending data from the Matlab/Simulink to the dsPIC:<br>
<br>
1. Open a serial port in the Matlab command line using "serial" command, and send data using "fwrite" command.<br>
<br>
Pros: you can create a GUI.<br>
<br>
Cons: you need a good understanding in Matlab.<br>
<br>
2. send data using simulinks Real time Windows target: you have a veriety of block such as: Packet input/ouput, Stream input/ouput, and so on. I recomend Packet input for sending int/uint/double and so on (not strings)<br>
<br>
Note - if you want to use these blocks you need to change in the "Simulink Configuration"-&gt;"Real Time Workshop"-&gt;"system target file"-&gt;Change file to rtwin.<br>
<br>
Pros: Easy to use, and you can check connectivity (using the test button) of your device.<br>
<br>
Cons: If you want to send and recieve a big amount of data, this might be a bit difficult.<br>
<br>
3. you can use Lubin's "Tx Output Multiplexed For Matlab-Labview" block to send arrays.<br>
<br>
Pros: Easiest to use.<br>
<br>
Cons: you can send only one array which is quite limmiting. I cant seem to send "serious" data using GUI.<br>
<br>
<br>
<br>
I hope this answers your question.<br>
<br>
Oded</div>
</article>

<article class="forum-post" id="p1849">
<header><strong>Saeed</strong><time datetime="2012-03-06 00:40 UTC">2012-03-06 00:40 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello to you dear odedyech,<br>
<br>
I am realy thankful for your kind well organised reply.<br>
<br>
Your advices are really fascinating! :D <br>
<br>
I tried your first proposed method.<br>
<br>
However, it didn't work.<br>
<br>
I tried to send a variable with unit value (say, A=1) by "fwrite" function. If this transmission was succesful, the LED of the dsPIC board would be turned ON.<br>
<br>
But, It didn't work. :( <br>
<br>
Would you plz kindly take a look at the project (an mdl file I uploaded) <br>
<br>
By The way, besides using serial port connection through rs232 with dsPIC UART, there is a USB connection possibility through SPI periphral of the PIC.<br>
<br>
Do you have any idea about that (Pros/Cons)?<br>
<br>
Do you know how to manage data import through USB port of SPI from matlab interface?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/486-Matlab2PICDataPr.mdl">Pièce jointe : Matlab2PICDataPr.mdl</a></p>
</article>

<article class="forum-post" id="p1850">
<header><strong>odedyech</strong><time datetime="2012-03-06 08:26 UTC">2012-03-06 08:26 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello Saeed,<br>
<br>
<br>
<br>
I see that you used Lubin's rs232 GUI block. If you wish to use this block you need to open it (by the way, you dont have to burn it on the dsPic's block diagram) select the COM Port you have connected your device to (the dsPIC or other device)<br>
<br>
select the BaudRate (this is important!! you must define the same BR everywhere! in the block diagram you defined UART 2 to be 19200 thus you must define the BR as well to 19200) and press the "connexion" button. wait untill it is purple (the connexion button) and the you can press the "send" button to send your data.<br>
<br>
<br>
<br>
I have attached an example code of how to open a COM PORT in the matlab command line.<br>
<br>
<br>
<br>
I also attached a Real Time Target model model. if you cant find the Real Time Target blocks write in the command line "rtwin -setup".<br>
<br>
after you finished defining the configurations (as described in the PDF file) build the model and press play.<br>
<br>
you will then (hopefully  :D ) see the dsPIC LED lit (Port A2 in the dsPIC). if you will change the constant (in the real time model) the LED will turn off (all in Real time - you dont need to rebuild)<br>
<br>
<br>
<br>
Good Luck<br>
<br>
<br>
<br>
Oded</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/487-rs232%20example.m">Pièce jointe : rs232 example.m</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/488-RealTimeTarget.mdl">Pièce jointe : RealTimeTarget.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/489-Real%20time%20target.pdf">Pièce jointe : Real time target.pdf</a></p>
</article>

<article class="forum-post" id="p1851">
<header><strong>Saeed</strong><time datetime="2012-03-06 12:03 UTC">2012-03-06 12:03 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Dear Oded,<br>
<br>
Thank you for your support. It is appreciating.<br>
<br>
How ever, I did as you explained. But there is something wrong when the packet target begins to connect to the board.<br>
<br>
Although I succeeded to read data from the board through rs232 in MATLAB in another project suggesting that my cable connection is ok.<br>
<br>
I attached snapshots of the error occurred.<br>
<br>
It is kind of you if taking a look at them.<br>
<br>
My comment is that, probably there is somthing wrong with send capability of USBSerial cable, (it is not realy full duplex... cause I used the fwrite command, the data was sent and ValuesSent:1, but ValuesReceived:0)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/490-SerialPort.rar">Pièce jointe : SerialPort.rar</a></p>
</article>

<article class="forum-post" id="p1855">
<header><strong>odedyech</strong><time datetime="2012-03-10 10:45 UTC">2012-03-10 10:45 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello again,<br>
<br>
<br>
<br>
I can see that the BaudRate in your dsPIC is 19200, and in the Real-Target the BaudRate is 9600. You should change the settings (Serial Port, and BaudRate) until the test passes.<br>
<br>
Are you sure that the Serial Port is COM2?<br>
<br>
You can check that by going to Manage, and check the PORT connections.</div>
</article>

<article class="forum-post" id="p1856">
<header><strong>Saeed</strong><time datetime="2012-03-10 18:30 UTC">2012-03-10 18:30 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hello odedyech,<br>
<br>
Thank you, you are right!<br>
<br>
Finally I accomplished to send and receive single data (A=1) through rs232 .<br>
<br>
As you suggested I used fwrite/fread MATLAB commands and now I have a good understanding of the procedure.<br>
<br>
I uploaded an mdl file, the goal is to send a series of data from MATLAB workspace and then receive the same from PIC in MATLAB. <br>
<br>
Would you please take a look and kindly modify the project so that answers my troubles as following.<br>
<br>
1- How is it possible to send a series of data from MATLAB (e.g. a column matrix) and then receive the same from PIC in MATLAB and see the result?<br>
<br>
2- How is it possible to apply a delay between receive and transmit of data by Rx and Tx (it seems that the delay is necessary)?<br>
<br>
3- Is using SPI as a digital input/output recommended in these conditions (if yes would you add a SPI and adjust it)?<br>
<br>
My email is [adresse e-mail retirée]; it is honourable sending a message to this email so as to have your Email.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/492-SerialConnection.mdl">Pièce jointe : SerialConnection.mdl</a></p>
</article>

<article class="forum-post" id="p1857">
<header><strong>odedyech</strong><time datetime="2012-03-10 19:36 UTC">2012-03-10 19:36 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Hi again Saeed,<br>
<br>
I am not sure that this block you used (Data Store Write) is suitable for burning on the dsPIC.. remember that this block is transferred to C code.<br>
<br>
Again I am not sure, I started using these blocks just a few months ago as well.<br>
<br>
<br>
<br>
As for your questions:<br>
<br>
1. I attached 2 simulink models: a. a model that will be burned on the dsPIC. In this model data is received via UART2 Rx and enter port A0, and sent via UART2 Tx.<br>
<br>
b. Real Time Target model: In this block I send a repeating sequence with RS232. The sequence is: 0 1 0 2 0 3 0 4 0 5 0 6. This sort of sequence could turn on/off a LED connected to Port A0 (for example).<br>
<br>
In this model I receive the data and display it, and send it to the Workspace.<br>
<br>
Note- Dont forget to configure the blocks Packet Input/Output correctly  :wink: <br>
<br>
<br>
<br>
2. I am not sure for what a delay is needed for but, you can change the "sample Time" in most blocks. I think that the dimensions are in seconds (e.g. if you will enter '1' every sec there will be an execution of the block, '2' means 2 sec etc.)<br>
<br>
also there is a block "Delay" (write Delay in the search line you will find it)<br>
<br>
<br>
<br>
3. For my understanding SPI is used to get 2 (or more) different micro-controllers to communicate. I am not sure this is what you need (unless it is)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/493-SerialConnection.mdl">Pièce jointe : SerialConnection.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/494-RealTimeTarget.mdl">Pièce jointe : RealTimeTarget.mdl</a></p>
</article>

<article class="forum-post" id="p1858">
<header><strong>Saeed</strong><time datetime="2012-03-10 21:03 UTC">2012-03-10 21:03 UTC</time></header>
<h3>Re: send and receive multiple data using GUI</h3>
<div class="forum-post-body">Dear odedyech,<br>
<br>
Thank you. Although whenever I use send or receive package in MATLAB I get error (I think its related to the MATLAB version), but fwrite/fread works.<br>
<br>
But, the problem still exits :( <br>
<br>
See, suppose you have measured the weather degree of a place during one month and you have 15000 samples in a form of MAT file (1st column time, 2nd column value);<br>
<br>
How do you build a project to import these values successively in to PIC to be prcessed (e.g. some data processing on the inserted value)?</div>
</article>

