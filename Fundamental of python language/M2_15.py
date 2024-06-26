# Write a Python program to count occurrences of a substring in a string.
# Input string and substring
string = "hello hello hell"
substring = "hell"

# Initialize counter for occurrences
count = 0

# Lengths of the string and the substring
string_length = len(string)
substring_length = len(substring)

# Iterate over the string
for i in range(string_length - substring_length + 1):
    # Check if the substring matches the current slice of the string
    if string[i:i + substring_length] == substring:
        count += 1

# Output the number of occurrences
print("The substring '{}' occurs {} times in the string.".format(substring, count))
