---
title: "Implementing the C Function Call"
url: "/forum/topic/100/"
archiveKind: "topic"
---
# Implementing the C Function Call

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p266">
<header><strong>malife</strong><time datetime="2008-03-18 00:17 UTC">2008-03-18 00:17 UTC</time></header>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 I've been looking at your blockset and it is really amazing. For me being a seasoned PIC and dsPIC programmer, it is just amazing how much leverage your tool gives. Congrats on a great product. One thing I am trying to implement is the QEI, now I've already read that you currently have no plans to suport it, and honestly I would much rather see you devote time to an interrupt driven (virtual buffer) UART, SPI and CAN. <br>
<br>
<br>
<br>
So I think (correct me if I am wrong) that using the C-Fucntion Call shall allow me to completely use the QEI in the following way:<br>
<br>
<br>
<br>
1.- Create a C function to initialize the QEI and call it once when the model starts execution; and,<br>
<br>
2.- Create a C function to read the status of the QEI registers (specially POSCNT) and send the data to Simulink to further use it.<br>
<br>
<br>
<br>
So I was wondering if you could post a simple example of the usage of the function call, and I will do the QEI Example and make it available here on the forum for your registered users.<br>
<br>
<br>
<br>
Cheers<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p267">
<header><strong>malife</strong><time datetime="2008-03-20 18:41 UTC">2008-03-20 18:41 UTC</time></header>
<h3>Re: Implementing the C Function Call</h3>
<div class="forum-post-body">Hello,<br>
<br>
 I am working on touching up the example for the QEI. I have a<br>
<br>
couple of requests in order to make this happen and I think that it<br>
<br>
would overall help make the usage of the C function call block more diverse.<br>
<br>
<br>
<br>
1.- Function prototype: In my previous email I forgot to include one<br>
<br>
detail. Sometimes you need to implement an interrupt (like in this<br>
<br>
case for the QEI), but as I am sure you know if I implement an<br>
<br>
interrupt it has to have a given prototype, which it does not work<br>
<br>
since I must adhere to the required prototype by your function call<br>
<br>
block.<br>
<br>
<br>
<br>
2.- Interrupts sometimes require access to a global variable,<br>
<br>
generally a switch to indicate something changed. So if you could do a<br>
<br>
very simple (I think :-) ) source block that was a global variable,<br>
<br>
then, I could change the value inside my interrupt and be done with<br>
<br>
it.<br>
<br>
<br>
<br>
I have probably not made myself clear, so I will put the scenario in<br>
<br>
front of you and let you decide:<br>
<br>
<br>
<br>
I initialize the QEI with this function:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;void QEIInit(void){
 ConfigIntQEI (QEI_INT_ENABLE &amp;  // Enable interrupts
               QEI_INT_PRI_5);   // Set Priority to 5
<wbr>
 POSCNT = 0;                     // Set Current Position to 0
 MAXCNT = 0xFFFF;                // Use the full 16bit counter
<wbr>
 OpenQEI (QEI_DIR_SEL_CNTRL &amp;    // UPDN bit decides direction count
          QEI_INT_CLK &amp;          // Use FCY for clocking
          QEI_INDEX_RESET_DISABLE &amp;
          QEI_CLK_PRESCALE_1 &amp;    // 1:1 Prescale
          QEI_GATED_ACC_DISABLE &amp;
          QEI_NORMAL_IO &amp;        // QEI Control state of IO pin
          QEI_INPUTS_NOSWAP &amp;    // Channels A and B are not swapped
          QEI_MODE_x2_MATCH &amp;    // X2 mode with counter reset by match
          QEI_UP_COUNT &amp;         // Read only for this mode
          QEI_IDLE_STOP,         // Stop in idle operation
          MATCH_INDEX_INPUT_PHASEA &amp;
          QEI_QE_CLK_DIVIDE_1_16 &amp;// Filter 1:16 divider
          QEI_QE_OUT_ENABLE);    // Enable the input digital filter
<wbr>
}</code></pre><br>
<br>
This is clearly doable using your c function call block<br>
<br>
<br>
<br>
then, every time the QEI overflows or underflows I increment a global<br>
<br>
variable that keeps track of the turn count of the motor (i.e. the<br>
<br>
motor can do more than one turn). This happens inside an interrupt.<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;void __attribute__((__interrupt__, no_auto_psv)) _QEIInterrupt(void){
<wbr>
// if it overflowed
 if (ReadQEI() &lt; 0x3FFF){
   ct_turns++;
 } else {
   ct_turns--;
 }
 // clear the interrupt flag
 IFS2bits.QEIIF =0;
}</code></pre><br>
<br>
This I can not do it using the c function call block because: 1.- I can not<br>
<br>
change the function prototype and 2.- I have no way of declaring from<br>
<br>
simulink the global variable ct_turns.<br>
<br>
<br>
<br>
Then I use it n the code to compute the actual position of the motor:<br>
<br>
<br>
<pre><code>thePID.y_m = (float)(ct_turns*65535 + POSCNT)*angle_ratio; 
//where POSCNT is a register</code></pre><br>
<br>
<br>
<br>
Maybe you can suggest a work around this limitation (maybe adding an<br>
<br>
external file from the project properties dialog?) or you can<br>
<br>
implement the changes in the block.<br>
<br>
<br>
<br>
I have attached a Simulink model Image of how I see it working inside<br>
<br>
simulink if you were to modify/add the suggeted blocks.<br>
<br>
<br>
<br>
Concretely in the C function call, I think it would be great if  you<br>
<br>
were to provide the following modifications:<br>
<br>
<br>
<br>
1.- A way to override your default function prototype<br>
<br>
2.- A way to decide whether it should be called once at the beginning<br>
<br>
(which I think you can by setting the sample time to inf), every cycle<br>
<br>
(by setting the sample time) or never (like an interrupt which is<br>
<br>
called by the microcontroller interrupt engine).<br>
<br>
<br>
<br>
And then provide a small block that declares a global variable (with a<br>
<br>
given name)  and initializes it a to given value and returns the<br>
<br>
current value each sample time.<br>
<br>
<br>
<br>
Also, how do I add the dsPIC library QEI.h? From the project properties dialog?<br>
<br>
<br>
<br>
Sorry for the extra long post, I hope I have made myself clear. I<br>
<br>
will try to look for workarounds for this in the mean while.<br>
<br>
<br>
<br>
Thanks Lubin!!</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/37-CFunCallQEI.JPG">Pièce jointe : CFunCallQEI.JPG</a></p>
</article>

<article class="forum-post" id="p268">
<header><strong>malife</strong><time datetime="2008-03-20 23:35 UTC">2008-03-20 23:35 UTC</time></header>
<h3>Re: Implementing the C Function Call</h3>
<div class="forum-post-body">Hello All,<br>
<br>
 It is with great pleasure that I give you an example Simulink Model of how to use the C function call to implement the QEI in a dsPIC30F4011. This is proven to work and if anybody has a question feel free to post it. Attached to this are two files: the Simulink model and the C file. Note that if you roll your own you need to add the C file to the Simulink options. The example is fully interrupt driven and supports more than one turns (in any direction of course :-) )<br>
<br>
<br>
<br>
I guess using the C function call is a great reason to buy any of the registered versions :-)<br>
<br>
<br>
<br>
Hope this is helpful to anyone looking to use the QEI.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/38-QEITest.mdl">Pièce jointe : QEITest.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/39-myQEI.c">Pièce jointe : myQEI.c</a></p>
</article>

<article class="forum-post" id="p271">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-21 00:34 UTC">2008-03-21 00:34 UTC</time></header>
<h3>Re: Implementing the C Function Call</h3>
<div class="forum-post-body">Hi Mariano,<br>
<br>
<br>
<br>
I was working on this post while you posted your solution.<br>
<br>
I keep it there since it was a piece of work. <br>
<br>
<br>
<br>
to resume,<br>
<br>
I declared the global variable using a different way. (yours may be better for this example).<br>
<br>
I do not like the way you initialize the QEI peripheral. It would make better C code to set its sampling time to inf !<br>
<br>
<br>
<br>
------<br>
<br>
It was quite long to make the example; I respond quickly, refer to the example for further details.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : malife</header>1.- A way to override your default function prototype</blockquote><br>
To implement a function that has no "interface" with the model (kind of internal function, like interrupt) . You do not need to use the C function call block. Just add the function in the C file that you declared in the Configuration Parameters dialog box.<br>
<br>
<br>
 <blockquote><header class="quote-author">Citation : malife</header>2.- A way to decide whether it should be called once at the beginning<br>
<br>
(which I think you can by setting the sample time to inf), every cycle<br>
<br>
(by setting the sample time) or never (like an interrupt which is<br>
<br>
called by the microcontroller interrupt engine).</blockquote><br>
<br>
You already have the solution!  I think it is better to enter into the simulink logic rather than adding a option for initialization.<br>
<ul>initialization (call only once at startup) ==&gt; sample time = inf<br>
<br>
call ==&gt; sample time = sampling time desired<br>
<br>
Interrupt ==&gt; do not need using a C function call block.</ul><br>
<br>
<blockquote><header class="quote-author">Citation : malife</header>And then provide a small block that declares a global variable (with a<br>
<br>
given name) and initializes it a to given value and returns the<br>
<br>
current value each sample time.</blockquote><br>
<br>
It is possible to use block 'Data Store Memory', 'Data Read Memory' and 'Data Write Memory' which are block of the standard simulink library.<br>
<br>
You must declare (in the Data Store Memory) the variable as global, assign its name in order to be able to use this variable in your C function written. In your C file, the variable will be declared as external.  You must declare the variable with the same datatype. <br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
The following example compile but <span style="color:#bf0040">has not been tested</span>. I don't know if this implementation of QEI function is working. I guess modifications will be required. I hope that the example is not too hard to read.<br>
<br>
The model and C file can be download at the end of the post.<br>
<br>
I also attached a basic example (the one I sent to you Mariano) that shows how to use different calling method to transfer data between simulink and C functions (using pointer or direct value...this example is not described on this post).<br>
<br>
<br>
<br>
I noticed that some images do not load correctly. It is a strange behaviour of the forum ; I guess there is too many image in this post. Reloading the page seems to gives results... (Press F5)<br>
<br>
<br>
<br>
<br>
<br>
<br>
C file content (Modified versioin of Mariano's proposition):<br>
 <pre><code>#include &lt;p30f4011.h&gt;
#include &lt;qei.h&gt;
<wbr>
/*------------------------------------------------------------------*/
void QEIInit(void){
  ConfigIntQEI (QEI_INT_ENABLE &amp;  // Enable interrupts
                QEI_INT_PRI_5);   // Set Priority to 5
<wbr>
  POSCNT = 0;                     // Set Current Position to 0
  MAXCNT = 0xFFFF;                // Use the full 16bit counter
<wbr>
  OpenQEI (QEI_DIR_SEL_CNTRL &amp;    // UPDN bit decides direction count
           QEI_INT_CLK &amp;          // Use FCY for clocking
           QEI_INDEX_RESET_DISABLE &amp;
           QEI_CLK_PRESCALE_1 &amp;    // 1:1 Prescale
           QEI_GATED_ACC_DISABLE &amp;
           QEI_NORMAL_IO &amp;        // QEI Control state of IO pin
           QEI_INPUTS_NOSWAP &amp;    // Channels A and B are not swapped
           QEI_MODE_x2_MATCH &amp;    // X2 mode with counter reset by match
           QEI_UP_COUNT &amp;         // Read only for this mode
           QEI_IDLE_STOP,         // Stop in idle operation
           MATCH_INDEX_INPUT_PHASEA &amp;
           QEI_QE_CLK_DIVIDE_1_16 &amp;// Filter 1:16 divider
           QEI_QE_OUT_ENABLE);    // Enable the input digital filter
<wbr>
}
<wbr>
/*------------------------------------------------------------------*/
long GetQEI()
{
	extern volatile unsigned int ct_turns;
	return (long) ct_turns * 65535 + POSCNT;
}
<wbr>
/*------------------------------------------------------------------*/
void __attribute__((__interrupt__)) _QEIInterrupt(void)
{
	extern volatile unsigned int ct_turns;
	// if it overflowed
	  if (ReadQEI() &lt; 0x3FFF){
	    ct_turns++;
	  } else {
	    ct_turns--;
	  }
	 // clear the interrupt flag
	  IFS2bits.QEIIF =0;
}
</code></pre><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<span style="color:#bf0000">Considere downloading the <a href="/forum/topic/100/#p271">QEI implementation from the previous post</a> (realized and tested by Mariano)</span></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/40-Model_QEItest2.png">Pièce jointe : Model_QEItest2.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/41-ConfigurationParameters.png">Pièce jointe : ConfigurationParameters.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/42-block_QEIInit.png">Pièce jointe : block_QEIInit.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/43-block_GetQEI.png">Pièce jointe : block_GetQEI.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/44-Dialog1_GlobalParam.png">Pièce jointe : Dialog1_GlobalParam.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/45-Dialog2_GlobalParam.png">Pièce jointe : Dialog2_GlobalParam.png</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/46-QEI_CFunction_v02.zip">Pièce jointe : QEI_CFunction_v02.zip</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/47-C_functionCall_Example.zip">Pièce jointe : C_functionCall_Example.zip</a></p>
</article>

<article class="forum-post" id="p273">
<header><strong>malife</strong><time datetime="2008-03-21 02:56 UTC">2008-03-21 02:56 UTC</time></header>
<h3>Re: Implementing the C Function Call</h3>
<div class="forum-post-body">Great Example Lubin. Thanks for the tip on the ct_turns variable. I find that more elegant than declaring a "ghost" variable from the code since in my example directly from the Simulink Model you can't really see that there is a global variable. Anyways, between the two examples it should be now more than clear how to use the C Function Call. Thanks !<br>
<br>
<br>
<br>
One thing though. I might be mistaken but I think that even if you put for sample time inf on the C Function call, it still is called on every step, at least it was on my case, but maybe I was doing something wrong. I had to import the code to MPLab and using the debugger figure out what was going on. That is why I choose the enabled system approach. Could you confirm that? <br>
<br>
<br>
<br>
Thanks!<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p277">
<header><strong>LubinKerhuel</strong><time datetime="2008-03-26 00:23 UTC">2008-03-26 00:23 UTC</time></header>
<h3>Re: Implementing the C Function Call</h3>
<div class="forum-post-body">Will check that. One advantage to initialize the way you do is that your initialization is last (not erased by the "standard initialisation code)<br>
<br>
<br>
<br>
However, I noticed a possible bug on the file myQEI.c, in the initialisation function :<br>
<br>
<br>
<pre><code>void QEIInit(void)
{
<wbr>
  // Configure I/O Ports
  ADPCFG = 0xFFFF; //ADPCFG | 0x0030;       // Disable the A/D pins 4 and 5
  TRISB = 0xFFFF; //TRISB | 0x0030;        // configure pins 4 and 5 as inputs
...</code></pre><br>
<br>
about the ADPCFG and TRISB register, ONLY the concerned bit used by the peripheral QEI should be modified (when required). Modifying the whole register could erase configuration of other peripheral.<br>
<br>
considere using binary mask (It is done in the comment I guess )<br>
<br>
<br>
<br>
Lubin</div>
</article>

