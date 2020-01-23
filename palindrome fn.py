# function to find that the number is palindrome or not

def palindrome(a):
    b=reversed(a)
    if list(a)==list(b):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")

c=input("Enter anything to check= ")
palindrome(c)
