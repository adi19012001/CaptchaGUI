# website for python programs
import tkinter as tk

def execute():
    # executing file
    import armstrong
def write():
    # reading from file
    f=open("armstrong.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    
    #quitb=tk.Button(program,text="QUIT",fg="red",command=exit(0))
    #quitb.pack()
    
    program.mainloop()
    f.close()
    
def execute1():
    # executing file
    import calculator
def write1():
    # reading from file
    f=open("calculator.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute2():
    # executing file
    import captcha
def write2():
    # reading from file
    f=open("captcha.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute3():
    # executing file
    import e
def write3():
    # reading from file
    f=open("e","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read())
    w.pack()
    program.mainloop()
    f.close()
    
def execute4():
    # executing file
    import fact
def write4():
    # reading from file
    f=open("factorial.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute5():
    # executing file
    import fib
def write5():
    # reading from file
    f=open("fibonnaci.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute6():
    # executing file
    import file
def write6():
    # reading from file
    f=open("file.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute7():
    # executing file
    import listsum
def write7():
    # reading from file
    f=open("list.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute8():
    # executing file
    import palindrome
def write8():
    # reading from file
    f=open("palindrome.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute9():
    # executing file
    import prime
def write9():
    # reading from file
    f=open("prime.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def execute10():
    # executing file
    import validation
def write10():
    # reading from file
    f=open("validation.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
def execute11():
    # executing file
    import perfect
def write11():
    # reading from file
    f=open("perfect.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()

def execute12():
    # executing file
    import tribonnaci
def write12():
    # reading from file
    f=open("tribonnaci.txt","r")
    #print(f.read())
    program=tk.Tk()
    program.geometry()
    w1 = tk.Label(program,text="Program:")
    w1.pack()
    w = tk.Label(program,text=f.read(),bg="white")
    w.pack()
    program.mainloop()
    f.close()
    
def armstrong():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

def calculator():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute1)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write1)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

def captcha():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute2)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write2)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

def email():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute3)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write3)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

def factorial():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute4)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write4)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def fib():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute5)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write5)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def file():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute6)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write6)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def lis():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute7)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write7)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def palindrome():
    root1=tk.Tk()
    root1.geometry("320x100")
    root1.title("Choice")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute8)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write8)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def prime():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute9)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write9)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def phonevalid():
    root1=tk.Tk()
    root1.title("Choice")
    root1.geometry("320x100")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute10)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write10)
    button00.pack(side=tk.LEFT)
    root1.mainloop()


def perfect():
    root1=tk.Tk()
    root1.geometry("320x100")
    root1.title("Choice")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute11)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write11)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

def tribonnaci():
    root1=tk.Tk()
    root1.geometry("320x100")
    root1.title("Choice")
    w = tk.Label(root1,text=" Select to Continue:\n ")
    w.pack()
    frame =tk.Frame(root1)
    frame.pack()
    
    button0= tk.Button(frame,text="Execute",width=20,command=execute12)
    button0.pack(side=tk.LEFT)
    button00= tk.Button(frame,text="Veiw Program",width=20,command=write12)
    button00.pack(side=tk.LEFT)
    root1.mainloop()

root= tk.Tk()
root.title("List of the Programs")
root.geometry("400x600")
root.config(bg="black")
w = tk.Label(root,text="List of Programs  : \n \n ",bg="black",fg="white")
w.config(font=("Comic Sans Ms",20))
w.pack()

button=tk.Button(root,text="Armstrong",width=25,command=armstrong,bg="white")
button.pack()
button1=tk.Button(root,text="Calculator",width=25,command=calculator,bg="white")
button1.pack()
button2=tk.Button(root,text="Captcha",width=25,command=captcha,bg="white")
button2.pack()
button3=tk.Button(root,text="E-Mail Validation",width=25,command=email,bg="white")
button3.pack()
button4=tk.Button(root,text="Factorial",width=25,command=factorial,bg="white")
button4.pack()
button5=tk.Button(root,text="Fibonnaci",width=25,command=fib,bg="white")
button5.pack()
button6=tk.Button(root,text="File Handling",width=25,command=file,bg="white")
button6.pack()
button7=tk.Button(root,text="List",width=25,command=lis,bg="white")
button7.pack()
button8=tk.Button(root,text="Palindrome",width=25,command=palindrome,bg="white")
button8.pack()
button9=tk.Button(root,text="Prime",width=25,command=prime,bg="white")
button9.pack()
button10=tk.Button(root,text="Phone-No Validation",width=25,command=phonevalid,bg="white")
button10.pack()
button11=tk.Button(root,text="Perfect Number",width=25,command=perfect,bg="white")
button11.pack()
button12=tk.Button(root,text="Tribonnaci",width=25,command=tribonnaci,bg="white")
button12.pack()
root.mainloop()




    
    
    
    
    
    