---
title: "Some help needed model for self-balancing"
url: "/forum/topic/109/"
archiveKind: "topic"
---
# Some help needed model for self-balancing

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p294">
<header><strong>micman2</strong><time datetime="2008-04-19 12:31 UTC">2008-04-19 12:31 UTC</time></header>
<div class="forum-post-body">Hi ,<br>
<br>
I am trying to work with IMU , work very well.<br>
<br>
In my system I have :<br>
<br>
Angle<br>
<br>
Angle rate<br>
<br>
Meters (encoder apply in motor)<br>
<br>
Meters/sec<br>
<br>
<br>
<br>
I need a model LQR in simulink for balancing robot  :?:</div>
</article>

<article class="forum-post" id="p303">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-24 22:26 UTC">2008-04-24 22:26 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Hi, <br>
<br>
<br>
<br>
I guess that you need a state space model. LQR is the method to compute your controller (the K gain).<br>
<br>
State space model can be done very easily using simulink using only gain blocks (that can make calculation with vectors and matrix) and a block 1/s or 1/z depending if you are modeling your system in continuous time or discrete time.<br>
<br>
<br>
<br>
To implement the state space model (observator and controller) on a dsPIC, you must use a discrete time model...<br>
<br>
<br>
<br>
Simulink fixed point optimization system will then give you the possibility to implement your calculation in fixed point rather than using floating point calculation. Even fixed point 32 bit calculation is faster than single or double calculations.<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p304">
<header><strong>micman2</strong><time datetime="2008-04-25 13:33 UTC">2008-04-25 13:33 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Hi ,<br>
<br>
Thanks you for your answer.<br>
<br>
<br>
<br>
The state space model is: (screen)<br>
<br>
<br>
<br>
<br>
<br>
I have taken int the site <br>
<br>
<a href="http://robotics.ee.uwa.edu.au/theses/2003-Balance-Ooi.pdf">http://robotics.ee.uwa.edu.au/theses/20 ... ce-Ooi.pdf</a><br>
<br>
<br>
<br>
How can implement it in simulink, thanks to the availability<br>
<br>
<br>
<br>
Michele</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/52-MWSnap.gif">Pièce jointe : MWSnap.gif</a></p>
</article>

<article class="forum-post" id="p308">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-26 14:06 UTC">2008-04-26 14:06 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I could not open the pdf link you provide ; so I realized the model in discret time on simulink (Te = 1ms) :<br>
If you want a model in continuous time, change 1/z with a block 1/s. You also have to change the Az,Bz,Cz,Dz and K coefficient to their continuous time equivalent.<br>
<br>
<br>
<br>
I made few assumption and compute a controllor to stabilize the angular position of the "pendulum".<br>
<br>
The position is not controlled.<br>
<br>
I assume that only the angle of the "pendulum" is measured.<br>
<br>
<br>
<br>
Note that this controllor will not work in "real life". You need to add an observator to estimate the internal state of your model or to add enough sensors to measure all internal states. Also, before implementing it, you will probably need to convert the calculation into a fixed point in order to get all calculation finished within the sampling time choosen (1ms here).<br>
<br>
<br>
<br>
The script is : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt;clear all;
close all;
<wbr>
Te=1e-3;    %% discret time
% Robot's model (continuous time)
A = [0 1 0 0 ; 0 -0.0097 11.1591 0 ; 0 0 0 1 ; 0 -0.0293 172.116 0 ];   % robot's dynamic
B = [0 1 0 0]';  % input : suppose you can apply a translating force on the robot ?
C = [0 0 1 0]; % Measurement : suppose you measure the angle
D = 0 ;     %% this is probably not 0 ?
<wbr>
Robot_s = ss(A,B,C,D);
<wbr>
%% Discretizing :
Robot_z = c2d(Robot_s,Te,'tustin');
[Az,Bz,Cz,Dz,Ts]=ssdata(Robot_z);
<wbr>
rank(obsv(Robot_s)) %% System not observable but
rank(ctrb(Robot_s)) %% controllable
<wbr>
%% LQR synthesis
R=1;
Q = diag([0 1e-2 1 1e-3]);  % you must find the best ponderation ...
[K,S,e] = dlqr(Az,Bz,Q,R);
Poles_s = log(abs(eig(Az-Bz*K)))/Te   % en continue 
</code></pre><br>
<br>
Find the model and the script file that must be run first.<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/53-ModeleRobot.png">Pièce jointe : ModeleRobot.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/54-BalancingRobot.mdl">Pièce jointe : BalancingRobot.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/57-Robot_Script.m">Pièce jointe : Robot_Script.m</a></p>
</article>

<article class="forum-post" id="p309">
<header><strong>micman2</strong><time datetime="2008-04-26 14:35 UTC">2008-04-26 14:35 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Hi ,<br>
<br>
Thanks you for your answer.<br>
<br>
<br>
<br>
Opss the link not work excuse me, I upload the document in the forum.<br>
<br>
<br>
<blockquote>Note that this controllor will not work in "real life". You need to add an observator to estimate the internal state of your model or to add enough sensors to measure all internal state</blockquote><br>
<br>
Yes, but is implement another  sensor, angle, rate angle, encoder position of wheel and velocity and is describe in state space<br>
<br>
<br>
<br>
mistake?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/58-2003-Balance-Ooi.pdf">Pièce jointe : 2003-Balance-Ooi.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/59-grasser_darrigo_colombi_rufer_ieee_02.pdf">Pièce jointe : grasser_darrigo_colombi_rufer_ieee_02.pdf</a></p>
</article>

<article class="forum-post" id="p310">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-26 15:36 UTC">2008-04-26 15:36 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">If you have all sensor and if they are not too noisy, it may work  :) <br>
<br>
<br>
<br>
The state space model must be correct otherwise the controllor will not be adapted.<br>
<br>
<br>
<br>
I modify the B vector that I missed up on the previous script. With this new vector, the position of the robot can be controlled.<br>
<br>
I also set the sampling time to 0.02s (50Hz) to have the same parameters than the Thesis of Richi Chi Ooi.<br>
<br>
<br>
<br>
The script modification are the following : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt;...
Te=2e-2;    %% discret time
...
B = [0 0.0815 0 0.2456]';  % input : suppose you can apply a translating force on the robot ?
...
Q = diag([5e1 0 1e-2 0]);  % you must find the best ponderation ...
...
</code></pre><br>
<br>
Note that at a sampling rate of 20ms, you will have time to get all calculation done within few ms (&lt; 20ms) without problem in double precision in a dsPIC. Thus, you could directly use the dsPIC blockset to implement the calculation onboard your chip, making the design process fast.<br>
<br>
<br>
<br>
<br>
<br>
New script and simulink model :<br>
<br>
<br>
If you implement this on a real robot, I would be interrested to see the results and the parameters you tune...</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/60-BalancingRobot.mdl">Pièce jointe : BalancingRobot.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/61-Robot_Script.m">Pièce jointe : Robot_Script.m</a></p>
</article>

<article class="forum-post" id="p311">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-26 15:44 UTC">2008-04-26 15:44 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Oups, mistakes,<br>
<br>
<br>
<br>
zoh method must be used to discretize the model, not tustin (becaue input is fixed for 20ms). The parameters for the Q vector changes.<br>
<br>
<br>
<br>
the script is :</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/62-Robot_Script.m">Pièce jointe : Robot_Script.m</a></p>
</article>

<article class="forum-post" id="p511">
<header><strong>mecch</strong><time datetime="2008-09-09 11:15 UTC">2008-09-09 11:15 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">I justed tested the embedded coder robot toolbox on the Lego mindstorm NXT platform for a self-balancing robot with one gyro sensor. The performance is quite good. The implementation details are well described in the attached document. Since It also uses the embedded coder for code generation, it will be very helpful.  <br>
<br>
<a href="http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=13399&amp;objectType=File">http://www.mathworks.com/matlabcentral/ ... tType=File</a><br>
<br>
<br>
<br>
Chen</div>
</article>

<article class="forum-post" id="p512">
<header><strong>micman2</strong><time datetime="2008-09-09 12:04 UTC">2008-09-09 12:04 UTC</time></header>
<h3>Re: Some help needed model for self-balancing</h3>
<div class="forum-post-body">Thanks!</div>
</article>

