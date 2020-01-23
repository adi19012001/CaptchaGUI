# captcha trying

import random
ops=['-','+','*','/','%','**']             # ops is a list with simple arthemetics opeartions
print("Prove you are not a robot= ")
print("You are not allowed after 3 times you will be terminated")
for i in range(0,3):
    a=random.randint(0,10)                   # random is a  function which will select one operation from 0,10 and ops
    b=random.randint(0,10)
    operation=random.choice(ops)
    print("This is your",i+1,"time of verification")
    print("\t",a,"  ",operation,"  ",b," =",)
    r=eval(str(a)+operation+str(b))     # eval() will evaluate the value of the arthemetic opeartion
    c=int(input())
    if r==c:
        print("Verified")
        break
    else:
        if i<2:
            print("Try Again:(")
        else:
            break


