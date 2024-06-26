# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Input string
input_string = "The weather is not that poor today."

# Initialize variables to track positions of 'not' and 'poor'
index_not = -1
index_poor = -1

# Find the position of 'not'
for i in range(len(input_string) - 2):
    if input_string[i:i+3] == 'not':
        index_not = i
        break

# Find the position of 'poor'
for i in range(len(input_string) - 3):
    if input_string[i:i+4] == 'poor':
        index_poor = i
        break

# Check if 'not' is before 'poor' and they are found
if index_not != -1 and index_poor != -1 and index_not < index_poor:
    # Construct the new string
    result = input_string[:index_not] + 'good' + input_string[index_poor+4:]
else:
    # If the conditions are not met, return the original string
    result = input_string

# Output the result
print("Resulting string:", result)
