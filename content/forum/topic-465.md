---
title: "Problem with rs232gui"
url: "/forum/topic/465/"
archiveKind: "topic"
---
# Problem with rs232gui

Forum : [bug reports](/forum/#forum-8)

13 message(s) · archive en lecture seule

<article class="forum-post" id="p1764">
<header><strong>alpert</strong><time datetime="2011-12-19 10:50 UTC">2011-12-19 10:50 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
I have a problem with the rs232gui that I'm trying to solve for a long time.<br>
<br>
I'm using a dspic30f4011, but i also tested it with dspic33fj256.<br>
<br>
when I'm trying to start the rs232gui, it stops immediately and show error in the command window.<br>
<br>
<br>
<br>
This is the model that I'm testing:<br>
<br>
(I've tried a lot of models, including sending a constant number)<br>
<br>
<br>
<br>
This is the Error that i get: <br>
<br>
I'm using Matlab 2010b and blockset v3.7<br>
<br>
<br>
<br>
<br>
<br>
What could be the problem?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Alpert</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/455-ex7_uart.mdl">Pièce jointe : ex7_uart.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/456-2011-12-19_124311.jpg">Pièce jointe : 2011-12-19_124311.jpg</a></p>
</article>

<article class="forum-post" id="p1765">
<header><strong>LubinKerhuel</strong><time datetime="2011-12-19 12:43 UTC">2011-12-19 12:43 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Alpert, you might try to press the Raw data button in the rs232gui interface.<br>
<br>
No decoding will be done, you should get 1 control byte, and 1 value 1 control byte, 1 value etc....<br>
<br>
<br>
<br>
Check that control byte is constant value, and that value is moving correctly (as it is an uint8, it does not need "reconstruction".)<br>
<br>
<br>
<br>
<br>
<br>
You might check that your quartz is a 2.5MHz precisely.<br>
<br>
Try removing I2C preipheral for testing UART only (IC2 will create problems if the I2C composant does not respond as it will freeze the software until timout take over the control)<br>
<br>
<br>
<br>
The, try using a higher bandwidth (here, bandwidth is slow, but the UART is fully load as you try to send 2 char within one time step (1 control byte, 1 uint8 value) ) and the baud rate is too slow to send two byes within 1ms.<br>
<br>
Try to get a baud rate for the UART with the lower % error possible (use PLL or change your quartz if necessary).<br>
<br>
<br>
<br>
Note that the protocol used works better when sending several values, and when values are moving (as it makes control byte easier to find out the stream).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1772">
<header><strong>alpert</strong><time datetime="2012-01-03 16:29 UTC">2012-01-03 16:29 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
Thanks for your answer, and by the way, grate job with the blockset! <br>
<br>
I have done a lot of experiments, and eventually I've discovered the problem.<br>
<br>
I have done those steps:<br>
<br>
1) I made a simple program (using your Simulink Blockset) that sand a constant number via the "Tx Output" block (not the gui), and I've set the "UART Configuration" to send at 115200 bps.<br>
<br>
2) I connected my DSPic33 UART to my laptop and i watched the incoming data with "Realterm", and i changed the baud rate until i got on the screen the same number that i have send. The baud rate was <strong>30,000</strong>.<br>
<br>
3) I've made a new program. this time i've sent the data using the "TX Output Multiplexed for Matlab / Labview" block. again,  I've set the "UART Configuration" to send at 115200 bps. then, i opened the rs232gui and i set it to recieve the data at <strong>30,000</strong>. <span style="color:#ff0000"><strong>It worked!!!</strong></span>.<br>
<br>
<br>
<br>
<span class="forum-size"><strong>What could cause the different between the desirable baud rate and the actual baud rate? Why does it send at 30000bps when i set it to 115200?</strong></span><br>
<br>
<br>
<br>
I am attaching a simulink model that sample IMU sensors and send them using the "Tx Output". I'll appreciate if you look at it and see if i've done something wrong.<br>
<br>
<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Alpert.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/458-ex8.mdl">Pièce jointe : ex8.mdl</a></p>
</article>

<article class="forum-post" id="p1784">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 10:01 UTC">2012-01-12 10:01 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Alpert,<br>
<br>
<br>
<br>
With your quartz and no PLL, you get a 1.73% error on the UART baud rate.<br>
<br>
This usually works but might be the problem(depending on your computer's hardware).<br>
<br>
<br>
<br>
Try to activete PLL and find a processor speed that would lower the UART baud rate error (below 1% should be Ok !).<br>
<br>
<br>
<br>
<br>
<br>
"2) I connected my DSPic33 UART to my laptop and i watched the incoming data with "Realterm", and i changed the baud rate until i got on the screen the same number that i have send. The baud rate was 30,000."<br>
<br>
This is weird, but this is not a strong proof as if you're lucky enough, the UART will sample the signal and retrive the pattern corresponding to your constant. Please send an incrementing value and check you get abcdefg.... 12345... ABCD... on realterm. This is much better for testing.<br>
<br>
Let me know if your finding is the same then.<br>
<br>
<br>
<br>
Are you testing the Sparkfun UDB4 board ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1786">
<header><strong>alpert</strong><time datetime="2012-01-12 12:05 UTC">2012-01-12 12:05 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
Thank you for your answer. I'll do some testing tomorrow morning.<br>
<br>
<br>
<br>
I'm using now the sparkfun UDB4, but I have the same problem with the "Gluon Pilot" board.<br>
<br>
<br>
<br>
Alpert.</div>
</article>

<article class="forum-post" id="p1787">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 13:03 UTC">2012-01-12 13:03 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">I am willing to test this board.<br>
<br>
<br>
<br>
First task for me is to embed a bootloader that would be quite practical.<br>
<br>
I am planning to use the ds30 loader... then, using the clock switching option from the blockset, you could use the board very efficiently...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1788">
<header><strong>alpert</strong><time datetime="2012-01-12 13:19 UTC">2012-01-12 13:19 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hello,<br>
<br>
Bootloader for the UDB4 can be very useful !<br>
<br>
I'm not familiar with the clock switching block. I'm not sure that i have it.<br>
<br>
<br>
<br>
Until now I have check the Gyros and the Accelerometers on that board and the works fine. I have a problem withe the I2C, but i still not sure what cause that problem. i need to inspect it.</div>
</article>

<article class="forum-post" id="p1790">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 14:11 UTC">2012-01-12 14:11 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hello Lior,<br>
<br>
<br>
<br>
I get one board. I am willing to use it for personal project but I am quite overloaded right now.<br>
<br>
You have clock switch options (something like) in the Master block.<br>
<br>
<br>
<br>
this board has a 8MhZ quartz, not a 7.5 MhZ ?<br>
<br>
<br>
<br>
I2C is always difficult to set-up!<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1794">
<header><strong>alpert</strong><time datetime="2012-01-12 17:40 UTC">2012-01-12 17:40 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hello,<br>
<br>
I have done another test like you suggested. I've activated  the PLL and I change the baud rate on the "UART Configuration" block, until i got in "Realterm" the same word that i've send from the simulink.<br>
<br>
I've found that i need to set the block to 202700bps if i want it to send in 115200bps.<br>
<br>
<br>
<br>
Here is the model:<br>
<br>
<br>
here is what i got in Realterm:<br>
<br>
<br>
<br>
<br>
Its really weird..</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/464-ex9_led.mdl">Pièce jointe : ex9_led.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/465-2012-01-12_192404.jpg">Pièce jointe : 2012-01-12_192404.jpg</a></p>
</article>

<article class="forum-post" id="p1795">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-12 18:44 UTC">2012-01-12 18:44 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">In Master block, is there any reason why the quartz is set to 14Mhz this time ?<br>
<br>
It should be 8Mhz !<br>
<br>
<br>
<br>
Try to make one led blinking at 1Hz.<br>
<br>
If it's not blinking at 1Hz, you have a problem with the oscillator configuration (thus UART cant be set at the appropriate baud rate)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1801">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-14 23:38 UTC">2012-01-14 23:38 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Lior,<br>
<br>
<br>
<br>
I did very first test with UDB4 board.<br>
<br>
the attach model send Rate gyro and Accelerometers values through UART correctly using appropriate PLL value.<br>
<br>
This is just for testing (plotting sensor in pseudo-real time). Note that baud rate used do not allow logging all 6 axis at 1kHz.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/468-UDB4_TestBoard.mdl">Pièce jointe : UDB4_TestBoard.mdl</a></p>
</article>

<article class="forum-post" id="p1802">
<header><strong>alpert</strong><time datetime="2012-01-15 16:21 UTC">2012-01-15 16:21 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
You were absolutely right about the clock. Yesterday I've done the test that you suggested with the 1Hz led, and i realized that my configuration of the clock were wrong. After i fixed that everything worked fine.<br>
<br>
<br>
<br>
Thank you very much!  You have done really grate job with your block set! <br>
<br>
I hope not to write anymore at this part of the forum (Bug report).<br>
<br>
<br>
<br>
Lior</div>
</article>

<article class="forum-post" id="p1803">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-15 22:20 UTC">2012-01-15 22:20 UTC</time></header>
<h3>Re: Problem with rs232gui</h3>
<div class="forum-post-body">I attached here the binary to use the bootloader <a href="http://mrmackey.no-ip.org/elektronik/ds30loader/">ds30</a> (from Mikael Gustafsson) with the UDB4 board:<br>
<br>
<br>
<br>
==&gt; Load this .hex into the board using classical programmer<br>
<br>
==&gt; then, use the ds30 GUI interface to upload new .hex. (Bootloader will be maintained on the board)<br>
<br>
<br>
<br>
Bootloader binary is configured to use the UART2 (accessible on the board) at 115200.<br>
<br>
Clock switching is enable (i.e. Simulink model to be loaded with the Bootloader might use any clock provided Clock Switching Enable is on in Master Block.)<br>
<br>
<br>
<br>
Also attached is an update of the previous simulink model for UDB4 tailored for easy used with bootloader (no need to reboot the board : first attempt to program the board will stop the embedded software. Secodn attempt will effectively program it.):<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/469-ds30_Bootloader_UDB4_Board_115200_UART2_ClkSwitchingEnable.zip">Pièce jointe : ds30_Bootloader_UDB4_Board_115200_UART2_ClkSwitchingEnable.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/470-UDB4_TestBoard.mdl">Pièce jointe : UDB4_TestBoard.mdl</a></p>
</article>

