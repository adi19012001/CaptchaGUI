# palindrome

a=input("\nEnter word to check whether it is palindrome or not")
b=reversed(a)
if list(a) == list(b):
    print("\nThe word is palindrome")
else:
    print("\nThe word entered is not a palindrome")
