---
title: "Changing oscillator configuration (was Two-speed start-up)"
url: "/forum/topic/161/"
archiveKind: "topic"
---
# Changing oscillator configuration (was Two-speed start-up)

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

3 message(s) · archive en lecture seule

<article class="forum-post" id="p536">
<header><strong>Bernard Leak</strong><time datetime="2008-09-25 12:20 UTC">2008-09-25 12:20 UTC</time></header>
<div class="forum-post-body">Thank you for the new block-set (0.98fe)!<br>
<br>
<br>
<br>
I have found no bugs, but there is still a problem of a different kind.<br>
<br>
For the code to run at all, I must give the model an oscillator<br>
<br>
configuration with which it can start stably.  However,<br>
<br>
none of the timers or peripheral modules are enabled until<br>
<br>
I have already changed the oscillator configuration - and then<br>
<br>
they are configured for the wrong CPU frequency!<br>
<br>
<br>
<br>
   I end up configuring the model *as though* starting at once<br>
<br>
with the modified oscillator settings: I then have to modify the<br>
<br>
&lt;modelname&gt;_main.c file in several ways:<br>
<br>
(a) The argument to _FOSCSEL() contains a FNOSC_* macro which I must change<br>
<br>
(b) The argument to _FOSC() contains a FCKSM_CS?CM? macro which I once had<br>
<br>
          to change<br>
<br>
(c) The settings of CLKDIV and PLLFBD need to be changed or removed.<br>
<br>
<br>
<br>
The effect of your latest change is that (b) is now unnecessary,<br>
<br>
but that's all!<br>
<br>
<br>
<br>
   I suggest an addition to the Master mask dialogue.  This is a<br>
<br>
parameter field with the prompt<br>
<br>
"Desired Instructions per Second for Configuring Peripherals" <br>
<br>
When clock-switching is enabled, this should be enabled too. The initial<br>
<br>
configuration macros and the PLLFBD and CLKDIV settings should still be<br>
<br>
found as usual, from the settings explicitly given, but the value of "fcy"<br>
<br>
used for configuring the peripheral modules should come from the extra<br>
<br>
parameter. For extra credit, when clock-switching is enabled, the<br>
<br>
existing prompt "Desired Instructions per Second" can be re-worded<br>
<br>
more explicitly as  "Desired Instructions per Second at power-on".<br>
<br>
<br>
<br>
This single change would make it possible to build everything from RTW<br>
<br>
without having to modify anything externally.  The intention is that the<br>
<br>
clock-setting can be handled by adjoining a custom source (or object) file,<br>
<br>
and injecting a call to it early in the &lt;modelname&gt;_Initialize()<br>
<br>
routine, using the Custom Code blocks from Real-time Workshop.<br>
<br>
<br>
<br>
                                              Bernard Leak.</div>
</article>

<article class="forum-post" id="p543">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-25 17:37 UTC">2008-09-25 17:37 UTC</time></header>
<h3>Re: Changing oscillator configuration (was Two-speed start-up)</h3>
<div class="forum-post-body">Bernard,<br>
<br>
<br>
<br>
I understand the problem since I was already thinking about it while adding the option you requested.<br>
<br>
<br>
<br>
The problem you described seems to be very specific (Does any others dsPIC users encounter a similar problem?)<br>
<br>
<br>
<br>
Anyway, thanks for proposing clear solutions.<br>
<br>
<br>
<br>
I will be out for 3 days from now (be back on Sunday). Thus, I will look at it next week.<br>
<br>
The idea is to find a solution that does not make the overall system too complicated for "new users"...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p545">
<header><strong>Bernard Leak</strong><time datetime="2008-09-26 09:35 UTC">2008-09-26 09:35 UTC</time></header>
<h3>Re: Changing oscillator configuration</h3>
<div class="forum-post-body">Dear List,<br>
<br>
                 The problem arises whenever the input frequency  to the PLL is<br>
<br>
not  in the range 4MHz to 8MHz.  The FRC is near the top of this range, at<br>
<br>
7.37MHz.  This means that HS + PLL is only possible with clock-switching.<br>
<br>
We are using 10MHz oscillators on several of our boards:<br>
<br>
hence the problem.<br>
<br>
<br>
<br>
The difficulty is with the initial states of the PLL control registers, before we get <br>
<br>
a chance to modify them.  These initial states are as follows:<br>
<br>
<br>
<br>
PLLPRE is 0 (i.e., prescale factor is 1/2),<br>
<br>
The initial frequency must be in the range 1.6MHz t 16.0MHz anyway, and<br>
<br>
after dividing by 2 it is in the range 0.8MHz to 8MHz, which is exactly the<br>
<br>
range permitted after using the pre-scaler.<br>
<br>
<br>
<br>
PLLPOST is 1 (i.e., postscale factor is 1/4)<br>
<br>
The final frequency will clearly be VCO frequency / 4, and in the range<br>
<br>
25MHz to 50MHz, which is all right.<br>
<br>
<br>
<br>
PLLDIV is 48 (i.e., PLL divider is 50)<br>
<br>
The  input to the PLL must be in the range<br>
<br>
100MHz / (PLLDIV + 2) to 200MHz / (PLLDIV + 2),<br>
<br>
that is (initially) 2MHz to 4MHz.  This corresponds<br>
<br>
to prescaler input of 4MHz to 8MHz.<br>
<br>
<br>
<br>
Bernard Leak.</div>
</article>

