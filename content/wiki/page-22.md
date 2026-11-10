---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:58Z"
title: "DsPIC Block/Tx Output Multiplexed For Matlab-Labview"
url: "/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UART_Tx_Output_Multiplexed_MatlabLabview.png" alt="Block UART Tx Output Multiplexed Matalb-Labview">

<figcaption>

Block UART Tx Output Multiplexed Matalb-Labview

</figcaption>
</figure>

Output driver to send internal variables to a matlab or labview graphical interface. Variables can be visualized and recorded from Matlab or Labview.

The \"Tx Output Multiplexed for Matlab-Labview\" Output block write up to 16 different variable of eigher 8 or 16 bits to matlab/labview using a specific developed serial protocol. The block \"Interface Tx-Matlab\" open the graphical user interface allowing to received the data from the microcontroller using the serial port of the computer. Using USB to serial hardware adaptater should be considered if your computer has no serial interface. Need one \"UART config\" block to set UART parameters.

Related blocks : [Block/UART_Configuration](/wiki/dspic-block-uart-configuration/) [Block/Rx_Input](/wiki/dspic-block-rx-input/) [Block/Tx_Output](/wiki/dspic-block-tx-output/) [Block/Tx_Output_Multiplexed_For_Matlab-Labview](/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/) [Block/Interface_Tx-Matlab](/wiki/dspic-block-interface-tx-matlab/)

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UARTMultiplexed_DialogBox.png" alt="UART Multiplexed For Matlab Labview Dialog" width="450">

<figcaption>

UART Multiplexed For Matlab Labview Dialog

</figcaption>
</figure>

## n° UART {#n_uart}

Select the microcontroller UART Used

## Intelligent Spreading {#intelligent_spreading}

If you send more data than the maximum data that can be send during one time step, this option allow to send each channel. All data will not be send, but each channel will be send. If not checked, the data of the last channel will never been send.

## Channel Number {#channel_number}

Select from 0 to 15 in a vector. If several channel are selected, the blocks will have several inputs.

## Tx Buffer Size {#tx_buffer_size}

Size of the buffer. Should be just bigger than the total amount data send. 8 bits channel need 2 bytes and 16 bits channels need 3 bytes.

## Blocking channel {#blocking_channel}

Specify channel that should not loose data. Be carefull to not violate the time step calculation time by setting all channel as blocking channel.

## Labview

[Media:PIC_Labview.rar](/images/PIC_Labview.rar) for viewing data using Labview (Last time edited was 2005. hope you could convert theses files).

## Related forum topics {#related_forum_topics}

- [GUI in Matlab2010a with virtual Com port problem](/forum/topic/295/#p1170)
- [Data Logging to LabVIEW (protocol description)](/forum/topic/98/#p320)

------------------------------------------------------------------------

\<comments \\\>
