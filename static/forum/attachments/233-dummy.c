/*
 * File: dummy.c
 *
 * Real-Time Workshop code generated for Simulink model dummy.
 *
 * Model version                        : 1.1995
 * Real-Time Workshop file version      : 6.5  (R2006b)  03-Aug-2006
 * Real-Time Workshop file generated on : Thu Apr 16 11:21:27 2009
 * TLC version                          : 6.5 (Aug  3 2006)
 * C source code generated on           : Thu Apr 16 11:21:28 2009
 *--------------------------------------------------------------
 *   Embedded Coder for Microchip dsPIC family.                 |
 *   Generate .c and .h files from your Matlab/simulink model   |
 *   and compile the diagram to .hex and .coff file that can be |
 *   downloaded directly into the microcontroller               |
 *                                                              |
 * Licence Accorded to Simon Clarke                             |
 *                     Add2 Ltd                                 |
 *                                                              |
 *   Written by Lubin KERHUEL -  http://www.kerhuel.eu          |
 *  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
 *   Version 0.99c+                            10-Apr-2009      |
 *   For Matlab 7.3             R2006b                          |
 *--------------------------------------------------------------
 */
#include "dummy.h"
#include "dummy_private.h"

/* Block signals (auto storage) */
BlockIO_dummy dummy_B;

/* Model step function */
void dummy_step(void)
{
  /* S-Function "dsPIC_Digital_Input" Block: <Root>/AN27 */
  dummy_B.AN27 = PORTEbits.RE3;

  /* S-Function "dsPIC_Digital_Input" Block: <Root>/AN28 */
  dummy_B.AN28 = PORTEbits.RE4;

  /* S-Function "dsPIC_Digital_Input" Block: <Root>/AN29 */
  dummy_B.AN29 = PORTEbits.RE5;

  /* S-Function "dsPIC_Digital_Input" Block: <Root>/AN30 */
  dummy_B.AN30 = PORTEbits.RE6;

  /* S-Function "dsPIC_Digital_Input" Block: <Root>/AN31 */
  dummy_B.AN31 = PORTEbits.RE7;
}

/* Model initialize function */
void dummy_initialize(boolean_T firstTime)
{
  (void)firstTime;

  /* Registration code */

  /* block I/O */
  (void) memset(((void *) &dummy_B),0,
                sizeof(BlockIO_dummy));

  /* S-Function "dsPIC_MASTER" initialization Block: <Root>/Master */
  /* 0 testfcy 	*/
  /*  5.0E+006	*/
  /* CONFIG TIMER 1 for scheduling steps 	*/
  ConfigIntTimer1(T1_INT_PRIOR_0 & T1_INT_OFF);
  T1CON = 0x8000 ;                     /* T1_PS_1_1	*/
  PR1 = 39999;

  /* Configuration TRIS */
  /* Configuration ADCHS */
  AD1PCFGL = (0);
  AD2PCFGL = (0);
}

/* File trailer for Real-Time Workshop generated code.
 *
 * [EOF]
 */
