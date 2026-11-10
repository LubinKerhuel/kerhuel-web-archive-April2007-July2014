---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:57Z"
title: "DsPIC Block/Output Compare HW"
url: "/wiki/dspic-block-output-compare-hw/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Output_Compare_HW.png" alt="Block Output Compare">

<figcaption>

Block Output Compare

</figcaption>
</figure>

Output driver for PWM output data.

# Outline

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_OutputCompare_DialogBox_HW.png" alt="Output Compare Dialog" width="450">

<figcaption>

Output Compare Dialog

</figcaption>
</figure>

The Output Compare Hardware (OC_HW) block generates PWM impulse on the Output Compare peripheral. This driver does not use any software, in comparison with [ PWM Output Compare block](/wiki/dspic-block-output-compare/) that use software interrupt. The two improvements (compared to [ PWM Output Compare block](/wiki/dspic-block-output-compare/)) are:

- Allow generation of very fast PWM signal
- Possibility to set accurately the ADC sampling time at any instant of the PWM period.

Drawbacks (compared to [ PWM Output Compare block](/wiki/dspic-block-output-compare/)) are:

- All PWM channels have the same Period (however, mode and duty cycle can be different)
- The peripheral will not be able to share the timer it uses with others peripheral

Three modes available allow defining PWM (block input) as:

- Time Up and Period
- Time Down and Period
- Time Set and Reset

The two first modes are robust and will never cause glitch whatever is the period or duty cycles of the PWM signal (even very fast). The third mode Time Set and Reset may cause glitch (for more details, ask on the forum).

Synchronisation with the ADC: The ADC can synchronize with the Timer 3. The sampling time starts at the end of the period. When the third mode (Time Set and Reset) is selected, it is possible to set within the timer period the rising and falling instant. This makes possible sampling at any instant of the PWM period. Input block value must be scaled using the following :

Up or Down or Periode = <math display="inline"><semantics><mrow><msub><mi>T</mi><mrow><mi>s</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>*</mo><mfrac><mrow><mi>O</mi><mi>C</mi><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mrow><mi>M</mi><mi>a</mi><mi>x</mi><mi>C</mi><mi>h</mi><mi>a</mi><mi>n</mi><mi>n</mi><mi>e</mi><mi>l</mi></mrow></mfrac></mrow><annotation encoding="application/x-tex">T_{set} * \frac{OCmax}{MaxChannel}</annotation></semantics></math>

With

- MaxChannel = The literal value (in second) you defined as the max time in the dialog box
- OCmax = a constant automatically evaluated in the matlab workspace
- Tset = the required time in second (inferior to MaxChannel)

for example, if the max value is set to 20ms (MaxChannel = <math display="inline"><semantics><mrow><mn>20</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup></mrow><annotation encoding="application/x-tex">20*10^{-3}</annotation></semantics></math>) on channel 1

<math display="inline"><semantics><mrow><mn>1</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup><mo>*</mo><mfrac><mrow><mi>O</mi><mi>C</mi><mn>1</mn><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mrow><mn>20</mn><mo>*</mo><msup><mn>10</mn><mrow><mi>−</mi><mn>3</mn></mrow></msup></mrow></mfrac></mrow><annotation encoding="application/x-tex">1*10^{-3}*\frac{OC1max}{20*10^{-3}}</annotation></semantics></math>

is the input value coding for 1ms.

**Clarifying note regarding OCkmax**: OCkmax is relevant to the internal chip frequency (typically depending on quartz and PLL used). the dsPIC blockset evaluate this variable in the MATLAB workspace. Type \"who\" at matlab prompt to list all variable. Get the variable value typing its name \"OC1max\" (case sensitive). There are two OC blocks : The *OC hardware* block creates one variable OCmax. The *OC* block creates multiple variables OC(x)max with x, corresponding to each channel (1, 2 3 or 4)

# Dialog Box Parameters {#dialog_box_parameters}

## Timer

Select either Timer 2 or Timer 3. The selected timer will be reserved for the Output Compare Hardware block.

## Output Channels {#output_channels}

Specify Output Compare channel(s) (OC) used starting from 1. This modifies the number of input of the block. Specify multiple channels in vector form: \[1 2\] for OC1 and OC2.

## Channels Input Type {#channels_input_type}

Select for each channel which input you want to define:

- 5 : set UP duty cycle and Period
- 10 : set Down duty cycle and Period
- 16 : set rise and fall time instant within the period (useful when using ADC)

Note that the Period is common to all channels!

## Periode as block input {#periode_as_block_input}

Add Period input to the block. Otherwise, the period will be the max period set by Period Max.

## Period Max {#period_max}

Define max time in seconds of the longest value that could be generated by each channel. Event is either Up, Down, or Period max time for one channel. It should be set to the lowest value possible in order to get the highest resolution.

## ValMax / Channel Variable Name {#valmax_channel_variable_name}

This Variable evaluated in the workspace allows setting correct scaling for input data. The ValMax is the max value that corresponds to the duration defined in Max/Channels.

## Result Byte Resolution {#result_byte_resolution}

This is the log2 of the ValMax Variables for each channels. i.e. it is resolution of the channel. It is updated when you push the update diagram button (top right of the simulink menu).

## Timer {#timer_1}

This is the timer assigned to each channel. It is set automatically. The timer prescaler are defined in the Master block. It is updated when you push the update diagram button (top right of the simulink menu).

## Sample Time {#sample_time}

-1 mean inherited

## Status

Information if error encountered.

# Related block & Examples {#related_block_examples}

Related block:

- [ Output Compare](/wiki/dspic-block-output-compare/)

Examples:

- [Hyper_Sampling](/wiki/hyper-sampling/)
- forum : </forum/topic/242/>
- forum : </forum/topic/312/>

------------------------------------------------------------------------

\<comments \\\>
