---
title: "No OC2 with 30f3012?"
url: "/forum/topic/228/"
archiveKind: "topic"
---
# No OC2 with 30f3012?

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p864">
<header><strong>john</strong><time datetime="2009-06-10 22:37 UTC">2009-06-10 22:37 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I have a problem when compiling a mdl with 2 PWM (using OC for 30f3012). With just 1 PWM (OC1), all is perfect. But with 2 PWM (OC1 and OC2 by using [1 2] in the OC block), I have the following error message for my double_PWM_test.mdl :<br>
<br>
<br>
<br>
double_PWM_test.c:118: error: structure has no member named `LATD1' <br>
<br>
double_PWM_test.c:122: error: structure has no member named `LATD1' <br>
<br>
gmake: *** [double_PWM_test.o] Error 255 <br>
<br>
<br>
<br>
with 30f3013 (same datasheet as 30f3012 but different pinout : 28pins instead of 18pins) it works.<br>
<br>
with 30f2011 (same datasheet as 30f3012 and same pinout, just the memory is different) : same error message.<br>
<br>
<br>
<br>
Thanks a lot if you can help!<br>
<br>
<br>
<br>
John</div>
</article>

<article class="forum-post" id="p868">
<header><strong>LubinKerhuel</strong><time datetime="2009-06-22 21:38 UTC">2009-06-22 21:38 UTC</time></header>
<h3>Re: No OC2 with 30f3012?</h3>
<div class="forum-post-body">Hello John,<br>
<br>
<br>
<br>
Thanks for that bug repport.<br>
<br>
It will be corrected in the next version.<br>
<br>
<br>
<br>
Tell me which matlab version you're using, I'll send you by mail the corrected version for testing purpose.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p877">
<header><strong>john</strong><time datetime="2009-06-29 21:39 UTC">2009-06-29 21:39 UTC</time></header>
<h3>Re: No OC2 with 30f3012?</h3>
<div class="forum-post-body">I am using MATLAB 2008b.<br>
<br>
In fact, it is working with OC(HW) for OC1 and OC2 with 30f3012; just when using normal OC is working only if we have OC1 (or OC2) alone. Perrhaps in 30f3012 they cannot have independant timers?</div>
</article>

<article class="forum-post" id="p878">
<header><strong>LubinKerhuel</strong><time datetime="2009-06-29 22:07 UTC">2009-06-29 22:07 UTC</time></header>
<h3>Re: No OC2 with 30f3012?</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
Could you post a model that generate this error ?<br>
<br>
<br>
<br>
Thanks<br>
<br>
Lubin</div>
</article>

