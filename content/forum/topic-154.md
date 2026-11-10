---
title: "Configuring in a sub-system"
url: "/forum/topic/154/"
archiveKind: "topic"
---
# Configuring in a sub-system

Forum : [bug reports](/forum/#forum-8)

2 message(s) · archive en lecture seule

<article class="forum-post" id="p501">
<header><strong>Bernard Leak</strong><time datetime="2008-09-03 17:50 UTC">2008-09-03 17:50 UTC</time></header>
<div class="forum-post-body">I want to use a fixed configuration hidden from ordinary users,<br>
<br>
so hiding it inside a masked sub-system makes sense.  However,<br>
<br>
the resulting &lt;model&gt;_main.c tries to include the generated<br>
<br>
headers from the sub-system, as<br>
<br>
&lt;model&gt;/&lt;subsystem name&gt;.h and &lt;model&gt;/&lt;subsystem name&gt;_private.h<br>
<br>
instead of<br>
<br>
&lt;model&gt;.h and &lt;model&gt;_private.h<br>
<br>
as expected (and as actually generated).<br>
<br>
<br>
<br>
At present only the Compiler Configuration and Master blocks<br>
<br>
are hidden in this way: I think it is the Master block which is<br>
<br>
causing trouble.   The other generated files do not have the problem.<br>
<br>
<br>
<br>
RTWGenSettings.MyModelName<br>
<br>
for my model is "ALT_WINDOW_SIM/Target Board Setup"<br>
<br>
and presumably gives the same result everywhere in the model.<br>
<br>
The string _private.h is only present in the *.tlc files as a suffix to<br>
<br>
%&lt;MyModelName&gt;, which in turn is always defined as<br>
<br>
CAST("String",RTWGenSettings.MyModelName)<br>
<br>
It seems to me that the definition of MyModelName is an attempt<br>
<br>
to second-guess just what RTW actually generates, and in this<br>
<br>
case gets it wrong, unless the Master block is in the root of the<br>
<br>
model.<br>
<br>
<br>
<br>
There is an obvious work-around - just keep the Master block<br>
<br>
in the root of the model - but is there any chance of changing<br>
<br>
this behaviour?  The comments associate with the definition of<br>
<br>
MyModelName suggests that this is really a rather hard problem!<br>
<br>
<br>
<br>
Bernard Leak.</div>
</article>

<article class="forum-post" id="p503">
<header><strong>LubinKerhuel</strong><time datetime="2008-09-03 22:04 UTC">2008-09-03 22:04 UTC</time></header>
<h3>Re: Configuring in a sub-system</h3>
<div class="forum-post-body">Hi Bernard, <br>
<br>
<br>
<br>
Thanks for the bug report. It is corrected.<br>
<br>
<br>
<br>
The correction will be available in the next release (current release is <strong>0.98fc</strong>)<br>
<br>
<br>
<br>
Lubin</div>
</article>

