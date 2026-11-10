---
title: "Digital Output Write whole 16 bit word"
url: "/forum/topic/367/"
archiveKind: "topic"
---
# Digital Output Write whole 16 bit word

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1492">
<header><strong>resodad</strong><time datetime="2011-03-02 21:15 UTC">2011-03-02 21:15 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
How can I send a 16 bit number to port B? The block only accepts a boolean type.<br>
<br>
Also, please clarify the use of "Exact Simultaneous Write" in the digital output block.<br>
<br>
Thanks,<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1500">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-06 21:56 UTC">2011-03-06 21:56 UTC</time></header>
<h3>Re: Digital Output Write whole 16 bit word</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>How can I send a 16 bit number to port B</blockquote> In the blockset current version, this is a pain to do as you will have to decompose each bytes of your 16 bits number to feed a write block.<br>
<br>
I should probably write another digital write function for this! Anyway, waiting for it, I would recommend to use the C call function block! The C function is quite straight here.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>Also, please clarify the use of "Exact Simultaneous Write" in the digital output block.</blockquote><br>
In the case that you are writing more than 1 bit, <br>
<br>
Actions when exact Simultaneous Write is checked:<br>
<br>
- Read port value (on LATx register) and store the value in intermediate variable<br>
<br>
- Modify the variable that depends on the values of the the simulink block input.<br>
<br>
- Write the resulting variable back to LATx register.<br>
<br>
<br>
<br>
Actions when exact Simultaneous Write is NOT checked:<br>
<br>
- Modify the LATx register depending on the values of the simulink block input.<br>
<br>
With this last method, bits are modified one by one thus bit change "is not simultaneous".<br>
<br>
<br>
<br>
I hope I make it clear.</div>
</article>

<article class="forum-post" id="p1503">
<header><strong>resodad</strong><time datetime="2011-03-07 14:43 UTC">2011-03-07 14:43 UTC</time></header>
<h3>Re: Digital Output Write whole 16 bit word</h3>
<div class="forum-post-body">Thanks Lubin,<br>
<br>
I will try the C file block; I am sure it is better than what I did. I attach my simulink file anyway for those of us who are scared of C  :? <br>
<br>
Thanks for the clear explanation of simultaneous write.<br>
<br>
Cheers,<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/393-writeWord.mdl">Pièce jointe : writeWord.mdl</a></p>
</article>

