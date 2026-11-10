---
title: "MPLAB C30 Optimizations"
url: "/forum/topic/252/"
archiveKind: "topic"
---
# MPLAB C30 Optimizations

Forum : [General Remark and Questions](/forum/#forum-1)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p983">
<header><strong>cjaskolski</strong><time datetime="2009-11-04 20:57 UTC">2009-11-04 20:57 UTC</time></header>
<div class="forum-post-body">I am using an evaluation version of the C30 compiler that has expired and thus doesn't support some optimizations. Do you know if the the blockset uses these optimizations? I would like to avoid buying the C30 compiler ($800), but if the optimizations are actually used by the blockset and will make my code run faster, I will do so and I am using a fair bit of the processor load.</div>
</article>

<article class="forum-post" id="p985">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-04 23:06 UTC">2009-11-04 23:06 UTC</time></header>
<h3>Re: MPLAB C30 Optimizations</h3>
<div class="forum-post-body">In Simulation==&gt;Configuration Parameters ==&gt; dsPIC options (last item on the left) and Optimisation parameter: OPTIM_GCC :<br>
<br>
There are the following optimisations parameters: <strong>-O3 -fschedule-insns -fschedule-insns2</strong><br>
<br>
<br>
<br>
Thus, if your C30 version is expired, compilation optimisations are not working anymore.<br>
<br>
<br>
<br>
Three solutions:<br>
<br>
- Check that you really need theses optimisation: you can use options in the master block to check real-time constraints, or more precisely, use the <a href="/wiki/dspic-block-calculus-time-step/">Calculus Time step</a>  and/or the <a href="/wiki/dspic-block-chronograph/">Chronograph</a> block for making precise real-time measurement (I am sorry, theses block are very badly documented. Ask is you are to use them)<br>
<br>
- <strong>Uninstall</strong>, then <strong>clean-up registry</strong> (remove all you can find about C30) and <strong>re-install</strong> again (however, that may be illegal, depending on the agreement you accepted while installe installing C30, please check first).<br>
<br>
- Microchip C30 is based on GCC compiler. Thus, Microchip has to publish its source code due to the <strong>GCC open source licence</strong>. You just need to find this source code on the microchip website, and compile it. (I think!)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p988">
<header><strong>cjaskolski</strong><time datetime="2009-11-05 01:02 UTC">2009-11-05 01:02 UTC</time></header>
<h3>Re: MPLAB C30 Optimizations</h3>
<div class="forum-post-body">Lubin,<br>
<br>
<br>
<br>
This is the information I was looking for. Thanks for the reply and thanks for making such a great product. I have 3 times tried installing the evaluation blockset from Microchip on Matlab 2007a, 2007b, and 2009b and get different errors each time either during installation or trying to run a simple mode. In all cases, Microchip was unable to help. In contrast, I was up and running a fairly complex model with your block set in 2 hours.<br>
<br>
<br>
<br>
 I am planning on buying a license in the next few weeks and am glad my money goes to you instead of Microchip!</div>
</article>

<article class="forum-post" id="p991">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-05 09:19 UTC">2009-11-05 09:19 UTC</time></header>
<h3>Re: MPLAB C30 Optimizations</h3>
<div class="forum-post-body">Hi Corey,<br>
<br>
<br>
<br>
I am glad that you enjoy the blockset I created.<br>
<br>
As you probably noticed, Microchip blockset started its blockset (<a href="/wiki/review/">inspired</a> partly based on my work), and is now a great challenger. This kind of testimonial is exactly what I am looking for. <br>
<br>
Please feel free to copy it or write similar remark (even positive or negative) on the <a href="/wiki/customer-feedback/">user feedback webpage</a> ! Note that you will be able to modify it whenever you want. (You’ll need to create an account on the wiki)<br>
<br>
<br>
<br>
Lubin</div>
</article>

