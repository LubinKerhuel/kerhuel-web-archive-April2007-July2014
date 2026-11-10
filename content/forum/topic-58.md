---
title: "QEI module"
url: "/forum/topic/58/"
archiveKind: "topic"
---
# QEI module

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p107">
<header><strong>lakmal</strong><time datetime="2007-09-17 02:15 UTC">2007-09-17 02:15 UTC</time></header>
<div class="forum-post-body">Do you have any plans of developing a SIMULINK block for the QEI interface?<br>
<br>
<br>
<br>
Is it possible to develop my own dsPIC (or any other PIC) Simulink block using the Simulink's "S function builder" ?</div>
</article>

<article class="forum-post" id="p108">
<header><strong>LubinKerhuel</strong><time datetime="2007-09-18 20:30 UTC">2007-09-18 20:30 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
QEI is not planned in a near future. My priority is:<br>
<br>
-	Make the toolbox compatible with all matlab version<br>
<br>
(Chinese, Japanese etc…)<br>
<br>
-	Make the I2C blockset<br>
<br>
-	Make the CAN blockset<br>
<br>
Then I will look at others peripheral like QEI.<br>
<br>
<br>
<br>
I do not know how to build a block for dsPIC using the Simulink's "S function builder". I do not know if this is possible.<br>
<br>
However, you could use the ‘Custom C function’ of the dsPIC toolbox to build easily your own Simulink block generating C code for dsPIC. Do you need an example on how using this block ?<br>
<br>
Note that this block is not available in the evaluation version of the toolbox.<br>
<br>
<br>
<br>
For information, I am planning to release version of the toolbox supporting only one microcontroller. This version will be cheaper, allowing hobbyists and students to get a complete version for the microcontroller they are using.</div>
</article>

<article class="forum-post" id="p269">
<header><strong>malife</strong><time datetime="2008-03-20 23:37 UTC">2008-03-20 23:37 UTC</time></header>
<h3>Re: QEI module</h3>
<div class="forum-post-body">If you are looking on how to implement the QEI module and have a registered version (that includes the C function call) take a look at <a href="/forum/topic/100/">this example</a> of how to implement the QEI with the C Function Call block<br>
<br>
<br>
<br>
Hope you find this helpful.<br>
<br>
<br>
<br>
Mariano</div>
</article>

<article class="forum-post" id="p680">
<header><strong>Simon_says</strong><time datetime="2009-01-10 21:53 UTC">2009-01-10 21:53 UTC</time></header>
<h3>Re: QEI module</h3>
<div class="forum-post-body">Hello Lubin...<br>
<br>
 I need some help with this model. I tried to read the QEI module using Mariano example and it worked fine. Thanks a lot Mariano! However, I tried to use your sample model  with a slight modification in order to read the counts of the QEI unsuccesfully. Coul you advise me if I am doing  something wrong?  Here is the model and the C code (same as yours) . I am still learning the dsPIC and the way to use the C function block. I am having a lot of questions that I´ll  ask soon... But so far so good. Thanks  a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/177-QEI_Functions.c">Pièce jointe : QEI_Functions.c</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/178-QEI1.mdl">Pièce jointe : QEI1.mdl</a></p>
</article>

<article class="forum-post" id="p1328">
<header><strong>Bobes</strong><time datetime="2010-11-17 22:13 UTC">2010-11-17 22:13 UTC</time></header>
<h3>Re: QEI module</h3>
<div class="forum-post-body">Well, I should have posted this sooner, but this is the code modification for 2 encoders, on dsPIC33fj128mc804<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;#include &lt;p33FJ128MC804.h&gt;
<wbr>
void QEIInit(void){
<wbr>
<wbr>
 //QEI configuration register 
  POS1CNT = 0;               // Set Current Position 
  MAX1CNT = 0;              // Use QEI in 2x mode
<wbr>
  POS2CNT = 0;               // Set Current Position
  MAX2CNT = 0;              // Use QEI in 2x mode
<wbr>
  DFLT1CON = 0b0000000100000000;        // Digital filter set to off, Count Error Interrupt Disable
  DFLT2CON = 0b0000000100000000;        // Digital filter set to off, Count Error Interrupt Disable
<wbr>
  QEI1CONbits.QEIM = 7;           // x4 reset by MAXCNT pulse
  QEI1CONbits.POSRES = 0;         // doesn't Allow Index pulse to reset counter
  QEI1CONbits.SWPAB = 1;          // direction 
<wbr>
  QEI2CONbits.QEIM = 7;           // x4 reset by MAXCNT pulse
  QEI2CONbits.POSRES = 0;         // doesn't Allow Index pulse to reset counter
  QEI2CONbits.SWPAB = 1;          // direction 
<wbr>
  //ConfigIntQEI 
    IEC3bits.QEI1IE = 1;                // Enable QEI interrupt
    IPC14bits.QEI1IP = 2;               // Interrupt priority level 2
<wbr>
    IEC4bits.QEI2IE = 1;                // Enable QEI interrupt
    IPC18bits.QEI2IP = 2;               // Interrupt priority level 2
   // extern volatile int ct_turns;
   // ct_turns = 0x8000;
<wbr>
}
<wbr>
<wbr>
<wbr>
/*------------------------------------------------------------------*/
void __attribute__((__interrupt__)) _QEI1Interrupt(void)
{
   extern volatile int ct_turnsE1;
   // if it overflowed
     if (QEI1CONbits.UPDN ==  1){
       ct_turnsE1++;
     } else {
       ct_turnsE1--;
     }
     IFS3bits.QEI1IF = 0;    // clear the interrupt flag
}
<wbr>
void __attribute__((__interrupt__)) _QEI2Interrupt(void)
{
   extern volatile int ct_turnsE2;
   // if it overflowed
     if (QEI2CONbits.UPDN ==  1){
       ct_turnsE2++;
     } else {
       ct_turnsE2--;
     }
     IFS4bits.QEI2IF = 0;    // clear the interrupt flag
}
<wbr>
</code></pre></div>
</article>

