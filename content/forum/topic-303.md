---
title: "ICS configured incorrectly"
url: "/forum/topic/303/"
archiveKind: "topic"
---
# ICS configured incorrectly

Forum : [bug reports](/forum/#forum-8)

13 message(s) · archive en lecture seule

<article class="forum-post" id="p1221">
<header><strong>bmairs</strong><time datetime="2010-05-04 17:31 UTC">2010-05-04 17:31 UTC</time></header>
<div class="forum-post-body">I've updated to the recent blockset version to 3.2b and I think I've found a bug. I have odd problems running my code where once it attempts to send a CAN message it halts. This does not occur if I open the generated source in MPLAB, though it asks me about fixing the ICS configuration bits before I run it there.<br>
<br>
<br>
<br>
The exact prompt MPLAB gives me is:<br>
<blockquote>The configuration bits in the file are invalid and may cause problems if programmed.<br>
<br>
Do you want to set them to their default value? [YES/NO]<br>
<br>
Please note you will need to either rebuild the file or export memory again to correct the file.<br>
<br>
Config Field: ICS</blockquote><br>
<br>
This has resulted in the standard compilation path of compile in MATLAB and download via the PICkit2 impossible. My only option is to open the generated source in an MPLAB project and load it that way.</div>
</article>

<article class="forum-post" id="p1222">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-04 22:14 UTC">2010-05-04 22:14 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">Hi Bryant,<br>
<br>
<br>
<br>
A new field was added in the master block about In Circuit debugging : ICD communication channel.  Default is set to none and this "default" value cause this error.<br>
<br>
<br>
<br>
Could you set it to another value than none ? typically, ICS_PGD1 would be fine.<br>
<br>
let me know if you still have the same problem.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1224">
<header><strong>bmairs</strong><time datetime="2010-05-04 23:00 UTC">2010-05-04 23:00 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">I've tried PGD1, but that didn't fix the problem. It also breaks programming via MPLAB.<br>
<br>
<br>
<br>
Before you made this change, what were the default values for the JTAG and ICD? Those seemed to work earlier, so I'd like to use those again. I don't have any old compilations to check the source from.</div>
</article>

<article class="forum-post" id="p1225">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-04 23:23 UTC">2010-05-04 23:23 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">it depends on the chip used :<br>
<br>
<br>
<br>
MB stand for Master block options...<br>
<br>
pic30 : <br>
<br>
_FICD( <strong>MB ICD</strong> )  line did not exist in earlier code<br>
<br>
<br>
<br>
pic33:<br>
<br>
_FICD(  JTAGEN_OFF )	replace in code by  _FICD( <strong>MB JTAG</strong> &amp; <strong>MB ICD</strong> )<br>
<br>
<br>
<br>
pic24f:<br>
<br>
_CONFIG1( JTAGEN_OFF &amp; GCP_OFF &amp; GWRP_OFF &amp; COE_OFF &amp; FWDTEN_OFF &amp; ICS_PGx2)<br>
<br>
replaced with <br>
<br>
_CONFIG1( <strong>MB JTAG</strong> &amp; GCP_OFF &amp; GWRP_OFF &amp; COE_OFF &amp; FWDTEN_OFF &amp; ICS_PGx2)<br>
<br>
<br>
<br>
pic24h :<br>
<br>
_FICD(<strong>MB JTAG</strong> &amp;  <strong>MD ICD</strong> ) line did not exist  in earlier code<br>
<br>
<br>
<br>
Did you also updated C30 compiler ?  <br>
<br>
There may be option or flags changed when compiler is launched.</div>
</article>

<article class="forum-post" id="p1227">
<header><strong>bmairs</strong><time datetime="2010-05-05 16:15 UTC">2010-05-05 16:15 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header><br>
_FICD( JTAGEN_OFF ) replace in code by _FICD( MB JTAG &amp; MB ICD )</blockquote><br>
<br>
These constants you suggest are not available even if I inject an underscore in them, so the above isn't a solution. Can I obtain the functionality from the last blockset version in this one? I don't want to have to modify the source code everytime I try to compile something.</div>
</article>

<article class="forum-post" id="p1228">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-05 17:04 UTC">2010-05-05 17:04 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">Hi Bryant,<br>
<blockquote><header class="quote-author">Citation : bmairs</header>Can I obtain the functionality from the last blockset version in this one?</blockquote><br>
I am not sure to get it. if you want to test, I can override theses new options inside C code with their default value, to get similar C code from old blockset. did you mean this ?<br>
<br>
or do you prefere to revert to old blockset ?<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : bmairs</header>These constants you suggest are not available</blockquote><br>
I did not get it<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1229">
<header><strong>bmairs</strong><time datetime="2010-05-05 17:08 UTC">2010-05-05 17:08 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body"><blockquote>_FICD( JTAGEN_OFF ) replace in code by _FICD( MB JTAG &amp; MB ICD )</blockquote><br>
<br>
That line you suggested replacing will not compile. It says both the "MB JTAG" and "MB_JTAG" symbols are not found. I have also tried deleting the whole _FICD line, but that didn't resolve the issue either.<br>
<br>
<br>
<br>
I just want my code to work again and I'm confused as to why the defaults which were working before were changed to something that now doesn't work. I'm hoping I can make adjust the settings so that I can use this updated blockset, especially once you add the ECAN blocks I'll want to use it. If my code can't run using your updated versions of the blocksets, that's a problem.</div>
</article>

<article class="forum-post" id="p1230">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-06 06:34 UTC">2010-05-06 06:34 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">Hello Bryant,<br>
<br>
<br>
<br>
I didn't make it clear enough: MB (for Master Block) JTAG and MB ICD in the new blockset version <strong>are  replaced</strong> by the parameters options taken from dsPIC Master Block (simulink). If you look at generated code, you will see it.<br>
<br>
<br>
<br>
In previous blockset version, it was not possible to precise theses options.<br>
<br>
They were added as <a href="/forum/topic/272/#p1087">someone asked for it</a>.<br>
<br>
<br>
<br>
Anyway, default options taken by theses new parameters compile properly but cause a warning when opening files with MPLAB. This warning was not an issue as code worked fine (as far as I tested it).<br>
<br>
<br>
<br>
I'll send you a blockset without theses new options. However, the problem probably comes from somewhere else. I already see with MPLAB some code working when running in debug mode, but not working in release mode! This was a really weird thing. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1232">
<header><strong>Ender</strong><time datetime="2010-05-06 19:34 UTC">2010-05-06 19:34 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">Just a track:<br>
<br>
The difference between code working in debug and not in debug is usually for some peripheral interrupts.<br>
<br>
Often, the problem come from the WDT, which is enable with a bad setting and reset (or else) the chip after a short while.   <br>
<br>
In debug mode the WDT is disable but in release mode, it can be enable in the code or in the Mplab config setting.</div>
</article>

<article class="forum-post" id="p1234">
<header><strong>LubinKerhuel</strong><time datetime="2010-05-09 08:50 UTC">2010-05-09 08:50 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">Another difference between compilation within MPLAB and MATLAB is pointed out on this post : (not in the correct topic, I'll try to move it)<br>
<br>
<br>
<br>
<a href="/forum/topic/11/#p1139">http://www.kerhuel.eu/forum/viewtopic.p ... ECAN#p1162</a></div>
</article>

<article class="forum-post" id="p1235">
<header><strong>bmairs</strong><time datetime="2010-05-10 19:32 UTC">2010-05-10 19:32 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">So at this point I'm not certain that the problem is I'm running into. I've tried versions 3.1, 3.2b, and the 3.3a that Lubin sent me and I'm running into the same problem with all of them: Code works just fine when imported into MPLAB and run in either the Debug or Release mode. It does not work, however, when being using the .hex file generated by MATLAB and pushed via PicKit2. I am able to transmit a single CAN message and then the processor hits either an infinite loop or halts (either is possible with my code). Transmission does use an interrupt, which could be the problem as it's triggered after the message is transmitted.</div>
</article>

<article class="forum-post" id="p1243">
<header><strong>bmairs</strong><time datetime="2010-05-14 22:01 UTC">2010-05-14 22:01 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">So I've updated my ECAN code to now use a circular buffer for transmission and skip the blocking infinite loop that I had in the my code previously. This was where the code was getting stuck, and I wasn't sure why. Right now I'm testing my code with the new 3.2b version, though I don't think I'll have a problem now.</div>
</article>

<article class="forum-post" id="p1244">
<header><strong>bmairs</strong><time datetime="2010-05-14 22:18 UTC">2010-05-14 22:18 UTC</time></header>
<h3>Re: ICS configured incorrectly</h3>
<div class="forum-post-body">The new version of the blockset isn't a problem. Looks like things are running fine over here now.</div>
</article>

