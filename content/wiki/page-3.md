---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:54Z"
title: "DsPIC Block"
url: "/wiki/dspic-block/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/BlocksetLibrary.png" alt="PIC/dsPIC blockset Library for Simulink" width="350">

<figcaption>

PIC/dsPIC blockset Library for Simulink

</figcaption>
</figure>

## Root

[Master](/wiki/dspic-block-master/)
:   Select the targeted microcontroller, Set its Clock configuration (Quartz or External Clock, PLL\...), and few options allowing to check that real time time step constraint is respected.

[Compiler Configuration](/wiki/dspic-block-compiler-configuration/)
:   set the size of double data type (32 or 64 bits ; default is 32)

[Ports Info](/wiki/dspic-block-ports-info/)
:   List all pin used. Provide also peripheral using theses pins.

## Configure Simulink for dsPIC Target {#configure_simulink_for_dspic_target}

## Digital I/O {#digital_io}

[Digital Input](/wiki/dspic-block-digital-input/)
:   Logic Input

[Digital Output Write](/wiki/dspic-block-digital-output-write/)
:   Logic Output, write a value

[Digital Output Read](/wiki/dspic-block-digital-output-read/)
:   Logic Output, get the las value written

## Peripheral I/O Functions {#peripheral_io_functions}

[Analog to Digital Converter (ADC)](/wiki/dspic-block-adc-analog-to-digital-converter/)
:   Input driver for analog-to-digital converter (ADC)

[Input Capture (IC)](/wiki/dspic-block-input-capture/)
:   Pulse width modulation capture

[Change Notification (CN)](/wiki/dspic-block-change-notification/)
:   Pulse width modulation capture and change notification

[External Interrupt (EI)](/wiki/dspic-block-external-interrupt-pwm/)
:   Pulse width modulation capture and change notification

[Output Compare (OC)](/wiki/dspic-block-output-compare/)
:   Pulse width modulation (PWM) signal generation

[Output Compare Hardware (OC_HW)](/wiki/dspic-block-output-compare-hw/)
:   Pulse width modulation (PWM) signal generation without interrupt, allow fast PWM and synchronisation with ADC

[PWM Motor Output](/wiki/dspic-block-pwm-motor-output/)
:   Pulse width modulation (PWM) signal generation

## Serial Port (UART) {#serial_port_uart}

[UART Configuration](/wiki/dspic-block-uart-configuration/)
:   Set UART configuration

[Tx Output](/wiki/dspic-block-tx-output/)
:   Serial output a scalar or vector of uint8 data

[Rx Input](/wiki/dspic-block-rx-input/)
:   Serial Input a scalar of uint8 data

[Tx Output Multplexed for Matlab-Labview](/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/)
:   Serial output of data with conditionning allowing graphical monitoring of variable into matalb in pseudo real time

[Interface Tx-Matlab](/wiki/dspic-block-interface-tx-matlab/)
:   MAtalb Grapical User Interface to collect, view and record varaible evolution send using Tx Output Multiplexed for Matlab-Labview

## BUS SPI {#bus_spi}

[SPI Configuration](/wiki/dspic-block-spi-configuration/)
:   Configure the microcontroller SPI port

[SPI Input/Output](/wiki/dspic-block-spi-input-output/)
:   Input-Output driver for SPI

[SPI Input/Output interrupt driven](/wiki/dspic-block-spi-input-output-interrupt-driven/)
:   Input-Output interrupt driven SPI driver

## BUS CAN {#bus_can}

[CAN Configuration](/wiki/dspic-block-can-configuration/)
:   Configure the CAN Peripheral

[CAN Transmit](/wiki/dspic-block-can-transmit/)
:   Output block for CAN Peripheral

[CAN Receive](/wiki/dspic-block-can-receive/)
:   Input block for CAN Peripheral

## BUS I2C {#bus_i2c}

[I2C Master](/wiki/dspic-block-i2c-master/)
:   I2C Peripheral (as master)

## Others

[Calculus Time Step](/wiki/dspic-block-calculus-time-step/)
:   Get the time step calculation time

[Chronograph](/wiki/dspic-block-chronograph/)
:   Get time within the time step

[ C Function Call](/wiki/dspic-block-c-function-call/)
:   Call custom write handed C function

[ Clock Switch to Low Power mode](/wiki/dspic-block-clock-switch-lp/)
:   Switch clock into a LP mode, reducing power consumption

[Nop](/wiki/dspic-block-nop/)
:   Add Nop instructions introducint a lag time between two blocks

[Software Reset](/wiki/dspic-block-software-reset/)
:   Reset the microcontroller

------------------------------------------------------------------------

\<comments \\\>

------------------------------------------------------------------------
