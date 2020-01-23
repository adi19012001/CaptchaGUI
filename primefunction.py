# function to find whether the number is prime or not

def prime(n):
    if n>1:
        for i in range(2,n):
            if(n%i == 0):
                print("The number is not a prime number")
                print(i, "times ", n//i, "is ", n)
                break
            else:
                print("Number", n," enetered is prime")
    else:
        print("The number",n," entered is not prime")

x=int(input("Enter the number= "))
prime(x)
        
                
