# Get input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
print(question[0])

# use match function for different input cases
match question:
    # if the input is "42", "forty two" or "forty-two", then go into this case and print "yes"
    case "42" | "forty two" | "forty-two":
        print ("yes")
    # if the input start with a " ", then go into this case
   # case question[0] == " ":
    #    question = question.replace(" ","")
    #    test = question
    #    print (test)
