---
title: "UART"
url: "/forum/topic/290/"
archiveKind: "topic"
---
# UART

Forum : [dsPIC Peripherals](/forum/#forum-9)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1138">
<header><strong>guille</strong><time datetime="2010-03-14 18:44 UTC">2010-03-14 18:44 UTC</time></header>
<div class="forum-post-body">Hello I´m Guillermo from Argentina! congratulations for the blocks! are great! I want to know if I am doing something badly in my design. I want to send a character for the UART, I am going to send numbers, I want to convert it to double, to add a number and return to send it. It does not work, returns garbage to me. Here is the model.<br>
<br>
If someone can help me please...<br>
<br>
Thanks<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/305-UART.mdl">Pièce jointe : UART.mdl</a></p>
</article>

<article class="forum-post" id="p1458">
<header><strong>resodad</strong><time datetime="2011-02-15 17:56 UTC">2011-02-15 17:56 UTC</time></header>
<h3>Re: UART</h3>
<div class="forum-post-body">Hi Guillermo,<br>
<br>
I'm not sure what you're trying to accomplish.<br>
<br>
Do you need the data store for some other purpose? <br>
<br>
Maybe you can eliminate it? <br>
<br>
<br>
<br>
Why are you converting to double? Convert to uint8 after the sum keeps only the least significant 8-bit byte.<br>
<br>
<br>
<br>
You may have a problem with the order of execution of the blocks.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/379-convertType.mdl">Pièce jointe : convertType.mdl</a></p>
</article>

