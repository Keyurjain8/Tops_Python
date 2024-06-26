# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Input strings
string1 = "hello"
string2 = "world"

# Ensure strings have at least two characters
if len(string1) < 2 or len(string2) < 2:
    print("Both strings must have at least two characters.")
else:
    # Swap the first two characters of each string
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]

    # Combine the new strings with a space
    result = new_string1 + " " + new_string2

    # Output the result
    print("Result:", result)
