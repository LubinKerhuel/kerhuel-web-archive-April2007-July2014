---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2011-12-29T13:57:04Z"
title: "Review"
url: "/wiki/review/"
archiveKind: "page"
---
Rapid Prototyping Tools or experimentation for Microchip PIC / dsPIC microcontroller

## Tools

### Microchip

Microchip released a first version of a blockst in late 2008 (about november). The version 2 of the microchip blockset were released on June, 5th 2009. It seems that The Dev Team get inspired from an old version of my blockset (\*). Anyway, with this blockset, you have to configure all registers of the peripheral. This it not really convenient. I also did not see efficient interrupt handling to make some peripheral works. A free evaluation version is available from their website. Please try it and report your impressions.

------------------------------------------------------------------------

3 simple steps to **remove the 30s pause** from microchip free evaluation version :

- **Remove/Rename** the file ./Microchip/MPLAB IDE/Tools/MATLAB/dsPIC_Matlab/dspic/**serKeyVal.p** (renamed in serKeyVal.old)
- **create a new m file** in the same directory

`function a = serKeyVal()`\
`disp('Hello Word')`\
`a=0;`\
`end`

- **save as serKeyVal.m**

------------------------------------------------------------------------

(\*) speicfic parts of code from my blockset can be found in microchip blockset (but that\'s not official !): In microchip dsPIC_mrmain.tlc file in directory dspicblks, you can find

`   %if (CalculusTimeStepEN == 1)`\
`          CalculusTimeStep = TMR1;`\
`   %endif`\
`   %if (MasterBusyPort != -1)`

Sames instructions in the original: In Lubin\'s blockset, dsPIC_mrmain.tlc file in directory blocks

`   %if (CalculusTimeStepEN == 1)`\
`       if (_T1IF) CalculusTimeStep = PR1;  /* Overload */`\
`       else CalculusTimeStep = TMR1;     `\
`   %endif`\
`   %if (MasterBusyPort != -1)`

[https://sites.google.com/site/writingservicesreviews/home/ispaperhelporgfraudornot PaperHelp.org Review](https://sites.google.com/site/writingservicesreviews/home/ispaperhelporgfraudornot_PaperHelp.org_Review)

`   (differences comes from the fact that I improved it, i.e. Microchip did not get inspired from my last version)`

This code is a very specific function that can only be found in the \"Lubin\'s blockset\" (not accessible in the microchip blockset). This code remains in Microchip blockset, even in V2 published on 5th 2009. There are probably other similar part of code.

(I now scramble tlc files so as to avoid non-official collaboration. Thus, you will recognize variables name : CalculusTimeStepEN and CalculusTimeStep in my tlc file.)

------------------------------------------------------------------------

------------------------------------------------------------------------

### Quantiphi

product from SimuQuest companie sell a Matlab toolbox for Microchip PIC18Fx480/x580 (9000\$ for a single licence including the UniPhi product)

------------------------------------------------------------------------

------------------------------------------------------------------------

### Scicos-Scilab {#scicos_scilab}

Evidence Companie built a Scilab/Scicos Code Generator for the FLEX board which is based on a microchip microcontroller

------------------------------------------------------------------------

------------------------------------------------------------------------

### Embedded Target for dsPIC {#embedded_target_for_dspic}

v3.7e - (10 sep 2012) - suporting 100 chips

<div class="chip-matrix"><table> <tbody> <tr> <td> <p><strong>See <a href="/wiki/release-notes/">Release Notes and known bug</a> for details</strong></p> <table> <tbody> <tr> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 24F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 32F**</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 30F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 30F</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ GP</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ MC</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ GP</th> <td style="text-align: center; background: #f0f0f0;"></td> <th scope="col" style="text-align: center; background: #f0f0f0;">PIC 33FJ MC*</th> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX360F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP206</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP202</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC202</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX360F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP306</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP204</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC204</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ128GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX460F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f2012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5015</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP310</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP802</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC802</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX460F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f5016</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC508</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128GP804</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj128MC804</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX775F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32GP302</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32MC302</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX775F256L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32GP304</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj32MC304</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA006</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX795F512L</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP202</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC202</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA008</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX320</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f3014</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC506</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP204</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC204</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ96GA010</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>32MX340</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4011</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6014</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ256GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC510</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP802</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC802</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ16GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4012</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f6015</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP206</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64GP804</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fj64MC804</p></td> </tr> <tr> <td style="text-align: center;"><p>24fJ32GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>30f4013</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP306</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ48GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP310</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ128MC710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP706</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ16GA004</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP708</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ32GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"><p>33fJ64GP710</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ48GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"><p>24fJ64GA002</p></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> <tr> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> <td style="text-align: center;"></td> </tr> </tbody> </table> <dl> <dt>Newly added chip</dt> <dd> 64MC204, 128MC204, 128GP202, 32MC202, 32MC204, 16MC304 , 33FJ256GP710A </dd> <dt>* PIC 32F</dt> <dd> SPI function not suported yet; </dd> <dt>* Compiler known and fixed bugs</dt> <dd> </dd> <dt>* Check your compiler installation and version</dt> <dd> at the matlab prompt ==&gt; <strong>!pic30-gcc -v</strong> for pic30 and <strong>!pic32-gcc -v</strong> for pic32. </dd> <dt>**Check pic32 compiler <a href="/wiki/pic32-gcc-v1-04-bugfix/"> v 1.04 Workaround</a><br /> **Check pic30 compiler <a href="/wiki/pic30-gcc-v3-12-bugfix/"> PWM 2 Workaround</a> from version v 3.12 to current version (3.25)...<br /> </dt> </dl> </td> </tr> </tbody> </table> <p></p></div>

------------------------------------------------------------------------

## Experimentation

### The Autonomous Unmanned Systems (USL) {#the_autonomous_unmanned_systems_usl}

This team at the University or South Florida works of Unmanned Aerial Vehicles (UAV). In a step by stem approach, they validate the simulink generated code by compiling it and connecting the \"Autopilote PC-software\" to a plane simulation software (X-Plane). Then, they compile the code to implement it into a PIC18f 4620. They deal with timing and PIC peripheral by integrating \"hand coding functions\" into the code generated by Matlab.

Two refferences:

D. Ernst, K. Valavanis, J. Craighead, "Unmanned Vehicle Controller Design, Evaluation and Implementation: From MATLAB to Printed Circuit Board", Journal of Intelligent and Robotic Systems (In print)

D. Ernst, K. Valavanis, J. Craighead, Automated Process for Unmanned Systems Controller Implementation Using MATLAB, CD-ROM Proceedings, 14th Mediterranean Conference on Control and Automation, Ancona, Italy, June 2006.

------------------------------------------------------------------------

\<comments \\\>
