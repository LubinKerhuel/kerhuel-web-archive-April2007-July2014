---
title: "PORT D bug on DSPIC33FJ64(128)MC804"
url: "/forum/topic/268/"
archiveKind: "topic"
---
# PORT D bug on DSPIC33FJ64(128)MC804

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1052">
<header><strong>rmikio</strong><time datetime="2010-01-26 23:16 UTC">2010-01-26 23:16 UTC</time></header>
<div class="forum-post-body">Hi Lubin and group,<br>
<br>
<br>
<br>
 I am new user for DSPIC and actually I am trying to use your very useful blockset (just downloaded it today).<br>
<br>
 However I have problems regarding the Digital Input. When I try to compile to DSPIC33FJ128MC804, the following error occurs:<br>
<br>
 <br>
<br>
 dsPIC_33f_Explorer16.c:165: error: 'PORTDbits' undeclared (first use in this function) <br>
<br>
<br>
<br>
  Looking into the .h files, I could notice that DSPIC33FJ128MC804 does not present any definition for PORTDbits.<br>
<br>
  It seems that the digital Input for DSPIC33FJ128MC804 is made in a different way, but I am not quite sure about that.<br>
<br>
<br>
<br>
  However it seems that this is the only error so far.<br>
<br>
<br>
<br>
  Can you enlighten me here, please?<br>
<br>
<br>
<br>
  I imagine I can use the Analog Input as a digital Input, just by configuring it correctly. But then I guess if the Analog Input is also implemented for this specific DSPIC.<br>
<br>
<br>
<br>
  Thank you and regards,<br>
<br>
  Mikio</div>
</article>

<article class="forum-post" id="p1053">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-27 00:26 UTC">2010-01-27 00:26 UTC</time></header>
<h3>Re: PORT D bug on DSPIC33FJ64(128)MC804</h3>
<div class="forum-post-body">I checked 33fj MC804 definition either on microchip h file, and in the blockset, it's coherent.<br>
<br>
<br>
<br>
Could you check you select the correct dsPIC in the master block ?<br>
<br>
Check then that your simulink model does not contain any port D.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1055">
<header><strong>Bobes</strong><time datetime="2010-01-27 01:08 UTC">2010-01-27 01:08 UTC</time></header>
<h3>Re: PORT D bug on DSPIC33FJ64(128)MC804</h3>
<div class="forum-post-body">hello I am using 804 as well, I do not think there is any PORTD at all. at least I cant see any pin on the Pin Diagram.<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1056">
<header><strong>rmikio</strong><time datetime="2010-01-27 13:54 UTC">2010-01-27 13:54 UTC</time></header>
<h3>Re: PORT D bug on DSPIC33FJ64(128)MC804</h3>
<div class="forum-post-body">Greetings all,<br>
<br>
<br>
<br>
  Thank you for your prompt reply.<br>
<br>
  Ok, my LACK of knowledge (or I shall say my dumbness and ignorance) is responsible for this mistake.<br>
<br>
  Actually dsPIC33fj64(128)MCx04 does NOT present any PORT D, but only PORT A, B or C.<br>
<br>
  <br>
<br>
  Thank you again and sorry for bothering!<br>
<br>
  Regards,<br>
<br>
  Mikio</div>
</article>

