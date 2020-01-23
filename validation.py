#program to validate a phone number

a=int(input("Enter the number= "))
b=str(a)
c=len(b)
if b[0]==0:
    print("INVALID")
elif c>10:
    print("Invalid number")
else:
    print("valid")



