---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-08-01T17:17:05Z"
title: "PIC32 Sensorless Speed Controller for DC Motor Applied on Picooz Main Rotor"
url: "/wiki/pic32-sensorless-speed-controller-for-dc-motor-applied-on-picooz-main-rotor/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_BeforeAfter.jpg" alt="The main motor with the rotor was used for the experiments" width="350">

<figcaption>

The main motor with the rotor was used for the experiments

</figcaption>
</figure>

Implementation of a sensorless DC speed motor control system with a PIC32 microcontroller.

# Introduction

One common problem of battery powered system is their dependence on the accumulator voltage. In the case of the Picooz tiny helicopter, the speed rates of the main and tail propellers are crucial for precise control. On the original Picooz electronics, it seems that motor are controlled in open loop in the way that the motor\'s power is proportional to the joystick stick. Thus, as the battery voltage decrease, both motor slow-down and the user have to adjust both sticks in real time. A sensorless speed controller which requires only one ADC input channel allows overcoming that problem. The speed controller will also speed up the dynamic of the motor and will reject efficiently external perturbations.

The objective here is to design a DC motor speed controller without any speed sensor. Motor\'s rotational speed is estimated by a measurement of the back-Electro Motrice Force (EMF). The motor is commanded through a PWM signal. During the PWM time where the motor is not powered, the motor acts as a dynamo. Measuring the generated voltage provides pretty good speed estimation.

A dsPIC or PIC32 are ideal target to test such controllers. The blockset for simulink available on this website allow implementing the controller efficiently without requiring knowledge about microcontrollers\'s programming technics.

# Electronics

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_Schematic.png" alt="Electronic schematic connected to an Explorer 16 board. This board power the DC motor with a PMW signal. The PIC OC1 pin generates a PWM signal with controllable duty cycle that controls a MOSFET transistor: FDC6305N. The back EMF is measured via the AN5 channel of the explorer 16 board. The overall system is powered here at 3.3V but could be powered with higher voltages." width="350">

<figcaption>

Electronic schematic connected to an Explorer 16 board. This board power the DC motor with a PMW signal. The PIC OC1 pin generates a PWM signal with controllable duty cycle that controls a MOSFET transistor: FDC6305N. The back EMF is measured via the AN5 channel of the explorer 16 board. The overall system is powered here at 3.3V but could be powered with higher voltages.

</figcaption>
</figure>

I did not build a complete embedded electronic system for the PICOOZ. This is a demo example is based on the Explorer 16 board, using the PIC32MX460F512L gracefully provided by Microchip. Converting the code for others dsPIC (30f, 33F, 24h) is quite straight using the Simulink blockset. Thus, the Picooz is taken as a test bench for the design of a sensorless speed controller. i.e. The helicopter will not flight in these tests.

One tiny electronics board composed of three components (see image) is connected to the Explorer 16 board. This tiny board allows providing energy power supply to the motor. The motor power supply is controlled through a PWM duty cycle from the microcontroller that controls the voltage given to the motor. The MOSFET transistor: [FDC6305N](http://www.fairchildsemi.com/ds/FD/FDC6305N.pdf) act as a high speed switch. When passing, its internal resistor is only of 0.1 Ohms. This small resistor has small impact on the max speed. It also makes the MOSFET to keep low temperature. The resistor between the Microcontrollers OC1 pin (PWM) and the MOSFET protects the microcontroller. The diode in parallel with the DC motor limits the nasty glitch due to the PWM signal passing through the motor coil. This diode is very important to protect the microcontroller. Removing this diode may severely damage the ADC of the microcontroller, of the entire microcontroller.

# Measuring the Back EMF {#measuring_the_back_emf}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_MeasureBackEMF_Simulink.png" alt="This model makes the motor PWM duty cycle increasing linearly increasing thus the picooz rotor&#x27;s speed rate. For each different duty cycle, channel 5 of the ADC (AN5) is sampled 120 times at 1200 different location within the PWM period. Data are sent through the UART 2 for analysis." width="350">

<figcaption>

This model makes the motor PWM duty cycle increasing linearly increasing thus the picooz rotor\'s speed rate. For each different duty cycle, channel 5 of the ADC (AN5) is sampled 120 times at 1200 different location within the PWM period. Data are sent through the UART 2 for analysis.

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_MeasureBackEMF_Results.png" alt="Back EMF Measurement. Up : Back-EMF at different instant within the PWM period. The first part of the curve emasuring 0 corresond to the MOSFET activated. The second part correspond to the MOSFET inactivated and thus, is a measurement of the back EMF. Down: Back-EMF at the PWM instant period 11980 for different PWM duty cycle (i.e. for different motor speed). This last curve provides an estimation of the motor speed." width="350">

<figcaption>

Back EMF Measurement. Up : Back-EMF at different instant within the PWM period. The first part of the curve emasuring 0 corresond to the MOSFET activated. The second part correspond to the MOSFET inactivated and thus, is a measurement of the back EMF. Down: Back-EMF at the PWM instant period 11980 for different PWM duty cycle (i.e. for different motor speed). This last curve provides an estimation of the motor speed.

</figcaption>
</figure>

A first simulink model programs the microcontroller so as to set-up the back-EMF measurement. This first model increase linearly the PWM motor duty cycle (from 0 to 11999 with a step size of 100) increasing the PICOOZ rotor\'s speed rate. There is no feed-back in this first experiment. For each 119 different duty cycle, the ADC channel 5 is sampled at 1200 different places within the PWM period. Thus, we obtain a 2D matrix, with the back EMF measurement (ADC conversion on AN5) in function of both

- The Sampling position within PWM period
- The PWM duty cycle

Theses measurement allows to determine the best place within the PWM period to measure the back EMF, and also allows to see the Back EMF evolution in function of the PWM duty cycle (i.e. in function of the motor speed rate).

# Identification of the dynamic of the Picooz\'s main rotor {#identification_of_the_dynamic_of_the_picoozs_main_rotor}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_ModeleResults.png" alt="Identification of the motor&#x27;s dynamic. The black line is the filtered measurement of the motor&#x27;s back EMF in response to a chirp input (at constant amplitude). The red line is the result of the simulated model, identified with theses data. We get a 72% fit." width="350">

<figcaption>

Identification of the motor\'s dynamic. The black line is the filtered measurement of the motor\'s back EMF in response to a chirp input (at constant amplitude). The red line is the result of the simulated model, identified with theses data. We get a 72% fit.

</figcaption>
</figure>

The design of a controller requires a model. A second simulink model programs the microcontroller to test the dynamic response of the motor. The Back EMF is there always sampled at 99.7% of the PWM duty cycle (instant 11970 of 11999, we takes some safety margin). The PWM duty cycle is now a chirp signal (sinus with increasing frequency) that makes the motor to accelerate and to slow down at increasing frequency. We supposed that the Back-EMF is an image of the motor speed rate. Thus, the motor model is identified using the matlab ident graphical user interface.

We get a two poles model for the Back-EMF (i.e. for the motor\'s dynamic)

<math display="inline"><semantics><mrow><msub><mi>G</mi><mrow><mi>m</mi><mi>o</mi><mi>t</mi><mi>o</mi><mi>r</mi></mrow></msub><mo stretchy="false" form="prefix">(</mo><mi>p</mi><mo stretchy="false" form="postfix">)</mo><mo>=</mo><mfrac><mrow><mi>−</mi><mn>24.62</mn></mrow><mrow><mo stretchy="false" form="prefix">(</mo><mi>p</mi><mo>+</mo><mn>78.65</mn><mo stretchy="false" form="postfix">)</mo><mo stretchy="false" form="prefix">(</mo><mi>p</mi><mo>+</mo><mn>9.78</mn><mo stretchy="false" form="postfix">)</mo></mrow></mfrac></mrow><annotation encoding="application/x-tex">G_{motor}(p) =  \frac{-24.62}{(p+78.65)(p+9.78)}</annotation></semantics></math>

The time constant of the motor <math display="inline"><semantics><mrow><msub><mi>τ</mi><mrow><mi>O</mi><mi>p</mi><mi>e</mi><mi>n</mi><mi>L</mi><mi>o</mi><mi>o</mi><mi>p</mi></mrow></msub><mo>=</mo><mn>102</mn><mi>m</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\tau_{OpenLoop} = 102ms</annotation></semantics></math> is calculated from the slower pole. Let\'s now design a close-loop controller to improve the motor\'s response and capacity to reject perturbation (due to gust of wind or to battery power decrease)

# Controller design {#controller_design}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_SSModel.png" alt="Sensorless speed controller : State Space Controller implemented on the PIC32 microcontroller using Simulink." width="350">

<figcaption>

Sensorless speed controller : State Space Controller implemented on the PIC32 microcontroller using Simulink.

</figcaption>
</figure>

The controller is designed keeping with theses two constraints:

- The implementation of the PWM output on the OC1 pin is quite sensitive to noisy set point (see blocks page). Thus, the controller command signal should have a reduced noise level.
- The continuous decrease of the battery level act as a continuous perturbation on the controller. Thus, rejecting with no steady states error this perturbation requires at least one integrator within the controller loop.

I decided to use an augmented state space model. A state space model has the advantage over a PID or PI only system to filter the output thanks to the internal model. The augmented state is the integral of the error, providing thus a controller with no steady state error.

We use the matlab new command lqi (available from Matlab 2008b) to compute the matrix gain K. The observer gain L is computed so as to get an observer pole as slow as the slowest pole of the close loop control system. Such a low gain allows filtering efficiently noise coming from the PWM measurement.

`Ts = .002;  % Controller Sample time `\
\
`Picooz_Mrotor = zpk([],[-78.68 -9.787],-24.6222);`\
`Picooz_Mrotor_z = c2d(Picooz_Mrotor,Ts,'zoh');`\
`[Picooz_Mrotor_z_ss,T] = canon(Picooz_Mrotor_z,'modal');     `\
`      % transformation pour calculs plus simple x ==> T*x`\
\
`[Az,Bz,Cz,Dz,Te] = ssdata(Picooz_Mrotor_z_ss);`\
`[m,n] = size(Az);`\
\
`%% Augmented state space synthesis (K)`\
\
`R = 1;`\
`Q = diag([1 1 2e6]);`\
`[K,Z,e] = lqi(Picooz_Mrotor_z_ss,Q,R,0);`\
\
`%Poles en continue : `\
`log(eig(Az))/Ts     % System Natural Poles`\
`log(e)/Ts           % Poles in close loop`\
\
`PolesControlleur_s = log(e)/Ts ;`\
\
`%% Observer L Synthesis`\
`poleLent = abs(PolesControlleur_s(1:end-1))`\
`PlacementPolesObs = exp(-poleLent * Ts * 1 );  %*3 usually`\
\
`L = acker(Az',Cz',PlacementPolesObs');`\
\
`%% Simplification`\
`% Az is diagonal (thanks to the cannon command)`\
`Az = diag(Az)';`\

We get results for L and K : L = \[-0.0593 0.826\] and K = \[0.5 1.2 1363.9\]. With this design, the new motor time constant is The time constant of the motor <math display="inline"><semantics><mrow><msub><mi>τ</mi><mrow><mi>C</mi><mi>l</mi><mi>o</mi><mi>s</mi><mi>e</mi><mi>L</mi><mi>o</mi><mi>o</mi><mi>p</mi></mrow></msub><mo>=</mo><mn>70</mn><mi>m</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\tau_{CloseLoop} =70ms</annotation></semantics></math>. Thus a 30% improvement. This improvement is not very huge. We are limited here by the necessity to have a low noise command signal. However, the close loop will counteract for the battery decreasing power.

# Results

<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_OpenVsCloseLoop.png" alt="From time 0 to time 22, the speed controller is activated: the PWM duty cycle (bottom blue line) is controlled with a feedback state space model. From 22s until the end (about 40s) the speed controller in not activated and the PWM duty cycle controlling the robot is set in open loop. The black line is the measured back EMF. This back EMF is related with the motor angular speed. The higher the back EMF is, the slower the motor rotates. The settling or rising time improvement can be noticed when the system is controlled with the sensorless regulator (close loop mode)." width="350">

<figcaption>

From time 0 to time 22, the speed controller is activated: the PWM duty cycle (bottom blue line) is controlled with a feedback state space model. From 22s until the end (about 40s) the speed controller in not activated and the PWM duty cycle controlling the robot is set in open loop. The black line is the measured back EMF. This back EMF is related with the motor angular speed. The higher the back EMF is, the slower the motor rotates. The settling or rising time improvement can be noticed when the system is controlled with the sensorless regulator (close loop mode).

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_OpenVsCloseLoop_Perturbation.png" alt="From time 0 to time 22, the speed controller is activated: the PWM duty cycle (bottom blue line) is controlled with a feedback state space model. I tried to slow down the rotor with my finger, but as it can be seen, the PWM duty cycle rise to compensate for the perturbation. From 22s until the end (about 40s) the speed controller in not activated and the PWM duty cycle controlling the robot is set in open loop. This time, when I disturbed the motor, the system do not compensate thus the motor just slow down, making the back EMF measurement getting higher." width="350">

<figcaption>

From time 0 to time 22, the speed controller is activated: the PWM duty cycle (bottom blue line) is controlled with a feedback state space model. I tried to slow down the rotor with my finger, but as it can be seen, the PWM duty cycle rise to compensate for the perturbation. From 22s until the end (about 40s) the speed controller in not activated and the PWM duty cycle controlling the robot is set in open loop. This time, when I disturbed the motor, the system do not compensate thus the motor just slow down, making the back EMF measurement getting higher.

</figcaption>
</figure>
<figure class="wiki-figure">

<img loading="lazy" src="/images/Picooz_SensorlessSpeedControl_TestBench.jpg" alt="Test Bench. The helicopter is fixed; the explorer 16 board can be seen in the right-up corner." width="550">

<figcaption>

Test Bench. The helicopter is fixed; the explorer 16 board can be seen in the right-up corner.

</figcaption>
</figure>

# Download

[SensorLess_Speed_Controller_ForPicooz.zip](/images/SensorLess_Speed_Controller_ForPicooz.zip)

The zip file contains all matlab files as is.

------------------------------------------------------------------------

[Category:Example](/wiki/category/example/)
