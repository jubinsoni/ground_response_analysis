# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:44:42 2017

@author: jubin
"""
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import tkMessageBox
import tkFileDialog as filedialog



import Tkinter as tk
import ttk


LARGE_FONT=("Verdana",12)
NORM_FONT=("Verdana",10)
SMALL_FONT=("Verdana",8)

style.use("ggplot") 

f = Figure()
a = f.add_subplot(313)

def popupmsg(msg):
    popup = tk.Tk()    
    popup.wm_title("!")
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="top",fill="x",pady=10)
    B1 = ttk.Button(popup,text="Okay",command = popup.destroy)
    B1.pack()
    popup.mainloop()
        
def animate(i):    
    pullData = open("sampleData.txt","r").read()
    dataList = pullData.split('\n')
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine) >1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
                
    a.clear()
    a.plot(xList,label = 'xlab')
    a.plot(yList,label = 'ylab')
    a.legend()
    
    title = "plot title\nLast ydata: "+str(xList[-1])+","+str(yList[-1])#to get last data entered
    a.set_title(title)
    
def mQuit():
    #mExit = tkMessageBox.askyesno(title='quit',message='Are you Sure?')
    mExit = tkMessageBox.askokcancel(title='quit',message='Are you Sure?')
    if(mExit > 0):
        #nGui.destroy()
        app.destroy()
        return
    
    
    
#all message Box prompt
def mAbout():
    tkMessageBox.showinfo(title="About GResponse",message="GResponse 1.0\nThis app is created by\nJubin Kumar Soni\nunder the guidance of Dr.Supriya Mohanty")
    #tkMessageBox.showerror(title="Say Hello",message="Hello World")
    #tkMessageBox.showwarning(title="Say Hello",message="Hello World")
    #tkMessageBox.askquestion(title="Say Hello",message="Hello World")
    return
    
    
class nGui(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self,default="clienticon.ico")
        tk.Tk.wm_title(self,"GResponse")
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Restart")
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command = mQuit)
        menubar.add_cascade(label="File",menu=filemenu)
        
        helpmenu= tk.Menu(menubar,tearoff=0)
        helpmenu.add_command(label="Help Docs")
        helpmenu.add_command(label="About",command = mAbout)
        menubar.add_cascade(label='Help',menu=helpmenu)
        
        tk.Tk.config(self,menu=menubar)
        
        
        self.frames = {}
        
        for F in (StartPage,BTCe_Page):
            frame = F(container,self)
            self.frames[F]=frame    
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(StartPage)
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    

def qf(param):
    print (param)
    
class StartPage(tk.Frame):
    
#Browze file(open file)
    def nOpen():
        myopen = filedialog.askopenfile()
        label2 = tk.Label(text=myopen)
        label2.grid(row = 5,column = 0)
        return
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text=("""GUI application
 use at you own risk.There is no 
  promise of warranty"""),font=LARGE_FONT)
        
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text="Agree",
                          command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()
        
        
        button2=ttk.Button(self,text="Disagree",
                          command=mQuit)        
        button2.pack()
        
class PageOne(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: controller.show_frame(StartPage))        
        button1.pack()
        
        

class BTCe_Page(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graph Page!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: controller.show_frame(StartPage))        
        button1.pack()        
        
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand = True) 
        
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand = True)

app = nGui()
app.resizable(0,0)
w = 1200 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = app.winfo_screenwidth() # width of the screen
hs = app.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
ani = animation.FuncAnimation(f,animate,interval=1000)
app.mainloop()