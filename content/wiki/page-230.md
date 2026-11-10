---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-02-27T22:04:13Z"
title: "Pic30-gcc v3.12 bugfix"
url: "/wiki/pic30-gcc-v3-12-bugfix/"
archiveKind: "page"
---
Problem in definition file for chip with 2 PWM motor peripheral. Affect all pic30-gcc version from **3.11** to current version (**3.25**)

Check PIC30 gcc version : type **!pic30-gcc -v** at the matlab prompt.

Workaround :

- in file **pwm12.h, line 511** (C:\\Program Files\\Microchip\\MPLAB C30\\support\\peripheral_30F_24H_33F\\pwm12.h) **replace** :

`#else`

by

`#endif`\
`#ifdef _PWM2IF`

[Category:Compiler_BugFix](/wiki/categories/)
