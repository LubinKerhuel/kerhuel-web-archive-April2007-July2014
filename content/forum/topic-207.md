---
title: "about Tx-Matlab"
url: "/forum/topic/207/"
archiveKind: "topic"
---
# about Tx-Matlab

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p782">
<header><strong>Magic</strong><time datetime="2009-03-16 08:31 UTC">2009-03-16 08:31 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I have a question about Tx-Matlab<br>
<br>
<br>
<br>
My baud rate is 115200 and max 23 Bytes/0.002s<br>
<br>
<br>
<br>
I send 3 Datas  every 0.002s.<br>
<br>
But I found the time interval is about 0.01s or 0.02s(sometime 0.03s) in t_R &amp; t_Rn in workspace.<br>
<br>
<br>
<br>
<br>
Is the UART wrong? or some configuration I do not set?<br>
<br>
<br>
<br>
Magic</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/214-time1.JPG">Pièce jointe : time1.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/215-MC710_ID2.mdl">Pièce jointe : MC710_ID2.mdl</a></p>
</article>

<article class="forum-post" id="p784">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-17 00:26 UTC">2009-03-17 00:26 UTC</time></header>
<h3>Re: about Tx-Matlab</h3>
<div class="forum-post-body">Hi Magic,<br>
<br>
<br>
<br>
Thanks for this interresting question.<br>
<br>
I tried to complete the doc of the<a href="/wiki/simulink-embedded-target-for-pic/">Interface_Tx-Matlab</a>  page. I added that :<br>
<pre><code>T_R is an approximation of time only, and shoudl be used for vewing purpose only. If you need precise data time stapm, follow the following procedure :
<wbr>
    * On the simulink model, make sure to not overload the UART. Check that you are sending less data than max allowed by the UART bauds. To count the number of bytes used, when using the Tx-Labview-Matlab block, add one byte for each data sent. For example sending one uint8 data takes 2 bytes, uint16 data takes 3 bytes and uint32 data takes 5 bytes.
    * Reconstruct a vector timing corresponding to the simulink's UART timing. 
<wbr>
T_R (and T_Rn) approximate the time using the computer clock. Each time Matlab read an UART sequence, time is read. Then, the first byte of the sequence is assigned to the time of the previous clock read, and the last byte of the sequence is assigned with current time. Any bytes in between is assigned to a time using a linear approximation (with time of sequenc start and time of sequence stop). Thus, the time received of the first trame may be much longer if no data is send at the beginning of the logging process. </code></pre><br>
<br>
I am not very happy of this explanation, but I hope anyway to make it clear enough !<br>
<br>
Let me know... <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p786">
<header><strong>Magic</strong><time datetime="2009-03-17 02:33 UTC">2009-03-17 02:33 UTC</time></header>
<h3>Re: about Tx-Matlab</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Thank you for this explanation. I understand now! <br>
<br>
<br>
<br>
Thus,after computer received the data,the time interval would be about the sampling time(0.002s).<br>
<br>
<br>
<br>
<br>
Thanks again.<br>
<br>
<br>
<br>
Magic</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/216-received%20data.JPG">Pièce jointe : received data.JPG</a></p>
</article>

<article class="forum-post" id="p787">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-17 14:34 UTC">2009-03-17 14:34 UTC</time></header>
<h3>Re: about Tx-Matlab</h3>
<div class="forum-post-body">Hi Magic,<br>
<blockquote><header class="quote-author">Citation : Magic</header>after computer received the data,the time interval would be about the sampling time(0.002s)</blockquote><br>
That true, but you should really recompute a time vector of exactly 0.002s as the dsPIC quartz is much better than the bad approximation that is done with the RS232GUI.<br>
<br>
If you do not overload the UART (It seems not to be overloaded here) the sampling time of the three data is exactly 0.002s !<br>
<br>
<br>
<br>
for example : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt;R = padr(R,1);
<wbr>
t_Rreconstructed = 0:.002:((length(R)-1)*.002);
<wbr>
%% if you want to generate a file to feed a simulink model : 
SimIn = [0:.002:(length(R)-1)*.002 ; R'];
save SimIn SimIn
</code></pre><br>
<br>
Lubin</div>
</article>

