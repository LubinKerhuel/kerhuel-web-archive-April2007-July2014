---
title: "A more friendly way to create a chip select with SPI ?"
url: "/forum/topic/115/"
archiveKind: "topic"
---
# A more friendly way to create a chip select with SPI ?

Forum : [dsPIC Peripherals](/forum/#forum-9)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p323">
<header><strong>Anonyme</strong><time datetime="2008-05-05 20:46 UTC">2008-05-05 20:46 UTC</time></header>
<div class="forum-post-body">Dear all,<br>
<br>
<br>
<br>
I'm trying to do a very simple thing : send some SPI to a peripheral (see model attached). The thing is that the peripheral needs its CS to be pulled down just before the transfer and pulled back up at the end. To do this, I used the block ordering function, but I had to introduce a lot of NOPs. The SPI block orders the next block as soon as it has transmitted the send request to the SPI peripheral, it does not wait for the transfer to be effectively over. <br>
<br>
<br>
<br>
The current method works, but I wondered if there was a more CPU friendly way, as this is quite ressource consuming.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Martin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/65-interfacage_spi.mdl">Pièce jointe : interfacage_spi.mdl</a></p>
</article>

<article class="forum-post" id="p324">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-05 22:32 UTC">2008-05-05 22:32 UTC</time></header>
<h3>Re: A more friendly way to create a chip select with SPI ?</h3>
<div class="forum-post-body">Hi Martin,<br>
<br>
<br>
<br>
This is your original solution: <br>
<br>
The first solution I propose is to disable the Chip first, and enable it just after...<br>
<br>
<br>
The second solution I propose is to configure the SPI read/write so as to read and write a data. In this way, the SPI block waits for the SPI communication to finish. <br>
<br>
<br>
Here is the model with the three solutions. These are not going to work all together. Delete at least two solutions!<br>
<br>
<br>
I corrected mistakes about sampling time. I strongly recommend using the "sample time color" option of simulink!<br>
<br>
<br>
<br>
Lubin<br>
<br>
 PS : I see that you were inscribed to the forum. You should loggin to the forum before writting message. It allows to get mail when a response is given and other usefull options ( also less administration task for me...)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/66-interfacage_SPI_original.png">Pièce jointe : interfacage_SPI_original.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/67-interfacage_SPI_Sol1.png">Pièce jointe : interfacage_SPI_Sol1.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/68-interfacage_SPI_Sol2.png">Pièce jointe : interfacage_SPI_Sol2.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/69-interfacage_spi_b.mdl">Pièce jointe : interfacage_spi_b.mdl</a></p>
</article>

<article class="forum-post" id="p326">
<header><strong>mhiernaux</strong><time datetime="2008-05-06 12:49 UTC">2008-05-06 12:49 UTC</time></header>
<h3>Re: A more friendly way to create a chip select with SPI ?</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for your reply.<br>
<br>
<br>
<br>
I tried the 2 options, but I think I'm doing some mistakes as the CS goes back to disable state in your last option, before all bits are effectively transmitted. The 2nd option is working but is less optimal for me, as the CS disable commands the latch of my SPI DAC, and thus is happening 1 cycle later here.<br>
<br>
<br>
<br>
Any ideas ?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Martin</div>
</article>

<article class="forum-post" id="p329">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-06 19:54 UTC">2008-05-06 19:54 UTC</time></header>
<h3>Re: A more friendly way to create a chip select with SPI ?</h3>
<div class="forum-post-body">Try to check "Wait for incomming data (slave mode)" and uncheck "Wait for previous operation to finish, and reset before read".<br>
<br>
The block menu is not very clear yet. I'll try to make it more clear in the next version...</div>
</article>

