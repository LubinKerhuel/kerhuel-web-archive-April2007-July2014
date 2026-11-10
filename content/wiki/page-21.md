---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:57Z"
title: "DsPIC Block/Rx Input"
url: "/wiki/dspic-block-rx-input/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UART_Rx_Input.png" alt="Block UART Rx Input">

<figcaption>

Block UART Rx Input

</figcaption>
</figure>

The Rx block require the \'Uart Config block\' that will configure all parameters of the UART peripheral.

**When no interruption are used**, the Rx Input block can receive only one byte (uint8 scalar) at each step. If several bytes have been received during the previous time step, only the first one will be available in the current step execution time.

**When interruption are enabled**, the Rx Input block can receive as many data as there is some empty space in the buffer. When the buffer is full, last received data are lost. The block act as a FIFO stack. The block output in priority the first data logged. You can place as many Rx block as you want.

If no bytes have been received, the output is set to the default value. The block can be a blocking function : stop the step execution until one byte is received ( not recommended due to possible real-time constraint violation).

Related blocks : [Block/UART_Configuration](/wiki/dspic-block-uart-configuration/) [Block/Rx_Input](/wiki/dspic-block-rx-input/) [Block/Tx_Output](/wiki/dspic-block-tx-output/) [Block/Tx_Output_Multiplexed_For_Matlab-Labview](/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/) [Block/Interface_Tx-Matlab](/wiki/dspic-block-interface-tx-matlab/)

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UARTRx_DialogBox.png" alt="UART Rx Dialog" width="450">

<figcaption>

UART Rx Dialog

</figcaption>
</figure>

Multiple instance of this block are allowed to receive several bytes within one time-step.

### n° UART {#n_uart}

UART Used

### Sample Time {#sample_time}

-1 for inherited

### Blocking Function {#blocking_function}

if checked, the block will stop execution of others blocks until one byte is received

### Output Default {#output_default}

If no data has been received, the block will output the value defined here. The value must be within the range \[0 255\]. -1 mean that the last value received (by this block) is keept

### Received Output Flag {#received_output_flag}

If checked, one logical output appears. Its value is

- 1 if one byte has been received,
- 0 if no data has been received ; the output value is the \"Output Default\" value.

------------------------------------------------------------------------

\<comments \\\>
