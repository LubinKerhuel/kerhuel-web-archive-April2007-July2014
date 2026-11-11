---
title: "Target for dsPIC's errors on my system..."
url: "/forum/topic/57/"
archiveKind: "topic"
---
# Target for dsPIC's errors on my system...

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

6 message(s) · archive en lecture seule

<article class="forum-post" id="p104">
<header><strong>just4you</strong><time datetime="2007-09-05 20:02 UTC">2007-09-05 20:02 UTC</time></header>
<div class="forum-post-body">I'm korean and I also want to make the target for dsPIC.  <br>
<br>
:idea: but the master of this forum has done.<br>
<br>
so I decide to change my purpose to use this tool.  :D <br>
<br>
<br>
<br>
However, target for dsPIC makes some troubles..<br>
<br>
so I can't try the examples on the web site.<br>
<br>
<br>
<br>
<strong>1. windows character encoding problem</strong><br>
<br>
the toolbox is made with 'windows-1252'<br>
<br>
'windows-949' is used in my coutry..<br>
<br>
When load the "\blocks\dsPICdrivers.mdl", 2 kind of errors are occured.<br>
<br>
<strong>'§'</strong> and  <strong>'°'</strong> character makes troubles.<br>
<br>
korean is one of representative 2-byte characters. Therefore it runs well on the korean windows, I expect that it runs well on other 2-byte chracter system.<br>
<br>
<br>
<br>
<a href="http://cafefiles.naver.net/data26/2007/9/6/53/load_error_just4u78.jpg">http://cafefiles.naver.net/data26/2007/ ... st4u78.jpg</a><br>
<br>
<br>
<br>
I'm using the slCharacterEncoding() function to avoid the upper problem.<br>
<br>
using the 'windows-1252', I cann't save well. so this must be improved.<br>
<br>
<br>
<br>
<br>
<br>
2. <strong>master &amp; configuration block</strong> error<br>
<br>
<br>
<br>
when double clicking the both blocks to set the master block and configuration block, the system show the following errors.<br>
<br>
Master block settings are not shown. How can I avoid the messages?<br>
<br>
<br>
<br>
<a href="http://cafefiles.naver.net/data26/2007/9/6/187/master_error_just4u78.jpg">http://cafefiles.naver.net/data26/2007/ ... st4u78.jpg</a><br>
<br>
<br>
<br>
<a href="http://cafefiles.naver.net/data26/2007/9/6/153/configuration_error_just4u78.jpg">http://cafefiles.naver.net/data26/2007/ ... st4u78.jpg</a><br>
<br>
<br>
<br>
<br>
<br>
P.S &gt; I hope that this article can contain the image files.<br>
<br>
         I can't upload the images, link is just allowed.<br>
<br>
         It's very inconvenient..  :shock:</div>
</article>

<article class="forum-post" id="p105">
<header><strong>just4you</strong><time datetime="2007-09-07 12:00 UTC">2007-09-07 12:00 UTC</time></header>
<h3>0.94e the newest version has also character problems</h3>
<div class="forum-post-body">The master of this forum anounced release of 0.94e version.<br>
<br>
<br>
<br>
Perhaps This version works in japanese windows well, but it's now working in korean windows.<br>
<br>
<br>
<br>
'§' and '°' characters make problems.</div>
</article>

<article class="forum-post" id="p106">
<header><strong>LubinKerhuel</strong><time datetime="2007-09-15 07:14 UTC">2007-09-15 07:14 UTC</time></header>
<div class="forum-post-body">Hi,<br>
<br>
<br>
<br>
I noticed that the release 94e still has trouble due<br>
<br>
to character coding in other country using different<br>
<br>
coding.<br>
<br>
<br>
<br>
I will investigate within few weeks. <br>
<br>
<br>
<br>
Let me few days, I just moved and I am quite busy<br>
<br>
right now.<br>
<br>
<br>
<br>
I will post a message when I get it working.<br>
<br>
<br>
<br>
Tanks for reporting the bug.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p111">
<header><strong>just4you</strong><time datetime="2007-09-27 23:46 UTC">2007-09-27 23:46 UTC</time></header>
<h3>0.94eb toolbox works..</h3>
<div class="forum-post-body">I've tested the new version of the Embedded workshop for dsPIC.<br>
<br>
<br>
<br>
This version of dsPIC RTW generates the compiled codes.  :D <br>
<br>
<br>
<br>
(Embedded Coder for dsPIC V0.94eb works in Korean Windows and MATLAB 2007a)<br>
<br>
<br>
<br>
I'll report more results after some more tests.</div>
</article>

<article class="forum-post" id="p114">
<header><strong>LubinKerhuel</strong><time datetime="2007-09-28 06:48 UTC">2007-09-28 06:48 UTC</time></header>
<div class="forum-post-body">This release is not yet available on the website. (beta version sent to 'just4you'  for testing)<br>
<br>
<br>
<br>
The new release working with Korean and Japaneses characteres will be released soon.<br>
<br>
<br>
<br>
Thanks for testing</div>
</article>

<article class="forum-post" id="p118">
<header><strong>LubinKerhuel</strong><time datetime="2007-10-06 12:22 UTC">2007-10-06 12:22 UTC</time></header>
<h3>Bug corrected</h3>
<div class="forum-post-body">The new version with bug corrected is now available : V0.95a<br>
<br>
Several improvement have also been made to this version which now support 56 Microcontrolleurs.<br>
<br>
<br>
<br>
Download it here : <a href="/RTWdsPIC/download.html">http://archive.kerhuel.eu/RTWdsPIC/download.html</a><br>
<br>
Release notes can be found here : <a href="/RTWdsPIC/ReleaseNotes.html">http://archive.kerhuel.eu/RTWdsPIC/ReleaseNotes.html</a></div>
</article>

