---
title: "Data Logging to LabVIEW"
url: "/forum/topic/98/"
archiveKind: "topic"
---
# Data Logging to LabVIEW

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p264">
<header><strong>Masaki</strong><time datetime="2008-03-12 02:12 UTC">2008-03-12 02:12 UTC</time></header>
<div class="forum-post-body">TX_Labview_MATLAB block is a powerful tool to data logging.<br>
<br>
But, thinking about the software integration, I would also like to data log to LabVIEW.<br>
<br>
So my questions here are:<br>
<br>
<br>
<br>
1) Is there any LabVIEW code which can interface to the TX_Labview_MATLAB block?<br>
<br>
<br>
<br>
2) If there isn't such code left, is it possible to know the data format?<br>
<br>
    I seem to find it in the following URL, but I cannot read french unfortunetely.<br>
<br>
<a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">http://lubink.free.fr/projelectro/Proto ... ew_FR.html</a><br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p320">
<header><strong>Masaki</strong><time datetime="2008-04-30 06:04 UTC">2008-04-30 06:04 UTC</time></header>
<h3>Re: Data Logging to LabVIEW</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<blockquote><br>
Anyway, I attach old labview files. I provide it "in its actual state".<br>
<br>
I have not installed labview on my computer right now.<br>
</blockquote><br>
<br>
Based on your LabVIEW program, I have made my interfacing program.<br>
<br>
At the same time, I've tried to figure our your French home page, where you wrote about the<br>
<br>
protocole. I understand that all data from "TX_LabVIEW_MATLAB" block have following headers:<br>
<br>
<br>
<br>
  bits 7-4:  Number of the channel (0 to 15) <br>
<br>
  bits 3-2:  type of data corresponding to the number of bytes composing the data (1 to 4) <br>
<br>
  bits 1-0:  signature of the byte controls =　"01" <br>
<br>
<br>
<br>
Is this understanding correct?<br>
<br>
If it's so, my next question is what happens if data happen to have confusing values <br>
<br>
resembling to header format. For example, in binary:<br>
<br>
<br>
<br>
   00000101  00010101 00020101  00000101 00010101 01000101 .....<br>
<br>
<br>
<br>
I wrote these bytes in terms of int16 data from channel 0. <br>
<br>
But they can also be interpreted as int 16 data from channel 1.<br>
<br>
<br>
<br>
How does your algorithm in "interface Tx-MATLAB" block distinguish the two cases?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p322">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-30 22:34 UTC">2008-04-30 22:34 UTC</time></header>
<h3>Re: Data Logging to LabVIEW</h3>
<div class="forum-post-body">Hi Masaki,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Masaki</header>bits 7-4: Number of the channel (0 to 15)<br>
<br>
bits 3-2: type of data corresponding to the number of bytes composing the data (1 to 4)<br>
<br>
bits 1-0: signature of the byte controls =　"01" </blockquote><br>
Correct !<br>
<br>
<blockquote><header class="quote-author">Citation : Masaki</header>If it's so, my next question is what happens if data happen to have confusing values<br>
<br>
resembling to header format. For example, in binary:<br>
<br>
00000101 00010101 00020101 00000101 00010101 01000101 .....<br>
<br>
I wrote these bytes in terms of int16 data from channel 0.<br>
<br>
But they can also be interpreted as int 16 data from channel 1.</blockquote><br>
<br>
It is not possible to distinguish here between the two possibilities on this example.<br>
<br>
However, in most case, data will not always have their two lowest bytes set to 01. If few data do not finish by 01, the labview algorithm will converge after a few data to the correct solution.<br>
<br>
If labview is started before the dsPIC started to send data, there will be no error. Errors may occur only when you hot plug the serial line or start labview while dsPIC is sending data.<br>
<br>
 <br>
<br>
Note that the matlab script is even more powerful that the labview algorithm because it extract the solution which is the best, considering the whole data frame received at time T. In this way, it is optimal because it use all the information available. The labview algorithm is suboptimal because it analyses the data frame byte after byte in chronological order and takes on the fly decisions.<br>
<br>
(dataframe is the set of data read from the COM port. It may contain 0 to several hundred or thousand of bytes)<br>
<br>
<br>
<br>
The labview algorithm that Masaki is using will be published soon on the website.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/64-Protocol.png">Pièce jointe : Protocol.png</a></p>
</article>

