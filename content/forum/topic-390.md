---
title: "mcp23017"
url: "/forum/topic/390/"
archiveKind: "topic"
---
# mcp23017

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1556">
<header><strong>davc22</strong><time datetime="2011-04-24 00:28 UTC">2011-04-24 00:28 UTC</time></header>
<div class="forum-post-body">hi ,<br>
<br>
<br>
<br>
i'm using 18F4620 with MCP23017 . the interface is I2C. <strong>i have no problem writing to MCP</strong> but i can't read.the mcp always return 0xC2.<br>
<br>
thanks for any help<br>
<br>
<br>
<br>
david<br>
<br>
<br>
<br>
<br>
<br>
#include &lt;p18cxxx.h&gt; <br>
<br>
#include "I2C.h"<br>
<br>
#include "Ports.h"<br>
<br>
#include "TypeDef.h"<br>
<br>
/******************************************************************/<br>
<br>
// Function:OpenI2C<br>
<br>
// Action  : This open the MSSP module &amp; Set it <br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
void OpenI2C(void)<br>
<br>
{<br>
<br>
//Reseting MSSP registers<br>
<br>
 SSPCON1 = 0x00; <br>
<br>
 SSPCON2 = 0x00;   <br>
<br>
// Set Ports<br>
<br>
I2C_SCL_AS_INPUT;<br>
<br>
I2C_SDA_AS_INPUT;<br>
<br>
// Disable Slew Rate<br>
<br>
SSPSTAT |= 0x80 ;<br>
<br>
// Set Baud Rate<br>
<br>
SSPADD = SSPADD_FOR_BAUD ;<br>
<br>
// Set Mode and enable Module<br>
<br>
SSPCON1 = I2C_MSTR_MOD + I2C_ENA ;<br>
<br>
PIR1bits.SSPIF = 0;//reset MSSP interrupt flag bi<br>
<br>
}// end of OpenI2C()<br>
<br>
<br>
<br>
/******************************************************************/<br>
<br>
// Function:IdleI2C<br>
<br>
// Action  :  sample status bits and wait for the bus   To Be free         <br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
void IdleI2C(void)<br>
<br>
 {<br>
<br>
     //Test and wait until I2C module is idle<br>
<br>
     while ( (SSPCON2 &amp; 0x1F) | (SSPSTATbits.R_W) ) <br>
<br>
         continue; //keep looping until idle<br>
<br>
 }//end of IdleI2C()<br>
<br>
<br>
<br>
/******************************************************************/<br>
<br>
// Function:NotAckI2C<br>
<br>
// Action  : Send nACK to slave(@ after received data)         <br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
void NotAckI2C(void)<br>
<br>
 {<br>
<br>
 <br>
<br>
     SSPCON2bits.ACKDT = 1; // set acknowledge bit for NOT ACK<br>
<br>
 <br>
<br>
     SSPCON2bits.ACKEN = 1; // initiate bus acknowledge sequence<br>
<br>
 <br>
<br>
 }//end of NotAckI2C()<br>
<br>
 <br>
<br>
/******************************************************************/<br>
<br>
// Function:StartI2C<br>
<br>
// Action  : Generate Start Bit and wait for flag to rise<br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
void StartI2C(void)<br>
<br>
 {<br>
<br>
     SSPCON2bits.SEN = 1; //Initiate Start condition<br>
<br>
     while(!PIR1bits.SSPIF ); //wait for Flag To rise<br>
<br>
     PIR1bits.SSPIF = 0; //reset MSSP interrupt flag bit<br>
<br>
 }//end of StartI2C()<br>
<br>
<br>
<br>
/******************************************************************/<br>
<br>
// Function:ReStartI2C<br>
<br>
// Action  : Generate ReStart Bit and wait for flag to rise<br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
 void ReStartI2C(void)<br>
<br>
 {<br>
<br>
     SSPCON2bits.RSEN = 1; //Initiate Start condition<br>
<br>
     while(!PIR1bits.SSPIF ); //wait for Flag To rise<br>
<br>
     PIR1bits.SSPIF = 0; //reset MSSP interrupt flag bit<br>
<br>
 }//end of StartI2C()<br>
<br>
/******************************************************************/<br>
<br>
// Function:Stop I2C<br>
<br>
// Action  :  Generate Stopt Bit and wait for flag to rise<br>
<br>
// Code    :<br>
<br>
// Input   :<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
 void StopI2C(void)<br>
<br>
 {<br>
<br>
     SSPCON2bits.PEN = 1; //Generate Stop condition<br>
<br>
     while(!PIR1bits.SSPIF ); //wait for interrupt<br>
<br>
     PIR1bits.SSPIF = 0; //reset MSSP interrupt flag bit   <br>
<br>
 <br>
<br>
 }//end of StopI2C()<br>
<br>
<br>
<br>
/******************************************************************/<br>
<br>
// Function:WriteI2C<br>
<br>
// Action  : Write byte to slave<br>
<br>
// Code    :<br>
<br>
// Input   :Data byte<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
<br>
<br>
Byte  WriteI2C(Byte data_out)<br>
<br>
 {<br>
<br>
     SSPCON2bits.ACKSTAT = 1; //reset ACK bit flag<br>
<br>
     SSPBUF = data_out;       // write single byte to SSPBUF<br>
<br>
     if(SSPCON1bits.WCOL )  // test if write collision occurred<br>
<br>
     {<br>
<br>
         SSPCON1bits.WCOL = 0;     //Reset collision bit<br>
<br>
         while(SSPSTATbits.BF );   // wait until write cycle is complete                                <br>
<br>
     }<br>
<br>
     while(!PIR1bits.SSPIF); //wait for interrupt<br>
<br>
     PIR1bits.SSPIF = 0; //reset MSSP interrupt flag bit<br>
<br>
     if(!SSPCON2bits.ACKSTAT ) //Was there an ACK sent from MCP?<br>
<br>
         return ACK; //MCP  sent ACK<br>
<br>
     else <br>
<br>
         return NACK; //No ACK was sent<br>
<br>
         <br>
<br>
       <br>
<br>
 } //end of WriteI2C()<br>
<br>
/******************************************************************/<br>
<br>
// Function:Read byte from slave <br>
<br>
// Action  : Write byte to slave<br>
<br>
// Code    :<br>
<br>
// Input   :Data byte<br>
<br>
// Output  :<br>
<br>
//*****************************************************************/<br>
<br>
Byte  ReadI2C(void)<br>
<br>
 {<br>
<br>
     IdleI2C();  //Wait bus to be free<br>
<br>
     SSPCON2bits.RCEN = 1;     // enable master for 1 byte reception<br>
<br>
 <br>
<br>
     while (SSPSTATbits.BF == 0); // wait until byte received <br>
<br>
 <br>
<br>
     while(PIR1bits.SSPIF == 0); //wait for interrupt<br>
<br>
 <br>
<br>
     PIR1bits.SSPIF = 0; //reset MSSP interrupt flag bit<br>
<br>
 <br>
<br>
     return SSPBUF;    // return with read byte<br>
<br>
 <br>
<br>
 }//end of ReadI2C()<br>
<br>
/******************************************************************/<br>
<br>
// Function:I2CWriteByteToMCP<br>
<br>
// Action  :Write To Mcp23017 GPIO expender.It sends 3 Bytes : first the Ic address , <br>
<br>
//           internal Register Address , the last byte is the register data <br>
<br>
// Code    :<br>
<br>
// Input   :Byte ICadd,Byte Regadd,Byte Regdata<br>
<br>
// Output  :Byte : NACK or ACK<br>
<br>
//*****************************************************************/<br>
<br>
<br>
<br>
Byte I2CWriteByteToMCP(Byte ICadd,Byte Regadd,Byte Regdata)<br>
<br>
{<br>
<br>
 OpenI2C();  //Configure &amp; Open Module<br>
<br>
 IdleI2C();  //Wait bus to be free<br>
<br>
 StartI2C(); //Generates a Start I2C condition<br>
<br>
 IdleI2C();  //Wait bus to be free<br>
<br>
// Write Device Address<br>
<br>
 if (WriteI2C(ICadd | WrtCmd ) == NACK)<br>
<br>
 {<br>
<br>
  while(1); //STOP program<br>
<br>
 }<br>
<br>
<br>
<br>
// Write Register Address<br>
<br>
 if (WriteI2C(Regadd ) == NACK)<br>
<br>
 {<br>
<br>
  while(1); //STOP program<br>
<br>
 }<br>
<br>
 <br>
<br>
// Write Register Data<br>
<br>
 if (WriteI2C(Regdata ) == NACK)<br>
<br>
 {<br>
<br>
 while(1); //STOP program<br>
<br>
<br>
<br>
 }<br>
<br>
Nop();<br>
<br>
// Send stop bit<br>
<br>
  StopI2C();<br>
<br>
<br>
<br>
} <br>
<br>
// end  I2CWriteByteToMCP()<br>
<br>
/******************************************************************/<br>
<br>
// Function:ReadByteFromMCp<br>
<br>
// Action  :ReadFrom Mcp23017 GPIO expender.<br>
<br>
// Code    :<br>
<br>
// Input   :Byte ICadd,Byte Regadd<br>
<br>
// Output  :Byte : data<br>
<br>
//*****************************************************************/<br>
<br>
Byte ReadByteFromMCp(Byte ICadd,Byte Regadd)<br>
<br>
<br>
<br>
{<br>
<br>
 Byte data_byte = 0; //variable to hold the data byte from the SLAVE<br>
<br>
 OpenI2C();  //Configure &amp; Open Module<br>
<br>
 IdleI2C();  //Wait bus to be free<br>
<br>
 StartI2C(); //Generates a Start I2C condition<br>
<br>
 IdleI2C();  //Wait bus to be free<br>
<br>
// Write Device Address<br>
<br>
 if (WriteI2C(ICadd | WrtCmd ) == NACK)<br>
<br>
 {<br>
<br>
  while(1); //STOP program<br>
<br>
 }<br>
<br>
<br>
<br>
// Write Register Address<br>
<br>
 if (WriteI2C(Regadd ) == NACK)<br>
<br>
 {<br>
<br>
  while(1); //STOP program<br>
<br>
 }<br>
<br>
IdleI2C();  //Wait bus to be free<br>
<br>
ReStartI2C();<br>
<br>
//StartI2C(); //Generates a Start I2C condition<br>
<br>
if (WriteI2C(ICadd | ReadCmd) == NACK)<br>
<br>
 {<br>
<br>
  while(1); //STOP program<br>
<br>
 }<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
data_byte = ReadI2C(); //read the received data from the SLAVE<br>
<br>
<br>
<br>
 //data_byte = ReadI2C(); //read the received data from the SLAVE<br>
<br>
NotAckI2C(); //Generates a Not Ack condition after reading data<br>
<br>
    <br>
<br>
StopI2C(); //Generates a Stop I2C condition<br>
<br>
<br>
<br>
IdleI2C(); //Loops until I2C BUS is Idle  <br>
<br>
 <br>
<br>
return data_byte; //return data byte from SLAVE<br>
<br>
<br>
<br>
}</div>
</article>

<article class="forum-post" id="p1557">
<header><strong>davc22</strong><time datetime="2011-04-25 15:27 UTC">2011-04-25 15:27 UTC</time></header>
<h3>Re: mcp23017</h3>
<div class="forum-post-body">it's o.k. i have solved the problem.</div>
</article>

