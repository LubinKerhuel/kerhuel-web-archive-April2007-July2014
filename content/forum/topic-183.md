---
title: "problem with master and ADC block"
url: "/forum/topic/183/"
archiveKind: "topic"
---
# problem with master and ADC block

Forum : [General Remark and Questions](/forum/#forum-1)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p639">
<header><strong>crh</strong><time datetime="2008-12-18 10:36 UTC">2008-12-18 10:36 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
I started some time ago with microcontrollers. <br>
<br>
I rebuild your first model with the compare block and compiled it. No problems.<br>
<br>
Now, I try to compile a model with a master block and an ADC block. <br>
<br>
In the error screen I received  the following message:<br>
<pre><code>Error building Real-Time Workshop target for block diagram 'BCwithBPfilter'. MATLAB error message: Error using ==&gt; genMakefileAndBuild at 1070
  Error(s) encountered while building model "BCwithBPfilter"
<wbr>
And in the Matlab workspace at the end:
BCwithBPfilter.o: Link Error: Could not allocate section .nbss, size = 13522 bytes, attributes = bss near  Link Error: Could not allocate data memory gmake: *** [..\../BCwithBPfilter.coff] Error 255 
### Real-Time Workshop build procedure for model: 'BCwithBPfilter' aborted due to an error.
C30 Compiler found</code></pre><br>
I suppose there are some mismatches in the settings of the block parameters. I tried to attach the mdl file, but I received the message: size too big.<br>
<br>
Kind regards, Casparus</div>
</article>

<article class="forum-post" id="p641">
<header><strong>LubinKerhuel</strong><time datetime="2008-12-18 12:49 UTC">2008-12-18 12:49 UTC</time></header>
<h3>Re: problem with master and ADC block</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
I just increased the max upload size from 256Ko to 2 Mo. You shoudl be able to upload your file now.<br>
<br>
<br>
<br>
If you just have an ADC block with a Master block, there is a problem !<br>
<br>
<br>
<br>
I guess that you implement a filter. If you are using a FIR filter, you may have too many coefficients.<br>
<br>
go to Configuration ==&gt; options parameters ==&gt; Optimization == &gt; check "inline paramemters". That may uses less RAM memory.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p645">
<header><strong>crh</strong><time datetime="2008-12-18 15:15 UTC">2008-12-18 15:15 UTC</time></header>
<h3>Re: problem with master and ADC block</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
I cannot believe myself, but now I managed to compile. But the process takes an extreme long time. I do not know if this is a normal situation for models with a filter.<br>
<br>
I uploaded my model in the attachment. <br>
<br>
I am very busy to study the filters. So far, as I understand fixed filters are using less space. But, I still wonder if there are some common problems (with the use of an ADC and gain block)to implement them in dsPic30F43013.<br>
<br>
For fewer coefficients I already checked the box: inline parameters. I did this already yesterday. For this, I used the model adviser, a very useful and easy tool.<br>
<br>
Kind regards, Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/166-BCwithBPfloat1.mdl">Pièce jointe : BCwithBPfloat1.mdl</a></p>
</article>

<article class="forum-post" id="p682">
<header><strong>malife</strong><time datetime="2009-01-11 05:58 UTC">2009-01-11 05:58 UTC</time></header>
<h3>Re: problem with master and ADC block</h3>
<div class="forum-post-body">Hello All,<br>
<br>
 This problem, which really is not a problem but a compiler feature is related with near and far code (data and code) take a look at the C30  compiler documentation so you can set the flags accordingly in the compiler settings in matlab. I've been through this error before. <br>
<br>
<br>
<br>
Regarding the long compilation time, if you are using dsp blocks in matlab the first time you compile takes a very long time since it is generating object files for many functions even if you do not use them directly. The second time around should be much faster. If not you might have some setting wrong.<br>
<br>
<br>
<br>
Hope this helps.</div>
</article>

<article class="forum-post" id="p691">
<header><strong>crh</strong><time datetime="2009-01-15 07:32 UTC">2009-01-15 07:32 UTC</time></header>
<h3>Re: problem with master and ADC block</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
Everything is clear now. Thanks for your help,<br>
<br>
<br>
<br>
regards, Casparus</div>
</article>

