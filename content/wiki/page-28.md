---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:55Z"
title: "DsPIC Block/CAN Receive"
url: "/wiki/dspic-block-can-receive/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CAN_Receive.png" alt="Block CAN Receive">

<figcaption>

Block CAN Receive

</figcaption>
</figure>

Read data from a CAN bus

The CAN Receive block with selected Identifier. The CAN message contain between 1 and 8 bytes. The five filters defined which message Identifier will be keept. Messages with Identifier not contained into one of the five filter are not catch. Two buffer allow to receive up to two different messages between the execution of two CAN Receive block (usually, from one time step to the other). The block works as a FIFO. Message with matching identifier comming while the buffer is already full are lost.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CANReceive_TabGeneral_DialogBox.png" alt="CAN Receive Dialog" width="450">

<figcaption>

CAN Receive Dialog

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CANReceive_TabRx0_DialogBox.png" alt="CAN Receive Dialog" width="450">

<figcaption>

CAN Receive Dialog

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CANReceive_TabRx1_DialogBox.png" alt="CAN Receive Dialog" width="450">

<figcaption>

CAN Receive Dialog

</figcaption>
</figure>

## Num CAN {#num_can}

Ref to the CAN peripheral being configured (some PIC have two CAN bus)

## Filter 0 and 1 Acceptance Mask / Filter 2, 3 and 4 Acceptance Mask {#filter_0_and_1_acceptance_mask_filter_2_3_and_4_acceptance_mask}

The two acceptance filter acts respectivly on Filter 0-1 and Filter 2-3-4. A bit set to 0 in the acceptance Filter will be ignored by the respective fitlers.

## Message x Data Length {#message_x_data_length}

For each filter (from 0 to 4) Message Data Length define the length of the message to be received by this filter. A message can contain up to eight bytes. If the Message Data Length is set to a lower value than the message being received, only the first bytes of the message will be taken into account. Iif the Message Data Length is set to a higher value than the message being received, the last bytes content of the message taken into account will be undefined (contains old values). If the Message Data Lengt is set to a value higher than 1, the block output with the same length as the Message Data Length. A simulink Demux block should be used to get each byte of the message. If the Message Data Length is set to Off, the Filter is not used. No message will be received.

## Acceptance Filter x {#acceptance_filter_x}

For each of the 5 filters, the acceptance filter allow to retain only the the CAN message with an identifier that match the Acceptance Filter. The Acceptance Filter is bitewise compare to the CAN message Identifier, except for the bytes where the Filter Acceptance Mask is set to 0.

## Acceptance Filter type {#acceptance_filter_type}

- Standard or Extended
- Standard 11 bits
- Extended 29 bits

## Output received Data Length {#output_received_data_length}

If checked, a block output with the Real Data Length of the message received appears. This Data Length is read from the CAN bus. It is independant from the Message x Data Length parameter.

## Output Flag New Message {#output_flag_new_message}

If checked, a block output with a logic flag set to 1 each time a new message arrived.

## Output Identifier {#output_identifier}

If checked, a block output with the Message Identifier received.

## Output Flag Data Request To send {#output_flag_data_request_to_send}

If checked, a block output with the Data Request To Send Flag appears.

## Receive Error Counter {#receive_error_counter}

The Receive Error Counter output the internal CAN Receive Error Counter. See CAN doccumentation for precision about Error Counter.

## Output Flag Data Lost {#output_flag_data_lost}

If checked, a block output with a flag appears. This flag is set to 1 when a message with a matching Identifier appears on the CAN bus, but cannot be stored because the buffer is already full.

## Sample Time {#sample_time}

Sample time of the block. -1 for inherited

## Block Ordering Input / Output {#block_ordering_input_output}

If you want to force the execution order of blocks that are not connected, this option allow to add either an input, an output or both to the block. These virtual connection allow to force the ordering of the blocks.

## Info

Information

------------------------------------------------------------------------

\<comments \\\>
