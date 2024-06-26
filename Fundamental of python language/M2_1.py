#Write a Python program to check if a number is positive, negative or zero.
n1= int(input("Enter a number :"))
if n1 > 0:
    print(f"{n1} Number is positive")
elif n1 < 0:
    print(f"{n1} Number is Negative")
else:
    print(f"{n1} Number is Zero")