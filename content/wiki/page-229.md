---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2009-07-14T14:49:02Z"
title: "Pic32-gcc v1.04 bugfix"
url: "/wiki/pic32-gcc-v1-04-bugfix/"
archiveKind: "page"
---
Bug reported on the Microchip .h definition file.

- In the file int.h localised in \\MPLAB C32\\pic32mx\\include\\peripheral\\int.h,

<!-- -->

- Lines (411, 424, 437, 450, 463) replace

`INTCONbits `\
`by `\
`INT0CONbits`

- Line 705, replace

`#define mOC1SetIntPriority(priority)        (IPC1CLR = _IPC1_OC1IP_POSITION, IPC1SET = ((priority) << _IPC1_OC1IP_MASK))`

by

`#define mOC1SetIntPriority(priority)        (IPC1CLR = _IPC1_OC1IP_MASK, IPC1SET = ((priority) << _IPC1_OC1IP_POSITION))`

- Line 746, replace

`#define mOC4SetIntSubPriority(subPriority)  (IPC4CLR = _IPC4_OC4IS_MASK, IPC4SET = ((subPriority) << v))`

by

`#define mOC4SetIntSubPriority(subPriority)  (IPC4CLR = _IPC4_OC4IS_MASK, IPC4SET = ((subPriority) << _IPC4_OCIS_POSITION))`

Thanks to Jiri Sehnal from [Humusoft](http://www.humusoft.com/index.php?lang=en) for identifying theses bugs.

[Category:Compiler_BugFix](/wiki/categories/)
