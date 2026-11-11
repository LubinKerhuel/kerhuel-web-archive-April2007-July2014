---
title: "PIC24 RS-232???"
url: "/forum/topic/255/"
archiveKind: "topic"
---
# PIC24 RS-232???

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1002">
<header><strong>dilhat</strong><time datetime="2009-11-17 14:27 UTC">2009-11-17 14:27 UTC</time></header>
<div class="forum-post-body">Hi, i'm using pic24f explorer development board and try to send data from serial port (RS232) to PC. All the configurations of terminal and COM settings are ok but i can not monitor wright character. i use the serial port monitor program for catch hex codes and generally received hex codes are like "00 00" form or different character but not sended data. trying different boudrates can not solve my problem. if you have any idea please share me. <br>
<br>
<br>
<pre><code>#include "p24fj128ga010.h"
<wbr>
#define CTS _RF12
#define RTS _RF13
<wbr>
#define BRATE 34
<wbr>
#define U_ENABLE 0x8008
#define U_TX 0x0400
<wbr>
<wbr>
void initU2(void){
<wbr>
U2BRG=BRATE;
U2MODE=U_ENABLE;
U2STA=U_TX;
<wbr>
TRISF=0xDFFF;
RTS=1;
}
<wbr>
int putU2(int c){
while(CTS);
while(U2STAbits.UTXBF);
U2TXREG=c;
}
<wbr>
char getU2(void){
RTS=0;
while(!U2STAbits.URXDA);
return U2RXREG;
RTS=1;
}
<wbr>
main(){
char c;
<wbr>
initU2();
<wbr>
putU2('b');
<wbr>
while(1){
<wbr>
c=getU2();
<wbr>
putU2(c);
}
}
</code></pre></div>
</article>

<article class="forum-post" id="p1003">
<header><strong>LubinKerhuel</strong><time datetime="2009-11-17 15:39 UTC">2009-11-17 15:39 UTC</time></header>
<h3>Re: PIC24 RS-232???</h3>
<div class="forum-post-body">Provided you have simulink, try to program your dsPIC using Simulink and this blockset : <a href="/wiki/release-notes/">http://archive.kerhuel.eu/wiki/Release_Notes</a><br>
<br>
Otherwise, you would porbably get better responses on the microchip forum.<br>
<br>
<br>
<br>
Lubin</div>
</article>

