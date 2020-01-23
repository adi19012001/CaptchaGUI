# fibonnaci series
# we can also make the default values of a and b as 0 and 1 simantenously
#a=0
#b=1
a=int(input("\nEnter the first term of fibonnaci series"))
b=int(input("\nEnter the second term of the fibonacci series"))
n=int(input("\nEnter the number of terms into fibonnaci series"))

print(a,b,end=" ")

while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1


