---
title: "Data Comunication - rs232GUI - Signed Number"
url: "/forum/topic/103/"
archiveKind: "topic"
---
# Data Comunication - rs232GUI - Signed Number

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p281">
<header><strong>Anonyme</strong><time datetime="2008-04-04 00:29 UTC">2008-04-04 00:29 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I am want to log data that from my encoder using the qei that is<br>
<br>
sometimes negative using the TX Output Multiplexed for matlab, but<br>
<br>
think it can only be used with signed values. Is it possible to configure the <br>
<br>
Tx Output Multiplexed to support negative values or a modification to the block software is<br>
<br>
necesary, and how is this achieved?<br>
<br>
<br>
<br>
I would like to know how the data is sent to PC serial port from the dsPic so I can<br>
<br>
may be able to interprete the data as signed unisng other matlab tools (external mode for example).<br>
<br>
<br>
<br>
Thanks.<br>
<br>
A. Soria.<br>
<br>
<br>
<br>
<br>
<br>
PS. My qei version for the 30f4012<br>
<br>
<br>
<br>
<br>
<br>
include &lt;qei.h&gt;<br>
<br>
#include &lt;p30f4012.h&gt;<br>
<br>
#include &lt;ports.h&gt;<br>
<br>
<br>
<br>
#include "rtwtypes.h"<br>
<br>
 <br>
<br>
int ct_turns;<br>
<br>
<br>
<br>
<br>
<br>
#define TRIS_QEA _TRISB4<br>
<br>
#define TRIS_QEB _TRISB5<br>
<br>
#define ENTRADA 1<br>
<br>
#define SALIDA 0<br>
<br>
<br>
<br>
void QEIInit(void)<br>
<br>
{<br>
<br>
    ct_turns=0;<br>
<br>
    ADPCFG = 0xFF;<br>
<br>
	TRIS_QEA=ENTRADA;<br>
<br>
	TRIS_QEB=ENTRADA;<br>
<br>
    <br>
<br>
	WriteQEI(0xFFFF);<br>
<br>
	ConfigIntQEI(QEI_INT_ENABLE &amp; QEI_INT_PRI_3);<br>
<br>
	OpenQEI(QEI_DIR_SEL_QEB &amp;<br>
<br>
			QEI_INPUTS_NOSWAP &amp;<br>
<br>
			QEI_MODE_x4_MATCH,0);<br>
<br>
	POSCNT = 0;<br>
<br>
	return;<br>
<br>
}<br>
<br>
   <br>
<br>
 void __attribute__((interrupt,auto_psv)) _QEIInterrupt(void)<br>
<br>
{<br>
<br>
	if(POSCNT==0)<br>
<br>
		ct_turns++;<br>
<br>
	if(POSCNT==0xFFFF)<br>
<br>
		ct_turns--;<br>
<br>
	_QEIIF=0;<br>
<br>
}<br>
<br>
    <br>
<br>
<br>
<br>
int32_T GetQEI(void)<br>
<br>
{<br>
<br>
    return (int32_T)(ct_turns*65535 +POSCNT);<br>
<br>
      <br>
<br>
}</div>
</article>

<article class="forum-post" id="p282">
<header><strong>LubinKerhuel</strong><time datetime="2008-04-04 09:26 UTC">2008-04-04 09:26 UTC</time></header>
<div class="forum-post-body">Hi Alberto,<br>
<br>
<br>
<br>
Receiving signed data is a problem of interpretation.<br>
<br>
The m code that plot data as signed for int16 data type is done.<br>
<br>
Just press the "dflt signe" (for default signed) at the top of the rs232gui user interface and this m code will replace current m  code in the interface.<br>
<br>
This code must be adapted if you use int8 or int83 data. Also you have to adapt if you use signed data on one channel and unsigned data another channel<br>
<br>
<br>
<br>
Thanks for providing your version of QEI peripheral code.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/51-rs232GUI_dfltSigned.png">Pièce jointe : rs232GUI_dfltSigned.png</a></p>
</article>

