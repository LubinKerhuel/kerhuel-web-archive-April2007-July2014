---
title: "DAC on 33fj64GP802"
url: "/forum/topic/176/"
archiveKind: "topic"
---
# DAC on 33fj64GP802

Forum : [General Remark and Questions](/forum/#forum-1)

16 message(s) · archive en lecture seule

<article class="forum-post" id="p612">
<header><strong>Lucien</strong><time datetime="2008-11-20 12:48 UTC">2008-11-20 12:48 UTC</time></header>
<div class="forum-post-body">Hello, <br>
<br>
<br>
<br>
Is there any block  "DAC" (digital analog converter) for the 33fj64GP802 in the simulink dspic library ?  <br>
<br>
<br>
<br>
Lucien</div>
</article>

<article class="forum-post" id="p616">
<header><strong>LubinKerhuel</strong><time datetime="2008-11-28 00:43 UTC">2008-11-28 00:43 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Lucien,<br>
<br>
<br>
<br>
DAC peripheral is not yet available. <br>
<br>
Considere using the C function call to build your own function.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p775">
<header><strong>crh</strong><time datetime="2009-03-09 07:47 UTC">2009-03-09 07:47 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
I wonder if you are intend to build a dac peripheral for the 33fj64(128)GP802.<br>
<br>
<br>
<br>
Casparus</div>
</article>

<article class="forum-post" id="p778">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-11 09:14 UTC">2009-03-11 09:14 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Casparus,<br>
<br>
<br>
<br>
This is not planned yet. However, if you want to give it a try and publish results, I can provide you with a blockset with C function call avaialble.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p779">
<header><strong>crh</strong><time datetime="2009-03-11 10:23 UTC">2009-03-11 10:23 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
<br>
<br>
That should be very agreeable. <br>
<br>
Of course, I shall publish the trials and results. <br>
<br>
<br>
<br>
Casparus</div>
</article>

<article class="forum-post" id="p783">
<header><strong>Lucien</strong><time datetime="2009-03-16 12:52 UTC">2009-03-16 12:52 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I'm very always interesting for a dac peripheral for the 33fj64(128)GP802.<br>
<br>
<br>
<br>
Lucien</div>
</article>

<article class="forum-post" id="p785">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-17 00:36 UTC">2009-03-17 00:36 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Lucien, I can propose the same solution than crh (No time to have a look by myself by right-now) <br>
LubinKerhuel&lt;/em&gt;"&gt;<blockquote><header class="quote-author">Citation : &lt;em&gt;LubinKerhuel&lt;/em&gt;</header>if you want to give it a try and publish results, I can provide you with a blockset with C function call avaialble.</blockquote><br>
Let me know <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p790">
<header><strong>Lucien</strong><time datetime="2009-03-18 19:57 UTC">2009-03-18 19:57 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Lubin,<br>
<br>
<br>
<br>
Yes I'm interesting for a C call blockset. As soon as the DAC peripherical is finished, of course I will publish the results.<br>
<br>
<br>
<br>
Lucien</div>
</article>

<article class="forum-post" id="p924">
<header><strong>Lucien</strong><time datetime="2009-07-29 12:12 UTC">2009-07-29 12:12 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
My C30 code does working now for the DAc peripherical on dspic33fj64gp802.<br>
<br>
But now I must integrate it in Matlab Simulink !<br>
<br>
<br>
<br>
Here is my complete C30 code:<br>
<br>
<br>
<pre><code>#include "p33FJ64GP802.h"
#include "dsp.h"
<wbr>
<wbr>
long i,j,k;
long mydataright,mydataleft;
<wbr>
int const sinus[60]={10,500,500,150,10,500,10,10,150,500,
					500,10,350,500,10,10,10,350,500,500,
					10,10,10,10,150,150,150,150,150,150,
					350,350,350,350,500,500,500,500,500,500,
					500,150,350,10,10,350,150,500,10,150,
					150,350,10,500,500,10,150,350,10,10};
<wbr>
int const cosinus[60]={150,10,350,500,150,10,10,350,500,500,
					10,150,10,500,10,350,10,500,10,150,
					10,150,350,500,10,150,350,500,500,150,
					500,350,150,10,10,150,350,500,10,10,
					10,10,10,10,150,150,150,150,10,500,
					500,500,500,500,350,350,350,10,150};
<wbr>
void __attribute__((interrupt,no_auto_psv))_DAC1RInterrupt(void);
<wbr>
void __attribute__((interrupt,no_auto_psv))_DAC1LInterrupt(void);
<wbr>
void initDAC();
<wbr>
<wbr>
void __attribute__((interrupt,no_auto_psv)) _DAC1RInterrupt(void)
{
	IFS4bits.DAC1RIF = 0;  /* Clear Right Channel Interrupt Flag */
	DAC1RDAT = mydataright; /* User Code to Write to FIFO Goes Here */
}
<wbr>
void __attribute__((interrupt, no_auto_psv)) _DAC1LInterrupt(void)
{
	IFS4bits.DAC1LIF = 0;  /* Clear Right Channel Interrupt Flag */
	DAC1LDAT = mydataleft; /* User Code to Write to FIFO Goes Here */
}
<wbr>
<wbr>
void initDAC()
{
ACLKCONbits.SELACLK=0;
ACLKCONbits.AOSCMD=0;
ACLKCONbits.ASRCSEL=0;
ACLKCONbits.APSTSCLR=7; //divide clock by 8
<wbr>
DAC1STATbits.ROEN = 1; /* Right Channel DAC Output Enabled */ 
DAC1STATbits.LOEN = 1; /* Right Channel DAC Output Enabled */
<wbr>
DAC1STATbits.RITYPE = 0; /* Right Channel Interrupt if FIFO is not Full */ 
DAC1STATbits.LITYPE = 0; /* Right Channel Interrupt if FIFO is not Full */ 
<wbr>
DAC1CONbits.AMPON = 0; /* Amplifier Disabled During Sleep and Idle Modes */
DAC1CONbits.DACFDIV = 5; /* Divide Clock by 100 (Assumes Clock is 25.6MHz) */
							//PLLCLK=80MHZ ; ACLK=10MHz ; DACCLK=100kHz
<wbr>
DAC1CONbits.FORM = 0; /* Data Format is unsigned integer */
DAC1DFLT = 0x8000; /* Default value set to Midpoint when FORM = 0 */
<wbr>
IFS4bits.DAC1RIF = 0; /* Clear Right Channel Interrupt Flag */
IFS4bits.DAC1LIF = 0; /* Clear Right Channel Interrupt Flag */
IEC4bits.DAC1RIE = 1; /* Right Channel Interrupt Enabled */
IEC4bits.DAC1LIE = 1; /* Right Channel Interrupt Enabled */
<wbr>
DAC1CONbits.DACEN = 1; /* DAC1 Module Enabled */
<wbr>
}
<wbr>
<wbr>
long writeDACdataR(void)
{
 	mydataright=128*sinus[i];
	mydataleft=128*cosinus[i];
<wbr>
}
<wbr>
// Internal FRC Oscillator
_FOSCSEL(FNOSC_FRC);							// FRC Oscillator
_FOSC(FCKSM_CSECMD &amp; OSCIOFNC_ON  &amp; POSCMD_NONE);
<wbr>
//_FOSC(FCKSM_CSECMD); 
<wbr>
_FWDT(FWDTEN_OFF);              				// Watchdog Timer Enabled/disabled by user software
												// (LPRC can be disabled by clearing SWDTEN bit in RCON register
<wbr>
<wbr>
int main(void)
{
/*  Configure Oscillator to operate the device at 40Mhz
    Fosc= Fin*M/(N1*N2), Fcy=Fosc/2
    Fosc= 7.37*M*43/(2*2)=80Mhz for 7.37M internal FRC */
   PLLFBD=42;                    /* M=43 */
   CLKDIVbits.PLLPOST=0;        /* N1=2 */
   CLKDIVbits.PLLPRE=0;        /* N2=2 */
   OSCTUN=23;                    /* Tune FRC oscillator, if FRC is used */
<wbr>
/* Disable Watch Dog Timer */
   RCONbits.SWDTEN=0;
<wbr>
/* Clock switch to incorporate PLL*/
   __builtin_write_OSCCONH(0x01);        // Initiate Clock Switch to FRC
                                       // Oscillator with PLL (NOSC=0b001)
   __builtin_write_OSCCONL(0x01);        // Start clock switching
   while (OSCCONbits.COSC != 0b001);    // Wait for Clock switch to occur
<wbr>
/* Wait for PLL to lock */
while(OSCCONbits.LOCK!=1);
<wbr>
//OSCCONbits.LPOSCEN=0;
CLKDIVbits.DOZE=0b000;
CLKDIVbits.FRCDIV=0b000;
// Initiate Clock Switch to FRC oscillator with PLL (NOSC=0b001)
// Wait for Clock switch to occur
while (OSCCONbits.COSC != 0b001);
<wbr>
<wbr>
<wbr>
<wbr>
initDAC();
<wbr>
i=1;
k=0;
for(;;)
	{
<wbr>
	while (j&lt;400)	
		{
		j=j+1;
		}
	j=0;
	i=i+1;
	writeDACdataR();
<wbr>
	if (i&gt;60)
		{
			i=0;
		}
<wbr>
<wbr>
	}
}</code></pre></div>
</article>

<article class="forum-post" id="p925">
<header><strong>LubinKerhuel</strong><time datetime="2009-07-29 13:04 UTC">2009-07-29 13:04 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Lucien, Do you have a blockst version with the C call function unrestricted ?<br>
<br>
If not, send me an email with the matlab version you are using, I'll provide you with that.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1495">
<header><strong>jannypan</strong><time datetime="2011-03-05 06:09 UTC">2011-03-05 06:09 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">I'm very always interesting for a dac peripheral for the 33fj64(128)GP802.</div>
</article>

<article class="forum-post" id="p1582">
<header><strong>kaab</strong><time datetime="2011-05-18 23:45 UTC">2011-05-18 23:45 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">Hi Lucien, did you figure out how the block of DAC for 33fj128GP802? I am working on a project and that will be very helpful to me. Thanks</div>
</article>

<article class="forum-post" id="p1587">
<header><strong>yannick</strong><time datetime="2011-05-27 08:11 UTC">2011-05-27 08:11 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">can you show me what is inside your header dsp.h ? <br>
<br>
<br>
<br>
How do you define your dsPIC ?<br>
<br>
<br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p1742">
<header><strong>yingxuy</strong><time datetime="2011-11-30 01:46 UTC">2011-11-30 01:46 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">I am interested in the C library calls the module. As long as the DAC peripherical is finished, of course, I will publish the results. ...</div>
</article>

<article class="forum-post" id="p2029">
<header><strong>Casper</strong><time datetime="2013-10-03 07:22 UTC">2013-10-03 07:22 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">It is learned from school physics, that an analog-to-digital converter is a device that converts a continuous physical quantity (usually voltage) to a digital number that represents the quantity's amplitude. It needs operating range as 40 MIPS and a high performance DSC CPU.<br>
<br>
<br>
<br>
<br>
<br>
Thanks<br>
<br>
<a href="http://www.snoringaidsnow.org">http://www.snoringaidsnow.org</a></div>
</article>

<article class="forum-post" id="p3478">
<header><strong>chiclothe</strong><time datetime="2014-01-14 03:13 UTC">2014-01-14 03:13 UTC</time></header>
<h3>Re: DAC on 33fj64GP802</h3>
<div class="forum-post-body">This is not planned yet. However</div>
</article>

