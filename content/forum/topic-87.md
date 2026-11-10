---
title: "Question about Filter"
url: "/forum/topic/87/"
archiveKind: "topic"
---
# Question about Filter

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p218">
<header><strong>micman2</strong><time datetime="2008-02-15 17:15 UTC">2008-02-15 17:15 UTC</time></header>
<div class="forum-post-body">I saw two examples that implement filters, I noticed the speed with which you can implement filters in a dspic.<br>
<br>
But I have a question: <br>
<br>
<br>
<br>
How has been calculated Band pass filter?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/18-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p228">
<header><strong>LubinKerhuel</strong><time datetime="2008-02-18 22:21 UTC">2008-02-18 22:21 UTC</time></header>
<h3>Re: Question about Filter</h3>
<div class="forum-post-body">Low pass filter with a cut off frequency at 1 Hz : <br>
<br>
1Hz means 2*pi rad/s which is approximatively 6 rad/s.<br>
<br>
<br>
<br>
matlab code :<br>
<pre><code>&gt;&gt; Filter_1Hz = tf([6],[1 6])
<wbr>
Transfer function:
  6
-----
s + 6
<wbr>
&gt;&gt; bode(Filter_1Hz)
&gt;&gt; </code></pre><br>
You will get :<br>
<br>
We have a 45° phase and a -3db cut off at 6 rad/s which is approximatively 1Hz.<br>
<br>
6 should be replace by 2*pi so as to get a precise 1Hz low pass filter.<br>
<br>
<br>
<br>
If you are note familiar with theses math, have a look on the Laplace transform.<br>
<br>
<br>
<br>
The filter is then discretized for a sampling rate of 200Hz using the c2d function with the tustin method.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/30-Filter_1Hz.png">Pièce jointe : Filter_1Hz.png</a></p>
</article>

<article class="forum-post" id="p297">
<header><strong>chukhivuitinh</strong><time datetime="2008-04-23 11:26 UTC">2008-04-23 11:26 UTC</time></header>
<h3>Re: Question about Filter</h3>
<div class="forum-post-body">can simu kalman filter ????</div>
</article>

<article class="forum-post" id="p302">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-24 22:17 UTC">2008-04-24 22:17 UTC</time></header>
<h3>Re: Question about Filter</h3>
<div class="forum-post-body">I will have a look on kalman filter to estimate the gyro bias. But I could not give a date when I will do it.<br>
<br>
<br>
<br>
You could do it anyway !</div>
</article>

