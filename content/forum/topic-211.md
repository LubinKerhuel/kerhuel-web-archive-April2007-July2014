---
title: "Error using ==&gt; rs232gui"
url: "/forum/topic/211/"
archiveKind: "topic"
---
# Error using ==&gt; rs232gui

Forum : [General Remark and Questions](/forum/#forum-1)

7 message(s) · archive en lecture seule

<article class="forum-post" id="p796">
<header><strong>Simon_says</strong><time datetime="2009-03-23 17:52 UTC">2009-03-23 17:52 UTC</time></header>
<div class="forum-post-body">Hello Lubin:<br>
<br>
<br>
<br>
 See,  I have succesfully connected and send data through rs232 gui from dsPIC to matlab before. However, I have had trouble this time to plot data from the dsPIC. I´ve got the error message  below when I try to plot data. What am I doing wrong?  Please help! Attached is the model I am using...<br>
<br>
<br>
<br>
jose  luis<br>
<br>
<br>
<br>
Connecting... May take few seconds...<br>
<br>
Port COM1 successfully open at 115200............OK<br>
<br>
redefinition SerialCOM<br>
<br>
??? Attempted to access s_control_pos(1); index out of bounds because numel(s_control_pos)=0.<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 75<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\rs232gui.p&gt;pushStart_Callback at 271<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 95<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\rs232gui.p&gt;rs232gui at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error using ==&gt; rs232gui('pushStart_Callback',gcbo,[],guidata(gcbo))<br>
<br>
Attempted to access s_control_pos(1); index out of bounds because numel(s_control_pos)=0.<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/223-PID20ejeYanalnivels.mdl">Pièce jointe : PID20ejeYanalnivels.mdl</a></p>
</article>

<article class="forum-post" id="p797">
<header><strong>LubinKerhuel</strong><time datetime="2009-03-23 21:46 UTC">2009-03-23 21:46 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hi Jose Luis,<br>
<br>
<br>
<br>
You model has an original blocks disposition. I'll probably get inspired from it.<br>
<br>
<br>
Anyway, I do not see errors. <br>
<br>
When does the error appears ? at the connexion time or when you click on start ?  Let me know...<br>
<br>
If it appears when you click on start, there may be problems with bauds. You computer's serial port may be not tolerant enough to baud errors.<br>
<br>
The % error of the UART@115200 is 1.7%. It should be Ok in most case. Anyway, you may try using a 57600 bauds that will have an negative error (-1.3%). bauds of 38400 will also offer even less error...<br>
<br>
<br>
<br>
The problem may come from the electronic max232 like level translator.<br>
<br>
<br>
<br>
You may try to receive data as raw datas (button raw). But as the data will not be demultiplexed, you will get a nice mess...<br>
<br>
<br>
<br>
I do not know if that will help so much. I have hardly no problem with this interface. My feeling is that it is quite robust now.<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/224-shot_20090323223845-140.png">Pièce jointe : shot_20090323223845-140.png</a></p>
</article>

<article class="forum-post" id="p804">
<header><strong>Simon_says</strong><time datetime="2009-03-27 17:38 UTC">2009-03-27 17:38 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
 You see, the error appears several seconds after I press start. The UART has a succesful connection, then I press start and it seems like waiting for information.  It takes 20 or 30 seconds and then the error appear. It is odd because sometimes it works and sometimes it dos not. I am testing the system with the 57600  and the 38400 baud rate. So far, so good. I´ll post if an error comes up!<br>
<br>
<br>
<br>
 Thanks a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
</article>

<article class="forum-post" id="p854">
<header><strong>Simon_says</strong><time datetime="2009-05-28 21:50 UTC">2009-05-28 21:50 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hello every one!<br>
<br>
Hi Lubin... I am still getting the same problem when trying to log data on matlab wit the RS232gui.... this is the error I get:<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Connecting... May take few seconds...<br>
<br>
Port COM1 successfully open at 2400............OK<br>
<br>
redefinition SerialCOM<br>
<br>
??? Error using ==&gt; plus<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 117<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\rs232gui.p&gt;pushStart_Callback at 271<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 95<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\BLOCKS COMPRADOS\install_dsPIC_R2007a_JsOrtizSimonA\blocks\rs232gui.p&gt;rs232gui at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error using ==&gt; rs232gui('pushStart_Callback',gcbo,[],guidata(gcbo))<br>
<br>
Error using ==&gt; plus<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
??? Error while evaluating uicontrol Callback<br>
<br>
<br>
<br>
&gt;&gt; <br>
<br>
<br>
<br>
 And this is the model I am working with. It is a servomotor controller using force feedback to move a load. It is kind of big, but if you look at it, focus on the RS232 data transmission blocks. The model is running well, but can not see the graph. I have tried all the baud rates unsuccesfully. However, I have tried a different model ( a smaller one)  and the communication works fine!!!! Can anyone help me?<br>
<br>
 Thanks a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/242-PID23y.mdl">Pièce jointe : PID23y.mdl</a></p>
</article>

<article class="forum-post" id="p855">
<header><strong>Simon_says</strong><time datetime="2009-05-29 19:48 UTC">2009-05-29 19:48 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hello Lubin. Thanks for the updated blockset. I have installed it and try them with the same model. After I pressed start it seemed to work fine , but after 2 or 3 seconds I got this:<br>
<br>
<br>
<br>
Port COM1 successfully open at 1200............OK<br>
<br>
redefinition SerialCOM<br>
<br>
??? Error using ==&gt; plus<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\install_dsPIC_R2007a_JsOrtizSimon Updated\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 120<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\install_dsPIC_R2007a_JsOrtizSimon Updated\blocks\rs232gui.p&gt;pushStart_Callback at 271<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 95<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; C:\Documents and Settings\123\Escritorio\PICPROG CD\MATLAB BLOCKS\install_dsPIC_R2007a_JsOrtizSimon Updated\blocks\rs232gui.p&gt;rs232gui at 43<br>
<br>
<br>
<br>
<br>
<br>
??? Error using ==&gt; rs232gui('pushStart_Callback',gcbo,[],guidata(gcbo))<br>
<br>
Error using ==&gt; plus<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
<br>
<br>
 Here the first data recorded until crash and get the error message. Odd isn´t it?<br>
<br>
jose luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/244-first%20try.JPG">Pièce jointe : first try.JPG</a></p>
</article>

<article class="forum-post" id="p856">
<header><strong>LubinKerhuel</strong><time datetime="2009-05-29 22:27 UTC">2009-05-29 22:27 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hi Jose Luis,<br>
<br>
<br>
<br>
I find the error ;-)<br>
<br>
<br>
<br>
You are using the internal RC oscillator of the dsPIC. (FRC for Fast RC oscillator). It is very difficult to make the UART works properly with such oscillaotr as it is not precise enough (to my experience). Even if the dsPIC is supposed to run at 30MIPS (7.5MHz RC oscillator, with PLL 16, divided by 4 cycles/instructions).<br>
<br>
<br>
<br>
I can suggest the following :<br>
<br>
<strong>- add an external quartz or oscillator  ! that is much better</strong><br>
<br>
<br>
<br>
If not possible, you may try to find the frequency : generate a simulink for dsPIC generating a 1ms clock signal, and measure with you scope the real signal, note T the measured time. You may now compute the real MIPS of the microcontroller : <br>
<br>
<em>multiply the <strong>number of Instruction per Second</strong> (in the master block)  by (1ms/T)</em><br>
<br>
and repport this MIPS in the MASTER block (The true generated signal must be 1ms now ! ). Then, find an UART baud rate with a small % error (as indicated in the UART config block).<br>
<br>
<br>
<br>
Note however that even if it works for a while, as the temperature will change, the RC oscillator frequency will swift and you will have to do again the calibration process.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p857">
<header><strong>Simon_says</strong><time datetime="2009-06-02 22:43 UTC">2009-06-02 22:43 UTC</time></header>
<h3>Re: Error using ==&amp;gt; rs232gui</h3>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
 You were right!!!<br>
<br>
 I did use a cristal instead of internal clock. Now I can even see multiple inputs in the ADC. I am still working with 30MIPS and use a baud rate of 115200b . It really works! <br>
<br>
 <br>
<br>
 I am still testing it, but so far so good!!!<br>
<br>
Thanks for your support!! <br>
<br>
<br>
<br>
Jose Luis</div>
</article>

