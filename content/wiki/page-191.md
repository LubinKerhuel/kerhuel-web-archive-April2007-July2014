---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-03-16T20:48:25Z"
title: "Picooz"
url: "/wiki/picooz/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_Photo.jpg" alt="Miniature flying helicopter Picooz from Silverlit" width="250">

<figcaption>

Miniature flying helicopter Picooz from Silverlit

</figcaption>
</figure>

I currently have two helicopters:

- One Picooz
- One Atlas

They are built by [Silverlit](http://www.silverlit.com)

I provide on this page technical measurement from the picooz helicopter. The Atlas model has not been yet opened so less information is presented about it.

# Picooz

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_Inside_Weight.jpg" alt="Inside a Picooz, different part with their respective weight" width="350">

<figcaption>

Inside a Picooz, different part with their respective weight

</figcaption>
</figure>

## Weight

- EPP : 1.57g
- Main propeller + main rotor + support : 4.55g
- accumulator : 1.87g
- Electronic board : 0.85g
- tail propeller : 0.08g
- tail motor : 0.63g
- tail motor housing : 0.17g
- tail main bar : 0.37g
- tail paper : 0.02g
- tail thin bar at the end : not measured but very small
- Total (Original Picooz measurement) : 10.40g

## main rotor force {#main_rotor_force}

The picooz helicopter weight **10.40g**. It can be **loaded** with a **3.5g** charge. With a 4g charge, the helicopter takes advantage of the ground effect and can fly, but can\'t elevate itself in the air. The maximum liftoff force given in gram force (gf) is about **14.2gf** (139.3 m) (This measurement includes the ground effect). Measurement is difficult to realize as it change over time. At full charge, the maximum liftoff force is attain after few instants (roughly speaking about 40s), time for the motor to warm up. Once wires are warm, their resistance get lower and more energy make it rotates faster.

## Tail rotor force {#tail_rotor_force}

The tail rotor generate a force during fly about **1.40gf** (13.7 mN). This force can be modulated with the radio command stick modulated about **+- 0.2gf** (1.96 mN). When directly connected to the battery, the tail rotor generates a maximum force between 2 and 2.5gf.

## Accumulator

The embedded energy is a **3.7V , 50maH LiPo** accumulator. When both rotors are at their maximum speed, the voltage drop is about 0.2V, very small compared to the 300 mA drain by the system.

## Onboard electronic {#onboard_electronic}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_BeforeAfter.jpg" alt="Before and after disassembling. these two versions fly successfully" width="350">

<figcaption>

Before and after disassembling. these two versions fly successfully

</figcaption>
</figure>

The tiny electronic board has two functions:

- controlling the main rotor and the tail propeller.
- demodulating the IR from the remote control

The control of the two propeller is done via PWM signal. For the main rotor, the period of the signal is **8.2ms**. For the tail motor, the period of the signal is **17ms**. The control of the rotor speed is done by changing the duty cycle duration. These are control directly by the remote control stick. However, the control is not continuous in the sense that several steps can be identified. The control is also not linear as the duty cycle step augmentation get smaller as the full power is approached. In other word, the command is **logarithmic**. The main motor can be fully powered (i.e. duty cycle = 100%) but the tail motor is never used with a 100% duty cycle.

**Two NPN transistors** are used to interface the reception part to the power part of the electronic. One NPN [**3DA8050M - HY1D**](http://www.btcparts.com/pdf/8050M.pdf) transistor is used for each propeller. The electronic can detect (probably using a current measurement) the blocking of the main rotor. The main rotor is blocked for example after a crash. As it happens, both motor are shut down to prevent break because of high current.

The main motor has an internal resistance of **3.20 Ohm**. The current measurement in normal operation (with rotor) gives **175 mA**. The tail motor has an internal resistance of **7.50 Ohms**. The current measurement in normal operation (with the propeller) is about **121 mA**. It seems that there is no sensorless speed controller on either of the propeller.

The modulation of the IR signal has not been studied. The [JRL project](http://www.jrl.cs.uni-frankfurt.de/wiki/ProtocolSilverlitIR) from Goethe University Frankfur provides details about the IR protocol.

# Atlas

The atlas helicopter from [Silverlit](http://www.silverlit.com) is like a picooz with an added actuator: It can go forward. [Modified version](http://www.rcgroups.com/forums/showthread.php?t=985475) of the Atlas with one more actuator can go forward, backward and sideslip.

The Atlas has the following characteristics: Weight: 11.57g The force generated by the main rotor is about 13.4g (test near the floor impacted by the ground effect). The Atlas fly well with an added 1.5g weight, 2g is the limit and won\'t fly with a 2.5g added weight.

# Sky Cruiser (NIKKO) {#sky_cruiser_nikko}

<figure class="wiki-figure">

<img loading="lazy" src="/images/NIKKO_SkyCruiser_Photo.jpg" alt="Miniature flying helicopter Sky Cruiser  NIKKO" width="250">

<figcaption>

Miniature flying helicopter Sky Cruiser NIKKO

</figcaption>
</figure>

- Total weight: 23.97g
- Red external cokpit weight: 2.76g

Accu: Full River 140mAh This helicopter does not have enough power to lift-up its weight except for the 20 first seconds. Then, the helicopter flight close to the ground thanks to the ground effect. Remote control is not an Infra Red one, but a real radio link (27Mhz). Removing the red cockpit allows normal flight, except that it goes slightly backward. The thin wire on the picture is the helicopter antenna (and not a broken wire that should be soldered to the tail rotor as it has been reported on some forum).
