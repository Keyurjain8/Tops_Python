# Accept two numbers from the user
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

# Check if the first number is positive or negative
if num1 > 0:
    print(f"The first number ({num1}) is positive")
elif num1 < 0:
    print(f"The first number ({num1}) is negative.")
else:
    print(f"The first number ({num1}) is zero.")

# Check if the second number is positive or negative
if num2 > 0:
    print(f"The second number ({num2}) is positive.")
elif num2 < 0:
    print(f"The second number ({num2}) is negative.")
else:
    print(f"The second number ({num2}) is zero.")

#check first number is even and odd  
if num1 % 2 == 0:
    print(f"The first number ({num1}) is even.")
else:
    print(f"The first number ({num1}) is odd.")
    
#check second number is even and odd  
if num2 % 2 == 0:
    print(f"The Second number ({num2}) is even.")
else:
    print(f"The Second number ({num2}) is odd.")