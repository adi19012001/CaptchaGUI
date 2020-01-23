#practicing the use of conditional staements
#calculator using python language
#I will do this using conditional statements if, elif statemets

b=float(input("Enter the value of first number"))
c=float(input("\nEnter the value of second number"))
print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Square \n6. Cube \n7. Square root \n8. Cube Root")
a=int(input("Enter your choice"))
if a==1:
    exp=b+c
    print("\nThe sum of two numbers is= ", exp)
elif a==2:
    exp=b-c
    print("\nThe Subtaction of two numbers is= ", exp)
elif a==3:
    exp=b*c
    print("\nThe multiplication of two numbers is= ", exp)
elif a==4:
    exp=b/c
    print("\nThe division of two numbers is= ", exp)
elif a==5:
    exp=b*b
    exp2=c*c
    s=int(input("First number or second no"))
    if s==1:
        print("\nThe square of the first number is= ",exp)
    else:
        print("\nThe square of the second number is= ",exp2)
elif a==6:
    exp=b**3
    exp2=c**3
    q=int(input("First number or second no"))
    if q==1:
        print("\nThe square of the first number is= ",exp)
    else:
        print("\nThe square of the second number is= ",exp2)
elif a==7:
    exp=pow(b,0.5)
    exp2=pow(c,0.5)
    w=int(input("First number or second no"))
    if w==1:
        print("\nThe square of the first number is= ",exp)
    else:
        print("\nThe square or the second number is= ",exp2)
else :
    exp=pow(b,(1/3))
    exp2=pow(c,(1/3))
    e=int(input("First number or second no"))
    if e==1:
        print("\nThe square of the first number is= ",exp)
    else:
        print("\nThe square of the second number is= ",exp2)

    
