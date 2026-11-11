---
title: "IMU Complementary filter method"
url: "/forum/topic/200/"
archiveKind: "topic"
---
# IMU Complementary filter method

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p741">
<header><strong>Martin</strong><time datetime="2009-02-08 13:01 UTC">2009-02-08 13:01 UTC</time></header>
<div class="forum-post-body">hi, <br>
<br>
I am new to this. <br>
<br>
I'm evaluating that method adopted to generate the artificial horizon. <br>
<br>
regarding the procedure of complementary filters for mixing Gyro and accelerometer, I see no way that prevents the spurious signals produced by the accelerations in typical flight.<br>
<br>
In <a href="/images/IMU_Simulation_ComplementaryFilter.png">http://www.kerhuel.eu/wiki/Image:IMU_Si ... Filter.png</a> <br>
<br>
I can see that an input acceleration will produce a change in the angle output.<br>
<br>
I'm correct..?</div>
</article>

<article class="forum-post" id="p742">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-08 13:21 UTC">2009-02-08 13:21 UTC</time></header>
<h3>Re: IMU Complementary filter method</h3>
<div class="forum-post-body">That's correct, but acceleration here is not the true acceleration of the IMU itself, but a change in the gravity vector orientation to which the <a href="http://en.wikipedia.org/wiki/Accelerometer">accelerometer</a> is sensitive.</div>
</article>

<article class="forum-post" id="p746">
<header><strong>Martin</strong><time datetime="2009-02-09 12:14 UTC">2009-02-09 12:14 UTC</time></header>
<h3>Not G accelerations</h3>
<div class="forum-post-body">hi, <br>
<br>
I have done by now: a 3-axis accelerometer MMA7260 read by a 12-bit Coldfire MCF52233 sampled at 500 Hz. <br>
<br>
noise filtering of vibrations do it by calculating the average value of the n-axis and then subtracting it to the n-axis. <br>
<br>
each n-axis average value is filtered by a 9 tap Hamming LP FIR. <br>
<br>
the result is excellent a clean  g axis. <br>
<br>
for now and for testing it is applied to the .net artificial horizon form Tom Pycke (tom.pycke.be.)<br>
<br>
now incorporate a Gyro signal on x-axis  (esky disassembly MA745/3) in a complementary filter configuration. <br>
<br>
but not G accelerations still produce erroneous angle indication.??<br>
<br>
sorry for my english.</div>
</article>

<article class="forum-post" id="p747">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-09 21:38 UTC">2009-02-09 21:38 UTC</time></header>
<h3>Re: IMU Complementary filter method</h3>
<div class="forum-post-body">Hi Martin,<br>
<br>
<br>
<br>
I did not get your question. It would be helpfull to add a quick draw with transfert functions (or a simulink model) <br>
<br>
Lubin</div>
</article>

