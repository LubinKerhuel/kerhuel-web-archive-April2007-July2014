---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:54Z"
title: "DsPIC Block/ADC Analog to Digital Converter"
url: "/wiki/dspic-block-adc-analog-to-digital-converter/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_ADC.png" alt="Block Analog to Digital Converter">

<figcaption>

Block Analog to Digital Converter

</figcaption>
</figure>

Input driver for Analog-to-Digital Converter peripheral

The ADC Input block convert an analog signal from the PIC input channel selected. For each channel you can, at each time step, either read one sample (get a scalar result) or several samples equaly time spreaded separated (with a period time inferior to the block time step). Thus, you get a vector result within one step time. Result format is specified as signed/unsigned and fractional/integer. The input pin \"voltage reference\" can be selected as voltage reference. 10 or 12 bits choice for conversion is available for dsPIC 33f family. On dsPIC 30f, PIC 24F and PIC 24H family, the bit resolution is fixed and device dependant.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_ADC_DialogBox.png" alt="Analog to Digital Converter Dialog" width="450">

<figcaption>

Analog to Digital Converter Dialog

</figcaption>
</figure>

## Type

10 or 12 bits resolution depending on the microcontroller used (set in the Master block). The two choices are available for the dsPIC 33f family.

## Mode

- Continuous Sampling and get last channel value : In this mode, all selected channel are continuously scanned and converted at high speed. When the simulink block outputs are read, the last value converted from each channel is used. This method provide the minimum time lag between the end of conversions and the calculations using theses values.
- Continuous Sampling get output vector : In this mode, all channel selected are scanned and converted at low speed allowing to get exactly the number of sample defined in 1 time step. For example, you can get 6 samples from both channels AN0 and AN1. The samples of AN0 (resp AN1) will have a fixed sample rate. To avoid missalignment between end of time step and sampling rate, considere using ADC as timer refference in the master block. In this case, the time step is triggered by the end of the ADC conversions.

## Number of output samples for each channel at each step {#number_of_output_samples_for_each_channel_at_each_step}

Only available if Mode is set to \"Continuous Sampling get output vector\". Set the number of sample desired for each output. All outputs have the same number of sample.

## Voltage Reference {#voltage_reference}

Select the Conversion voltage reference. It can be the microcontroller alimentation, or external voltage reference when using external PIN reference.

## Output Format {#output_format}

Select the output. Choice are integer or fractional (right or left justification) and signed/unsigned.

## Interrupt Priority {#interrupt_priority}

Used when mode is set to \"Continuous Sampling get output vector\".

## AN Channel to convert {#an_channel_to_convert}

Choose AN input pins (enter the vector with channel number to convert). This will also set the number of output of the block. Starting at 0 for AN0. For example, \[0 1\] will convert channels AN0 and AN1 and block will have two outputs.

## Max Value ANmax {#max_value_anmax}

Simulink set the **ANmax** variable equal to the max value for the AN converter. For 10 bits, it is **1024** and for 12 bits it is **4096**. This **ANmax** variable is evaluated in the matlab workspace. It allows to normalise the output of the ADC and to keep calculation correct while changing from 10 bits to 12 bits mode.

## External Input Resistor {#external_input_resistor}

Define the value (in ohm) of the input resistor. The bigger, the slower is the charge of the capacity and the slower is the conversion time.

## Temperature °C {#temperature_c}

Define the ambiant temperature. The higher, the slower the conversion time is. (see Microchip Refference manual)

## Sample Time {#sample_time}

-1 mean inherited (Define the time step of this block, -1 or a multiple of the diagram time step)

## Info

Provides the following informations :

- Tsmp : Time to sample 1 channel
- T/Channel : Time of sample and convert 1 channel
- Tall : Conversion time for all samples

## Trigger Source {#trigger_source}

Should be auto convert for most case. When another mode is selected, the mode should be Continous Sampling & get last channel value. Thus, the conversion will only occurs when the selected event occurs. If no event occurs between two simulink time step, the previoius value remains.

- auto convert (default)
- Motor Control PWM
- Timer3 (OC_HW PWM)
- Low to High transition on INT0 pin

------------------------------------------------------------------------

\<comments \\\>
