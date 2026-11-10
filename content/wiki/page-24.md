---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:57Z"
title: "DsPIC Block/SPI Configuration"
url: "/wiki/dspic-block-spi-configuration/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_SPI_Configuration.png" alt="Block SPI Configuration">

<figcaption>

Block SPI Configuration

</figcaption>
</figure>

The configuration block set the SPI parameters.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_SPIConfig_DialogBox.png" alt="SPI Configuration Dialog" width="450">

<figcaption>

SPI Configuration Dialog

</figcaption>
</figure>

## n° SPI {#n_spi}

SPI used

## Mode

Master or Slave : define who is driving the clock signal

## Prescaler

Choose the speed of the transmission. The resulting speed is showed in Status

## SDO Enable {#sdo_enable}

Send data from the microcontroller. If checked, a input entry will appear on the block to connect data to be send.

## Data length {#data_length}

Select between 8 or 16 bits. It is the same length for input or output of the block.

## Slave Select Pin Enable {#slave_select_pin_enable}

When checked, The bus will be activated only rise time of Slave Select Pin. The output will be high impedence during fall time of Slave Select Pin.

## Sample phase {#sample_phase}

Choose the place where the sampling take place when reading data (middle or end of bit)

## Clock Active State {#clock_active_state}

Choose the active state of the clock

## Output change on transition {#output_change_on_transition}

Choose where update take place when writng data.

## Status

Provides information like bit rate and status

------------------------------------------------------------------------

\<comments \\\>
