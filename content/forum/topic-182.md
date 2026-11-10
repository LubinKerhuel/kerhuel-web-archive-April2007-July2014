---
title: "C function call block"
url: "/forum/topic/182/"
archiveKind: "topic"
---
# C function call block

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p633">
<header><strong>Simon_says</strong><time datetime="2008-12-11 17:32 UTC">2008-12-11 17:32 UTC</time></header>
<div class="forum-post-body">Hi you all!<br>
<br>
 Hello Lubin:<br>
<br>
 <br>
<br>
I am trying to understand how the C call function block works but I am stuck. I have just tried to read a variable "data"  and put it out . I compare it with a constant and set a port bit if it is greater or iqual.  I have attached the C function also. After I compile it I get this error:<br>
<br>
<br>
<br>
.<br>
<br>
.<br>
<br>
.<br>
<br>
.<br>
<br>
callf4.o(.text+0x0):C:\Documents and Settings\123\Mis documentos\MATLAB\call4_dspic\sources\..\..\callf4.c: Link Error: Cannot access symbol (_data) at an odd address. <br>
<br>
C:\Program Files\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../call4.coff' <br>
<br>
gmake: *** [..\../call4.coff] Error 0xff <br>
<br>
### Real-Time Workshop build procedure for model: 'call4' aborted due to an error.<br>
<br>
C30 Compiler found<br>
<br>
C30 Compiler found<br>
<br>
&gt;&gt; <br>
<br>
<br>
<br>
 I was trying to attach the .mdl file and the .c function but I do not know how to attach the files.<br>
<br>
Can you explain me how to attach files?<br>
<br>
 Can you  tell me what am I doing wrong?<br>
<br>
<br>
<br>
Jose Luis</div>
</article>

<article class="forum-post" id="p634">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-11 17:44 UTC">2008-12-11 17:44 UTC</time></header>
<h3>Re: C function call block</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Simon_says</header>Can you explain me how to attach files?</blockquote><br>
Hi Jose Luis,<br>
<br>
<br>
<br>
To attach files on this forum, just look below the<strong> Save - Preview - Submit</strong> buttons, there is a tab : "<strong>upload attachement</strong>". <br>
<br>
It will help to see the model.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p636">
<header><strong>Simon_says</strong><time datetime="2008-12-12 20:08 UTC">2008-12-12 20:08 UTC</time></header>
<h3>Re: C function call block</h3>
<div class="forum-post-body">Hi Lubin..  <br>
<br>
Here are the  .mdl and .c files. I am just trying to turn a pair of leds when the ADC reads more than 2.5V or less than 1.5V. I wanted to use the C function call in order to lear how to use it. I decided to use the example format you posted and it compiles succesfully. However, I program the dsPIC30f4012 and it  just turns led  RD1 on. That´s all it does. No response to ADC input...nothing. Just RD1 on. <br>
<br>
 Can you suggest me please?<br>
<br>
<br>
<br>
Thanks a lot!<br>
<br>
<br>
<br>
 I was trying to see the C call function output with the matlab scope, but there is no output... Is it posible to simulate and check the performance before program the dsPIC?<br>
<br>
<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/160-call6.mdl">Pièce jointe : call6.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/161-callf6.c">Pièce jointe : callf6.c</a></p>
</article>

<article class="forum-post" id="p637">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-13 01:45 UTC">2008-12-13 01:45 UTC</time></header>
<h3>Re: C function call block</h3>
<div class="forum-post-body">Dear Joze Luis,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Simon_says</header>Is it posible to simulate [C function block] before program the dsPIC?</blockquote><br>
No, C function block will have no behaviour in a simulation. (Like all others blocks from the dsPIC library)<br>
<br>
<br>
<br>
I had a quick glande on your model.<br>
<br>
Sample time are Ok for every blocks ; thanks ! (It's a common source of error)<br>
<br>
<br>
<br>
I noticed a <strong>datatype </strong>error in the C file that make the condition (&lt;=  256) always true and the condition ( &gt;= 512) false !<br>
 <pre><code>&lt;i&gt;
&lt;/i&gt;#include &lt;p30f4012.h&gt;
unsigned char call6(unsigned char Input)
{	
	unsigned char Temp;
	Temp = (Input);
<wbr>
	return Temp;       
} 
</code></pre><br>
should be : <br>
 <pre><code>&lt;i&gt;
&lt;/i&gt;#include &lt;p30f4012.h&gt;
unsigned int call6(unsigned int Inputtt)
{	
	unsigned int Temp;
	Temp = (Inputtt);
<wbr>
	return Temp;       
} 
</code></pre><br>
<br>
Be aware that a global variable called Input is declared by the simulink model. You also use a variable named Input inside your function (That may cause trouble). You may considere to rename this variable either in your C function file or in the simulink model file or just directly connect ADC to C function Call.<br>
<br>
<br>
<br>
It should works ! However, I did not tested on the dsPIC. Let us know !<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p676">
<header><strong>Simon_says</strong><time datetime="2009-01-08 16:14 UTC">2009-01-08 16:14 UTC</time></header>
<h3>Re: C function call block</h3>
<div class="forum-post-body">Hi Lubin.. Sorry for the delay of my response...<br>
<br>
 Happy new year to all of you! This season I did not work at all, but now I have tested the model and I can see what my mistakes were. It works as you suggested!!! I have implemented it in a dsPIC and it is working. Thanks a lot. I am continuing experimenting and learning. I´ll get back to you again soon.<br>
<br>
<br>
<br>
Jose Luis</div>
</article>

