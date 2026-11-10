---
title: "Huge tables. full memory. Type Double vs Other. Optimization"
url: "/forum/topic/171/"
archiveKind: "topic"
---
# Huge tables. full memory. Type Double vs Other. Optimization

Forum : [Advanced Simulink &amp; RTW Questions](/forum/#forum-6)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p600">
<header><strong>Ender</strong><time datetime="2008-10-31 07:07 UTC">2008-10-31 07:07 UTC</time></header>
<div class="forum-post-body">Hello Lumbin<br>
<br>
I’m trying to fit the huge tables in the static memory.<br>
<br>
<br>
<br>
Example: 2 tables of 140 x 100  of doubles. So usually 112Ko. The target is a Dspic33FJ256MC710 (256K) and the compiler is a licensed C30 v10b.<br>
<br>
<br>
<br>
For one table alone the compiler works fine and the report returns about 42K and 16% in the total program memory used. <br>
<br>
How that is possible, just 42K ?<br>
<br>
Does it changes the value in single or integer over the optimization ?<br>
<br>
<br>
<br>
For two tables, it returns the message bellow :<br>
<br>
     _ error: size of variable 'memory_try_ConstP' is too large    gmake: *** [memory_try_data.o] Error 255 _<br>
<br>
<br>
<br>
I tried some options on the compiler line but I didn’t understand how the static datas work with the data space ?<br>
<br>
Is it Possible to declare the data type as a integer in Mathlab table ?</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/136-memory_try.mdl">Pièce jointe : memory_try.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/137-Table2_14000.mat">Pièce jointe : Table2_14000.mat</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/138-Table1_14000.mat">Pièce jointe : Table1_14000.mat</a></p>
</article>

<article class="forum-post" id="p602">
<header><strong>LubinKerhuel</strong><time datetime="2008-10-31 19:31 UTC">2008-10-31 19:31 UTC</time></header>
<h3>Re: Huge tables. full memory. Type Double vs Other. Optimization</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : Ender</header>For one table alone the compiler works fine and the report returns about 42K and 16% in the total program memory used.<br>
<br>
How that is possible, just 42K ?<br>
<br>
Does it changes the value in single or integer over the optimization ?</blockquote><br>
programmable memory's elementary storage case is not 8 bits width. It is something like 12 or 14 or more ?<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : Ender</header>Is it Possible to declare the data type as a integer in Mathlab table ?</blockquote><br>
Is is highly recommanded if you want your software to fin in the dsPIC !<br>
<br>
convert your variable at the matlab prompt:<br>
 <pre><code>Table_14000 = int16(Table_14000);</code></pre><br>
To store fixed point variable,  you should multiply your variable by the 2^(Width of fractional part) before convertign it into a  int8 or 16 or 32 datatype. Then, in Simulink, following the lookup table, use a convert block to convert the int8 into the fixed point format <strong>using 'Stored Integer' option</strong>. I advise to practise with simulation to understand how thinks works.<br>
<br>
<br>
<br>
I also advise to use the '<strong>Direct Lookup Table</strong>' block instead of the '<strong>Lookup Table</strong>' since your index are integers.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p605">
<header><strong>Ender</strong><time datetime="2008-11-04 00:11 UTC">2008-11-04 00:11 UTC</time></header>
<h3>Re: Huge tables. full memory. Type Double vs Other. Optimization</h3>
<div class="forum-post-body"><blockquote><header class="quote-author">Citation : LubinKerhuel</header><br>
To store fixed point variable,  you should multiply your variable by the 2^(Width of fractional part) before convertign it into a  int8 or 16 or 32 datatype. Then, in Simulink, following the lookup table, use a convert block to convert the int8 into the fixed point format <strong>using 'Stored Integer' option</strong>. I advise to practise with simulation to understand how thinks works.<br>
<br>
<br>
<br>
I also advise to use the '<strong>Direct Lookup Table</strong>' block instead of the '<strong>Lookup Table</strong>' since your index are integers.</blockquote><br>
<br>
Hi .<br>
<br>
I tried to convert the data to int8 or 16 data type, but the final size didn't change. The optimizations by Mathlab and the C30 compiler seem did this yet. But thank your advices and for the prompt command, it's useful.<br>
<br>
I don't manage still to store more than 32K of Data, in one or many tables and to reuse them it the model.  Could you help me please ?<br>
<br>
<br>
<br>
Obviously the code use the PSV methodology to map 32KB of data space addresses into a page of Program Memory. And there are a limitation on the PSV method of 32K. So I understand why for one Table less than 32K the model work fine and for more than 32K it doesn't work.<br>
<br>
But with two Tables less than 32K, I hoped that the data was mapped by the PSV process again when then code switched between the tables. But the compiler say always that the variable is too large.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/139-memory_try_direct.mdl">Pièce jointe : memory_try_direct.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/140-2tab10000_int.mat">Pièce jointe : 2tab10000_int.mat</a></p>
</article>

<article class="forum-post" id="p606">
<header><strong>LubinKerhuel</strong><time datetime="2008-11-05 23:07 UTC">2008-11-05 23:07 UTC</time></header>
<h3>Re: Huge tables. full memory. Type Double vs Other. Optimization</h3>
<div class="forum-post-body">Hi Ender,<br>
<br>
<br>
<br>
A first look on the generated code shows that all constant from the two lookup table are stored into one varaible.<br>
<br>
Thus, you may try to copy-past the two part of the generated code that correspond to the two array to create your own C function that will<br>
<br>
- declare theses two table<br>
<br>
- the two function to read the two array<br>
<br>
This solution should be tested.<br>
<br>
<br>
<br>
if modifying compilation parameters can solve the probleme, let me know.<br>
<br>
<br>
<br>
Lubin</div>
</article>

