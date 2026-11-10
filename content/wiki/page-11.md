---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Digital Output Write"
url: "/wiki/dspic-block-digital-output-write/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Digital_OutputWrite.png" alt="Block Digital Output Write">

<figcaption>

Block Digital Output Write

</figcaption>
</figure>

The \"Digtal Output write\" block write the logical value to the microcontroller pin.

# Dialog Box {#dialog_box}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_DigitalOutputWrite_DialogBox.png" alt="Digital Output WriteDialog" width="450">

<figcaption>

Digital Output WriteDialog

</figcaption>
</figure>

## Port

- Port used

## Pin

- Pin used, start at 0 and is defined in vector form.

## Block Ordering Input / Output {#block_ordering_input_output}

Create one input and/or output port on simulink. This port is just used to set the order of execution between severals blocks. You want for example inside one time step set a pin to its high value and to its low value just after (create a glitch). You will used two blocks digital output, but they should be activated in a certain order. Connecting with the ordering Input/Output port the first block to the second one (temporaly speaking) will define the execution order.

See forum related question: </forum/topic/367/#p1500> Please feel free to complete this page !

------------------------------------------------------------------------

\<comments \\\>
