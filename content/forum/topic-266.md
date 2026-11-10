---
title: "QEI - changed target, stoped working"
url: "/forum/topic/266/"
archiveKind: "topic"
---
# QEI - changed target, stoped working

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p1040">
<header><strong>Bobes</strong><time datetime="2010-01-21 04:15 UTC">2010-01-21 04:15 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
I think, it is some trivial problem, but I can not find out where...<br>
<br>
I have used the example from here: <a href="/forum/topic/100/">viewtopic.php?f=1&amp;t=100&amp;start=0&amp;st=0&amp;sk=t&amp;sd=a#p266</a><br>
<br>
When I compile as it is, it works fine, but when I change target to 33FJ128MC804 I start getting these errors:<br>
<pre><code>D:\bobes\0 skola\_car4\my matlab\dsPIC33\QEI 5\QEITest2_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2009a\bin\win32\gmake" -f QEITest2.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  
''pic30-gcc  -c -mcpu=33fj128MC804 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2009a/simulink/include -IC:\PROGRA~1\MATLAB\R2009a/extern/include -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src/ext_mode/common -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1\QEITest2_dspic\sources -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1 -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    QEITest2_data.c 
''pic30-gcc  -c -mcpu=33fj128MC804 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2009a/simulink/include -IC:\PROGRA~1\MATLAB\R2009a/extern/include -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src/ext_mode/common -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1\QEITest2_dspic\sources -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1 -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    QEITest2_main.c 
''pic30-gcc  -c -mcpu=33fj128MC804 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2009a/simulink/include -IC:\PROGRA~1\MATLAB\R2009a/extern/include -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2009a/rtw/c/src/ext_mode/common -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1\QEITest2_dspic\sources -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI5~1 -ID:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c: In function 'QEIInit': 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:5: error: 'QEI_INT_ENABLE' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:5: error: (Each undeclared identifier is reported only once 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:5: error: for each function it appears in.) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:6: error: 'QEI_INT_PRI_5' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:11: error: 'QEI_DIR_SEL_CNTRL' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:12: error: 'QEI_INT_CLK' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:13: error: 'QEI_INDEX_RESET_DISABLE' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:14: error: 'QEI_CLK_PRESCALE_1' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:15: error: 'QEI_GATED_ACC_DISABLE' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:16: error: 'QEI_NORMAL_IO' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:17: error: 'QEI_INPUTS_NOSWAP' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:18: error: 'QEI_MODE_x2_MATCH' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:19: error: 'QEI_UP_COUNT' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:20: error: 'QEI_IDLE_STOP' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:21: error: 'MATCH_INDEX_INPUT_PHASEA' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:22: error: 'QEI_QE_CLK_DIVIDE_1_16' undeclared (first use in this function) 
D:\bobes\0SKOLA~1\_car4\MYMATL~1\dsPIC33\QEI6~1/QEI_Functions.c:23: error: 'QEI_QE_OUT_ENABLE' undeclared (first use in this function) 
gmake: *** [QEI_Functions.o] Error 255 
### Real-Time Workshop build procedure for model: 'QEITest2' aborted due to an error.</code></pre><br>
<br>
I have changed include in QEI_functions.c to #include &lt;p33FJ128MC804.h&gt;. It seems it does not find qei.h, but it is included, and it is in place (otherwise, it would not work in the first place - before changing the target)<br>
<pre><code>void __attribute__((__interrupt__)) _QEI1Interrupt(void)
{
	extern volatile unsigned int ct_turns;
	// if it overflowed
	  if (ReadQEI() &lt; 0x3FFF){
	    ct_turns++;
	  } else {
	    ct_turns--;
	  }
	 // clear the interrupt flag
	  IFS3bits.QEI1IF =0;
}</code></pre><br>
This is how I changed the Interrupt routine, I believe the problem may be, that the target I am using has 2 QEI. However I can´t find out why it does not take qei.h in consideration?<br>
<br>
If someone has tryed using two QEI, or have an idea where I should look for a solution, please advice.<br>
<br>
Thanks<br>
<br>
Kind regards<br>
<br>
Josef</div>
</article>

<article class="forum-post" id="p1041">
<header><strong>LubinKerhuel</strong><time datetime="2010-01-21 16:13 UTC">2010-01-21 16:13 UTC</time></header>
<h3>Re: QEI - changed target, stoped working</h3>
<div class="forum-post-body">Hi Josef,<br>
<br>
<br>
<br>
typically, chips that have 2 identical peripheral will have a peripheral ref in the peripheral configuration register, like QEI1 / QEI2.<br>
<br>
You should have a look on the doc of the chip.<br>
<br>
<br>
<br>
anyway, I did not has occasions to work on QEI peripheral. You may post your question after the forum thread you mentionned. Thus, "QEI developers" will get mails and you may get a more detailed response from them...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1042">
<header><strong>Bobes</strong><time datetime="2010-01-21 21:12 UTC">2010-01-21 21:12 UTC</time></header>
<h3>Re: QEI - changed target, stoped working</h3>
<div class="forum-post-body">Hello, we (actually my colleague did) have sorted out the problem, right now I am not exactly sure why it did not work, I hope I will have some time to make some report on that and publish it here, just not sure when yet.<br>
<br>
I did correct the QEI numbering before I posted here.... and that works now. However I have still to modify the c-function to work for two QEI... that will take some time as it is not my priority.</div>
</article>

