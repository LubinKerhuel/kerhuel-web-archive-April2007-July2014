---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2010-09-29T12:32:59Z"
title: "Flex Board Blinking Led"
url: "/wiki/flex-board-blinking-led/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/FlexBoard_Photo.jpg" alt="Flex Board equiped with a dsPIC33Fj256MC710, from Evidence Srl" width="250">

<figcaption>

Flex Board equiped with a dsPIC33Fj256MC710, from Evidence Srl

</figcaption>
</figure>

This example shows how to configure the Flex board for programming using Simulink. It also shows how to send data from the PC to the \"onboard Simulink model\".

The flex board is a product from the [Evidence Srl](http://www.evidence.eu.com/). It is equipped with a dsPIC 33FJ256MC710. The pin out of the dsPIC is accessible through easy to use connections (HE14 connectors). The overall board is powered with a simple 12V PC alim. Onboard regulator generates the appropriate tension to power up the microcontroller. The board is equipped with a 4Mhz Quartz.

Download the Simulink model: [FlexBoard_Blinking_Led.mdl](/images/FlexBoard_Blinking_Led.mdl)

# Model Configuration {#model_configuration}

<figure class="wiki-figure">

<img loading="lazy" src="/images/FlexBoard_Model_BlinkingLed.png" alt="download the model" width="400">

<figcaption>

download the model

</figcaption>
</figure>

)\]\]

The master block is set up for the dsPIC 33FJ256MC710 with a quartz at 4Mhz.

UART is configured with its maximum speed (for the PC) i.e. 115200 bauds. This UART speed cannot be achieved without enabling the dsPIC clock multiplier PLL. Without PLL, the microcontroller run at 2MIPS and the UART speed error (read from the UART configuration block) is of 8.5%. Therefore, PLL is activated. The targeted speed must be compatible with the UART baud used. With a configuration of 9.2MIPS, UART has a speed error of -0.17% (The real baud is 115000 ; error is : <math display="inline"><semantics><mrow><mfrac><mrow><mn>115000</mn><mo>−</mo><mn>115200</mn></mrow><mn>115200</mn></mfrac><mo>=</mo><mi>−</mi><mn>0.0017</mn></mrow><annotation encoding="application/x-tex">\frac{115000 - 115200}{115200} = -0.0017</annotation></semantics></math>)

The orange Led of the Flex board is connected to the PIN B14. Therefore, a digital output is set up on B14. Its input is a limited counter with its higher limit set to 1. The counter sampling rate is set to 0.25s (blue colored part of the model). The binary signal generated has therefore a period of 0.5Hz thus the Led blink at 0.5Hz.

# Send data from the PC to the dsPIC {#send_data_from_the_pc_to_the_dspic}

<figure class="wiki-figure">

<img loading="lazy" src="/images/FlexBoard_rs232gui_BlinkingLed.png" alt="Matlab Graphical User Interface to send and log data to and from the Flex Board" width="400">

<figcaption>

Matlab Graphical User Interface to send and log data to and from the Flex Board

</figcaption>
</figure>

The protocol created allows modifying some variables declared at the simulink model while the model is running in the dsPIC. The variable are declared as uint8 with the block **data store memory** from the standard simulink library. The variables names are Variable60, Variable61 and Variable62.

Changing the value of a variable in the running dsPIC program needs to send two data bytes through the UART. The first byte is the variable reference to be change (it can be 60, 61 or 62). The second byte is the new value of the variable. Thus, the vector \[60 50\] is set up in the Matlab user interface (rs232gui). Values are sent when the send1 or send2 button is pressed.

<figure class="wiki-figure">

<img loading="lazy" src="/images/FlexBoard_ResultSinus.png" alt="Sinus with variable amplitude logged from the Flex Board throught UART" width="500">

<figcaption>

Sinus with variable amplitude logged from the Flex Board throught UART

</figcaption>
</figure>

On this model (see the model):

- the variable 60 set the amplitude of the sinus generated.
- the variable 61 define which data is send to the PC :
  - if 0, the Time Step is being sent
  - if 1, the Sinus is being sent.
- the variable 62 is directly sent to the PC

We can see on the figure that the amplitude of the sinus changes as we click on the button send1 or send2 on the matlab user interface.

<figure class="wiki-figure">

<img loading="lazy" src="/images/FlexBoard_ResultTimeStep.png" alt="Time Step. From the Master block, the 2ms time step correspond to a value of 18399. Real time constraints are respected." width="500">

<figcaption>

Time Step. From the Master block, the 2ms time step correspond to a value of 18399. Real time constraints are respected.

</figcaption>
</figure>

The max time step recorded for this model is about 4500. With the same scale, the model time step configuration corresponds to 18399. Thus, the dsPIC is used at 25%

<math display="inline"><semantics><mrow><mfrac><mn>4500</mn><mn>18399</mn></mfrac><mo>=</mo><mn>0.25</mn></mrow><annotation encoding="application/x-tex">\frac{4500}{18399} = 0.25</annotation></semantics></math>

It is quite time consuming but this model could be optimized. Generation of the sinus should be done using a look up table (from the simulink standard library) and all calculation should be done using only fixed step variable (no double !)

------------------------------------------------------------------------

Thanks to Evidence for providing this Flex Board Light.

[Category:Example](/wiki/category/example/)
