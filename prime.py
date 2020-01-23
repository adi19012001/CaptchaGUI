# program to find whether the entered number is prime or not

n=int(input("\nEnter the number= "))

if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not a prime number")
            print(i,"times",n//i,"is",n)
            break
        else:
            print(n,"is a prime number")
else:
    print("Not a prime number")
