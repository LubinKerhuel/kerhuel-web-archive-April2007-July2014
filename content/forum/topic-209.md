---
title: "Interrupt function instead of a while cicle?"
url: "/forum/topic/209/"
archiveKind: "topic"
---
# Interrupt function instead of a while cicle?

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p792">
<header><strong>graele</strong><time datetime="2009-03-19 18:56 UTC">2009-03-19 18:56 UTC</time></header>
<div class="forum-post-body">Hello everybody..<br>
<br>
<br>
<br>
The generated code substantially work with a for cicle of this type:<br>
<br>
<br>
<br>
  for (;;) {<br>
<br>
    /* Associate rt_OneStep() with a timer that executes at the base rate of the model */<br>
<br>
    while (!_T1IF);<br>
<br>
    _T1IF = 0;<br>
<br>
    rt_OneStep();<br>
<br>
  }<br>
<br>
<br>
<br>
so, that everytime the timer generates the interrupt, the flag changes and, after resetting it, the program executes the step routine..<br>
<br>
<br>
<br>
I wonder about the differences if I implement it by changing the code in a different way.. like this for example:<br>
<br>
  for (;;) {<br>
<br>
     // my code...<br>
<br>
  }<br>
<br>
<br>
<br>
and then I call the step routine from the timer interrupt function...<br>
<br>
<br>
<br>
void __attribute__((interrupt, no_auto_psv))_T0Interrupt(void) {<br>
<br>
   _T1IF = 0;<br>
<br>
   rt_OneStep();<br>
<br>
}<br>
<br>
<br>
<br>
I'm thinking about this solution so that I can put my control routine in rt_onestep.. and this is called each T time.. assuming that for the routine it takes Tr time,<br>
<br>
I can efford the other code in the T-Tr time without compromising the performance of my control algorithm..<br>
<br>
<br>
<br>
What do you think about this solution? Can it really improve my control algorithm as I'm thinking, or is there something I'm not considering??<br>
<br>
<br>
<br>
Manu</div>
</article>

<article class="forum-post" id="p795">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-21 15:42 UTC">2009-03-21 15:42 UTC</time></header>
<h3>Re: Interrupt function instead of a while cicle?</h3>
<div class="forum-post-body">Hi Grael, <br>
<br>
<br>
<br>
This is a good solution to run a task in background (i.e., with a low priority). This background task will be interrupted (preempted) by the main control task..<br>
<br>
<br>
<br>
On some microcontrollers, calling function from interrupt may cause problems. That must be tested/checked.<br>
<br>
Just set the timer interrupt to the lowest priority to allow others interrupt to execute.<br>
<br>
<br>
<br>
Btw, I do not know how to make a background task from simulink. So, except if you add manually the background task (modifying generated C code ), there is no interrest to add this possibility (in the master block for example). Anyway, If you know a way to do it from simulink directly, please let me know...<br>
<br>
<br>
<br>
Ps: Wat about using a multirate model ? you could divide tasks of your background tasks and execute them at lower rates to not disturb the main real time algorithm.<br>
<br>
<br>
<br>
Lubin</div>
</article>

