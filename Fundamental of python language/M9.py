#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
n3 = int(input("Enter third number :"))

if n1==n2 or n2 == n3 or n3 == n1:
    sum=0
    print(f"{sum}")
else:
    sum = n1+n2+n3
    print(f"sum of {n1} + {n2} +{n3} = {sum}")