---
title: "dsPIC &amp; MCP23017 using I2C"
url: "/forum/topic/172/"
archiveKind: "topic"
---
# dsPIC &amp; MCP23017 using I2C

Forum : [General Remark and Questions](/forum/#forum-1)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p601">
<header><strong>Stefano</strong><time datetime="2008-10-31 13:35 UTC">2008-10-31 13:35 UTC</time></header>
<div class="forum-post-body">Hi, I'm trying to use a dsPIC30F4011 to communicate via I2C with a MCP23017 (a 16-bit I/O port expander) but I have not fully understood how to setup the communication using the "I2C Bus Master" block. In order to read from a specific register of the MCP23017 the datasheet specifies this communication protocol:<br>
<br>
<br>
<br>
S _ OPCODE+W _ ACK* _ ADDRESS _ ACK* _ SR _ OPCODE+R _ ACK* _ DATAOUT* _ P<br>
<br>
<br>
<br>
where:<br>
<br>
<br>
<br>
S = start<br>
<br>
OPCODE+W =  7bit I2C addres of MCP23017 + LSB bit set to 0 (write instruction)<br>
<br>
ACK* = acknowledge provided by the MCP23017<br>
<br>
ADDRESS = register address to be read<br>
<br>
SR = restart<br>
<br>
OPCODE+R =  7bit I2C addres of MCP23017 + LSB bit set to 1 (read instruction)<br>
<br>
DATAOUT* = data out from MCP23017<br>
<br>
<br>
<br>
I'm using this sequence in the "I2C Bus Master" block: 'S A W Sr A R P' (with A1 = I2C addres of MCP23017, W2 = register address, A3 =  I2C addres of MCP23017), but I get a communication error. <br>
<br>
Can someone tell me the correct sequence that I have to use?<br>
<br>
<br>
<br>
Thank you</div>
</article>

<article class="forum-post" id="p603">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-31 19:41 UTC">2008-10-31 19:41 UTC</time></header>
<h3>Re: dsPIC &amp;amp; MCP23017 using I2C</h3>
<div class="forum-post-body">Hi Stefano,<br>
<br>
<br>
<br>
I2C is a very sensitive protocol and hard to debug. It greatly help to check with an oscillsocope what's going on.<br>
<br>
you may try to use  : S A W Sr A R<strong>nack</strong> P<br>
<br>
<br>
<br>
Good luck.</div>
</article>

<article class="forum-post" id="p608">
<header><strong>Stefano</strong><time datetime="2008-11-08 11:35 UTC">2008-11-08 11:35 UTC</time></header>
<h3>Re: dsPIC &amp;amp; MCP23017 using I2C</h3>
<div class="forum-post-body">Thanks Lubin for your answer. In these days I have tryed to solve the communication problem, and finally I have solved it!<br>
<br>
I have used the string that you have suggested (S A W Sr A Rnack P) where:<br>
<br>
<br>
<br>
A  = 7bit I2C addres of MCP23017 <strong>+ LSB bit set to 0 (write instruction)</strong><br>
<br>
W = register address to read from<br>
<br>
A = 7bit I2C addres of MCP23017 <strong>+ LSB bit set to 1 (read instruction)</strong><br>
<br>
<br>
<br>
I'd suggest you to specify that the addresse (A) in the "I2C Bus Master" block it's not only the I2C addres of MCP23017, but it must contain the bit that specify if the subsequent instruction (W or R or Rnack) is a write or read instruction (at first I thought that this bit was automatically set by the "I2C Bus Master" block).<br>
<br>
<br>
<br>
Stefano</div>
</article>

<article class="forum-post" id="p840">
<header><strong>g2dag</strong><time datetime="2009-05-06 03:33 UTC">2009-05-06 03:33 UTC</time></header>
<h3>Re: dsPIC &amp;amp; MCP23017 using I2C</h3>
<div class="forum-post-body">Hi Lubin, I am trying to interface with a similar device as stefano that uses the same I2C protocol  - it is a 3 axis accelerometer LIS3LV02DQ. I wrote a very simple test program but I've had no success so far.  You mentioned in your response that it helps to use an oscilloscope to troubleshoot, so I'm looking at the SDA and SCL with an oscilloscope but I am not seeing any signals, they are just pulled high by my 5K pull up resistors. Is there an error in my diagram that could be causing this? I attached it to this post. Thanks in advance,<br>
<br>
<br>
<br>
Gabe<br>
<br>
<br>
<br>
PS great job on the blockset, I see myself upgrading to 8 or 10 pins once I have a project that needs it!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/237-I2Ctest.mdl">Pièce jointe : I2Ctest.mdl</a></p>
</article>

<article class="forum-post" id="p845">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-06 22:32 UTC">2009-05-06 22:32 UTC</time></header>
<h3>Re: dsPIC &amp;amp; MCP23017 using I2C</h3>
<div class="forum-post-body">Dear Gabe,<br>
<br>
<br>
<br>
I did not see any obvious error in your model. You may add a blinking led to make sure the dsPIC is running anyway.<br>
<br>
<br>
<br>
I do not look at the specific chip you are using, and at the I2C parameters. I2C digital bus is really a pain to debug compared to its SPI equivalent. <br>
<br>
<br>
<br>
I am using I2C bus for one project, but I configured it quite a long time ago, I am not really up to date...<br>
<br>
<br>
<br>
Anyway, <br>
<br>
<br>
<br>
Look closely at initialisation time if really nothing is happening when you switch-on the system. You may have few data exchange on the SCL and SDA line and then I2C get stuck. In that case, it is a protocol problem.<br>
<br>
<br>
<br>
Otherwise, I could only advice to play with parameters until you get something to move on your scope. <br>
<br>
There is timeout mechanism on this I2C block that makes the execution to continue, even if the I2C bus is stuck. (Note that Real time constraints are not going to be respected if I2C bus is not working properly!) <br>
<br>
<br>
<br>
- disturb SCL and SDA line by hand during the execution to see if nothing happens. (Sometime, I2C bus is stuck)<br>
<br>
Or, in the simulink model:<br>
<br>
- Enable I2C before use<br>
<br>
- Disable I2C after use<br>
<br>
- Force with a/several digital output to make changes on SCL and SDA signals. <br>
<br>
That may unlock the accelerometer from a stuck state!<br>
<br>
<br>
<br>
<br>
<br>
I wish you good luck for that part!<br>
<br>
<br>
<br>
Lubiun</div>
</article>

<article class="forum-post" id="p846">
<header><strong>g2dag</strong><time datetime="2009-05-07 00:32 UTC">2009-05-07 00:32 UTC</time></header>
<h3>Re: dsPIC &amp;amp; MCP23017 using I2C</h3>
<div class="forum-post-body">Hi, thanks for the reply.<br>
<br>
<br>
<br>
I had already verified that it was running by flashing an LED as you suggested, so it isn't getting stuck. I ended up importing the project in to MPLAB so that I could debug a little more in detail. I noticed the timeout variable "slowDown" in several places, and so I turned on an LED if slowDown was &gt; 4000 (it times out at 5000) after each of the timeouts. It was actually timing out at the last step of the sequence (stop).<br>
<br>
<br>
<br>
But what is even weirder is that the acknowlegde bit from the slave, i2ccon.ACKDT, gets set to zero (slave acknowledge) even when I don't plug in my slave device! Or when I put an arbitrary slave address in. I verified this by having it turn on an LED just after it checks for an acknowledge, the first time. It actually makes it through the entire sequence, up until the end where it times out.<br>
<br>
<br>
<br>
Anyway it got too late last night but I'll give it another stab tonight and see if I can figure it out. I must say though, even though I am having problems it is much easier to start from your generated code than starting from scratch. I'll let you know once (if) I figure it out.<br>
<br>
<br>
<br>
Gabe</div>
</article>

