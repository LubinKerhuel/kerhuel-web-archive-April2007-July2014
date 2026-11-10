#include <p33FJ256MC710.h>

void QEIInit(void){
 // Config_QEI
 
    
  // Configure I/O Ports
  AD1PCFGL = ADPCFG | 0x0038;       // Disable the A/D pins 3, 4 and 5
  AD2PCFGL = ADPCFG | 0x0038;       // Disable the A/D pins 3, 4 and 5

  TRISB = TRISB | 0x38;           // configure pins 3, 4 and 5 as inputs
    
 //QEI configuration register 
 // POSCNT = 0x8000;                // Set Current Position to 8000 does't work, reset and speed effect ???
    MAXCNT = 1000;              // Use QEI in 2x mode and 500counts by roll
  //  DFLTCON = 0;                    // Digital filter set to off
  // DFLTCON = 0b0000000110100000;     // Digital filter set with 1:4 clock
  DFLTCON = 0b0000000100000000;        // Digital filter set to off, Count Error Interrupt Disable
  QEICON = 0;
  QEICONbits.QEIM = 5;           // x2 reset by MAXCNT pulse
  QEICONbits.POSRES = 1;         // doesn't Allow Index pulse to reset counter
  QEICONbits.SWPAB = 0;          // direction 
 
  //ConfigIntQEI 
    IEC3bits.QEIIE = 1;                // Enable QEI interrupt
    IPC14bits.QEIIP = 2;               // Interrupt priority level 2
    
   // extern volatile int ct_turns;
   // ct_turns = 0x8000;
    
}


double GetQEI()
{
 extern volatile int ct_turns;
 return (double) ct_turns * MAXCNT + POSCNT;
}




/*------------------------------------------------------------------*/
void __attribute__((__interrupt__)) _QEIInterrupt(void)
{
   extern volatile int ct_turns;
   // if it overflowed
     if (QEICONbits.UPDN ==  1){
       ct_turns++;
     } else {
       ct_turns--;
     }
     IFS3bits.QEIIF = 0;    // clear the interrupt flag
}
