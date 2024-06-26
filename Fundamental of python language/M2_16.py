# Write a Python program to count the occurrences of each word in a given sentence
# Input sentence
sentence = "Hello, world! Hello, how are you? Are you fine, world?"

# Convert the sentence to lowercase to handle case insensitivity
sentence = sentence.lower()

# Initialize an empty dictionary to store word counts
word_count = {}

# Initialize an empty string to accumulate characters for the current word
current_word = ""

# List of characters that are considered part of a word (letters and digits)
word_characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Iterate over each character in the sentence
for char in sentence:
    if char in word_characters:
        # If the character is part of a word, add it to the current word
        current_word += char
    else:
        # If the character is not part of a word, finalize the current word
        if current_word:
            # If the word is in the dictionary, increment its count
            if current_word in word_count:
                word_count[current_word] += 1
            else:
                # Otherwise, add the word to the dictionary with a count of 1
                word_count[current_word] = 1
            # Reset the current word
            current_word = ""

# After the loop, check if there's a word left to add
if current_word:
    if current_word in word_count:
        word_count[current_word] += 1
    else:
        word_count[current_word] = 1

# Print the word counts
for word in word_count:
    print(f"'{word}': {word_count[word]} times")
