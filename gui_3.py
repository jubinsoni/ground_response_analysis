# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:08:34 2017

@author: jubin
"""

from Tkinter import *
import ttk
import tkMessageBox
import tkFileDialog as filedialog



    
class nGui:
    
    def __init__(self,master):
        frame1 = ttk.Frame(master)
        frame1.pack()
        #button
        self.button1 = ttk.Button(frame1,text='button1',command=self.printmessage)
        self.button1.grid(row=0,column=0)
        
        self.button2 = ttk.Button(frame1,text='quit',command=self.Quit)
        self.button2.grid(row=1,column=0)
        
        self.button3 = ttk.Button(frame1,text = 'next')
        self.button3.grid(row=2,column=0)
        ##
        
        # Menu construction
        menubar=Menu(frame1)
        #filemenu
        filemenu= Menu(menubar,tearoff=0)
        filemenu.add_command(label="New")
        menubar.add_cascade(label='File',menu=filemenu)
    
    def printmessage(self):
        print("this actually worked")
        
        
    def Quit(self):
    #mExit = tkMessageBox.askyesno(title='quit',message='Are you Sure?')
        mExit = tkMessageBox.askokcancel(title='quit',message='Are you Sure?')
        if(mExit > 0):
            root.destroy()
            return
    
        
        
    

root = Tk()
root.geometry("1280x720")
b = nGui(root)
root.mainloop()