# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:47:53 2017

@author: jubin
"""

import Tkinter as tk
import ttk
import tkFileDialog 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from scipy import integrate
import os


global ml
ml=2


#0.1)initialization for plot
style.use("ggplot")
f0 = Figure(figsize=(5,5),dpi=100)
a10 = f0.add_subplot(311)
a20 = f0.add_subplot(312)
a30 = f0.add_subplot(313) 

def animate0(i):
    accln=np.loadtxt("test1.txt")
    g=9.81#g=9.81m/sec2
        
    rs1,cs1=accln.shape
    X=[]
    Y1=[]
    for i in range(0,rs1-1):
        X.append(accln[i,0])
        Y1.append(accln[i,1]*g)
        
    a10.clear()
    a10.plot(X,Y1)
    a10.legend()
    a10.set_title('corresponing input time histories\naccln(m/sec^2),vel(m\sec),displacement(m)')


    Y2=integrate.cumtrapz(Y1,X,initial=0)
         
    a20.clear()
    a20.plot(X,Y2)
    a20.legend()
    
    
    
    Y3=integrate.cumtrapz(Y2,X,initial=0)
    
    a30.clear()
    a30.plot(X,Y3)
    a30.legend()
#0.1)->
    
#0.2)initialization for plot

f1 = Figure(figsize=(5,5),dpi=100)
a11 = f1.add_subplot(311)
a21 = f1.add_subplot(312)
a31 = f1.add_subplot(313) 

def animate1(i):
    accln=np.loadtxt('sample.txt')
            
    a11.clear()
    a11.plot(accln)
    a11.legend()
    a11.set_title('corresponing input time histories\naccln(m/sec^2),vel(m\sec),displacement(m)')
#0.2)->   
    

#1)container creation(all frame will be inside this container)    
#__init__ method gets called automatically if any object of that class is made
class nGui(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self,default="eqicon.ico")
        tk.Tk.wm_title(self,"GResponse")   
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        ###1)->
        
        
        #2)multi frame creation
        self.frames = {} #declaring empty dictionary for frames
        
                      
                      
        #so that F object contains all frames              
        for F, arg  in ((startpage,None),(pageselect,None),(pagegraph,None),(page2D1,None),(page2D2,None),(page3D1,None),(page3D2,None),(pagegraph1,None)):#iterate through all the pages
            page_name = F.__name__
            frame = F(parent=container, controller=self, attr=arg) 
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            if(arg == None):
                pass
            else:
                frame.arg = arg
                
        
        
        #starting startpage class
        self.show_frame('startpage')#to show startpage by default
    
    
    


    def show_frame(self,cont,arg=None): #cont = controller(or key=which frame to show)
        frame = self.frames[cont]
        frame.tkraise()
        if(arg == None):
            pass
        else:
            frame.attr = arg
            
         
    
class startpage(tk.Frame): #class(inheritence),here we are inheriting tk.Frame for use
    def __init__(self,parent,controller, attr=None):
        tk.Frame.__init__(self,parent)
        
        label1 = ttk.Label(self,text='select a *.txt file from button below.')
        label1.pack(padx=10,pady=10)
        
        label2 = ttk.Label(self,text='Text file must contain time steps( in sec) and accln(in g) data')
        label2.pack(padx=10,pady=10)
        
        label3 = ttk.Label(self,text='Note: timesteps and accln data should be space seperated')
        label3.pack(padx=10,pady=10)
        
        button1 = ttk.Button(self,text='browse accln time history file',command=self.onOpen)
        button1.pack()
        
        label4 = ttk.Label(self,text='Your selected file directory will be shown below :-')
        label4.pack(padx=10,pady=10)
        
        button2 = ttk.Button(self,text='Next',command=lambda:controller.show_frame('pagegraph'))
        button2.pack()
        
    
    def onOpen(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        mlabel4 = tk.Label(self,text='File Path:-'+fl)
        mlabel4.pack()        
        if(fl != ''):
            self.text = self.readFile(fl)
            
        with open('test1.txt', 'w') as out_file:
                out_file.write(self.text)
                
    

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text
        #2)->
    
    #3)adding page1 after startpage
class pageselect(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        label = ttk.Label(self,text='select type of analysis')
        label.grid(row=0,column=0,columnspan=2)
        
        
        
        self.rad_var=tk.IntVar()
        radio_1 = ttk.Radiobutton(self,text='2D analysis',value=1,variable=self.rad_var)
        radio_1.grid(row=1,column=0,columnspan=2)
        radio_2 = ttk.Radiobutton(self,text='3D analysis',value=2,variable=self.rad_var)
        radio_2.grid(row=2,column=0,columnspan=2)
        
        button1 = ttk.Button(self,text='back to home',command=lambda:controller.show_frame('startpage'))
        button1.grid(row=3,column=0) 
        
        #NOTE..1:this is how we move to next page via method
        button2 = ttk.Button(self,text='Next',command=lambda:self.select(self.rad_var,controller))
        button2.grid(row=3,column=1)
        #->
        
        
    def select(self,rad_var,cont):
        if(self.rad_var.get() == 1):
            cont.show_frame('page2D1')
        elif(self.rad_var.get() == 2):
            cont.show_frame('page3D1')
        #cont.show_frame(pagetwo)
        #NOTE..1.......

    #3)adding page2 
class page2D2(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
        label1 = ttk.Label(self,text='Final step 2D analysis page')
        label1.grid(row=0,column=0,columnspan=2)
        
        button1 = ttk.Button(self,text='back to home',command=lambda:controller.show_frame(startpage))
        button1.grid(row=1,column=0,columnspan=1,sticky='w') 
        button2 = ttk.Button(self,text='Reselect parameters',command=lambda:controller.show_frame(startpage))
        button2.grid(row=2,column=0,columnspan=1,sticky='w') 
        
        label2 = ttk.Label(self,text='The analysis is going to take approx 5 mins depending on your parameter choice')
        label2.grid(row=3,column=0,columnspan=2)
        
        label2 = ttk.Label(self,text='are you sure you want to continue ?')
        label2.grid(row=4,column=0,columnspan=2)
        
        button3 = ttk.Button(self,text='dummy',command=lambda:self.onclickz(controller))
        button3.grid(row=5,column=0,columnspan=2)
        
    
    
    def onclickz(self,cont):
        print self.attr
        init = self.attr
        args_init = []
        
        args_init=['{:.3f}'.format(x) for x in init]
            
        
        args = "" 
        for i in range(len(args_init)):
            args = args +" " + args_init[i]
            
            
            
        str_1 = "opensees learn_tcl.tcl"
        
        str_1 = str_1 + " " + args 
        os.system(str_1)
        
        file = open('sample.txt', 'r') 
        print file.read() 
        file.close()
        cont.show_frame('pagegraph1')
        #print ml # No need for global declaration to read value of globvar
        #print arg
        #->
        
   #3)adding page3
class pagegraph(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        label = ttk.Label(self,text='graph page')
        label.pack()
        
        button1 = ttk.Button(self,text='back to home',command=lambda:controller.show_frame('startpage'))
        button1.pack() 
        
        button2 = ttk.Button(self,text='Next',command=lambda:controller.show_frame('pageselect'))
        button2.pack() 
        
        ###3.2)plotting in a frame
        
        canvas = FigureCanvasTkAgg(f0,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand = True) 
        
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand = True)
        #->
        
        
        #-> 
        
    #3)adding page4 
class page2D1(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        
        #self.columnconfigure(column no,relative weight)
        #both relative weight = 1 means both will have equal contribution
        #ipadx=internal spacing
        #padx=external spacing
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        
        label1 = ttk.Label(self,text='2D analysis page')
        label1.grid(row=0,column=0,columnspan=4)
        
        button1 = ttk.Button(self,text='Back to home',command=lambda:controller.show_frame('startpage'))
        button1.grid(row=1,column=0,sticky='nsew',columnspan=1)
        
        button2 = ttk.Button(self,text='Reselect type of analysis ',command=lambda:controller.show_frame('pageselect'))
        button2.grid(row=2,column=0,sticky='nsew',columnspan=1)
        
        
        label2 = ttk.Label(self,text='Define your parameters')
        label2.grid(row=2,column=0,columnspan=4)
        
        label31 = ttk.Label(self,text='Bottom layer')
        label31.grid(row=3,column=0,columnspan=2)
        
        label32 = ttk.Label(self,text='Top layer')
        label32.grid(row=3,column=2,columnspan=2)
        
        L11 = ttk.Label(self, text="User Name")
        L11.grid(row=4,column=0,sticky='e',ipadx=5,pady=10)
        
        self.E11 = ttk.Entry(self)
        self.E11.insert(0,124)#To set default value in insert box 
        self.E11.grid(row=4,column=1,sticky='w',ipadx=5,pady=10)
        
        L21 = ttk.Label(self, text="User Name")
        L21.grid(row=5,column=0,sticky='e',ipadx=5,pady=10)
        self.E21 = ttk.Entry(self)
        self.E21.grid(row=5,column=1,sticky='w',ipadx=5,pady=10)
        
        L31 = ttk.Label(self, text="User Name")
        L31.grid(row=6,column=0,sticky='e',ipadx=5,pady=10)
        self.E31 = ttk.Entry(self)
        self.E31.grid(row=6,column=1,sticky='w',ipadx=5,pady=10)
        
        L12 = ttk.Label(self, text="User Name")
        L12.grid(row=4,column=2,sticky='e',ipadx=5,pady=10)
        self.E12 = ttk.Entry(self)
        self.E12.grid(row=4,column=3,sticky='w',ipadx=5,pady=10)
        
        L22 = ttk.Label(self, text="User Name")
        L22.grid(row=5,column=2,sticky='e',ipadx=5,pady=10)
        self.E22 = ttk.Entry(self)
        self.E22.grid(row=5,column=3,sticky='w',ipadx=5,pady=10)
        
        L32 = ttk.Label(self, text="User Name")
        L32.grid(row=6,column=2,sticky='e',ipadx=5,pady=10)
        self.E32 = ttk.Entry(self)
        self.E32.grid(row=6,column=3,sticky='w',ipadx=5,pady=10)
        
        button3 = ttk.Button(self,text='run analysis',command=lambda:self.on_button(controller))
        button3.grid(row=7,column=1)
        
    def on_button(self,cont):
        print(self.E11.get())
        self.x1=[]
        self.x1.append(11)
        self.x1.append(12)
        self.x1.append(13)
        self.x1.append(1)
        self.x1.append(2)
        self.x1.append(3)
        self.x1.append(41)
        self.x1.append(42)
        self.x1.append(43)
        #x1 ka lenth to make sure all variables filled
        #print self.x1
        global ml # Needed to modify global copy of globvar
        ml = 7
        cont.show_frame('page2D2',self.x1)
        #->
        
    #3)adding page2 
class page3D1(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        
        label1 = ttk.Label(self,text='page3D')
        label1.grid(row=0,column=0,columnspan=4)
        
        button1 = ttk.Button(self,text='back to home',command=lambda:controller.show_frame('startpage'))
        button1.grid(row=1,column=0,sticky='nsew',columnspan=1)
        
        button2 = ttk.Button(self,text='Reselect type of analysis',command=lambda:controller.show_frame('pageselect'))
        button2.grid(row=2,column=0,sticky='nsew',columnspan=1) 
        
        label2 = ttk.Label(self,text='Enter no of layers for analysis')
        label2.grid(row=3,column=1,sticky='e',ipadx=5,pady=10)
        
        self.E1 = ttk.Entry(self)
        self.E1.insert(0,2)#To set default value in insert box 
        self.E1.grid(row=3,column=2,sticky='w',ipadx=5,pady=10)
        
        button4 = ttk.Button(self,text='next',command=lambda:self.button_add(controller))
        button4.grid(row=4,column=2,columnspan=1)
        #->
    def button_add(self,cont):
        self.var1 = self.E1.get()
        cont.show_frame('page3D2',self.var1)
        
        
   #3)adding page2 
    
    
    #3)adding page2 
class page3D2(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        
        button = ttk.Button(self,text='next',command=lambda:self.button_add(controller,dynamic_buttons))
        dynamic_buttons=[]
        dynamic_buttons.append(button)
        button.grid()
        #->
    def button_add(self,cont,dynamic):
        nl = int(self.attr)
        print nl
        dynamic[0].destroy()
        for i in range(0,2*nl):
            self.columnconfigure(i,weight=1)
            
         
        label = ttk.Label(self,text='page3D2')
        label.grid(row=0,column=0,columnspan=nl)
            
        button1 = ttk.Button(self,text='restart app',command=lambda:restart_program())
        button1.grid(row=1,column=0,sticky='nsew',columnspan=1)
        
        label1 = ttk.Label(self,text='no of layers for analysis selected:'+ str(nl))
        label1.grid(row=2,column=1,sticky='e',ipadx=10,pady=10)
        
        r1=3
        t=0
        for i in range(0,nl):
            L11 = ttk.Label(self, text=" User Name ")
            L11.grid(row=r1,column=t,sticky='e')
            t=t+1
            
            self.E11 = ttk.Entry(self)
            self.E11.insert(0,124)#To set default value in insert box 
            self.E11.grid(row=r1,column=t,sticky='w')
            t=t+1
            
        
        def restart_program():
            root.destroy()
            os.system("python gui_4.py")
            
   #3)adding page2 
    
    
class pagegraph1(tk.Frame): #default#for every page class,inherit tk.Frame everytime
    def __init__(self,parent,controller, attr=None): #default
        tk.Frame.__init__(self,parent) #default
        #3)->
        ##3.1)options in page1
        label = ttk.Label(self,text='graph page 1')
        label.pack()
        
        button1 = ttk.Button(self,text='back to home',command=lambda:controller.show_frame('startpage'))
        button1.pack() 
        
        button2 = ttk.Button(self,text='Next',command=lambda:controller.show_frame('pageselect'))
        button2.pack() 
        
        ###3.2)plotting in a frame
        
        canvas = FigureCanvasTkAgg(f1,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand = True) 
        
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand = True)
        #->
       

        
root = nGui()

#root.style = ttk.Style()
#('clam', 'alt', 'default', 'classic')
#root.style.theme_use("classic")
#root.style.configure("TFrame", background="#333")

root.resizable(0,0)
w = 1200 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
ani0 = animation.FuncAnimation(f0,animate0,interval=1000)
ani1 = animation.FuncAnimation(f1,animate1,interval=1000)
root.mainloop()


#test page code
#button1 = ttk.Button(self,text='page1',command=lambda:qf('this worked'))
#button1.pack()  
#lambda:controller.show_frame(pageone))

#NOTE:
#command should get only lambda