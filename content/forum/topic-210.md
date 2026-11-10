---
title: "How to setup the SPI module to send and recieve data"
url: "/forum/topic/210/"
archiveKind: "topic"
---
# How to setup the SPI module to send and recieve data

Forum : [dsPIC Peripherals](/forum/#forum-9)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p793">
<header><strong>karabo</strong><time datetime="2009-03-20 16:20 UTC">2009-03-20 16:20 UTC</time></header>
<div class="forum-post-body">Hello Mr. Lubin,<br>
<br>
 <br>
<br>
We are a team of students at Oakland University, USA and we are currently working on a project that uses dspic (30f4011)controller and we are currently using your dspic toolbox for spi communication.  We are communicating to the pressure sensor that has spi interface.  We looked through your forum and exmaple and it's useful, however it didn't help us setup the SPI block for receiving data from the pressure sensor to micro and to send data from micro to a transmitter though UART.   Could you please give us a direction on how to configure the spi block to send and receive data.  I have attached the simulink model that we have so far, but our model is not complete.  Your help is appreciated.<br>
<br>
 <br>
<br>
Here is a summary of the things that we want to accomplish:<br>
<br>
Send 8 bits command to the pressure sensor through the SPI module of the dspic.<br>
<br>
Receive the pressure data from the pressure sensor<br>
<br>
Send the pressure sensor data to the UART using the dspic<br>
<br>
<br>
<br>
I have attached the simulink block diagram and pressure sensor data sheet<br>
<br>
Thank you very much for your help.<br>
<br>
Khalid</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/218-sp12.pdf">Pièce jointe : sp12.pdf</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/219-PressureSensor.mdl">Pièce jointe : PressureSensor.mdl</a></p>
</article>

<article class="forum-post" id="p794">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-21 15:31 UTC">2009-03-21 15:31 UTC</time></header>
<h3>Re: How to setup the SPI module to send and recieve data</h3>
<div class="forum-post-body">I had a quick look.<br>
<br>
<br>
<br>
On the model prinple, it is Ok. However, I noticed few possible problems :<br>
<br>
- It seems that data length is 8 bits on the with this SP12 Tyre pressure sensor. Thus, SPI Should be configured with 8 bit data length. (except if you use 16 bits length commands)<br>
<br>
- Uart : 9% error @115200 : It is too much. I modified it to 38400.<br>
<br>
<br>
<br>
There may still be some errors, try modifying the SPI mode (or check it carefully from the datasheet), try with and without the 'wait' checkbox.<br>
<br>
<br>
<br>
You may try this attached version, using rs232gui from matlab to watch temperature.<br>
<br>
I may have exchange LSB with MSB, It will be quick to check...<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/222-shot_20090321163216-031.png">Pièce jointe : shot_20090321163216-031.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/221-PressureSensor_corr.mdl">Pièce jointe : PressureSensor_corr.mdl</a></p>
</article>

<article class="forum-post" id="p799">
<header><strong>karabo</strong><time datetime="2009-03-24 01:30 UTC">2009-03-24 01:30 UTC</time></header>
<h3>Re: How to setup the SPI module to send and recieve data</h3>
<div class="forum-post-body">Thank you Lubin for your diagram, it builds and compiles fine, but the chip select doesn't seem to be selected(pulled low) by the pic micro.  We are using 10k resistor.  Do you know why this is happening?<br>
<br>
<br>
<br>
Thanks<br>
<br>
Khalid</div>
</article>

<article class="forum-post" id="p800">
<header><strong>karabo</strong><time datetime="2009-03-24 02:16 UTC">2009-03-24 02:16 UTC</time></header>
<h3>Re: How to setup the SPI module to send and recieve data</h3>
<div class="forum-post-body">I have another question, do we have to use the pin mapping in our simulink model?<br>
<br>
<br>
<br>
thanks<br>
<br>
Khalid</div>
</article>

<article class="forum-post" id="p803">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-25 23:22 UTC">2009-03-25 23:22 UTC</time></header>
<h3>Re: How to setup the SPI module to send and recieve data</h3>
<div class="forum-post-body">Hey,<br>
<br>
<br>
<br>
About chip select, are you checking the correct pin. It is B2 on the model presented here. You should try to disconnect the B2 pin from the temperature sensor pin. Check that its value changes with an scope. You may also check that both :<br>
<br>
- the dsPIC SPI clock <br>
<br>
- the output data (SDO) <br>
<br>
are changing with a scope (while not connected to the SPI sensor to possibly electronic design problems like short-circuit).<br>
<br>
This is possible because the SPI peripheral do not wait for incomming data. Thus, its output pin (Chip Select, clock and SDO) will change even if no component are connected on the other side. In that way, it is much more easy to debug than I2C...<br>
<br>
<br>
<br>
There is not PIN mapping requirement of dsPIC 30f4011 because there is no PIN mapping mechanisme built-in that chip.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p805">
<header><strong>EZY</strong><time datetime="2009-03-31 02:16 UTC">2009-03-31 02:16 UTC</time></header>
<h3>Re: How to setup the SPI module to send and recieve data</h3>
<div class="forum-post-body">Hello Lubin:<br>
<br>
<br>
<br>
The SPI block diagram works partially, at least there is a communication established from dsPIC to the pressure sensor (SP12). The only problem I'm running into is sending two consecutive messages at almost the same time. The SP12 pressure/voltage/temp/acceleration sensor works this way. Initial message is sent to request measurement (in this case voltage) of a voltage 0010 0101(MEASURE _B) followed by 0010 1001 (RCBD - read compensated voltage data). These two messages need to be send to the SP12 in one SPI clock cycle (8bit clock) in order for the sensor to recognize the message as a valid request to measurement and read back measured value message.  I tried playing with the chip select but that doesn't make a difference since there are two blocks of SPI in the diagram, two 8bit SPI clocks are generated. Is there anyway to send the 148 and 164 from one SPI block, one after the other to the sensor?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
-Esayas<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/229-PressureSensor_corr_Voltage.mdl">Pièce jointe : PressureSensor_corr_Voltage.mdl</a></p>
</article>

