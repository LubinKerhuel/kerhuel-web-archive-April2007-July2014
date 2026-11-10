---
title: "fuzzy logic"
url: "/forum/topic/187/"
archiveKind: "topic"
---
# fuzzy logic

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p663">
<header><strong>salemimoh</strong><time datetime="2009-01-07 20:48 UTC">2009-01-07 20:48 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I have tried to simulate a controller of the speed of a motor using fuzzy logic. After developing the model in MATLAB and transfer it to MPLAB V8.15a and build it. All went ok. But when i fired the program into the DSPIC30F6014 and tried to run it using microchip ICD2, it starts to run but it hangs up.  I then tried to run it in step by step mode using animate, it gave me the following error message. Is this due a shortage of program memory or what ? If this is the case, is it due to the number of rules implemented in the fuzzier where i am implementing 25 rules of the form (if rule1 and rule2 then decision) which makes the program too long so that it could not be accomodated into the programming memory? <br>
<br>
But if this is the case, i suppose the program could not be downloaded  into the DSPIC because an overflow  will take place.<br>
<br>
By the way, i tried to run the program in the MPLAB simulator and it did not work either.<br>
<br>
So could you please advise.<br>
<br>
Here are the error messages<br>
<pre><code>CORE-E0011: Trap due to unimplemented RAM or PSV memory access, occurred from instruction at 0x000688
CORE-E0001: Trap due to stack error, occurred from instruction at 0x000688
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688
CORE-W0008: Software Reset Instruction called at PC=0x002f16</code></pre></div>
</article>

<article class="forum-post" id="p666">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 21:29 UTC">2009-01-07 21:29 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : salemimoh</header>After developing the model in MATLAB and transfer it to MPLAB V8.15a and build it</blockquote><br>
How did you transfer it to MPLAB ? are you using the dsPIC blockset for Simulink available on this website ?<br>
<br>
<br>
<br>
The hang up and restart behaviour is typical from trap error. Theses one are hard to find and solve. Look in the doc about memory, there may be compilation options to avoid this error. I do not know much than that. Try the microchip forum for further help on this.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p667">
<header><strong>salemimoh</strong><time datetime="2009-01-07 22:38 UTC">2009-01-07 22:38 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Dear Lubbin,<br>
<br>
What I did, is to build  the model in the MATLAB using the your blocksets. Then I built the system successfully.<br>
<br>
Then I loaded the resulting files into the MPLAB V8.15a in the way is explained in your tutorial. Then I tried to run it. I was faced with dilema the  I mentioned to you.</div>
</article>

<article class="forum-post" id="p683">
<header><strong>malife</strong><time datetime="2009-01-11 06:09 UTC">2009-01-11 06:09 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">If you are stepping through see in which instruction it fails. This might help us to help you. Also, try compiling the model with a "far" memory model. See the C30 Documentation. Also it might just be that the chip you are trying to use does not have enough RAM to perform whatever it is you are trying to do. Remember the fact that the hex fits in flash is no guarantee that you have enough RAM for the program to run. Try the exact same model on a dsPic with more RAM. Finally, stack overflow errors are typical of a huge amount of local variables. If you have a C function you wrote or you are using embedded matlab try declaring large local arrays as static (or persistent if in eml) and see if that solves it.<br>
<br>
<br>
<br>
Hope this helps<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p684">
<header><strong>salemimoh</strong><time datetime="2009-01-12 12:03 UTC">2009-01-12 12:03 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Dear Mario thanx for you help<br>
<br>
In the next  step  by step and what happened in W14 and w15 and where it jumps, probably you figure out the bug<br>
<br>
<br>
<br>
<br>
<br>
I executed the program in step by step mode. the instruction at address 686 is: <br>
<br>
<br>
<br>
<span style="color:#ff0000">00686  FA1B48     lnk #0x1b48 </span><br>
<br>
<br>
<br>
Before execution the registers contents are: <br>
<br>
<span style="color:#0000bf">W14 = 137C <br>
<br>
W15 =  1380 <br>
<br>
SPLIM = 2790 <br>
<br>
PC = 686 <br>
<br>
W8 =0x0000 </span><br>
<br>
<br>
<br>
After instruction's execution: <br>
<br>
<br>
<br>
<span style="color:#0000bf">W14 =1382 <br>
<br>
W15 = 2ECA <br>
<br>
SPLIM = 2790 <br>
<br>
PC = 688 <br>
<br>
W8 =0x0000 </span><br>
<br>
as expected then the problem starts from next at address 688 <br>
<br>
<br>
<br>
<span style="color:#ff0000">00688  781F88     mov.w 0x0010,[0x001e++] </span><br>
<br>
before  as above <br>
<br>
<br>
<br>
After here is the problem: <br>
<br>
<br>
<br>
<span style="color:#0000ff">W14 = 1382 <br>
<br>
W15 = 2ECE <br>
<br>
SPLIM = 2790 </span><br>
<br>
<span style="color:#0000ff">PC = 2A98 </span> which is out of the range of the program (last instruction is at address (2A96) <br>
<br>
<span style="color:#0000ff">W8= 0x0000 </span><br>
<br>
and the  following error messages occur: <br>
<br>
<br>
<pre><code>CORE-E0011: Trap due to unimplemented RAM or PSV memory access, occurred from instruction at 0x000688 
CORE-E0001: Trap due to stack error, occurred from instruction at 0x000688 
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688 
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688 
CORE-E0003: Trap due to unimplemented RAM memory access, occurred from instruction at 0x000688 
CORE-W0008: Software Reset Instruction called at PC=0x002a98 </code></pre><br>
<br>
next step PC = 0x00000000000 <br>
<br>
The question is why when excuting instruction at address 688, it does not go to next instruction at address: <br>
<br>
  <span style="color:#ff0000">0068A  804000     mov.w 0x0800,0x0000 </span><br>
<br>
and it goes wild as i explained?</div>
</article>

<article class="forum-post" id="p689">
<header><strong>malife</strong><time datetime="2009-01-15 01:00 UTC">2009-01-15 01:00 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Can you post a bit more about what you are doing (application wise) and which dsPIC you are using? Not really sure what is wrong. Evidently PC is getting lost for some reason.</div>
</article>

<article class="forum-post" id="p699">
<header><strong>salemimoh</strong><time datetime="2009-01-16 17:17 UTC">2009-01-16 17:17 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Dear Malife,<br>
<br>
What I am basically doing is to use MATLAB fuzzy logic. The number of rules implemented is 25 rules.<br>
<br>
As a guess, when the program is compiled in MATLAB then transfered to MPLAB, and built, those rules probably introduce too many loops which requires a larger stack. And that is probably the root of the error mentioned earlier.<br>
<br>
to solve it,<br>
<br>
I wrote a program in custom linker script as shown below.<br>
<br>
.stack :<br>
<br>
{<br>
<br>
__SP_init = .;<br>
<br>
. += 0x2000;<br>
<br>
__SPLIM_init = .;<br>
<br>
. += 8;<br>
<br>
} &gt;data <br>
<br>
<br>
<br>
Then i tried to call it from MPLAB custom build but it did not work yet.<br>
<br>
my question: What should i do to call when the program is built or Is there a better way how to increase the stack?</div>
</article>

<article class="forum-post" id="p700">
<header><strong>malife</strong><time datetime="2009-01-16 18:28 UTC">2009-01-16 18:28 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Hello Salemimoh,<br>
<br>
 I am not familiar with the Fuzzy logic toolbox (blockset?) in Matlab so I can not help you there. But I have previously encountered similar stack overflow problems, and as I mentioned in previous post, making the arrays and variables static (or persistent in matlab) did solve the problem. If this is an issue of too many nested loops I think you need to rethink your approach, because I don't know (but I don't think) there is much to do about growing the stack. Also unless you are at the top of the dsPIC family tree, try using a more capable chip, specially one with more RAM.<br>
<br>
<br>
<br>
Sorry I can not be of more help.<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p701">
<header><strong>salemimoh</strong><time datetime="2009-01-17 12:07 UTC">2009-01-17 12:07 UTC</time></header>
<h3>Re: fuzzy logic</h3>
<div class="forum-post-body">Dear malife<br>
<br>
I am using the DSPIC30F5014. It has a considarble memory. If fact I checked the memory used: It using 5906 from the program memory which is: 49152 <br>
<br>
and using 2934 from 8192 available. so there is still a considerable memory.<br>
<br>
I think the problem is how to relocate the stack and how to increase it. Thing which i could not solve up to now.<br>
<br>
There is a suggestion by usind custom linker script, I tired it but it gives a syntax error. I have looked in the literature and i could not find anything yet.</div>
</article>

