---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Master"
url: "/wiki/dspic-block-master/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Master.png" alt="Master Block">

<figcaption>

Master Block

</figcaption>
</figure>

<Big>The Master block set important dsPIC options like PLL, Quartz used, and share theses parameters with others blocks from the blockset.</Big>

# Dialog Box Parameters {#dialog_box_parameters}

**The dialog box parameters differs depending on which microcontroller is used**. Unexpected close of the dialog box and few errors when re-opening it may appears when selecting a different chip. This has no consequence.

The principal change concern the **Real Time Quartz** tab. see [Instruction Cycle Frequency](/wiki/dspic-block-master/#instruction-cycle-frequency)

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Master_DialogBox.png" alt="Master Block Dialog for the 30f3012 chip, General Tab" width="400">

<figcaption>

Master Block Dialog for the 30f3012 chip, General Tab

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Master_DialogBox_Quartz.png" alt="Master Block Dialog for the 30f3012 chip, Quartz Tab" width="400">

<figcaption>

Master Block Dialog for the 30f3012 chip, Quartz Tab

</figcaption>
</figure>

## Step Based on {#step_based_on}

- Tmer1 : The model time step is set using the Timer1 automatically configured (Prescaler and PR1).
- ADC : The ADC conversion time can be used only when the ADC block is set to produce two or more sample per channel. The conversion time is \'augmented\' so as to have reach the model time step at the end of all conversion needed in 1 time step.
- Free Run : The model execute at its maximum speed. The Time step is not constant since the calculation time may changed slightly between time step. The simulink model time step is not taken into acount.

## PIC

Specify the Microchip microcontroller target.

59 Supported devices :

<div class="chip-matrix"><table> <tbody> <tr> <td> <p><strong>See <a href="/wiki/release-notes/">Release Notes and known bug</a> for details</strong></p> <table> <tbody> <tr> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 24F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 32F**</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 30F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 30F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ GP</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ MC</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ GP</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ MC*</th> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX360F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP206</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP202</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC202</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX360F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP306</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP204</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC204</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX460F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5015</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP310</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP802</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC802</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX460F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5016</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC508</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP804</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC804</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX775F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32GP302</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32MC302</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX775F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32GP304</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32MC304</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX795F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP202</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC202</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX320</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3014</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP204</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC204</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX340</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6014</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP802</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC802</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ16GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6015</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP206</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP804</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC804</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ32GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP306</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ48GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP310</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ16GA004</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ32GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ48GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> </tbody> </table> <dl> <dt>Newly added chip</dt> <dd> 64MC204, 128MC204, 128GP202, 32MC202, 32MC204, 16MC304 , 33FJ256GP710A </dd> <dt>* PIC 32F</dt> <dd> SPI function not suported yet; </dd> <dt>* Compiler known and fixed bugs</dt> <dd> </dd> <dt>* Check your compiler installation and version</dt> <dd> at the matlab prompt ==&gt; <strong>!pic30-gcc -v</strong> for pic30 and <strong>!pic32-gcc -v</strong> for pic32. </dd> <dt>**Check pic32 compiler <a href="/wiki/pic32-gcc-v1-04-bugfix/"> v 1.04 Workaround</a><br /> **Check pic30 compiler <a href="/wiki/pic30-gcc-v3-12-bugfix/"> PWM 2 Workaround</a> from version v 3.12 to current version (3.25)...<br /> </dt> </dl> </td> </tr> </tbody> </table> <p></p></div>

## Instruction Cycle Frequency {#instruction_cycle_frequency}

<figure class="wiki-figure">

<img loading="lazy" src="/images/TimeStep_SingleRateTimer1.png" alt="Time Step  reference is Timer 1. Timer 1 prescaler and PR1 register are configured  so as to meet the time step set in Simulink. When Timer 1 reach PR1, it  is reset and a next step is started." width="400">

<figcaption>

Time Step reference is Timer 1. Timer 1 prescaler and PR1 register are configured so as to meet the time step set in Simulink. When Timer 1 reach PR1, it is reset and a next step is started.

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/TimeStep_SingleRateADC.png" alt="Time  Step reference is the ADC peripheral. ADC conversion are slowed down so  as to meet the time step requirement set in Simulink. On this example,  Three channels are converted ; Two sample are read at each step (i.e.  the three ADC blocks output are vectors of 2 elements each)." width="400">

<figcaption>

Time Step reference is the ADC peripheral. ADC conversion are slowed down so as to meet the time step requirement set in Simulink. On this example, Three channels are converted ; Two sample are read at each step (i.e. the three ADC blocks output are vectors of 2 elements each).

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/TimeStep_SingleRateFreeRun.png" alt="Time  Step in Free Run mode. The model is executed as fast as it can. The  time step set in Simulink is not respected." width="400">

<figcaption>

Time Step in Free Run mode. The model is executed as fast as it can. The time step set in Simulink is not respected.

</figcaption>
</figure>

Specify or shows the number of Instruction Per Secondes (MIPS) executed (in million here). Configuratoin of UART baud, timers prescaler and the real-timetime step **rely on this frequency information**.

For 30f family microcontroller
:   You must compute yourself the Instruction Per Seconds using :

<math display="inline"><semantics><mrow><mi>I</mi><mi>P</mi><mi>S</mi><mo>=</mo><mfrac><mrow><mi>F</mi><mi>r</mi><mi>e</mi><mi>q</mi><mi>Q</mi><mi>u</mi><mi>a</mi><mi>r</mi><mi>t</mi><mi>z</mi></mrow><mn>4</mn></mfrac><mo>*</mo><mi>P</mi><mi>L</mi><msub><mi>L</mi><mrow><mi>f</mi><mi>a</mi><mi>c</mi><mi>t</mi><mi>o</mi><mi>r</mi></mrow></msub></mrow><annotation encoding="application/x-tex">IPS = \frac{FreqQuartz}{4} * PLL_{factor}</annotation></semantics></math>

:   With FreqQuartz the frequency of the source (Quartz or internal oscillator, External Clock \...) and with PLL factor set to 1 when PLL multiplication is not used.

<!-- -->

For 24, 33 and 32 microcontroller
:   The Instruction Per Seconds is automatically computed using the Quartz frequency provided. If you activate the PLL multiplication, you have to enter the **Desired Instruction Cycle Frequency** (24f,32f and 33f dialog box only).

<!-- -->

:   From the entered Desired Instruction Cycle Frequency, the toolbox compute the best PLL multiplication which provides the Instruction Cycle Frequency the closest to the Desired one.

## Config Timer {#config_timer}

Set the prescaler for the timer 2,3 and 4,5 when available in the microcontrôller. Theses times are used by certain periphery like Output Compare, Input Capture. Set -1 for the timer prescaler to be set by matlab using optimal criterion.

Forcing a prescaler for one timer can be done by replacing -1 with your prescaler value. You must beware that when one peripheral use a timer, the timer value must not be changed as this would cause peripheral failure. Setting two timers with the same prescaler will insure that the second one will not be used by any peripheral. You will then be able to modify this timer value without affecting peripheral.

32 bits timer cannot be configured.

## Busy Flag Port {#busy_flag_port}

Set the port specified to 1 during the time step calculation and 0 during idle time. This allow to check that all calculation are finished in less that one time step.

## Overload Flag Port {#overload_flag_port}

Set the port specified to 1 during one time step if the previous time step was not finished when starting the execution of current time step.

## config Oscillator mode {#config_oscillator_mode}

Sepecify PIC Oscillator configuration.

## config Born Out Reset {#config_born_out_reset}

Specify Voltage under which the microcontrôller Reset.

## config Power Time {#config_power_time}

Specify time for the pic to start onced powered. (Lets time for alimentation tension to settle properly before starting instructions execution).

## config MCLR {#config_mclr}

If disable, MCLR pin has not the hardware reset function on programme execution. When enable, Pic stop execution and reset when MCLR pin is in its low state.

------------------------------------------------------------------------

\<comments \\\>
