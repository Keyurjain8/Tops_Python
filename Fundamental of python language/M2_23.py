# Write a Python function to insert a string in the middle of a string.
# Input strings
main_string = "Mr  Jain"
insert_string = "Keyur"

# Calculate the middle index of the main string
middle_index = len(main_string) // 2

# Insert the string in the middle
result_string = main_string[:middle_index] + insert_string + main_string[middle_index:]

# Print the result
print(result_string)
