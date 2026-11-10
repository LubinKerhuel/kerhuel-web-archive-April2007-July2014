---
title: "Quad-Rotor project I2C blockset"
url: "/forum/topic/277/"
archiveKind: "topic"
---
# Quad-Rotor project I2C blockset

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1089">
<header><strong>Liverpool</strong><time datetime="2010-02-26 10:38 UTC">2010-02-26 10:38 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I need some help with I2C blockset. I am using dsPIC30F4013 and magnetometer HMC6352. I struggle to communicate with with as my magnetometer sencor. <br>
<br>
This is principal of opperation:<br>
<br>
"There is a clock line (SCL) and a data SDA line in this bus specification and a host of devices can be connected. The bus can be a<br>
<br>
single Master – multi Slave or it can be a Multi-Master configuration. All data transfers are initiated by the Master device which is<br>
<br>
responsible for generating the clock signal, and the transfers are 8 bit long. All devices are addressed by its unique 7 bit Address.<br>
<br>
After each 8-bit transfer, the Master generates a 9 th clock pulse, and the transmitting device releases the SDA line. The receiving<br>
<br>
device will pull the SDA line low to acknowledge (ACK) the successful transfer or leave the SDA high to NACK."<br>
<br>
full document attached.<br>
<br>
Question:<br>
<br>
Could you advice how to generate the clock signal addressed to the sencor in I2C and how to read the I2C data from the sencor? Do you have any example to see how I2C bus master is used? <br>
<br>
<br>
<br>
Very Big Thanks in advance!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/292-hmc6353_i2c_operational_overview.pdf">Pièce jointe : hmc6353_i2c_operational_overview.pdf</a></p>
</article>

<article class="forum-post" id="p1090">
<header><strong>Liverpool</strong><time datetime="2010-02-26 11:27 UTC">2010-02-26 11:27 UTC</time></header>
<h3>Re: Quad-Rotor project I2C blockset</h3>
<div class="forum-post-body">In the specifications of dsPIC30F4013 I found address value of 120, but not sure about it? Is it dsPIC address? Where to find it?<br>
<br>
For HMC6352 addresses for Write is 42(hex) and for read 43(hex)<br>
<br>
magnetometer operation frequency is 100kHz<br>
<br>
<br>
<br>
So as I understand I have to create to I2C blocks with sequencies as follows:<br>
<br>
'S A120 W42 P' and 'S A120 W43 P'? or 'S A120 W42 R43 P'?<br>
<br>
<br>
<br>
but anyway there is clock signal and how will I get output headings Mag X and Mag Y?</div>
</article>

