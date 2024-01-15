# Get input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
#question = question.replace(" ","")

#if question == "42":
#    print ("yes")
#elif question == "forty-two":
#    print ("yes")
#elif question == "forty two":
#    print ("yes")
#else:
#    print ("no")

def answer():
    if question == "42":
        print ("yes")
    elif question == "forty-two":
        print ("yes")
    elif question == "forty two":
        print ("yes")
    elif question == "FoRty TwO":
        print ("yes")
    elif question == "  42  ":
        print ("yes")
    else:
        print ("no")

answer()
