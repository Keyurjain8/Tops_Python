#Write python program that swap two number with temp variable andwithout temp variable. Write a Python program
n1=10
n2=20
temp = 0
print(f"Before Swap the value of n1 is {n1}")
print(f"Before Swap the value of n2 is {n2}")

print(" Swap Using third variable ")
temp = n1
n1 = n2 
n2 = temp
print(f"After Swap the value of n1 is {n1}")
print(f"After Swap the value of n2 is {n2}")


print("#########################################")
print("Without using third variable ")
n1,n2 =n2,n1
print(f"After Swap without third variable the value of n1 is {n1}")
print(f"After Swap without third variable the value of n2 is  {n2}")


