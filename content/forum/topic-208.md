---
title: "Help using angle estimation"
url: "/forum/topic/208/"
archiveKind: "topic"
---
# Help using angle estimation

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p788">
<header><strong>karthikeyan</strong><time datetime="2009-03-18 13:38 UTC">2009-03-18 13:38 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I am building a self-balancing wheeled inverted pendulum. I am using the IMU from sparkfun <a href="http://www.sparkfun.com/commerce/product_info.php?products_id=741">http://www.sparkfun.com/commerce/produc ... cts_id=741</a>. It has ADXL330 accelerometer and IDG300 gyroscope. I am using dsPIC30F4011. I am attaching the model which I programmed into the dsPIC but it's not working properly. I have the following problems. <br>
<br>
<br>
<br>
1. Regarding bias removal. Should I just use the value specified by the datasheet ? <br>
<br>
2. The estimated angles are not in degrees. They keep varying always. The accelerometer angle estimation is giving a value of 65000 .. !! What should I do so that I get the values in degrees<br>
<br>
3. The gyroscope angle estimation is also not in angles. <br>
<br>
4. the complimentary filter does not give the same value at zero degree. !!<br>
<br>
<br>
<br>
I just want the output in angles. What are the values I should change and how ? Kindly help me.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/217-angle_estimator.mdl">Pièce jointe : angle_estimator.mdl</a></p>
</article>

<article class="forum-post" id="p791">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-18 22:47 UTC">2009-03-18 22:47 UTC</time></header>
<h3>Re: Help using angle estimation</h3>
<div class="forum-post-body">Hi Karthikeyan,<br>
<br>
To resume, you are to adapt the <a href="/wiki/simulink-embedded-target-for-pic/">complementary filter</a> presented on the wiki for the Spark "<a href="http://www.sparkfun.com/commerce/product_info.php?products_id=741">IMU 5 Degrees of Freedom</a>" card.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : karthikeyan</header>just want the output in angles</blockquote><br>
I like "just" ;-)<br>
<br>
<br>
<br>
Anyway, <br>
<br>
- Calculations are in double thus no problems about fixed point overflow or so on...<br>
<br>
- The bias you set for both accelerometers and the gyro is weird. Log data for each : *the gyro  *the Z accel and *the X accel (with the two accelerometers axis horizontal to measure 0g and no gravity) The mean of theses logged data is the bias to remove from the data. (You could find it wth docs, but for sure it will not be exact)<br>
<br>
- You must find the gain of the gyro to express the value is degree/s. This should be in by the doc byt should be refine by hand (have a look on the provided simulation, I rotate My rate gyro by a precise 90°, and I integrated the valud and find the gain necessary to get a 90° integral.)<br>
<br>
<br>
<br>
Few recommendation: <br>
<br>
- have a look on the data in step by step (using the Tx Output Multiplexed for Matlab/Labview with many input for example) <br>
<br>
- Check that both the output of both "filters" (angle computed from gyro and accel)<br>
<br>
- remember to check that the algorithm is executed within one time step time! (Many solution to check that the algorithm comply with the real time constraint with the blockset)<br>
<br>
<br>
<br>
<br>
<br>
Anyway, that may be quite a lot of testing (programming, loggind data, reprogramming...)<br>
<br>
 It is much better to log data once and to <strong>do simulation using logged data</strong>. Care about sampling time must be taken while logging data... (Please have a look on the <a href="/wiki/simulink-embedded-target-for-pic/">complementary filter</a> page and feel free to ask question, many point may be not clear, or difficult to understand despite my proficient English level ;-)<br>
<br>
<br>
<br>
<br>
<br>
I would be glad if you make that algorithm working on the spark fun board (The dsPIC blockset demo version gives the possibility to do it).<br>
<br>
<br>
<br>
Once the IMU works, you may consider transforming the floating point algorithm into a fixed point algorithm. That should give you enough power for the stabilisation of the pendulum. (Not sure that complex control algorithm will works with double data type at 1KHz. You also may have the pendulum controller running at a lower rate than the IMU (that would be a multirate simulink model)<br>
<br>
I hope that help !<br>
<br>
<br>
<br>
That is a fun project, I would be happy to have news from it.<br>
<br>
<br>
<br>
Lubin</div>
</article>

