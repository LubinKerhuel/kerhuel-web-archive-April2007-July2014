---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Input Capture"
url: "/wiki/dspic-block-input-capture/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Input_Capture.png" alt="Block Input Capture">

<figcaption>

Block Input Capture

</figcaption>
</figure>

The Input Capture (IC) block provides measurements from any kind of PWM data. Uptime, downtime, or both value can be captured. For each channel captured a timer is automatically chosen and set to obtain the maximum resolution. Timer configuration is based on the max pulse duration you are to measure.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_InputCapture_DialogBox.png" alt="Input Capture Dialog" width="450">

<figcaption>

Input Capture Dialog

</figcaption>
</figure>

## Interrupt Priority {#interrupt_priority}

The interrupt is triggered on the rising and/or falling edge. The measurement is then calculated and saved. The interrupt priority will not affect the accuracy of the measure because timers are read in hardware. Interrupt priority can affect measurements on fast consecutive events, however.

## Input Channels {#input_channels}

Specify Input Capture channel(s) (IC), they are numbered starting from 1. Multiple channels can be specified as a vector. This will affect the number of outputs for the block.

## Channels Input Type {#channels_input_type}

Select for each channel which kind of data you want to extract.

- 1 : is to get the High pulse duration
- 2 : is to get the Low pulse duration
- 3 : is to get both High and Low pulse duration
- 4 : is to get the period using rising edge
- 8 : is to get the period using falling edge
- 5 : is to get both High pulse duration and period using rising edge
- 10 : is to get both Low pulse duration and period using falling edge

The value of the vector referring to corresponding channel defined in \"Input Channels\".

## Max/Channels

Define the max time in seconds of the largest event to be measured by the respective channel.

## Safety margin in % {#safety_margin_in}

Add a margin to the max time defined previously. This margin time allow to avoid provided the event is larger than the max attempted value.

## ValMax / Channel Variable Name {#valmax_channel_variable_name}

This Variable will be evaluated in the workspace and allow you to scale the data.The ValMax is the max value that will be given by an event of the duration defined in Max/Channels. This value does not take into account the Safety margin.

## Result Byte Resolution {#result_byte_resolution}

This is the log2 of the ValMax Variables for each channels.

## Timer

This is the timer that is used with the corresponding channel and is set automatically. The timer prescalers are defined in the Master block.

## Changed Detected on {#changed_detected_on}

Adds boolean outputs to the block. This output takes the value 1 if a change has occurred since the last block execution. The output can be set to 1 either at rising edge, falling edge or both.

## Sample Time {#sample_time}

-1 mean inherited

## Status

Information if error encountered.

------------------------------------------------------------------------

\<comments \\\>
