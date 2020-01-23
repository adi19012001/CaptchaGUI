# factorial using for loop

fact=1
n=int(input("\nEnter the number for which you want to find the factorial= "))
for i in range(1,n+1):
    fact=fact*i
print(fact)
