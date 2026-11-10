---
title: "Speeding up the chip"
url: "/forum/topic/317/"
archiveKind: "topic"
---
# Speeding up the chip

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1283">
<header><strong>Jodoku</strong><time datetime="2010-07-31 19:07 UTC">2010-07-31 19:07 UTC</time></header>
<div class="forum-post-body">I have a question:<br>
<br>
<br>
<br>
I am working on a program in Simulink that models a 30f4011 chip as a sort of wireless node transmitter/receiver.  The basic premise is that after every fixed period of time, it sends a data packet and then looks for an acknowledgement.  If it does not receive one, it will resend (up to 9 times).  I have accomplished this by creating an embedded matlab function, and I use a limited counter to keep track of time.  Ideally I want the aforementioned period of time to be 1 microsecond or even 1 nanosecond, however I can not get it to run nearly this fast.  I am reading the send data in matlab via a serial connection from a dsPICDEM2 board.  How can I go about fixing this?  I have attached the model for reference.<br>
<br>
<br>
<br>
Thank you</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/349-nodetest.mdl">Pièce jointe : nodetest.mdl</a></p>
</article>

