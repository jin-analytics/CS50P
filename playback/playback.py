# Ask for input and define it with variable "sentence"
sentence=input()

# Use a string method to add "..." between white space
# String Method .replace is chosen -> replace('old','new', [optional count])
sentence = sentence.replace(' ','...')

# Print the new sentence
print(f"{sentence}")
