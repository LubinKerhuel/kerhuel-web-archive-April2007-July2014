---
title: "SLUGS - an open source autopilot"
url: "/forum/topic/335/"
archiveKind: "topic"
---
# SLUGS - an open source autopilot

Forum : [Version compatibility issues](/forum/#forum-15)

25 message(s) · archive en lecture seule

<article class="forum-post" id="p1331">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-21 23:25 UTC">2010-11-21 23:25 UTC</time></header>
<div class="forum-post-body">The open source SLUG UAV autopilot is being developed at the Autonomous Systems Lab at the University of California Santa Cruz. More information can be found at <a href="http://slugsuav.soe.ucsc.edu/">http://slugsuav.soe.ucsc.edu/</a><br>
<br>
<br>
<br>
The autopilot can be compiled using the blockset (with a demo version allowing only 8 I/O, 2 I/O should be removed first for testing the compilation process)<br>
<br>
<br>
<br>
I get into a mail exchange with Mariano and another team. I rewrite here few tricks to compile successfully the SLUG autopilot with the most recent compiler and blockset version.<br>
<br>
<br>
<br>
SLUG : <br>
<br>
Sources downloaded from git at <strong><a href="https://github.com/malife/slugs">https://github.com/malife/slugs</a></strong><br>
<br>
Revert the git repository to a former stable and working version (From mariano, : <strong>git checkout 13d8c62a7d2</strong>)<br>
<br>
(Problem with missing navlink.h with head SLUG version (November 2010) )<br>
<br>
<br>
<br>
I tested with the following configuration :<br>
<br>
MATLAB 2010a (0x64)<br>
<br>
dsPIC blockset V3.3a<br>
<br>
dsPIC30, Microchip v3_25<br>
<br>
<br>
<br>
I get a error as shown in the compilation report:<br>
<pre><code>PPNumber of I/O PINs used : 8
TPTPTTPNumber of I/O PINs used : 8
TPNumber of I/O PINs used : 8
TTTWarning: Could not find an exact (case-sensitive) match for 'dsPIC_PWM_Motor_callback_InitMask'.
C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\blocks\dsPIC_PWM_motor_callback_InitMask.m is a case-insensitive
match and will be used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
PTPTPTTPNumber of I/O PINs used : 8
TPTWarning: Input port 1 of 'controlMCUSlugsMKII/Trim Vals/Log  Trims Using PWM High [groundStationDriver.c]/Report
Airspeed' is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/[dR dE dA dT]2' is not
connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/[dR dE dA dT]3' is not
connected. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Compute psi_dot_m/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane
of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Control  Law/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/L1 Output Feedback Controller With  Projection Operator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/L1 Output Feedback Controller With  Projection Operator/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane
of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/State Predictor/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1
Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1
Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1
Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1
Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/L1 Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/L1 Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/L1 Output Feedback Controller With  Projection Operator/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Angle Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Angle Conversion2/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Bank to Psi Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Bank to Psi Dot/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Bank to Psi Dot/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/High Pass (Washout) Filter/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/High Pass (Washout) Filter/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/High Pass (Washout) Filter/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Protect NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Roll Control [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Sideslip Compensation/Bank to Psi Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Sideslip Compensation/Constant'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Sideslip Compensation/Low Pass/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Sideslip Compensation/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Sideslip Compensation/psi_dot to Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/Yaw Damper [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Lateral Channel/psi_dot to Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Air Density from Height/Constant 2 from Model'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Air Density from Height/Length Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Air Density from Height/Rho_0 (Kg//m^3)'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Compute Airspeed/[ 0.01 50000]'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch  Command [PI]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs4/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Schedule LPF'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute Lateral Error/Subsystem3/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Compute T  in Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get Circles/Compute delta Left Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get Circles/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get Circles/compute delta Right Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS Location/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS Location/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS Location/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line Segment/1st WP'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line Segment/Compute  Projection/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line Segment/Compute Total Run/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Compute Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Compute Frenet/Normalize Vector /Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP2/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP2/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP2/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Geod2LTP2/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Switch'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Gravity'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/Compute Eta/Subsystem6/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'UpperLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/GainSchedule L2 and Get Groundspeed/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/Park's Lateral Accel Command/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/as_c to phi_c/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Trim
Vals/Gain1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Trim
Vals/Gain2'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Trim
Vals/Gain3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/Generate PWM Signals Based on the Control Type/If  Control Type Is Selective
Passthrough/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/Generate PWM Signals Based on the Control Type/If  Control Type Is Selective
Passthrough/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/Generate PWM Signals Based on the Control Type/If  Control Type Is Selective
Passthrough/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/Generate PWM Signals Based on the Control Type/If  Control Type Is Selective
Passthrough/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/get Nav
Vars/Angle Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'UpperLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/get Nav
Vars/Direction Cosine Matrix to Euler Angles/Subsystem3/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be represented exactly
using the run-time data type. A small quantization error has occurred. You can control this diagnostic on the
Diagnostics pane of the Configuration Parameters dialog. This originated from 'controlMCUSlugsMKII/get Nav
Vars/Direction Cosine Matrix to Euler Angles/Subsystem3/[-1,1]'. 
### Invoking Target Language Compiler on controlMCUSlugsMKII.rtw
### Using System Target File: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic.tlc
### Loading TLC function libraries
.......
### Initial pass through model to cache user defined code
.....................
### Caching model source code
...............................................................................
...............................................................................
...............................................................................
...............................................................................
............................................................
### Writing main
..
### Writing source file controlMCUSlugsMKII.c
.
### Writing header file controlMCUSlugsMKII_private.h
### Writing header file controlMCUSlugsMKII.h
.
### Writing header file controlMCUSlugsMKII_types.h
### Writing header file rtwtypes.h
.
### Writing header file rt_MAXf_snf.h
### Writing header file rt_zcfcn.h
### Writing source file rt_zcfcn.c
.
### Writing header file rt_nonfinite.h
### Writing source file rt_nonfinite.c
.
### Writing header file rt_SATURATE.h
### Writing header file rt_SIGNf_snf.h
.
### Writing header file rtGetInf.h
### Writing source file rtGetInf.c
.
### Writing header file rtGetNaN.h
### Writing source file rtGetNaN.c
.
### Writing source file controlMCUSlugsMKII_data.c
### Writing header file autobuild.h
### Writing source file controlMCUSlugsMKII_main.c
.
### TLC code generation complete.
..........
### Creating HTML report file controlMCUSlugsMKII_codegen_rpt.html
.### Creating project marker file: rtw_proj.tmw
### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V&amp;&amp;Version&amp;&amp;(&amp;&amp;  Date       &amp;&amp;) for Matlab &amp;&amp; Release &amp;&amp;.
<wbr>
<wbr>
Licence Accorded to  &amp;&amp;               Licence Name          &amp;&amp;
                     &amp;&amp;               Mailcontact           &amp;&amp;
                     &amp;&amp;               Companie              &amp;&amp;
                     &amp;&amp;               CompanieAddress1      &amp;&amp;
                     &amp;&amp;               CompanieAddress2      &amp;&amp;
                     &amp;&amp;               CompanieAddress3      &amp;&amp;
                     &amp;&amp;               CompanieAddress4      &amp;&amp;
<wbr>
 Facturation to :    &amp;&amp;               BuyerName             &amp;&amp;
                     &amp;&amp;               MailBuyer             &amp;&amp;
                     &amp;&amp;               BuyerAddress1         &amp;&amp;
                     &amp;&amp;               BuyerAddress2         &amp;&amp;
                     &amp;&amp;               BuyerAddress3         &amp;&amp;
                     &amp;&amp;               BuyerAddress4         &amp;&amp;
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating controlMCUSlugsMKII.mk from C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
### Building controlMCUSlugsMKII: "C:\PROGRA~1\MATLAB\R2010a\bin\win64\gmake" -f controlMCUSlugsMKII.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDS=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/DEE.c 
''pic30-gcc  -c C:\Users\Lubin\Desktop\SLUGS\clib/DEES.s -Wa,-p=33fJ256MC710,-g 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/apUtils.c 
C:\Users\Lubin\Desktop\SLUGS\clib/apUtils.c:852:7: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/circBuffer.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_data.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_main.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    dsPIC_InputCapture_Interrupt.c 
dsPIC_InputCapture_Interrupt.c: In function '_IC2Interrupt': 
dsPIC_InputCapture_Interrupt.c:11: warning:  PSV model not specified for '_IC2Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC3Interrupt': 
dsPIC_InputCapture_Interrupt.c:32: warning:  PSV model not specified for '_IC3Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC4Interrupt': 
dsPIC_InputCapture_Interrupt.c:53: warning:  PSV model not specified for '_IC4Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC5Interrupt': 
dsPIC_InputCapture_Interrupt.c:74: warning:  PSV model not specified for '_IC5Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC8Interrupt': 
dsPIC_InputCapture_Interrupt.c:95: warning:  PSV model not specified for '_IC8Interrupt'; 
   assuming 'auto_psv' this may affect latency 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/groundStationDriver.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/interProcCommSlave.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/navSupport.c 
C:\Users\Lubin\Desktop\SLUGS\clib/navSupport.c:211:2: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/protDecoder.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rtGetInf.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rtGetNaN.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rt_nonfinite.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rt_zcfcn.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/sbrk.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch 	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII.c 
''pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~2\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld -o ..\../controlMCUSlugsMKII.cof  DEE.o DEES.o apUtils.o circBuffer.o controlMCUSlugsMKII_data.o controlMCUSlugsMKII_main.o dsPIC_InputCapture_Interrupt.o groundStationDriver.o interProcCommSlave.o navSupport.o protDecoder.o rtGetInf.o rtGetNaN.o rt_nonfinite.o rt_zcfcn.o sbrk.o controlMCUSlugsMKII.o      C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Program Files (x86)\Microchip\mplabc30\v3.25\bin\bin/pic30-coff-ld.exe: mode pic30_coff 
DEE.o 
DEES.o 
apUtils.o 
circBuffer.o 
controlMCUSlugsMKII_data.o 
controlMCUSlugsMKII_main.o 
dsPIC_InputCapture_Interrupt.o 
groundStationDriver.o 
interProcCommSlave.o 
navSupport.o 
protDecoder.o 
rtGetInf.o 
rtGetNaN.o 
rt_nonfinite.o 
rt_zcfcn.o 
sbrk.o 
controlMCUSlugsMKII.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)brk.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)putsUART2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenTimer2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture4.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture4.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture5.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture5.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture8.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture8.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)SetDCMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memcpy.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)vsprintf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memset.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xprintf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xvacopy.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)strchr.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xputfld.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xputtxt.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldtob.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xlitob.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)strlen.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memchr.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldunsca.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldscale.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)ldiv.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xgenld.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xdnorm.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)div.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixsfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)atan2f.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)powf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sqrtf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)atanf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)asinf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sinf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)cosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)tanf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)acosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)expf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fne.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floorf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)extendsfdf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)deqltle.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixdfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsidf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)subdf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dgtge.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)muldf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divdf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)umodsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)udivsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divmoddi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)muldi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)errno.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)futil.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fchop.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)_frexpf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)ldexpf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)logf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)asinacosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sincosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dcompare.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatdidf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)adddf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)umuldi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dtype.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dpropagateNaN.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x2aa00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x200              0x296e          0x3e25  (15909) 
.text                       0x2b6e                0x8c            0xd2  (210) 
.isr                        0x2bfa                 0x2             0x3  (3) 
_036e5a804ce95ae1           0x2c00              0x1000          0x1800  (6144) 
.const                      0x3c00                0x94            0xde  (222) 
.text                       0x3c94              0x6012          0x901b  (36891) 
.dinit                      0x9ca6               0x1da           0x2c7  (711) 
.text                       0x9e80               0x3be           0x59d  (1437) 
.text                       0xa23e                0x8e            0xd5  (213) 
<wbr>
                     Total program memory used (bytes):         0xf12c  (61740) 23% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x7800] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.nbss                        0x800                   0          0x174e  (5966) 
.ndata                      0x1f4e                   0            0x56  (86) 
.nbss                       0x1fa4                   0            0x2c  (44) 
.ndata                      0x1fd0                   0             0x4  (4) 
.nbss                       0x1fd4                   0             0x4  (4) 
.ndata                      0x1fd8                   0             0x4  (4) 
.nbss                       0x1fdc                   0             0x2  (2) 
.data                       0x1fde                   0            0x48  (72) 
.dconst                     0x2026                   0            0x32  (50) 
.data                       0x2058                   0            0x34  (52) 
.dconst                     0x208c                   0             0x8  (8) 
.bss                        0x2094                   0             0x2  (2) 
.data                       0x2096                   0             0x2  (2) 
.dconst                     0x2098                   0             0x2  (2) 
.data                       0x209a                   0             0x2  (2) 
_0299ea804ce95aea           0x7f32                   0            0xce  (206) 
<wbr>
                        Total data memory used (bytes):         0x196a  (6506) 21% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                       0x209c                              0x5e96  (24214) 
<wbr>
                        Maximum dynamic memory (bytes):         0x5e96  (24214) 
<wbr>
sbrk.o(.libc+0x4):C:\Users\Lubin\Desktop\SLUGS\clib\sbrk.c: Link Error: Cannot access symbol (___curbrk) with file register addressing. Value must be less than 8192. Suggest large-data model. 
C:\Program Files (x86)\Microchip\mplabc30\v3.25\bin\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../controlMCUSlugsMKII.cof' 
gmake: *** [..\../controlMCUSlugsMKII.cof] Error 255 
### Real-Time Workshop build procedure for model: 'controlMCUSlugsMKII' aborted due to an error.
&gt;&gt; 
</code></pre><br>
Problem encounter while linking; Compiler suggest large-data model. <br>
<br>
<br>
<br>
The project can be opened within MPLAB (the blockset creates an MPLAB project file from version 3.3). Right click on the mcp file within the MATLAB file browser, and select <strong>open outside MATLAB</strong> ==&gt; it will open MPLAB.<br>
<br>
MPLAB will allow changing graphically the compilation options and to play with...<br>
<br>
Thus, in the compilation options of MPLAB C30 choose large data model and re-compile the project (within MPLAB).<br>
<br>
It works successfully.<br>
<br>
<br>
<br>
Let’s integrate the new compilation options.<br>
<br>
The problem could directly be solved within matlab:<br>
<br>
In the opened model, choose <br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt;<br>
<br>
In the tab Real-Time Workshop ==&gt; DsPIC options, add<strong> -mlarge-data</strong> to the optimisation parameter (OPTIM_GCC). The line should now be : -mcpu=33fJ256MC710 -O -merrata=exch <strong>-mlarge-data</strong><br>
<br>
(Mariano provided the same trick by mail)<br>
<br>
Generating C and compiling the model within Simulink is now Ok.<br>
<br>
<br>
<br>
The finale report becomes:<br>
<pre><code>PTTPTPTPNumber of I/O PINs used : 8
TTPTPTWarning: Input port 1 of 'controlMCUSlugsMKII/Trim Vals/Log  Trims Using PWM High
[groundStationDriver.c]/Report Airspeed' is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/[dR dE dA
dT]2' is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/[dR dE dA
dT]3' is not connected. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Compute psi_dot_m/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented
exactly using the run-time data type. A small quantization error has occurred. You can control
this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With  Projection
Operator/Control  Law/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented
exactly using the run-time data type. A small quantization error has occurred. You can control
this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With  Projection
Operator/State Predictor/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You can
control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output Feedback Controller With
Projection Operator/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Angle
Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Angle
Conversion2/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Bank to Psi
Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Bank to Psi
Dot/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Bank to Psi
Dot/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/High Pass (Washout)
Filter/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/High Pass (Washout)
Filter/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/High Pass (Washout)
Filter/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Protect
NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Protect
NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Protect
NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Roll Control
[PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Sideslip
Compensation/Bank to Psi Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Sideslip
Compensation/Constant'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Sideslip
Compensation/Low Pass/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Sideslip
Compensation/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Sideslip
Compensation/psi_dot to Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/Yaw Damper
[PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral Channel/psi_dot to
Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Air Density
from Height/Constant 2 from Model'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Air Density
from Height/Length Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Air Density
from Height/Rho_0 (Kg//m^3)'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Airspeed Hold
[PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Compute
Airspeed/[ 0.01 50000]'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Height Error
to Pitch  Command [PI]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Pitch To
Elevator [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Protect
NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Protect
NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Protect
NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Protect
NaNs4/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Schedule LPF'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute Lateral
Error/Subsystem3/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Compute T  in Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Get Circles/Compute delta Left Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Get Circles/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Compute
P/Get Circles/compute delta Right Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Grab
IC/Compute GS Location/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Grab
IC/Compute GS Location/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Grab
IC/Compute GS Location/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Switch
when  in Line Segment/1st WP'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Switch
when  in Line Segment/Compute  Projection/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Compute WP Index/Switch
when  in Line Segment/Compute Total Run/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Compute Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Compute Frenet/Normalize Vector /Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP2/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP2/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP2/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Geod2LTP2/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get Wps Compute
Frenet/Switch'. 
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Gravity'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Park, Deyst &amp; How Lat
Accel Cmd/Compute Eta/Subsystem6/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'UpperLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Park, Deyst &amp; How Lat
Accel Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Park, Deyst &amp; How Lat
Accel Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Park, Deyst &amp; How Lat
Accel Cmd/GainSchedule L2 and Get Groundspeed/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Park, Deyst &amp; How Lat
Accel Cmd/Park's Lateral Accel Command/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/as_c to phi_c/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Inner Loop// Navigation/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Trim Vals/Gain1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Trim Vals/Gain2'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Trim Vals/Gain3'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/Generate PWM Signals
Based on the Control Type/If  Control Type Is Selective Passthrough/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/Generate PWM Signals
Based on the Control Type/If  Control Type Is Selective Passthrough/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/Generate PWM Signals
Based on the Control Type/If  Control Type Is Selective Passthrough/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/Update PWM Commands and Send Telemetry/Generate PWM Signals
Based on the Control Type/If  Control Type Is Selective Passthrough/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/get Nav Vars/Angle Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'UpperLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/get Nav Vars/Direction Cosine Matrix to Euler
Angles/Subsystem3/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'. The parameter's value cannot be
represented exactly using the run-time data type. A small quantization error has occurred. You
can control this diagnostic on the Diagnostics pane of the Configuration Parameters dialog. This
originated from 'controlMCUSlugsMKII/get Nav Vars/Direction Cosine Matrix to Euler
Angles/Subsystem3/[-1,1]'. 
### Invoking Target Language Compiler on controlMCUSlugsMKII.rtw
### Using System Target File: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic.tlc
### Loading TLC function libraries
.......
### Initial pass through model to cache user defined code
.....................
### Caching model source code
...............................................................................
...............................................................................
...............................................................................
...............................................................................
............................................................
### Writing main
..
### Writing source file controlMCUSlugsMKII.c
.
### Writing header file controlMCUSlugsMKII_private.h
### Writing header file controlMCUSlugsMKII.h
.
### Writing header file controlMCUSlugsMKII_types.h
### Writing header file rtwtypes.h
.
### Writing header file rt_MAXf_snf.h
### Writing header file rt_zcfcn.h
### Writing source file rt_zcfcn.c
.
### Writing header file rt_nonfinite.h
### Writing source file rt_nonfinite.c
.
### Writing header file rt_SATURATE.h
### Writing header file rt_SIGNf_snf.h
.
### Writing header file rtGetInf.h
### Writing source file rtGetInf.c
.
### Writing header file rtGetNaN.h
### Writing source file rtGetNaN.c
.
### Writing source file controlMCUSlugsMKII_data.c
### Writing header file autobuild.h
### Writing source file controlMCUSlugsMKII_main.c
.
### TLC code generation complete.
..........
### Creating HTML report file controlMCUSlugsMKII_codegen_rpt.html
.### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V&amp;&amp;Version&amp;&amp;(&amp;&amp;  Date       &amp;&amp;) for Matlab &amp;&amp; Release &amp;&amp;.
<wbr>
<wbr>
Licence Accorded to  &amp;&amp;               Licence Name          &amp;&amp;
                     &amp;&amp;               Mailcontact           &amp;&amp;
                     &amp;&amp;               Companie              &amp;&amp;
                     &amp;&amp;               CompanieAddress1      &amp;&amp;
                     &amp;&amp;               CompanieAddress2      &amp;&amp;
                     &amp;&amp;               CompanieAddress3      &amp;&amp;
                     &amp;&amp;               CompanieAddress4      &amp;&amp;
<wbr>
 Facturation to :    &amp;&amp;               BuyerName             &amp;&amp;
                     &amp;&amp;               MailBuyer             &amp;&amp;
                     &amp;&amp;               BuyerAddress1         &amp;&amp;
                     &amp;&amp;               BuyerAddress2         &amp;&amp;
                     &amp;&amp;               BuyerAddress3         &amp;&amp;
                     &amp;&amp;               BuyerAddress4         &amp;&amp;
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating controlMCUSlugsMKII.mk from C:\Mes_doccuments_Maison\prog\Matlab2\RTWdsPIC\dspic\dspic_pic30_gcc.tmf
### Building controlMCUSlugsMKII: "C:\PROGRA~1\MATLAB\R2010a\bin\win64\gmake" -f controlMCUSlugsMKII.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDS=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/DEE.c 
''pic30-gcc  -c C:\Users\Lubin\Desktop\SLUGS\clib/DEES.s -Wa,-p=33fJ256MC710,-g 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/apUtils.c 
C:\Users\Lubin\Desktop\SLUGS\clib/apUtils.c:852:7: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/circBuffer.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_data.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_main.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    dsPIC_InputCapture_Interrupt.c 
dsPIC_InputCapture_Interrupt.c: In function '_IC2Interrupt': 
dsPIC_InputCapture_Interrupt.c:11: warning:  PSV model not specified for '_IC2Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC3Interrupt': 
dsPIC_InputCapture_Interrupt.c:32: warning:  PSV model not specified for '_IC3Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC4Interrupt': 
dsPIC_InputCapture_Interrupt.c:53: warning:  PSV model not specified for '_IC4Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC5Interrupt': 
dsPIC_InputCapture_Interrupt.c:74: warning:  PSV model not specified for '_IC5Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC8Interrupt': 
dsPIC_InputCapture_Interrupt.c:95: warning:  PSV model not specified for '_IC8Interrupt'; 
   assuming 'auto_psv' this may affect latency 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/groundStationDriver.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/interProcCommSlave.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/navSupport.c 
C:\Users\Lubin\Desktop\SLUGS\clib/navSupport.c:211:2: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/protDecoder.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rtGetInf.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rtGetNaN.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rt_nonfinite.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    rt_zcfcn.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    C:\Users\Lubin\Desktop\SLUGS\clib/sbrk.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Lubin\Desktop\SLUGS\controlMCUSlugsMKII_dspic\sources -IC:\Users\Lubin\Desktop\SLUGS -IC:\Users\Lubin\Desktop\SLUGS\clib   -I C:\PROGRA~2\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII.c 
''pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~2\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld -o ..\../controlMCUSlugsMKII.cof  DEE.o DEES.o apUtils.o circBuffer.o controlMCUSlugsMKII_data.o controlMCUSlugsMKII_main.o dsPIC_InputCapture_Interrupt.o groundStationDriver.o interProcCommSlave.o navSupport.o protDecoder.o rtGetInf.o rtGetNaN.o rt_nonfinite.o rt_zcfcn.o sbrk.o controlMCUSlugsMKII.o      C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Program Files (x86)\Microchip\mplabc30\v3.25\bin\bin/pic30-coff-ld.exe: mode pic30_coff 
DEE.o 
DEES.o 
apUtils.o 
circBuffer.o 
controlMCUSlugsMKII_data.o 
controlMCUSlugsMKII_main.o 
dsPIC_InputCapture_Interrupt.o 
groundStationDriver.o 
interProcCommSlave.o 
navSupport.o 
protDecoder.o 
rtGetInf.o 
rtGetNaN.o 
rt_nonfinite.o 
rt_zcfcn.o 
sbrk.o 
controlMCUSlugsMKII.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)brk.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)putsUART2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenTimer2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture4.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture4.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture5.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture5.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture8.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture8.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)SetDCMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenMCPWM.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memcpy.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)vsprintf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memset.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xprintf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xvacopy.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)strchr.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xputfld.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xputtxt.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldtob.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xlitob.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)strlen.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)memchr.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldunsca.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xldscale.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)ldiv.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xgenld.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)xdnorm.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libc-coff.a)div.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixsfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)atan2f.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)powf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sqrtf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)atanf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)asinf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sinf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)cosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)tanf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)acosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)expf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fne.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floorf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)extendsfdf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)deqltle.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fixdfsi.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsidf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)subdf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dgtge.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)muldf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divdf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)umodsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)udivsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)divmoddi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)muldi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)errno.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)futil.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fchop.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)_frexpf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)ldexpf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)logf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)asinacosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)sincosf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dcompare.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack2.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)floatdidf.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)adddf3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dpack.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)umuldi3.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dtype.o 
(C:\PROGRA~2\MICROC~1\MPLABC~2\lib\libm-coff.a)dpropagateNaN.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x2aa00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x200              0x296e          0x3e25  (15909) 
.text                       0x2b6e                0x8c            0xd2  (210) 
.isr                        0x2bfa                 0x2             0x3  (3) 
_03597a804ce99355           0x2c00              0x1000          0x1800  (6144) 
.const                      0x3c00                0x94            0xde  (222) 
.text                       0x3c94              0x646a          0x969f  (38559) 
.dinit                      0xa0fe               0x1da           0x2c7  (711) 
.text                       0xa2d8               0x3be           0x59d  (1437) 
.text                       0xa696                0x8e            0xd5  (213) 
<wbr>
                     Total program memory used (bytes):         0xf7b0  (63408) 24% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x7800] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.nbss                        0x800                   0             0x2  (2) 
.bss                         0x802                   0          0x174e  (5966) 
.data                       0x1f50                   0            0x9e  (158) 
.dconst                     0x1fee                   0            0x32  (50) 
.data                       0x2020                   0            0x22  (34) 
.bss                        0x2042                   0            0x2c  (44) 
.data                       0x206e                   0            0x12  (18) 
.dconst                     0x2080                   0             0x8  (8) 
.data                       0x2088                   0             0x4  (4) 
.bss                        0x208c                   0             0x4  (4) 
.data                       0x2090                   0             0x4  (4) 
.bss                        0x2094                   0             0x2  (2) 
.data                       0x2096                   0             0x2  (2) 
.dconst                     0x2098                   0             0x2  (2) 
.data                       0x209a                   0             0x2  (2) 
_0291ea804ce9935e           0x7f32                   0            0xce  (206) 
<wbr>
                        Total data memory used (bytes):         0x196a  (6506) 21% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                       0x209c                              0x5e96  (24214) 
<wbr>
                        Maximum dynamic memory (bytes):         0x5e96  (24214) 
<wbr>
 ================================================================
*** Embedded Target for dsPIC by Lubin KERHUEL - http://www.kerhuel.eu
 | Licence Accorded to &amp;&amp;               Licence Name          &amp;&amp;|
 |                     &amp;&amp;               Mailcontact           &amp;&amp;|
 |          Companie : &amp;&amp;               Companie              &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress1      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress2      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress3      &amp;&amp;|
 |                     &amp;&amp;               CompanieAddress4      &amp;&amp;|
 | Financial Service : &amp;&amp;               BuyerName             &amp;&amp;|
 | Contact             &amp;&amp;               MailBuyer             &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress1         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress2         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress3         &amp;&amp;|
 |                     &amp;&amp;               BuyerAddress4         &amp;&amp;|
 | Version &amp;&amp;Version&amp;&amp;                       &amp;&amp;  Date       &amp;&amp;  |
 | For Matlab &amp;&amp; VerMatlab &amp;&amp; &amp;&amp; Release &amp;&amp;                     |
 ================================================================
*** Created executable: ..\../controlMCUSlugsMKII.cof
''pic30-bin2hex ..\../controlMCUSlugsMKII.cof  
*** Created executable: ..\../controlMCUSlugsMKII.hex
.
***Ready to be downloaded into 33fJ256MC710. (with MPLAB: file -&gt; import, choose controlMCUSlugsMKII.hex)
***alternative (experimental): load the project and re-compile it in MPLAB IDE
### Successful completion of Real-Time Workshop build procedure for model: controlMCUSlugsMKII
&gt;&gt; </code></pre><br>
Lubin</div>
</article>

<article class="forum-post" id="p1335">
<header><strong>dambrosio</strong><time datetime="2010-11-23 00:15 UTC">2010-11-23 00:15 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Here is what has been going on when I try and compile the stable version (checkout: 13d8c62a7d2) of the SLUG software. <br>
<br>
<br>
<br>
To make sure the latest blockset (V3.3a Matlab 20010a) was working I compiled the example mode files and it succeed with no errors.<br>
<pre><code>Ok  ==&gt;   Data_Login_Matlab.mdl
Ok  ==&gt;   FlexBoard_Blinking_Led.mdl
Ok  ==&gt;   Servo_ADC.mdl
Ok  ==&gt;   Servo_Sinus.mdl
Ok  ==&gt;   dsPIC_32MX460F512L_Explorer16_HyperSampling.mdl
Ok  ==&gt;   dsPIC_33f_Explorer16.mdl
End of Compilation in Elapsed time is 114.912392 seconds.
<wbr>
<wbr>
Some models may not compile if the appropriate 
dsPIC (24 30 33) or PIC32 Compiler is not installed
<wbr>
Ok  ==&gt;   Data_Login_Matlab.mdl
Ok  ==&gt;   FlexBoard_Blinking_Led.mdl
Ok  ==&gt;   Servo_ADC.mdl
Ok  ==&gt;   Servo_Sinus.mdl
Ok  ==&gt;   dsPIC_32MX460F512L_Explorer16_HyperSampling.mdl
Ok  ==&gt;   dsPIC_33f_Explorer16.mdl
</code></pre><br>
<br>
I went ahead and tried to compile the controlMCUSlugsMKII.c file to created the necessary files and I got the following error. Below is a copy-paste of my command window.<br>
<br>
<br>
<pre><code>PTTPNumber of I/O PINs used : 8
TPNumber of I/O PINs used : 8
TPNumber of I/O PINs used : 8
TTPNumber of I/O PINs used : 8
TPTWarning: Input port 1 of 'controlMCUSlugsMKII/Trim Vals/Log  Trims
Using PWM High [groundStationDriver.c]/Report Airspeed' is not
connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands
and Send Telemetry/[dR dE dA dT]2' is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM Commands
and Send Telemetry/[dR dE dA dT]3' is not connected. 
failed assertion in .\cdr\cdr_api.cpp at line 3194:
	!errorOccurred
Stack Trace:
  [0] stateflow.dll:0x286b1e4a(0x28739f5c "!errorOccurred", 0x28739490 ".\cdr\cdr_api.cpp", 3194, 0)
  [1] stateflow.dll:0x284bd540(0, 0x00c18664, 0, 0x00c186cc)
  [2] stateflow.dll:0x284bdf0d(44, 0, 0x00c18664, 2)
  [3] stateflow.dll:0x286b7e70(0, 0x00c18664, 3, 0x00c186c4)
  [4] stateflow.dll:0x285ebd77(0, 0x00c18664, 0x00c186c4, 0x22242550)
  [5] stateflow.dll:0x285ebdba(0, 0x00c18664, 3, 0x00c186c4)
  [6] libmex.dll:_mexRunMexFile(0, 0x00c18664, 3, 0x00c186c4) + 132 bytes
  [7] libmex.dll:private: void __thiscall Mfh_mex::runMexFileWithSignalProtection(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c18664, 3, 0x00c186c4) + 73 bytes
  [8] libmex.dll:public: virtual void __thiscall Mfh_mex::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c18664, 3, 0x00c186c4) + 321 bytes
  [9] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c18664, 3, 0x00c186c4) + 249 bytes
  [10] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c18664, 3, 0x00c186c4) + 420 bytes
  [11] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1282, 0x27c08eec "sf", 0, 3) + 626 bytes
  [12] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 12106, 125, 0) + 1282 bytes
  [13] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 12106, 10, 0) + 39 bytes
  [14] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 12106, 10, 0) + 251 bytes
  [15] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0, 0xffffffff, 0x260fe318, 1) + 876 bytes
  [16] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c18eac, 5, 0x00c18f0c) + 466 bytes
  [17] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c18eac, 5) + 23 bytes
  [18] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c18eac, 5, 0x00c18f0c) + 25 bytes
  [19] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c18eac, 5, 0x00c18f0c) + 249 bytes
  [20] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c18eac, 5, 0x00c18f0c) + 420 bytes
  [21] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(2689, 0x2a8b8eac "code_sfun_glue_code", 1, 5) + 626 bytes
  [22] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 921, 55, 0) + 1282 bytes
  [23] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 921, 13, 0) + 39 bytes
  [24] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 921, 13, 0) + 251 bytes
  [25] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x0fa45300, 0xffffffff, 0x26276090, 0) + 876 bytes
  [26] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c196f4, 3, 0x00c19754) + 466 bytes
  [27] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c196f4, 3) + 23 bytes
  [28] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c196f4, 3, 0x00c19754) + 25 bytes
  [29] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c196f4, 3, 0x00c19754) + 249 bytes
  [30] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c196f4, 3, 0x00c19754) + 420 bytes
  [31] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(2683, 0x2becf680 "code_chart_source_file_sfun", 0, 3) + 626 bytes
  [32] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 210, 10, 0) + 1282 bytes
  [33] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 210, 7, 0) + 39 bytes
  [34] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 210, 7, 0) + 251 bytes
  [35] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x722b4c00, 0xffffffff, 0x26276978, 0) + 876 bytes
  [36] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c19f3c, 3, 0x00c19f9c) + 466 bytes
  [37] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c19f3c, 3) + 23 bytes
  [38] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c19f3c, 3, 0x00c19f9c) + 25 bytes
  [39] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c19f3c, 3, 0x00c19f9c) + 249 bytes
  [40] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c19f3c, 3, 0x00c19f9c) + 420 bytes
  [41] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(2652, 0x2bbc8320 "code_chart_source_file", 0, 3) + 626 bytes
  [42] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1721, 70, 0) + 1282 bytes
  [43] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1721, 5, 0) + 39 bytes
  [44] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1721, 5, 0) + 251 bytes
  [45] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x080d8800, 0xffffffff, 0x260fbbe8, 0) + 876 bytes
  [46] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c1a784, 2, 0x00c1a7e4) + 466 bytes
  [47] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c1a784, 2) + 23 bytes
  [48] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1a784, 2, 0x00c1a7e4) + 25 bytes
  [49] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1a784, 2, 0x00c1a7e4) + 249 bytes
  [50] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1a784, 2, 0x00c1a7e4) + 420 bytes
  [51] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1703, 0x21d9ebdc "generate_code_for_charts_and_mac..", 0, 2) + 626 bytes
  [52] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 2556, 163, 0) + 1282 bytes
  [53] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 2556, 13, 0) + 39 bytes
  [54] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 2556, 13, 0) + 251 bytes
  [55] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x722b4c00, 0xffffffff, 0x260f8f60, 1) + 876 bytes
  [56] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c1afcc, 5, 0x00c1b02c) + 466 bytes
  [57] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c1afcc, 5) + 23 bytes
  [58] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1afcc, 5, 0x00c1b02c) + 25 bytes
  [59] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1afcc, 5, 0x00c1b02c) + 249 bytes
  [60] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1afcc, 5, 0x00c1b02c) + 420 bytes
  [61] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1697, 0x2b5bd4e0 "sfc", 1, 5) + 626 bytes
  [62] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 388, 309, 0) + 1282 bytes
  [63] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 388, 293, 0) + 39 bytes
  [64] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 388, 293, 0) + 251 bytes
  [65] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x01003800, 0xffffffff, 0x2af36300 "|1 zak", 2) + 876 bytes
  [66] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(2, 0x00c1b934, 6, 0x00c1b998) + 466 bytes
  [67] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 2, 0x00c1b934, 6) + 23 bytes
  [68] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c1b934, 6, 0x00c1b998) + 25 bytes
  [69] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c1b934, 6, 0x00c1b998) + 249 bytes
  [70] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c1b934, 6, 0x00c1b998) + 420 bytes
  [71] m_interpreter.dll:_inCallFcn(2, 0x00c1b934, 6, 0x00c1b998) + 84 bytes
  [72] m_interpreter.dll:_inFullFevalFcn(2, 0x00c1b934, 7, 0x00c1b994) + 234 bytes
  [73] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c1b934, 7, 0x00c1b994) + 92 bytes
  [74] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c1b934, 7, 0x00c1b994) + 247 bytes
  [75] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(311, 0x2b5bd14c "feval", 2, 7) + 626 bytes
  [76] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1133, 130, 0) + 1282 bytes
  [77] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1133, 122, 0) + 39 bytes
  [78] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1133, 122, 0) + 251 bytes
  [79] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x080e1100, 0xffffffff, 0x2af36be8 "|1 zfk", 0) + 876 bytes
  [80] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c1c238, 8, 0x00c1c1a8) + 466 bytes
  [81] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c1c238, 8) + 23 bytes
  [82] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1c238, 8, 0x00c1c1a8) + 25 bytes
  [83] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1c238, 8, 0x00c1c1a8) + 249 bytes
  [84] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c1c238, 8, 0x00c1c1a8) + 420 bytes
  [85] m_interpreter.dll:public: void __thiscall ResolverFunctionDesc::CallFunction(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(0, 0x00c1c238, 8, 0x00c1ca00) + 81 bytes
  [86] m_interpreter.dll:public: bool __thiscall Resolver::CallMFunction(int,int,class _m_operand * const,union m_operand_storage *,int,class _m_operand * const,union m_operand_storage *,int *)(0x00c1c4c8, 0, 1, 0x2b77af60) + 1209 bytes
  [87] m_interpreter.dll:private: bool __thiscall accelImpl::MFunctionCall(struct _accelOp * *)(0x00c1ca14 "À[§+", 0xffffffff, 0x2b562d50, 0xffffffff) + 545 bytes
  [88] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelImpl::Exec(void)(0x00c1ca00, 0xffffffff, 0x2ba32d80, 0xffffffff) + 170 bytes
  [89] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelCode::Call(enum inMarshalType *,int *)const (0x00c1ccd8, 0xffffffff, 0, 0) + 133 bytes
  [90] m_interpreter.dll:public: static bool __cdecl inJit::ExecuteHotSegment(struct _inJitAccelInfo *,enum opcodes *,int *,int *)(0x00c1cea0 "À\²!`ÏÁ", 0x00c1cff0, 0x00c1cf94, 0x00c1d170) + 2529 bytes
  [91] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1476, 62, 0) + 797 bytes
  [92] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1476, 8, 0) + 39 bytes
  [93] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1476, 8, 0) + 251 bytes
  [94] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x0fa45300, 0xffffffff, 0x21b25cc0, 1) + 876 bytes
  [95] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c1d580, 7, 0x00c1d4f0) + 466 bytes
  [96] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c1d580, 7) + 23 bytes
  [97] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1d580, 7, 0x00c1d4f0) + 25 bytes
  [98] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1d580, 7, 0x00c1d4f0) + 249 bytes
  [99] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1d580, 7, 0x00c1d4f0) + 420 bytes
  [100] m_interpreter.dll:public: void __thiscall ResolverFunctionDesc::CallFunction(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(1, 0x00c1d580, 7, 0x00c1dd48 "\àÁ") + 81 bytes
  [101] m_interpreter.dll:public: bool __thiscall Resolver::CallMFunction(int,int,class _m_operand * const,union m_operand_storage *,int,class _m_operand * const,union m_operand_storage *,int *)(0x00c1d810, 1, 1, 0x2bb76f30) + 1209 bytes
  [102] m_interpreter.dll:private: bool __thiscall accelImpl::MFunctionCall(struct _accelOp * *)(0x00c1dd5c, 0xffffffff, 0x2abb7ed0, 0xffffffff) + 545 bytes
  [103] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelImpl::Exec(void)(0x00c1dd48 "\àÁ", 0xffffffff, 0x2b9c0588, 0xffffffff) + 170 bytes
  [104] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelCode::Call(enum inMarshalType *,int *)const (0x00c1e020, 0xffffffff, 0, 0) + 133 bytes
  [105] m_interpreter.dll:public: static bool __cdecl inJit::ExecuteHotSegment(struct _inJitAccelInfo *,enum opcodes *,int *,int *)(0x00c1e1e8 "À7ò*¨âÁ", 0x00c1e338, 0x00c1e2dc, 0x00c1e4b8) + 2529 bytes
  [106] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1470, 191, 0) + 797 bytes
  [107] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1470, 73, 0) + 39 bytes
  [108] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1470, 73, 0) + 251 bytes
  [109] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x0fa45300, 0xffffffff, 0x2af237c0 "|1 zËj", 1) + 876 bytes
  [110] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c1e8c8, 5, 0x00c1e838) + 466 bytes
  [111] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c1e8c8, 5) + 23 bytes
  [112] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1e8c8, 5, 0x00c1e838) + 25 bytes
  [113] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1e8c8, 5, 0x00c1e838) + 249 bytes
  [114] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1e8c8, 5, 0x00c1e838) + 420 bytes
  [115] m_interpreter.dll:public: void __thiscall ResolverFunctionDesc::CallFunction(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(1, 0x00c1e8c8, 5, 0x00c1f090 "¤óÁ") + 81 bytes
  [116] m_interpreter.dll:public: bool __thiscall Resolver::CallMFunction(int,int,class _m_operand * const,union m_operand_storage *,int,class _m_operand * const,union m_operand_storage *,int *)(0x00c1eb58, 1, 1, 0x2b652878) + 1209 bytes
  [117] m_interpreter.dll:private: bool __thiscall accelImpl::MFunctionCall(struct _accelOp * *)(0x00c1f0a4 "@t=+", 0xffffffff, 0x2abb9ec8, 0xffffffff) + 545 bytes
  [118] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelImpl::Exec(void)(0x00c1f090 "¤óÁ", 0xffffffff, 0x2b287ff8, 0xffffffff) + 170 bytes
  [119] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelCode::Call(enum inMarshalType *,int *)const (0x00c1f368, 0xffffffff, 0, 0) + 133 bytes
  [120] m_interpreter.dll:public: static bool __cdecl inJit::ExecuteHotSegment(struct _inJitAccelInfo *,enum opcodes *,int *,int *)(0x00c1f530, 0x00c1f680, 0x00c1f624, 0x00c1f800) + 2529 bytes
  [121] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 497, 53, 0) + 797 bytes
  [122] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 497, 20, 0) + 39 bytes
  [123] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 497, 20, 0) + 251 bytes
  [124] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x0fa45300, 0xffffffff, 0x260f5498, 1) + 876 bytes
  [125] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c1fc10, 5, 0x00c1fb80) + 466 bytes
  [126] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c1fc10, 5) + 23 bytes
  [127] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1fc10, 5, 0x00c1fb80) + 25 bytes
  [128] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1fc10, 5, 0x00c1fb80) + 249 bytes
  [129] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c1fc10, 5, 0x00c1fb80) + 420 bytes
  [130] m_interpreter.dll:public: void __thiscall ResolverFunctionDesc::CallFunction(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(1, 0x00c1fc10, 5, 0x00c203d8) + 81 bytes
  [131] m_interpreter.dll:public: bool __thiscall Resolver::CallMFunction(int,int,class _m_operand * const,union m_operand_storage *,int,class _m_operand * const,union m_operand_storage *,int *)(0x00c1fea0, 1, 1, 0x2aeaea28) + 1209 bytes
  [132] m_interpreter.dll:private: bool __thiscall accelImpl::MFunctionCall(struct _accelOp * *)(0x00c203ec "ÈEË'", 0xffffffff, 0x2aa35c40, 0xffffffff) + 545 bytes
  [133] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelImpl::Exec(void)(0x00c203d8, 0xffffffff, 0x2aa6e400, 0xffffffff) + 170 bytes
  [134] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelCode::Call(enum inMarshalType *,int *)const (0x00c206b0, 0xffffffff, 0, 0) + 133 bytes
  [135] m_interpreter.dll:public: static bool __cdecl inJit::ExecuteHotSegment(struct _inJitAccelInfo *,enum opcodes *,int *,int *)(0x00c20878, 0x00c209c8, 0x00c2096c, 0x00c20b48) + 2529 bytes
  [136] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 2185, 96, 0) + 797 bytes
  [137] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 2185, 8, 0) + 39 bytes
  [138] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 2185, 8, 0) + 251 bytes
  [139] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0, 0xffffffff, 0x260f5660, 0) + 876 bytes
  [140] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c20f58, 3, 0x00c20ec8) + 466 bytes
  [141] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c20f58, 3) + 23 bytes
  [142] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c20f58, 3, 0x00c20ec8) + 25 bytes
  [143] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c20f58, 3, 0x00c20ec8) + 249 bytes
  [144] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c20f58, 3, 0x00c20ec8) + 420 bytes
  [145] m_interpreter.dll:public: void __thiscall ResolverFunctionDesc::CallFunction(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(0, 0x00c20f58, 3, 0x00c21720) + 81 bytes
  [146] m_interpreter.dll:public: bool __thiscall Resolver::CallMFunction(int,int,class _m_operand * const,union m_operand_storage *,int,class _m_operand * const,union m_operand_storage *,int *)(0x00c211e8, 0, 1, 0x2aead6c0) + 1209 bytes
  [147] m_interpreter.dll:private: bool __thiscall accelImpl::MFunctionCall(struct _accelOp * *)(0x00c21734, 0xffffffff, 0x27553b68 " ³÷) ³÷)(³÷)à³÷)Ð´÷)8¶÷)8¶÷)", 0xffffffff) + 545 bytes
  [148] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelImpl::Exec(void)(0x00c21720, 0xffffffff, 0x274e2ec0, 0xffffffff) + 170 bytes
  [149] m_interpreter.dll:public: enum jitReturnFlags __thiscall accelCode::Call(enum inMarshalType *,int *)const (0x00c219f8, 0xffffffff, 0, 0) + 133 bytes
  [150] m_interpreter.dll:public: static bool __cdecl inJit::ExecuteHotSegment(struct _inJitAccelInfo *,enum opcodes *,int *,int *)(0x00c21bc0, 0x00c21d10, 0x00c21cb4, 0x00c21e90) + 2529 bytes
  [151] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1588, 122, 0) + 797 bytes
  [152] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1588, 9, 0) + 39 bytes
  [153] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1588, 9, 0) + 251 bytes
  [154] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x00c22600, 0xffffffff, 0x21b295c0, 1) + 876 bytes
  [155] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c235ec, 3, 0x00c22c14) + 466 bytes
  [156] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c235ec, 3) + 23 bytes
  [157] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 3, 0x00c22c14) + 25 bytes
  [158] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 3, 0x00c22c14) + 249 bytes
  [159] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 3, 0x00c22c14) + 420 bytes
  [160] m_interpreter.dll:_inCallFcn(1, 0x00c235ec, 3, 0x00c22c14) + 84 bytes
  [161] m_interpreter.dll:public: virtual int __thiscall InterpBridge::CallFcnWithTrap(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const,char const *,bool)(1, 0x00c235ec, 3, 0x00c22c14) + 104 bytes
  [162] m_interpreter.dll:_inMexCallMATLAB(1, 0x00c23501 "5Â", 3, 0x00c22c14) + 136 bytes
  [163] libmex.dll:_mexCallMATLAB(1, 0x00c235ec, 3, 0x00c22c14) + 41 bytes
  [164] stateflow.dll:0x286b16d0(1, 0x00c235ec, 3, 0x00c22c14)
  [165] stateflow.dll:0x285ed065(167, 1, 0x00c235ec, 4)
  [166] stateflow.dll:0x286b7e70(1, 0x00c235ec, 5, 0x00c22c0c)
  [167] stateflow.dll:0x285ebd77(1, 0x00c235ec, 0x00c22c0c, 0x22242550)
  [168] stateflow.dll:0x285ebdba(1, 0x00c235ec, 5, 0x00c22c0c)
  [169] libmex.dll:_mexRunMexFile(1, 0x00c235ec, 5, 0x00c22c0c) + 132 bytes
  [170] libmex.dll:private: void __thiscall Mfh_mex::runMexFileWithSignalProtection(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 5, 0x00c22c0c) + 73 bytes
  [171] libmex.dll:public: virtual void __thiscall Mfh_mex::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 5, 0x00c22c0c) + 321 bytes
  [172] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 5, 0x00c22c0c) + 249 bytes
  [173] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 5, 0x00c22c0c) + 420 bytes
  [174] m_interpreter.dll:_inCallFcn(1, 0x00c235ec, 5, 0x00c22c0c) + 84 bytes
  [175] m_interpreter.dll:public: virtual int __thiscall InterpBridge::CallFcnWithTrap(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const,char const *,bool)(1, 0x00c235ec, 5, 0x00c22c0c) + 104 bytes
  [176] m_interpreter.dll:_inMexCallMATLAB(1, 0x00c23501 "5Â", 5, 0x00c22c0c) + 136 bytes
  [177] libmex.dll:_mexCallMATLAB(1, 0x00c235ec, 5, 0x00c22c0c) + 41 bytes
  [178] stateflow.dll:0x286b18c0(1, 0x00c235ec, 3, 0x00c235d8)
  [179] stateflow.dll:0x285edb6c(120, 1, 0x00c235ec, 3)
  [180] stateflow.dll:0x286b7e70(1, 0x00c235ec, 4, 0x00c235d4)
  [181] stateflow.dll:0x285ebd77(1, 0x00c235ec, 0x00c235d4, 0x22242550)
  [182] stateflow.dll:0x285ebdba(1, 0x00c235ec, 4, 0x00c235d4)
  [183] libmex.dll:_mexRunMexFile(1, 0x00c235ec, 4, 0x00c235d4) + 132 bytes
  [184] libmex.dll:private: void __thiscall Mfh_mex::runMexFileWithSignalProtection(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 4, 0x00c235d4) + 73 bytes
  [185] libmex.dll:public: virtual void __thiscall Mfh_mex::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 4, 0x00c235d4) + 321 bytes
  [186] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 4, 0x00c235d4) + 249 bytes
  [187] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c235ec, 4, 0x00c235d4) + 420 bytes
  [188] m_interpreter.dll:_inCallFcn(1, 0x00c235ec, 4, 0x00c235d4) + 84 bytes
  [189] sl_services.dll:protected: virtual void __thiscall CallFcn_MLCommand::operator()(void)(1, 0x6ffd2bc4, 1, 0x00c235ec) + 26 bytes
  [190] sl_services.dll:class slsvDiagnosticImpl * __cdecl slsvFEVAL_NoThrow(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const,char const *,bool)(1, 0x00c235ec, 4, 0x00c235d4) + 84 bytes
  [191] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl callSlSfCommand(struct slBlockDiagram_tag *,double,char const *,void *)(0x27db9358, 0, 0x40310000, 0x6ecd9158 "compile_post_propagation") + 166 bytes
  [192] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl slNotifyStateflowModel(struct slBlockDiagram_tag *,char const *)(0x27db9358, 0x6ecd9158 "compile_post_propagation", 0x2b36d800 "Ø6J/0ÔU/", 0x2e46c200 "ÜMÎn") + 140 bytes
  [193] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl sleCompileBlockDiagram(struct slBlockDiagram_tag *,bool,bool,enum SimType,struct mxArray_tag *)(0x27db9358, 0, 0, 4) + 8988 bytes
  [194] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl GetBlockDiagramModelType(class slModel *,struct sleInitModelContext *,bool,bool)(0x00c23818, 0, 0, 0x062342b8) + 2132 bytes
  [195] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl sleInitModel(class slModel *,struct sleInitModelContext,bool,bool)(0x00c237b8, 4, 0xffffffff, 0) + 287 bytes
  [196] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl DoRTWGen(struct RTWInfo *,struct mxArray_tag *,int,struct mxArray_tag * * const)(0x00c238f0, 0x080ea470, 3, 0x00c23bb4) + 685 bytes
  [197] libmwsimulink.dll:void __cdecl sleRTWGen(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(3, 0x00c23bb4, 13, 0x00c23c14) + 189 bytes
  [198] libmwsimulink.dll:void __cdecl slFullRTWGen(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(3, 0x00c23bb4, 13, 0x00c23c14) + 82 bytes
  [199] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(3, 0x00c23bb4, 13, 0x00c23c14) + 92 bytes
  [200] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(3, 0x00c23bb4, 13, 0x00c23c14) + 247 bytes
  [201] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(629, 0x262240e8 "rtwgen", 3, 13) + 626 bytes
  [202] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 4772, 160, 0) + 1282 bytes
  [203] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 4772, 76, 0) + 39 bytes
  [204] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 4772, 76, 0) + 251 bytes
  [205] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x722b4c00, 0xffffffff, 0x216eb2c8, 1) + 876 bytes
  [206] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c243fc, 10, 0x00c2445c) + 466 bytes
  [207] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c243fc, 10) + 23 bytes
  [208] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c243fc, 10, 0x00c2445c) + 25 bytes
  [209] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c243fc, 10, 0x00c2445c) + 249 bytes
  [210] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c243fc, 10, 0x00c2445c) + 420 bytes
  [211] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1568, 0x22440154 "tlc_c", 1, 10) + 626 bytes
  [212] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 3436, 227, 0) + 1282 bytes
  [213] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 3436, 8, 0) + 39 bytes
  [214] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 3436, 8, 0) + 251 bytes
  [215] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x00c24b00, 0xffffffff, 0x216eaf38, 1) + 876 bytes
  [216] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c24e18, 3, 0x2c253b18) + 466 bytes
  [217] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c24e18, 3) + 23 bytes
  [218] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2c253b18) + 25 bytes
  [219] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2c253b18) + 249 bytes
  [220] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2c253b18) + 420 bytes
  [221] udd_mi.dll:public: void __thiscall ExternalMethodInfo::invokeMethodDirect(bool,class UDMethodSignature *,int *,void * *,int,void * *,class UDErrorStatus *)(0, 0x219229d8, 0x00c24cf8, 0x00c24e18) + 463 bytes
  [222] udd_mi.dll:bool __cdecl ouCallMethodWithErrorTrap(class UDMethodInfo *,struct mxArray_tag *,int,struct mxArray_tag * * const,int,struct mxArray_tag const * * const,class Exception * *)(0x21618378, 0x080fa700, 1, 0x00c24e18) + 480 bytes
  [223] udd_mi.dll:bool __cdecl ouCallMethod(struct mxArray_tag *,struct mxArray_tag *,int,struct mxArray_tag * * const,int,struct mxArray_tag const * * const)(0, 0x080fa700, 1, 0x00c24e18) + 182 bytes
  [224] mcos.dll:public: virtual void __thiscall Mfh_opaque_dynamic::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2f4a3550) + 148 bytes
  [225] m_dispatcher.dll:public: virtual void __thiscall Mfh_MATLAB_fn::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2f4a3550) + 399 bytes
  [226] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c24e18, 3, 0x2f4a3550) + 420 bytes
  [227] m_interpreter.dll:_inOpaqueReferenceFcn(0x2f4a4af0 "make_rtw", 0x00fff9c0, 0x2f4a3b90, 1) + 276 bytes
  [228] m_interpreter.dll:_inOpaqueStructureReferenceOrAssignment(0x080fa700, 0, 0x00c2556c, 0x00c25758) + 928 bytes
  [229] m_interpreter.dll:_inStructureReference(0x080fa700, 1, 0x00c2556c, 0x00c2574c) + 139 bytes
  [230] m_interpreter.dll:_inComplexReference(1, 0, 0x080fa700, 2) + 126 bytes
  [231] m_interpreter.dll:_inMatRefDispatch(36, 0x73746e00, 1, 0) + 709 bytes
  [232] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 58, 22, 0) + 1032 bytes
  [233] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 58, 18, 0) + 39 bytes
  [234] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 58, 18, 0) + 251 bytes
  [235] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x722b4c00, 0xffffffff, 0x1f3590f0, 0) + 876 bytes
  [236] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c25fa4, 2, 0x00c26004) + 466 bytes
  [237] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c25fa4, 2) + 23 bytes
  [238] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c25fa4, 2, 0x00c26004) + 25 bytes
  [239] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c25fa4, 2, 0x00c26004) + 249 bytes
  [240] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c25fa4, 2, 0x00c26004) + 420 bytes
  [241] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1552, 0x2179eaac "make_rtw", 0, 2) + 626 bytes
  [242] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 449, 5, 0) + 1282 bytes
  [243] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 449, 4, 0) + 39 bytes
  [244] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 449, 4, 0) + 251 bytes
  [245] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0, 0xffffffff, 0x216ea488, 0) + 876 bytes
  [246] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c2690c, 2, 0x00c26970) + 466 bytes
  [247] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c2690c, 2) + 23 bytes
  [248] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2690c, 2, 0x00c26970) + 25 bytes
  [249] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2690c, 2, 0x00c26970) + 249 bytes
  [250] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2690c, 2, 0x00c26970) + 420 bytes
  [251] m_interpreter.dll:_inCallFcn(0, 0x00c2690c, 2, 0x00c26970) + 84 bytes
  [252] m_interpreter.dll:_inFullFevalFcn(0, 0x00c2690c, 3, 0x00c2696c) + 234 bytes
  [253] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2690c, 3, 0x00c2696c) + 92 bytes
  [254] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2690c, 3, 0x00c2696c) + 247 bytes
  [255] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(311, 0x2183d030 "feval", 0, 3) + 626 bytes
  [256] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 495, 88, 0) + 1282 bytes
  [257] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 495, 47, 0) + 39 bytes
  [258] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 495, 47, 0) + 251 bytes
  [259] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x011c0000 "¦h}Ì)9", 0xffffffff, 0x216e3618 "|1 z#f", 1) + 876 bytes
  [260] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c27274, 2, 0x00c272d8) + 466 bytes
  [261] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c27274, 2) + 23 bytes
  [262] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27274, 2, 0x00c272d8) + 25 bytes
  [263] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27274, 2, 0x00c272d8) + 249 bytes
  [264] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27274, 2, 0x00c272d8) + 420 bytes
  [265] m_interpreter.dll:_inCallFcn(1, 0x00c27274, 2, 0x00c272d8) + 84 bytes
  [266] m_interpreter.dll:_inFullFevalFcn(1, 0x00c27274, 3, 0x00c272d4) + 234 bytes
  [267] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27274, 3, 0x00c272d4) + 92 bytes
  [268] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27274, 3, 0x00c272d4) + 247 bytes
  [269] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(311, 0x2183d030 "feval", 1, 3) + 626 bytes
  [270] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 101, 6, 0) + 1282 bytes
  [271] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 101, 0, 0) + 39 bytes
  [272] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 101, 0, 0) + 251 bytes
  [273] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x080e3500, 0xffffffff, 0x1f783198, 1) + 876 bytes
  [274] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c27abc, 3, 0x00c27b1c) + 466 bytes
  [275] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c27abc, 3) + 23 bytes
  [276] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27abc, 3, 0x00c27b1c) + 25 bytes
  [277] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27abc, 3, 0x00c27b1c) + 249 bytes
  [278] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c27abc, 3, 0x00c27b1c) + 420 bytes
  [279] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1501, 0x21507c4c "build_target", 1, 3) + 626 bytes
  [280] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 512, 51, 0) + 1282 bytes
  [281] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 512, 11, 0) + 39 bytes
  [282] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 512, 11, 0) + 251 bytes
  [283] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0, 0xffffffff, 0x1f783360, 1) + 876 bytes
  [284] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(1, 0x00c28304, 2, 0x00c28364) + 466 bytes
  [285] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 1, 0x00c28304, 2) + 23 bytes
  [286] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c28304, 2, 0x00c28364) + 25 bytes
  [287] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c28304, 2, 0x00c28364) + 249 bytes
  [288] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(1, 0x00c28304, 2, 0x00c28364) + 420 bytes
  [289] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1419, 0x1ebc3da0 "build_standalone_rtw_target", 1, 2) + 626 bytes
  [290] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 1751, 473, 0) + 1282 bytes
  [291] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1751, 348, 0) + 39 bytes
  [292] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 1751, 348, 0) + 251 bytes
  [293] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x08102300, 0xffffffff, 0x22c92a48 "|1 z«e", 2) + 876 bytes
  [294] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(2, 0x00c28b4c, 4, 0x00c28bac) + 466 bytes
  [295] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 2, 0x00c28b4c, 4) + 23 bytes
  [296] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c28b4c, 4, 0x00c28bac) + 25 bytes
  [297] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c28b4c, 4, 0x00c28bac) + 249 bytes
  [298] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(2, 0x00c28b4c, 4, 0x00c28bac) + 420 bytes
  [299] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(1424, 0x1ebc3fa0 "loc_codegenentry", 2, 4) + 626 bytes
  [300] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 3226, 278, 0) + 1282 bytes
  [301] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 3226, 12, 0) + 39 bytes
  [302] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 3226, 12, 0) + 251 bytes
  [303] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x00c29800, 0xffffffff, 0x1ee30d98, 0) + 876 bytes
  [304] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c294b4, 6, 0x00c29518) + 466 bytes
  [305] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c294b4, 6) + 23 bytes
  [306] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c294b4, 6, 0x00c29518) + 25 bytes
  [307] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c294b4, 6, 0x00c29518) + 249 bytes
  [308] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c294b4, 6, 0x00c29518) + 420 bytes
  [309] m_interpreter.dll:_inCallFcn(0, 0x00c294b4, 6, 0x00c29518) + 84 bytes
  [310] m_interpreter.dll:_inFullFevalFcn(0, 0x00c294b4, 7, 0x00c29514) + 234 bytes
  [311] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c294b4, 7, 0x00c29514) + 92 bytes
  [312] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c294b4, 7, 0x00c29514) + 247 bytes
  [313] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(311, 0x22cd7698 "feval", 0, 7) + 626 bytes
  [314] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 171, 16, 0) + 1282 bytes
  [315] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 171, 0, 0) + 39 bytes
  [316] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 171, 0, 0) + 251 bytes
  [317] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0x722b4c00, 0xffffffff, 0x1ef9f9c0, 0) + 876 bytes
  [318] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x00c29cfc, 7, 0x00c29d5c) + 466 bytes
  [319] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x00c29cfc, 7) + 23 bytes
  [320] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c29cfc, 7, 0x00c29d5c) + 25 bytes
  [321] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c29cfc, 7, 0x00c29d5c) + 249 bytes
  [322] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c29cfc, 7, 0x00c29d5c) + 420 bytes
  [323] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(892, 0x2127d34c "sl", 0, 7) + 626 bytes
  [324] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(1, 41, 62, 0) + 1282 bytes
  [325] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 41, 62, 0) + 39 bytes
  [326] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(1, 41, 62, 0) + 251 bytes
  [327] m_interpreter.dll:int __cdecl inExecuteMFunctionOrScript(class Mfh_mp *,bool)(0, 0xffffffff, 0x22c91c08, 0) + 876 bytes
  [328] m_interpreter.dll:void __cdecl inRunMfile(int,struct mxArray_tag * *,int,struct mxArray_tag * *,class Mfh_mp *,struct inWorkSpace_tag *)(0, 0x2ac1a438, 6, 0x00c2a694) + 466 bytes
  [329] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(struct _mdUnknown_workspace *,int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0, 0x2ac1a438, 6) + 23 bytes
  [330] m_interpreter.dll:public: virtual void __thiscall Mfh_mp::dispatch_file(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x2ac1a438, 6, 0x00c2a694) + 25 bytes
  [331] m_dispatcher.dll:public: virtual void __thiscall Mfh_file::dispatch_fh(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x2ac1a438, 6, 0x00c2a694) + 249 bytes
  [332] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x2ac1a438, 6, 0x00c2a694) + 420 bytes
  [333] m_interpreter.dll:_inCallFcn(0, 0x2ac1a438, 6, 0x00c2a694) + 84 bytes
  [334] sl_services.dll:protected: virtual void __thiscall CallFcn_MLCommand::operator()(void)(1, 0x6ffd2bc4, 0, 0x2ac1a438) + 26 bytes
  [335] sl_services.dll:class slsvDiagnosticImpl * __cdecl slsvFEVAL_NoThrow(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const,char const *,bool)(0, 0, 6, 0x00c2a694) + 84 bytes
  [336] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl slCallFcnWithTrappingPrompt(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const,char const *,int)(0, 0, 6, 0x00c2a694) + 71 bytes
  [337] libmwsimulink.dll:void __cdecl RTWBuildCore(struct slBlockDiagram_tag *)(0x27db9358, 0x00c2a868, 0x2afd5770, 0x00c2a714 "T§Â") + 307 bytes
  [338] libmwsimulink.dll:void __cdecl RTWSimprmGcbf(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(0, 0x00c2a804, 1, 0x00c2a868) + 271 bytes
  [339] libmwbuiltins.dll:void __cdecl bnFeatureFcn(int,struct mxArray_tag * * const,int,struct mxArray_tag * * const)(0, 0x00c2a804, 2, 0x00c2a864) + 111 bytes
  [340] m_dispatcher.dll:public: virtual void __thiscall Mfh_builtin::dispatch_mf(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2a804, 2, 0x00c2a864) + 92 bytes
  [341] m_dispatcher.dll:public: void __thiscall Mfunction_handle::dispatch(int,struct mxArray_tag * *,int,struct mxArray_tag * *)(0, 0x00c2a804, 2, 0x00c2a864) + 247 bytes
  [342] m_interpreter.dll:int __cdecl inDispatchFromStack(int,char const *,int,int)(131, 0x2f0b4044 "feature", 0, 2) + 626 bytes
  [343] m_interpreter.dll:enum opcodes __cdecl inDispatchCall(char const *,int,int,int,int *,int *)(0x2f0b4044 "feature", 131, 0, 2) + 107 bytes
  [344] m_interpreter.dll:int __cdecl inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag volatile *,int *)(0, 0, 0, 0) + 6048 bytes
  [345] m_interpreter.dll:int __cdecl protected_inInterp(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(0, 0, 0, 0) + 39 bytes
  [346] m_interpreter.dll:int __cdecl inInterPcodeSJ(enum inDebugCheck,int,int,enum opcodes,struct inPcodeNest_tag *,int *)(0, 0, 0, 0) + 251 bytes
  [347] m_interpreter.dll:_inInterPcode(0, 0x00c2af64, 0x00c2ade0 "p®Â", 0) + 92 bytes
  [348] m_interpreter.dll:enum inExecutionStatus __cdecl in_local_call_eval_function(int *,struct _pcodeheader *,int *,struct mxArray_tag * * const,enum inDebugCheck,bool)(0, 0x00c2af64, 0, 0) + 189 bytes
  [349] m_interpreter.dll:enum inExecutionStatus __cdecl inEvalStringWithIsVarFcn(struct _memory_context *,char const *,enum EvalType,int,struct mxArray_tag * * const,enum inDebugCheck,struct _pcodeheader *,int *,bool (__cdecl*)(void *,char const *),void *,bool,bool)(0x7b9dd604, 0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0) + 484 bytes
  [350] m_interpreter.dll:enum inExecutionStatus __cdecl inEvalCmdWithLocalReturn(char const *,int *,bool,bool,bool (__cdecl*)(void *,char const *))(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0, 0) + 79 bytes
  [351] m_interpreter.dll:public: virtual enum inExecutionStatus __thiscall InterpBridge::EvalCmdWithLocalReturn(char const *,int *,bool,bool)(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0, 0) + 25 bytes
  [352] m_interpreter.dll:_inEvalCmdWithLocalReturn(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0, 0) + 30 bytes
  [353] m_interpreter.dll:public: virtual enum inExecutionStatus __thiscall InterpBridge::EvalCmd(char const *,bool)(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0x00c2b060, 0x6ffb5fcc) + 35 bytes
  [354] m_interpreter.dll:_inEvalCmd(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 0, 0x6ffb6f5a, 0x0fb147a0) + 24 bytes
  [355] sl_services.dll:protected: virtual void __thiscall EvalCmd_MLCommand::operator()(void)(1, 0x6ffd2bd8 "pcûo _ûo", 0, 0) + 12 bytes
  [356] sl_services.dll:class slsvDiagnosticImpl * __cdecl slsvEVAL_NoThrow(char const *,bool)(0x2aa333b0 "try\nfeature('RTWBuild',get_para", 1, 0x1eb5ea60 "controlMCUSlugsMKII/Inner Loop//..", 9) + 63 bytes
  [357] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl EvalCmd(char const *,struct inWorkSpace_tag *)(0x261acf28 "try\nfeature('RTWBuild',get_para", 0x0fb147a0, 19, 0x2a14bb50) + 63 bytes
  [358] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl slCallCallbackWithType(void *,char const *,int,enum CBGraphValidity,enum CBWkSpType)(0x261d5cd8, 0x261acf28 "try\nfeature('RTWBuild',get_para", 19, 1) + 601 bytes
  [359] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl BlockCallback(class slBlock *,int)(0x261d5cd8, 0x00c2b1c0, 0x00c2b180, 0x6e6e4c65) + 70 bytes
  [360] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl BlockOpenCallback(class slBlock *)(0x261d5cd8, 0x261acf29 "ry\nfeature('RTWBuild',get_param", 0, 0x405d8010) + 18 bytes
  [361] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl BlockOpenOpenFcn(class slBlock * *,struct BlockOpenRec *)(0x00c2b228, 0, 0x261d5cd8, 0x00c2b228) + 21 bytes
  [362] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl BlockOpenDefault(class slBlock * *,struct BlockOpenRec *)(0x00c2b1c0, 0x00c2b228, 0x7be8f460, 0x261d5cd8) + 58 bytes
  [363] libmwsimulink.dll:class slsvDiagnosticImpl * __cdecl BlockOpen(class slBlock *,struct BlockOpenRec *)(0x261d5cd8, 0x00c2b228, 0x29f8d468, 4) + 89 bytes
  [364] libmwsimulink.dll:void __cdecl BlockOpenFromUI(class slBlock *,struct slGraph_tag const *,struct BlockOpenRec *)(0x261d5cd8, 0x2a40de70, 0x00c2b228, 0x29f8d468) + 78 bytes
  [365] libmwsimulink.dll:void __cdecl DefaultBlockHandleClickFcn(struct slGraph_tag *,class slBlock *,class SlEvent *,struct mwpoint *)(0x2a40de70, 0x261d5cd8, 0x2249adc0, 0x00c2b304) + 740 bytes
  [366] libmwsimulink.dll:void __cdecl BlockHandleClick(struct slGraph_tag *,class slBlock *,void *,struct mwpoint *)(0x2a40de70, 0x261d5cd8, 0x2249adc0, 0x00c2b304) + 30 bytes
  [367] libmwsimulink.dll:void __cdecl bdeButtonDownFcn(struct WinRec_tag *,class SlEvent *)(0x29f8d468, 0x2249adc0, 0x29f8d468, 0x00c2b33c "h³Â") + 745 bytes
  [368] libmwsimulink.dll:public: static void __cdecl SlUserEvent::sendUserEvent(void (__cdecl*)(struct WinRec_tag *,class SlEvent *),struct WinRec_tag *,void *)(0x6e142bd0, 0x29f8d468, 0x00c2b384, 0x00c2b368 "¨³Â") + 205 bytes
  [369] libmwsimulink.dll:_bdeButtonDownWrapper(0x29f8d468, 0x00c2b384, 0x29f8d468, 3408078) + 21 bytes
  [370] libmwgui.dll:void __cdecl wm_ButtondownFcn(struct WinRec_tag *,void *)(0x29f8d468, 0x00c2b384, 0x29e93d00, 0x6e8cbef0) + 67 bytes
  [371] libmwsimulink.dll:protected: void __thiscall CMdlView::OnLButtonDblClk(unsigned int,class CPoint)(1, 206, 52, 0x7d73bbe0) + 126 bytes
  [372] MFC80.DLL:0x00de2cd8(515, 1, 3408078, 0x00c2b474)
  [373] MFC80.DLL:0x00de277e(515, 1, 3408078, 0x7d73bcc0)
  [374] MFC80.DLL:0x00de1514(0, 525174, 515, 1)
  [375] MFC80.DLL:0x00de172a(525174, 515, 1, 3408078)
  [376] libmwsimulink.dll:long __stdcall AfxWndProcDllStatic(struct HWND__ *,unsigned int,unsigned int,long)(525174, 515, 1, 3408078) + 51 bytes
  [377] USER32.dll:0x769d86ef(0x6e9afe7f, 525174, 515, 1)
  [378] USER32.dll:0x769d8876(1292564, 0x6e9afe7f, 525174, 515)
  [379] USER32.dll:0x769d89b5(0x6e9afe7f, 1, 0x00c2b6d0 "à¶Â", 0x7b22ec0e)
  [380] USER32.dll:0x769d3578(0x00c2b694, 0x7b2967b0 "H8&amp;{", 0, 0x7c1322f0)
  [381] uiw.dll:char * __cdecl getCommand(char *,int)(0x7e86b988, 4096, 0x00c2b730 "¬·Â", 0x7e857bbf) + 606 bytes
  [382] uiw.dll:public: virtual char * __thiscall uiw::UIW_IOProxy::getCmdWindowCommand(char *,int)const (0x7e86b988, 4096, 0, 0) + 16 bytes
  [383] libmwbridge.dll:char * __cdecl winReadStdin(char * const,unsigned int,bool)(0x7e86b988, 4096, 0, 0x00c2f8d4) + 79 bytes
  [384] libmwbridge.dll:char * __cdecl ioReadLineOS(bool,struct _iobuf * const,char * const,char * const,int,bool * const,void (__cdecl*const)(void),char * (__cdecl*const)(char * const,unsigned int,bool))(0, 0x72341b78 "@I4r", 0x1d19d4a0, 4096) + 265 bytes
  [385] libmwbridge.dll:char * __cdecl ioReadLine(bool,struct _iobuf *,char *,char *,int,bool *)(0, 0x72341b78 "@I4r", 0x1d19d4a0, 0x1d19d4a0) + 99 bytes
  [386] libmwbridge.dll:void __cdecl mnGetFullLine(char * *,unsigned int *,unsigned int *,bool)(0x00c2f8d8, 0x00c2f8cc, 0, 0x7b95ab70) + 205 bytes
  [387] libmwbridge.dll:_mnGetCommandLineBuffer(0, 0, 0x0fbdc488, 0) + 124 bytes
  [388] libmwbridge.dll:__catch$_mnParser$0(0x0109ffd8, 0, 0x0d0c4601, 1) + 164 bytes
  [389] mcr.dll:private: void __thiscall mcrInstance::mnParser_on_interpreter_thread(void)(0x0fbdc4c0, 0x084ae39c, 10, 0x00c2fb98) + 51 bytes
  [390] mcr.dll:public: void __thiscall boost::function0&lt;void&gt;::operator()(void)const (0, 0x0fbdc488, 0, 0x0fbdc488) + 63 bytes
  [391] mcr.dll:public: virtual void __thiscall mcr::runtime::InterpreterThread::Impl::NoResultInvocationRequest::run(void)(0x7a0ee820, 0x083a3c00 "¬±Íy", 0x00c2fa20, 0) + 53 bytes
  [392] mcr.dll:private: static void __cdecl mcr::runtime::InterpreterThread::Impl::invocation_request_handler(int)(0x0fbdc488, 0, 0x00030000 "Actx ", 0x00c2fb9c) + 40 bytes
  [393] uiw.dll:bool __cdecl UIW_DispatchUserMessage(int,int)(9223, 0x0fbdc488, 0x00c2fb9c, 3) + 81 bytes
  [394] uiw.dll:long __stdcall HandleUserMsgHook(int,unsigned int,long)(0, 1, 0x00c2fb9c, 9223) + 95 bytes
  [395] USER32.dll:0x769f6e6e(0x00030000 "Actx ", 1, 0x00c2fb9c, 0x7b2563e0)
  [396] USER32.dll:0x769d31eb(0x00c2fb8c, 0x00c2fb9c, 0x00c2fbb8, 0)
  [397] USER32.dll:0x769d4260(0x00c2fb8c, 48, 0x00c2fc98 "ÔüÂ", 0x771e63e0)
  [398] ntdll.dll:0x771e642e(0x00c2fc08, 0, 0, 0)
  [399] uiw.dll:void __cdecl UIW_GetAndDispatchMessage(struct tagMSG *)(0x00c2fc08, 0x010ba268, 0, 0x00c2fc50 "hüÂ") + 20 bytes
  [400] uiw.dll:void __cdecl UIW_GetAndDispatchMessage(void)(0x0fc0e640, 0x0fc0e638, 0, 9223) + 15 bytes
  [401] uiw.dll:public: virtual void __thiscall uiw_ppeHook::pollingDuringFcn(bool)(0, 0, 0x00c2fcd2, 0x0fc0e638) + 53 bytes
  [402] libuij.dll:struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; __cdecl std::for_each&lt;class std::_Vector_iterator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *,class std::allocator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; &gt;,struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; &gt;(class std::_Vector_iterator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *,class std::allocator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; &gt;,class std::_Vector_iterator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *,class std::allocator&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; &gt;,struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt;)(0x00c2fcd2, 0x0fc0e638, 0x0fc0e640, 0) + 41 bytes
  [403] libuij.dll:struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; __cdecl sysq::ppe_for_each&lt;struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt; &gt;(struct sysq::during_F&lt;class sysq::wsfcn_proxy&lt;class sysq::ws_ppeHook *&gt; *&gt;)(0x00c2fcd2, 0, 0x010a1288, 0x7b990f43) + 70 bytes
  [404] libuij.dll:void __cdecl sysq::ppeMainLoop(int,int,bool)(1, 0xffffffff, 0, 2) + 243 bytes
  [405] libuij.dll:void __cdecl sysq::ppeLoopIfOK(int,int,bool)(1, 0xffffffff, 0, 0) + 118 bytes
  [406] libuij.dll:void __cdecl sysq::processPendingEvents(int,int,bool)(1, 0xffffffff, 0, 0x00c2fd90 "ÐýÂ") + 100 bytes
  [407] libuij.dll:void __cdecl UIJ_WS_ProcessPendingEvents(int,int)(1, 0xffffffff, 0x010a1288, 0x0109a1d8) + 18 bytes
  [408] mcr.dll:public: void __thiscall mcr::runtime::InterpreterThread::Impl::process_events(class boost::shared_ptr&lt;class mcr::runtime::InterpreterThread::Impl&gt; const &amp;)(0x00c2fde8, 2, 0x0109faa8, 0x03dcdd60) + 138 bytes
  [409] mcr.dll:__catch$?run@Impl@InterpreterThread@runtime@mcr@@QAEKABV?$shared_ptr@VImpl@InterpreterThread@runtime@mcr@@@boost@@PAUinit_context@1234@@Z$0(0x00c2fde8, 0x0109d470, 0x7a0f1940, 0x0109b6a0) + 128 bytes
  [410] mcr.dll:unsigned long __cdecl run_init_and_handle_events(void *)(0x03dcdd60, 0x0040b7cc, 602478, 0) + 76 bytes
  [411] mcr.dll:private: void __thiscall mcr::runtime::InterpreterThreadFactory::runThreadFunction(void)(0x00c2fe98, 0x00c2fe54, 0x00c2fe58 "¸þÂ", 0x7b95c1bc) + 108 bytes
  [412] MATLAB.exe:public: void __thiscall boost::function0&lt;void&gt;::operator()(void)const (0, 0, 1, 0x0109b6a0) + 63 bytes
  [413] MATLAB.exe:int __cdecl mcrMain(int,char const * * const)(1, 0x0109c6b0, 4194304, 10) + 158 bytes
  [414] MATLAB.exe:_WinMain@16(4194304, 0, 602478, 10) + 109 bytes
  [415] MATLAB.exe:___tmainCRTStartup(0x7ffd8000, 0x00c2ffd4 "ìÿÂ", 0x771fb495, 0x7ffd8000) + 320 bytes
  [416] kernel32.dll:0x76871194(0x7ffd8000, 0x77e555c0, 0, 0)
  [417] ntdll.dll:0x771fb495(0x00406e06, 0x7ffd8000, 0, 0)
  [418] ntdll.dll:0x771fb468(0x00406e06, 0x7ffd8000, 0, 0x78746341)
MATLAB m-file stack trace:
&gt; In coder\private\code_sfun_glue_code at 125
  In coder\private\code_chart_source_file_sfun at 55
  In coder\private\code_chart_source_file at 10
  In coder\private\generate_code_for_charts_and_machine at 70
  In sfc at 163
  In stateflow\private\targetman&gt;code_method at 309
  In stateflow\private\targetman&gt;method_nag_wrapper at 130
  In stateflow\private\targetman at 76
  In stateflow\private\autobuild_kernel&gt;autobuild_local at 195
  In stateflow\private\autobuild_kernel at 53
  In stateflow\private\autobuild_driver at 110
  In stateflow\private\slsf at 122
  In tlc_c at 160
  In RTW.makertw.make_rtw at 227
  In make_rtw at 22
  In C:\Users\SLUG_Test\Documents\MATLAB\dsPIC Blockset\dspic\make_CreateMPLAB.p&gt;make_CreateMPLAB at 5
  In simulink\private\build_target&gt;RunBuildCmd at 88
  In simulink\private\build_target at 6
  In simulink\private\build_standalone_rtw_target at 51
  In C:\Program Files\MATLAB\R2010a\toolbox\simulink\simulink\private\slbuild_private.p&gt;loc_codegenentry at 473
  In C:\Program Files\MATLAB\R2010a\toolbox\simulink\simulink\private\slbuild_private.p&gt;slbuild_private at 278
  In sl at 16
  In slbuild at 62
Code Directory :
     "C:\Users\SLUG_Test\Documents\MATLAB\SLUG_Autopilot\slprj\_sfprj\controlMCUSlugsMKII\_self\sfun\src"
<wbr>
Machine (#17): "controlMCUSlugsMKII"  Target : "sfun"
<wbr>
<wbr>
Chart "myMux Fun1" (#18):
<wbr>
.
     "c1_controlMCUSlugsMKII.h"
<wbr>
     "c1_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "myMux Fun1" (#28):
<wbr>
.
     "c2_controlMCUSlugsMKII.h"
<wbr>
     "c2_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "myMux Fun5" (#38):
<wbr>
.
     "c3_controlMCUSlugsMKII.h"
<wbr>
     "c3_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Buffer IC Channel" (#49):
<wbr>
.
     "c4_controlMCUSlugsMKII.h"
<wbr>
     "c4_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Embedded MATLAB Function" (#56):
<wbr>
.
     "c5_controlMCUSlugsMKII.h"
<wbr>
     "c5_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Buffer IC Channel1" (#64):
<wbr>
.
     "c6_controlMCUSlugsMKII.h"
<wbr>
     "c6_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "negprotect" (#71):
<wbr>
.
     "c7_controlMCUSlugsMKII.h"
<wbr>
     "c7_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Compute  Circles" (#78):
<wbr>
.
     "c8_controlMCUSlugsMKII.h"
<wbr>
     "c8_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Embedded MATLAB Function1" (#93):
<wbr>
.
     "c9_controlMCUSlugsMKII.h"
<wbr>
     "c9_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Embedded MATLAB Function" (#100):
<wbr>
.
     "c10_controlMCUSlugsMKII.h"
<wbr>
     "c10_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "Embedded MATLAB Function1" (#112):
<wbr>
.
     "c11_controlMCUSlugsMKII.h"
<wbr>
     "c11_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "myMux Fun1" (#120):
<wbr>
.
     "c12_controlMCUSlugsMKII.h"
<wbr>
     "c12_controlMCUSlugsMKII.c"
<wbr>
<wbr>
Chart "myMux Fun2" (#128):
<wbr>
.
     "c13_controlMCUSlugsMKII.h"
<wbr>
     "c13_controlMCUSlugsMKII.c"
<wbr>
Code generation failed !errorOccurred
<wbr>
<wbr>
<wbr>
### Real-Time Workshop build procedure for model: 'controlMCUSlugsMKII' aborted due to an error.
&gt;&gt; </code></pre><br>
<br>
I attached the error window also.<br>
<br>
<a href="http://img713.imageshack.us/i/error1t.png/">http://img713.imageshack.us/img713/9108/error1t.th.png</a><br>
<br>
<a href="http://img99.imageshack.us/i/error2m.png/">http://img99.imageshack.us/img99/443/error2m.th.png</a><br>
<br>
<br>
<br>
Am I not initiating something? MATLAB isn't sucessfully compiling the model correctly so I can't try the -mlarge-data compile flag.<br>
<br>
<br>
<br>
Do have an Idea of what I am doing wrong? <br>
<br>
<br>
<br>
EDIT 11-22-10: Tried to compile the latest commit and got the same error. This has to be caused by MATLAB.<br>
<br>
Here is my compiler info, etc.<br>
<br>
OS: Windows 7 (32-bit)<br>
<br>
MATLAB: Matlab 2010a (32-bit)<br>
<br>
mex and mbuild compiler: Microsoft Visual C++ 2008 Express<br>
<br>
dsPIC Blockset V3.3a<br>
<br>
MPLAB C30 Compiler (MPLAB C Compiler for PIC24 MCUs and dsPICs v3.25 LITE Mode)<br>
<br>
MPLAB C32 Compiler (MPLAB C Compiler for PIC32 v1.1B LITE Mode)<br>
<br>
MPLAB IDE v8.60 <br>
<br>
<br>
<br>
Dan</div>
</article>

<article class="forum-post" id="p1337">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-23 12:00 UTC">2010-11-23 12:00 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hi Dan,<br>
<br>
<br>
<br>
I tested again with another configuration : <br>
<br>
<br>
<br>
OS: Windows 7 (32-bit)<br>
<br>
MATLAB: Matlab 2010a (32-bit)<br>
<br>
mex and mbuild compiler: <strong>LCC</strong><br>
<br>
dsPIC Blockset V3.3a<br>
<br>
MPLAB C30 Compiler (MPLAB C Compiler for PIC24 MCUs and dsPICs v3.24 LITE Mode)<br>
<br>
MPLAB IDE v8.60 <br>
<br>
<br>
<br>
The first attempt crash (I mean, that MATLAB crashed i.e. exit)<br>
<br>
Thus, I restarted matlab, removed the two directory created : <strong>slpjr </strong>and <strong>controlMCUSlugsMKII_dspic.</strong><br>
<br>
Then compiling went Ok (or you will get a link error if -mdata-large is not added, see previous post)<br>
<br>
HOWEVER, when I compile the model a second time, I get a matlab crash (propose to save the model and then exit) !<br>
<br>
<strong>Thus, I suspect a matlab problem with windows memory</strong>. The model might be memory consumming, the blockset may also do something wront that create the problem if memory is not sufficient ?<br>
<br>
<br>
<br>
The windows 32 system I am using has 3Go of RAM (from system properties)<br>
<br>
Test with previous windows 64 had only 2go or RAM)<br>
<br>
<br>
<br>
The difference with your configuration is only on C30 compiler and mex compiler.<br>
<br>
- The problem you get is not at compilation time. C30 Compiler should not be responsible.<br>
<br>
- The model might call mex  and the difference between LCC and visual C compiler may change something ? (change with mex-setup, provided you have LCC installed, from matlab CD)<br>
<br>
<br>
<br>
There is clearly something weird about the model file, however, It can be compiled anyway. It might be too big ? Can you try with other computer ? try also to remove some blocks of the model, that may isolate the problem and reduce memory required. Perhaps something can be configured differently with matlab memory or windows cache memory ?<br>
<br>
<br>
<br>
You could also try to create a new model, configure it properly and copy-past all blocks. Simulink model file store information about blockset that SLUG team has but that we do not have. Theses information may create problems thus copying blocks into a new model file might clean it up !<br>
<br>
<br>
<br>
I may have a look on the blockset to check if it might create such problems.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1338">
<header><strong>dambrosio</strong><time datetime="2010-11-23 16:23 UTC">2010-11-23 16:23 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Lubin,<br>
<br>
I reinstalled everything on a different computer. It compiled all the way to the following error.<br>
<pre><code>sbrk.o(.libc+0x4):C:\Users\Lubin\Desktop\SLUGS\clib\sbrk.c: Link Error: Cannot access symbol (___curbrk) with file register addressing. Value must be less than 8192. Suggest large-data model. </code></pre><br>
I then followed the directions on recompiling the mcp file and adding the -mlarge-data to the simulink model. I recompiled and got the following command window output:<br>
<pre><code>PPTPTPNumber of I/O PINs used : 8
TTPNumber of I/O PINs used : 8
TPTTTPTPTPNumber of I/O PINs used : 8
TTPTPTWarning: Input port 1 of 'controlMCUSlugsMKII/Trim Vals/Log
Trims Using PWM High [groundStationDriver.c]/Report Airspeed'
is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/[dR dE dA dT]2' is not connected. 
Warning: Output port 1 of 'controlMCUSlugsMKII/Update PWM
Commands and Send Telemetry/[dR dE dA dT]3' is not connected. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Compute
psi_dot_m/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Control
Law/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Protect
NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/State
Predictor/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/L1 Output
Feedback Controller With  Projection Operator/Trapezoidal
Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Angle Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Angle Conversion2/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Bank to Psi Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Bank to Psi Dot/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Bank to Psi Dot/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/High Pass (Washout) Filter/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/High Pass (Washout) Filter/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/High Pass (Washout) Filter/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Protect NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal
Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal
Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal
Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal Integrator/Protect
NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal Integrator/Protect
NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Roll Control [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Sideslip Compensation/Bank to Psi Dot/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Sideslip Compensation/Constant'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Sideslip Compensation/Low Pass/Compute Coef/-T'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Sideslip Compensation/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Sideslip Compensation/psi_dot to Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Protect NaNs
/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Protect
NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/Yaw Damper [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Lateral
Channel/psi_dot to Bank/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Air Density from Height/Constant 2 from Model'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Air Density from Height/Length Conversion/Unit
Conversion'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Air Density from Height/Rho_0 (Kg//m^3)'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/Trapezoidal
Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/Trapezoidal
Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/Trapezoidal
Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/Trapezoidal
Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Airspeed Hold
[PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Airspeed Hold [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Compute Airspeed/[ 0.01
50000]'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Height Error to Pitch  Command [PI]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Height Error to Pitch  Command [PI]/Trapezoidal
Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Height Error to Pitch  Command [PI]/Trapezoidal
Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Height Error to Pitch  Command [PI]/Trapezoidal
Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Height Error to Pitch  Command [PI]/Trapezoidal
Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch
Command [PI]/Trapezoidal Integrator/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch
Command [PI]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Height Error to Pitch
Command [PI]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/Gain'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/Trapezoidal
Integrator/Constant'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/Trapezoidal
Integrator/Constant1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/Trapezoidal
Integrator/Constant2'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/Trapezoidal
Integrator/Constant3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator
[PID]/Trapezoidal Integrator/Protect NaNs /Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator
[PID]/Trapezoidal Integrator/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Pitch To Elevator
[PID]/Trapezoidal Integrator/Switch1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Longitudinal
Channel/Pitch To Elevator [PID]/delayTime'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs1/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs2/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs3/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Protect NaNs4/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Schedule LPF'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Longitudinal Channel/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute Lateral
Error/Subsystem3/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Compute T
in Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute
P/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get
Circles/Compute delta Left Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get
Circles/Constant5'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Compute P/Get
Circles/compute delta Right Turn/Constant5'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS
Location/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS
Location/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Grab IC/Compute GS
Location/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line
Segment/1st WP'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line
Segment/Compute  Projection/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Compute WP Index/Switch when  in Line
Segment/Compute Total Run/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Compute
Frenet/Normalize Vector/Zero Bound'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Compute
Frenet/Normalize Vector /Zero Bound'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP1/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP1/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP1/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute
Frenet/Geod2LTP1/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP2/ECEF2LTP (UEN)/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP2/Geod2ECEF1/Deg2R'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute Frenet/Geod2LTP2/Geod2ECEF1/Deg2R1'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop// Navigation/Navigation/Get
Wps Compute
Frenet/Geod2LTP2/Geod2ECEF1/eccentricity^2/Rp=polar radius'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Get Wps Compute Frenet/Switch'. 
Warning: Parameter precision loss occurred for 'Value'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Gravity'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel
Cmd/Compute Eta/Subsystem6/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'UpperLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel
Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel
Cmd/Compute Eta/Subsystem6/[-1,1]'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel
Cmd/GainSchedule L2 and Get Groundspeed/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/Park, Deyst &amp; How Lat Accel Cmd/Park's
Lateral Accel Command/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop//
Navigation/Navigation/as_c to phi_c/Protect NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Inner Loop// Navigation/Protect
NaNs/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Trim Vals/Gain1'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Trim Vals/Gain2'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/Trim Vals/Gain3'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Update PWM Commands and Send
Telemetry/Generate PWM Signals Based on the Control Type/If
Control Type Is Selective Passthrough/Switch'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Update PWM Commands and Send
Telemetry/Generate PWM Signals Based on the Control Type/If
Control Type Is Selective Passthrough/Switch1'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Update PWM Commands and Send
Telemetry/Generate PWM Signals Based on the Control Type/If
Control Type Is Selective Passthrough/Switch2'. 
Warning: Parameter precision loss occurred for 'Threshold'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/Update PWM Commands and Send
Telemetry/Generate PWM Signals Based on the Control Type/If
Control Type Is Selective Passthrough/Switch3'. 
Warning: Parameter precision loss occurred for 'Gain'. The
parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred.
You can control this diagnostic on the Diagnostics pane of
the Configuration Parameters dialog. This originated from
'controlMCUSlugsMKII/get Nav Vars/Angle Conversion/Unit
Conversion'. 
Warning: Parameter precision loss occurred for 'UpperLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/get Nav Vars/Direction Cosine
Matrix to Euler Angles/Subsystem3/[-1,1]'. 
Warning: Parameter precision loss occurred for 'LowerLimit'.
The parameter's value cannot be represented exactly using
the run-time data type. A small quantization error has
occurred. You can control this diagnostic on the Diagnostics
pane of the Configuration Parameters dialog. This originated
from 'controlMCUSlugsMKII/get Nav Vars/Direction Cosine
Matrix to Euler Angles/Subsystem3/[-1,1]'. 
### Invoking Target Language Compiler on controlMCUSlugsMKII.rtw
### Using System Target File: C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\dspic\dspic.tlc
### Loading TLC function libraries
.......
### Initial pass through model to cache user defined code
.....................
### Caching model source code
...............................................................................
...............................................................................
...............................................................................
...............................................................................
............................................................
### Writing main
..
### Writing source file controlMCUSlugsMKII.c
.
### Writing header file controlMCUSlugsMKII_private.h
### Writing header file controlMCUSlugsMKII.h
.
### Writing header file controlMCUSlugsMKII_types.h
### Writing header file rtwtypes.h
### Writing header file rt_MAXf_snf.h
.
### Writing header file rt_zcfcn.h
### Writing source file rt_zcfcn.c
.
### Writing header file rt_nonfinite.h
### Writing source file rt_nonfinite.c
.
### Writing header file rt_SATURATE.h
### Writing header file rt_SIGNf_snf.h
.
### Writing header file rtGetInf.h
### Writing source file rtGetInf.c
.
### Writing header file rtGetNaN.h
### Writing source file rtGetNaN.c
.
### Writing source file controlMCUSlugsMKII_data.c
### Writing header file autobuild.h
### Writing source file controlMCUSlugsMKII_main.c
.
### TLC code generation complete.
..........
### Creating HTML report file controlMCUSlugsMKII_codegen_rpt.html
.### Evaluating PostCodeGenCommand specified in the model
<wbr>
     ----------------------------------------------------
     ----------------------------------------------------
Embedded Coder for dsPIC V3.3a(22-Nov-2010) for Matlab R2010a.
<wbr>
<wbr>
Licence Accorded to  Blake Mills
                     [adresse e-mail retirée]
                     University of Colorado-Boulder
                     University of Colorado at Boulder
                     xxx UCB
                     Boulder, Colorado 80309-0xxx
                     USA
<wbr>
 Facturation to :    Blake Mills
                     [adresse e-mail retirée]
<wbr>
<wbr>
<wbr>
<wbr>
<wbr>
     ----------------------------------------------------
Check updates and new informations at :  www.kerhuel.eu 
     ----------------------------------------------------
<wbr>
.
### Processing Template Makefile: C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\dspic\dspic_pic30_gcc.tmf
-- Bypassing matlab internal LCC configuration --
### Creating controlMCUSlugsMKII.mk from C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\dspic\dspic_pic30_gcc.tmf
### Building controlMCUSlugsMKII: "C:\PROGRA~1\MATLAB\R2010a\bin\win32\gmake" -f controlMCUSlugsMKII.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/DEE.c 
''pic30-gcc  -c C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/DEES.s -Wa,-p=33fJ256MC710,-g 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/apUtils.c 
C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/apUtils.c:852:7: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/circBuffer.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_data.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII_main.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    dsPIC_InputCapture_Interrupt.c 
dsPIC_InputCapture_Interrupt.c: In function '_IC2Interrupt': 
dsPIC_InputCapture_Interrupt.c:11: warning:  PSV model not specified for '_IC2Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC3Interrupt': 
dsPIC_InputCapture_Interrupt.c:32: warning:  PSV model not specified for '_IC3Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC4Interrupt': 
dsPIC_InputCapture_Interrupt.c:53: warning:  PSV model not specified for '_IC4Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC5Interrupt': 
dsPIC_InputCapture_Interrupt.c:74: warning:  PSV model not specified for '_IC5Interrupt'; 
   assuming 'auto_psv' this may affect latency 
dsPIC_InputCapture_Interrupt.c: In function '_IC8Interrupt': 
dsPIC_InputCapture_Interrupt.c:95: warning:  PSV model not specified for '_IC8Interrupt'; 
   assuming 'auto_psv' this may affect latency 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/groundStationDriver.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/interProcCommSlave.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/navSupport.c 
C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/navSupport.c:211:2: warning: no newline at end of file 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/protDecoder.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    rtGetInf.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    rtGetNaN.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    rt_nonfinite.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    rt_zcfcn.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    C:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib/sbrk.c 
''pic30-gcc  -c -mcpu=33fJ256MC710 -O -merrata=exch -mlarge-data	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2010a/simulink/include -IC:\PROGRA~1\MATLAB\R2010a/extern/include -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\controlMCUSlugsMKII_dspic\sources -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62 -IC:\Users\Dan\Documents\MATLAB\SLUG_Autopilot\malife-SLUGS-13d8c62\clib   -I C:\PROGRA~1\MICROC~1\MPLABC~2\include    controlMCUSlugsMKII.c 
''pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld -o ..\../controlMCUSlugsMKII.cof  DEE.o DEES.o apUtils.o circBuffer.o controlMCUSlugsMKII_data.o controlMCUSlugsMKII_main.o dsPIC_InputCapture_Interrupt.o groundStationDriver.o interProcCommSlave.o navSupport.o protDecoder.o rtGetInf.o rtGetNaN.o rt_nonfinite.o rt_zcfcn.o sbrk.o controlMCUSlugsMKII.o      C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\Program Files\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: mode pic30_coff 
DEE.o 
DEES.o 
apUtils.o 
circBuffer.o 
controlMCUSlugsMKII_data.o 
controlMCUSlugsMKII_main.o 
dsPIC_InputCapture_Interrupt.o 
groundStationDriver.o 
interProcCommSlave.o 
navSupport.o 
protDecoder.o 
rtGetInf.o 
rtGetNaN.o 
rt_nonfinite.o 
rt_zcfcn.o 
sbrk.o 
controlMCUSlugsMKII.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)crt0_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)brk.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a)data_init_standard.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)putsUART2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer1.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenTimer2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture4.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture4.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture5.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture5.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenCapture8.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntCapture8.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)SetDCMCPWM.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)ConfigIntMCPWM.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a)OpenMCPWM.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)memcpy.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)vsprintf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)memset.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)doprnt.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)powers.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)fputc.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)fseek.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)fflush.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)flsbuf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)buf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a)errno.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixsfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)atan2f.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)powf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sqrtf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)atanf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)asinf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sinf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)cosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)tanf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)acosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)expf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunssfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)feqltle.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fne.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fgtge.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)mulsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)addsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)divsf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floatsisf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floorf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)muldf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)extendsfdf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)deqltle.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dne.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixdfdi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floatdisf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)frexpf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dgtge.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)divdf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunsdfsi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)subdf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)adddf3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)divmoddi3.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fixunsdfdi.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)floatdidf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)funpack2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)futil.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fchop.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)_frexpf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)ldexpf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)logf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)asinacosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)sincosf.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fcompare.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)fmodrem.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack2.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dcompare.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dunpack.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dpropagateNaN.o 
(C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a)dtype.o 
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x2aa00] 
<wbr>
section                    address   length (PC units)   length (bytes) (dec) 
-------                    -------   -----------------   -------------------- 
.text                        0x200              0x2b52          0x40fb  (16635) 
.const                      0x2d52                0x94            0xde  (222) 
.text                       0x2de6               0x126           0x1b9  (441) 
.text                       0x2f0c                0xf0           0x168  (360) 
.isr                        0x2ffc                 0x2             0x3  (3) 
_02bc8a804cebe8d0           0x3000              0x1000          0x1800  (6144) 
.text                       0x4000              0x6190          0x9258  (37464) 
.dinit                      0xa190               0x384           0x546  (1350) 
.text                       0xa514               0x2da           0x447  (1095) 
.text                       0xa7ee               0x10e           0x195  (405) 
.text                       0xa8fc               0x1b4           0x28e  (654) 
<wbr>
                     Total program memory used (bytes):         0xfd05  (64773) 24% 
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x7800] 
<wbr>
section                    address      alignment gaps    total length  (dec) 
-------                    -------      --------------    ------------------- 
.bss                         0x800                   0          0x174e  (5966) 
.data                       0x1f4e                   0           0x386  (902) 
.dconst                     0x22d4                   0            0x2a  (42) 
.bss                        0x22fe                   0            0x2c  (44) 
.data                       0x232a                   0             0x4  (4) 
.bss                        0x232e                   0             0x4  (4) 
.data                       0x2332                   0             0x4  (4) 
.bss                        0x2336                   0             0x8  (8) 
_020821504cebe8d9           0x7f32                   0            0xce  (206) 
<wbr>
                        Total data memory used (bytes):         0x1c0c  (7180) 23% 
<wbr>
<wbr>
Dynamic Memory Usage 
<wbr>
region                     address                      maximum length  (dec) 
------                     -------                      --------------------- 
heap                             0                                   0  (0) 
stack                       0x233e                              0x5bf4  (23540) 
<wbr>
                        Maximum dynamic memory (bytes):         0x5bf4  (23540) 
<wbr>
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.ftell+0xa):fake: undefined reference to `lseek' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.fseek+0x1e):fake: undefined reference to `lseek' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.fseek+0x52):fake: undefined reference to `lseek' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.fseek+0x5c):fake: undefined reference to `lseek' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.fseek+0x66):fake: undefined reference to `lseek' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fseek.o)(.libc.fseek+0xc8):fake: more undefined references to `lseek' follow 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(fflush.o)(.libc.fflush+0x2e):fake: undefined reference to `write' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(flsbuf.o)(.libc._flsbuf+0x3a):fake: undefined reference to `write' 
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a(flsbuf.o)(.libc._flsbuf+0x56):fake: undefined reference to `write' 
C:\Program Files\Microchip\MPLAB C30\bin\bin/pic30-coff-ld.exe: link errors found, deleting executable `..\../controlMCUSlugsMKII.cof' 
gmake: *** [..\../controlMCUSlugsMKII.cof] Error 255 
### Real-Time Workshop build procedure for model: 'controlMCUSlugsMKII' aborted due to an error.</code></pre><br>
<br>
Getting closer!<br>
<br>
Thanks,<br>
<br>
Dan</div>
</article>

<article class="forum-post" id="p1339">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-23 21:41 UTC">2010-11-23 21:41 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">It's getting closer.<br>
<br>
You can now open the project within MPLAB and play with compilation options (anyway, not sure that would solve the problem)<br>
<br>
<br>
<br>
The problem is in the last step : linking all objects and library binary files.<br>
<br>
Comparing your list of object file being used with mine (in earlier post), it can be seen that the .o file list are different (after replacing few ~2 by ~1...)<br>
<br>
At first sight, mine has 10 more file.<br>
<br>
However, your list contains also library file not present in mine like (not exhaustive list) :<br>
<br>
fputc.o<br>
<br>
fseek.o<br>
<br>
fflush.o<br>
<br>
flsbuf.o<br>
<br>
buf.o<br>
<br>
Mine contain also library file not present in yours like (not exhaustive list) :<br>
<br>
xprintf.o<br>
<br>
<br>
<br>
At first thought, I do not see why file system fonction are needed (like fputc, fseek ...)<br>
<br>
I think that some simulink model configuration have change a bit. (for example, there are option for the  embedded code to report or not error, or to log data or not). Theses configuration bit change a bit the code and calls function that are not available ?<br>
<br>
Same model should generate the same code.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1341">
<header><strong>malife</strong><time datetime="2010-11-26 16:22 UTC">2010-11-26 16:22 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hello,<br>
<br>
 Sorry for the long silence. I was out of town. I agree completely with Lubin. lseek() and write () are NOT used at all neither by Simulink (on a 2007A Windows XP configuration) nor by the custom C code I wrote for the low-level drivers. I think this is something completely different. It could be the Matlab version. It could be that it is trying to use the wrong linker. Or it could be the language tool library version.<br>
<br>
<br>
<br>
The only thing I've seen come close to a report about this is in here: <a href="http://www.microchip.com/forums/tm.aspx?m=535514&amp;high=fake%3A+undefined+reference+to">http://www.microchip.com/forums/tm.aspx ... ference+to</a><br>
<br>
<br>
<br>
My best guess would be for you to try to downgrade the C 30 compiler to version 3.12 which is the one I have installed. You can download an older version from here : <a href="http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&amp;nodeId=1406&amp;dDocName=en023073">http://www.microchip.com/stellent/idcpl ... e=en023073</a><br>
<br>
<br>
<br>
See if it gets you somewhere. Please do report here if this suggestion works or if you get exactly the same error.<br>
<br>
<br>
<br>
This is very strange.</div>
</article>

<article class="forum-post" id="p1342">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-26 19:46 UTC">2010-11-26 19:46 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Thanks Mariano for the idea,<br>
<br>
<br>
<br>
very quick post just to inform that I downloaded the latest version of C30 compiler (3.25) on my windows 32bits system with matlab 2010a and  successfully get the model compiling.<br>
<br>
<br>
<br>
Perhaps Dan may upload its model on the forum so as I will be able to test it ? Thet may provide new informations...<br>
<br>
<br>
<br>
(I am not available this WE)<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1344">
<header><strong>dambrosio</strong><time datetime="2010-11-27 16:01 UTC">2010-11-27 16:01 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hey Guys,<br>
<br>
Sorry for the late reply, I was on vacation for a bit. So I attached the current SLUG Autopilot folder that I have been compiling from to see if it is a model issue. Let me know if you get anything working with this.<br>
<br>
Thanks,<br>
<br>
Dan<br>
<br>
<br>
<br>
Here is the zip file link: <br>
<br>
<a href="http://hotfile.com/dl/85363043/5dbefa9/SLUG_Autopilot_Ambrosio.zip.html">http://hotfile.com/dl/85363043/5dbefa9/ ... o.zip.html</a></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/353-SLUG_Autopilot_Ambrosio.zip">Pièce jointe : SLUG_Autopilot_Ambrosio.zip</a></p>
</article>

<article class="forum-post" id="p1345">
<header><strong>malife</strong><time datetime="2010-11-27 17:54 UTC">2010-11-27 17:54 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Dan,<br>
<br>
 I confirm the version you uploaded compiles without a problem in my setup. This really narrows it to either your setup (compiler/Matlab version/ dsPIC Blockset version) or OS version. I am really sorry you are going through this but neither Lubin nor I have been able to reproduce it and, as you can expect, if we can't reproduce the error than we can not debug it.<br>
<br>
<br>
<br>
You can download the version of the complete folder you uploaded with the files I just compiled here:  <a href="http://dl.dropbox.com/u/6400827/Stable.zip">http://dl.dropbox.com/u/6400827/Stable.zip</a><br>
<br>
<br>
<br>
Did you try downgrading the compiler version as I suggested in my previous post? I am really out of ideas. Do you have any other computer where you can install from scratch?<br>
<br>
<br>
<br>
I think it is a good time for a Skype telecon, ideally with Lubin Joining us.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/352-Stable.zip">Pièce jointe : Stable.zip</a></p>
</article>

<article class="forum-post" id="p1346">
<header><strong>malife</strong><time datetime="2010-11-27 17:57 UTC">2010-11-27 17:57 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">I forgot to add that the only thing I did to compile was to double click the configuration block, then adding the errata and large data model flags to the compiler options. After that it compiled with no issue</div>
</article>

<article class="forum-post" id="p1347">
<header><strong>dambrosio</strong><time datetime="2010-11-27 21:04 UTC">2010-11-27 21:04 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Guys,<br>
<br>
I double clicked the configure block and made sure all the flags were added and tried to re-compile. I got the exact same error. I feel like a teleconference would be perfect. I have all day Monday open if that works for both of you. I will try and compile the model with the older version of the C30 compiler (v3.12) on Monday before talking to you both. <br>
<br>
<br>
<br>
Thanks,<br>
<br>
Dan</div>
</article>

<article class="forum-post" id="p1350">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 12:25 UTC">2010-11-29 12:25 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : malife</header>I think it is a good time for a Skype telecon, ideally with Lubin Joining us.</blockquote><br>
I'll ba available on monday eivening (either about 19h30, or 20h30 or later on, French time is UTC+1.)<br>
<br>
Lubin<br>
<br>
<br>
<br>
PS : I uploaded on the forum directly mariano dropbox's file (more sustainable for the forum). Prefere using the forum upload function that is more sustainable in time.</div>
</article>

<article class="forum-post" id="p1351">
<header><strong>dambrosio</strong><time datetime="2010-11-29 17:27 UTC">2010-11-29 17:27 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Lubin,<br>
<br>
If I did my math right then I will be available at 2:00pm MST which is 21hr your time. Does this work for you? My Skype name is dan_ambrosio.<br>
<br>
Let me know if this works for you.<br>
<br>
Dan<br>
<br>
<br>
<br>
Ps. Mariano do you have a preferred time?</div>
</article>

<article class="forum-post" id="p1354">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-29 19:44 UTC">2010-11-29 19:44 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Ok for me</div>
</article>

<article class="forum-post" id="p1362">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 09:28 UTC">2010-11-30 09:28 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">I also have MPLAB IDE installed on my computer. While installing MPLAB, Mirochip also propose to install compiler and so on. I usually install them all.<br>
<br>
Thus, you may try to install MPLAB also (freely available from Microchip website)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1363">
<header><strong>dambrosio</strong><time datetime="2010-11-30 16:06 UTC">2010-11-30 16:06 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Lubin,<br>
<br>
I do have the MPLAB IDE installed on my computer and install all the compilers. I tried to install your version of the MPLAB C30 compiler V3.25 and got the same lseek error as above. When I downgraded my compiler to V3.24 I get an error about memory when trying to compile the model <br>
Also, when I double click to open the controlMCUSlugsMKII.mdl I get the following output from MATLAB.<br>
<br>
<br>
<pre><code>Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\dspic\execBatch.p is a case-insensitive match and will be
used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2010a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 97
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\blocks\dsPIC_ConfigRTWOption.p&gt;dsPIC_ConfigRTWOption at 45
  In C:\Users\Dan\Documents\MATLAB\dsPIC_blockset\blocks\dsPIC_MASTER_callback.p&gt;dsPIC_MASTER_callback at 87
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The *System Target File
must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time
workshop 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time workshop 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: In instantiating linked block 'controlMCUSlugsMKII/Master' : Invalid setting in Master block
(mask) 'Master' for parameter 'MCLR' 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Calculus Time Step'. two
dsPIC_MASTER blocks find. Max number of dsPIC_MASTER block is one ! 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: two dsPIC_MASTER blocks find. Max number of dsPIC_MASTER block is one ! 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
&gt;&gt; </code></pre><br>
<br>
I don't know if this is relevant at all since I wasn't getting most of these before. I am kind of running out of options here on what do to. Do you think it is the way I installed the MPLAB C30 compiler?<br>
<br>
<br>
<br>
Thanks,<br>
<br>
Dan</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/358-error2.png">Pièce jointe : error2.png</a></p>
</article>

<article class="forum-post" id="p1364">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 17:43 UTC">2010-11-30 17:43 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hi Dan,<br>
<br>
<br>
<br>
It seems you model file get two MASTER blocks now ! One of them may be in a subsystem ?<br>
<br>
Here is the message I get while opening the model :<br>
<br>
<br>
<pre><code>Warning: Could not find an exact (case-sensitive) match for 'ExecBatch'.
C:\Program Files\81eq9Z16RLFXQ\dspic\execBatch.m is a case-insensitive match and will be
used instead.
You can improve the performance of your code by using exact
name matches and we therefore recommend that you update your
usage accordingly. Alternatively, you can disable this warning using
warning('off','MATLAB:dispatcher:InexactCaseMatch').
This warning will become an error in future releases. 
&gt; In C:\Program Files\MATLAB\R2010a\toolbox\rtw\rtw\private\getSTFInfo.p&gt;getSTFInfo at 97
  In rtwprivate at 12
  In stf4target at 34
  In stf2target at 61
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: GMAKE_PLACE not defined, check tlc target 
&gt; In dsPIC_ConfigRTWOption at 45
  In dsPIC_MASTER_callback at 45
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: Error evaluating 'LoadFcn' callback of Master block (mask) 'Master'. The
*System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt;
Configuration Parameters ==&gt; Real Time workshop 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: The *System Target File must be defined to dsPIC Real Time workshop
(Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
Warning: In instantiating linked block 'controlMCUSlugsMKII/Master' : Invalid setting
in Master block (mask) 'Master' for parameter 'MCLR' 
  In general\private\openmdl at 13
  In open at 158
  In uiopen at 196
PT&gt;&gt; </code></pre><br>
<br>
With a 32 bit windows,<br>
<br>
I downloaded the zip fild you posted :  SLUG_Autopilot_Ambrosio.zip<br>
<br>
I unzip it into the same directory as you : C:\USERS\SLUG\Documents\MATLAB\<br>
<br>
Then, I directly open the MPLAB project file : C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcp<br>
<br>
and it sucessfully compiled within MPLAB. I get the following report :<br>
<pre><code>----------------------------------------------------------------------
Debug build of project `C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcp' started.
Language tool versions: pic30-as.exe v3.24, pic30-gcc.exe v3.24, pic30-ld.exe v3.24, pic30-ar.exe v3.25
Preprocessor symbol `__DEBUG' is defined.
Tue Nov 30 18:21:37 2010
----------------------------------------------------------------------
Clean: Deleting intermediary and output files.
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\DEE.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\DEES.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\apUtils.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\circBuffer.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\groundStationDriver.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\navSupport.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\protDecoder.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rtGetInf.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rtGetNaN.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\sbrk.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.hex".
Clean: Deleted file "C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcs".
Clean: Done.
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\DEE.c" -o"controlMCUSlugsMKII_dspic\sources\DEE.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -c -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\DEES.s" -o"controlMCUSlugsMKII_dspic\sources\DEES.o" -Wa,-I"controlMCUSlugsMKII_dspic\sources",--defsym=__DEBUG=1
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\apUtils.c" -o"controlMCUSlugsMKII_dspic\sources\apUtils.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\apUtils.c:852:7: warning: no newline at end of file
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\circBuffer.c" -o"controlMCUSlugsMKII_dspic\sources\circBuffer.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c" -o"controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC2Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:11: warning:  PSV model not specified for '_IC2Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC3Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:32: warning:  PSV model not specified for '_IC3Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC4Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:53: warning:  PSV model not specified for '_IC4Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC5Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:74: warning:  PSV model not specified for '_IC5Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC8Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:95: warning:  PSV model not specified for '_IC8Interrupt';
   assuming 'auto_psv' this may affect latency
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\groundStationDriver.c" -o"controlMCUSlugsMKII_dspic\sources\groundStationDriver.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\interProcCommSlave.c" -o"controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\navSupport.c" -o"controlMCUSlugsMKII_dspic\sources\navSupport.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\navSupport.c:211:2: warning: no newline at end of file
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\protDecoder.c" -o"controlMCUSlugsMKII_dspic\sources\protDecoder.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rtGetInf.c" -o"controlMCUSlugsMKII_dspic\sources\rtGetInf.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rtGetNaN.c" -o"controlMCUSlugsMKII_dspic\sources\rtGetNaN.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rt_nonfinite.c" -o"controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rt_zcfcn.c" -o"controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib\sbrk.c" -o"controlMCUSlugsMKII_dspic\sources\sbrk.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o" "controlMCUSlugsMKII_dspic\sources\DEE.o" "controlMCUSlugsMKII_dspic\sources\DEES.o" "controlMCUSlugsMKII_dspic\sources\apUtils.o" "controlMCUSlugsMKII_dspic\sources\circBuffer.o" "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o" "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o" "controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o" "controlMCUSlugsMKII_dspic\sources\groundStationDriver.o" "controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o" "controlMCUSlugsMKII_dspic\sources\navSupport.o" "controlMCUSlugsMKII_dspic\sources\protDecoder.o" "controlMCUSlugsMKII_dspic\sources\rtGetInf.o" "controlMCUSlugsMKII_dspic\sources\rtGetNaN.o" "controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o" "controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o" "controlMCUSlugsMKII_dspic\sources\sbrk.o" "C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a" "C:\
PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a" "C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a" -o"controlMCUSlugsMKII.cof" -Wl,-L"controlMCUSlugsMKII_dspic\sources",--script="..\..\..\..\..\..\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld",--defsym=__MPLAB_BUILD=1,--defsym=__MPLAB_DEBUG=1,-Map="controlMCUSlugsMKII.map",--report-mem
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x2aa00]
<wbr>
section                    address   length (PC units)   length (bytes) (dec)
-------                    -------   -----------------   --------------------
.text                        0x200              0x296e          0x3e25  (15909)
.text                       0x2b6e                0x8c            0xd2  (210)
.isr                        0x2bfa                 0x2             0x3  (3)
_01b4ba104cf532a2           0x2c00              0x1000          0x1800  (6144)
.const                      0x3c00                0x94            0xde  (222)
.text                       0x3c94              0x646a          0x969f  (38559)
.dinit                      0xa0fe               0x1da           0x2c7  (711)
.text                       0xa2d8               0x3be           0x59d  (1437)
.text                       0xa696                0x8e            0xd5  (213)
<wbr>
                     Total program memory used (bytes):         0xf7b0  (63408) 24%
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x7800]
<wbr>
section                    address      alignment gaps    total length  (dec)
-------                    -------      --------------    -------------------
.nbss                        0x800                   0             0x2  (2)
.bss                         0x802                   0          0x174e  (5966)
.data                       0x1f50                   0            0x9e  (158)
.dconst                     0x1fee                   0            0x32  (50)
.data                       0x2020                   0            0x22  (34)
.bss                        0x2042                   0            0x2c  (44)
.data                       0x206e                   0            0x12  (18)
.dconst                     0x2080                   0             0x8  (8)
.data                       0x2088                   0             0x6  (6)
.bss                        0x208e                   0             0x4  (4)
.data                       0x2092                   0             0x2  (2)
.bss                        0x2094                   0             0x2  (2)
.data                       0x2096                   0             0x2  (2)
.dconst                     0x2098                   0             0x2  (2)
.data                       0x209a                   0             0x2  (2)
_00f01a104cf532a5           0x7f32                   0            0xce  (206)
<wbr>
                        Total data memory used (bytes):         0x196a  (6506) 21%
<wbr>
<wbr>
<wbr>
Dynamic Memory Usage
<wbr>
region                     address                      maximum length  (dec)
------                     -------                      ---------------------
heap                             0                                   0  (0)
stack                       0x209c                              0x5e96  (24214)
<wbr>
                        Maximum dynamic memory (bytes):         0x5e96  (24214)
<wbr>
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-bin2hex.exe" "C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof"
Loaded C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof.
----------------------------------------------------------------------
Debug build of project `C:\USERS\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcp' succeeded.
Language tool versions: pic30-as.exe v3.24, pic30-gcc.exe v3.24, pic30-ld.exe v3.24, pic30-ar.exe v3.25
Preprocessor symbol `__DEBUG' is defined.
Tue Nov 30 18:21:47 2010
----------------------------------------------------------------------
BUILD SUCCEEDED</code></pre><br>
<br>
Then, I renamed the directory where the c files are generated : controlMCUSlugsMKII_dspic (into controlMCUSlugsMKII_dspic_original)<br>
<br>
I opened the model controlMCUSlugsMKII.mdl from MATLAB (2010a). Simulink was able to generate C code and compile it.<br>
<br>
<br>
<br>
Comparing your generated source files with mines shows no differences (except in comment, like time etc...)<br>
<br>
<br>
<br>
The only weird things I noticed is that matlab sometimes crashed. It may be due to the large size of the model file ?<br>
<br>
<br>
<br>
From theses elements, I think that you are facing a problem with the compiler as the code you generated and that does not compile from your side successfully compiled here. Also, generated code from your matlab and mine is equal (except for comments)<br>
<br>
<br>
<br>
You may have more insight posting the problem on the microchip forum (or to ask Microchip directly if you can)<br>
<br>
<br>
<br>
The only solution I could propose is to start a new model from scratch, add blocks from mariano model one by one, compiling the model at several step. Do not forget to add custom c file written by the slug team in simulink configuration panel.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1365">
<header><strong>dambrosio</strong><time datetime="2010-11-30 18:06 UTC">2010-11-30 18:06 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Lubin,<br>
<br>
I opened the controlMCUSlugsMKII.mcp file in MPLAB IDE v8.60 and right click on the main folder to BuildAll. Here is the output:<br>
<pre><code>----------------------------------------------------------------------
Debug build of project `C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcp' started.
Language tool versions: pic30-as.exe v3.25, pic30-gcc.exe v3.25, pic30-ld.exe v3.25, pic30-ar.exe v3.25
Preprocessor symbol `__DEBUG' is defined.
Tue Nov 30 11:03:16 2010
----------------------------------------------------------------------
Clean: Deleting intermediary and output files.
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\DEE.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\DEES.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\apUtils.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\circBuffer.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\groundStationDriver.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\navSupport.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\protDecoder.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rtGetInf.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rtGetNaN.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII_dspic\sources\sbrk.o".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.hex".
Clean: Deleted file "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcs".
Clean: Done.
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\DEE.c" -o"controlMCUSlugsMKII_dspic\sources\DEE.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -c -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\DEES.s" -o"controlMCUSlugsMKII_dspic\sources\DEES.o" -Wa,-I"controlMCUSlugsMKII_dspic\sources",--defsym=__DEBUG=1
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\apUtils.c" -o"controlMCUSlugsMKII_dspic\sources\apUtils.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\apUtils.c:852:7: warning: no newline at end of file
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\circBuffer.c" -o"controlMCUSlugsMKII_dspic\sources\circBuffer.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.c" -o"controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c" -o"controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC2Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:11: warning:  PSV model not specified for '_IC2Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC3Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:32: warning:  PSV model not specified for '_IC3Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC4Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:53: warning:  PSV model not specified for '_IC4Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC5Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:74: warning:  PSV model not specified for '_IC5Interrupt';
   assuming 'auto_psv' this may affect latency
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c: In function '_IC8Interrupt':
controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.c:95: warning:  PSV model not specified for '_IC8Interrupt';
   assuming 'auto_psv' this may affect latency
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\groundStationDriver.c" -o"controlMCUSlugsMKII_dspic\sources\groundStationDriver.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\interProcCommSlave.c" -o"controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\navSupport.c" -o"controlMCUSlugsMKII_dspic\sources\navSupport.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\navSupport.c:211:2: warning: no newline at end of file
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\protDecoder.c" -o"controlMCUSlugsMKII_dspic\sources\protDecoder.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rtGetInf.c" -o"controlMCUSlugsMKII_dspic\sources\rtGetInf.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rtGetNaN.c" -o"controlMCUSlugsMKII_dspic\sources\rtGetNaN.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rt_nonfinite.c" -o"controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "controlMCUSlugsMKII_dspic\sources\rt_zcfcn.c" -o"controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 -x c -c   "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib\sbrk.c" -o"controlMCUSlugsMKII_dspic\sources\sbrk.o" -I"controlMCUSlugsMKII_dspic\sourcescontrolMCUSlugsMKII_dspic\sources" -I"." -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\controlMCUSlugsMKII_dspic\sources" -I"C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\stable\clib" -I"C:\PROGRA~1\MICROC~1\MPLABC~2\include" -I"C:\PROGRA~1\MATLAB\R2010a/simulink/include" -I"C:\PROGRA~1\MATLAB\R2010a/extern/include" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/ert" -I"C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/common" -D__DEBUG -O -merrata=exch -mlarge-data
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-gcc.exe" -mcpu=33FJ256MC710 "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII.o" "controlMCUSlugsMKII_dspic\sources\DEE.o" "controlMCUSlugsMKII_dspic\sources\DEES.o" "controlMCUSlugsMKII_dspic\sources\apUtils.o" "controlMCUSlugsMKII_dspic\sources\circBuffer.o" "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_data.o" "controlMCUSlugsMKII_dspic\sources\controlMCUSlugsMKII_main.o" "controlMCUSlugsMKII_dspic\sources\dsPIC_InputCapture_Interrupt.o" "controlMCUSlugsMKII_dspic\sources\groundStationDriver.o" "controlMCUSlugsMKII_dspic\sources\interProcCommSlave.o" "controlMCUSlugsMKII_dspic\sources\navSupport.o" "controlMCUSlugsMKII_dspic\sources\protDecoder.o" "controlMCUSlugsMKII_dspic\sources\rtGetInf.o" "controlMCUSlugsMKII_dspic\sources\rtGetNaN.o" "controlMCUSlugsMKII_dspic\sources\rt_nonfinite.o" "controlMCUSlugsMKII_dspic\sources\rt_zcfcn.o" "controlMCUSlugsMKII_dspic\sources\sbrk.o" "C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a" "C:\
PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256MC710-coff.a" "C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a" -o"controlMCUSlugsMKII.cof" -Wl,-L"controlMCUSlugsMKII_dspic\sources",--script="..\..\..\..\..\..\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256MC710.gld",--defsym=__MPLAB_BUILD=1,--defsym=__MPLAB_DEBUG=1,-Map="controlMCUSlugsMKII.map",--report-mem
<wbr>
<wbr>
Program Memory  [Origin = 0x200, Length = 0x2aa00]
<wbr>
section                    address   length (PC units)   length (bytes) (dec)
-------                    -------   -----------------   --------------------
.text                        0x200              0x2bda          0x41c7  (16839)
.const                      0x2dda                0x94            0xde  (222)
.text                       0x2e6e               0x126           0x1b9  (441)
.text                       0x2f94                0x3e            0x5d  (93)
.text                       0x2fd2                0x1e            0x2d  (45)
.isr                        0x2ff0                 0x2             0x3  (3)
_02b13a804cf53c67           0x3000              0x1000          0x1800  (6144)
.text                       0x4000              0x6190          0x9258  (37464)
.dinit                      0xa190               0x38c           0x552  (1362)
.text                       0xa51c               0x2da           0x447  (1095)
.text                       0xa7f6               0x324           0x4b6  (1206)
.text                       0xab1a                0x32            0x4b  (75)
<wbr>
                     Total program memory used (bytes):         0xfddd  (64989) 24%
<wbr>
<wbr>
Data Memory  [Origin = 0x800, Length = 0x7800]
<wbr>
section                    address      alignment gaps    total length  (dec)
-------                    -------      --------------    -------------------
.bss                         0x800                   0          0x174e  (5966)
.data                       0x1f4e                   0           0x386  (902)
.dconst                     0x22d4                   0            0x2a  (42)
.bss                        0x22fe                   0            0x2c  (44)
.data                       0x232a                   0             0x6  (6)
.bss                        0x2330                   0             0x4  (4)
.data                       0x2334                   0             0x2  (2)
.bss                        0x2336                   0             0x8  (8)
.data                       0x233e                   0             0x2  (2)
_01fb21504cf53c71           0x7f32                   0            0xce  (206)
<wbr>
                        Total data memory used (bytes):         0x1c0e  (7182) 23%
<wbr>
<wbr>
Dynamic Memory Usage
<wbr>
region                     address                      maximum length  (dec)
------                     -------                      ---------------------
heap                             0                                   0  (0)
stack                       0x2340                              0x5bf2  (23538)
<wbr>
                        Maximum dynamic memory (bytes):         0x5bf2  (23538)
<wbr>
Executing: "C:\Program Files\Microchip\MPLAB C30\bin\pic30-bin2hex.exe" "C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof"
Loaded C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.cof.
----------------------------------------------------------------------
Debug build of project `C:\Users\SLUG\Documents\MATLAB\SLUG_Autopilot\Stable\controlMCUSlugsMKII.mcp' succeeded.
Language tool versions: pic30-as.exe v3.25, pic30-gcc.exe v3.25, pic30-ld.exe v3.25, pic30-ar.exe v3.25
Preprocessor symbol `__DEBUG' is defined.
Tue Nov 30 11:03:45 2010
----------------------------------------------------------------------
BUILD SUCCEEDED
</code></pre><br>
<br>
I then looked at the main directory and found the a new controlMCUSlugsMKII.hex was generated. Doesn't this mean that it compiled sucessfully? There could be something wrong with the makefile that is being used by MATLAB to generate the hex file. Theoretically, I should be able to compile in MATLAB till it breaks then open the mcp file to finish the hex compile right?<br>
<br>
Thanks,<br>
<br>
Dan</div>
</article>

<article class="forum-post" id="p1368">
<header><strong>LubinKerhuel</strong><time datetime="2010-11-30 22:29 UTC">2010-11-30 22:29 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>Doesn't this mean that it compiled sucessfully?</blockquote><br>
Yes, very good news !<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : LubinKerhuel</header> Theoretically, I should be able to compile in MATLAB till it breaks then open the mcp file to finish the hex compile right?</blockquote><br>
Yes. If I were in your shoes, I would (at least once) delete the two generated folder : <strong>slpjr</strong> and <strong>controlMCUSlugsMKII_dspic</strong> to make sure that matlab created new files. Then, if it compiles within MPLAB, it's all Ok. <br>
<br>
I am just a bit frustrated as we did not find the problem that make the compiler not working when it is called from MATLAB !<br>
<br>
<br>
<br>
Anyway, it's lucky that the automatic generation of the MPLAB project file has been added very recently !<br>
<br>
<br>
<br>
I hope we'll have some in flight video soon ! Do not hesitate to embed  youtube or vimeo video within this wiki website !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1383">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-05 22:00 UTC">2010-12-05 22:00 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : dambrosio</header>There could be something wrong with the makefile that is being used by MATLAB to generate the hex file</blockquote><br>
That's correct ! There was something wrong with the makefile that does not work anymore with the latest Microchip linker pic30-ld (V3.25).<br>
<br>
I could not have this tools working (with this version only as it works great with all previous version ) thus I replaced it by the pic30-gcc tools that call the linker in backend. <br>
<br>
This solution is a bit tricky but seems Ok anyway.<br>
<br>
<br>
<br>
Please let me know !<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1445">
<header><strong>coolj</strong><time datetime="2011-01-20 07:16 UTC">2011-01-20 07:16 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hi Lubin, Mariano,<br>
<br>
<br>
<br>
Were you able to compile the controlMCUSlugsMKII.mdl file w/ v3.4 of the blockset?<br>
<br>
<br>
<br>
I am using r2010b, v3.4b of the blockset, and the 13d8c62 version of Mariano's awesome AP project.  I was able to successfully compile the sensorMCUSlugsMKII.mdl file after adding four missing variables (baroTempK, baroMeanTemp, pitTempK, pitMeanTemp), but have not been able to compile the control model file.<br>
<br>
<br>
<br>
The recurring error is shown below involving the reshape block.  I tried removing the block and re-adding it from the r2010b math library, but I get the same error.  Any thoughts?<br>
<br>
<br>
<br>
Thanks!<br>
<br>
Justin<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/372-controlMCU_error1.gif">Pièce jointe : controlMCU_error1.gif</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/373-controlMCU_error2.gif">Pièce jointe : controlMCU_error2.gif</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/374-controlMCU_error3.gif">Pièce jointe : controlMCU_error3.gif</a></p>
</article>

<article class="forum-post" id="p1453">
<header><strong>dambrosio</strong><time datetime="2011-02-01 06:18 UTC">2011-02-01 06:18 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Lubin,<br>
<br>
I am trying to get the SLUG autopilot code to compile without having to do the "work around" in mplab could you give me a little more information on what you did in the following quote?<br>
<br>
<br>
<blockquote>There was something wrong with the makefile that does not work anymore with the latest Microchip linker pic30-ld (V3.25).<br>
<br>
I could not have this tools working (with this version only as it works great with all previous version ) thus I replaced it by the pic30-gcc tools that call the linker in backend.<br>
<br>
This solution is a bit tricky but seems Ok anyway.</blockquote><br>
<br>
Thanks,<br>
<br>
Dan</div>
</article>

<article class="forum-post" id="p1459">
<header><strong>LubinKerhuel</strong><time datetime="2011-02-15 21:24 UTC">2011-02-15 21:24 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hi Dan,<br>
<br>
<br>
<br>
There are two ways to execute the linker :<br>
<br>
- Either calling directly the linker executable: <strong>pic30-ld</strong><br>
<br>
- Neither calling the compiler with appropriate flags (compiler is <strong>pic30-gcc</strong>) <br>
<br>
<br>
<br>
In one of the recent version I tested (3.25), I could not manage to get the linker<strong>pic30-ld</strong> working properly. Thus, the blockset now use the other way to call the linker!<br>
<br>
<br>
<br>
Which blockset version are you using?<br>
<br>
I could provide you with the latest version which might solve the problem you are facing.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1592">
<header><strong>ismaeelbit</strong><time datetime="2011-05-30 06:52 UTC">2011-05-30 06:52 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hi guys,<br>
<br>
I am working on UAV application and i  wish to adopt the SLUG files WITH lubin BLOCKSETS. I real appreciate your discussion so far on this forum.<br>
<br>
<br>
<br>
1. I will appreciate a brief guidelines on adoption of the SLUG .mdl first for sensors' data acquisition for flight data based on the experience already share on this forum<br>
<br>
2. is the GPS codes generic for all gps module: am using EM-406A, <br>
<br>
if it works for this GPS,  what is the minimum  c.codes to be included in order to use only the GPS function. I am planning to use other IMU through analog inputs into the simulink sensordata, So, I will want to remove other c. functions related to other sensors for now.<br>
<br>
<br>
<br>
looking for to read from you. Let me know if additional info is required.<br>
<br>
<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p1993">
<header><strong>Buffalo_guy</strong><time datetime="2013-04-28 03:47 UTC">2013-04-28 03:47 UTC</time></header>
<h3>Re: SLUGS - an open source autopilot</h3>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
Much has happened in the past two or three years since this thread was originally created. SLUGS has been tested and fully developed, and Lubin now works @ Microchip, and stopped developing this blockset and now develops the official Microchip blockset (congrats on your position!).<br>
<br>
<br>
<br>
So my question:<br>
<br>
<br>
<br>
What modifications are needed to adapt SLUGS in its final form to work with the official Microchip blockset?<br>
<br>
<br>
<br>
I am interested in this, and if someone can guide me I can perform this task and provide you with the result once finished.<br>
<br>
<br>
<br>
Regards</div>
</article>

