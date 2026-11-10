---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2010-12-22T13:17:35Z"
title: "MEMS based Autopilote on dsPIC for RC model airplane"
url: "/wiki/mems-based-autopilote-on-dspic-for-rc-model-airplane/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Plane_Photo.jpg" alt="Remote Control Glider (1m25 wingspan) equipped with sensors (Gyrometers, Accelerometers) and calculators (dsPIC 30f4012)." width="350">

<figcaption>

Remote Control Glider (1m25 wingspan) equipped with sensors (Gyrometers, Accelerometers) and calculators (dsPIC 30f4012).

</figcaption>
</figure>

# The RC model airplane {#the_rc_model_airplane}

The airplane is a Delta wing called IXIR II chosen for its good flight performance, simplicity to build , robust to crashes and low cost (based on low cost construction material). The plane was created by \... who gives all instruction to build it on its website: \... (French)

Caracteristics :

- 1m25 wingspan
- 400g weight
- 2 actuated surfaces

# Embedded System {#embedded_system}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Plane_Inside.jpg" alt="Plane during the construction. Differents elements placed inside the planed are showed" width="350">

<figcaption>

Plane during the construction. Differents elements placed inside the planed are showed

</figcaption>
</figure>

The plane is equipped with standard RC components. A sensor board with a calculator are added into the plane. Finally, a solution for telemetry is also placed in the plane to retrieved in flight datas.

## Classical RC Material {#classical_rc_material}

The classical RC material is made of

- one 6 channel receiver (GWS 610)
- Two servo motor (HPX )
- 4 accumulator NiMh placed in the noise of the plane
- A beeper is also added. The plane can thus emit a sound to provide different indications and after a crash, to help research.

## Calculator

The calculator (dsPIC 30f4012) is the brain of the plane. It is connected to all different sensor and actuator embedded in the plane. Thus, it receives all data from both the RC receiver and the sensor board embedded in the plane. Algorithms can use theses data to estimate the plane attitude (IMU) and to control the plane (feedback controller).

## Sensors

<figure class="wiki-figure">

<img loading="lazy" src="/images/IMU_Photo.jpg" alt="IMU sensors : 1 accelerometer MMA7260 from freescale (3 axis) coupled with 2 rate gyros ADIS16080 from analog device (1 axis each)" width="350">

<figcaption>

IMU sensors : 1 accelerometer MMA7260 from freescale (3 axis) coupled with 2 rate gyros ADIS16080 from analog device (1 axis each)

</figcaption>
</figure>

Micro Electro-Mechanical Sensor (MEMS) are used to estimate the attitude of the plane. Theses sensors have many advantages : They are small, lightweight, low power consumption, robust from the mechanical point of view (i.e. crashproof) and some are precise (rate gyro).

Two different type of MEMS feed the IMU algorithm:

- rate gyro (ADIS 16080 from analog device)

<!-- -->

- Accelerometers (MMA7260) from freescale

The rate gyro measures the angular speed of the plane. Each ADIS16080 measure the angular speed on one axis, three of them are used to measure speed rate on the three axes.

The MMA7260 measure the forces due to the acceleration or gravity applied on itself. This component measures the acceleration on the 3 axis. The measure is 0 on the three axes only in 0G condition (free fall without friction). Otherwise, the gravity is measured as acceleration.

From both the rate gyro and the accelerometers, it is possible to compute the attitude of the plane. For more details on the calculation details, see the page dedicated to the Inertial Measurement Unit (IMU). Weight : Servos GWS HPX : 19g (X2) DC DC converter MCP1252-33X50 - MCP1253-33X50 (3.3V) ==\> 2.92g DC DC converter (5.0V) ==\> 3.73g Beeper : 3.95g SST SST25VF016B 16 Mbit SPI Serial Flash ==\> 3.95g Card dsPIC 30f4012 ==\> 17.87g Recepteur RS610 ==\> 7g Capteurs Inertiels (2 gyro + 1 accelero) ==\> 8.29g

boite maxim DALLAS : 9.35g

total : 85.71g

## Recording In Flight Data {#recording_in_flight_data}

The plane is an experimental platform to test IMU algorithms and AutoPilote (AP) Flight controller. IMU algorithms tested on the earth provide good results. However, in flight dynamic condition are difficult to mimic by handshaking the Miniature IMU. Thus, Telemetry gives a possibility to get an insight on data in flight conditions. It can be used for both logging raw sensor data and to log the embedded calculation result.

Data logged from raw data are typically used in simulation and allow improving algorithms.

The two methods to log data are

- place a data recorder in the plane (Solutions with SD cards)
- transmit data to a base-station using a wireless transmission system (Telemetry)

Both methods were explored. First a data-logger based on the SST EEPRPOM technology was developed. However, due to difficulties to cope with data recording time constraints, a wireless telemetry system was developed and installed onboard the plane. This wireless technology based on Free2Move Bluetooth card works. In flight data presented were recorded with this system. I will describe the two system developed.

### Data Recorder {#data_recorder}

SST

16 Mbits that is in a more common unit 2Mo. This is already a nice capacity.

Methods based on SD cards have capacity even bigger (up to 4Go) but are more complex to use.

### Telemetry

<figure class="wiki-figure">

<img loading="lazy" src="/images/Bluetooth_logo.png" alt="50">

<figcaption>

50

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Free2move_Schematic.png" alt="Electronic schematic of the two free2move Bluetooth module. The left is the F2M03GXA-S03 (USB version). Connected through USB to a computer, it is used as a long range USB Bluetooth dongle able to communicate with the second Bluetooth module. The left schematic is the embedded module: F2M03GXA-S01 (UART version). It is connected to the dsPIC microcontroller through UART. When both modules are paired, a virtual COM port is created on the computer allowing transmit/receive data from the embedded system." width="350">

<figcaption>

Electronic schematic of the two free2move Bluetooth module. The left is the F2M03GXA-S03 (USB version). Connected through USB to a computer, it is used as a long range USB Bluetooth dongle able to communicate with the second Bluetooth module. The left schematic is the embedded module: F2M03GXA-S01 (UART version). It is connected to the dsPIC microcontroller through UART. When both modules are paired, a virtual COM port is created on the computer allowing transmit/receive data from the embedded system.

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Free2move_PictureInside.jpg" alt="(top) Ground station Bluetooth module made of a free2move F2M03GXA-S03. It is linked to a PC using a standard USB cable. (Bottom) Embedded Bluetooth module (F2M03GXA-S01) component connected to the microcontroller." width="350">

<figcaption>

(top) Ground station Bluetooth module made of a free2move F2M03GXA-S03. It is linked to a PC using a standard USB cable. (Bottom) Embedded Bluetooth module (F2M03GXA-S01) component connected to the microcontroller.

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Free2move_Picture.jpg" alt="(top) Ground station Bluetooth module made of a free2move F2M03GXA-S03. It is linked to a PC using a standard USB cable. (Bottom) Embedded Bluetooth module (F2M03GXA-S01) component connected to the microcontroller." width="350">

<figcaption>

(top) Ground station Bluetooth module made of a free2move F2M03GXA-S03. It is linked to a PC using a standard USB cable. (Bottom) Embedded Bluetooth module (F2M03GXA-S01) component connected to the microcontroller.

</figcaption>
</figure>

Classical Bluetooth system can transmit/receive data in a small range of 10m (Class 1). However, some Bluetooth system can transmit to up to 100m (Class 3). Free2move developed a Bluetooth receiver that comply with the class 3 specification but the receiver is more sensitive allowing to receive data at 350m and more. (350m tested but not tested farther)

[WT11](http://www.bluegiga.com/WT11_Class_1_Bluetooth_Module) from Bluegiga

ZigBee solution

# Rate gyro and Accelerometers data in flight {#rate_gyro_and_accelerometers_data_in_flight}

<figure class="wiki-figure">

<img loading="lazy" src="/images/BlueToothDataLog_Flight003.png" alt="Inflight data transmitted via Bluetooth. Three curves pannel are presented. The first pannel (big one) present datas recorded during a short flight lasting 46s. The launch time and crash time are marked by the two wide black vertical line. Datas between theses two lines are taken inflight. The first three curves show the three glider angular rate measured with the three rate gyro (ADIS16080). The three curves in the middle are the acceleration as measured by the accelerometer (MMA7260). The last two curves are the remote control stick position controlling the plane, measured at the receiver level. The two subpannel, in the bottom left and bottom right are a close-up of the Launch and Crash detail. All data are recorded at 1Khz and the detail level is very high. Launch tme and Crash time are detected automatically by a script." width="350">

<figcaption>

Inflight data transmitted via Bluetooth. Three curves pannel are presented. The first pannel (big one) present datas recorded during a short flight lasting 46s. The launch time and crash time are marked by the two wide black vertical line. Datas between theses two lines are taken inflight. The first three curves show the three glider angular rate measured with the three rate gyro (ADIS16080). The three curves in the middle are the acceleration as measured by the accelerometer (MMA7260). The last two curves are the remote control stick position controlling the plane, measured at the receiver level. The two subpannel, in the bottom left and bottom right are a close-up of the Launch and Crash detail. All data are recorded at 1Khz and the detail level is very high. Launch tme and Crash time are detected automatically by a script.

</figcaption>
</figure>

# Airplane dynamics identification {#airplane_dynamics_identification}

Model : Two first order system describe respectively the pitch and roll dynamic of the plane.

# Angular rate control loop {#angular_rate_control_loop}

## Angular rate control {#angular_rate_control}

[Category:Example](/wiki/category/example/)
