# Write a Python function to reverses a string if its length is a multiple of 4.
# Input string
input_string = input("Enter your string :")

# Lambda function to reverse the string if its length is a multiple of 4
reverse_if_multiple_of_4 = (lambda s: s[::-1] if len(s) % 4 == 0 else s)

# Apply the lambda function to the input string
result = reverse_if_multiple_of_4(input_string)

# Output the result
print(result)

