---
title: "rs232gui data format"
url: "/forum/topic/375/"
archiveKind: "topic"
---
# rs232gui data format

Forum : [General Remark and Questions](/forum/#forum-1)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p1522">
<header><strong>ismaeelbit</strong><time datetime="2011-03-29 10:38 UTC">2011-03-29 10:38 UTC</time></header>
<div class="forum-post-body">Dear Lubin,<br>
<br>
I regarding the rs232 data format, I have tried to use int16 button and also simulate the data in Matlab.<br>
<br>
The results are included in the attachment together with signal block setting.<br>
<br>
<br>
<br>
I noticed the amplute to be aroung -1600 instead of 1000 input amplitude.<br>
<br>
<br>
<br>
what do you think is wrong?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/397-Data%20Logging%20results.docx">Pièce jointe : Data Logging results.docx</a></p>
</article>

<article class="forum-post" id="p1523">
<header><strong>LubinKerhuel</strong><time datetime="2011-03-29 11:28 UTC">2011-03-29 11:28 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">Ismaeel,<br>
<br>
<br>
<br>
I do not see reasons for this problem.<br>
<br>
There might then be a problem with your electronics.<br>
<br>
Could you check the UART signal on a scope, is the signal clean (no capacitance). Check also the timing of UART bits.<br>
<br>
Are you using external quartz, or the internal RC oscillator (which is not precise enough)<br>
<br>
<br>
<br>
You could also try to make a blinking led at 1Khz (1ms) and checking the timing with a scope.<br>
<br>
<br>
<br>
You may also try to use faster UART baud so as to have a delay between data sent at each step  to allows resynchronization of UART for the case your quartz is not precise enough. Currently, your UART is overloaded as 6 bytes should be sent at each time step, but UART baud rate of 19600 allows only sending 1.9 data thus, all data are not being sent, and the UART is emitting continuously.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1529">
<header><strong>ismaeelbit</strong><time datetime="2011-04-02 10:01 UTC">2011-04-02 10:01 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">Lubin,<br>
<br>
thanks for the support.<br>
<br>
I already check external oscillator freq. and is ok at 8Mhz, also the LED blinks at 1s when tested. But when I increased the baud to 115200 I got this error:<br>
<blockquote>?? Error using ==&gt; plus<br>
<br>
Matrix dimensions must agree.<br>
<br>
<br>
<br>
Error in ==&gt; D:\EMBEDDED WORKS\blocks\RS232_analyzBloc.p&gt;RS232_analyzBloc at 120<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; D:\EMBEDDED WORKS\blocks\rs232gui.p&gt;pushStart_Callback at 305<br>
<br>
<br>
<br>
<br>
<br>
Error in ==&gt; gui_mainfcn at 96<br>
<br>
        feval(varargin{:});<br>
<br>
<br>
<br>
Error in ==&gt; D:\EMBEDDED WORKS\blocks\rs232gui.p&gt;rs232gui at 43</blockquote><br>
<br>
<br>
<br>
But I tried it now with explorer 16 board is ok with 115200 baud rate. <br>
<br>
<br>
<br>
What does about error messages imply?</div>
</article>

<article class="forum-post" id="p1530">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-02 10:48 UTC">2011-04-02 10:48 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : ismaeelbit</header>What does about error messages imply?</blockquote><br>
By default, the rs232gui interface try to decode a frame whose definition is detailed <a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">here (french)</a><br>
<br>
<br>
<br>
If data are too much corrupted, this error may appear.<br>
<br>
You may try to reset the buffer (push button resetBuffer), bug if there is a problem with the UART rate, the error will appears again.<br>
<br>
<br>
<br>
You could disable the frame decoding pressing once the raw button. Note that you will then get the raw data receiving by the PC UART (or virtual UART for Bluetooth connexion for example). It may be a way to manually check for data integrity.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1537">
<header><strong>ismaeelbit</strong><time datetime="2011-04-08 12:50 UTC">2011-04-08 12:50 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">Hi Lubin, <br>
<br>
sorry for my disturbance. Am yet to get over the data transmission issue. I already got explorer 16 boar to examine the rs232gui data logging exercise am working on. I got good result with Matlab signal generator but with potentiometer and other external sensor, the data still remains corrupted. I hereby atatched the results for both the signal generator and onboard potentiometer on explorer 16.<br>
<br>
<br>
<br>
Incase u have a sample mdl for external sensor u have tried, kindly let me know so as to compare if it is my setting is the one that is wrong or what do u suggest?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/401-Data%20Logging%20results%20with%20explorer%2016.docx">Pièce jointe : Data Logging results with explorer 16.docx</a></p>
</article>

<article class="forum-post" id="p1538">
<header><strong>ismaeelbit</strong><time datetime="2011-04-08 12:52 UTC">2011-04-08 12:52 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">here is my simulink model for your reference</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/402-Data_Login_E3.mdl">Pièce jointe : Data_Login_E3.mdl</a></p>
</article>

<article class="forum-post" id="p1539">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-08 14:45 UTC">2011-04-08 14:45 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">Ismaeel,<br>
<br>
<br>
<br>
I could not figure out what the problem is as your docx file (please prefere to upload .png or .jpg file) shows the three output you sent to the Rx-Tx matlab block. Red curve is the matlab generated square signal, and blue and green are the ADC output raw data and its filtered version.<br>
<br>
ADC data are 10 bits integer. Thus to convert the represented value to Volt, you should multiply by 3.3 / 2^10 (provided you are using a 3.3V cards which is probably the case)<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1543">
<header><strong>ismaeelbit</strong><time datetime="2011-04-13 12:03 UTC">2011-04-13 12:03 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body">Yes. the curves are as you have identified. I am looking into your suggestion regarding the convertion. It is 3.3v and the ADC is 10bit as you have rightly said.<br>
<br>
thanks</div>
</article>

<article class="forum-post" id="p1548">
<header><strong>LubinKerhuel</strong><time datetime="2011-04-17 17:12 UTC">2011-04-17 17:12 UTC</time></header>
<h3>Re: rs232gui data format</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header>ADC data are 10 bits integer. Thus to convert the represented value to Volt, you should multiply by 3.3 / 2^10 (provided you are using a 3.3V cards which is probably the case)</blockquote><br>
do the 3.3 / 2^10 calculation within the rs232gui interface (i.e. receiver side) and not on the value beeing sent within the microcontrollers. (otherwise, you will get low resolution results as int : 0, 1 2 or 3)</div>
</article>

