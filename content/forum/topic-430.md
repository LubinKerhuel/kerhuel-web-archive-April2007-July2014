---
title: "restorePath, and slbuild errors, matlab working directory ch"
url: "/forum/topic/430/"
archiveKind: "topic"
---
# restorePath, and slbuild errors, matlab working directory ch

Forum : [bug reports](/forum/#forum-8)

9 message(s) · archive en lecture seule

<article class="forum-post" id="p1649">
<header><strong>resodad</strong><time datetime="2011-08-09 19:36 UTC">2011-08-09 19:36 UTC</time></header>
<div class="forum-post-body">Lubin and all,<br>
<br>
Here is an interesting problem:<br>
<br>
I attempt to build the attached model and Simulink produces "Undefined function or variable restorePath" and changes the working directory, e.g. I build in C:\Users\ij8977\Documents\MatlabWork\ArmFireX2 and then Matlab switches to  C:\Users\ij8977\Documents.<br>
<br>
<br>
<br>
I have also seen " recursive call to slbuild."<br>
<br>
<br>
<br>
Is this a problem with the Blockset or Matlab or Microsoft Vista?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/431-ArmFireX2.mdl">Pièce jointe : ArmFireX2.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/432-MatlabBuidErrorScript.txt">Pièce jointe : MatlabBuidErrorScript.txt</a></p>
</article>

<article class="forum-post" id="p1655">
<header><strong>LubinKerhuel</strong><time datetime="2011-08-12 23:34 UTC">2011-08-12 23:34 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Hi John,<br>
<br>
<br>
<br>
Thanks for bug reports.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>I have also seen " recursive call to slbuild."</blockquote><br>
When the previous compilation hand-up in an unexpected way, you get this message the next time your try to compile the model. Usually, next time you try to compile should be Ok (or hang-up again...)<br>
<br>
Hang-up is typically caused by a bug. The blockset might be the cause. Please report the problem if you get this message.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : resodad</header>Undefined function or variable restorePath</blockquote> I installed recently the dsPIC blockset on a vista windows and I get this error.<br>
<br>
This is mysterious bug for me as the blockset has no variable or script called restorePath.<br>
<br>
However, I noticed that when installing the blockset, the matlab path is updated until matlab is restarted.<br>
<br>
Thus, it seems that vista does not allow matlab to save the updated path. It might be a user right problem. I could not tell much about user right with vista.<br>
<br>
Anyway, the problem might be solved by adding the two blockset directory (respectively "<strong>dspic</strong>" and "<strong>blocks</strong>") to the matlab path.<br>
<br>
<br>
<br>
Two ways :<br>
<br>
1) Menue file ==&gt; Set PAth ==&gt; select the two folder and save the path<br>
<br>
2) with matlab browser, goes to the blockset folder ==&gt; mouse right on dspic ==&gt; "add to path". same for blocks directory.<br>
<br>
<br>
<br>
You might also write a script called startup.m and place it within the matlab search path. It will execute at matlab startup.<br>
<br>
use the addpath('c:/.../dspic','c;/.../blocks') command.<br>
<br>
<br>
<br>
Please let me know if you find another workaround.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1656">
<header><strong>bmairs</strong><time datetime="2011-08-14 17:03 UTC">2011-08-14 17:03 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">For the path configuration settings on Windows Vista and 7 you need to run Matlab as an administrator (right-click on the link and select Run as administrator) in order to permanently edit the path. This is a permissions issue with Windows that Mathworks hasn't fixed as of 2010a at least.</div>
</article>

<article class="forum-post" id="p1718">
<header><strong>resodad</strong><time datetime="2011-10-04 16:52 UTC">2011-10-04 16:52 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Lubin, this problem persists.it is a BIG problem since I cannot use the blockset.<br>
<br>
I run Matlab R2011a as administrator.<br>
<br>
The path includes ...\blocks and...\dspic.<br>
<br>
<br>
<br>
neither of these help.<br>
<br>
<br>
<br>
Why does the current folder jump up two levels? <br>
<br>
Please let me know if you find a work around.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1719">
<header><strong>resodad</strong><time datetime="2011-10-04 17:02 UTC">2011-10-04 17:02 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Here is a pair of files that may help track the error. The difference is the addition of a pulse block and a multiply block.<br>
<br>
Please see if you get the same error as I do.<br>
<br>
John</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/442-PinCode.mdl">Pièce jointe : PinCode.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/443-PinCode2.mdl">Pièce jointe : PinCode2.mdl</a></p>
</article>

<article class="forum-post" id="p1720">
<header><strong>resodad</strong><time datetime="2011-10-04 17:48 UTC">2011-10-04 17:48 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Also,<br>
<br>
 if you remove the "if" block from ArmFireX2.mdl, it builds OK.<br>
<br>
John</div>
</article>

<article class="forum-post" id="p1722">
<header><strong>LubinKerhuel</strong><time datetime="2011-10-07 23:33 UTC">2011-10-07 23:33 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Hi John<br>
<br>
<br>
<br>
The good news is that I can reproduce the error with windows x64, matlab x64.<br>
<br>
<br>
<br>
I think I get it :<br>
<br>
Multiply block (X) does not support boolean type at its output.<br>
<br>
Digital Output Write block after Multiply block is a boolean.<br>
<br>
<br>
<br>
For some reason, the error message is silly and my guess is that the blockset does alterate mathworks error message. (There might be a bug here, will look for it!)<br>
<br>
Anyway, replacing X block with a logical solve the problem. yo might also use a datatype conversion block to get a uint8 after the X block (not tested however).<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1724">
<header><strong>LubinKerhuel</strong><time datetime="2011-10-08 15:31 UTC">2011-10-08 15:31 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">I confirm that the blockset was corrupting mathworks error message making model's error very difficult to handle.<br>
<br>
Fixed in blockset release 3.7.<br>
<br>
<br>
<br>
Thanks for reporting that bug, it really worth it !<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1725">
<header><strong>resodad</strong><time datetime="2011-10-11 14:11 UTC">2011-10-11 14:11 UTC</time></header>
<h3>Re: restorePath, and slbuild errors, matlab working director</h3>
<div class="forum-post-body">Thanks Lubin.<br>
<br>
The new version is working so far.<br>
<br>
John</div>
</article>

