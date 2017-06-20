# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 16:02:49 2017

@author: jubin
"""

import matplotlib.pyplot as plt

mylinear = []
myquadratic = []
myexp = []
mycubic = []
mysapmle = []
mysample = []

for i in range(30):
    mysample.append(i)
    mylinear.append(i)
    myquadratic.append(i*i)
    mycubic.append(i**3)
    myexp.append(i**5)
    
    
print(mysample,mylinear,myquadratic,mycubic,myexp)

#plt.figure at start
#xlim and ylim before plot command
#xlabel and ylabel after plot command
#title after plot
#legend at the end
plt.ylim(0,100)
plt.xlim(0,20)
plt.plot(mysample,mylinear,label = 'linear',linewidth = 3.0)
plt.plot(mysample,myquadratic,label = 'quad')
plt.plot(mysample,mycubic,label = 'cubic')

plt.xlabel('sample points')
plt.ylabel('quad points')
plt.title('functions')

plt.legend(loc = 'upper right')

plt.figure('linquad')
plt.clf()
plt.plot(mysample,mylinear,'b-',label = 'linear')
plt.plot(mysample,myquadratic,'ro',label = 'quad')
plt.legend(loc = 'upper left')
plt.title('linear vs quadratic')

plt.figure('cubic')
plt.clf()
plt.plot(mysample,mylinear,'b-',label = 'linear')
plt.plot(mysample,myquadratic,'g^',label = 'cubic')
plt.legend(loc = 'upper left')
plt.title('linear vs cubic')


plt.figure('exp')
plt.clf()
plt.subplot(121) #(defination rows,defination columns,position)
plt.plot(mylinear,myexp,'r--',label = 'exp')
plt.legend(loc = 'upper left')#should be at the end
plt.title('linear vs exp')

plt.subplot(122)
plt.plot(mylinear,myquadratic,'b^',label = 'quadratic')
plt.legend(loc = 'upper left')#should be at the end
plt.title('linear vs quadratic')


plt.figure('cube exp log')
plt.clf()
plt.plot(mysample,mycubic,'g--',label = 'cubic',linewidth = 2.0)
plt.plot(mysample,myexp,'r',label = 'exp',linewidth = 4)





x=[]
y=[]
for i in range(1,11):
    x.append(i)
    y.append((x[i-1]*x[i-1])+(2*x[i-1])+(5))
    

plt.figure('quiz')
plt.plot(x,y,'b-',label = 'quiz',linewidth = 4.0)
plt.legend(loc = 'upper left')
plt.title('equation')

l=[2,3,1,8,9]
print(l)
for i in range(0,5):
    max = 0;
    maxind = -1;
    for j in range (0,5):
        if(l[j]>max):
            max=l[j];
            maxind=j;
            
    l[maxind]=-1
    print max,

import numpy as np
a=np.array([1,2,3,4])
print a
