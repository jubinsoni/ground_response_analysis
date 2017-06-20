# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:09:54 2017

@author: jubin
"""


import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold='nan',suppress=False)

stress1=np.loadtxt("stress1.out")
strain1=np.loadtxt("strain1.out")



eno=55
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(strain1[i,((eno-1)*3)+3]*100)
      


plt.figure('1')
plt.clf()
plt.xlim(-4,0.5)
plt.ylim(-40,40)
plt.plot(Y,X)
plt.title('shear stress vs shear strain(%) at 3m from surface',color='r')
plt.grid()
plt.show()

eno=47
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(strain1[i,((eno-1)*3)+3]*100)
      


plt.figure('2')
plt.clf()
plt.xlim(-6,1)
plt.ylim(-40,40)
plt.plot(Y,X)
plt.title('shear stress vs shear strain(%) at 7m from surface',color='r')
plt.grid()
plt.show()


eno=29
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(strain1[i,((eno-1)*3)+3]*100)
      


plt.figure('3')
plt.clf()
plt.xlim(-4,0.5)
plt.ylim(-80,80)
plt.plot(Y,X)
plt.title('shear stress vs shear strain(%) at 16m from surface',color='r')
plt.grid()
plt.show()


eno=55
rs1,cs1=stress1.shape
rs2,cs2=stress1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(stress1[i,((eno-1)*5)+2]*-1)
      


plt.figure('4')
plt.clf()
plt.xlim(0,100)
plt.ylim(-40,40)
plt.plot(Y,X)
plt.title('shear stress vs effective stress(sigma''y'') at 3m from surface',color='r')
plt.grid()
plt.show()

eno=47
rs1,cs1=stress1.shape
rs2,cs2=stress1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(stress1[i,((eno-1)*5)+2]*-1)
      


plt.figure('5')
plt.clf()
plt.xlim(0,100)
plt.ylim(-40,40)
plt.plot(Y,X)
plt.title('shear stress vs effective stress(sigma''y'') at 7m from surface',color='r')
plt.grid()
plt.show()


eno=29
rs1,cs1=stress1.shape
rs2,cs2=stress1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append(stress1[i,((eno-1)*5)+4])
 
for i in range(0,rs2-1):
     Y.append(stress1[i,((eno-1)*5)+2]*-1)
      


plt.figure('6')
plt.clf()
plt.xlim(0,250)
plt.ylim(-80,80)
plt.plot(Y,X)
plt.title('shear stress vs effective stress(sigma''y'') at 16m from surface',color='r')
plt.grid()
plt.show()

######################################################



pore1=np.loadtxt("porePressure.out")
eno=55
pele=109
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append((pore1[i,pele]-pore1[0,pele])/stress1[0,((eno-1)*5)+2]*-1)
     
              
plt.figure('7')
plt.clf()
plt.plot(X)
plt.title('pore water pressure ratio vs time steps at 3m from surface',color='r')
plt.grid()  
plt.show()




eno=47
pele=94
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append((pore1[i,pele]-pore1[0,pele])/stress1[0,((eno-1)*5)+2]*-1)
     
                   
              
plt.figure('8')
plt.clf()
plt.plot(X)
plt.title('pore water pressure ratio vs time steps at 7m from surface',color='r')
plt.grid()
plt.show()



eno=29
pele=58
rs1,cs1=stress1.shape
rs2,cs2=strain1.shape
X=[]
Y=[]
for i in range(0,rs1-1):
     X.append((pore1[i,pele]-pore1[0,pele])/stress1[0,((eno-1)*5)+2]*-1)
     


plt.figure('9')
plt.clf()
plt.plot(X)
plt.title('pore water pressure ratio vs time steps at 16m from surface',color='r')
plt.grid()
plt.show()