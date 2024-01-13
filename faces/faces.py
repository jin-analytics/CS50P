# Create a function called convert
def convert():

    hello = input()
    #Slightly Smiling Faces - Unicode: "U+1F642" - In Python: "\U0001F642"
    hello = hello.replace(f":)","\U0001F642")
    #Slightly Frowning Faces - Unicode: "U+1F641" - In Python: "\U0001F641"
    #hello = hello.replace(f":(","\U0001F641")
    print(hello)

convert()


