---
title: "RS232gui problem..."
url: "/forum/topic/332/"
archiveKind: "topic"
---
# RS232gui problem...

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1317">
<header><strong>Lola</strong><time datetime="2010-11-04 06:53 UTC">2010-11-04 06:53 UTC</time></header>
<div class="forum-post-body">Dear Lubin, <br>
<br>
<br>
<br>
I will be using the blockset as part of my graduation project so I was testing the different functions of the microchip dspic 30f 4013 before starting. The TX block however is the only block that hasn't functioned properly. I am using a simple program using an ADC input and a TX as the output, the pin does generate a signal ( shown on an scilloscope) but the graph is not appearing on Matlab, and the bytes in the rs232gui show wither \ or / or - . I have attached my program, please let me know what I have done wrong.<br>
<br>
<br>
<br>
Thank you :)</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/350-test2010_4.mdl">Pièce jointe : test2010_4.mdl</a></p>
</article>

<article class="forum-post" id="p1318">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-04 13:33 UTC">2010-11-04 13:33 UTC</time></header>
<h3>Re: RS232gui problem...</h3>
<div class="forum-post-body">It should works : low % error on the transmission speed.<br>
<br>
<br>
<br>
you can check the following points  :<br>
<br>
- Is the dsPIC running at 2.5 MIPS (make a output pin to toggle at a defined freuqency and check that you get this frequency with your scope).<br>
<br>
- Are you oppening the correct port COM . check with hyper terminal, (or real term that is a free hyperterminal quite good). Try to short circuit Rx and Tx pin of the computer and to see that the computer is receiving char sent through the keyboard.<br>
<br>
<br>
<br>
What type of interface converter are you using for connecting the chip to the PC ?<br>
<br>
<br>
<br>
I could not help more on this as I see no real reasons.</div>
</article>

