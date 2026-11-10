---
title: "Configuration bits warning"
url: "/forum/topic/204/"
archiveKind: "topic"
---
# Configuration bits warning

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p766">
<header><strong>karthikeyan</strong><time datetime="2009-02-24 08:05 UTC">2009-02-24 08:05 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I am new to using the dspic and the blockset .. I just tried a very simple LED blinking program in simulink .. I am using PICKit 2 to burn the dspic and the dspic i am using is the dspic30f4011 .. i compiled the block and when i try to burn the hex, the pickit programming window says that the configuration bits are not proper and its defaulting to preset default values .. my code doesn't work .. all the bits of port B are permanently high .. <br>
<br>
<br>
<br>
i tried just blinking pin 2 of port B in a 0.5Hz frequency .. what could be the problem ? kindly help me .. i am not using a external oscillator .. what configuration should i change to use the internal oscillator ? could that be the problem ?? .. and where am i setting whether the port B is a input or a output port ?</div>
</article>

<article class="forum-post" id="p769">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-26 00:40 UTC">2009-02-26 00:40 UTC</time></header>
<h3>Re: Configuration bits warning</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : karthikeyan</header>where am i setting whether the port B is a input or a output port ?</blockquote><br>
That is set automatically, depending if you use Port read or port write blocks...<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : karthikeyan</header>window says that the configuration bits are not proper and its defaulting to preset default values</blockquote><br>
Problems comes from that. Try generating the html c code report in matlab. and have a look at the end of the main file. There should be configuration code. Check that oscillators are defined correctly in the C language. If you find any problem, please report-it so that I can make appropriate corrections.<br>
<br>
Anyway, I hardly not use internal oscillator, could not help so much... <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p789">
<header><strong>karthikeyan</strong><time datetime="2009-03-18 13:41 UTC">2009-03-18 13:41 UTC</time></header>
<h3>Re: Configuration bits warning</h3>
<div class="forum-post-body">even though it shows configuration bits warning .. the program works once i connect a external oscillator .. the oscillator was the problem i guess  :)</div>
</article>

