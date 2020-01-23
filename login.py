# login page for project

import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2,rowspan=1)
        self.pack()

    def _login_btn_clicked(self):
        # accessing values from the class
        username = self.entry_username.get()
        password = self.entry_password.get()

        # default user assigning

        if username == "Aditya" and password == "12345":
            tm.showinfo("Login info", "Verify Captcha")
            import captchagui
        else:
            tm.showerror("Login error", "Incorrect username")

root = tk.Tk()
root.title("Login")
root.geometry("400x200")
w = tk.Label(root,text="  Log In Page / Registered User : \n \n ")
w.config(font=(18))
w.pack()
lf = LoginFrame(root)
root.mainloop()
