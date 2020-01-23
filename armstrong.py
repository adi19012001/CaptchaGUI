#Armstrong number

sum1=0
n=int(input("\nEnter the number to check= "))
temp=n
while temp>0:
    digit=temp%10
    sum1=sum1+(digit**3)
    temp=temp/10
    
if n==sum1:
    print("\nArmstrong number")
else:
    print("\nNot armstrong number")
