---
title: "bug while compiling the PIC24Fj128GA010"
url: "/forum/topic/325/"
archiveKind: "topic"
---
# bug while compiling the PIC24Fj128GA010

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p1299">
<header><strong>francois.bateman</strong><time datetime="2010-09-27 16:23 UTC">2010-09-27 16:23 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I use an Explorer16 development card and I tried to compile the example that you have provided with a PIC24Fj128GA010 and I received the following message.<br>
<br>
On the other hand, I compiled it successfully with the dsPIc 33Fj256GP710 (also provided with the board). Have you already met any problem with the PIC24Fj128GA010.<br>
<br>
Regards, amicalement<br>
<br>
François<br>
<br>
.<br>
<br>
### Processing Template Makefile: C:\Users\François BATEMAN\Documents\Enseignement Recherche\Outils\install_dsPIC_R2007b_F_BATEMAN_Unlocked_SalonP_lsis\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Creating dsPIC_33f_Explorer16.mk from C:\Users\François BATEMAN\Documents\Enseignement Recherche\Outils\install_dsPIC_R2007b_F_BATEMAN_Unlocked_SalonP_lsis\dspic\dspic_pic30_gcc.tmf<br>
<br>
### Building dsPIC_33f_Explorer16: .\dsPIC_33f_Explorer16.bat<br>
<br>
 <br>
<br>
C:\Users\Fran‡ois BATEMAN\Documents\Enseignement Recherche\Outils\install_dsPIC_R2007b_F_BATEMAN_Unlocked_SalonP_lsis\examples\dsPIC_33f_Explorer16_dspic\sources&gt;set MATLAB=C:\Program Files\MATLAB\R2007b  <br>
<br>
 <br>
<br>
C:\Users\Fran‡ois BATEMAN\Documents\Enseignement Recherche\Outils\install_dsPIC_R2007b_F_BATEMAN_Unlocked_SalonP_lsis\examples\dsPIC_33f_Explorer16_dspic\sources&gt;"C:\PROGRA~1\MATLAB\R2007b\bin\win32\gmake" -f dsPIC_33f_Explorer16.mk  GENERATE_REPORT=1 MULTI_INSTANCE_CODE=0 PORTABLE_WORDSIZES=0 GENERATE_ASAP2=0 TMW_EXTMODE_TESTING=0  <br>
<br>
C:\\PROGRA~1\\MICROC~1\\MPLABC~1\\bin\\pic30-gcc  -c -mcpu=24fJ128GA010 -O3 -fschedule-insns -fschedule-insns2	 -O   -I. -I..\.. -IC:\PROGRA~1\MATLAB\R2007b/simulink/include -IC:\PROGRA~1\MATLAB\R2007b/extern/include -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/ert -IC:\PROGRA~1\MATLAB\R2007b/rtw/c/src/ext_mode/common -IC:\Users\FRANOI~1\DOCUME~1\ENSEIG~1\Outils\INSTAL~2\examples\DSPIC_~2\sources -IC:\Users\FRANOI~1\DOCUME~1\ENSEIG~1\Outils\INSTAL~2\examples -IC:\PROGRA~1\MATLAB\R2007b\rtw\c\libsrc   -I C:\PROGRA~1\MICROC~1\MPLABC~1\include    dsPIC_33f_Explorer16_main.c <br>
<br>
In file included from c:/progra~1/microc~1/mplabc~1/bin/bin/../../support/peripheral_24F/timer.h:35, <br>
<br>
                 from dsPIC_33f_Explorer16_private.h:47, <br>
<br>
                 from dsPIC_33f_Explorer16_main.c:28: <br>
<br>
c:/progra~1/microc~1/mplabc~1/bin/bin/../../support/peripheral_24F/GenericTypeDefs.h:53: error: syntax error before '(' token <br>
<br>
gmake: *** [dsPIC_33f_Explorer16_main.o] Error 255 <br>
<br>
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.</div>
</article>

<article class="forum-post" id="p1300">
<header><strong>LubinKerhuel</strong><time datetime="2010-09-28 15:54 UTC">2010-09-28 15:54 UTC</time></header>
<h3>Re: bug while compiling the PIC24Fj128GA010</h3>
<div class="forum-post-body">Hey François,<br>
<br>
<br>
<br>
Thanks for that remark.<br>
<br>
This error seems to be a file def problem from Microchip described quite a long time ago (see notes on release of blockset 13/02/2008 V0.96b <a href="/wiki/release-notes/">here</a> ). <br>
<br>
<br>
<br>
The workaround is to edit the Microchip def file GenericTypeDefs.h usually placed at (win XP 32 bits) :<br>
<br>
C:\Program Files\Microchip\MPLAB C30\support\peripheral_24F\GenericTypeDefs.h<br>
<br>
and to comment line 64 as follow :<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;in file : GenericTypeDefs.h
<wbr>
64 // typedef enum _BOOL { FALSE = 0, TRUE } BOOL;    /* Undefined size */
65 typedef enum _BIT { CLEAR = 0, SET } BIT;
</code></pre><br>
It should fix the problem. Let me know otherwise.<br>
<br>
<br>
<br>
Lubin</div>
</article>

