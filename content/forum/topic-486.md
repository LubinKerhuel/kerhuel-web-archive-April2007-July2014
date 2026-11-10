---
title: "PIC18f4620 with mcc18 Fsfprintf Error SD card"
url: "/forum/topic/486/"
archiveKind: "topic"
---
# PIC18f4620 with mcc18 Fsfprintf Error SD card

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1853">
<header><strong>yiwen89</strong><time datetime="2012-03-08 08:07 UTC">2012-03-08 08:07 UTC</time></header>
<div class="forum-post-body">Hi, <br>
<br>
<br>
<br>
I am facing an error in my program code.  <br>
<br>
<br>
<br>
Error - could not find definition of symbol 'FSfprintf' in file './testingtesting.o'. <br>
<br>
<br>
<br>
<br>
<br>
I am wondering why i cant get through this error. I am able to use Fsfwrite and Fsfopenpgm. I get to create a file text in the SD card and I get to write "harlooo" inside the file text. But, when I want to use Fsfprintf command, it fails me. Anyone here could help?And I am thinking to outsource my project. All you need to do with my project is just log the data from an accelerometer into the SD card. I am using C language with mcc18 compiler.  <br>
<br>
<br>
<br>
p/s:1)I already enable the Fsfprintf in FSconfig.h. <br>
<br>
      2) I enable the integer promotion in the Build Options.  <br>
<br>
<br>
<br>
      3) I added SECTION    NAME=dataBuffer RAM=buffer1 into my linker scripts.  <br>
<br>
                        SECTION    NAME=FATBuffer  	 RAM=buffer2 <br>
<br>
      4) I added SECTION	   NAME=_SRAM_ALLOC_HEAP	RAM=gpr11 into my linker script too but I am not sure whether i got          add wrong for this section as I modify it from a book.  <br>
<br>
<br>
<br>
Hope to hear from you soon. <br>
<br>
<br>
<br>
Regards, <br>
<br>
yiwen</div>
</article>

