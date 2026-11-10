---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:58Z"
title: "DsPIC Block/Tx Output"
url: "/wiki/dspic-block-tx-output/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UART_Tx_Output.png" alt="Block UART Tx Output">

<figcaption>

Block UART Tx Output

</figcaption>
</figure>

The Tx Output Output block send the uint8 **scalar** or **vector** data throw the UART Tx pin of the microcontroller. The \"UART Config\" is needed for configuration of the UART peripheral. This block act as a blocking function in the way that all its input will be placed in the UART Tx buffer. If the buffer is full, the function will wait for empty space until all data are placed inside the buffer. Thus, there is no data loss.

When not using interruption (not recommended), the UART internal buffer length is 4 bytes. When using interrupt, you set the Tx buffer size in the UART Config block.

To avoid real time violation (i.e. waiting for some place in the Tx buffer), you should send throught the UART less than the max number of characteres that can be send within ont time step ( this value is computed in the UART Configuration dialog box). Also, note that when sending a vector with more character than the Tx buffer size (ie, uint8 or int8 values), the block will wait until all character can find a place into the buffer. You can use several Tx blocks.

For sending multiple data at once, use a mux block to create the vector that will feed the Tx block.

Multiple instance of this block are allowed to receive several bytes within one time-step.

Related blocks : [Block/UART_Configuration](/wiki/dspic-block-uart-configuration/) [Block/Rx_Input](/wiki/dspic-block-rx-input/) [Block/Tx_Output](/wiki/dspic-block-tx-output/) [Block/Tx_Output_Multiplexed_For_Matlab-Labview](/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/) [Block/Interface_Tx-Matlab](/wiki/dspic-block-interface-tx-matlab/)

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UARTTx_DialogBox.png" alt="UART Tx Dialog" width="450">

<figcaption>

UART Tx Dialog

</figcaption>
</figure>

### n° UART {#n_uart}

UART Used

### Block Ordering Input / Output {#block_ordering_input_output}

Create one input and/or output port on simulink. This port is just used to set the order of execution between severals blocks.

## Forum related discussions {#forum_related_discussions}

- </forum/topic/143/>

(please complete this list)

------------------------------------------------------------------------

\<comments \\\>
