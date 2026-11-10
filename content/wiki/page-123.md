---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-03-04T09:34:37Z"
title: "Importing Simulink Generated Code into Mplab"
url: "/wiki/importing-simulink-generated-code-into-mplab/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/CompilingSimulinkCodeWithMPLAB.png" alt="MPLAB project with imported C files and library files (.a) previously generated with simulink" width="350">

<figcaption>

MPLAB project with imported C files and library files (.a) previously generated with simulink

</figcaption>
</figure>

This example explain how to import simulink generated C files (using Real Time Workshop Embedded Coder and the dsPIC blockset) into a MPLAB project. This method should not be used in normal operation because the Blockset compile the generated files so as to obtain the binary file (.hex and .elf). However, compiling the C files within MPLAB allows to debug the software using the MPLAB deugging capabilities.

For this demonstration, I use the simulink model described in the example for Explorer 16 Development Board (with the dsPIC 33FJ256GP710 or PIC 24JF128GA010 microcontroller).

The model file is in the toolbox directory : **examples\\dsPIC_33f_Explorer16.mdl**

This method do not use the MPLAB function to import C code from simulink that may be difficult to use.

## Step 1 : Simulink {#step_1_simulink}

- Compile the model

The model must be compiled in simulink (the dsPIC blockset must be installed) to get the matlab lirarys compiled so as to import them easily in MPLAB.

Real Time Workshop creates the subdirectory **dsPIC_33f_Explorer16_dspic\\Source**. It contains the .C and .h source files generated.

## Step 2 : MPLAB {#step_2_mplab}

from Version 3.3 of the blockset, a MPLAB project file is created. Thus, you just have to compile once the project in MATLAB and then open the created MPLAB project. The following steps are no more required !

1.  **Create a new project**
2.  **Select the target device** (The same as defined in the simulink model : 33fJ256GP710)
3.  **Select Language Toolsuite** : Use the C30 Compiler ( free student version available on the microchip website)
4.  **Import C sources files** (from \*Toolbox\* \\ examples \\ dsPIC_33f_Explorer16_dspic \\ Source )
5.  **Import h source files** (from \*Toolbox\* \\ examples \\ dsPIC_33f_Explorer16_dspic \\ Source )
6.  **Import Matlab library and PIC/dsPIC library** : (all .a files in the *\*Toolbox\*\\examples\\dsPIC_33f_Explorer16_dspic\\Source* directory ; The .a library corresponding to the PIC in the Microchip directory *C:\\Program Files\\Microchip\\MPLAB C30\\lib* for 24f pic, use the 24Fxxx file ( I use the coff version)
7.  **Import Linker script file** for the chosen PIC/dsPIC ; from the microchip directory : C:\\Program Files\\Microchip\\MPLAB C30\\support\\gld
8.  **Compile**

## Remarks

Illustrations were realized with MPLAB 7.52.

### Know bug {#know_bug}

with MPLAB 7.60 and get the following message during the compilation process:

\"*A language-plugin exception occurred and was logged*\"

It seems to be an MPLAB error. Refere post about this error on the microchip forum. My advice would be to use MPLAB 7.52.

### Why you should avoid to use MPLAB {#why_you_should_avoid_to_use_mplab}

I would not recommend to import C code files generated with simulink into MPLAB for the following reasons :

- I is easier to maintain and improve code using simulink
- Adding personnal C code can be easily done in simulink using the dsPIC block \"call C function\"
- There should be no low level bug
- High level debugging is easier in real-time, using MPLAB debugger usually add strange behaviour and make the debugging very hard.

MPLAB should only be used if the generated C code contains bug, or to debug peripheral ( If you find bugs in peripheral C code, please let me know)

[Category:Example](/wiki/category/example/)
