---
title: "counter application"
url: "/forum/topic/66/"
archiveKind: "topic"
---
# counter application

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p129">
<header><strong>learner</strong><time datetime="2007-11-30 15:25 UTC">2007-11-30 15:25 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I am considering to use your dsPIC simulink blockset for my project and I have tested some blocks on my target board and it works really great! However, one application that I am really concerned about is the use of timer as counter. I need to count the input pulses (with frequency varies from 1k Hz to 300k Hz) using a timer, and read the counted value - then reset it - periodically. But I have no idea on how to use your blockset to implement this, as it seems that there is no block that can directly do this. Your suggestions on this issue will be greatly appreciated.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Learner</div>
</article>

<article class="forum-post" id="p130">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-02 11:10 UTC">2007-12-02 11:10 UTC</time></header>
<div class="forum-post-body">Hi Learner,<br>
<br>
<br>
<br>
I’m glad that the blockset succeed to program your board. Thanks for this interesting problem. Could you give more detail about it. What do you want to count?<br>
<br>
<br>
<br>
About your problem, setting the time step of the simulink diagram to 1/300KHz = 3.3us will probably not work!<br>
<br>
With the dsPIC peripheral supported by the blockset, you could measure easily the period or duty cycle of your signal (good for monitoring motor speed…)<br>
<br>
  One peripheral not supported by the blockset is QEI interface. It can count, but you should check if it will work in your case (not a quadrature signal I guess). You could add this peripheral to simulink using the ‘Custom C function’. Note that this block is not available on the evaluation version of the blockset.<br>
<br>
Last solution I see is to use the interrupt function. The block will only tell if, at least, one interrupt appears during the time step. It will not provide you with the number of interrupt that appears. So, You should implement the function by yourself (Custom C function again !). Note however that counting 300Khz signal is feasible in theory, but the dsPIC would not be able to do something else…<br>
<br>
<br>
<br>
I would suggest using an external dedicated logic component that you will control with the dsPIC...<br>
<br>
<br>
<br>
I hope it help. I would be glad to get your final solution!<br>
<br>
If you have any suggestion for the blockset (ideas for new blocks), feel free to post it…<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p131">
<header><strong>learner</strong><time datetime="2007-12-03 16:50 UTC">2007-12-03 16:50 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for your reply on the counter issue. Like you suggested, I think the "C Function Call" block can do the work. However, I still think that a couple of Simlink blocks capable of doing the timer/counter configuration, control and reading/resetting will be the perfect solution since that would be where the advantage of using the blockset is. Technically, I guess that implementing the timer/counter blocks would be pretty much similar to implementing the other peripherals like serial port.<br>
<br>
<br>
<br>
Another issue that I am having is the follwoing error message I got when I started to run or build a simple model consisting of only two blocks - "Master" (configured to use dsPIC 30f3014) and "External Intterrupt &amp; PWM":<br>
<br>
<br>
<br>
        Error evaluating 'InitFcn' callback of Master block (mask) 'Master'. Index exceeds matrix dimensions.<br>
<br>
<br>
<br>
If I took off the "External Intterrupt &amp; PWM" block, the error was gone.<br>
<br>
<br>
<br>
Your suggestion on solving this problem would be greatly appreciated.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Learner</div>
</article>

<article class="forum-post" id="p132">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-04 10:36 UTC">2007-12-04 10:36 UTC</time></header>
<div class="forum-post-body">Hi Learner<br>
<br>
<br>
<br>
I understand that you want to make me working harder!<br>
<br>
As you mention, implementing the timer blocks would be pretty much similar to implementing the other peripherals: a nice piece a work!<br>
<br>
<br>
<br>
For counter, you should use a discrete resetable integrator provided in the simulink default library.<br>
<br>
 Except if you are running in ‘free run mode’, Timers are useless since they do not provide determinist result (may vary depending on interrupt, calculation time …)<br>
<br>
In fixed time step mode (through Timer 1, default, or through ADC) Resetable integrator will provide determinist result.<br>
<br>
<br>
<br>
I will however study the possibility to provide blocks with timer (no guarantee yet). The main difficulty is that timer are configured automatically with peripheral. Modifying timer may corrupt peripheral operation.<br>
<br>
<br>
<br>
Thank you for reporting the error you get. It is a bug of the blockset on the timer configuration routine. In its current version, at least one Output Compare (OC) or Input Capture (IC) must be present on the diagram to get a correct Timer configuration. I suggest you to add one of these peripheral, even if you do not use it.<br>
<br>
The bug is already corrected and new version will be release in few weeks.<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p133">
<header><strong>learner</strong><time datetime="2007-12-04 16:30 UTC">2007-12-04 16:30 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks again for your reply.<br>
<br>
<br>
<br>
If I go with the "C Function Call" block (I know it is only available for full version), <br>
<br>
<br>
<br>
1) Is there any restrictions/limitations for me to write/read any Special Function Registers (SFR) of the dsPIC within the C code (provided I don't corrupt other code)?<br>
<br>
<br>
<br>
2) Can I use all the resources (function calls, headers, etc..) that are provided by the MPLAB C30?<br>
<br>
<br>
<br>
3) Can I make a C function call as either initialization (i.e., configuration) or in the loop (i.e., gets executed every sampling circle).<br>
<br>
<br>
<br>
Your kind help will be a great help for my solution.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Learner</div>
</article>

<article class="forum-post" id="p134">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-04 22:19 UTC">2007-12-04 22:19 UTC</time></header>
<h3>C function Call</h3>
<div class="forum-post-body">Hi Learner,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : learner</header><br>
If I go with the "C Function Call" block (I know it is only available for full version)<br>
<br>
<br>
<br>
1) Is there any restrictions/limitations for me to write/read any Special Function Registers (SFR) of the dsPIC within the C code (provided I don't corrupt other code)?<br>
</blockquote><br>
You could write any PIC register that you can reach with C instruction (you could not change the dsPIC Quartz, PLL, Watch dog and that kind of  configuration, But you could write any register of Timer, ADC, any peripheral...)<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : learner</header><br>
2) Can I use all the resources (function calls, headers, etc..) that are provided by the MPLAB C30?<br>
</blockquote><br>
Yes, you will have to declare in you C file the appropriate library declaration (h file). The default dsPIC library is linked during the linking process. <br>
<br>
<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : learner</header><br>
3) Can I make a C function call as either initialization (i.e., configuration) or in the loop (i.e., gets executed every sampling circle).<br>
</blockquote><br>
The C function call block has a configurable sampling time :<br>
<br>
Set the sampling time to "inf" for the C function that will initialize (run only once at diagram starting point)<br>
<br>
Set the sampling time to "-1" or to the sample time needed to call the function at each diagram time step, or any integer multiple of the base time step for multirate diagram. (See multirate model in matlab help for more info about  TimeStep/rate)<br>
<br>
<br>
<br>
Learner, I propose If you are OK to send me a simple mdl model file with your custom C file containing your two functions (initialization and the function to be called each time step with input and output if any). I compile it on my computer and I build the help page with that example.<br>
<br>
<br>
<br>
Thanks for theses interesting question.<br>
<br>
<br>
<br>
For your previous question you may use a counter configured to count from an external Pin (not from the internal clock).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p135">
<header><strong>learner</strong><time datetime="2007-12-10 19:36 UTC">2007-12-10 19:36 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Thanks for your answers for my questions.<br>
<br>
<br>
<br>
Here is another question: when I build your example model dsPIC_33f_Explorer16.mdl I got the following error message:<br>
<br>
<br>
<br>
error: Invalid -mcpu option.  CPU 33FJ256GP710 not recognized.<br>
<br>
<br>
<br>
while the other three examples succeeded in building. I noticed that the other three examples use dsPIC30f processors while the one with build error uses dsPIC33f processor.<br>
<br>
<br>
<br>
Your suggestion on this issue would be greatly appreciated.<br>
<br>
<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Learner</div>
</article>

<article class="forum-post" id="p136">
<header><strong>LubinKerhuel</strong><time datetime="2007-12-10 22:00 UTC">2007-12-10 22:00 UTC</time></header>
<div class="forum-post-body">Hi Learner,<br>
<br>
<br>
<br>
It seems this is a compiler problem. I guess it do not find the definitions files for 33f mcu on your computer. It is working on my computer. <br>
<br>
<br>
<br>
Did you install the definition files for the 33f mcu familly ?<br>
<br>
<br>
<br>
Could you update your C30 compiler and install the last MPLAB (including support for 33f mcu) ?<br>
<br>
<br>
<br>
If this does not solve the problem, please provide more details.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p137">
<header><strong>learner</strong><time datetime="2007-12-11 16:25 UTC">2007-12-11 16:25 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
I updated my old version of C30 and now it works.<br>
<br>
<br>
<br>
Thanks!<br>
<br>
<br>
<br>
Learner</div>
</article>

