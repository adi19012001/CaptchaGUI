# function to find the palindrome of the number given( non negative)

def fact(a):
    if(a>0) or a==0:
        fac=1
        for i in range(1,a+1):
          fac=fac*i
        print("Factorial of number", a, "is=", fac)
    else:
        print("The number is a negative number anf factorial is not possible")

x=int(input("Enter the number= "))
fact(x)
