% Extract and plot data from rate gyro and accelerometers placed onboard a
% 1.25 wingspan RC flying wing. Data are logged with a high sampling rate of 1kHz.
% Remote control instructions are also recorded and plotted at a lower
% sampling rate.
% Script also detect the launch time, and the landing (i.e. crash time).
% from inertial sensors and mark theses time with wide black vertical line.
% Time where bluetooth transmission lost errors occurs are marked with thin blue vertical
% line.
% Script written by Lubin Kerhuel -- January 2009
% see website : http://www.kerhuel.eu for more details about this script

fclose all;         % close all files
fid = -1;           % flag
%% Uncomment one of the Fid open line and run the script or run it as is
%% Morning flight (Poor wind condition)
%fid = fopen('Flight003.txt');  %46 seconds flight with end of flight
%fid = fopen('Flight004.txt');  %47 seconds flight
%fid = fopen('Flight005.txt');  %35 seconds flight
%fid = fopen('Flight006.txt');   %12.65 seconds flight with end of flight

%% Launch time flight (huge weight added on the airplane noze)
%fid = fopen('Flight010.txt');  %159 seconds flight (start at 56s)
%fid = fopen('Flight011.txt');  %66 seconds flight with end of flight
%fid = fopen('Flight012.txt');  %12.35 second flight with end of flight, more than one minute long log 
%fid = fopen('Flight013.txt');  %268.442 seconds flight - 11 errors
%fid = fopen('Flight015.txt');  %272.59 seconds flight - 7 errors

if (fid == -1)  % open user dialog to select a .txt file with flight's data
    d = dir('*.txt');
    str = {d.name};
    [s,v] = listdlg('PromptString','Select a flight datafile to plot:',...
                    'SelectionMode','single',...
                    'ListString',str);
    fid = fopen(str{s});            
end            


%% Read and close file
Rn = fread(fid);    % read txt file
fclose(fid);        % close file
    
Rr = uint16(Rn);

%% check the signature value every 11 sample, count transmission errors
idxError = 1;
Rout = [];
IndexError = [];
while ~isempty(idxError)
    idx = find(Rr==55);
    Rr = Rr(idx(1):end);

    sizeR = floor(length(Rr)/11)*11;
    Rr = Rr(1:sizeR);
    Rlocal = reshape(Rr,11,sizeR/11)';

    idxError = find(Rlocal(:,1) ~= 55);
    if isempty(idxError)
        Rout = [Rout ; Rlocal ];
    else
    Rlocal = Rlocal(1:(idxError(1)-2),:);
    Rr = Rr((idxError(1)*11):end);
    Rout = [Rout ; Rlocal ];
    IndexError(end+1) = length(Rout)+1;%idxError(1)-1;  % store place where error appears
    end
end
fprintf('%d Reception errors',length(IndexError));

%% reconstruct int16 values from binary field data
Rr = Rout;
V1 = Rr(:,2)+bitand(Rr(:,3),15)*256;
V2 = Rr(:,4)*16 + bitand(Rr(:,3),240) ./ 16;

V3 = Rr(:,5)+bitand(Rr(:,6),15)*256;
V4 = Rr(:,7)*16 + bitand(Rr(:,6),240) ./ 16;

V5 = Rr(:,8)+bitand(Rr(:,9),15)*256;
V6 = Rr(:,10)*16 + bitand(Rr(:,9),240) ./ 16;

%% Generate time
L = length(V6);
t = 0:.001:L*.001-.001;

TimeReceptionError = t(IndexError);

%ForSimulink = [t;double(V1');double(V2');double(V3');double(V4');double(V5');double(V6')];
%save ForSimulink ForSimulink;

%save CalibrationGyroZ Rr;
%save Static Rr;

%% convert data into double
GyroY = double(V1);
GyroX = double(V4);
GyroZ = double(V6);

AccelY = double(V2);
AccelX = double(V5);
AccelZ = double(V3);

%% unbias and scald gyro
GyroY = (GyroY - (2048+50) ) * 80/2048*4.93;
GyroX = (GyroX - (2048-141) ) * 80/2048*2.49;
GyroZ = (GyroZ - (2048-130) ) * 80/2048*2.5;

%% unbias accelerometers
AccelX = (AccelX + (-704-615) );
AccelY = -(AccelY + (-783) );
AccelZ = (AccelZ + (-764) );

%Accel X : vertical (Positive = acceleration toward down)
%Accel Y : horizontal forward (positive = acceleration forward) (change sign)
%Accel Z : Horizontal lateral (positive = acceleration toward left)

%% rename angular rate variables : 
p = -GyroY;  % p : roll (positive = roll right) (change sign)
q = -GyroX;  % q : pitch (negatif = pich down)  (change sign)
r = -GyroZ;  % r : yaw (positive = yaw toward right) (change sign)


%% Plot 3 rate gyro, 3 accelerometers
figure('Name','Rate gyro and accelerometers data remotely transmitted from an RC flying wing'); 
subplot(3,1,1)
plot(t,p,'b') ; hold on; plot(t,q,'r'); plot(t,r,'g'); hold off; axis tight;
ylabel({'rate gyro','deg/s'}); legend('p','q','r','Location','Best');

subplot(3,1,2)
plot(t,AccelX./630,'r') ; hold on; plot(t,AccelY./630,'b'); plot(t,AccelZ./630,'g'); hold off;axis tight;
ylabel({'Accelerometers','(g)'});


%% Reconstruct remote control and servo command data
% check the signature value (170) every 17 sample, reconstruct valide
% sequence
V7 = Rr(:,11);
V7 = double(V7);
idx2 = find(V7 == 170);         % index of all possible signature value
V7Vector = V7;

diffidx2 = diff(idx2);
tmp = 0; idx2OK=[];
for(i=1:length(diffidx2));
    if((diffidx2(i)+tmp) < 17)      % if less than 17 bytes between each signature
        i = i+1;                    % do not take into account 
        tmp = tmp + diffidx2(i);
    else
        tmp = 0;
        idx2OK(end+1) = idx2(i+1);
    end            
end
idx2OK = [idx2(1)  idx2OK(1:end-1) ];   % Only valide index separated by 17 or more bytes

t2 = t(idx2OK); % Time index for theses datas

%% Reconstruct data from remote control and servo control command
Check = V7Vector((idx2OK-1)+1); % column with signature value : 170
VertLeft = V7Vector((idx2OK-1)+2) + V7Vector((idx2OK-1)+3)*256;
HorzLeft = V7Vector((idx2OK-1)+4) + V7Vector((idx2OK-1)+5)*256;
VertRight = V7Vector((idx2OK-1)+6) + V7Vector((idx2OK-1)+7)*256;
HorzRight = V7Vector((idx2OK-1)+8) + V7Vector((idx2OK-1)+9)*256;
Pot1 = V7Vector((idx2OK-1)+10) + V7Vector((idx2OK-1)+11)*256;
Pot2 = V7Vector((idx2OK-1)+12) + V7Vector((idx2OK-1)+13)*256;
ServoLeft = V7Vector((idx2OK-1)+14) + V7Vector((idx2OK-1)+15)*256;
ServoRight = V7Vector((idx2OK-1)+16) + V7Vector((idx2OK-1)+17)*256;

verif = find(Check ~= 170);
if isempty(verif)
    disp('- data processing OK');
else
    disp('- data processing Not OK');
end

%% take into account sign of data
idx = find(VertLeft > 65535 / 2);
VertLeft(idx)= VertLeft(idx)-65536;

idx = find(HorzRight > 65535 / 2);
HorzRight(idx)= HorzRight(idx)-65536;

%% Plot remote control data
subplot(3,1,3)
plot(t2(1:length(VertLeft)),VertLeft,t2(1:length(HorzRight)),HorzRight);
legend('Up/Down stick','roll stick','Location','Best');
axis tight;
ylim([-6000 6000])
ylabel('RC command')
xlabel('Time (s)')





%%




%% Search and Plot Tlaunch
% find the end of the first saturation on the Y accel axis (longitudinal)
Tmp = find(AccelY == 783); % Saturation value
Tlaunch = t(Tmp(1));
Tmp2 = find(diff(Tmp) >20 );
if ~isempty(Tmp2)
    Tlaunch = t(Tmp(Tmp2(1))+1);
end

figure(1);
subplot(3,1,1); hold on; plot([Tlaunch Tlaunch+eps],[-40000 40000],'k','linewidth',2); hold off;
subplot(3,1,2); hold on; plot([Tlaunch Tlaunch+eps],[-40000 40000],'k','linewidth',2); hold off;
subplot(3,1,3); hold on; plot([Tlaunch Tlaunch+eps],[-40000 40000],'k','linewidth',2); hold off;

%% Search and plot TCrash
% find the first deceleration on the Y accel axis that occurs after Tlaunch (longitudinal axis)
Tmp = find(AccelY < -500); 
if isempty(Tmp) 
    Tmp = length(AccelY);
end
Tmp2 = find(t(Tmp) > (Tlaunch+1));  % take 1 second marging
if ~isempty(Tmp2)
    Tcrash = t(Tmp(Tmp2(1)));
else Tcrash = t(end);
end

figure(1);
subplot(3,1,1); hold on; plot([Tcrash Tcrash+eps],[-40000 40000],'k','linewidth',2);hold off;
subplot(3,1,2); hold on; plot([Tcrash Tcrash+eps],[-40000 40000],'k','linewidth',2);hold off;
subplot(3,1,3); hold on; plot([Tcrash Tcrash+eps],[-40000 40000],'k','linewidth',2);hold off;

subplot(3,1,1); hold on; plot([TimeReceptionError ; TimeReceptionError+eps],[-40000 40000]'*ones(1,length(TimeReceptionError)),'--c');hold off;
subplot(3,1,2); hold on; plot([TimeReceptionError ; TimeReceptionError+eps],[-40000 40000]'*ones(1,length(TimeReceptionError)),'--c');hold off;
subplot(3,1,3); hold on; plot([TimeReceptionError ; TimeReceptionError+eps],[-40000 40000]'*ones(1,length(TimeReceptionError)),'--c');hold off;


disp(sprintf('Flight time is %3.2f seconds',Tcrash-Tlaunch));
subplot(3,1,1) ;title(sprintf('Flight of %3.2f seconds : from %3.2f s until %3.2f s',Tcrash-Tlaunch,Tlaunch,Tcrash));
text(Tlaunch,-200,'\leftarrow Take off');
text(Tcrash,-200,'\leftarrow Crash');
text(Tlaunch/2+Tcrash/2,200,'Flight');

%% end of raw data plot

break;

%% Interpolation
VertLeft = interp1q(t2',VertLeft,t');
HorzLeft = interp1q(t2',HorzLeft,t');
VertRight = interp1q(t2',VertRight,t');
HorzRight = interp1q(t2',HorzRight,t');
Pot1 = interp1q(t2',Pot1,t');
Pot2 = interp1q(t2',Pot2,t');
ServoLeft = interp1q(t2',ServoLeft,t');
ServoRight = interp1q(t2',ServoRight,t');

VertLeft(isnan(VertLeft)) = 0;
HorzLeft(isnan(HorzLeft)) = 0;
VertRight(isnan(VertRight)) = 0;
HorzRight(isnan(HorzRight)) = 0;
Pot1(isnan(Pot1)) = 0;
Pot2(isnan(Pot2)) = 0;
ServoLeft(isnan(ServoLeft)) = 0;
ServoRight(isnan(ServoRight)) = 0;


% few more test

%plot(sqrt(AccelX.^2+AccelY.^2+AccelZ.^2))
%plot(cumsum(sqrt(AccelX.^2+AccelY.^2+AccelZ.^2)-605))

% figure(2);
% plot(t,VertLeft); hold on;
% plot(t,GyroX*10,'r'); hold on;
% 
% figure(3);
% plot(t,HorzRight); hold on;
% plot(t,GyroY*10,'r'); hold on;
% 
% figure(4);
% VertLeft2 = VertLeft * 90/2000;
% plot(diff(VertLeft2)*1000);


%% export graph
%print('-depsc2','-r600','graph');

%Lauhch close up
for i=1:3
    subplot(3,1,i); xlim([Tlaunch-.6 Tlaunch+.4]);
end

for i=1:3
    subplot(3,1,i); xlim([Tcrash-.2 Tcrash+.6]);
end
