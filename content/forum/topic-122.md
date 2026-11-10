---
title: "Passing a Vector to the C-Function Call block"
url: "/forum/topic/122/"
archiveKind: "topic"
---
# Passing a Vector to the C-Function Call block

Forum : [bug reports](/forum/#forum-8)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p360">
<header><strong>malife</strong><time datetime="2008-05-16 21:18 UTC">2008-05-16 21:18 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I am trying to pass a vector to the C-Function Call block but apparently it is only getting the first element in that vector: You can see in the image shown below I assemble a vector using a Mux, and then pass it to the C function call, but the call to the function call is this:<br>
<br>
<br>
<pre><code>* S-Function "dsPIC_Digital_OutputWrite" Block: &lt;Root&gt;/Digital Output Write3 */
  LATBbits.LATB2 = FALSE;
<wbr>
  /* S-Function "dsPIC_C_function_Call" Block: &lt;Root&gt;/C Function Call */
  myPutSPI(8U);
<wbr>
  /* S-Function "dsPIC_Digital_OutputWrite" Block: &lt;Root&gt;/Digital Output Write2 */
  LATBbits.LATB2 = TRUE;</code></pre><br>
<br>
which is of course wrong since the function myPutSPI is expecting a vector and not a constant. Any ideas what I am doing wrong? Is this a bug? I have attached the code so you can verify it for yourself.<br>
<br>
<br>
<br>
Thanks!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/76-spi.JPG">Pièce jointe : spi.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/78-spi.zip">Pièce jointe : spi.zip</a></p>
</article>

<article class="forum-post" id="p361">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-16 22:24 UTC">2008-05-16 22:24 UTC</time></header>
<h3>Re: Passing a Vector to the C-Function Call block</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
<br>
<br>
I confirm the bug.<br>
<br>
Will fix that shortly !<br>
<br>
<br>
<br>
I propose the following solution (while I am working on that bug !) <br>
<br>
<br>
<br>
- add an output to the C function call block (like char or whatever)<br>
<br>
- uncheck the "inline parameters" in Simulation ==&gt; Configuration Parameters ==&gt; Optimization<br>
<br>
<br>
<br>
This solution is working on my blockset version. Note that I already made some change on the C function call block that are not yet published (blockset still in developments).<br>
<br>
If you encounter a problem with the "dirty" solution proposed here, let me know.<br>
<br>
<br>
<br>
Anyway, I will correct that bug soon. Thanks for reporting it !</div>
</article>

<article class="forum-post" id="p362">
<header><strong>malife</strong><time datetime="2008-05-16 23:14 UTC">2008-05-16 23:14 UTC</time></header>
<h3>Re: Passing a Vector to the C-Function Call block</h3>
<div class="forum-post-body">Thanks for a very quick response. I will try what you suggest and report back. <br>
<br>
<br>
<br>
If it does not work I will wait for the next version. <br>
<br>
<br>
<br>
DMA SPI si comming along, hope to give positive reports soon :-)<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p363">
<header><strong>malife</strong><time datetime="2008-05-16 23:20 UTC">2008-05-16 23:20 UTC</time></header>
<h3>Re: Passing a Vector to the C-Function Call block</h3>
<div class="forum-post-body">Yes, that took care of it. I confirm the work around solves the problem.<br>
<br>
<br>
<br>
Thanks for excellent support!<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p369">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-18 22:50 UTC">2008-05-18 22:50 UTC</time></header>
<h3>Re: Passing a Vector to the C-Function Call block</h3>
<div class="forum-post-body">Hi, I corrected the bug : if you have only one input vector, you do not need to add an (unused) output to the function.<br>
<br>
This will be available in the next version (i.e. 0.97b)<br>
<br>
<br>
<br>
Remark about the inline parameters :<br>
<br>
When the C call function use input vectors with more than 2 elements (an array in C language), the adress of the first element (pointer) is passed to the C function . <br>
<br>
In your exemple, when inline parameters is checked in simulink options, the first element of the array is a constant. This constant may not be stored next to the remaining vector variables values.<br>
<br>
<br>
<br>
When inline parameters, the vectors intern variable usually follows each other in memory. (from experiment, I did not read anything about it)<br>
<br>
Thus, I suggest to use an intermediate variable : <br>
<br>
I wish you good luck with SPI using DMA !<br>
<br>
<br>
<br>
Right now, I have done a new SPI block that use interrupt (but no DMA) However, It works only in master mode. It is usefull if you read data from external component (ADC, gyro or others) and have stringent real-time constraints. I will try to extend to slave mode.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/79-C_funCall_WithInterVariable.png">Pièce jointe : C_funCall_WithInterVariable.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/80-SPI_CFunctionCall.zip">Pièce jointe : SPI_CFunctionCall.zip</a></p>
</article>

<article class="forum-post" id="p1298">
<header><strong>bmairs</strong><time datetime="2010-09-16 16:08 UTC">2010-09-16 16:08 UTC</time></header>
<h3>Re: Passing a Vector to the C-Function Call block</h3>
<div class="forum-post-body">This bug still exists. I'd like to keep inline parameters checked as an optimization, is there anyway to fix this on your end, Lubin, or is this something that we're just going to have to deal with?<br>
<br>
<br>
<br>
Mariano did find that replicating a Mux block with an embedded Matlab block fixed the bug. I'm not certain if that helps to fix this.</div>
</article>

