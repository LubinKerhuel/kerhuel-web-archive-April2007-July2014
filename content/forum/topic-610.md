---
title: "uartrx and uarttx configuration blocks"
url: "/forum/topic/610/"
archiveKind: "topic"
---
# uartrx and uarttx configuration blocks

Forum : [dsPIC Peripherals](/forum/#forum-9)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p2052">
<header><strong>dan</strong><time datetime="2013-11-05 13:06 UTC">2013-11-05 13:06 UTC</time></header>
<div class="forum-post-body">Hey guys,<br>
<br>
<br>
<br>
   I'm trying to send a constant value through serial connection using a instrument control toolbox library from simulink as you can see in the files attached. The problem is when I get back this signal through the receive serial block, it is different from the signal I sent. I actually don't  know whether I'm doing some wrong settings in the dspic blocksets. But when I set up the blocking function of the uartRx block, the signal comes properly as it would be. But if unset it, the signal comes totally different. And even though if I still keep the blocking function of the block when I do any operation with this signal, for example multiplying it by 2, the signal comes through serial receive totally wrong.<br>
<br>
If someone has ever dealt with this, I would appreciate any help.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/521-sim_conv.mdl">Pièce jointe : sim_conv.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/522-serial_test_hoy.mdl">Pièce jointe : serial_test_hoy.mdl</a></p>
</article>

