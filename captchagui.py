# -*- coding: utf-8 -*-

# captcha page for project

import random
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import sqlite3


class CaptchaFrame(Frame):
    def __init__(self, master):
        ops=['-','+','*']             # ops is a list with simple arthemetics opeartions
        self.a=random.randint(0,10)                   # random is a  function which will select one operation from 0,10 and ops
        self.b=random.randint(0,10)
        self.operation=random.choice(ops)
        super().__init__(master)
        # captcha
        c=[self.a,self.operation,self.b]
        
        self.label_captcha = Label(self, text=c)
        self.entry_captcha = Entry(self)

        self.label_captcha.grid(row=0, sticky=E)
        self.entry_captcha.grid(row=0, column=1)

        self.robot = Checkbutton(self, text="I am not a robot")
        self.robot.grid(columnspan=2)

        self.button = Button(self, text="Confirm", command=self.buttonclicked)
        self.button.grid(columnspan=2)
        
        self.pack()
    
    def buttonclicked(self):
        #root.destroy()
        # print("Clicked")
        a=self.a
        b=self.b
        operation=self.operation
        q = int(self.entry_captcha.get())
        r=eval(str(a)+operation+str(b))         # eval() will evaluate the value of the arthemetic opeartion
        
        conn=sqlite3.connect("project.db")
        #conn.execute("create table captcha1(A,Sign,B,Value);")
        conn.execute("insert into captcha1(A,Sign,B,Value)values(?,?,?,?)",(a,operation,b,r))
        conn.commit()
        
        if q == r:
            tm.showinfo("Captcha info", "Verfied")
            import programs
            
        else:
            tm.showerror("Captcha error", "Please enter valid captcha")
            import captchagui
            
        
        #root.title("Aditya Kumar Singh")
root = tk.Tk()
root.title("Captcha")
w = tk.Label(root,text="Verify Captcha")
w.pack()
root.geometry("250x100")
lf = CaptchaFrame(root)
root.mainloop()
