---
title: "Control of DC servomotor with digital encoder"
url: "/forum/topic/196/"
archiveKind: "topic"
---
# Control of DC servomotor with digital encoder

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p723">
<header><strong>Simon_says</strong><time datetime="2009-02-04 00:31 UTC">2009-02-04 00:31 UTC</time></header>
<div class="forum-post-body">Hi Lubin... <br>
<br>
Hello you all.<br>
<br>
 This is one of the first projects I made. I am trying to control a DC servomotor with incremental encoder (FAULHABER  1717V0023  this is the link:    <a href="http://micromo.com/servlet/com.itmr.waw.servlet.Anzeige?fremdaufruf=ja&amp;kdid=40929&amp;sprachid=1&amp;htdigurl=/n112053/i404618.html&amp;fremdurl=http://prodcat.faulhaber.net/prodcat/technology?technologyID=41%26brandID=141%26lngCode=en%26vtype=metric%26sortSpecifID=%26sortType=%26serieID=1596#1596">http://micromo.com/servlet/com.itmr.waw ... =1596#1596</a> ). The purpose is place a load on the end of a bar attached to the motor shaft and  the motor must keep steadily with no move at all. The motor must stay firm as as shown in the drawing attached. So if I change the mass of the load or if I unload the bar, the motor has to stay immobile. This is the model and the C file I am using in a dsPIC30F4012. It seems to work fine, but sometimes when I am pushing or pulling the bar the motor lose control and start running wildly. Can you please tell me if my design is correct, or if I am not considering something important?  Why the motor gets crazy? <br>
<br>
 Thanks for your help.<br>
<br>
<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/199-Motor%20drawing.JPG">Pièce jointe : Motor drawing.JPG</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/197-PID15m.mdl">Pièce jointe : PID15m.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/198-myQEI.c">Pièce jointe : myQEI.c</a></p>
</article>

<article class="forum-post" id="p725">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-04 02:18 UTC">2009-02-04 02:18 UTC</time></header>
<h3>Re: Control of DC servomotor with digital encoder</h3>
<div class="forum-post-body">Hi Jose,<br>
<br>
<br>
<br>
I would like to do a case-study with that example if that's Ok with you. I posted few elements on the wiki : <a href="/wiki/case-study-position-control-of-dc-motor/">http://archive.kerhuel.eu/wiki/Case_Study:_ ... f_DC_Motor</a> <br>
<br>
<br>
<br>
You should be able to edit the wiki once you logged-in (different from the forum login system) Feel free to add elements directly in this page, even if pagination i not good.<br>
<br>
<br>
<br>
May I add a link from the <a href="/wiki/category/example/">example page</a> to this example? Could you tell me is that solve the problem? Could you post the math model of the motor for simulation purpose?<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p758">
<header><strong>Simon_says</strong><time datetime="2009-02-12 20:34 UTC">2009-02-12 20:34 UTC</time></header>
<h3>Re: Control of DC servomotor with digital encoder</h3>
<div class="forum-post-body">Hi Lubin:<br>
<br>
 Absolutely you can put this project in a case study and add the link to the example page. I had been working getting the math model of the system. This is the first time I do this so it is taking me some time. I hope I get the math model soon. I´ll post it when I get it. Meanwhile hang on please!<br>
<br>
<br>
<br>
Thanks a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
</article>

<article class="forum-post" id="p763">
<header><strong>Simon_says</strong><time datetime="2009-02-18 21:55 UTC">2009-02-18 21:55 UTC</time></header>
<h3>Re: Control of DC servomotor with digital encoder</h3>
<div class="forum-post-body">Hello Lubin and you all.<br>
<br>
 Here I got the math model of the motor with the pendulum.  I think for simulation purposes this model (servomotor_pendul.mdl) is very close to reality. I have made the changes suggested in order to get a better performance and here it is. It seems to work and I am still testing it. I´ll let you know if something goes wrong. Attached is the new model with th changes suggested. Could you please take a look and suggest?<br>
<br>
 Thanks a lot!<br>
<br>
<br>
<br>
Jose Luis</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/208-servomotor_pendul.mdl">Pièce jointe : servomotor_pendul.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/211-PID15m1.mdl">Pièce jointe : PID15m1.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/210-myQEI.c">Pièce jointe : myQEI.c</a></p>
</article>

<article class="forum-post" id="p765">
<header><strong>LubinKerhuel</strong><time datetime="2009-02-23 21:35 UTC">2009-02-23 21:35 UTC</time></header>
<h3>Re: Control of DC servomotor with digital encoder</h3>
<div class="forum-post-body">Hello Jose Luis,<br>
<br>
<br>
<br>
I have  hardly no time at the moment to have a close look. I'll try later on. Anyway, Feel free to complete the wiki page. Let me know if you get trouble because of right permission to edit it or so...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1979">
<header><strong>geniusity</strong><time datetime="2013-01-11 16:14 UTC">2013-01-11 16:14 UTC</time></header>
<h3>Re: Control of DC servomotor with digital encoder</h3>
<div class="forum-post-body">Hello,<br>
<br>
I am really new with this blockset, can u tell me what is the function of the constant 38000 in that model, and also, what is the output of the PID controller and why the input need to be converted before feeding into PID blockset, tq.</div>
</article>

