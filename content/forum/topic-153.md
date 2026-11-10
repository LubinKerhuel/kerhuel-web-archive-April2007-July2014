---
title: "C-Function Call and Muxes - to solve"
url: "/forum/topic/153/"
archiveKind: "topic"
---
# C-Function Call and Muxes - to solve

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p487">
<header><strong>malife</strong><time datetime="2008-09-01 02:37 UTC">2008-09-01 02:37 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 This another bug that has been killing me all day and have not found a work-around. I have three separate signals that come from different sources and have different widths. They are joined by a mux and then passed on to a C-Function call. The problem is that the signal is overall 46 bytes wide, but it only allocates space in the code generation for the first one that goes into the mux (26) so when I try to read all the input, after 26 bytes I get junk. I wonder what the global input parameter does in the C-Function call, because I explicitly say 46 (otherwise it would no let me compile) but the code that is generated, reuses the output from my first block, the GPS parser.<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;uint8_T GPSSentenceParser_o1[27];    /* '&lt;S2&gt;/GPS Sentence Parser' */
</code></pre><br>
<br>
This is REALLY a show stopper. Please take a look at it. I can not post the model/code, but if you want me to email you the model, let me know.<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p488">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-01 07:37 UTC">2008-09-01 07:37 UTC</time></header>
<h3>Re: C-Function Call and Muxes</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
I am just back and "setting up" my flat again!<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : malife</header>I wonder what the global input parameter does in the C-Function call</blockquote> <br>
<br>
The <strong>Global Input <em>Size</em></strong> parameters set all input with the defined size.<br>
<br>
If that size is 1, each input is considered as a scalar. (Simulink call the function with the value as parameter)<br>
<br>
If that size is greater than 1, each input is considered as a vector. (Simulink call the function using pointers)<br>
<br>
<br>
<br>
From the function call block point of view, there is no difference if the input size is 2 or 100. The pointer provided by Simulink is taken as is.<br>
<br>
<br>
<br>
I can propose few independent solutions that you perhaps already tested: <br>
<br>
<br>
<br>
- change the optimization option of the real time workshop (like "reuse signal").<br>
<br>
- use the input of the C call function with 3 independent vector input (i.e. size of the global input Size parameter greater than 2) and mux the three input in the C function.<br>
<br>
- Set the output of the GPS parser block with a size of 46 (so the 20 last bytes are not used) and use the Simulink standard block that can fill in a vector starting at a defined index (here 21 for the 2nd input and so on...)<br>
<br>
<br>
<br>
It is not clear to me how Simulink mux vectors and if the RTW optimization parameters change the way it do it. I will look at that as soon as I unpack my computer (I am using the old vacation laptop that does not like matlab at all ;-)<br>
<br>
<br>
<br>
To have a close look on theses bugs, it is always helpful to get model with the bug. I would be glad if you could send it (or a simplified version with the same bug!)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p604">
<header><strong>malife</strong><time datetime="2008-11-03 01:58 UTC">2008-11-03 01:58 UTC</time></header>
<h3>Re: C-Function Call and Muxes - to solve</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 Just wanted to follow up on the Muxes issue. I can positively confirm that Muxes do not work with the code translation. I don't know if it is the matlab version, the blockset version or some of the code simplification settings. But to work around this what I do is for every mux I use instead an embedded matlab function that does exactly what a Mux would do. This solves the problem. Demuxes work just fine which is strange. Anyways, no show stopper but just wanted to let everyone know that if they see a funny behavior and muxes are involved, try substituting them with an embedded matlab block like:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;function y = myMux (u1, u2);
y = zeros(9,1) % size of output vector
<wbr>
y = [u1(:); u2(:)];
</code></pre> <br>
<br>
<br>
<br>
and see if this fixes the issue. Would be happy to discuss this further.<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p1622">
<header><strong>ismaeelbit</strong><time datetime="2011-06-25 10:48 UTC">2011-06-25 10:48 UTC</time></header>
<h3>Re: C-Function Call and Muxes - to solve</h3>
<div class="forum-post-body">Hi Malife,<br>
<br>
Can you share with me how you implment gps parser with this blockset. I have trying to do similar things since using C-call function for a gps which does not work still.<br>
<br>
thanks</div>
</article>

