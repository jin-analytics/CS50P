# Ask for input and define it with variable "sentence"
sentence=input('Write "This is CS50"\n')

# Use a string method to add "..." between white space
#sentence = sentence.split(' ')
sentence = sentence.replace(' ', '...')

# Print the new sentence
print(f"{sentence}")
