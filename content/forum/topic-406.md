---
title: "SPI on dsPic30F2010"
url: "/forum/topic/406/"
archiveKind: "topic"
---
# SPI on dsPic30F2010

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1589">
<header><strong>frouby</strong><time datetime="2011-05-27 16:13 UTC">2011-05-27 16:13 UTC</time></header>
<div class="forum-post-body">Hi there!<br>
<br>
<br>
<br>
I've got some problems on a SPI communication between a 33FJ128GP802 (master) and a µ-gyro ADIS16100 (slave) and a 30F2010 (slave) . Here is the configuration parameters :<br>
<br>
<span class="underline">Master 33FJ128GP802 :</span> SPI config block<br>
<br>
Mode:Master<br>
<br>
Clock 625000Hz<br>
<br>
Starting : Enable<br>
<br>
SDO Enable<br>
<br>
Data length 16bits<br>
<br>
Sample phase : End of bit<br>
<br>
Clock Active State : High<br>
<br>
Output change on transition : Active to Idle<br>
<br>
 I use the SPI I/O Interrupt driven block with the mode 'read once - interrupt re-enable after block execution'. I try to send 2 trames to the gyro and 3 trames to the 30F2010. I expect to receive 5 trames too. I've also configured the the chip select of each slave in the block.<br>
<br>
<br>
<br>
<span class="underline">Slave 30F2010</span> SPI config block<br>
<br>
Mode:Slave<br>
<br>
Clock : 625000Hz<br>
<br>
Starting : Enable<br>
<br>
SDO Enable<br>
<br>
Data length: 16 bits<br>
<br>
Slave Select PIN enable (slave mode)<br>
<br>
Sample phase : End of bit<br>
<br>
Clock active state : high<br>
<br>
Output change on transition : Active to Idle<br>
<br>
<br>
<br>
Here is the configuration of the SPI I/O Interrupt driven of the 30F2010: mode : continuous run - Interrupt always enable. If I change the mode to 'read once - interrupt re-enable after block execution' the dspic does not boot after programmation. I don't have selected a chip enable because it's already configured previously on the SPI Config block.<br>
<br>
<br>
<br>
My problem is that with this configuration the 30F2010 always send some datas on his SDO even when his chip select is at an high level. So that, it makes a conflict with SDO of the µgyro.<br>
<br>
<br>
<br>
I've also noticed that the trames of the SDO are not in the good order.</div>
</article>

<article class="forum-post" id="p1590">
<header><strong>frouby</strong><time datetime="2011-05-27 18:24 UTC">2011-05-27 18:24 UTC</time></header>
<h3>Re: SPI on dsPic30F2010</h3>
<div class="forum-post-body">I think I iderstood what was my real problem. It's that my 30F2010 doesn't boot if I change the mode to 'read once - interrupt-enable after block execution'. Sometimes it boots and it works well but mostly it doesn't boot....any ideas for this bug? Does it happen to anyone? thanks to reply!! :)</div>
</article>

<article class="forum-post" id="p1597">
<header><strong>frouby</strong><time datetime="2011-06-06 20:40 UTC">2011-06-06 20:40 UTC</time></header>
<h3>Re: SPI on dsPic30F2010</h3>
<div class="forum-post-body">I know the origins of the problem!! At the boot of the unit, after 5-6 seconds, the bit SPI1STAT.SPIROV is set because of the overflow in the SPI1BUF that makes the dsPic crash. To avoid the crash, I just have to put the SPI1STATbits.SPIROV=0 at the beginning of the SPI Interrupt function. But during 700ms every 6 seconds, I have no data on the SPI network...How can I fix this problem ??</div>
</article>

