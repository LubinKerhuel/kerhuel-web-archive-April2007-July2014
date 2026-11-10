---
title: "setting variables in OPC server"
url: "/forum/topic/289/"
archiveKind: "topic"
---
# setting variables in OPC server

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1128">
<header><strong>dorijan</strong><time datetime="2010-03-11 01:37 UTC">2010-03-11 01:37 UTC</time></header>
<div class="forum-post-body">For my final work at university I am making a way to connect a dsPIC to SCADA over OPC server, so I want to share with everyone my proof of concept code in python...<br>
<br>
<br>
<pre><code>import serial, binascii, struct,time,OpenOPC
ser = serial.Serial(0, 38400) #for com1: use 0, for com2 use 1 etc...38400 is speed of com port
opc = OpenOPC.client()
opc.connect('Matrikon.OPC.Simulation')
buff=25
sampletime=0.2
<wbr>
while 1:
	s = ser.read(buff)
	prvi=s.find('\x05')
	print '1. kanal:'
	print struct.unpack('&lt;H',s[prvi+1]+s[prvi+2])[0]
	opc['Bucket Brigade.data1'] = struct.unpack('&lt;H',s[prvi+1]+s[prvi+2])[0]
<wbr>
	prvi=s.find('\x15')
	print '2. kanal:'
	print struct.unpack('&lt;H',s[prvi+1]+s[prvi+2])[0]
	opc['Bucket Brigade.data2'] = struct.unpack('&lt;H',s[prvi+1]+s[prvi+2])[0]
	print
	print
	time.sleep(sampletime)
<wbr>
ser.close()
opc.close()
</code></pre><br>
<br>
for this you need a python (32 bit) and this (I used 2.5 version)<br>
<br>
<br>
<br>
	Pyserial - <a href="http://pyserial.sourceforge.net/">http://pyserial.sourceforge.net/</a> <br>
<br>
	OpenOPC - <a href="http://openopc.sourceforge.net/">http://openopc.sourceforge.net/</a> <br>
<br>
	Pyro - <a href="http://pyro.sourceforge.net/">http://pyro.sourceforge.net/</a> <br>
<br>
	Python for windows extensions - <a href="http://sourceforge.net/projects/pywin32/">http://sourceforge.net/projects/pywin32/</a></div>
</article>

