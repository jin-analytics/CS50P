# Get input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# use match function for different input cases
match question:

    # if the input is "42", "forty two" or "forty-two", then go into this case and print "yes"
    case "42" | "forty two" | "forty-two":
        print ("yes")

    # if the input start with a " ", then go into this case
    case _:
        # All letters of question will be lowered
        question = question.lower()

        # if the input start with a " ", then go into this case
        if question[0] == " ":

            # Replace all " " with no spaces
            question = question.replace(" ","")
            if question == "42"
            print ("yes")

        # If the input "Forty Two" had caps on, then they are lowered now and can be detected
        elif question == "forty two":
        print ("yes")
        # If still no match, then print "no"
        else:
        print ("no")

