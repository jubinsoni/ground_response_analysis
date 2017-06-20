# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:01:35 2017

@author: jubin
"""

import Tkinter as tk
import ttk
import tkMessageBox
import tkFileDialog as filedialog



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.title("Gresponse")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            ttk.Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky='E'+'W')
        
        
        def bOpen():
            myopen = filedialog.askopenfile()
            mlabel4 = tk.Label(Frame1,text=myopen)
            mlabel4.grid(row = 1,column = 0)
            return
        
        Frame1 = tk.Frame(master, bg="black")
        Frame1.rowconfigure(5,weight=1)
        Frame1.columnconfigure(3,weight=1)
        ttk.Button(Frame1,text='Browse',command=bOpen).grid(row=0,column=0,sticky='E'+'W')
        ttk.Button(Frame1,text='Browse',command=bOpen).grid(row=4,column=0,sticky='E'+'W')
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = 'W'+'E'+'N'+'S')
        
        Frame21 = tk.Frame(master, bg="red")
        ttk.Button(Frame21,text='Buuton').grid(row=0,column=0)
        Frame21.grid(row = 0, column = 1, rowspan = 2, columnspan = 4, sticky = 'W'+'E'+'N'+'S')
        Frame22 = tk.Frame(master, bg="blue")
        Frame22.grid(row = 2, column = 1, rowspan = 2, columnspan = 4, sticky = 'W'+'E'+'N'+'S')
        Frame23 = tk.Frame(master, bg="green")
        Frame23.grid(row = 4, column = 1, rowspan = 2, columnspan = 4, sticky = 'W'+'E'+'N'+'S')
    
root = tk.Tk()
root.geometry("1280x720")
app = Application(master=root)
app.mainloop()