---
title: "Possible bug in ADC of dsPIC30F6010A"
url: "/forum/topic/133/"
archiveKind: "topic"
---
# Possible bug in ADC of dsPIC30F6010A

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p404">
<header><strong>NigmaTech</strong><time datetime="2008-05-31 18:01 UTC">2008-05-31 18:01 UTC</time></header>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
Could You check connections of pin AN7 and AN3 in your blockset? It's very strange, but when I want to convert AN7 analog input, dsPIC is converting different value than it's real. I checked all connections in my PCB and that value is on pin AN3. Is this possible, AN3 and AN7 are changed places? <br>
<br>
<br>
<br>
Blockset version 0.98</div>
</article>

<article class="forum-post" id="p405">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-31 20:14 UTC">2008-05-31 20:14 UTC</time></header>
<h3>Re: Possible bug in ADC of dsPIC30F6010A</h3>
<div class="forum-post-body">Hi Nigma,<br>
<br>
<br>
<br>
This would be quite surpising to have an inversion on pin AN7 ==&gt; AN3.<br>
<br>
Could you upload the model (.mdl file) so as to have a look ?<br>
<br>
What are the parameters for Vref+ and Vref- ?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p406">
<header><strong>NigmaTech</strong><time datetime="2008-05-31 20:42 UTC">2008-05-31 20:42 UTC</time></header>
<h3>Re: Possible bug in ADC of dsPIC30F6010A</h3>
<div class="forum-post-body">I used AVdd - AVss.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/88-Gyro_test.mdl">Pièce jointe : Gyro_test.mdl</a></p>
</article>

<article class="forum-post" id="p407">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-01 22:06 UTC">2008-06-01 22:06 UTC</time></header>
<h3>Re: Possible bug in ADC of dsPIC30F6010A</h3>
<div class="forum-post-body">The generated code for the configuration of the ADC with your model is : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt;  124     /* S-Function "dsPIC_ADC" initialization Block: &lt;Root&gt;/ADC Input */
  125     /* Initialise ADC converter */
  126     /* 0 mean each 1 conversion */
  127   #define NoSamplesADC                   1
  128   #define ADCSval                        3
  129   #define SAMCval                        (1 &lt;&lt; 8)
  130   #define OutFormatBitsval               (0 &lt;&lt; 8)
  131   #define VoltRef                        (0 &lt;&lt; 13)
  132   
  133     
  134     ADCON1 = 0x00E4 | (0 &lt;&lt; 10)| OutFormatBitsval;
  135     ADCON2 = 0x0400 | (NoSamplesADC &lt;&lt; 2) | VoltRef;
  136     ADCSSL = 144;
  137     ADCON3 = (ADCSval | SAMCval) &amp; 0xff7f;
  138     ADCHS = 0x0000;
  139     IPC2 = (IPC2 | (6 &lt;&lt; 12));           /*Interrupt Priority : 6*/
  140     _ADIF = 0;
  141   
  142  
  143   
  144   
  145     /* Turn on ADC Module */
  146     ADCON1bits.ADON= 1;
</code></pre><br>
<br>
To read the converted values, the code is : <br>
<pre><code>&lt;i&gt;
&lt;/i&gt;   39       /* S-Function "ADC" Block: &lt;Root&gt;/ADC Input */
   40       Gyro_test_B.ADCInput_o1 = ADCBUF0;
   41       Gyro_test_B.ADCInput_o2 = ADCBUF1;
</code></pre><br>
<br>
If there is something wrong with that, I would be glad to correct it.</div>
</article>

