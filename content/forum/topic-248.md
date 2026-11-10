---
title: "Error building dsPIC30F3012 with Fuzzy"
url: "/forum/topic/248/"
archiveKind: "topic"
---
# Error building dsPIC30F3012 with Fuzzy

Forum : [General Remark and Questions](/forum/#forum-1)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p963">
<header><strong>Alan</strong><time datetime="2009-09-29 23:48 UTC">2009-09-29 23:48 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I create a model that use Fuzzy Logic Controller block, and when I try build show this error:<br>
<br>
<em>Error building Real-Time Workshop target for block diagram 'fuzzy_stepmotor_casa'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1070<br>
<br>
Error(s) encountered while building model "fuzzy_stepmotor_casa".<br>
<br>
</em><br>
<br>
<br>
<br>
I attach the model, the FIS file and the error for help in analisys.<br>
<br>
<br>
<br>
I need a help urgently, Thanks.<br>
<br>
<br>
<br>
Alan</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/266-fuzzy_stepmotor_casa.mdl">Pièce jointe : fuzzy_stepmotor_casa.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/267-lente_act3.fis.mdl">Pièce jointe : lente_act3.fis.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/268-errorbuild_fuzzy_dspic.JPG">Pièce jointe : errorbuild_fuzzy_dspic.JPG</a></p>
</article>

<article class="forum-post" id="p964">
<header><strong>Alan</strong><time datetime="2009-10-11 20:26 UTC">2009-10-11 20:26 UTC</time></header>
<h3>Re: Error building dsPIC30F3012 with Fuzzy</h3>
<div class="forum-post-body">Hi again,<br>
<br>
<br>
<br>
I found the problem, my model use the 3036 bytes of data memory and the dspic 30f3012 has only 2048 bytes.<br>
<br>
Now I wanna know if the EEPROM memory(1024 bytes) can be used like RAM, to data memory,  and how I use it?<br>
<br>
<br>
<br>
Thanks<br>
<br>
Alan</div>
</article>

<article class="forum-post" id="p965">
<header><strong>LubinKerhuel</strong><time datetime="2009-10-17 14:40 UTC">2009-10-17 14:40 UTC</time></header>
<h3>Re: Error building dsPIC30F3012 with Fuzzy</h3>
<div class="forum-post-body">Hi Alan,<br>
<br>
<br>
<br>
It is not possible to replace RAM by EEPROM.<br>
<br>
however, you may try to activate simulink optimization, try to check the box "inline parameters". This may save a lot of RAM memory.<br>
<br>
<br>
<br>
Lubin</div>
</article>

