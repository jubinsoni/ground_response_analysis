# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 03:19:50 2017

@author: jubin
"""

from Tkinter import *
import ttk

root = Tk()

topFrame = ttk.Frame(root)
topFrame.pack()

bottomFrame = ttk.Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = ttk.Button(topFrame,text='Button1')
button2 = ttk.Button(topFrame,text='Button2')
button3 = ttk.Button(topFrame,text='Button3')
label1 = ttk.Label(topFrame,text='one')
label1.pack(fill=X)

label2 = ttk.Label(topFrame,text='two')
label2.pack(fill=X)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)




label4 = ttk.Label(bottomFrame,text='Name')
label5 = ttk.Label(bottomFrame,text='Pass')
entry1 = ttk.Entry(bottomFrame)
entry2 = ttk.Entry(bottomFrame)
label4.grid(row = 0,column = 0)
label5.grid(row = 1,column = 0)
entry1.grid(row = 0,column = 1)
entry2.grid(row = 1,column = 1)

check1 = ttk.Checkbutton(bottomFrame,text='keep me loged in')
check1.grid(columnspan=2)

radio1 = ttk.Radiobutton(bottomFrame,text='radio1',value=1)
radio1.grid(columnspan = 2)
radio2 = ttk.Radiobutton(bottomFrame,text='radio2',value=2)
radio2.grid(columnspan = 2)


def printname(event):
    print 'my name is bucky'


button4 = ttk.Button(bottomFrame,text='Button4')
button4.bind('<Button-1>',printname)
button4.grid()


    
    
root.mainloop()