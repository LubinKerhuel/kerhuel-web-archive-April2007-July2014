---
title: "Error after using Integer to Bit Converter"
url: "/forum/topic/251/"
archiveKind: "topic"
---
# Error after using Integer to Bit Converter

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p982">
<header><strong>cjaskolski</strong><time datetime="2009-11-04 20:55 UTC">2009-11-04 20:55 UTC</time></header>
<div class="forum-post-body">I recieve the error message "Error building Real-Time Workshop target for block diagram 'PIC_vector_concatenate_test'. MATLAB error message:<br>
<br>
Error using ==&gt; RTW.genMakefileAndBuild at 967 Error(s) encountered while building model "PIC_vector_concatenate_test". " when I try to use Vector Concatenate to join a constant vector of booleans and a vector of booleans created through the Simulink block "Integer to Bit Converter". I do not get this error when I try to join any other boolean vectors... just when I use Integer to Bit Converter. I am using Matlab r2007a and have sucessfully run other models using your blockset.<br>
<br>
<br>
<br>
Model file is attached.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/274-PIC_vector_concatenate_test.mdl">Pièce jointe : PIC_vector_concatenate_test.mdl</a></p>
</article>

<article class="forum-post" id="p984">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-04 22:52 UTC">2009-11-04 22:52 UTC</time></header>
<h3>Re: Error after using Integer to Bit Converter</h3>
<div class="forum-post-body">I was able to test your model on a<strong> 2009b matlab</strong> with the communication blockset and<strong> it compiled</strong> without requiring any modifications.<br>
<br>
<br>
<br>
I do not have installed the communication blockset (for the integer to Bit Converter block) on the <strong>2007a matlab</strong> version. However, you may post one more time the model, but before uploading the model, right click on the Bit Converter Block and press disable link and one right click again to break link. Thus, I may test it with matlab 2007a. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p987">
<header><strong>cjaskolski</strong><time datetime="2009-11-05 00:58 UTC">2009-11-05 00:58 UTC</time></header>
<h3>Re: Error after using Integer to Bit Converter</h3>
<div class="forum-post-body">Thank you for the swift reply. I have attached the model after following your instructions to disable and break the link. I can test it on 2007b and an evaluation version of 2009b here as well if this doesn't work.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/276-PIC_vector_concatenate_test_link_disabled_and_break.mdl">Pièce jointe : PIC_vector_concatenate_test_link_disabled_and_break.mdl</a></p>
</article>

<article class="forum-post" id="p990">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-05 09:06 UTC">2009-11-05 09:06 UTC</time></header>
<h3>Re: Error after using Integer to Bit Converter</h3>
<div class="forum-post-body">Ok, I can open the model with the block with matlab 2007b, but it will not compile because it needs an S function that is in the communication blockset that is not installed. Thus, I still cannot test it with matlab 2007b until I install the comm blockset.<br>
<br>
<br>
<br>
Anyway, the first model you upload compiled correctly with matlab 2009b. Thus, I guess it is a bug from matlab 2007b (that generate code that can't be understand by C30). Anyway, there are options on how to represent boolean values in the real time workshop configuration parameters. Perhaps playing with theses parameters may help.<br>
<br>
<br>
<br>
I noticed a difference between the dialog box the integer to bit converter of matlab 2007b with the one of matlab 2009b. I attached the one of maltlab 2009b :<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/277-shot_20091105095911-218.png">Pièce jointe : shot_20091105095911-218.png</a></p>
</article>

