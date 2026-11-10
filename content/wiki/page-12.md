---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Digital Output Read"
url: "/wiki/dspic-block-digital-output-read/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Digital_OutputRead.png" alt="Block Digital Output Read">

<figcaption>

Block Digital Output Read

</figcaption>
</figure>

The Digtal Output get the last value written to the microcontroller pin.

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_DigitalOutputRead_DialogBox.png" alt="Digital Output Read Dialog" width="450">

<figcaption>

Digital Output Read Dialog

</figcaption>
</figure>

## Port

- Port used

## Pin

- Pin used, start at 0 and is defined in vector form.

## Block Ordering Input / Output {#block_ordering_input_output}

Create one input and/or output port on simulink. This port is just used to set the order of execution between severals blocks. You want for example inside one time step set a pin to its high value and to its low value just after (create a glitch). You will used two blocks digital output, but they should be activated in a certain order. Connecting with the ordering Input/Output port the first block to the second one (temporaly speaking) will define the execution order.

------------------------------------------------------------------------

\<comments \\\>
