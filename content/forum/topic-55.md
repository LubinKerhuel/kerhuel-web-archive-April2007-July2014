---
title: "dsPIC and PIC 18F"
url: "/forum/topic/55/"
archiveKind: "topic"
---
# dsPIC and PIC 18F

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p100">
<header><strong>vedant</strong><time datetime="2007-08-21 09:41 UTC">2007-08-21 09:41 UTC</time></header>
<div class="forum-post-body">Hi i have seen your work on dsPIC toolbox and also had a look at your resume. Was very impressed . Can you please send me the toolbox for PIC 18 F4580 so that i can work on my project.</div>
</article>

<article class="forum-post" id="p101">
<header><strong>LubinKerhuel</strong><time datetime="2007-08-21 21:00 UTC">2007-08-21 21:00 UTC</time></header>
<div class="forum-post-body">Hi Vedant,<br>
<br>
<br>
<br>
The PIC18F family do not use the same C compiler. <br>
<br>
I looked at the possibility to do a toolbox for 18F chips long time ago ( 2 or 3 years) and concluded that the C compiler for PIC18 I used (from Hi-tech) was not Compliant with the standard C, thus, it does not work with C code generated with the matlab Real Time Workshop Embedded Coder. <br>
<br>
<br>
<br>
Consider using a dsPIC or PIC24 if you want to generate your code with matlab and the toolbox I created. You could also have a look on the SimuQuest companie that propose a toolbox for some PIC18. Let us know if the product is good. <br>
<br>
<br>
<br>
Regards<br>
<br>
<br>
<br>
Lubin KERHUEL</div>
</article>

<article class="forum-post" id="p581">
<header><strong>arsen</strong><time datetime="2008-10-21 16:24 UTC">2008-10-21 16:24 UTC</time></header>
<h3>pic 16F84A/16f87X</h3>
<div class="forum-post-body">hi  again Lubin,<br>
<br>
my tool is working fine and everything goes well( ı ve got compiling problem some weeks ago maybe u remember) now i ve another question to you about pic 16f84A or 16f87X. İs ir possible to use 16f84A  /16f87X with your tool ?? i would like to use this pic cos its very cheap and easy to find etc..<br>
<br>
also i ve compared 16f with 30f , 30f has a lot of fetures and abilities , since i am gonna embedd very simple programma i think i dont need 30f,<br>
<br>
i hope that 16f84Aor 16f87X  works with ur tool <br>
<br>
<br>
<br>
thanx for now<br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p582">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-21 16:36 UTC">2008-10-21 16:36 UTC</time></header>
<h3>Re: dsPIC and PIC 18F</h3>
<div class="forum-post-body">Hi Arsen,<br>
<br>
<br>
<br>
I'm glad your "tool" is working fine now.<br>
<br>
The blockset do not support 16f chips and there is no plan to support 16f in the near futur ;-).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p583">
<header><strong>arsen</strong><time datetime="2008-10-21 16:51 UTC">2008-10-21 16:51 UTC</time></header>
<h3>Re: dsPIC and PIC 18F</h3>
<div class="forum-post-body">hi lubinnn,<br>
<br>
thanx again for your quick responce, so then i ve got to use from your supported chips , then i ve got onother question , as a begginner ( and my programme is not that big space only controlling leds with diiferent time cycles, for example i ve got 2or 3  inputs in every 30 sec cycle and according to these inputs, as an output i ve got to switch some leds on some not or switch some leds for 30 sec on or X sec on, depending  on the input ) which chip model  would you  advise for real application which one is more stable for real application ( ofcourse among the chips which are supported from ur tool)<br>
<br>
thanx again  <br>
<br>
<br>
<br>
arsen</div>
</article>

<article class="forum-post" id="p584">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-21 20:57 UTC">2008-10-21 20:57 UTC</time></header>
<h3>Re: dsPIC and PIC 18F</h3>
<div class="forum-post-body">Hi Arsen,<br>
<br>
<br>
<br>
Coudn't give you an usefull advice. All chips seems to works well for direct I/O input/output.</div>
</article>

<article class="forum-post" id="p1236">
<header><strong>sreenatg</strong><time datetime="2010-05-11 10:32 UTC">2010-05-11 10:32 UTC</time></header>
<h3>Re: dsPIC and PIC 18F</h3>
<div class="forum-post-body">Can i have the PIC 18F 4580 blockset. I would be greatfull if someone help me on this.</div>
</article>

