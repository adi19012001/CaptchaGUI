# welcome page
import tkinter as tk

from tkinter import *

import tkinter.messagebox as tm
def new():
    import welcome
def about():
    tm.showinfo("About","The project is entirely made by ADITYA KUMAR SINGH. Used database, file handling, class to accomplish this project. Made in spyder and python 3.7.")
def ow():
    tm.showerror("Error","Anything at this stage of site cannot be opened. You need to login before opening this site. This site contains basic python programs which you can use to learn python")
    
def login():
    root.destroy()
    import login
def signup():
    root.destroy()
    import signup

      
root = tk.Tk()
menu = Menu(root)
c=Label(text="PYTHON\n",bg="black",fg="white")
c.pack()
image1=PhotoImage(file="py.gif")
q=Label(image=image1)
q.pack()
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New',command=new) 
filemenu.add_command(label='Open...',command=ow) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About',command=about) 

root.title("Welcome Page")
root.geometry("760x600")
root.config(bg="black")
w = tk.Label(root,text="WELCOME \n")
w.config(width=200,bg="black",fg="white")
w.config(font=("Arial Black", 44))
w.pack()
w1 = tk.Label(root,text="Made By-Aditya Kumar Singh \n INT213\nMathematical Based Captcha\n")
w1.config(width=200,bg="black",fg="white")
w1.config(font=("Comic Sans Ms", 14))
w1.pack()
frame =tk.Frame(root)
frame.pack()
button= tk.Button(frame,text="Login",width=20,bg="white",command=login)
button.pack(side=tk.LEFT)
button1= tk.Button(frame,text="Sign Up",width=20,bg="white",command=signup)
button1.pack(side=tk.RIGHT)
root.mainloop()
