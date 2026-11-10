/*
 * File: dsPIC_33f_Explorer16_main.c
 *
 * Real-Time Workshop code generated for Simulink model dsPIC_33f_Explorer16.
 *
 * Model version                        : 1.228
 * Real-Time Workshop file version      : 6.4  (R2006a)  03-Feb-2006
 * Real-Time Workshop file generated on : Mon Jul 13 12:07:12 2009
 * TLC version                          : 6.4 (Jan 31 2006)
 * C source code generated on           : Mon Jul 13 12:07:13 2009
 *--------------------------------------------------------------
 *   Embedded Coder for Microchip dsPIC family.                 |
 *   Generate .c and .h files from your Matlab/simulink model   |
 *   and compile the diagram to .hex and .coff file that can be |
 *   downloaded directly into the microcontroller               |
 *                                                              |
 * Licence Accorded to &&               Licence Name          &&|
 *                     &&               Companie              &&|
 *                                                              |
 *   Written by Lubin KERHUEL -  http://www.kerhuel.eu          |
 *  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
 *   Version &&Version&&                       &&  Date       &&|
 *   For Matlab && VerMatlab && && Release &&                   |
 *--------------------------------------------------------------
 */

#include "dsPIC_33f_Explorer16.h"
#include "dsPIC_33f_Explorer16_private.h"

_FSS( RSS_NO_RAM & SSS_NO_FLASH & SWRP_WRPROTECT_OFF )
_FGS( GCP_OFF & GSS_OFF & GWRP_OFF )

_FOSCSEL( FNOSC_PRI & IESO_OFF & 0xFFFF )
_FOSC( FCKSM_CSDCMD & OSCIOFNC_OFF & POSCMD_XT)

_FPOR( FPWRT_PWR1 )
_FWDT( FWDTEN_OFF )

_FICD( JTAGEN_OFF )

void rt_OneStep()
{

  boolean_T eventFlags[2];
  int_T i;

  /* Disable interrupts here */

  /* Save FPU context here (if necessary) */
  /* Re-enable timer or interrupt here */

  dsPIC_33f_Explorer16_SetEventsForThisBaseStep(eventFlags);
  dsPIC_33f_Explorer16_step(0);

  for (i = 1; i < 2; i++) {
    if (eventFlags[i]) {

      dsPIC_33f_Explorer16_step(i);
    }
  }

  /* Disable interrupts here */
  /* Restore FPU context here (if necessary) */
  /* Enable interrupts here */
}

int main(void)
{
  PLLFBD = 0;                           /* configure clock speed */
  CLKDIV = 0;
  /* Initialize model */
  dsPIC_33f_Explorer16_initialize(1);

  /* Associate rt_OneStep() with a timer that executes at the base rate of the model */
  for(;;)
  {

    /* Associate rt_OneStep() with a timer that executes at the base rate of the model */

    while(!_T1IF);
    _T1IF = 0;

    rt_OneStep();
  }
}

/* File trailer for Real-Time Workshop generated code.
 *
 * [EOF]
 */
