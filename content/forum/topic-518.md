---
title: "Adding Linux Support"
url: "/forum/topic/518/"
archiveKind: "topic"
---
# Adding Linux Support

Forum : [Request for new functions / Peripheral / Chip support](/forum/#forum-5)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p1920">
<header><strong>marcb</strong><time datetime="2012-09-12 16:29 UTC">2012-09-12 16:29 UTC</time></header>
<div class="forum-post-body">Hello, and first of all congratulations on what seems like a real cool blockset.<br>
<br>
<br>
<br>
However, people like me, stuck in the Linux world cannot take full advantage of your toolbox, as it does not play well with Linux... Actually, it doesn't work at all. The S-functions are only compiled for Windows targets, i.e. mexw32 and mexw64.<br>
<br>
Therefore, I would be very much obliged if you could compile the whole thing for Linux too - that will be pure awesome! <br>
<br>
<br>
<br>
Furthermore, I am willing to lend you a helping hand in porting the whole thing to Linux and Mac, as I have some programming skills up my sleeve. Also, if anyone wants to join in, by all means - this is an open party!<br>
<br>
<br>
<br>
For examples, I've quickly scanned through some of the files in the library, and it seems that the paths for the Microchip compiler are hardcoded to the Windows install folder (e.g. C:\Program Files\Microchip\C32\...). To add Linux support in an instant, you can do something like this (in pic32.tlc):<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;ProgramFiles = '/opt' % default Microchip install folder on Linux, change if needed
ProgramFilesx86 = ProgramFiles;
<wbr>
if (ispc) % if we're on Windows, check for the Program Files folder
    ProgFile_path=getenv('PROGRAMFILES') ;
    ProgFilex86_path=getenv('PROGRAMFILES(x86)') ;
    winpath=getenv('PATH') 
else
    [s,w]=system(['find ' ProgramFiles filesep 'microchip' filesep 'xc32 -name docs']);
    [C32path,C32ver,ext]=fileparts(w);
    if isdir(C32path)
        C32dir = C32path;
    end
end
</code></pre><br>
<br>
Also you can use <em>filesep</em> (wich uses <em>\</em> or <em>/</em> as a separator, depending on the environment) and <em>computer</em> to build the path to the compiler and MATLAB's gmake:<br>
<br>
<br>
<pre><code>&lt;i&gt;
&lt;/i&gt;if (VerMatlab &lt; 7.5)     % 'old skool' Windows hard-coded style
    rtwoptions(oIdx).default = [rtw_alt_pathname(matlabroot) '\rtw\bin\win32\gmake'];
else     % platform independent
     rtwoptions(oIdx).default = [rtw_alt_pathname(matlabroot) filesep 'bin' filesep computer('arch') filesep 'gmake'];
     % this would be expand to /usr/local/MATLAB/R2012a/bin/glnxa64/gmake, for example
end
</code></pre><br>
<br>
Please let me know if you're interested, I am more than willing to help you out in porting to Linux and Mac.<br>
<br>
<br>
<br>
Cheers!</div>
</article>

