s=serial('COM2') %%define s as a serial port using COM2 port

set(s,'BaudRate',19200) %%set s Bauds rate to be 19200

fopen(s); %%open serial port s (COM2) to use

A=1;

fwrite(s,A); %%writes the binary data A

fclose(s);

delete(s);