---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-02-17T23:31:08Z"
title: "CAN communication between two dsPIC"
url: "/wiki/can-communication-between-two-dspic/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Circuit_CAN.png" alt="Components schematic and electronics picture of two dsPIC 30f4012 exchanging data’s through a CAN bus (CANH and CANL). The MCP2551 is a CAN bus driver which translate dsPIC’s CAN peripheral output into CAN bus level. These two drivers are absolutely required. The MCP2551 represented upside on the top schematic is rotated of 180° in the electronics picture. The electronic picture is composed of two dsPIC 30f4012 connected to their respective MCP2551 driver. The CAN bus wire is here made of the two short green wires on the left side. The electronic schematic is symmetric (no master, no slave…)" width="350">

<figcaption>

Components schematic and electronics picture of two dsPIC 30f4012 exchanging data's through a CAN bus (CANH and CANL). The MCP2551 is a CAN bus driver which translate dsPIC's CAN peripheral output into CAN bus level. These two drivers are absolutely required. The MCP2551 represented upside on the top schematic is rotated of 180° in the electronics picture. The electronic picture is composed of two dsPIC 30f4012 connected to their respective MCP2551 driver. The CAN bus wire is here made of the two short green wires on the left side. The electronic schematic is symmetric (no master, no slave...)

</figcaption>
</figure>

# Description

This example shows two dsPIC 30f4012 exchanging data through a bus CAN. The dsPIC embedded program is generated through Simulink and Realtime-Workshop Embedded Coder and the [dsPIC blockset](/wiki/download/#download). The CAN bus is symmetrical consequently there is no master and no slave. Every 2ms, each dsPIC place one data (frame) on the bus to be read by the other dsPIC. The internal dsPIC CAN peripheral arbitrate bus access to avoid conflict (only one peripheral can write to the bus at one time). Both dsPIC places the received data from the CAN bus to its UART. The dsPIC UART is connected to the PC and the Matlab graphical interface [rs232gui](/wiki/dspic-block-interface-tx-matlab/) allows to plot theses data in real time.

# Characteristics of a CAN bus {#characteristics_of_a_can_bus}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Scope_HM205_CAN_01.jpg" alt="Photo (1) of a scope showing absolute voltage of the CANH and CANL wires. 6 CAN composed of recessive (CANH != CANL) and dominant (CANH=CANL) states . The three yellow highlighted belong to the dsPIC (A) and the three blue highlighted belong to the dsPIC (B). The dsPIC (A) frame (yellow) contains 3 data bytes while the dsPIC (B) frame (blue) contains only 2 data bytes (Blue highlighted frames are shorten than the yellow one). Each dsPIC feed its CAN peripheral with the 3 or 2 byte composing the frame at a frequency of 500Hz. A 2 ms time delay separates two consecutive frame created by one dsPIC (resp yellow one or blue one). However, time delay (Delta BA) separating a frame B=&gt;A from a frame A=&gt;B increase (or decrease) slowly because of the slight frequency difference between the two 8Mhz quartz clocking both dsPIC (frequency error). When both frame are close to each other, the CAN peripheral manage automatically bus arbitration to avoid conflict. Consequently, the first dsPIC writing a dominant state (byte) on the bus gets the priority. Consequently, the two frames keep close until switching their respective place and continuing to evaluate in time relatively to each other (see photo (2))." width="350">

<figcaption>

Photo (1) of a scope showing absolute voltage of the CANH and CANL wires. 6 CAN composed of recessive (CANH != CANL) and dominant (CANH=CANL) states . The three yellow highlighted belong to the dsPIC (A) and the three blue highlighted belong to the dsPIC (B). The dsPIC (A) frame (yellow) contains 3 data bytes while the dsPIC (B) frame (blue) contains only 2 data bytes (Blue highlighted frames are shorten than the yellow one). Each dsPIC feed its CAN peripheral with the 3 or 2 byte composing the frame at a frequency of 500Hz. A 2 ms time delay separates two consecutive frame created by one dsPIC (resp yellow one or blue one). However, time delay (Delta BA) separating a frame B=\>A from a frame A=\>B increase (or decrease) slowly because of the slight frequency difference between the two 8Mhz quartz clocking both dsPIC (frequency error). When both frame are close to each other, the CAN peripheral manage automatically bus arbitration to avoid conflict. Consequently, the first dsPIC writing a dominant state (byte) on the bus gets the priority. Consequently, the two frames keep close until switching their respective place and continuing to evaluate in time relatively to each other (see photo (2)).

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Scope_HM205_CAN_02.jpg" alt="Photo (2) of a scope showing absolute voltage of the CANH and CANL wires taken few seconds after the first photo (see photo 1). The voltages for dominant and recessive states are specified here. As mentioned in photo (1) caption, the time delay (Delta BA) separating two consecutive frames (B=&gt;A from A=&gt;B) is longer than in photo (1) due to the slight frequency difference between the two quartz driving each dsPIC." width="350">

<figcaption>

Photo (2) of a scope showing absolute voltage of the CANH and CANL wires taken few seconds after the first photo (see photo 1). The voltages for dominant and recessive states are specified here. As mentioned in photo (1) caption, the time delay (Delta BA) separating two consecutive frames (B=\>A from A=\>B) is longer than in photo (1) due to the slight frequency difference between the two quartz driving each dsPIC.

</figcaption>
</figure>

CAN acronym stands for Controller Area Network. It is a numerical bus coding its two states (one dominant and one recessive) using differential voltage between its two wires namely CANH and CANL.

CAN bus is a "multi-slave" bus where any connected dispositive can send a message. Frames are composed of an id which is set by user, and 1 to 8 data bytes. Device waiting for a specific data will filter out incoming frames based on their id. Thus both emitter and receiver exchanging data must have in common the frame id that will be used.

Each CAN frame are acknowledged by the receiver. The message is reemitted by its author until it is acknowledged. However, the reemission is stopped after the xx attempted.

Robust, use in car, error free CRC,

The CAN bus presentation is beyond the scope of this example. Readers are referred to the Wikimedia page on the [1](http://en.wikipedia.org/wiki/Controller_area_network) for further information.

Three blocks related to the CAN bus are available in the dsPIC blockset library.

- [CAN Configuration](/wiki/dspic-block-can-configuration/),
- [CAN Transmit](/wiki/dspic-block-can-transmit/) and
- [CAN Receive](/wiki/dspic-block-can-receive/).

The [CAN Configuration](/wiki/dspic-block-can-configuration/) block configure CAN peripheral like bus frequency, time quanta. This block is required as soon as one CAN peripheral is used.

The block [CAN Transmit](/wiki/dspic-block-can-transmit/) define frame id, data length (1 to 8 bytes) ... The block [CAN Receive](/wiki/dspic-block-can-receive/) filter out id, set max length of the incoming frame...

# Electronics

<figure class="wiki-figure">

<img loading="lazy" src="/images/CAN_addedComponents.jpg" alt="Added components for CAN bus: two CAN driver (MCP2551) drives the CAN differential signals. Two 10kOhm are required for theses drivers. One 68Ohms resistor is placed between the two CAN lines." width="120">

<figcaption>

Added components for CAN bus: two CAN driver (MCP2551) drives the CAN differential signals. Two 10kOhm are required for theses drivers. One 68Ohms resistor is placed between the two CAN lines.

</figcaption>
</figure>

We use the same prototyping board described in the [PWM example](/wiki/pwm-communication-between-two-dspic/#electronics). And a bootloader capable of flashing the binary into the chip through UART is also used as it is described [here](/wiki/pwm-communication-between-two-dspic/#bootloader).

The PWM wire is removed.

CAN driver description, added components

# Simulink models {#simulink_models}

Two simulink models generate the code for the dsPIC (A) and the dsPIC (B). The common parts of these two models have been described on the [PWM example](/wiki/pwm-communication-between-two-dspic/#common-parts), including the bootloader reset system.

Let's considers only the specific parts related to the CAN bus of these two models.

## Model A: Emission {#model_a_emission}

<figure class="wiki-figure">

<img loading="lazy" src="/images/SimulinkModel_CAN_a_30f4012.png" alt="Simulink model A: CAN_a_30f4012" width="350">

<figcaption>

Simulink model A: CAN_a_30f4012

</figcaption>
</figure>

The model A creates an internal sine wave signal of type int16 with amplitude 5000 and frequency 4 Hz.

Optimized method for sine wave generation was described in the [PWM example](/wiki/pwm-communication-between-two-dspic/#sine-wave-generation).

## Model B: Reception {#model_b_reception}

<figure class="wiki-figure">

<img loading="lazy" src="/images/SimulinkModel_CAN_b_30f4012.png" alt="Simulink model B: CAN_b_30f4012" width="350">

<figcaption>

Simulink model B: CAN_b_30f4012

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Rs232gui_CAN_b_ReceivedValue.png" alt="Matlab plot of the data sent by microcontroller B through UART. The rs232gui interface is used to plot incoming data in real-time" width="350">

<figcaption>

Matlab plot of the data sent by microcontroller B through UART. The rs232gui interface is used to plot incoming data in real-time

</figcaption>
</figure>
