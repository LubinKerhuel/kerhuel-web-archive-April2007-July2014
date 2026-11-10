---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:57Z"
title: "DsPIC Block/SPI Input Output"
url: "/wiki/dspic-block-spi-input-output/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_SPI_Input_Output.png" alt="Block SPI Input/Output">

<figcaption>

Block SPI Input/Output

</figcaption>
</figure>

Input-Output Driver for SPI module

The SPI Input-Output block can be configured as an input for SPI data, as an SPI output, or as both Input-Output. The SPI pin can be disabled after reading or sending data allowing the pin tu be used as a digital output (usefull if weird protocole is used)

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_SPIInputOutput_DialogBox.png" alt="SPI Input Output Dialog" width="450">

<figcaption>

SPI Input Output Dialog

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/SPI_Example_NoInterrupt.png" alt="Example of SPI block reading data from an rate-gyro (ADIS16100). Chip Select of the rate gyro is connected to the B4 dsPIC pin which is activated just before execution of the SPI block. Note the Ordering connection to force block ordering." width="450">

<figcaption>

Example of SPI block reading data from an rate-gyro (ADIS16100). Chip Select of the rate gyro is connected to the B4 dsPIC pin which is activated just before execution of the SPI block. Note the Ordering connection to force block ordering.

</figcaption>
</figure>

## n° SPI {#n_spi}

SPI used

## SPI Input {#spi_input}

If checked, SPI data will be read This add one output to the Simulink block.

## Wait for previous operation to finish, and Reset before Read {#wait_for_previous_operation_to_finish_and_reset_before_read}

Wait for previous operation to finish, and Reset before Read

## SPI Output {#spi_output}

When checked, SPI data will be written to the SPI pin. This add one input to the Simulink block.

## Special SPI {#special_spi}

Allow to disable SPI pin function and to use theses pin as digital input/output. The choices are :

- Always Enable
- Disable After block execution
- Re-Enable before block execution
- Re-Enable Execute and disable

## Data Length {#data_length}

8 or 16 bits. This option is set in SPI Configuration block

## Wait for incomming data (slave mode) {#wait_for_incomming_data_slave_mode}

Stop execution of other blocks while no data are received

## Block Ordering Input / Output {#block_ordering_input_output}

Create one input and/or output port on simulink. This port is just used to set the order of execution between severals blocks. You want for example inside one time step set a pin to its high value and to its low value just after (create a glitch). You will used two blocks digital output, but they should be activated in a certain order. Connecting the first block to the second one (temporaly speaking) will allow to respect the execution order you desire.

## Status

Provides information like bit rate and status

------------------------------------------------------------------------

\<comments \\\>
