---
title: "Failed compilation still generated MPLAB 8 project"
url: "/forum/topic/472/"
archiveKind: "topic"
---
# Failed compilation still generated MPLAB 8 project

Forum : [bug reports](/forum/#forum-8)

5 message(s) · archive en lecture seule

<article class="forum-post" id="p1805">
<header><strong>bmairs</strong><time datetime="2012-01-16 19:40 UTC">2012-01-16 19:40 UTC</time></header>
<div class="forum-post-body">If my project fails compilation then a .mcp file for MPLAB 8.x is still generated.</div>
</article>

<article class="forum-post" id="p1806">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-16 20:13 UTC">2012-01-16 20:13 UTC</time></header>
<h3>Re: Failed compilation still generated MPLAB 8 project</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
This is done on purpose : It allows to find out why compilation breaks. For example, if the blockset mispell one fuse register, you might correct it this way quite easily.<br>
<br>
However, depending where the compilation stops, you might have missing files...<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1808">
<header><strong>bmairs</strong><time datetime="2012-01-17 19:34 UTC">2012-01-17 19:34 UTC</time></header>
<h3>Re: Failed compilation still generated MPLAB 8 project</h3>
<div class="forum-post-body">But there isn't a similarly compiled MPLAB X project, which is why I assumed this was a bug. I'd prefer to switch over to X whenever possible, so could you also make the MPLAB X project be generated?</div>
</article>

<article class="forum-post" id="p1812">
<header><strong>LubinKerhuel</strong><time datetime="2012-01-18 20:33 UTC">2012-01-18 20:33 UTC</time></header>
<h3>Re: Failed compilation still generated MPLAB 8 project</h3>
<div class="forum-post-body">Bryant, I am a bit confused.<br>
<br>
<br>
<br>
Could you described what you obtained and what you would like to obtain ? <br>
<br>
(I am not sure I could do it for this blockset, but it would be useful for next Microchip blockset)<br>
<br>
<br>
<br>
Currently, the model <br>
<br>
- generates a .mcp file (mplab 8 project) and <br>
<br>
- add into the directory created (with almost similar name than the model) the information for the mplab X project : nbproject folder and files...<br>
<br>
<br>
<br>
Thus with mplab X, you should be able to open that folder which is the project (browse the folder with MPLAB X, you will see that folder icon is like a project).<br>
<br>
MPLAB X does not provide one "clikable" file that would allows opening the project.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1818">
<header><strong>bmairs</strong><time datetime="2012-01-23 23:58 UTC">2012-01-23 23:58 UTC</time></header>
<h3>Re: Failed compilation still generated MPLAB 8 project</h3>
<div class="forum-post-body">If I build a project and it fails compilation an MPLAB 8 project is generated but NOT an MPLAB X project. I just thought it was weird that a project was generated for only one of the IDEs and not both. I figured it was a bug because you'd either want no project to be generated when compilation failed or for both projects to be generated regardless of whether compilation fails or not, but what's happening is in between.</div>
</article>

