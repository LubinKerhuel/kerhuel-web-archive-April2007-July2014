---
title: "Compilation with submodels"
url: "/forum/topic/414/"
archiveKind: "topic"
---
# Compilation with submodels

Forum : [bug reports](/forum/#forum-8)

4 message(s) · archive en lecture seule

<article class="forum-post" id="p1605">
<header><strong>bmairs</strong><time datetime="2011-06-15 23:22 UTC">2011-06-15 23:22 UTC</time></header>
<div class="forum-post-body">I have run into a problem when compiling a project of mine when using submodels. The submodel never finishes compilation and I don't know why. I get the following errors when it tries to compile my submodel 'controller':<br>
<pre><code>Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 33 Column: 10
Unable to open %include file dsPIC_srmain.tlc
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 34 Column: 10
Unable to open %include file dsPIC_mrmain.tlc
### Writing main
--- Multi Rate &amp; Single Tasking implementation
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 45 Column: 3
Attempt to call a non-function value: FcnSingleTaskingMain
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 45 Column: 23
Values of NULL type cannot be expanded</code></pre><br>
<br>
I've included a zip file with everything necessary to compile my model. You just need to set the path to include Autoboat\code\basic_model\Lib\[mlib|slib]. You'll also need to run Lib/mlib/busses.m to add the various bus definitions to the current workspace.<br>
<br>
<br>
<br>
The full output during compilation is below:<br>
<br>
<br>
<pre><code>### Checking the status of model reference RTW target for model 'controller' used in 'code_gen'
### Model reference RTW target (controller_rtwlib.lib) for model controller is out of date because controller_rtwlib.lib does not exist
### Updating model reference RTW target for model: controller
### Generating code into build directory: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller
Warning: Parameter precision loss occurred for 'Value'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/Rudder Command/Constant1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/Rudder Command/Gain1'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/Rudder Command/Heading Control/Angle
Conversion/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/Rudder Command/Heading Control/Angle
Conversion1/Unit Conversion'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Forces &amp; Moments/Divide by wheelbase'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Gain'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Outputs/Convert to acceleration'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Subsystem/Angle Conversion/Gain'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Subsystem/Gain'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Subsystem/Reorder/Angle Conversion/Gain'. 
Warning: Parameter precision loss occurred for 'Gain'. The parameter's value cannot be represented exactly using the
run-time data type. A small quantization error has occurred. You can control this diagnostic on the Diagnostics pane of the
Configuration Parameters dialog. This originated from 'controller/Autonomous Controller/State Keeper &amp; Estimator/GPS
Estimator/Subsystem/Reorder/Angle Conversion1/Gain'. 
Warning: Model reference Accelerator, SIL and PIL modes do not support data logging via To-Workspace blocks and Scope blocks
that are configured to save data to the workspace. Model 'controller' contains To-Workspace or Scope blocks with data
logging option turned on. Data is not being logged to workspace when this model is referenced using Accelerator (or SIL or
PIL) simulation mode. To turn off the reporting of this message, set 'Unsupported data logging' parameter on the 'Model
Referencing' group of the Diagnostics page of the Configuration Parameters to 'none' 
### Invoking Target Language Compiler on controller.rtw
### Using System Target File: C:\Users\Bryant\Documents\MATLAB\Lubin_Blockset\dspic\dspic.tlc
### Loading TLC function libraries
.......
### Initial pass through model to cache user defined code
....
### Caching model source code
............................................................
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 33 Column: 10
Unable to open %include file dsPIC_srmain.tlc
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 34 Column: 10
Unable to open %include file dsPIC_mrmain.tlc
### Writing main
--- Multi Rate &amp; Single Tasking implementation
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 45 Column: 3
Attempt to call a non-function value: FcnSingleTaskingMain
Error: File: C:\Users\Bryant\Projects\Autoboat\Code\basic_model\slprj\dspic\controller\tmwinternal\tlc\dsPIC_main.tlc Line: 45 Column: 23
Values of NULL type cannot be expanded
### Writing source file controller.c
### Writing header file controller_private.h
.
### Writing header file controller.h
### Writing header file controller_types.h
### Writing header file rt_MAXf_snf.h
.
### Writing header file rt_MAXd_snf.h
### Writing header file rt_MINf_snf.h
### Writing header file rt_SATURATE.h
.
### Writing header file rt_SIGNf_snf.h
### Writing header file rt_SIGNd_snf.h
### Writing source file controller_data.c
.
### TLC code generation complete.
.### Real-Time Workshop build procedure for model: 'controller' aborted due to an error.
--dir C:\PROGRA~1\MATLAB\R2010a/rtw/c/src/ext_mode/tcpip not found. It is not added to MPLAB project.</code></pre></div>
<p class="attachment-line"><a class="attachment" download href="/forum/attachments/424-Projects.zip">Pièce jointe : Projects.zip</a></p>
</article>

<article class="forum-post" id="p1606">
<header><strong>bmairs</strong><time datetime="2011-06-16 04:48 UTC">2011-06-16 04:48 UTC</time></header>
<h3>Re: Compilation with submodels</h3>
<div class="forum-post-body">So I did some more experimenting. It looks like I didn't have the RTW target for the submodel 'controller' set to the dsPIC. Unfortunately, even setting that to the dsPIC didn't fix it. I then added the master block, but that was still giving me errors. I'm not certain if there's anything left on my end that can get this blockset compiling with submodels.</div>
</article>

<article class="forum-post" id="p1629">
<header><strong>LubinKerhuel</strong><time datetime="2011-06-27 23:01 UTC">2011-06-27 23:01 UTC</time></header>
<h3>Re: Compilation with submodels</h3>
<div class="forum-post-body">Sorry for the response delay.<br>
<br>
<br>
<blockquote><header class="quote-author">Citation : bmairs</header>submodel </blockquote> I guess this is called by Mathworks guys model referencing : when you include a simulink model file within another one.<br>
<br>
The blockset is just not working as soon as you are doing model referencing. I should investigate much more, but it seems quite complex to solve. Thus, no solution for now.<br>
<br>
<br>
<br>
Lubin</div>
</article>

<article class="forum-post" id="p1638">
<header><strong>bmairs</strong><time datetime="2011-07-11 19:17 UTC">2011-07-11 19:17 UTC</time></header>
<h3>Re: Compilation with submodels</h3>
<div class="forum-post-body">I do imagine it's quite complex, but without this functionality larger models become very hard to maintain. Even SLUGS, which isn't that big of a codebase, is incredibly difficult to maintain. We've had to resort to using libraries, but that isn't a desirable nor complete solution to making the project easily modifiable and maintainable.</div>
</article>

