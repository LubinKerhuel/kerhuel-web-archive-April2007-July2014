clc
clear all
close all


% definir a porta serie a utilizar
s=serial('COM5', 'BaudRate',19200,'DataBits',8,'StopBits',1);

fopen(s)

 
handle = plot(0);
hold on;
idata = 0;
valor_anterior = 0;

valores_recebidos=[];
for i= 1:500,
   
    
     vala1 = fread(s,1,'uint8')
     vala2 = fread(s,1,'uint8')
     vala3 = fread(s,1,'uint8')
    
     val=(bitor(bitshift(vala3,8),vala2));
    
    if isempty(val) break; end
    if idata==0, valor_anterior=val; end
    idata = idata + 1;
    plot([idata-1 idata], [valor_anterior val],'*-');
    valor_anterior=val;
    valores_recebidos(i)=val;
    if idata<100,
        xlim([0 100]);
    else
        xlim([0 idata+5]);
    end
    drawnow
end


fclose(s);
delete(s);
clear s