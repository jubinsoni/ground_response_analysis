clear all
clc
fcount=1;
displacements = load('displacement.out');

allTimes = displacements(:,1);
displacements(:,1) = [];

%numDisps = no of nodes as only displacement in
%xdirection is considered
%otherwise->numNodes = numDisps/3;(as 3 dsiplacements is recorded)
[numSteps,numDisps] = size(displacements)
central_node = floor(numDisps/2)    
%plot(displacements(:,244))
fprintf('######################################\n')
%element = 60
%element size = 0.5 in y direction
stress1 = load('stress1.out');
stress2 = load('stress2.out');
stress3 = load('stress3.out');
stress4 = load('stress4.out');
stress9 = load('stress9.out');
strain1 = load('strain1.out');
strain2 = load('strain2.out');
strain3 = load('strain3.out');
strain4 = load('strain4.out');
strain9 = load('strain9.out');
Gstress1 = load('Gstress1.out');
Gstress1(:,1) = [];
stress1(:,1) = [];
strain1(:,1) = [];
stress2(:,1) = [];
strain2(:,1) = [];
stress3(:,1) = [];
strain3(:,1) = [];
stress4(:,1) = [];
strain4(:,1) = [];
stress9(:,1) = [];
strain9(:,1) = [];

%----------------------------------
eno=55;%element no
 for i=1:1:size(stress1,1)
     X(i,1)=stress1(i,((eno-1)*5)+4);
 end
 
 for i=1:1:size(strain1,1)
     Y(i,1)=strain1(i,((eno-1)*3)+3)*100;
 end
 
 figure(fcount)
 plot(Y,X)
 fcount = fcount + 1;
 xlim([-2 2])
 
 eno=55;%element no
 for i=1:1:size(stress1,1)
     X(i,1)=stress1(i,((eno-1)*5)+4);
 end
 
 for i=1:1:size(stress1,1)
     Y(i,1)=stress1(i,((eno-1)*5)+2)*-1;
 end
 
 figure(fcount)
 plot(Y,X)
 fcount = fcount + 1;
 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 pore1=load('porePressure.out');
 
 eno=55;
 for i=1:1:size(stress1,1)
     X(i,1)=pore1(i,110)/stress1(i,((eno-1)*5)+2)*-1;
 end
 
 figure(fcount)
 plot(X)
 fcount = fcount + 1;
%  
%  
%  
%  eno=47;
%  for i=1:1:size(stress1,1)
%      X1(i,1)=stress1(i,((eno-1)*5)+4);
%  end
%  
%  for i=1:1:size(strain1,1)
%      Y1(i,1)=strain1(i,((eno-1)*3)+3)*100;
%  end
%  figure(fcount)
%  plot(Y1,X1)
%  fcount = fcount + 1;
%  xlim([-8 2])
%  ylim([-40 40])
%  
%  
%  
%  eno=29
%  for i=1:1:size(stress1,1)
%      X1(i,1)=stress1(i,((eno-1)*5)+4);
%  end
%  
%  for i=1:1:size(strain1,1)
%      Y1(i,1)=strain1(i,((eno-1)*3)+3)*100;
%  end
%  figure(fcount)
%  plot(Y1,X1)
%  fcount = fcount + 1;
%  xlim([-4 0.5])
%  ylim([-90 90])