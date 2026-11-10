---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:58Z"
title: "DsPIC Block/Software Reset"
url: "/wiki/dspic-block-software-reset/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Software_Reset.png" alt="Block Software Reset">

<figcaption>

Block Software Reset

</figcaption>
</figure>

Software RESET

The \"dsPIC Reset\" block Reset the microcontroller when its input is different from 0. The effect of the reset is the same switch off then on the alimentation. This can be usefull when using a bootloader (I considere the Tiny Boot loader TinyBld written by Claudio Chiculita). You can reset the microcontroller when receiving one specific data on the UART for example.

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Reset_DialogBox.png" alt="Reset Dialog" width="450">

<figcaption>

Reset Dialog

</figcaption>
</figure>

------------------------------------------------------------------------

\<comments \\\>
