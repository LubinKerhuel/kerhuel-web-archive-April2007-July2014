---
title: "Can not find dsPIC.tlc"
url: "/forum/topic/51/"
archiveKind: "topic"
---
# Can not find dsPIC.tlc

Forum : [Requirement, Installation &amp; Configuration](/forum/#forum-4)

17 message(s) · archive en lecture seule

<article class="forum-post" id="p72">
<header><strong>p.erasmus</strong><time datetime="2007-05-31 19:04 UTC">2007-05-31 19:04 UTC</time></header>
<div class="forum-post-body">Hallo I have installed the toolbox and if I place the master block on the simulink page and select configure  simulink I can not fine the dspic.tlc file as the tutorial shows <br>
<br>
Please help <br>
<br>
Thanks</div>
</article>

<article class="forum-post" id="p73">
<header><strong>LubinKerhuel</strong><time datetime="2007-05-31 22:46 UTC">2007-05-31 22:46 UTC</time></header>
<div class="forum-post-body">Hi Peter,<br>
<br>
<br>
<br>
The installer m file should add the two subdirectory created: <br>
<br>
- *\dspic<br>
<br>
- *\blocks<br>
<br>
In the matlab path.<br>
<br>
--&gt;Check that this has been done correctly: <br>
<br>
in matlab : File ==&gt; set path and check that the theses two directory are present. If they are not, add them...<br>
<br>
<br>
<br>
It still doesn't work: <br>
<br>
Try to refresh the <span style="color:red">matlab path cache</span> if it is enable ; disable the path cache: <br>
<br>
File ==&gt; Preferences ==&gt; in the General Tab...<br>
<br>
<br>
<br>
It still doesn't work?<br>
<br>
<span style="color:red">The toolbox must not be installed in the matlab directory or subdirectory</span>. Make sure you did not install the toolbox inside the matlab directory or sudirectory !<br>
<br>
<br>
<br>
You should now see dspic.tlc file in simulink ==&gt; Simulation ==&gt; Configuration Parameters ==&gt; Real time workshop Tab, clicking Browse on the System Target File selection <br>
<br>
<br>
<br>
If not, please, tell me.</div>
</article>

<article class="forum-post" id="p74">
<header><strong>p.erasmus</strong><time datetime="2007-06-01 16:59 UTC">2007-06-01 16:59 UTC</time></header>
<div class="forum-post-body">Hallo Lubin<br>
<br>
Thank you for the reply ,<br>
<br>
I have refreshed the matlab path and I can now see the dsPIC.tlc in the simulink properties however when I select it it brings the message error FCN callback main block <br>
<br>
<br>
<br>
Please help me I really want to stert to us simulink<br>
<br>
Thanks <br>
<br>
Peter<br>
<br>
ps the toolbox is installed C:\toolbox</div>
</article>

<article class="forum-post" id="p75">
<header><strong>p.erasmus</strong><time datetime="2007-06-01 17:39 UTC">2007-06-01 17:39 UTC</time></header>
<div class="forum-post-body">Hi Lubin<br>
<br>
Here is a copy of the error message in the work space<br>
<br>
It appears after I select the dsPIC.tlc filein the sim properties -&gt; Real time workshop<br>
<br>
Thanks  <br>
<br>
<br>
<br>
Warning: Error evaluating 'CopyFcn' callback of Master block (mask) 'Master'. Error using ==&gt; dsPIC_ConfigRTWOption<br>
<br>
The *System Target File must be defined to dsPIC Real Time workshop (Simulation ==&gt; Configuration Parameters ==&gt; Real Time workshop.</div>
</article>

<article class="forum-post" id="p76">
<header><strong>LubinKerhuel</strong><time datetime="2007-06-02 08:01 UTC">2007-06-02 08:01 UTC</time></header>
<div class="forum-post-body">Hi Peter,<br>
<br>
<br>
<br>
Good news : Your simulink configuration is fine!<br>
<br>
<br>
<br>
While configuring new simulink diagram for use with the dsPIC blockset, or while opening simulink model using the dsPIC blockset, you will some erratic warning message in the workspace. ==&gt; dont' care about theses one !<br>
<br>
<br>
<br>
That is due to unresolved internal toolbox's variables and appears only while configuring or opening simulink models.<br>
<br>
<br>
<br>
To confirme your configuration is correct, clean the workspace screen :<br>
<br>
 &gt;&gt; clc<br>
<br>
On your simulink model, click on "Update diagram" (Icon in simulink menu)<br>
<br>
You will get error message in the workspace if configuration is not correct or if there are conflict with dsPIC peripheral for example.<br>
<br>
<br>
<br>
Always click on "Update diagram" before compiling usng "Incremental build" icon. ( or Ctrl-B)</div>
</article>

<article class="forum-post" id="p77">
<header><strong>p.erasmus</strong><time datetime="2007-06-02 13:29 UTC">2007-06-02 13:29 UTC</time></header>
<div class="forum-post-body">Hallo Lubin<br>
<br>
<br>
<br>
Thank you for the reply,<br>
<br>
I will try to do the tutorial and see if I am able to simulate and generate the code <br>
<br>
<br>
<br>
 :D <br>
<br>
Best Regards <br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p78">
<header><strong>p.erasmus</strong><time datetime="2007-06-02 18:38 UTC">2007-06-02 18:38 UTC</time></header>
<div class="forum-post-body">Hallo Lubin<br>
<br>
 I am sorry I am so stupid I just cant get the RTW to run I have done the update function as you sugested in the last post  here is an extract of the error messages <br>
<br>
<br>
<br>
Thanks a lot<br>
<br>
Peter<br>
<br>
<br>
<br>
Warning: The dialog of 'untitled/Master' is being closed because a mask parameter has been changed.<br>
<br>
&gt; In dsPIC_Set_Dialog_PopUp_Param at 57<br>
<br>
  In dsPIC_MASTER_callback_InitMask at 222<br>
<br>
NbrPortUsed is 0<br>
<br>
NbrPortUsed is 0<br>
<br>
NbrPortUsed is 0<br>
<br>
NbrPortUsed is 0<br>
<br>
<br>
<br>
tack Trace:<br>
<br>
  [0] simulink.dll:public: void __thiscall SLDialogData::broadcastApplyEvent(class UDInterface *,bool)(0x168c0250, 1, 0x1695d7d0, 3) + 10 bytes<br>
<br>
  [1] simulink.dll:public: virtual void __thiscall HandleComboSelectionEventMI::invokeMethod(class UDMethodSignature *,int *,void * *,int,void * *)(0x0efe00f0, 0x00cdafc0, 0x1695d7d0, 4) + 117 bytes<br>
<br>
  [2] udd.dll:public: virtual void __thiscall UDMethodInfo::invokeMethodE(class UDMethodSignature *,int *,void * *,int,void * *,class UDErrorStatus *)(0x0efe00f0, 0x00cdafc0, 0x1695d7d0, 4) + 65 bytes<br>
<br>
  [3] dastudio.dll:protected: bool __thiscall Dialog::executeObjectMethod(class UDInterface *,char const *,char const *,struct mxArray_tag const *,struct mxArray_tag const *,bool *)(0x168bc830, 0x158f4200 "?freeMaskDialogCallback@@YAXPAUs..", 0x01eba100, 0x1590ec40 "?setMaskDialogPromptToDefault@@Y..") + 1281 bytes<br>
<br>
  [4] dastudio.dll:protected: bool __thiscall Dialog::executeObjectandMatlabMethodsForDestination(class GLWidget *)(0x16236978, 0x1618f480, 0x16305bf8, 0x16236978) + 131 bytes<br>
<br>
  [5] dastudio.dll:public: virtual bool __thiscall Dialog::glEventNotify(class GLEvent const *)(0x16173660, 0xffffffff, 0x16173660, 0) + 1838 bytes<br>
<br>
  [6] glee.dll:public: virtual void __thiscall GLWidget::notifyListeners(class GLEvent const *)(0x16</div>
</article>

<article class="forum-post" id="p79">
<header><strong>LubinKerhuel</strong><time datetime="2007-06-02 21:24 UTC">2007-06-02 21:24 UTC</time></header>
<div class="forum-post-body">Hi Peter,<br>
<br>
<br>
<br>
I do not see the point here !<br>
<br>
<br>
<br>
I just created a new schematic from scratch with the last version of the toolbox (V0.93) and It works without problems ( Tested with booth : Matlab 2007a and 2006b).<br>
<br>
<br>
<br>
Notice that When you change, in the MASTER lock, the dsPIC/PIC you use as target, the dialog get close and you have to re-open it to continue to configure it. When the dsPIC/PIC is changed, parameters of the dialog must also change and it is not possible to do it while it is opened.<br>
<br>
<br>
<br>
<br>
<br>
Did you manage to get the example compiling successfully ?<br>
<br>
If so, why don't you "save as" one of the example and use it as the starting point for  your model ?<br>
<br>
<br>
<br>
otherwise, <br>
<br>
which Matlab version are you using ?</div>
</article>

<article class="forum-post" id="p80">
<header><strong>p.erasmus</strong><time datetime="2007-06-03 08:56 UTC">2007-06-03 08:56 UTC</time></header>
<div class="forum-post-body">Hallo Lubin<br>
<br>
<br>
<br>
Yes I am sure the problem is not in the RTw it is with my matlab or with my setup or with the instulation of the RTW .<br>
<br>
<br>
<br>
I am using MATLAB 7.01 <br>
<br>
I can not do the tutorial for the following reasons<br>
<br>
(1) when I select the tlc file in the Configuration  RTW workshop matlab reports and error with a pop up messgae Error SCN Callback function.<br>
<br>
then I update new diagram as you mentioned then it save the tlc file in the config ,then I save this simulink page with the master block on it<br>
<br>
<br>
<br>
(2) I then open the simulink saved file now when it opens it brings up all these errors as show above and matlam crashes<br>
<br>
<br>
<br>
I have uninstalled matlab and installed it again and I have tried to install the toolbox again however I must mention that I was not able to invoke the dspIC installer from the command winow ,I have to open the mfile and invoke it by degug -&gt; run and then it would install the dsPIC toolbox <br>
<br>
I think if we could find the problem why it does not install from the <br>
<br>
command window it would work.<br>
<br>
I am sorry that I bother you so much with this however I would like to use this feature  and as I said I am sure the problem is with me and not with your RTW if I can only find the problem</div>
</article>

<article class="forum-post" id="p81">
<header><strong>p.erasmus</strong><time datetime="2007-06-03 08:57 UTC">2007-06-03 08:57 UTC</time></header>
<div class="forum-post-body">:D <br>
<br>
I am sorry once again</div>
</article>

<article class="forum-post" id="p83">
<header><strong>LubinKerhuel</strong><time datetime="2007-06-03 11:33 UTC">2007-06-03 11:33 UTC</time></header>
<div class="forum-post-body">Dear Peter,<br>
<br>
<br>
<br>
I find the origine of the problem : It is your Matlab version. You mentionned : <br>
<blockquote><br>
I am using MATLAB 7.01 </blockquote> 7.01 or R14SP1 released in 2003 or 2004.<br>
<br>
<br>
<br>
As mentionned on the <a href="/RTWdsPIC/download.html">download page</a>:<br>
<blockquote>The toolbox has been tested with MPLAB C30 (v2.05 and v3) compiler and with Matlab R2006a, R2006b and R2007a.</blockquote><br>
<br>
Since the toolbox use the last matlab capabilities, It will not work on former version of matlab R2006a ( released on 1 march 2006)<br>
<br>
<br>
<br>
Future version of matlab and C30 will be supported. However, I will not make the toolbox compatible with former version of matlab R2006a.<br>
<br>
<br>
<br>
Install a recent matlab version (R2006a or above) to get the blockset working.</div>
</article>

<article class="forum-post" id="p84">
<header><strong>p.erasmus</strong><time datetime="2007-06-03 12:21 UTC">2007-06-03 12:21 UTC</time></header>
<div class="forum-post-body">Dear Lubin<br>
<br>
Thank you for the reply it is clear ,<br>
<br>
I will update in the near future <br>
<br>
Thanks and sorry for this<br>
<br>
Best Regards<br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p91">
<header><strong>p.erasmus</strong><time datetime="2007-07-21 12:26 UTC">2007-07-21 12:26 UTC</time></header>
<div class="forum-post-body">Dear Lubin <br>
<br>
I have upgraded to 2007 matlab and now the toolbox is working ,<br>
<br>
I would like to buy a full verion of the toolbox with out any limitation on the number of pins used <br>
<br>
 Thank you for your reply<br>
<br>
Regards <br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p92">
<header><strong>LubinKerhuel</strong><time datetime="2007-07-21 14:58 UTC">2007-07-21 14:58 UTC</time></header>
<div class="forum-post-body">Hi Peter, <br>
<br>
<br>
<br>
I'm glad that you made it working on your computer !<br>
<br>
<br>
<br>
<a href="/RTWdsPIC/download.html">Download the latest version</a>  of the toolbox that has been improved.<br>
<br>
<br>
<br>
Pricing and procedure to <a href="/RTWdsPIC/pricing.html">buy the toolbox</a> are decribed on the website.<br>
<br>
<br>
<br>
Because I could not test all peripheral with all microcontroller supported by the toolbox, test the peripheral with the microcontroller you want to use first (using the <a href="/RTWdsPIC/download.html">demonstration version</a>).<br>
<br>
Repport any bug that may appear. <br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p93">
<header><strong>p.erasmus</strong><time datetime="2007-07-21 15:35 UTC">2007-07-21 15:35 UTC</time></header>
<div class="forum-post-body">Hi Lubin<br>
<br>
Do I have to remove the old version files first from my folder C\toolbox and then copy new version files again into this folder and reinstall it in matlab as with the old version ,I am just afraid things stop to work now <br>
<br>
Thanks <br>
<br>
Best Regards <br>
<br>
Peter</div>
</article>

<article class="forum-post" id="p94">
<header><strong>LubinKerhuel</strong><time datetime="2007-07-21 16:32 UTC">2007-07-21 16:32 UTC</time></header>
<div class="forum-post-body">That is correct. It should work. <br>
<br>
<br>
<br>
Note however that some diagram done using the old toolbox could encounter few problems since blocks parameters may be different in the new toolbox.<br>
<br>
<br>
<br>
To be sure, keep a copy of the installation file of the "old" toolbox somewhere.<br>
<br>
<br>
<br>
Let me know.</div>
</article>

<article class="forum-post" id="p99">
<header><strong>p.erasmus</strong><time datetime="2007-08-11 19:26 UTC">2007-08-11 19:26 UTC</time></header>
<div class="forum-post-body">Hi Lubin<br>
<br>
<br>
<br>
I have installed the latest verion of the toolbox for Matlab 2007a ,<br>
<br>
I am able to comple all the examples succesfully with this version no problems at all<br>
<br>
<br>
<br>
Best regards<br>
<br>
Peter</div>
</article>

