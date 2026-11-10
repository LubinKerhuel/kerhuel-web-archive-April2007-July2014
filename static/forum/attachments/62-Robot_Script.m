clear all;
close all;

Te=2e-2;    %% discret time
% Robot's model (continuous time)
A = [0 1 0 0 ; 0 -0.0097 11.1591 0 ; 0 0 0 1 ; 0 -0.0293 172.116 0 ];   % robot's dynamic
B = [0 0.0815 0 0.2456]';  % input : suppose you can apply a translating force on the robot ?
C = [0 0 1 0]; % Measurement : suppose you measure the angle
D = 0 ;     %% this is probably not 0 ?

Robot_s = ss(A,B,C,D);

%% Discretizing :
Robot_z = c2d(Robot_s,Te,'zoh');
[Az,Bz,Cz,Dz,Ts]=ssdata(Robot_z);

rank(obsv(Robot_s)) %% System not observable but
rank(ctrb(Robot_s)) %% controllable

%% LQR synthesis
R=1e-2;
Q = diag([1e5 0 1e-2 0]);  % you must find the best ponderation ...
[K,S,e] = dlqr(Az,Bz,Q,R);
log(abs(e))/Te
%Poles_s = log(abs(eig(Az-Bz*K)))/Te   % en continue 
