---
title: "Recive Multiple Data from the same UART"
url: "/forum/topic/471/"
archiveKind: "topic"
---
# Recive Multiple Data from the same UART

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1796">
<header><strong>Vladimir Dvorkin</strong><time datetime="2012-01-13 12:50 UTC">2012-01-13 12:50 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I am using dsPic 30F4011 microcontroller.<br>
<br>
I am commuincating with the dsPIC using Xbee Pro series 1 modules, and using Simulink's Real Time Workshop.<br>
<br>
<br>
<br>
I am trying to send multiple data from my RTW model (see attachment) using mux function and sending threw Packet output.<br>
<br>
I can't split the recieved data vector using demux, since the UART Rx Block produce 1 output uint 8 signal, and matlab wont let me compile my program!<br>
<br>
<br>
<br>
How can I recieve multiple data from the same UART port? (e.g. turn on LED with PORTB0, and conrol PWM)<br>
<br>
<br>
<br>
Thanks<br>
<br>
<br>
<br>
Vladimir</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/466-LED_PWM.mdl">Pièce jointe : LED_PWM.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/467-rtw.mdl">Pièce jointe : rtw.mdl</a></p>
</article>

<article class="forum-post" id="p1797">
<header><strong>resodad</strong><time datetime="2012-01-13 16:07 UTC">2012-01-13 16:07 UTC</time></header>
<h3>Re: Recive Multiple Data from the same UART</h3>
<div class="forum-post-body">Vladimir,<br>
<br>
You want to parse incoming data (UART Rx). I did similar for Tx. See the post "Rx Interrupt buffer size" linked here: <a href="/forum/topic/143/#p453">http://archive.kerhuel.eu/forum/viewtopic.p ... +uart#p453</a>.<br>
<br>
<br>
<br>
You might get some ideas that will work for you.<br>
<br>
Regards,<br>
<br>
John</div>
</article>

