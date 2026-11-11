---
title: "dspic building error - solved"
url: "/forum/topic/145/"
archiveKind: "topic"
---
# dspic building error - solved

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p456">
<header><strong>JacquesKleynhans</strong><time datetime="2008-08-13 20:35 UTC">2008-08-13 20:35 UTC</time></header>
<div class="forum-post-body">Hi i bought my Expl 16 dev kit this morning but have a few problems building the sim blocks examples provided.<br>
<br>
I am using Matlab 2007b and also installed the embedded toolbox for 2007b"Super great toolbox"<br>
<br>
<br>
<br>
My problem is<pre><code>Error building Real-Time Workshop target for block diagram 'dsPIC_33f_Explorer16'. MATLAB error message:
Error using ==&gt; rtw_create_directory_path at 26
Error creating directory 'C:\Program Files\MATLAB\R2007b\My Work\slprj' : The directory or file cannot be created.</code></pre><br>
<br>
Something dodge is going on. I am very new to matlab so solving it myself, dont even ask!! I copied the .hex file and programed it to the board with mplab<br>
<br>
and used the rs232 gui" not the one in the sim example" but actually typing "rs232gui in the gui of matlab and this works fine.<br>
<br>
<br>
<br>
I am just struggeling with the building and compliing in matlab.<br>
<br>
<br>
<br>
Any Help greatly appreciated<br>
<br>
<br>
<br>
Kind Regards<br>
<br>
Jacques Kleynhans</div>
</article>

<article class="forum-post" id="p457">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-13 22:17 UTC">2008-08-13 22:17 UTC</time></header>
<h3>Re: dspic building error</h3>
<div class="forum-post-body">Hi Jacques,<br>
<br>
<br>
<br>
I did not encounter such a bug where matlab cannot create a directory. <br>
<br>
You should avoid working in the c:\program file\... directory!<br>
<br>
Try copy your working file somewhere else and try again.<br>
<br>
<br>
<br>
If it does not work, you could try to create the slprj directory from the matlab prompt : &gt;&gt;mkdir slprj<br>
<br>
<br>
<br>
It is not clear if you manage to compile the provided example for the explorer 16 board.<br>
<br>
If it did not compile, how did you generates the .hex file? Did you use one .hex taken from the website?<br>
<br>
<br>
<br>
Regards<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p458">
<header><strong>JacquesKleynhans</strong><time datetime="2008-08-14 11:08 UTC">2008-08-14 11:08 UTC</time></header>
<h3>Re: dspic building error</h3>
<div class="forum-post-body">Ok i moved my working to file to another place that seemed to solve the building error. Thanks!!<br>
<br>
<br>
<br>
But now when i compile i get a long list of good news and a short one of bad<br>
<pre><code>"### Creating rtwlib.a " 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-ar -r rtwlib.a rt_backsubcc_dbl.o rt_backsubcc_sgl.o rt_backsubrc_dbl.o rt_backsubrc_sgl.o rt_backsubrr_dbl.o rt_backsubrr_sgl.o rt_enab.o rt_forwardsubcc_dbl.o rt_forwardsubcc_sgl.o rt_forwardsubcr_dbl.o rt_forwardsubcr_sgl.o rt_forwardsubrc_dbl.o rt_forwardsubrc_sgl.o rt_forwardsubrr_dbl.o rt_forwardsubrr_sgl.o rt_look.o rt_look1d.o rt_look1d32.o rt_look2d32_general.o rt_look2d32_normal.o rt_look2d_general.o rt_look2d_normal.o rt_look32.o rt_lu_cplx.o rt_lu_cplx_sgl.o rt_lu_real.o rt_lu_real_sgl.o rt_matdivcc_dbl.o rt_matdivcc_sgl.o rt_matdivcr_dbl.o rt_matdivcr_sgl.o rt_matdivrc_dbl.o rt_matdivrc_sgl.o rt_matdivrr_dbl.o rt_matdivrr_sgl.o rt_matmultandinccc_dbl.o rt_matmultandinccc_sgl.o rt_matmultandinccr_dbl.o rt_matmultandinccr_sgl.o rt_matmultandincrc_dbl.o rt_matmultandincrc_sgl.o rt_matmultandincrr_dbl.o rt_matmultandincrr_sgl.o rt_matmultcc_dbl.o rt_matmultcc_sgl.o rt_matmultcr_dbl.o rt_matmultcr_sgl.o rt_matmultrc_dbl.o rt_matmultrc_sgl.o rt_matmultrr_dbl.o rt_matmultrr_sgl.o rt_sat_div_int16.o rt_sat_div_int32.o rt_sat_div_int8.o rt_sat_div_uint16.o rt_sat_div_uint32.o rt_sat_div_uint8.o rt_sat_prod_int16.o rt_sat_prod_int32.o rt_sat_prod_int8.o rt_sat_prod_uint16.o rt_sat_prod_uint32.o rt_sat_prod_uint8.o  
"### rtwlib.a Created" 
C:\\PROGRA~1\\MICROC~1\\MPLABC~2\\bin\\pic30-ld   -t --report-mem -Map ../untitled.map --heap 0  -cref -T C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256GP710.gld -o ..\../dsPIC_33f_Explorer16.coff  dsPIC_33f_Explorer16_main.o dsPIC_Multiplexed_out_UART2.o dsPIC_UART2_Interrupt.o dsPIC_33f_Explorer16.o     rtwlib.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC33F\libp33fJ256GP710-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a 
C:\PROGRA~1\MICROC~1\MPLABC~2\bin\pic30-coff-ld: cannot open linker script file C:\PROGRA~1\MICROC~1\MPLABC~2\support\dsPIC33F\gld\p33fJ256GP710.gld: No such file or directory 
gmake: *** [..\../dsPIC_33f_Explorer16.coff] Error 255 
### Real-Time Workshop build procedure for model: 'dsPIC_33f_Explorer16' aborted due to an error.
C30 Compiler found
C30 Compiler found
C30 Compiler found
C30 Compiler found
Model configured...</code></pre><br>
<br>
Oya and that hex file i got from <a href="/wiki/explorer-16-board/">http://archive.kerhuel.eu/wiki/Explorer_16_Board</a><br>
<br>
<br>
<br>
Thanks<br>
<br>
Jacques Kleynhans</div>
</article>

<article class="forum-post" id="p461">
<header><strong>LubinKerhuel</strong><time datetime="2008-08-14 17:21 UTC">2008-08-14 17:21 UTC</time></header>
<h3>Re: dspic building error</h3>
<div class="forum-post-body">- Please Check that you are using the C30 compiler version 3.10 or above.<br>
<br>
<br>
<br>
Then, you could find the .gld file required, copy it into the root directory c:\<br>
<br>
On your simulink model, go to:<br>
<br>
Simulation ==&gt; Configuration Parameters ==&gt; DsPIC Options<br>
<br>
Change the line LDPICTYPE from<br>
<br>
<strong>-T C:\PROGRA~1\MICROC~1\MPLABC~1\support\dsPIC30F\gld\p30f3012.gld</strong><br>
<br>
to <strong>-T C:\p30f3012.gld</strong><br>
<br>
And Compile!<br>
<br>
<br>
<br>
Matab should find the file with such a simple path!<br>
<br>
<br>
<br>
You may find useful information on others topics : <br>
<br>
<a href="/forum/topic/116/">viewtopic.php?f=4&amp;t=116</a><br>
<br>
<br>
<br>
Let know if you still get the problem.</div>
</article>

<article class="forum-post" id="p462">
<header><strong>JacquesKleynhans</strong><time datetime="2008-08-14 22:39 UTC">2008-08-14 22:39 UTC</time></header>
<h3>Re: dspic building error</h3>
<div class="forum-post-body">:D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D <br>
<br>
 :D Great Support Everything works i updated my compiler :D <br>
<br>
 :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D  :D <br>
<br>
<br>
<br>
Kind Regards<br>
<br>
Jacques Kleynhans</div>
</article>

