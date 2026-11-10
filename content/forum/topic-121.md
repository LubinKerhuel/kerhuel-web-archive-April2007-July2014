---
title: "Installation problem :("
url: "/forum/topic/121/"
archiveKind: "topic"
---
# Installation problem :(

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p353">
<header><strong>Anonyme</strong><time datetime="2008-05-15 07:44 UTC">2008-05-15 07:44 UTC</time></header>
<div class="forum-post-body">Hi all,<br>
<br>
I have a problem with the installation.<br>
<br>
I have Matlab R2007A and C30 compiler installed in the C:\Programmi\Microchip\MPLAB C30 directory<br>
<br>
<br>
<br>
Before the installation I have used the command: "rtw_alt_pathname('C:\Programmi\Microchip\MPLAB C30\support\gld')"<br>
<br>
After, I have installed the RTWdsPIC (in C:\programmi\DsPIC) without any problem or error.<br>
<br>
<br>
<br>
When I open an example and I build it I have <strong>always</strong> this error:<br>
<br>
<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'Data_Login_Matlab'. MATLAB error message:
Error using ==&gt; rtwgen
--&gt; Error evaluating 'InitFcn' callback of Master block (mask) 'Data_Login_Matlab/Master'. File "C:\Programmi\Dspic\blocks\[b]dsPIC_MASTER_callback.p" not recognizable as a P-file[/b].
--&gt; Error evaluating 'InitFcn' callback of send structured data frame to Matlab / Labview block (mask) 'Data_Login_Matlab/TX Output Multiplexed for Matlab // Labview'. File "C:\Programmi\Dspic\blocks\dsPIC_UART_TX_Labview_Matlab_callback.p" not recognizable as a P-file.
--&gt; Error evaluating 'InitFcn' callback of Configure UART block (mask) 'Data_Login_Matlab/UART Configuration'. File "C:\Programmi\Dspic\blocks\dsPIC_UART_config_callback.p" not recognizable as a P-file.</code></pre><br>
<br>
Also I have tried to change the dir in the simulation--&gt;configuration--&gt;dspic option..... but  it doesn't work :(<br>
<br>
Please help me!<br>
<br>
Thanks a lot.<br>
<br>
Bye ;)</div>
</article>

<article class="forum-post" id="p356">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-15 22:21 UTC">2008-05-15 22:21 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body">Hi Kova,<br>
<br>
<br>
<br>
It seems that you are using a version of the blockset for dsPIC that is not adapted to your matlab version. (so .p files are not recognized)<br>
<br>
You must use a version of the dsPIC blockset that is supported by your matlab version...<br>
<br>
==&gt; use the version of the dsPIC blockset that support Matlab 2007a. This version have the same capabilities than the version that support later matlab version.<br>
<br>
<br>
<br>
Is this solving the problem ?</div>
</article>

<article class="forum-post" id="p358">
<header><strong>Anonyme</strong><time datetime="2008-05-16 05:47 UTC">2008-05-16 05:47 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>Is this solving the problem ?</blockquote><br>
<br>
Hi LubinKerhuel,<br>
<br>
thanks for the answer ;) <br>
<br>
<br>
<br>
I have update my Matlab to R2008A version!<br>
<br>
Now the Data_Login_Matlab and dsPIC_33f_Explorer16<strong> works perfectly</strong>  :D <br>
<br>
But the Servo_ADC example give me this error:<br>
<br>
<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'Servo_ADC'. MATLAB error message:
Error using ==&gt; genMakefileAndBuild at 1138
Error(s) encountered while building model "Servo_ADC".</code></pre><br>
<br>
and Servo_Sinus gives me a nag error screen:<br>
<br>
"<strong>The left hand side is initialized and has an empty range of indices. However, the right and side returned one or more results.</strong>"<br>
<br>
<br>
<br>
And also this error:<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'Servo_Sinus'. MATLAB error message:
Error using ==&gt; genMakefileAndBuild at 1138
Error(s) encountered while building model "Servo_Sinus".</code></pre><br>
<br>
Another question:<br>
<br>
I want to do a notch filter with a dsPIC for an university project.<br>
<br>
The scheme is: <br>
<br>
<strong>Matlab ECG signal --&gt; dsPIC filter ---&gt; Matlab Graph</strong><br>
<br>
Is it possible to do this?<br>
<br>
I don't want to create and flash effectly the dsPIC with the hex..but I want only simulate the dsPIC and visualize on Matlab the result post filter.<br>
<br>
<br>
<br>
Thanks a lot for your time.<br>
<br>
Sorry for my english.<br>
<br>
Bye ;)</div>
</article>

<article class="forum-post" id="p359">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-16 18:59 UTC">2008-05-16 18:59 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body">Hi kova,<br>
<br>
<br>
<br>
Could you provide the complete compilation message (including the error) ?<br>
<br>
<br>
<br>
Note that he last version of the C30 compiler (V 3.10 and 3.10b)  is not supported yet. It seems that microchip has changed the repertory where some difinition files are stored. This change make the matlab script unable to compile a smulink model.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p365">
<header><strong>Anonyme</strong><time datetime="2008-05-17 05:53 UTC">2008-05-17 05:53 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>Could you provide the complete compilation message (including the error) ?<br>
</blockquote><br>
<br>
Hi Lubin,<br>
<br>
thanks for the answer ;)<br>
<br>
I have solved my problem and now works all perfectly....thanks a lot :P <br>
<br>
<br>
<br>
For my second question, some indication?  :P <br>
<br>
<br>
<br>
Thanks <br>
<br>
Bye ;)</div>
</article>

<article class="forum-post" id="p366">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-17 10:01 UTC">2008-05-17 10:01 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body">Hi Kovak,<br>
<br>
<br>
<br>
It would be interesting to get your solution to the problem ! <br>
<br>
<br>
<br>
For the second question <br>
<blockquote><header class="quote-author">Citation : Guest</header>I want to do a notch filter with a dsPIC for an university project.<br>
<br>
The scheme is:<br>
<br>
Matlab ECG signal --&gt; dsPIC filter ---&gt; Matlab Graph<br>
<br>
Is it possible to do this?<br>
<br>
I don't want to create and flash the dsPIC with the hex..But I want only simulate the dsPIC and visualize on Matlab the result post filter.</blockquote><br>
<br>
I do not understand the problem: <br>
<br>
If you do not want to "flash the dsPIC with the .hex" file, why do you want to generate this .hex file ? Do you want to use a dsPIC Simulator to load the .hex file, simulate the behavior and get the result in matlab ? <br>
<br>
<br>
<br>
When you use Simulink to program a dsPIC, the .hex file obtained will behave like the Simulink model (.mdl file). Simulating the behavior of the .hex file is similar to run a simulation with simulink. That is why programming dsPIC with Simulink and Real Time Workshop is very powerful.<br>
<br>
<br>
<br>
Have a look on the <a href="/RTWdsPIC/examples/IMU.html">IMU</a> I am working on. On this example, I get raw data from the electronics (I get my data vector in matlab, like your ECG signal). Then, I design the IMU calculation using Simulink with my data. Last, I make few changes on the simulation model (replace model's simulation input by dsPIC input) and generate the .hex file that will have the same behavior as the model (If real time constraints are respected).<br>
<br>
<br>
<br>
Hope that I respond to the question!</div>
</article>

<article class="forum-post" id="p367">
<header><strong>Anonyme</strong><time datetime="2008-05-17 10:04 UTC">2008-05-17 10:04 UTC</time></header>
<h3>Re: Installation problem :(</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>Hope that I respond to the question!</blockquote><br>
<br>
Perfectly!<br>
<br>
Thank you very much for the help!!  :P  :P</div>
</article>

