# Signup page for project

import sys
import time
import tkinter as tk
from time import sleep
from tkinter import *
import tkinter.messagebox as tm
import sqlite3


class SignupFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_name=Label(self, text="Name")
        self.label_username=Label(self, text="Username")
        self.label_password=Label(self, text="Password")
        self.label_cpassword=Label(self, text="Confirm Password")
        self.label_email = Label(self, text="E-mail ID")
        self.label_phone=Label(self, text="Phone Number")

        self.entry_name=Entry(self)
        self.entry_username=Entry(self)
        self.entry_password=Entry(self, show="*")
        self.entry_cpassword=Entry(self, show="*")
        self.entry_email=Entry(self)
        self.entry_phone=Entry(self)

        self.label_name.grid(row=0, sticky=E)
        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.label_cpassword.grid(row=3, sticky=E)
        self.label_email.grid(row=4, sticky=E)
        self.label_phone.grid(row=5, sticky=E)

        self.entry_name.grid(row=0, column=1)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)
        self.entry_cpassword.grid(row=3, column=1)
        self.entry_email.grid(row=4, column=1)
        self.entry_phone.grid(row=5, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Sign Up", command=self.newaccount)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def newaccount(self):
        # validations of all enteries
        name=self.entry_name.get()
        username=self.entry_username.get()
        password=self.entry_password.get()
        cpassword=self.entry_cpassword.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        
        conn=sqlite3.connect("project.db")
        conn.execute("insert into new_form(Name,Username,Password,Email_Id,Phone)values(?,?,?,?,?)",(name,username,password,email,phone))
        conn.commit()
        # validating password entry
        if password != cpassword:
            tm.showerror("Password info", "Password don't match")
        else:
            print()

        # validating email
        if "@" in email and "." in email:
            print()
        else:
            tm.showerror("Email info", "Invalid Email")

        # validating phone number
        w=len(phone)
        if w>10:
            tm.showerror("Phone info", "Invalid Phone")
        else:
            print()
        tm.showinfo("Successful Login", "You have successfully filled the form\n\t   Redirecting..")
        
        import login

root = tk.Tk()
#root.config(bg="white")
w = tk.Label(root,text="  Sign Up Page  /  New User  : \n \n ")
w.config(font=(16))
w.pack()
root.title("SignUP")
root.geometry("300x300")
lf = SignupFrame(root)
root.mainloop()
