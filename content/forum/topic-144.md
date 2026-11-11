---
title: "Another method of gyro integrating."
url: "/forum/topic/144/"
archiveKind: "topic"
---
# Another method of gyro integrating.

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

27 message(s) · archive en lecture seule

<article class="forum-post" id="p454">
<header><strong>NigmaTech</strong><time datetime="2008-08-13 15:38 UTC">2008-08-13 15:38 UTC</time></header>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
I've created my own method of using gyro and accelerometer to measure tilt. On the begining I was using ADXRS150EB from Analog Devices gyros, but they were failure (manufacturer delivered two times broken units). Now I'm using 2-axial IDG-300 from InvenSense, and MMA7260Q accelerometer from Freescale. Both units has got internal temperature compensation. Unfortunately using VREF to compensate gyro drift is producing greater noises. To measure angles of tilt i've created following model:<br>
<br>
<br>
<br>
<br>
AN_11 - X-axis of accelerometer<br>
<br>
AN_7 - Z-axis of accelerometer<br>
<br>
AN_8 - Y-axis of gyroscope (on the picture is GYRO_X - thats bug)<br>
<br>
<br>
<br>
I'm filtering data using one of yours filters. After start dsPIC is waiting 5 seconds for stabilization our sensors. 5 sec. after start last value logged inside Calibrating block in "Data Store Memory" (ACC_X, GYRO_X), is used inside next block to calibrate data's from Accelerometer and gyroscope. Value inside ACC-Z is loaded manually. Using atan2 function we're computing actual angle from accelerometer. Data from gyro is inntegrated using Accumulation: Forward Euler method. Sum block permits to measure drift in relate to angle from accelerometer. Value inside Gain1 block permits to increse or decrease sensitivity of our gyro_combo, and  a bit lets us to control horizontal movement sensitivity.<br>
<br>
Unfortunately GIF files with simulation are bigger than 250kB (about 800kB).<br>
<br>
<br>
<br>
What do You think about it Lubin? Have You got any suggestions? Something to correct?<br>
<br>
<br>
<br>
Few examples in JPG's (blue line is a tilt computed using atan2, green is gyro compensated response):<br>
<br>
<br>
<br>
Gain 0.01:<br>
<br>
<br>
Gain 0.003:<br>
<br>
<br>
Gain 0.001:<br>
<br>
<br>
How you see, large values of gain has an effect on large values of phase lead, but on large values of overshoot too.<br>
<br>
Any ideas how to damp overshoots?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/106-Accelero_Gyro_Combo.jpg">Pièce jointe : Accelero_Gyro_Combo.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/107-Accelero_Gyro_Combo.mdl">Pièce jointe : Accelero_Gyro_Combo.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/108-Gain_001.jpg">Pièce jointe : Gain_001.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/109-Gain_01.jpg">Pièce jointe : Gain_01.jpg</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/110-Gain_003.jpg">Pièce jointe : Gain_003.jpg</a></p>
</article>

<article class="forum-post" id="p455">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-13 17:48 UTC">2008-08-13 17:48 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
It's nice to hear from you.<br>
<br>
I guess that you manage with the compilation problem you described earlier ;-)<br>
<br>
<br>
<br>
Thanks for sharing this work.<br>
<br>
<br>
<br>
I have only one remark, but as I can't simulate it, you will have to check if I am right :<br>
<br>
The low pass filter applied to the gyro may be useless because the integrator already acts as a low pass filter. You may remove it so as to not add phase lag to the system.<br>
<br>
<br>
<br>
The method you describe looks like the one that was described by Pisano (2005) (but I did not manage to get the original paper!)<br>
<br>
This filtering method works fines, but when the gyro drift, a static error remains on the angle estimation. I did simulation recently including this method ("Pisano") and I am about to update the IMU page. Feel free to add your comment on this page or on the related discussion page. (Login first on the wiki)<br>
<br>
<a href="/wiki/miniature-inertial-measurement-unit-imu/">http://www.kerhuel.eu/wiki/Miniature_In ... Unit_-_IMU</a><br>
<br>
<br>
<br>
I obtain the best results using a structure with a non adaptative kalman structure or with a complementary filter of order 2. (try to publish it online soon!)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p459">
<header><strong>NigmaTech</strong><time datetime="2008-08-14 11:12 UTC">2008-08-14 11:12 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">I've updated this post. New pictures.  :)</div>
</article>

<article class="forum-post" id="p468">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-19 15:15 UTC">2008-08-19 15:15 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
It's a nice work. Note that .png picture format is the best one for simple graph like the one you uploaded. <br>
<br>
<br>
<br>
I add few remarks hopping that it may help.<br>
<br>
<br>
<br>
- Overshoot is not due to the low pass filter (Filtering here at 30 rad/s ; about 5hz)<br>
<br>
- I did not see the calibration of the gyro gain. You may add a gain to obtain the angular rotation speed in a know range. When calibrating the gyro, be careful to precision loss (for example, if you scale gyro with degree/s, use either a fixed point or double variable rather than an int16 data type.<br>
<br>
This calibration step may solve the overshoot problem.<br>
<br>
<br>
<br>
- The static difference between the angle estimated from the accelerometers and the reconstructed angle from gyro and accelero should converge toward 0. It seems to remain to a value of about 4-5° here. (Also, calibration of the gyro gain may solve it)<br>
<br>
<br>
<br>
With the calibration done on the accelerometer X axe, the IMU must be at an angle of 0° at initialization time.<br>
<br>
In fact, I am not sure that calibration on the accelerometers is necessary.<br>
<br>
<br>
<br>
Not published yet my simulation works, I will try to work at it...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p473">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-20 19:30 UTC">2008-08-20 19:30 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Webpage partly updated. Please have a look and download the simulink file that may help for your projects.<br>
<br>
<br>
<br>
<a href="/wiki/miniature-inertial-measurement-unit-imu/">http://www.kerhuel.eu/wiki/Miniature_In ... U#Download</a><br>
<br>
<br>
<br>
Another look to your structure, I do not understand it. I guess that Gain1 should be the gain of the rate gyro being integrated. Another gain may be added in the feedback loop to control convergence speed. Btw, any gyro bias will produce a static error in the angle estimation (it may be small, depending on the parameters used)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p474">
<header><strong>NigmaTech</strong><time datetime="2008-08-21 08:22 UTC">2008-08-21 08:22 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I've got folowing error when trying to open IMU_Simulation.mdl:<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/111-error.jpg">Pièce jointe : error.jpg</a></p>
</article>

<article class="forum-post" id="p475">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-21 11:44 UTC">2008-08-21 11:44 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">I removed the 'french caracter'. Is it Ok now ?</div>
</article>

<article class="forum-post" id="p527">
<header><strong>NigmaTech</strong><time datetime="2008-09-24 20:24 UTC">2008-09-24 20:24 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
How to use subsystem block "Simplified Kalman for publi" from IMU_Simulation.mdl ??<br>
<br>
<br>
<br>
<br>
Where is definied matrix Az, Ts, Kz... ?? How to use it?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/113-Bez%20nazwy.jpg">Pièce jointe : Bez nazwy.jpg</a></p>
</article>

<article class="forum-post" id="p528">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-24 21:02 UTC">2008-09-24 21:02 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
The script <strong>Script_Kalman.m</strong> define theses constants.<br>
<br>
<br>
<br>
The block "<em>Simplified Kalman for publi</em>" is a simplified version of the block that is really implemented in my IMU.<br>
<br>
<br>
<br>
Despite the IMU described is already working well, it is still under developpment.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p529">
<header><strong>NigmaTech</strong><time datetime="2008-09-24 21:37 UTC">2008-09-24 21:37 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
How to compile the file? I have the following error:<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/115-error.png">Pièce jointe : error.png</a></p>
</article>

<article class="forum-post" id="p530">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-24 21:54 UTC">2008-09-24 21:54 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma !<br>
<br>
<br>
<br>
You have a datatype error. The easiest way to make it works is to do all calculation in double (i.e. open each block ans set data type to double, or use the Simulink Fixed point tool to do all at once...)<br>
<br>
<br>
<br>
If you with to do the calculation in fixed point, avoid to get a fixed point calcul or result data length greater than 32 bits (This is the error shown on your post)<br>
<br>
<br>
<br>
Anyway, the model <strong>IMU_dsPIC_30f4012_AlphaBetaFilter_20Mips.mdl</strong> implement a floating point version of the filter and the model  <strong>IMU_dsPIC_30f4012_AlphaBetaFilter_20Mips_FixedPoints.mdl</strong> implement a fixed point version, booth for dsPIC 30f4012 (you can compile it, remove few input/output if you are using the dsPIC blockset demo version limited to 6 Input/Output)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p531">
<header><strong>NigmaTech</strong><time datetime="2008-09-24 22:39 UTC">2008-09-24 22:39 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
Could you to correct my model? I've compiled it, but dsPIC still displays value -1 on figure (via RS-port), durring random move of IMU. Whats wrong?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/116-Accelero_Gyro_Combo_Lubins_Kalman.mdl">Pièce jointe : Accelero_Gyro_Combo_Lubins_Kalman.mdl</a></p>
</article>

<article class="forum-post" id="p532">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-25 09:05 UTC">2008-09-25 09:05 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
I see at least 1 error in the model: <br>
<br>
<br>
<br>
- The gyro MUST NOT be integrated before the "Non adaptive Kalman block". The gyro in already integrated in this block.<br>
<br>
<br>
<br>
I could give then few advices : <br>
<br>
- It is useless to low pass filter the Gyro before the "Non adaptive Kalman block" because this block already does it.<br>
<br>
- Same for the Accelerometers. The state space observer takes care of it.<br>
<br>
<br>
<br>
- Why don't you use the UART at a speed of 57600 ? This baud rate is compatible with your 10Mips configuration.<br>
<br>
- You should consider using many input of the Tx Output Multiplexed for Matlab/Labview to monitor intermediate variables<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p533">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 09:55 UTC">2008-09-25 09:55 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">I've removed integrator block before Kalman, Low Pass filters too and nothing changes. dsPIC still displays value "-1" on figure. I'm using 9600 baud rate because when I'm trying to set faster rate, Matlab displays error durring connection:<br>
<br>
<br>
<br>
??? Attempted to access s_control_pos(1); index out of bounds because<br>
<br>
numel(s_control_pos)=0.<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program<br>
<br>
Files\MATLAB\R2007b\pic\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 75<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program<br>
<br>
Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;pushStart_Callback at 254<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;rs232gui<br>
<br>
at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback<br>
<br>
<br>
<br>
??? Error using ==&gt; serial.fprintf at 143<br>
<br>
An error occurred during writing.<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program<br>
<br>
Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;pushConnexion_Callback at 121<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;rs232gui<br>
<br>
at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback<br>
<br>
<br>
<br>
I asked you several times about it, but you didn't answer me.</div>
</article>

<article class="forum-post" id="p534">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-25 10:04 UTC">2008-09-25 10:04 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
Matlab use a Java interface to access to the COM port. This interface sometimes bug while trying to connect. In this case, you should press the connect button with the dsPIC off or at least not sending datas. But it seems that you got another error. This may be due to your specific UART PC port.<br>
<br>
<br>
<br>
If you get always the same valueof -1 (which is all 1 in binary), you should try to send directly the ADC result to the UART block to check that UART transmission is working properly. (or try to send a counter, sine wave or whatever. Check the example directory)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p535">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 11:07 UTC">2008-09-25 11:07 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">This error appers, just when I'm starting sending data from dsPIC to Matlab (not durring connecting):<br>
<br>
<br>
<br>
??? Attempted to access s_control_pos(1); index out of bounds because<br>
<br>
numel(s_control_pos)=0.<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program<br>
<br>
Files\MATLAB\R2007b\pic\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 75<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program<br>
<br>
Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;pushStart_Callback at 254<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; D:\Program Files\MATLAB\R2007b\pic\blocks\rs232gui.p&gt;rs232gui<br>
<br>
at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback<br>
<br>
<br>
<br>
redefinition SerialCOM<br>
<br>
<br>
<br>
_______________________________________________________________<br>
<br>
<br>
<br>
To communicate dsPIC and PC I'm using BlueSMIRF module, from Sprakfun:<br>
<br>
<br>
<br>
<a href="http://www.felix-beck.de/diplom/blog/2007/03/26/bluesmirf/">http://www.felix-beck.de/diplom/blog/20 ... bluesmirf/</a><br>
<br>
<br>
<br>
_______________________________________________________________<br>
<br>
<br>
<br>
Data sended directly from ADC to UART (9600 baud rate):<br>
<br>
<br>
<br>
<br>
Sine wave:<br>
<br>
<br>
<br>
<br>
Mybe I'm doing something wrong durring compilation? First I'm running Script_Kalman.m file:<br>
<br>
<br>
<br>
<br>
Matlab displays:<br>
<br>
<br>
<br>
Poles_s =<br>
<br>
<br>
<br>
  -0.5000 + 0.8660i<br>
<br>
  -0.5000 - 0.8660i<br>
<br>
<br>
<br>
Discrete<br>
<br>
<br>
<br>
and, now I'm starting "Incremental build". After writing program to dsPIC I see something that:<br>
<br>
<br>
<br>
<br>
Durring random move of IMU.   :cry:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/117-direct.png">Pièce jointe : direct.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/118-sine.png">Pièce jointe : sine.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/119-run.png">Pièce jointe : run.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/120-cry.png">Pièce jointe : cry.png</a></p>
</article>

<article class="forum-post" id="p537">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 14:07 UTC">2008-09-25 14:07 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">OK, Kalman is working, but something's going wrong. <br>
<br>
1. IMU can't be longer than 1-2 seconds in near-horizontal position. If it happened figure displays value "-1" and do not move any more. I must to reset dsPIC. <br>
<br>
<br>
<br>
2. There is still drift.</div>
</article>

<article class="forum-post" id="p538">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 14:31 UTC">2008-09-25 14:31 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">The same error appears during using Complementary filter.</div>
</article>

<article class="forum-post" id="p539">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-25 14:48 UTC">2008-09-25 14:48 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma, is gyro calibration OK ? signal should be in degree/s</div>
</article>

<article class="forum-post" id="p540">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 14:48 UTC">2008-09-25 14:48 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">It looks that:<br>
<br>
<br>
<br>
<br>
Lines:<br>
<br>
<br>
<br>
Blue - integrated data complementary filtered<br>
<br>
Green - accelerometer X-axis<br>
<br>
Red - accelerometer Z-axis<br>
<br>
and this color between blue and green - gyroscope Y  :wink:</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/121-strange.png">Pièce jointe : strange.png</a></p>
</article>

<article class="forum-post" id="p541">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 14:56 UTC">2008-09-25 14:56 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">How do You think, what's the reason of this behavior?</div>
</article>

<article class="forum-post" id="p542">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-25 17:34 UTC">2008-09-25 17:34 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
I am glad to see that you manage to works with the blockset and with the data viewer "rs232gui"  interface.<br>
<br>
I hope you are enjoying dealing now with the interesting part.<br>
<br>
<br>
<br>
I faced the problem you describe: <br>
<br>
<br>
<br>
If you use only one transfer function to filter and integrate the rate gyro, you may have an internal variable (in the transfer function block) that saturates. This is due to the fact that the transfer function may integrate first the gyro and then apply the high pass filter; thus, the result of the integration will saturate after few seconds or minutes.<br>
<br>
The solution is to "cut" the transfer function into two parts: one high pass filter and one integration and to have them in a serial form starting with the high pass filter. <br>
<br>
This solution is better but certainly not full proof. Note than even if the integral value is not saturated, it will reach high value that will lower the resolution of the overall calculation (due to floating point calculation)<br>
<br>
Check on a long time run your IMU before using it on a flying machine !<br>
<br>
<br>
<br>
The last fixed point state space model in the model <strong>IMU_dsPIC_30f4012_AlphaBetaFilter_20Mips_FixedPoints.mdl</strong> works well during a long time.<br>
<br>
<br>
<br>
Btw, what component are you dealing with? Are you using a sparkfun module with 2 gyro and 3 accelerometers?<br>
<br>
<br>
<br>
I will be out for 3 days and will not be able to provide more response. I hope this help !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p544">
<header><strong>NigmaTech</strong><time datetime="2008-09-25 18:13 UTC">2008-09-25 18:13 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">I'm using:<br>
<br>
<br>
<br>
<a href="http://www.sparkfun.com/commerce/product_info.php?products_id=252">http://www.sparkfun.com/commerce/produc ... cts_id=252</a><br>
<br>
<br>
<br>
and<br>
<br>
<br>
<br>
<a href="http://www.sparkfun.com/commerce/product_info.php?products_id=698">http://www.sparkfun.com/commerce/produc ... cts_id=698</a></div>
</article>

<article class="forum-post" id="p761">
<header><strong>Tchangov</strong><time datetime="2009-02-13 20:02 UTC">2009-02-13 20:02 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma (and Lubin)...<br>
<br>
<br>
<br>
The Integrator (Discrete-Time has a Cte = 0.003 i.e. Time Cte = 1/0.003 = 333s.<br>
<br>
Analyze the (SubSystem Feedback) from (In = Output SubSys3) to the (Out= Summing point) from Acc and Gyro:<br>
<br>
<br>
<br>
The G = 0.003 represents the “speed of integration”  - very slow; <br>
<br>
The Feed back is Unity  - Write the Transf Function....Drastically slow dynamic design. (or LOWLOWLOW PASS-never Pass filter).<br>
<br>
<br>
<br>
As Lubin said there is no convergence to Zero Compensation, which is due to slow work of the Integrator.<br>
<br>
<br>
<br>
If you stay long enough time, then the Acc and Gyro sum will be Zeroed by the integrator. Right now the SubSystem including the Integrator have to stay –study state for 5 X 333s = 1666 s = 27 minutes (for 2% accuracy) in order to see it …it is working. <br>
<br>
<br>
<br>
Yes, it works but extremely slow, practically slower than the Gyro Drift.<br>
<br>
<br>
<br>
This is actually the place for Observer-Kalman…you name it.<br>
<br>
<br>
<br>
<br>
<br>
( Another minor think – the previous DIG Low past filter for the Gyro should  be different.)<br>
<br>
<br>
<br>
It is only a hope that this will be (one of the) problem.        <br>
<br>
Back to Simulation…the rest is easy.<br>
<br>
Don't forget to have funnnnn!<br>
<br>
Todor</div>
</article>

<article class="forum-post" id="p853">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-18 21:33 UTC">2009-05-18 21:33 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Nigma, <br>
<br>
<br>
<br>
Is there any news on the ongoing IMU project ?</div>
</article>

<article class="forum-post" id="p865">
<header><strong>NigmaTech</strong><time datetime="2009-06-13 18:46 UTC">2009-06-13 18:46 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
There's nothing new. I've defended my Master's thesis. IMU project is closed (I hope just temporarily).  I'm planning to start new IMU project in a few months and fix one's attention on it only. This time I'm thinking about using 3-Axis Magnetometer from Sparkfun too:<br>
<br>
<br>
<br>
<a href="http://www.sparkfun.com/commerce/product_info.php?products_id=244">http://www.sparkfun.com/commerce/produc ... cts_id=244</a><br>
<br>
<br>
<br>
I've bought it last year (with gyro and accelerometer) as a reserve solution, but never used. <br>
<br>
I'm still thinking about PhD studies but I'm disgusted after team-work with one guy on M.A. Now I must to cool down, maybe next year.<br>
<br>
<br>
<br>
Regards Michael :D</div>
</article>

<article class="forum-post" id="p867">
<header><strong>melodyincognito</strong><time datetime="2009-06-21 08:03 UTC">2009-06-21 08:03 UTC</time></header>
<h3>Re: Another method of gyro integrating.</h3>
<div class="forum-post-body">Hi all!<br>
<br>
Does anyone know how to conpensate gyro drift using particle filter...like there are great resources on the net posted by lubin and many others using 6DOF imu... I want a simulink model doing the same task using particle filter... If anyone has worked on it earlier...kindly share ur work...!<br>
<br>
Thanks!</div>
</article>

