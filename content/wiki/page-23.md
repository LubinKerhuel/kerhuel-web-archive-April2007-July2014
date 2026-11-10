---
source: "MediaWiki snapshot 2019-03-25"
lastmod: "2015-05-03T17:30:56Z"
title: "DsPIC Block/Interface Tx-Matlab"
url: "/wiki/dspic-block-interface-tx-matlab/"
archiveKind: "page"
---
<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_UART_Interface_TxMatlab.png" alt="Block UART Interface Tx-Matlab">

<figcaption>

Block UART Interface Tx-Matlab

</figcaption>
</figure>

Open Graphical User Interface to receive data from the microcontrollers throw the PC serial port. Data can be plotted in real time.

Double click on this block open the GUI to log data from the dsPIC into matlab.

Related blocks : [Block/UART_Configuration](/wiki/dspic-block-uart-configuration/) [Block/Rx_Input](/wiki/dspic-block-rx-input/) [Block/Tx_Output](/wiki/dspic-block-tx-output/) [Block/Tx_Output_Multiplexed_For_Matlab-Labview](/wiki/dspic-block-tx-output-multiplexed-for-matlab-labview/) [Block/Interface_Tx-Matlab](/wiki/dspic-block-interface-tx-matlab/)

# Interface PIC-Matlab {#interface_pic_matlab}

<figure class="wiki-figure">

<img loading="lazy" src="/images/Block_rs232gui_DialogBox.png" alt="User Interface for logging data from UART with matlab" width="450">

<figcaption>

User Interface for logging data from UART with matlab

</figcaption>
</figure>

Set the connexion of the PC serial port. You can select the COM port used, the baudrate ( select the same used by the dsPIC) and the hardware control flow (usually, set to none if you are using a simple UART interface like 2 wires). External module like bluetooth, you may need hardware control Flow.

The **connexion** and **Reset** button connect and release the COM port. Once the connexion is established, modification on port parameters have no influence. MAtlab\'s Java may crash (Matlab just close in such a case) when connectiing while the dsPIC is sending data. The workaround is to disconnect the PIC while pushing the connection button.

The data received are decoded using the PIC - Matalb protocole created and stored into the R matrix. Each column of **R** correspond to one channel. lines are added to R until the max buffer size (number of line) is reached (here 50000). Then, oldest data are deleted at the profit of newest one.

Time **T_R** is the estimated time of the data reception.

R, T_R, Rn, T_Rn are accessible from the workspace. R and Rn matrix contains NaN values. The function padr allow to remove NaN values.

The Rn matrix is a subset of the R matrix. Rn contain the last 10000 values of R. The size of R can be set. Rn is the matrix that should be used for real time plotting.

Write the command that are interpreted in the central large text box. After the delay during which data are being received (0.2s here). You can enter any valid Matlab command. It is also possible to call a matlab script file or function you previously wrote. The four buttons Default, Dflt signe, Simulink, Emission are four example of pre-recorded plotting script. Default is to plot unsigned data. Dflt signe allow to plot signed int16 data.

Watch out : When logging data for a long time usinga big buffer size, some data may be lost : As the matrix R is growing,Matlab reallocate memory when the matrix is growing. This memory allocation may take some time and for reason that are still unclear, Seral port lose some datas. Note that Matlab use Java to acces to the serail PORT. Thus, it is not optimal!

Start and Stop button is for start and stop the reception-execution of the script. Do not forget to release (\"reset button\") the COM port before leaving.

The Send1 and Send2 button allow to send the vector next to the button (respect Send1 and Send2) to the Serial PORT.

# Real-Time Consideration {#real_time_consideration}

**T_R is an approximation of time only**, and shoudl be used for vewing purpose only. If you need precise data time stapm, follow the following procedure :

- On the simulink model, make sure to **not overload the UART**. Check that you are sending less data than max allowed by the UART bauds. To count the number of bytes used, when using the Tx-Labview-Matlab block, add one byte for each data sent. For example sending one uint8 data takes 2 bytes, uint16 data takes 3 bytes and uint32 data takes 5 bytes.
- **Reconstruct a vector timing** corresponding to the simulink\'s UART timing.

T_R (and T_Rn) approximate the time using the computer clock. Each time Matlab read an UART sequence, time is read. Then, the first byte of the sequence is assigned to the time of the previous clock read, and the last byte of the sequence is assigned with current time. Any bytes in between is assigned to a time using a linear approximation (with time of sequenc start and time of sequence stop). Thus, the time received of the first trame may be much longer if no data is send at the beginning of the logging process.

# Forum related question {#forum_related_question}

real time : </forum/topic/207/#p787>
