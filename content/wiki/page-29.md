---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/I2C Master"
url: "/wiki/dspic-block-i2c-master/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_IC2_Master.png" alt="Block I2C Master">

<figcaption>

Block I2C Master

</figcaption>
</figure>

Input driver for I2C Peripheral

Provide acces to the I2C peripheral of the dsPIC (when available). The I2C bus sequence depends on the component being addressed. This sequence is configured very quickly with the \'sequence\' parameter. The number of input and the number of output of the block is modified in order to match the sequence specification.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_I2CMaster_DialogBox.png" alt="I2C Master Dialog" width="450">

<figcaption>

I2C Master Dialog

</figcaption>
</figure>

## Ref I2C {#ref_i2c}

use either I2C 1 or I2C 2 if the dsPIC has two distinct I2C peripheral

## Alternative I2C pin {#alternative_i2c_pin}

This option is display when the dsPIC has an alternative I2C pin option. All I2C blocks must have the same configuration. Either this option is checked in all of the I2C blocks, neither none of them are checked. Mixing both will result in chosing randomly one of the PIN configuration and may also provide unexpected behaviour.

## Sequence

Specify the I2C bus sequence. The sequence is enterred as text, between single quote \'xxx\'.

- **S** : generate a start condition on the bus
- **Sr** : generate a re-start condition on the bus
- **P** : generate a stop condition on the bus

<!-- -->

- **A** and **Axxx** : send the address of the component of the bus. If followed by a decimal number (like A104) this number is taken as the address. Otherwise, a block input appear noted A1

<!-- -->

- **W** and **Wxxx** : write a data of type uint8 on the bus. If followed by a decimal number (like W82) this number is taken as the data being written. Otherwise, a block input noted W1 appears.

<!-- -->

- **R** and **Rnack** : Read a data of type uint8 on the bus. R generate an acknowledge. Rnack do not generate the acknowledge. A block output noted R1, R2 \... Rn appears for each R or Rnack present in the sequence.

Example of sequence : \' **S A125 W R R P** \'

## Initialisation

Define when the I2C peripheral is configured :

- When PIC is initialized (only once)
- When I2C bus is enable (if Enable I2C is checked)
- Both
- None

For simple schematic, use the first item.

## Enable I2C peripheral before use {#enable_i2c_peripheral_before_use}

Enable or Re-enable the I2C peripheral. for simple model, the I2C bus is never disabled, this option can be unchecked.

## Wait after enable {#wait_after_enable}

Place a number or No OPerating (nop) instruction after re-enabling the I2C BUS. This is to avoid problems du to fast transition.

## Disable I2C peripheral after use {#disable_i2c_peripheral_after_use}

to disable the I2C peripheral after use.

## I2C bus frequency {#i2c_bus_frequency}

Configure the I2C bus frequency. The I2C bus frequency Fscl is updated in the info part of the dialog each time this parameter is modified.

## Slew rate active {#slew_rate_active}

Activate Slew rate

## Enable SMB bus threshold {#enable_smb_bus_threshold}

Enable SMB bus threshold

## Output Error flag {#output_error_flag}

Add an output to the block. This output will output 0 if no error occurs. 1 otherwise.

## Sample Time {#sample_time}

Sample time of the block. -1 for inherited

## Block Ordering Input / Output {#block_ordering_input_output}

If you want to force the execution order of blocks that are not connected, this option allow to add either an input, an output or both to the block. These virtual connection allow to force the ordering of the blocks.

## Info

Information, give the clock frequency Fscl of the I2C bus.

------------------------------------------------------------------------

\<comments \\\>
