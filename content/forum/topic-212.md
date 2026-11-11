---
title: "send more data within one time step"
url: "/forum/topic/212/"
archiveKind: "topic"
---
# send more data within one time step

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p801">
<header><strong>Magic</strong><time datetime="2009-03-24 08:22 UTC">2009-03-24 08:22 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I want to send 3 data(6 bytes) within one time step(0.0005s) and set Baud rate = 115200(kb/s).<br>
<br>
<br>
<br>
And the max is 5.75 Bytes/Step was read on UART Configuration block.  <br>
<br>
<br>
<br>
Obviously, the UART can't not send 3 data within one time step.<br>
<br>
<br>
<br>
Thus,from <a href="/wiki/simulink-embedded-target-for-pic/">your example</a>, I use the Tx_Output block(not the Tx_matlab)  to send my datas. <br>
<br>
<br>
On the rs232gui, I  press down the RAW button and clear the script.<br>
<br>
<br>
<br>
<br>
But rs232gui received nothing after dsPic started. <br>
<br>
<br>
<br>
And the R is also all zero in workspace.<br>
<br>
<br>
<br>
Could you help me? Thx!<br>
<br>
<br>
<br>
or is there anthor way to send more data within one time step?<br>
<br>
<br>
<br>
Magic</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/225-MC710_ID2.mdl">Pièce jointe : MC710_ID2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/226-2009-03-24_161523.jpg">Pièce jointe : 2009-03-24_161523.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/227-2009-03-24_161605.jpg">Pièce jointe : 2009-03-24_161605.jpg</a></p>
</article>

<article class="forum-post" id="p802">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-24 22:09 UTC">2009-03-24 22:09 UTC</time></header>
<h3>Re: send more data within one time step</h3>
<div class="forum-post-body">Hi Magic,<br>
<br>
<br>
<br>
Thx for the Screen shoot.<br>
<br>
<br>
<br>
I am not sure that model was very well doccumented. However, you may find on the page :<br>
<blockquote>On the embedded simulink model, a mechanism allow to send data during a predefined time: The model embedded on the dsPIC send data only when the value variable60 is different from 0. This variable is changed through the UART using the same rs232gui graphical user interface with the send1 and send2 button. When receiving values [60 x], the embedded simulink model load the value x into the Simulink variable 'variable60'. The Simulink model decreases automatically this variable at a sampling rate of 1 second. This mechanism makes the user able to log data during a predefined time. </blockquote><br>
<br>
There was on the original model a block with sublocks that received data from the UART interface. This one is not present on your model. It is inside the TinyBld Reset block in the model : <a href="/archive-assets/">http://archive.kerhuel.eu/wiki/images/8/86/ ... ta_Raw.png</a><br>
<br>
<br>
<br>
Anyway, to do it much more simple, replace the <strong>Triggered Log Data block</strong> by the Tx block it contains. (you don't really care about trigger here do you ?<br>
<br>
You will then receive your data. But you are sending 7 bytes that is much that the max allowed by the UART as you mention. You should slow down the model time step to allow logging all datas. You may also just slow down few blocks (thus creating a multirate model).<br>
<br>
<br>
<br>
Lubin</div>
</article>

