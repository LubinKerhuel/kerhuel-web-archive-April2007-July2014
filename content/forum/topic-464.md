---
title: "Problem with Flag Output of UART RX Block"
url: "/forum/topic/464/"
archiveKind: "topic"
---
# Problem with Flag Output of UART RX Block

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1762">
<header><strong>shatteredmaul</strong><time datetime="2011-12-14 21:23 UTC">2011-12-14 21:23 UTC</time></header>
<div class="forum-post-body">My Build Environment:<br>
<br>
MATLAB R2011a<br>
<br>
Block Set Version 3.5b  <br>
<br>
<br>
<br>
My Application:<br>
<br>
I'm using the block set with a dsPIC33. I'm streaming ADC samples over UART1. You could call it a low speed oscilloscope. Each sample is encoded to a 5 character frame which is packed with a Vector Concatenate block and transmitted with the UART TX block. Because I'm sampling in the neighborhood of 100Hz, the TX block gets executed very frequently. The baud rate is set to 115200 and the simulation step size is set to 500us.<br>
<br>
The application is also designed to receive commands which is accomplished with a UART RX block. I use the Flag output to indicate that a new character has been received and needs to be processed.<br>
<br>
<br>
<br>
My Problem:<br>
<br>
The encoded samples are being transmitted without issue over UART1. However, I'm having trouble getting UART1 to receive data reliably once the UART TX block starts being executed frequently. I've tied the Flag output from the UART RX block to a digital output and sampled it with an oscilloscope. When the UART TX block is being executed frequently, the Flag output doesn't go high. I've tried using and not using RX and TX interrupts. However, the problem persists whether or not interrupts are used. Are there any known caveats with executing the UART TX block frequently, or am I simply doing something wrong?<br>
<br>
<br>
<br>
I'd be enormously grateful for any help the community could render and will gladly contribute back in the near future!</div>
</article>

<article class="forum-post" id="p1763">
<header><strong>LubinKerhuel</strong><time datetime="2011-12-15 08:12 UTC">2011-12-15 08:12 UTC</time></header>
<h3>Re: Problem with Flag Output of UART RX Block</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
There is no know caveeats until now.<br>
<br>
Your description is very clear, thanks for it.<br>
<br>
Would it be possible to upload your model on the forum (or an equivalent model creating that problem) ? It will help to find out what's going on.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1767">
<header><strong>shatteredmaul</strong><time datetime="2011-12-19 20:54 UTC">2011-12-19 20:54 UTC</time></header>
<h3>Re: Problem with Flag Output of UART RX Block</h3>
<div class="forum-post-body">Thanks for your response. For the time being, I'm going to implement a workaround to my problem. At some point in the near future I'm going to upload a version of the model so we can find out what the problem was.  :)<br>
<br>
<br>
<br>
Matt</div>
</article>

<article class="forum-post" id="p1859">
<header><strong>palacio</strong><time datetime="2012-03-12 10:48 UTC">2012-03-12 10:48 UTC</time></header>
<h3>Re: Problem with Flag Output of UART RX Block</h3>
<div class="forum-post-body">I want to know about FPGA implementation of UART? Hi, I have to give a seminar on Field Programmable Graphic Array Implementation Of UART. Please any one can help regarding this.I dont have any material for this. Thanks in advance.<br>
<br>
___________________________<br>
<br>
<a href="http://www.keywordspy.com/overview/keyword.aspx?q=yahoo%20keyword%20tool">yahoo keyword tool</a> ~ <a href="http://www.keywordspy.com/overview/keyword.aspx?q=overture">overture</a> ~ <a href="http://www.keywordspy.com/overview/keyword.aspx?q=traffic%20estimator">traffic estimator</a> ~ <a href="http://www.keywordspy.com/overview/keyword.aspx?q=adwords%20traffic%20estimator">adwords traffic estimator</a></div>
</article>

