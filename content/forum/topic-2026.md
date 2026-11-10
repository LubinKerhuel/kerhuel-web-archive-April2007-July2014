---
title: "Stateflow and timer1/freerun"
url: "/forum/topic/2026/"
archiveKind: "topic"
---
# Stateflow and timer1/freerun

Forum : [General Remark and Questions](/forum/#forum-1)

1 message(s) · archive en lecture seule

<article class="forum-post" id="p3477">
<header><strong>mperearo</strong><time datetime="2013-12-19 14:15 UTC">2013-12-19 14:15 UTC</time></header>
<div class="forum-post-body">Hello,<br>
<br>
<br>
<br>
I found a weird behavior when using Stateflow in a dsPIC33FJ256MC710A, I haven't checked for other microcontrollers, also I don't know if other users have experienced it.<br>
<br>
<br>
<br>
What my program does is mesure the current from a motor, the motor starts moving when I push a button, then a motor moves which then closes a mechanical piece. When closing, the current grows and when the current achieves a target current (lets say 5A) then the motor stops moving. Finally to release the mechanical piece I push the button again, and the command is to make the motor move in the opposite direction for 2 seconds. For this last part I use the condition [after(2,sec)] in the transition from applying -12V to applying 0V.<br>
<br>
<br>
<br>
The weird part comes when I actually mesure the time the motor releases, the condition is to move during 2 seconds, but it doesn't move 2 seconds, it moves more or less, depending on many parameters. <br>
<br>
<br>
<br>
First I tried modifying the Sample Time of the entire model, it was first set to 0.001 seconds, and the stateflow was inheriting this time step, in this configuration the motor moved 26 seconds or so instead of 2. It is also worth mentioning that in the Master block I had configured Timer1 as my Time Step Reference.<br>
<br>
<br>
<br>
Then I tried modifying the Sample Time of the entire model to 0.01 seconds, and the stateflow was inheriting this time step again, in this configuration the motor moved 2 seconds sometimes, if i modified things in the program some other times it moved 3 seconds or 1.5<br>
<br>
<br>
<br>
As this didn't seem to solve the problem I started moving the Stateflow Sample Time, the global Sample Time, the Time Step Reference from Timer1 to FreeRun until I arrived to a configuration set which made the motor actually move 2 seconds. This configuration is 0.01 seconds as model Sample Time, 0.01 seconds as Stateflow Sample Time (not inherited), Master's Time Step Reference in FreeRun and I kept working with this configuration without touching it for a while.<br>
<br>
<br>
<br>
However, there are times when I move to another configuration like Time Step Reference in Timer1 or Sample Time 0.1 seconds and the motor moves 2 seconds as it should, and when I come back to the "good" configuration which i found first it doesn't work well anymore. In small words, it's really unstable but I can't understand why. What is weird for me is that this seconds are the only thing that works different than it should in the program. All other things such as mesures, operations even UART communication work fine. I am using Matlab R2011a in case it is relevant.<br>
<br>
<br>
<br>
I hope you can help me solve this issue which is really driving me a little crazy. Thanks in advance.<br>
<br>
Here I include my model.</div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/525-uC_Stateflow_after.mdl">Pièce jointe : uC_Stateflow_after.mdl</a></p>
</article>

