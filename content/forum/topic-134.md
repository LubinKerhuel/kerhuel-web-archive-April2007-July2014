---
title: "Importing data from Interface TX-Matlab to excel"
url: "/forum/topic/134/"
archiveKind: "topic"
---
# Importing data from Interface TX-Matlab to excel

Forum : [General Remark and Questions](/forum/#forum-1)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p408">
<header><strong>NigmaTech</strong><time datetime="2008-06-02 13:18 UTC">2008-06-02 13:18 UTC</time></header>
<div class="forum-post-body">Hi Lubin!<br>
<br>
<br>
<br>
Is that possible to import data, received using Interface TX-Matlab,<br>
<br>
to EXCEL using some simple method?<br>
<br>
<br>
<br>
I must to filtrate signal from IMU gyro (ADXRS150) and accelerometer. Propably I shoul implement Kalman filter, but I don't know how. Filtering is something new for me. Could you help?</div>
</article>

<article class="forum-post" id="p409">
<header><strong>LubinKerhuel</strong><time datetime="2008-06-02 20:29 UTC">2008-06-02 20:29 UTC</time></header>
<h3>Re: Importing data from Interface TX-Matlab to excel</h3>
<div class="forum-post-body">To import data received using Interface Tx-Matlab, I can see two methods : <br>
<br>
First of all, receve data in the matlab workspace using the graphical interface.<br>
<br>
To remove NaN values from the R matrix, use the custom made function : R = padr(R,1);<br>
<br>
<br>
<br>
Then, either you save data using a file format that Excel can understand (like cvs file format),<br>
<br>
or just open the R array with the matlab variable viewer, and copy-past to excel.<br>
<br>
<br>
<br>
I may write a webpage describing methods to log data using the Tx-Matlab interface. There are few tricks that allow to obtain complete data with a fine timing.<br>
<br>
<br>
<br>
For the filters of gyro and accelerometers, you may have a look on <a href="/RTWdsPIC/examples/IMU.html">this exemple</a> given on the website. <br>
<br>
If you are beginning with digital filter, You should avoid starting with adaptive kalman filter.</div>
</article>

