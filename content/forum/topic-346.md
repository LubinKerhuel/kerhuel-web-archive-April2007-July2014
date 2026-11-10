---
title: "how to send data using rs232gui"
url: "/forum/topic/346/"
archiveKind: "topic"
---
# how to send data using rs232gui

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1431">
<header><strong>coolj</strong><time datetime="2011-01-07 06:54 UTC">2011-01-07 06:54 UTC</time></header>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
Do you have any examples on how to send data from Matlab to the dspic using rs232gui?  I believe it is possible since you have two "Send" buttons, but I don't know how to configure my model to accept the incoming data.<br>
<br>
<br>
<br>
Can you help?<br>
<br>
<br>
<br>
Much appreciated!<br>
<br>
Justin</div>
</article>

<article class="forum-post" id="p1434">
<header><strong>LubinKerhuel</strong><time datetime="2011-01-08 22:54 UTC">2011-01-08 22:54 UTC</time></header>
<h3>Re: how to send data using rs232gui</h3>
<div class="forum-post-body">Hi Justin,<br>
<br>
<br>
<br>
You may have a look on the <a href="/wiki/flex-board-blinking-led/">Flex Board blinking LED</a> example<br>
<br>
<br>
<br>
This example demonstrates how to modify a variable in your model running in real time into your dsPIC, through the UART and using the rs232gui graphical interface available in the blockset.<br>
<br>
<br>
<br>
Please have a look on this one. You may simplify it so as to make testing of your UART interface.<br>
<br>
<br>
<br>
Please let me know if you can use it with theses explanations.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1435">
<header><strong>coolj</strong><time datetime="2011-01-09 21:13 UTC">2011-01-09 21:13 UTC</time></header>
<h3>Re: how to send data using rs232gui</h3>
<div class="forum-post-body">Lubin,<br>
<br>
<br>
<br>
Thanks as always!  The example worked great on the explorer 16 board after making a couple modifications (digital output pin, RS232 port).<br>
<br>
<br>
<br>
I attached the model that worked well on my explorer 16 for others.<br>
<br>
<br>
<br>
A note for others:  make sure to select the script button in the rs232gui "dflt Signe" to plot signed data instead of unsigned.<br>
<br>
<br>
<br>
The only issue I see is it is hard to change the "Send1"/"Send2" data while it is receiving data.  You also often have to press the send buttons several times before it will send the data (probably because it is busy receiving).<br>
<br>
<br>
<br>
Justin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/365-Explorer16_Blinking_Led_Uart_Send.mdl">Pièce jointe : Explorer16_Blinking_Led_Uart_Send.mdl</a></p>
</article>

<article class="forum-post" id="p1436">
<header><strong>coolj</strong><time datetime="2011-01-09 21:35 UTC">2011-01-09 21:35 UTC</time></header>
<h3>Re: how to send data using rs232gui</h3>
<div class="forum-post-body">One other question:<br>
<br>
<br>
<br>
When compiling the FlexBoard_Blinking_Led.mdl, the upper right corner of blocks are an apparent time.  Can you tell me what this time is and how to configure it?  <br>
<br>
<br>
<br>
Thanks!<br>
<br>
Justin<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/366-Printscreen_089.gif">Pièce jointe : Printscreen_089.gif</a></p>
</article>

