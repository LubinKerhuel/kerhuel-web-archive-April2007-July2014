---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:57Z"
title: "DsPIC Block/PWM Motor Output"
url: "/wiki/dspic-block-pwm-motor-output/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_PWM_Motor_Output.png" alt="Block PWM Motor Output">

<figcaption>

Block PWM Motor Output

</figcaption>
</figure>

The PWM Motor block allows to generate either simple PWM pulse like OC block or PWM pulse with two channel in opposit phase for motor control. This block do not use a timer like the OC or IC blocks.

# Main Dialog Box Parameters {#main_dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_PWMMotor_DialogBox.png" alt="PWM Motor Output main Dialog" width="400">

<figcaption>

PWM Motor Output main Dialog

</figcaption>
</figure>

## General Input Enable {#general_input_enable}

Add the enable input to the block. Allow to Start and Stop the PWM pulses.

## Input Periode {#input_periode}

Add the Periode Input. When the PWM periode is not constant, this input allow to control the PWM periode dynamically. **Only one Input Periode appears** as this periode is common for PWM channels of the PWM peripheral. If your application require different input period, you may either

- use the second PWM peripheral if the chip has two PWM peripheral (PWM1 and PWM2) or
- use the [Output Compare (OC)](/wiki/dspic-block-output-compare/), or [Output Compare Hardware (OC_HW)](/wiki/dspic-block-output-compare-hw/) block that are able to generate PWM signals with differents Periode for each channel.

## Output Channel {#output_channel}

Choose the PWM motor Channels to be used.

## Periode

- When Input Periode is disable, Fixed the Periode value.
- When Input Periode is enable, This define the max Periode that will be used.

All temporal value provided to the bock input must be uint16 variable. The integer variable PWMmax created automatically in the workspace code for the time defined in Periode. Thus, any temporal value at block input must be multiplied by <math display="inline"><semantics><mfrac><mrow><mi>P</mi><mi>W</mi><mi>M</mi><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mrow><mi>P</mi><mi>e</mi><mi>r</mi><mi>i</mi><mi>o</mi><mi>d</mi><mi>e</mi></mrow></mfrac><annotation encoding="application/x-tex">\frac{PWMmax}{Periode}</annotation></semantics></math>. integer value at block input = <math display="inline"><semantics><mrow><msub><mi>T</mi><mrow><mi>s</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>*</mo><mfrac><mrow><mi>P</mi><mi>W</mi><mi>M</mi><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mrow><mi>P</mi><mi>e</mi><mi>r</mi><mi>i</mi><mi>o</mi><mi>d</mi><mi>e</mi></mrow></mfrac></mrow><annotation encoding="application/x-tex">T_{set} * \frac{PWMmax}{Periode}</annotation></semantics></math>

With

- Tset = the requested time in second (should be inferior to Periode)
- Periode = The literal value (in second) you defined in the Periode dialog box
- PWMmax = a constant automatically evaluated in the matlab workspace

for example, a 1ms is coded with (Periode is set to 20ms : <math display="inline"><semantics><mrow><mn>20</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup></mrow><annotation encoding="application/x-tex">20*10^{-3}</annotation></semantics></math>):

<math display="inline"><semantics><mrow><mn>1</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup><mo>*</mo><mfrac><mrow><mi>P</mi><mi>W</mi><mi>M</mi><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mrow><mn>20</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup></mrow></mfrac></mrow><annotation encoding="application/x-tex">1*10^{-3}*\frac{PWMmax}{20*10^{-3}}</annotation></semantics></math>

## ValMax Periode Calcule {#valmax_periode_calcule}

This Variable will be evaluated in the workspace and allow you to scale the data.The ValMax is the max value that correspond to the duration defined in Periode.

## Centered

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_PWMMotor_Illustration_Centered.png" alt="Edge-Aligned PWM vs Center-Aligned PWM. Center-Aligned PWM multiply by two the max Period and Duty Cycle achievable" width="400">

<figcaption>

Edge-Aligned PWM vs Center-Aligned PWM. Center-Aligned PWM multiply by two the max Period and Duty Cycle achievable

</figcaption>
</figure>

This parameter center-aligned PWM duty cycle (see figure on the right). A side effect is to add a factor 2 to the internal PWM prescaler. Thus, This option multiply by 2 the MAX Period and the MAX duty Cycle time that can be achieved. However, for fast PWM (with prescalar set to 1), this option divide by two the resolution.

## Activate H Complementary Output {#activate_h_complementary_output}

Activate the Complementary output (**PWM l**ow) of each channel.

## Info

Gives information :

- NbrBits is the resolution for the full scale defined by Periode.
- PWM max value corresponing to the time defined in Periode. PWM is evaluated in the workspace to allow you to scale the data.
- Prescaler is the Prescaler internally used in the microcontroller..

## Status

Information if error encountred.

# Dead Time TAB {#dead_time_tab}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_PWMMotor_DialogBox_DeadTime.png" alt="PWM Motor Output Dead Time Dialog. some dsPIC has only one Dead Time Prescaler. This Dialog may be different, depending on the dsPIC being used" width="400">

<figcaption>

PWM Motor Output Dead Time Dialog. some dsPIC has only one Dead Time Prescaler. This Dialog may be different, depending on the dsPIC being used

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_PWMMotor_Illustration_DeadTime.png" alt="PWM motor Dead Time" width="400">

<figcaption>

PWM motor Dead Time

</figcaption>
</figure>

This tab may change. Some PIC / dsPIC has only one Dead Time, others have two.

## Dead Time A - B {#dead_time_a___b}

Value in second for Dead Time A or B. When only one Dead time is available on the chip, only one value is requested and this value affect all PWM channels.

## Dead Time Info {#dead_time_info}

Get the real Dead Time value achievable

## Dead Time PWMx Active {#dead_time_pwmx_active}

**PWM h**igh : delay the positive edge of the selected Dead Time (see figure)

## Dead Time PWMx Inactive {#dead_time_pwmx_inactive}

**PWM l**ow : delay the positive edge of the selected Dead Time (see figure)

# Know Bugs {#know_bugs}

## PWM 2 peripheral : error at compilation time {#pwm_2_peripheral_error_at_compilation_time}

Microchip pwm12.h definition has an error that cause a **error** at compilation time when using **PWM2 peripheral**. [Read the workaround](/wiki/pic30-gcc-v3-12-bugfix/).

------------------------------------------------------------------------
