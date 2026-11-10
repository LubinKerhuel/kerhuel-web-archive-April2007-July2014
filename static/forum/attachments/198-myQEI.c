//#include "myQEI.h"

#include <p30f4012.h>   //////////////

#include <qei.h>
#include "rtwtypes.h"
 
int ct_turns = 0;
//extern volatile unsigned int POSCNT __attribute__((__sfr__));

void QEIInit(void)
{
    
  // Configure I/O Ports
  ADPCFG =ADPCFG | 0x0030; 
  TRISB = 0xFFFF; //TRISB | 0x0030;        // configure pins 4 and 5 as inputs
  TRISD =0;	 //  configure PORT D as outputs////////////////////				
	
 
  // Disable Interrupt Nesting (Errata 80215F)
  INTCON1bits.NSTDIS = 1;
  
  ConfigIntQEI (QEI_INT_ENABLE &  // Enable interrupts
               QEI_INT_PRI_5);   // Set Priority to 5

POSCNT = 0;                     // Set Current Position to 0
MAXCNT = 0xFFFF;                // Use the full 16bit counter

OpenQEI (QEI_DIR_SEL_CNTRL &    // UPDN bit decides direction count
          QEI_INT_CLK &          // Use FCY for clocking
          QEI_INDEX_RESET_DISABLE &
          QEI_CLK_PRESCALE_1 &    // 1:1 Prescale
          QEI_GATED_ACC_DISABLE &
          QEI_NORMAL_IO &        // QEI Control state of IO pin
          QEI_INPUTS_NOSWAP &    // Channels A and B are not swapped
          QEI_MODE_x2_MATCH &    // X2 mode with counter reset by match
          QEI_UP_COUNT &         // Read only for this mode
          QEI_IDLE_STOP,         // Stop in idle operation
          MATCH_INDEX_INPUT_PHASEA &
          QEI_QE_CLK_DIVIDE_1_256 &// Filter 1:16 divider
          QEI_QE_OUT_DISABLE);    // Enable the input digital filter
}

void __attribute__((__interrupt__, no_auto_psv)) _QEIInterrupt(void){

    // if it overflowed
    if (ReadQEI() < 0x3FFF){
        ct_turns++;
    } else {
        ct_turns--;
    }
    // clear the interrupt flag
    IFS2bits.QEIIF =0;
}

int32_T GetQEI(void)
{
     return (int32_T)(ct_turns*65535 + ReadQEI());
} 


/////////////////////////////////////////
int CERO(int x)
{
 
if (x==1) 
    {
	  POSCNT = 0;                     // Set Current Position to 0
	  //PORTDbits.RD1=1;
     }
  

}