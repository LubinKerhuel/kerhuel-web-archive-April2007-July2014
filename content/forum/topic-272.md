---
title: "debugging registry"
url: "/forum/topic/272/"
archiveKind: "topic"
---
# debugging registry

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1064">
<header><strong>Bobes</strong><time datetime="2010-01-31 21:06 UTC">2010-01-31 21:06 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
may be I have overlooked it somewhere, but I think it would be a good idea to add i.e.: a tick-box for some general registry settings, to be specific, I need to use MPLAB debugger, with ICD3. This means I have to set i.e.: "_FICD( JTAGEN_OFF &amp; ICS_PGD3 )"  in "whatever_main.c".<br>
<br>
I guess it should not be very difficult, and there is possibly more registers that would be helpful to have in this fashion.<br>
<br>
I hope its not to much trouble.<br>
<br>
Thanks for consideration<br>
<br>
Kind regards<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1087">
<header><strong>LubinKerhuel</strong><time datetime="2010-02-23 20:55 UTC">2010-02-23 20:55 UTC</time></header>
<h3>Re: debugging registry</h3>
<div class="forum-post-body">Hi Josef, <br>
<br>
<br>
<br>
This option _FICD( JTAGEN_OFF &amp; ICS_PGD3 ) is added and will be available in the next blockset release (following V 3.1).<br>
<br>
Is there any others "hard coded" options you will need ?<br>
<br>
anyway, adding a general box is more complicated right now but may be done if necessary.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1093">
<header><strong>Bobes</strong><time datetime="2010-02-26 20:39 UTC">2010-02-26 20:39 UTC</time></header>
<h3>Re: debugging registry</h3>
<div class="forum-post-body">thanks, that is good news.<br>
<br>
so far this is all I can think of. well actually the I2C selection... but I believe we have discussed that somewhere already</div>
</article>

