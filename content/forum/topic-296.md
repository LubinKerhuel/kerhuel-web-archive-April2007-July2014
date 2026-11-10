---
title: "sparkfun - UAV v2 Development Platform - dspic30f4011"
url: "/forum/topic/296/"
archiveKind: "topic"
---
# sparkfun - UAV v2 Development Platform - dspic30f4011

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1173">
<header><strong>zafer</strong><time datetime="2010-04-22 06:21 UTC">2010-04-22 06:21 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I and my friends are working on a mini helicopter uav project. We bought an open source uav development board of sparkfun. But there are a lot of codes about this. I think simulink is more user friendly. Then I came across your blockset and I have very big smile on my face until now  :D  I tried your examples (servo sinus, servo adc etc.) and they all worked. I know this 6 I/O is not enough for me, for now I am working on the blocksets,trying to understand, after having some experiance, it will be necessary for me to have 10 I/O. Now I have a problem. <br>
<br>
<br>
<br>
My development board has 3 axis gyro and accelerometers, 4 radio inputs and 3 servo outputs. As you can see from the hardware description of dev board I attached, I3 and I4 pins are OC pins. When I use OC block, I can use only these 2 pins for my servo outputs. How can I have my servo PWM outputs from 3 servo out pins?<br>
<br>
<br>
<br>
Sincerely</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/325-GPSUAV2Manual_v29.doc">Pièce jointe : GPSUAV2Manual_v29.doc</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/326-UAV_v29.pdf">Pièce jointe : UAV_v29.pdf</a></p>
</article>

<article class="forum-post" id="p1174">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-22 06:34 UTC">2010-04-22 06:34 UTC</time></header>
<h3>Re: dspic30f4011</h3>
<div class="forum-post-body">Hi Zafer,<br>
<br>
<br>
<br>
This board seems very nice for many projects. <br>
<br>
<br>
<br>
I quickly read of the doc; why don't you use the PWM motor block to generate PWM for servo motor?<br>
<br>
You get O1 O2 and O3 pins wired as I understand it.<br>
<br>
As the duty cycle is fixed for servo motor to 20ms, PWM motor peripheral should be perfect. (It is even better than OC peripheral)<br>
<br>
You can also use booth: two servo on OC peripheral, and the last one on PWM motor peripheral...<br>
<br>
<br>
<br>
Let me know if you encounter problems. <br>
<br>
I am interested by your project. Are you going to publish it somewhere?<br>
<br>
You may find similar project I started few years ago: <a href="/wiki/miniature-inertial-measurement-unit-imu/">http://www.kerhuel.eu/wiki/Miniature_In ... Unit_-_IMU</a>.<br>
<br>
Sparkfun board is better!<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1184">
<header><strong>zafer</strong><time datetime="2010-04-26 14:23 UTC">2010-04-26 14:23 UTC</time></header>
<h3>Re: dspic30f4011</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
First, thank you very much for your quick response. <br>
<br>
As you said, you can use this board for many project. Normally this board is designed for fixed wing uav autopilot applications and you can easily find its open source files in the internet. But we decided to use uavdevboard on a ccpm (cyclic collective pitch mixing) helicopter and if we succeed, it is a dream but we will try something intelligent like cooperative flight of 3 or more helicopters.<br>
<br>
<br>
<br>
Now, here is my question again.<br>
<br>
1. You said I could use PWM motor block for servo outputs, I still can not have any outputs from servo outputs. On the model which I attached, I have moving servos from the OC channels and they look fine but I still can not have any outputs from servo output ports.<br>
<br>
As you said I get O1 (PWMH1, RE1), O2 (PWMH2, RE3) and O3 (PWMH3, RE5) pins. For example in Digital output write, we assign the output port like RE1 or RE3. Do i forget to assign my PWM ports like that or something else? I am confused.<br>
<br>
<br>
<br>
2. In the picture I uploaded, you can see that there is nothing above input enable selection, I mean I can not select PWM 1 or PWM 2.<br>
<br>
<br>
<br>
Thank you very much again, I am looking forward to have your answer.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/329-servo%20adc.JPG">Pièce jointe : servo adc.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/330-Servo_ADC.mdl">Pièce jointe : Servo_ADC.mdl</a></p>
</article>

<article class="forum-post" id="p1185">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-26 17:11 UTC">2010-04-26 17:11 UTC</time></header>
<h3>Re: dspic30f4011</h3>
<div class="forum-post-body">Hello, I noticed few things.<br>
<br>
<br>
<br>
Please try the following modification :<br>
<br>
<br>
<br>
First of all, change OC1max variable (used for normalizing signals) :<br>
<br>
For OC (HW) block, you must use OCmax variable (is set to 9999 in matlab workspace)<br>
<br>
For PWM motor block, you must use PWM (is set to 40000 in matlab workspace)<br>
<br>
<br>
<br>
If you have a scope, do you have a signal on the PWM motor output block?<br>
<br>
If you have a servo, does the servo try to get on the extreme position (because of the normalization error here)<br>
<br>
If so, it should works now with the correction above.<br>
<br>
<br>
<br>
If not, there is something else wrong, I have no idea now but I would be interested to determine what happening there ; That may be a bug from the blockset ! (I hope not)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1186">
<header><strong>zafer</strong><time datetime="2010-04-27 07:18 UTC">2010-04-27 07:18 UTC</time></header>
<h3>Re: dspic30f4011</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
You are great !!! I tried the modifications you said and now servos are dancing  :D <br>
<br>
Again thank you very much for your quick response. We will be in touch during the project. Your blockset showed the shortcut  :o</div>
</article>

<article class="forum-post" id="p1188">
<header><strong>LubinKerhuel</strong><time datetime="2010-04-27 08:33 UTC">2010-04-27 08:33 UTC</time></header>
<h3>Re: sparkfun - UAV v2 Development Platform - dspic30f4011</h3>
<div class="forum-post-body">Good to see it working.<br>
<br>
<br>
<br>
You will be able to focus on the interresting part now (that's one of the reason why I created  that blockset, when I discovered I spent more time on programming problem than math problems...)<br>
<br>
The wiki is open for you if you wish to publish results in a pretty way.<br>
<br>
<br>
<br>
Lubin</div>
</article>

