# Create a function called convert
def convert(face):

    #hello = input()
    print(face)
    # Replace the smiley ":)" and ":("
    # Slightly Smiling Faces - Unicode: "U+1F642" - In Python: "\U0001F642"
    # Slightly Frowning Faces - Unicode: "U+1F641" - In Python: "\U0001F641"
    hello = hello.replace(f":)","\U0001F642").replace(f":(","\U0001F641")
    print(hello)

    # print out smiley with converted
face=input() #1 Input "Hello :)"
convert(face) #2 Gives "Hello :)" to function convert()


