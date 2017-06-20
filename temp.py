# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
photo = PhotoImage(file="icon.gif")
w = Label(parent, image=photo)
w.photo = photo
w.pack()
"""
import Tkinter as tk
import tkMessageBox
import tkFileDialog as filedialog
import tkFileDialog 
import ttk

def nhello():
    ntext = ment.get()
    nlabel1 = tk.Label(text = ntext,fg = 'white',bg = 'gray',font=("Helvetica", 16))
    #nlabel1 = Label(text = 'Hello',fg = 'white',bg = 'gray',font=("Helvetica", 16))
    nlabel1.grid(row = 4,column = 0)
    
def nNew():
    mlabel3 = tk.Label(nGui,text="You Clicked New")
    mlabel3.grid(row = 6 , column = 0)
    return

#all message Box prompt
def mAbout():
    tkMessageBox.showinfo(title="Say Hello",message="Hello World")
    #tkMessageBox.showerror(title="Say Hello",message="Hello World")
    #tkMessageBox.showwarning(title="Say Hello",message="Hello World")
    #tkMessageBox.askquestion(title="Say Hello",message="Hello World")
    return

def mQuit():
    #mExit = tkMessageBox.askyesno(title='quit',message='Are you Sure?')
    mExit = tkMessageBox.askokcancel(title='quit',message='Are you Sure?')
    if(mExit > 0):
        nGui.destroy()
        return
    
#How to openfile    
def nOpen():
    ftypes = [('Python files', '*.py'), ('All files', '*')]
    dlg = tkFileDialog.Open(filetypes = ftypes)
    fl = dlg.show()

    if fl != '':
        text = readFile(fl)
        txt.insert(END, text)


def readFile(self, filename):
    f = open(filename, "r")
    text = f.read()
    return text




nGui = tk.Tk()
ment = tk.StringVar()#to use as string variable class for textvaraible field in Entry command

#setting default color to canvas
nGui.configure(background='white')

nGui.geometry("1280x720")
nGui.title("Ground_Response_Application")



#label widget creation
mlabel1 = tk.Label(text = 'Input',fg = 'black',bg = 'white',font=("Comic Sans ms", 16))#place centre(default)
mlabel1.grid(row=0,column=0,sticky='W')
mlabel2 = tk.Label(text = 'Input_Screen',fg = 'white',bg = 'gray',font=("Helvetica", 16))#place centre(default)
mlabel2.grid(row=1,column=0)


#button widget creation
nbutton = ttk.Button(text='OK',command = nhello)
nbutton.grid(row=3,column=0)



#entry widget creation
nEntry = tk.Entry(bd = 5,textvariable=ment)
nEntry.grid(row = 5,column = 0)

# Menu construction
menubar=tk.Menu(nGui)
#filemenu
filemenu= tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command = nNew)
filemenu.add_command(label="Open",command = nOpen)
filemenu.add_command(label="SaveAs")
filemenu.add_command(label="Close",command = mQuit)
menubar.add_cascade(label='File',menu=filemenu)

#help menu
helpmenu= tk.Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About",command = mAbout)
menubar.add_cascade(label='Help',menu=helpmenu)


nGui.config(menu = menubar)

#radio button
radio_1=tk.Radiobutton(nGui,text='Option 1',value = 1,variable = 1,fg = 'black',bg = '#E91E63')
radio_1.grid(row = 7 , column = 0)
radio_2=tk.Radiobutton(nGui,text='Option 2',value = 2,variable = 2,fg = 'black',bg = '#E91E63')
radio_2.grid(row = 8 , column = 0)
radio_3=tk.Radiobutton(nGui,text='Option 3',value = 3,variable = 3,fg = 'black',bg = '#E91E63')
radio_3.grid(row = 9 , column = 0)

#canvas
canvas_1 = tk.Canvas(nGui,height = 300,width = 300,bg = 'white')
canvas_1.grid(row = 11 , column = 0)

#this is create on canvas
#canvas_1.create_line(0,0,300,300)
nGui.mainloop()
