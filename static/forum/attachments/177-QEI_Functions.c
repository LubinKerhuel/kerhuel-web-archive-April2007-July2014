#include <p30f4012.h>
#include <qei.h>

void QEIInit(void){
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
           QEI_QE_CLK_DIVIDE_1_16 &// Filter 1:16 divider
           QEI_QE_OUT_ENABLE);    // Enable the input digital filter

}

long GetQEI()
{
	extern volatile unsigned int ct_turns;
	return (long) ct_turns * 65535 + POSCNT;
}


void __attribute__((__interrupt__)) _QEIInterrupt(void)
{
	extern volatile unsigned int ct_turns;
	// if it overflowed
	  if (ReadQEI() < 0x3FFF){
	    ct_turns++;
	  } else {
	    ct_turns--;
	  }
	 // clear the interrupt flag
	  IFS2bits.QEIIF =0;
}
