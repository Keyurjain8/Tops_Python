# Write a Python function that takes a list of words and returns the length of the longest one.

# List of words
words = ["apple", "banana", "cherry", "blueberry", "grape"]
print(words)
longest_word = max(words, key=lambda word: len(word))
print(longest_word)

# Using a lambda function with max to find the length of the longest word
length_of_longest_word = len(max(words, key=lambda word: len(word)))

# Output the length of the longest word
print(length_of_longest_word)

