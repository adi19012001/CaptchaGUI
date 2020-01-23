#Tribonnaci Series
# According to tribonnaci series the next term is the sum of previous three terms
# and hence the first three terms is 0,1,1

#a=0
#b=1
#c=1

a=int(input("\nEnter the value of first term of tribonnaci series"))
b=int(input("\nEnter the value of first term of tribonnaci series"))
c=int(input("\nEnter the value of first term of tribonnaci series"))
n=int(input("\nEnter the number of terms into the tribonnaci series"))

print(a,b,c,end=" ")

while(n-3):
    d=a+b+c
    a=b
    b=c
    c=d
    print(d,end=" ")
    n=n-1
