---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/External Interrupt PWM"
url: "/wiki/dspic-block-external-interrupt-pwm/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_External_Interrupt_PWM.png" alt="Block External Interrupt PWM">

<figcaption>

Block External Interrupt PWM

</figcaption>
</figure>

The External Interrupt block allow to detect and/or measure Time Pulse (like PWM) on EI ports of dsPIC. This block define function of one EI port only. Use many blocks to use many EI..

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_ExternalInterrupt_DialogBox.png" alt="External Interrupt Dialog" width="450">

<figcaption>

External Interrupt Dialog

</figcaption>
</figure>

## Port

Specify the External Interrupt PIN used.

## ext Interrupt Priority {#ext_interrupt_priority}

Select the priority for the interrupt since each modification start interrupt execution code..

## Capture PWM {#capture_pwm}

Speicfy what you want to measure.

## Max capture Time {#max_capture_time}

Define max time in secondes of the largest event to be measure by the respective channel.

## Safety Margin in % {#safety_margin_in}

Add a margin to the max time defined previously. This margin time allow to avoid provided the event is larger than the max attempted value.

## ValMax / Channel Variable Name {#valmax_channel_variable_name}

This Variable will be evaluated in the workspace and allow you to scale the data.The ValMax is the max value that will be given by an event of the duration defined in Max/Channels. This value does not take into account the Safety margin.

## Result Byte Resolution {#result_byte_resolution}

This is the log2 of the ValMax Variables for each channels.

## Timer

This is the timer that is used with the corresponding channel. It is set automatically. The timer prescaler are defined in the Master block.

## Change Detected on {#change_detected_on}

Add outputs to the block. For each channel, you can know if a changed has appears. The output is set to 1 either on rising edge, falling edge or both.

## Block Ordering Input/Output {#block_ordering_inputoutput}

Add the Ordering port on Simulink block.This does not affect code generated excepted for the block execution order.

## Sample Time {#sample_time}

-1 mean inherited

------------------------------------------------------------------------

\<comments \\\>
