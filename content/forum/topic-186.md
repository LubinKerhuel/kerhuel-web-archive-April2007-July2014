---
title: "analog in PWM out"
url: "/forum/topic/186/"
archiveKind: "topic"
---
# analog in PWM out

Forum : [dsPIC Peripherals](/forum/#forum-9)

15 message(s) · archive en lecture seule

<article class="forum-post" id="p654">
<header><strong>fonty</strong><time datetime="2009-01-06 22:57 UTC">2009-01-06 22:57 UTC</time></header>
<div class="forum-post-body">Hallo<br>
<br>
<br>
<br>
I’m a student of the fontys university. Per accident I fount your dsPIC toolbox. I was very impressed because we ware looking to make this library on ore own because we have some dsPIC boards at the UNI. The UNI what to change the les method. In the new method it is important that students can program a microcontroller (dsPIC) very fast whit a model made in simulink. So your toolbox is perfect. There is only on one thing I need to show sum profs at the UNI that is works. So I like to make a motor controller whit a analog input an a pwm output. But when I put in the PWM motor output I cant open the master block. Is there someone that can make a PWM output which change when the analog input change. I need this fast because I have a presentation at 8 January. Ant I like to show this. I think that when I can show a working model whit a analog in ant a pwm out the UNI will be very interested in this toolbox. I don’t think I can make it myself that fast. So is there someone who can help me?? It all neat to be run on a dsPIC30f6012</div>
</article>

<article class="forum-post" id="p655">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 00:00 UTC">2009-01-07 00:00 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Hi Fonty,<br>
<blockquote><header class="quote-author">Citation : fonty</header>Per accident</blockquote><br>
Nice accident ;-)<br>
<br>
<br>
<br>
dsPIC30f6012 has no <a href="/wiki/simulink-embedded-target-for-pic/">PWM motor peripheral</a>. <br>
<br>
To generate a PWM signal with a 30f6012, use the <a href="/wiki/simulink-embedded-target-for-pic/">Output Compare</a> (OC) block.<br>
<br>
<br>
<br>
Therefore, place an ADC block, a gain and a OC block. It should works very easily! (Have a look on <a href="/wiki/simulink-embedded-target-for-pic/">examples</a>...)<br>
<br>
Post your model if you get into trouble.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p659">
<header><strong>fonty</strong><time datetime="2009-01-07 16:21 UTC">2009-01-07 16:21 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Hallo Lubin<br>
<br>
<br>
<br>
I just found some time to make a simulink model and it built whiteout errors so it could be working. The problem is that I’m at home at this moment and I cant test it. So I hope you maybe can tell me I understand it right.<br>
<br>
<br>
<br>
I have a: ADC Input connected whit a gain (1) the gain is connected whit a data type conversion  that is connected whit UC5_up from the Output Compare. Than I have a constant (5) connected whit the OC5_periode.<br>
<br>
<br>
<br>
Is it right when I say that the output compare compares the ADC input whit the constant en generate a PWM out this? So when the input is 5 the PWM is100% when the input is 2.5 the PWM is 50% and when the input is 0 the PWM is 0??<br>
<br>
<br>
<br>
Than my last question. Is it possible to make a simulation model of this model. Can I scoop the output of the OC block sum way?? So I can simulate without my microcontroller board??</div>
</article>

<article class="forum-post" id="p660">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 17:42 UTC">2009-01-07 17:42 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Hi Fonty,<br>
<blockquote><header class="quote-author">Citation : fonty</header>So I can simulate without my microcontroller board??</blockquote><br>
dsPIC peripheral can't be simulated. It is not possible to simulate dsPIC peripheral because it would necessitate a simulation time step equal to the dsPIC Mips and this would not be efficient !<br>
<br>
It is however not very usefull to do such a peripheral simulation. Thus, simulation of the embedded calculation and feedback controller is very usefull and this is of course possible with simulink...<br>
<br>
<br>
<br>
It would be easier to help if you could upload your model on the forum.<br>
<br>
<br>
<br>
The blockset will define the variable OC5max and ANmax in the workspace (check your workspace)<br>
<br>
<br>
<br>
The gain between ADC and OC must be : OC5max / ANmax <br>
<br>
The constant connected to the OC5_periode should have the value OC5max.<br>
<br>
<br>
<br>
It should work as is. However, If OC5max/ANmax is not an integer <strong>and </strong>if you want very precise calculation, you should considere add 2 converter before and after the gain block. The one before would convert value into double to do floating point multiplication, and the one afte would convert the result to uint16 value.<br>
<br>
<br>
<br>
That's it</div>
</article>

<article class="forum-post" id="p661">
<header><strong>fonty</strong><time datetime="2009-01-07 18:32 UTC">2009-01-07 18:32 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">thanks for helping me so fast. I have changest the gain in OC5max/ANmax and the constant in OC5max. and it built successful so I hope it will work tomorrow when Iload it in the controller.. <br>
<br>
<br>
<br>
I like to upload my model at this forum but I don’t know how to do that.</div>
</article>

<article class="forum-post" id="p662">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 19:00 UTC">2009-01-07 19:00 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">upload the model tomorrow if you get in trouble.<br>
<br>
uplaod is just by the option tab at the bottom of the <strong>reply page</strong>, below the save-Preview-submit button</div>
</article>

<article class="forum-post" id="p664">
<header><strong>fonty</strong><time datetime="2009-01-07 20:56 UTC">2009-01-07 20:56 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">This is the model so far I will test it tomorrow.<br>
<br>
<br>
</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/175-example1.mdl">Pièce jointe : example1.mdl</a></p>
</article>

<article class="forum-post" id="p665">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-07 21:20 UTC">2009-01-07 21:20 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Will not work : <br>
<br>
<br>
<br>
in your model, the output of the ADC is an integer.<br>
<br>
OC5max/ANmax value will be defined as integer because of the inherited datatype option choosen. But  in your case, real value of OC5max/ANmax is 0.0488 ; converted into integer, result is 0.<br>
<br>
You multiply by 0.<br>
<br>
<br>
<br>
solution : <br>
<br>
turn your calculation into double (download the model attached)<br>
<br>
or use a PWM with a duty cycle larger than 0,2ms (that's quite short becaue of the slow quartz (giving 1 MIPS) Check also that with such a quartz, the Quartz configuration should not be the XT instead of HS  !)<br>
<br>
<br>
<br>
Lubin</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/176-example1b.mdl">Pièce jointe : example1b.mdl</a></p>
</article>

<article class="forum-post" id="p678">
<header><strong>fonty</strong><time datetime="2009-01-08 20:55 UTC">2009-01-08 20:55 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Thanks for helping Lubin. I changest the duty cycle and the Quartz configuration. After bilding en programming the controller it works well. After showing it in my presentation everyone was very enthusiast about it.</div>
</article>

<article class="forum-post" id="p709">
<header><strong>fonty</strong><time datetime="2009-01-27 13:56 UTC">2009-01-27 13:56 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">hallo lubin<br>
<br>
<br>
<br>
Hallo I try to rebuild the model we make earlier. But it doesn’t work I check all the configurations but I cant find the problem. Can you tell me where I can find the problem??<br>
<br>
<br>
<br>
This is the error I get<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'tutorial'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1138<br>
<br>
Error(s) encountered while building model "tutorial".</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/191-tutorial.mdl">Pièce jointe : tutorial.mdl</a></p>
</article>

<article class="forum-post" id="p710">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-27 15:52 UTC">2009-01-27 15:52 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">try the following :<br>
<br>
<br>
<br>
add the block "Configure Model for dsPIC Target" in your model and dbl click on that block !<br>
<br>
If it does not work, report the complete error message<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p711">
<header><strong>fonty</strong><time datetime="2009-01-27 20:06 UTC">2009-01-27 20:06 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">I add the block configuration block and I dbl clickt on it but I still get the error.<br>
<br>
I add also the model<br>
<br>
<br>
<br>
<br>
<br>
this is the error that I get<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Model error	tutorial	Simulink	Error building Real-Time Workshop target for block diagram 'tutorial'. MATLAB error message:Error using ==&gt; genMakefileAndBuild at 1138Error(s) encountered while building model "tutorial".<br>
<br>
<br>
<br>
Error building Real-Time Workshop target for block diagram 'tutorial'. MATLAB error message:<br>
<br>
Error using ==&gt; genMakefileAndBuild at 1138<br>
<br>
Error(s) encountered while building model "tutorial".</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/192-tutorial.mdl">Pièce jointe : tutorial.mdl</a></p>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/193-example1b.mdl">Pièce jointe : example1b.mdl</a></p>
</article>

<article class="forum-post" id="p712">
<header><strong>LubinKerhuel</strong><time datetime="2009-01-27 20:44 UTC">2009-01-27 20:44 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Hi Fonty,<br>
<br>
<br>
<br>
I did not see the "<strong>Configuration Model for dsPIC</strong>" block on your model !<br>
<br>
<br>
<br>
There is definitly a problem in your first problem, briefly : <br>
<br>
the LDPICTYPE line in the simulink Configuration Parameters is : <br>
<br>
C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libpic30-coff.a  C:\PROGRA~1\MICROC~1\MPLABC~2\lib\dsPIC30F\<strong>libpPIC24Fxxx-coff.a</strong> C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libc-coff.a C:\PROGRA~1\MICROC~1\MPLABC~2\lib\libm-coff.a<br>
<br>
<br>
<br>
The 24f has nothing to do there, This problem is corrected with the block I mention earlier.<br>
<br>
<br>
<br>
If it does not work, make sure you are using a blockset up to date.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/194-tutorial.mdl">Pièce jointe : tutorial.mdl</a></p>
</article>

<article class="forum-post" id="p713">
<header><strong>fonty</strong><time datetime="2009-01-28 09:11 UTC">2009-01-28 09:11 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">I’m sorry I add the wrong block</div>
</article>

<article class="forum-post" id="p816">
<header><strong>crh</strong><time datetime="2009-04-13 07:49 UTC">2009-04-13 07:49 UTC</time></header>
<h3>Re: analog in PWM out</h3>
<div class="forum-post-body">Hello Lubin,<br>
<br>
When I use the original model as above and I use a function generator instead of a potentiometer it works well. But when I insert a filter (in this model I use your filter form the explorer16) the system works during 30 to 60 seconds. I tried several kind of filters.<br>
<br>
I connected the AN and OC pin with a scope to see what is happening. In the beginning I see the square wave from the OC, but then the voltage drops down and there is no signal any more.  <br>
<br>
Casparus</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/231-ADCLP145PWM.mdl">Pièce jointe : ADCLP145PWM.mdl</a></p>
</article>

