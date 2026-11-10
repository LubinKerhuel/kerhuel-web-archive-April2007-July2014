---
title: "ADC doesn't produce correct output type"
url: "/forum/topic/239/"
archiveKind: "topic"
---
# ADC doesn't produce correct output type

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p915">
<header><strong>bmairs</strong><time datetime="2009-07-27 18:57 UTC">2009-07-27 18:57 UTC</time></header>
<div class="forum-post-body">It doesn't matter if I select signed or unsigned integer for the output of the ADC, it always shows it being a uint16. Has anyone else seen this behavior?</div>
</article>

<article class="forum-post" id="p928">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-30 09:59 UTC">2009-07-30 09:59 UTC</time></header>
<h3>Re: ADC doesn&#x27;t produce correct output type</h3>
<div class="forum-post-body">Datatype of the output of the block ADC is always uint16. Anyway, this uint16 store the value in the format you selected. Thus, you should use a type convert block, with <strong>Stored Integer Value (SI) (in opposition to Real Word Value)</strong> to convert the simulink representation of the data. <br>
<br>
<br>
<br>
Thanks for repporting that, I should change the datatype output of the block depending on the representation selected.</div>
</article>

