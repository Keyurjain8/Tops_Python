# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2,
# return instead of the empty string.
# Input string
input_string = "Keyurjain"

# Check the length of the string
if len(input_string) < 2:
    # If the length is less than 2, print an empty string
    print("")
else:
    # Otherwise, create a new string with the first 2 and last 2 characters
    result_string = input_string[:2] + input_string[-2:]
    # Print the result
    print(result_string)
