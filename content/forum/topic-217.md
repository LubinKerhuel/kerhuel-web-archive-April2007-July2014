---
title: "Send data from Explorer16 to Matlab ?"
url: "/forum/topic/217/"
archiveKind: "topic"
---
# Send data from Explorer16 to Matlab ?

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p817">
<header><strong>laurent841</strong><time datetime="2009-04-13 16:07 UTC">2009-04-13 16:07 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I started to use the toolbox for a couple of days. I work on the Explorer 16 board and I'm currently trying to send data to Matlab using the UART, but it doesn't work.<br>
<br>
<br>
<br>
In order to begin with a very simple model, I just want to send a constant (uint16) to Matlab using UART communication. <br>
<br>
<br>
<br>
Since I don't have any DB9 port on my computer, I use a serial to serial (USB) adaptater. Matlab doesn't even seem to recognize when I unplug the USB port because it still gives me this message when I click on "Connexion" in the rs232gui :<br>
<br>
<br>
<br>
Connecting... May take few seconds...<br>
<br>
Port COM1 successfully open at 19200............OK<br>
<br>
<br>
<br>
I let the original plot commands in the script frame of rs232gui. If I let the USB cable plugged, Matlab displays the following message when I click on Start :<br>
<br>
<br>
<br>
redefinition SerialCOM<br>
<br>
<br>
<br>
and nothing else happens.<br>
<br>
<br>
<br>
Is there any test I can perform to check if data are sended from the board trough UART ? Am I right to precise COM1 in the model if I use an USB adaptator ?<br>
<br>
<br>
<br>
Thank you in advance for your reply,<br>
<br>
Kind regards,<br>
<br>
<br>
<br>
Laurent</div>
</article>

<article class="forum-post" id="p818">
<header><strong>laurent841</strong><time datetime="2009-04-13 17:14 UTC">2009-04-13 17:14 UTC</time></header>
<h3>Re: Send data from Explorer16 to Matlab ?</h3>
<div class="forum-post-body">Ok it seems to work fine now. I used UART1 but only UART2 is cabled on Explorer16.<br>
<br>
<br>
<br>
In addition, the USB adaptater was in fact the port COM8 instead of COM1.<br>
<br>
<br>
<br>
Have a nice Easter Eggs,<br>
<br>
Kind regards,<br>
<br>
<br>
<br>
Laurent</div>
</article>

<article class="forum-post" id="p820">
<header><strong>LubinKerhuel</strong><time datetime="2009-04-14 12:05 UTC">2009-04-14 12:05 UTC</time></header>
<h3>Re: Send data from Explorer16 to Matlab ?</h3>
<div class="forum-post-body">Hi laurent, <br>
<br>
Thanks for sharing your experience.<br>
<br>
<br>
<br>
Lubin</div>
</article>

