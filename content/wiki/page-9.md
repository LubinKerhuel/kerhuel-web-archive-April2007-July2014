---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Compiler Configuration"
url: "/wiki/dspic-block-compiler-configuration/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_Compiler_Configuration.png" alt="Block Compiler Configuration">

<figcaption>

Block Compiler Configuration

</figcaption>
</figure>

Set compilers options

# Dialog Box Parameters {#dialog_box_parameters}

## Double in 64 bits if checked, default is 32 {#double_in_64_bits_if_checked_default_is_32}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CompilerConfiguration_DialogBox.png" alt="Configuration Dialog" width="450">

<figcaption>

Configuration Dialog

</figcaption>
</figure>

Simulink simulation use 64 bits double for double data type. The C30 compiler default size for double is 32 bits (equivalent to simulink single variable). This option force the dsPIC/PIC24 C30 Compiler size for double diagram data type to 64 bits doubles. 64 bits double gives more precise results at the cost of a slower computation time and a larger code size. You should considere using fixed point calculation that will speed up the calculation and reduced the code size ! The fixed point toolbox is perfect to optimized the scaling of your fixed point variables.

------------------------------------------------------------------------
