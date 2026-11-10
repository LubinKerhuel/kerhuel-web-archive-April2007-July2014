---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Digital Input"
url: "/wiki/dspic-block-digital-input/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Digital_Input.png" alt="Block Digital Input">

<figcaption>

Block Digital Input

</figcaption>
</figure>

The Digtal Input block reads the logical value of the selected microcontroller pin.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_DigitalInput_DialogBox.png" alt="Digital Input Dialog" width="450">

<figcaption>

Digital Input Dialog

</figcaption>
</figure>

## Port

- Port used

## Pin

- Pin used, start at 0 and is defined in vector form allowing several Pin to be read at the same time.

## Sample Time {#sample_time}

- -1 is inherited

## Block Ordering Input / Output {#block_ordering_input_output}

Create one input and/or output port on simulink. This port is virtual and do not add code in the microcontroller. It is used to force the execution order between two dsPIC/PIC24 peripheral blocks. (see examples)

------------------------------------------------------------------------

\<comments \\\>
