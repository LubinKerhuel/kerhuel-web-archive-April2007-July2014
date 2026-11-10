---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:55Z"
title: "DsPIC Block/C Function Call"
url: "/wiki/dspic-block-c-function-call/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_C_Function_Call.png" alt="Block C Function Call">

<figcaption>

Block C Function Call

</figcaption>
</figure>

Call user defined C function

The C Function Call block allows to include your custom C written functions (that could contain assembly language) into the schematic. It Interfaces your functions with the MathWorks Simulink diagram. The .c file containing the code of the function should be placed in the same directory as the .mdl file. If the c file is in another directory, it must be manually added in the \"Configuration Parameters \> Code Generation \> Custom Code \> include list of additional: Source files ; Include directories ; Libraries\...\"

# Dialog Box Parameters {#dialog_box_parameters}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_CFunctionCall_DialogBox.png" alt="C Function Call Dialog" width="450">

<figcaption>

C Function Call Dialog

</figcaption>
</figure>

## Function Name {#function_name}

Enter your C function name between single quotes \'zzz\'. Do not provide the prototype.

## Global input size {#global_input_size}

Specify if the variables of the inputs are scalar (1) or vector ( \>1 : array with one dimension). All different input data have the same size. they must all be either scalars nor vectors of equal dimension.

## Input 1 2 3 {#input_1_2_3}

Set the input type for the first three input. Set unused input as \-- (all to \-- if no input)

## Output Size {#output_size}

Size of the output variable. It can be either a scalar (1) ; neither a vector ( \>1 : array with one dimension)

## Output type {#output_type}

data type of the output data.

## Sample time {#sample_time}

-1 means inherited

## Function declaration {#function_declaration}

This is the declaration of your function in the generated Matlab/Simulink C files. Your C function declaration must be compatible with this prorotype.

## Function call {#function_call}

This is the call of your function in the Matlab/Simulink C files. Your function must comply with this call.

- **%y** represent blocks output
- **%u** represent blocks input

------------------------------------------------------------------------

\<comments \\\>
