---
title: "Long time acquisitions using rs232gui/labview"
url: "/forum/topic/340/"
archiveKind: "topic"
---
# Long time acquisitions using rs232gui/labview

Forum : [General Remark and Questions](/forum/#forum-1)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p1387">
<header><strong>vaniaga</strong><time datetime="2010-12-09 17:29 UTC">2010-12-09 17:29 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I read in the Wiki:<br>
<br>
<br>
<br>
" Watch out : When logging data for a long time usinga big buffer size, some data may be lost : As the matrix R is growing,Matlab reallocate memory when the matrix is growing. This memory allocation may take some time and for reason that are still unclear, Seral port lose some datas. "<br>
<br>
<br>
<br>
How do i make long time acquisitions?<br>
<br>
Labview is better solution than Matlab?<br>
<br>
<br>
<br>
Someone could help me?<br>
<br>
Thanks,<br>
<br>
<br>
<br>
Vânia Almeida</div>
</article>

<article class="forum-post" id="p1388">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-09 22:44 UTC">2010-12-09 22:44 UTC</time></header>
<h3>Re: Long time acquisitions using rs232gui/labview</h3>
<div class="forum-post-body">Hi Vânia ,<br>
<br>
<br>
<br>
I updated the wiki page with a response to your question.<br>
<br>
<a href="/wiki/dspic-block-interface-tx-matlab/">http://archive.kerhuel.eu/wiki/Block/Interf ... b#Long_log</a><br>
<br>
<br>
<br>
I hope it will help.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1389">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-09 23:27 UTC">2010-12-09 23:27 UTC</time></header>
<h3>Re: Long time acquisitions using rs232gui/labview</h3>
<div class="forum-post-body">Labview is also pretty goog for logging data. I think I already upload on the forum few labview file.<br>
<br>
An exemple of the protocole is presented on my old (french) website : see <a href="http://lubink.free.fr/projelectro/Protocole_PIC_Matlab_Labview/Protocole_PIC_Matlab_Labview_FR.html">http://lubink.free.fr/projelectro/Proto ... ew_FR.html</a></div>
</article>

<article class="forum-post" id="p1390">
<header><strong>vaniaga</strong><time datetime="2010-12-10 11:14 UTC">2010-12-10 11:14 UTC</time></header>
<h3>Re: Long time acquisitions using rs232gui/labview</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
Now i can't test your solutions, but for the next week i hope to have news. <br>
<br>
Thank you.<br>
<br>
<br>
<br>
I send you my best regards.<br>
<br>
<br>
<br>
Vânia Almeida</div>
</article>

<article class="forum-post" id="p1391">
<header><strong>vaniaga</strong><time datetime="2010-12-10 15:30 UTC">2010-12-10 15:30 UTC</time></header>
<h3>Re: Long time acquisitions using rs232gui/labview</h3>
<div class="forum-post-body">Dear Lubin,<br>
<br>
<br>
<br>
I have questions about realterm because in my project i need of long time acquisitions with real time vizualization.<br>
<br>
If i receive the data using realterm, i can plot us in real time (like the start button of the rs232gui)?<br>
<br>
<br>
<br>
Using the rs232gui interface (with the button load)  is not possible.<br>
<br>
<br>
<br>
Vânia Almeida</div>
</article>

<article class="forum-post" id="p1392">
<header><strong>LubinKerhuel</strong><time datetime="2010-12-10 20:34 UTC">2010-12-10 20:34 UTC</time></header>
<h3>Re: Long time acquisitions using rs232gui/labview</h3>
<div class="forum-post-body">Hi Vânia,<br>
<br>
<br>
<br>
I am not sure to get it.<br>
<br>
If you use a hyperterminel like realterm, you will record raw data into a file but you will not be able to see graph in real time ; only binary data that will appears on the screen with sometime beep (I think ascii 7).<br>
<br>
<br>
<br>
To record data while seeing curve in real time, you could however use matlab with rs232gui with the Log.txt button to record raw data. Choosing a small value for values to be seen (You will see only the latest data, for exemple latest 10 seconds demending on the size of R and Rn (you should use R and Rn with equal size here). <br>
<br>
<br>
<br>
The inconvenient of Matlab is only that the UART is accessed through Java that is less responsive. However, If it works, You will get your data without any data lost.<br>
<br>
At the opposit, the good point of an hyperterminal is that it can be used on a computer were matlab is very slow. Thus you could use an old laptop for in the field recording.<br>
<br>
<br>
<br>
If you want to see curve from the very beginning of the log, with a long log, you would rather use labview. I may have posted somewhere old Labview model that implement the protocole used here as rs232gui.<br>
<br>
<br>
<br>
Lubin</div>
</article>

