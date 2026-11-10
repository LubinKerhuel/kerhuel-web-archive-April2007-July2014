---
title: "Two-speed start-up"
url: "/forum/topic/157/"
archiveKind: "topic"
---
# Two-speed start-up

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p516">
<header><strong>Bernard Leak</strong><time datetime="2008-09-16 13:35 UTC">2008-09-16 13:35 UTC</time></header>
<div class="forum-post-body">M. Kerhuel,<br>
<br>
                   we use the PIC mechanism for two-speed start-up, and we would very<br>
<br>
much like this to be supported in the block-set.   The necessary strange invocations<br>
<br>
for the dsPIC33F series follow (taken from the Microchip manual section 70186b.pdf).<br>
<br>
I believe it's similar for other PIC variants, but have not checked.<br>
<br>
<br>
<br>
The extra configuration settings (in _FOSC()) are<br>
<br>
FCKSM_CSECME         Both enabled<br>
<br>
FCKSM_CSECMD         Only clock switching enabled<br>
<br>
FCKSM_CSDCMD         Both disabled   (default, as the block-set does at present)<br>
<br>
<br>
<br>
                                                     Bernard Leak.<br>
<br>
<br>
<br>
<br>
<br>
Just *after* setting PLLFBD and CLKDIV as at present, the oscillator mode can be<br>
<br>
switched over as follows:<br>
<br>
<br>
<br>
;Place the New Oscillator Selection (NOSC=0b101) in W0<br>
<br>
MOV #0x15,w0<br>
<br>
;OSCCONH (high byte) Unlock Sequence<br>
<br>
MOV #OSCCONH, w1<br>
<br>
MOV #0x78, w2<br>
<br>
MOV #0x9A, w3<br>
<br>
MOV.B w2, [w1] ; Write 0x78<br>
<br>
MOV.B w3, [w1] ; Write 0x9A<br>
<br>
;Set New Oscillator Selection<br>
<br>
MOV.B w0, [w1]<br>
<br>
; Place 0x01 in W0 for setting clock switch enabled bit<br>
<br>
MOV #0x01, w0<br>
<br>
;OSCCONL (low byte) Unlock Sequence<br>
<br>
MOV #OSCCONL, w1<br>
<br>
MOV #0x46, w2<br>
<br>
MOV #0x57, w3<br>
<br>
MOV.B w2, [w1] ; Write 0x46<br>
<br>
MOV.B w3, [w1] ; Write 0x9A<br>
<br>
; Enable Clock Switch<br>
<br>
MOV.B w0, [w1] ; Request Clock Switching by Setting OSWEN bit<br>
<br>
wait:<br>
<br>
btsc OSCCONL, #OSWEN<br>
<br>
bra wait</div>
</article>

<article class="forum-post" id="p517">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-16 16:29 UTC">2008-09-16 16:29 UTC</time></header>
<h3>Re: Two-speed start-up</h3>
<div class="forum-post-body">Dear Bernard,<br>
<br>
<br>
<br>
I am not sure to understand what your need is.<br>
<br>
Do you want to manually "change" the clock source within the program (i.e. add a block to do it in the simulink model ?)<br>
<br>
<br>
<br>
<br>
<br>
Or do you want to use the "Two Speed Start-up" as it is described from the 70186b.pdf doc you mentioned page 7-31 ?<br>
<br>
In this last case, my understanding of this page is the following: <br>
<br>
The include file of dsPIC33 has the following parameters : <br>
<br>
<br>
<br>
;   Two-speed Oscillator Startup :<br>
<br>
;     IESO_OFF             Disabled<br>
<br>
;     IESO_ON              Enabled<br>
<br>
<br>
<br>
The blockset always set the two speed startup to off (IESO_OFF).<br>
<br>
<br>
<br>
If I add an option so as to configure it to (IESO_ON), the two speed startup will be enabled. Thus, the dsPIC will start with the internal FRC clock and when the "user source clock" will be working, it will switch <strong> automatically </strong> to this source clock.<br>
<br>
<br>
<br>
Is it right? (I did not tested yet the two speed startup ? )<br>
<br>
Is this solution what you are asking for?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p518">
<header><strong>Bernard Leak</strong><time datetime="2008-09-17 17:35 UTC">2008-09-17 17:35 UTC</time></header>
<h3>Re: Two-speed start-up</h3>
<div class="forum-post-body">Apologies! The "two-speed start-up" is a complete red herring: I misunderstood what it meant.<br>
<br>
This simplifies things.  If you give an option in the "Master" block which allows the oscillator<br>
<br>
to be changed, that would help.  I only want to set the oscillator once, as early as possible,<br>
<br>
and I can do that with a block of my own, though it would be kind if you supplied one<br>
<br>
yourself.<br>
<br>
   The reason why I need it is one which I don't fully understand (it depends on the<br>
<br>
hardware outside the chip).  For some reason, although our external oscillator is fine<br>
<br>
(we start up with it), we can't start using the oscillator AND the PLL until later.<br>
<br>
At the beginning of main() is not too early!  Moreover, we do need to wait until the new<br>
<br>
oscillator state is stable before using it.  I therefore start with the XT HS oscillator, then<br>
<br>
drop briefly to the RFC oscillator, and return to the XT HS oscillator, this time with the PLL. <br>
<br>
The easiest way to do this is, as I suggested, to replace the existing PLL and CLKDIV<br>
<br>
setting.<br>
<br>
<br>
<br>
                             Bernard.</div>
</article>

<article class="forum-post" id="p521">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-21 18:01 UTC">2008-09-21 18:01 UTC</time></header>
<h3>Re: Two-speed start-up</h3>
<div class="forum-post-body">Hi Bernard, <br>
<br>
<br>
<br>
I did not looked at this problem yet. I'll do it shortly...</div>
</article>

