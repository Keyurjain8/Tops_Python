#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it unchanged.
# Input string
input_string = "play"

# Check the length of the string
if len(input_string) >= 3:
    # Check if the string ends with 'ing'
    if input_string[-3:] == "ing":
        # Add 'ly' at the end
        new_string = input_string + "ly"
    else:
        # Add 'ing' at the end
        new_string = input_string + "ing"
else:
    # If the length is less than 3, leave it unchanged
    new_string = input_string

# Output the result
print("Modified string:", new_string)
