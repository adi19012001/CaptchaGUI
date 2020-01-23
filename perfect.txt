# function to find whether the number is perfect or not

def perfect(n):
    c=n//2
    s=0
    for i in range(1,c+1):
        if(n%i)==0:
            s=s+i

    if s==n:
        print("The number is perfect")
    else:
        print("The number is not perfect")

x=int(input("Enter the number to check= "))
perfect(x)


