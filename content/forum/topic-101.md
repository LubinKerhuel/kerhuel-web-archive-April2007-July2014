---
title: "How much RAM area can a program use?"
url: "/forum/topic/101/"
archiveKind: "topic"
---
# How much RAM area can a program use?

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

13 message(s) · archive en lecture seule

<article class="forum-post" id="p274">
<header><strong>Masaki</strong><time datetime="2008-03-21 10:54 UTC">2008-03-21 10:54 UTC</time></header>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
My project is to build a sensor filtering and logging program.<br>
<br>
In order to make a longing period longer, I would like to use as much  RAM area as possible.<br>
<br>
<br>
<br>
My implementation in Simulink program is to use Data Store Memory block in which I declear<br>
<br>
an UINT16 array of size 300. When I increase the size to 325, the dsPIC hangs up. <br>
<br>
The memory usage is investigated as follows. My CPU is 30f3013 with ROM 24k and RAM 2k.<br>
<br>
<br>
<br>
Size = 300: Program Memory 4107bytes, Data memory 1282bytes, Max dynamic memory 766bytes.<br>
<br>
Size = 325: Program Memory 4158bytes, Data memory 1382bytes, Max dynamic memory 666bytes.<br>
<br>
<br>
<br>
My question here is:<br>
<br>
<br>
<br>
1) What is a criteria to know the maximum available memory space?<br>
<br>
2) When I increase the UINT16 array size by 325-300=25, Data memory size increases 100bytes,<br>
<br>
    where I think should be 50bytes. Is there any trick here? Maybe some Simulink programing tip?<br>
<br>
<br>
<br>
Thanks in advance,<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p275">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-21 12:09 UTC">2008-03-21 12:09 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hi Masaki,<br>
<br>
<br>
<br>
I do not know exactly what simulink is doing in your case. It may be some Simulink tricks.<br>
<br>
<br>
<br>
It would be easier to see the mdl file to propose tips. Could you send it (either with the forum upload function or by email if  you can't upload (In the last case, tell me if I can publish it on the forum).<br>
<br>
<br>
<br>
There is several optimization options for RTW C code generation. Some of theses optimization are very efficient to reduce code size and memory (RAM) usage.<br>
<br>
<br>
<br>
Regards<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p276">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-25 23:55 UTC">2008-03-25 23:55 UTC</time></header>
<h3>Optimizing RAM usage</h3>
<div class="forum-post-body">Hi Masaki,<br>
<br>
<br>
<br>
I provide few tricks to optimize RAM usage.<br>
<br>
<br>
<br>
First of all, checking the "inline parameters" greatly reduce RAM usage. (It means that all constant variables are stored inside the ROM memory rather than inside the RAM)<br>
<br>
<br>
About storing data inside a vector; I noticed that the generated code of the assignment block is not very efficient:<br>
<br>
Generated code (RTW Embedded Coder, Matlab 2007b):<br>
<br>
<br>
<pre><code>/* Assignment: '&lt;S1&gt;/Assignment' incorporates:
*  DataStoreRead: '&lt;S1&gt;/Data Store Read'
*/
for (i = 0; i &lt; 700; i++) {
 rtb_Assignment[i] = Model8_DWork.HISTORY[i];
}
<wbr>
i = 0;
for (yDimIdx = 0; yDimIdx &lt; 2; yDimIdx++) {
 rtb_Assignment[(int32_T)cg_in_0[yDimIdx] - 1L] = cg_in[i];
 i = (int16_T)((int32_T)i + 1L);
}
<wbr>
for (i = 0; i &lt; 700; i++) {
 /* DataStoreWrite: '&lt;S1&gt;/Data Store Write' */
 Model8_DWork.HISTORY[i] = rtb_Assignment[i];
}</code></pre><br>
<br>
As you may notice, the Variable <span style="color:#0000ff">HISTORY </span>(vector) is copied into the variable <span style="color:#0000ff">rtb_Assignment</span>. Then modified and copied back into the <br>
<br>
<span style="color:#0000ff">HISTORY </span> vector. This code is slow and needs a lots of memory because during a short moment, two version of the vector ( called table in C language) are present in memory.<br>
<br>
<br>
<br>
A better way is to not use the block Assignment. Replace this block by a very simple C function that will write into the vector at the desired location the desired value. This function will takes 2 parameters: index and value. The variable should be declared as a global variable in Simulink.<br>
<br>
Have a look on the post <a href="/forum/topic/100/#p273">viewtopic.php?f=1&amp;p=273#p271</a> to see details about including C function into the model. The example given here uses a global variable which is declared in simulink.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/48-inline.png">Pièce jointe : inline.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/50-assignment2.png">Pièce jointe : assignment2.png</a></p>
</article>

<article class="forum-post" id="p278">
<header><strong>Masaki</strong><time datetime="2008-03-29 02:27 UTC">2008-03-29 02:27 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Thanks Lubin,<br>
<br>
<br>
<br>
I understand your techniques.<br>
<br>
<br>
<br>
As for the first one (checking inline parameters), it increased the memory usage performance by 50%.<br>
<br>
In other words, I can take 450 history length compared to 300 before.<br>
<br>
<br>
<br>
For the second one (introducing C functions), I still cannot make it happen.<br>
<br>
My C programs goes:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;
/* Data history reading */
unsigned int ReadHistory(unsigned int index)
{
    extern volatile unsigned int *HISTORY;
    return(HISTORY[index-1]); /* 1-base indexing */
}
<wbr>
/* Data history logging */
void WriteHistory(unsigned int index, unsigned int value)
{
    extern volatile unsigned int *HISTORY;
    HISTORY[index-1]=value;  /* 1-base indexing */
}
<wbr>
</code></pre><br>
<br>
I also prepared correspoinding C Function Call blocks and compiled the program without errors.<br>
<br>
Still the downloaded code won't work, maybe getting trouble with C interfacing.<br>
<br>
Can you tell what might be a problem?<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p279">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-29 10:41 UTC">2008-03-29 10:41 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">C code seems Ok,<br>
<br>
<br>
<br>
Sampling time of some blocks or subsystem seems to be the problem on your model.<br>
<br>
<br>
<br>
Any blocks with a sample time set of inf ( or set to -1, where value inf is inherited) will execute only once at the initialisation time.<br>
<br>
Using the "Sample Time Color" option of the Port/Signal display of simulink is very helpfull to see how sample time is inherited on your model's blocks.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p343">
<header><strong>malife</strong><time datetime="2008-05-13 00:13 UTC">2008-05-13 00:13 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hello All,<br>
<br>
 So your general advise is to use inline parameters always? or just for this application? <br>
<br>
<br>
<br>
Also, I noticed that Masaki's model was not posted, could we at least know what dsPIC is being used and at what sampling frequency and Fcy, just to have an upper bound in case someone else is using the same part?<br>
<br>
<br>
<br>
Thanks!</div>
</article>

<article class="forum-post" id="p345">
<header><strong>Masaki</strong><time datetime="2008-05-13 03:03 UTC">2008-05-13 03:03 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body"><blockquote><br>
So your general advise is to use inline parameters always? or just for this application? <br>
</blockquote><br>
<br>
This is Masaki.<br>
<br>
My way of understanding is this:<br>
<br>
- When you have a plenty of ROM area, chech inline parameters.<br>
<br>
- When you don't have enough ROM area, don't check inline parameters.<br>
<br>
<br>
<br>
In my application, the program is fairly simple but requires a large amout of RAM to keep data history.<br>
<br>
So I used inline parameters.<br>
<br>
<br>
<blockquote><br>
Also, I noticed that Masaki's model was not posted, could we at least know what dsPIC is being used and at what sampling frequency and Fcy, just to have an upper bound in case someone else is using the same part?<br>
</blockquote><br>
<br>
I used dsPIC30F3013 which has 2kByte RAM and 24kByte ROM with Fosc=120MHz. <br>
<br>
The program is running at 1kHz sampling rate.<br>
<br>
<br>
<br>
Finally, I'm using this program with history length of 450.<br>
<br>
I could not make in-line C program work correctly from some unknow reason.<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p346">
<header><strong>malife</strong><time datetime="2008-05-13 16:12 UTC">2008-05-13 16:12 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Thanks for posting that information Masaki. I am sure many will find it useful. <br>
<br>
<br>
<blockquote>I could not make in-line C program work correctly from some unknow reason.</blockquote><br>
<br>
When you say that you were not able to get the in-line C program to work, do you mean the  C function call inside the Simulink Model. If so, I would be more than glad to help you out on how to get it to work. I would be really interested in seeing how much that can improve the performance. I still think that 450 if kind of low for a 2K RAM chip, so maybe implementing the C function call is the way to go.<br>
<br>
<br>
<br>
Again, thanks for the info<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p347">
<header><strong>Masaki</strong><time datetime="2008-05-14 00:42 UTC">2008-05-14 00:42 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
Thanks for your comment.<br>
<br>
<br>
<br>
My final C-code looks like this:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;    extern volatile unsigned int HISTORY[];
<wbr>
/* Data history reading */
unsigned int ReadHistory(unsigned int index)
{
	if (index &lt; 1) index = 1;
    return(HISTORY[index-1]); /* 1-base indexing */
}
<wbr>
/* Data history logging */
void WriteHistory(unsigned int index, unsigned int value)
{
	if (index &lt; 1) index = 1;
    HISTORY[index-1]=value;  /* 1-base indexing */
}
</code></pre><br>
<br>
In this manner, the program can be compiled and downloaded onto a dsPIC.<br>
<br>
As I wrote before, history size can be 900, which is almost theoretical limit for the RAM size.<br>
<br>
But unfortunately, the program won't work correctly.<br>
<br>
<br>
<br>
The problem was:<br>
<br>
- The program seems to be reading hisotory correctly.<br>
<br>
- But it cannot write a correct value in History array in a right position.<br>
<br>
<br>
<br>
I thought RTW's core program is interfereing with my C-function, and that this is beyond my ability.<br>
<br>
<br>
<br>
Masaki</div>
</article>

<article class="forum-post" id="p349">
<header><strong>malife</strong><time datetime="2008-05-14 18:51 UTC">2008-05-14 18:51 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hello Masaki,<br>
<br>
 It's kind of hard to help you without seeing the overall model and the C-source. I understand if you can not post your model, so I will do my best to help you out from what I see.<br>
<br>
<br>
<br>
First, if you are using the C-function call block in your model, then your functions should have the following prototypes:<br>
<br>
<br>
<br>
uint16_T ReadHistory(uint16_T index)<br>
<br>
void WriteHistory(uint16_T index, uint16_T value)<br>
<br>
<br>
<br>
since that is how Lubin's code inserts the declaration in the Main file (you can actually read that out in the grayed area of the C-function call block). <br>
<br>
<br>
<br>
Also, you should include rtwtypes.h in this C file. <br>
<br>
<br>
<br>
If you can, try posting the generated C-Code files if you do not want to post the model, so I can go over the generated code and see if I can find what is wrong.<br>
<br>
<br>
<br>
Hope this helps</div>
</article>

<article class="forum-post" id="p354">
<header><strong>Masaki</strong><time datetime="2008-05-15 11:50 UTC">2008-05-15 11:50 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hi  Mariano,<br>
<br>
<br>
<br>
Sorry for my not positing the model file. But all of the C source code is posted in my perevious writing.<br>
<br>
<br>
<blockquote><br>
First, if you are using the C-function call block in your model, then your functions should have the following prototypes:<br>
<br>
<br>
<br>
uint16_T ReadHistory(uint16_T index)<br>
<br>
void WriteHistory(uint16_T index, uint16_T value)<br>
</blockquote><br>
<br>
I have confirmed almost the same definition:<br>
<br>
extern uint16_T ReadHistory(uint16_T u1);<br>
<br>
extern void WriteHistory(uint16_T u1, uint16_T u2);<br>
<br>
<br>
<blockquote><br>
Also, you should include rtwtypes.h in this C file. <br>
</blockquote><br>
<br>
I didn't include it in my C source file, because there wasn't no error.<br>
<br>
<br>
<blockquote><br>
If you can, try posting the generated C-Code files if you do not want to post the model, so I can go over the generated code and see if I can find what is wrong.<br>
</blockquote><br>
<br>
OK, I try. <br>
<br>
I picked the biggest C source file from the three. Is this right?<br>
<br>
<br>
<br>
Hoping this big post won't screw up the system,<br>
<br>
<br>
<br>
Masaki<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;/*
 * File: testanemo9a.c
 *
 * Real-Time Workshop code generated for Simulink model testanemo9a.
 *
 * Model version                        : 1.57
 * Real-Time Workshop file version      : 7.0  (R2007b)  02-Aug-2007
 * Real-Time Workshop file generated on : Sun Apr 13 10:48:00 2008
 * TLC version                          : 7.0 (Jul 26 2007)
 * C source code generated on           : Sun Apr 13 10:48:01 2008
 *--------------------------------------------------------------
 *   Embedded Coder for Microchip dsPIC family.                 |
 *   Generate .c and .h files from your Matlab/simulink model   |
 *   and compile the diagram to .hex and .coff file that can be |
 *   downloaded directly into the microcontroller               |
 *                                                              |
 * 
 * 
 *                                                              |
 *   Written by Lubin KERHUEL -  http://www.kerhuel.eu          |
 *  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
 *   Version 0.95ba                            07-Feb-2008      |
 *   For Matlab 7.5             R2007b                          |
 *--------------------------------------------------------------
 */
<wbr>
#include "testanemo9a.h"
#include "testanemo9a_private.h"
<wbr>
/* Exported block states */
uint16_T HISTORY[900];                 /* '&lt;Root&gt;/Data Store Memory' */
<wbr>
/* Block signals (auto storage) */
BlockIO_testanemo9a testanemo9a_B;
<wbr>
/* Block states (auto storage) */
D_Work_testanemo9a testanemo9a_DWork;
<wbr>
/* Real-time model */
RT_MODEL_testanemo9a testanemo9a_M_;
RT_MODEL_testanemo9a *testanemo9a_M = &amp;testanemo9a_M_;
static void rate_monotonic_scheduler(void);
<wbr>
/* Set which subrates need to run this base step (base rate always runs).
 * This function must be called prior to calling the model step function
 * in order to "remember" which rates need to run this base step.  The
 * buffering of events allows for overlapping preemption.
 */
void testanemo9a_SetEventsForThisBaseStep(boolean_T *eventFlags)
{
  /* Task runs when its counter is zero, computed via rtmStepTask macro */
  eventFlags[1] = ((boolean_T)rtmStepTask(testanemo9a_M, 1));
}
<wbr>
/* This function updates active task flag for each subrate
 * and rate transition flags for tasks that exchagne data.
 * The function assumes rate-monotonic multitasking scheduler.
 * The function must be called at model base rate so that
 * the generated code self-manages all its subrates and rate
 * transition flags.
 */
static void rate_monotonic_scheduler(void)
{
  /* To ensure a safe and deterministic data transfer between two rates,
   * data is transferred at the priority of a fast task and the frequency
   * of the slow task.  The following flags indicate when the data transfer
   * happens.  That is, a rate interaction flag is set true when both rates
   * will run, and false otherwise.
   */
<wbr>
  /* tid 0 shares data with slower tid rate: 1 */
  testanemo9a_M-&gt;Timing.RateInteraction.TID0_1 =
    (testanemo9a_M-&gt;Timing.TaskCounters.TID[1] == 0);
<wbr>
  /* Compute which subrates run during the next base time step.  Subrates
   * are an integer multiple of the base rate counter.  Therefore, the subtask
   * counter is reset when it reaches its limit (zero means run).
   */
  if (++testanemo9a_M-&gt;Timing.TaskCounters.TID[1] == 3000) {/* Sample time: [3.0s, 0.0s] */
    testanemo9a_M-&gt;Timing.TaskCounters.TID[1] = 0;
  }
}
<wbr>
/* Model step function for TID0 */
void testanemo9a_step0(void)           /* Sample time: [0.001s, 0.0s] */
{
  /* local block i/o variables */
  real_T rtb_Add3;
  real_T rtb_Divide;
  real_T rtb_DiscreteFilter1f001Hz;
  uint16_T rtb_Add1;
  uint16_T rtb_Add2;
<wbr>
  {                                    /* Sample time: [0.001s, 0.0s] */
    rate_monotonic_scheduler();
  }
<wbr>
  {
    int16_T s4_iter;
<wbr>
    /* S-Function "ADC" Block: &lt;Root&gt;/ADC Input */
    testanemo9a_B.ADCInput_o1 = ADCBUF0;
    testanemo9a_B.ADCInput_o2 = ADCBUF1;
    testanemo9a_B.ADCInput_o3 = ADCBUF2;
<wbr>
    /* DataTypeConversion: '&lt;Root&gt;/Data Type Conversion4' */
    rtb_DiscreteFilter1f001Hz = (real_T)testanemo9a_B.ADCInput_o2;
<wbr>
    /* Sum: '&lt;Root&gt;/Add3' incorporates:
     *  DataTypeConversion: '&lt;Root&gt;/Data Type Conversion3'
     */
    rtb_Add3 = (real_T)testanemo9a_B.ADCInput_o1 - rtb_DiscreteFilter1f001Hz;
<wbr>
    /* DataTypeConversion: '&lt;Root&gt;/Data Type Conversion5' */
    rtb_DiscreteFilter1f001Hz = (real_T)testanemo9a_B.ADCInput_o3;
<wbr>
    /* Product: '&lt;Root&gt;/Divide' incorporates:
     *  Constant: '&lt;Root&gt;/Constant3'
     *  Saturate: '&lt;Root&gt;/Saturation'
     */
    rtb_Divide = rtb_Add3 * 600.0 / rt_SATURATE(rtb_DiscreteFilter1f001Hz, 1.0,
      65535.0);
<wbr>
    /* DiscreteFilter: '&lt;Root&gt;/Discrete Filter f=1Hz' */
    rtb_DiscreteFilter1f001Hz = 3.1317539583613544E-003*rtb_Divide;
    rtb_DiscreteFilter1f001Hz += 6.2438921510112842E-003*
      testanemo9a_DWork.DiscreteFilterf1Hz_DSTATE;
<wbr>
    /* Sum: '&lt;Root&gt;/Add1' incorporates:
     *  Constant: '&lt;Root&gt;/Constant'
     *  Gain: '&lt;Root&gt;/Gain'
     */
    rtb_Add3 = fmod(floor(30.0 * rtb_DiscreteFilter1f001Hz - 32768.0), 65536.0);
    if (rtb_Add3 &lt; 0.0) {
      rtb_Add3 += 65536.0;
    }
<wbr>
    rtb_Add1 = (uint16_T)rtb_Add3;
<wbr>
    /* DiscreteFilter: '&lt;Root&gt;/Discrete Filter1 f=0.01Hz' */
    rtb_DiscreteFilter1f001Hz = 3.1414939606463125E-005*rtb_Divide;
    rtb_DiscreteFilter1f001Hz += 6.2827905416065283E-005*
      testanemo9a_DWork.DiscreteFilter1f001Hz_DSTATE;
<wbr>
    /* Sum: '&lt;Root&gt;/Add2' incorporates:
     *  Constant: '&lt;Root&gt;/Constant2'
     *  Gain: '&lt;Root&gt;/Gain1'
     */
    rtb_Add3 = fmod(floor(30.0 * rtb_DiscreteFilter1f001Hz - 32768.0), 65536.0);
    if (rtb_Add3 &lt; 0.0) {
      rtb_Add3 += 65536.0;
    }
<wbr>
    rtb_Add2 = (uint16_T)rtb_Add3;
<wbr>
    /* RateTransition: '&lt;Root&gt;/Rate Transition' */
    if (testanemo9a_M-&gt;Timing.RateInteraction.TID0_1) {
      testanemo9a_B.RateTransition = rtb_Add2;
    }
<wbr>
    /* S-Function "UART_RX" Block: &lt;Root&gt;/Rx Input */
    if (U1STAbits.URXDA == 1) {
      testanemo9a_B.RxInput = (unsigned char) U1RXREG;/* Use only the 8 low bytes or RxReg */
    } else {
      testanemo9a_B.RxInput = 0;
    }
<wbr>
    U1STAbits.OERR = 0;                /* Buffer Overflow cleared */
<wbr>
    /* SwitchCase: '&lt;Root&gt;/Switch Case' */
    switch (testanemo9a_B.RxInput) {
     case 97L:
      /* Outputs for iterator SubSystem: '&lt;S2&gt;/For Iterator Subsystem' incorporates:
       *  Constant: '&lt;Root&gt;/Constant1'
       */
      for (s4_iter = 1; s4_iter &lt;= 900; s4_iter++) {
        /* DataTypeConversion: '&lt;S4&gt;/Data Type Conversion1' */
        testanemo9a_B.DataTypeConversion1 = (uint16_T)s4_iter;
<wbr>
        /* S-Function "dsPIC_C_function_Call" Block: &lt;S4&gt;/C Function Call */
        testanemo9a_B.CFunctionCall = ReadHistory
          (testanemo9a_B.DataTypeConversion1);
<wbr>
        /* DataTypeConversion: '&lt;S6&gt;/Extract Desired Bits' */
        testanemo9a_B.ExtractDesiredBits_i = (uint8_T)
          testanemo9a_B.CFunctionCall;
<wbr>
        /* DataTypeConversion: '&lt;S5&gt;/Extract Desired Bits' */
        testanemo9a_B.ExtractDesiredBits_n = (uint8_T)
          (testanemo9a_B.CFunctionCall &gt;&gt; 8);
<wbr>
        /* S-Function "UART_Tx" Block: &lt;S4&gt;/Tx Output */
        while (BusyUART1()) ;
        WriteUART1(testanemo9a_B.ExtractDesiredBits_i);
        while (BusyUART1()) ;
        WriteUART1(testanemo9a_B.ExtractDesiredBits_n);
      }
<wbr>
      /* end of Outputs for SubSystem: '&lt;S2&gt;/For Iterator Subsystem' */
      break;
<wbr>
     case 114L:
      /* DataTypeConversion: '&lt;S8&gt;/Extract Desired Bits' */
      testanemo9a_B.ExtractDesiredBits = (uint8_T)rtb_Add1;
<wbr>
      /* DataTypeConversion: '&lt;S7&gt;/Extract Desired Bits' */
      testanemo9a_B.ExtractDesiredBits_o = (uint8_T)(rtb_Add1 &gt;&gt; 8);
<wbr>
      /* S-Function "UART_Tx" Block: &lt;S3&gt;/Tx Output */
      while (BusyUART1()) ;
      WriteUART1(testanemo9a_B.ExtractDesiredBits);
      while (BusyUART1()) ;
      WriteUART1(testanemo9a_B.ExtractDesiredBits_o);
      break;
    }
<wbr>
    /* DiscreteFilter Block: '&lt;Root&gt;/Discrete Filter f=1Hz' */
    {
      testanemo9a_DWork.DiscreteFilterf1Hz_DSTATE = rtb_Divide +
        9.9373649208327730E-001*testanemo9a_DWork.DiscreteFilterf1Hz_DSTATE;
    }
<wbr>
    /* DiscreteFilter Block: '&lt;Root&gt;/Discrete Filter1 f=0.01Hz' */
    {
      testanemo9a_DWork.DiscreteFilter1f001Hz_DSTATE = rtb_Divide +
        9.9993717012078698E-001*testanemo9a_DWork.DiscreteFilter1f001Hz_DSTATE;
    }
  }
}
<wbr>
/* Model step function for TID1 */
void testanemo9a_step1(void)           /* Sample time: [3.0s, 0.0s] */
{
  /* S-Function "dsPIC_C_function_Call" Block: &lt;S1&gt;/C Function Call2 */
  WriteHistory(testanemo9a_ConstB.DataTypeConversion,
               testanemo9a_B.RateTransition);
}
<wbr>
void testanemo9a_step(int_T tid)
{
  switch (tid) {
   case 0 :
    testanemo9a_step0();
    break;
<wbr>
   case 1 :
    testanemo9a_step1();
    break;
<wbr>
   default :
    break;
  }
}
<wbr>
/* Model initialize function */
void testanemo9a_initialize(boolean_T firstTime)
{
  (void)firstTime;
<wbr>
  /* Registration code */
  /* initialize real-time model */
  (void) memset((char_T *)testanemo9a_M,0,
                sizeof(RT_MODEL_testanemo9a));
<wbr>
  /* block I/O */
  (void) memset(((void *) &amp;testanemo9a_B),0,
                sizeof(BlockIO_testanemo9a));
<wbr>
  /* states (dwork) */
  {
    real_T *dwork_ptr = (real_T *) &amp;testanemo9a_DWork.DiscreteFilterf1Hz_DSTATE;
    dwork_ptr[0] = 0.0;
    dwork_ptr[1] = 0.0;
  }
<wbr>
  /* exported global states */
  (void) memset(&amp;HISTORY,0,
                900*sizeof(uint16_T));
<wbr>
  {
    int16_T i;
<wbr>
    /* S-Function "dsPIC_MASTER" initialization Block: &lt;Root&gt;/Master */
    /* 0 testfcy 	*/
    /*  3.0E+007	*/
    /* CONFIG TIMER 1 for scheduling steps 	*/
    ConfigIntTimer1(T1_INT_PRIOR_0 &amp; T1_INT_OFF);
    T1CON = 0x8000 ;                   /* T1_PS_1_1	*/
    PR1 = 30000;
<wbr>
    /* Configuration TRIS */
    TRISB = 65023;
<wbr>
    /* Configuration ADCHS */
    ADPCFG = 512;
<wbr>
    /* S-Function "dsPIC_UART_config" initialization Block: &lt;Root&gt;/UART Configuration */
    /* set priority */
    _U1RXIP = 0x0007 &amp; 1;
    _U1TXIP = 0x0007 &amp; 1;
<wbr>
    /* enable/disable interrupt */
    _U1RXIE = 0;
    _U1TXIE = 0;
    U1MODE = 0x8080 + 1024;
    U1STA = 0x0 + 32768 + 1024;
    U1BRG = 15;
<wbr>
    /* S-Function "dsPIC_ADC" initialization Block: &lt;Root&gt;/ADC Input */
    /* Initialise ADC converter */
    /* 0 mean each 1 conversion */
#define NoSamplesADC                   2
#define ADCSval                        39
#define SAMCval                        (1 &lt;&lt; 8)
#define OutFormatBitsval               (0 &lt;&lt; 8)
#define VoltRef                        (0 &lt;&lt; 13)
<wbr>
    /* Use internal counter Trigger, continuous simulatenous sampling */
    ADCON1 = 0x00E4 | (1 &lt;&lt; 10)| OutFormatBitsval;
    ADCON2 = 0x0400 | (NoSamplesADC &lt;&lt; 2) | VoltRef;
    ADCSSL = 14;
    ADCON3 = (ADCSval | SAMCval) &amp; 0xff7f;
    ADCHS = 0x0000;
    IPC2 = (IPC2 | (6 &lt;&lt; 12));         /*Interrupt Priority : 6*/
    IFS0bits.ADIF = 0;
<wbr>
    /* _ADIE = 1; */
    /* 1 sample/output-Step ; Do not need interrupt so do not enable it. */
    /* Clear Off Any Interrupt Due To Configuration */
    /* Turn on ADC Module */
    ADCON1bits.ADON= 1;
    for (i = 0; i &lt; 900; i++) {
      /* Start for DataStoreMemory: '&lt;Root&gt;/Data Store Memory' */
      HISTORY[i] = testanemo9a_ConstP.DataStoreMemory_Ini[i];
    }
  }
<wbr>
  /* S-Function "dsPIC_C_function_Call" Block: &lt;S1&gt;/C Function Call */
  WriteHistory(1U,testanemo9a_ConstB.DataTypeConversion);
}
<wbr>
/* File trailer for Real-Time Workshop generated code.
 *
 * [EOF]
 */
</code></pre></div>
</article>

<article class="forum-post" id="p355">
<header><strong>malife</strong><time datetime="2008-05-15 17:25 UTC">2008-05-15 17:25 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Masaki,<br>
<br>
 The only  thing that  I noticed from your code is that WriteHistory is called every three seconds, which seems kind a long considering your main sample rate is 0.001, but this by no means implies it is wrong. Also, you did not post the H-files, but in your function declarations (i.e. you C file) you SHOULD NOT include the extern keyword. Lubin does so, so the code nows that your functions are in another file. rtwtypes.h allows you to use the real time workshop types like uint8_T, uint16_T and so on.<br>
<br>
<br>
<br>
It is quite hard for me to help you any further without seeing your model. Sorry I could not be of any further help.</div>
</article>

<article class="forum-post" id="p357">
<header><strong>LubinKerhuel</strong><time datetime="2008-05-15 23:21 UTC">2008-05-15 23:21 UTC</time></header>
<h3>Re: How much RAM area can a program use?</h3>
<div class="forum-post-body">Hi Mariano, Hi Masaki,<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : malife</header>in your function declarations (i.e. you C file) you SHOULD NOT include the extern keyword</blockquote><br>
<br>
If you declare the variable (in the sense that you want the C file to provide a memory place to store it) in the C file, you are true (i.e. needs to remove extern keyword). <br>
<br>
However, there is the possibility to declare the variable in simulink using the block "Data Store memory" (from simulink standard library) and defining it as "global". In this way, the variable can be used easily anywhere in the simulink file with the "Data Store Read" or "Data Store Write" block ; ans can be used in the C file if you precise (with "extern") that the variable is being declared in another c file.<br>
<br>
<br>
<br>
It's a good point to use rtwtypes.h to use exactly the same declaration keyword ! Thanks for that trick.</div>
</article>

