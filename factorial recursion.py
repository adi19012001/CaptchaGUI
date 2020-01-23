# factorial program

a=int(input("\nEnter the number for factorial of the number= "))
def factorial(a):
      return 1 if(a==0 or a==1) else a*factorial(a-1)
print("\nFactorial of the given number is= ", factorial(a))
