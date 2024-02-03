def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length(s)
    sign_detection(s)



# Check if the string Length of the input is in the allowed range from between 2 to 6
def length(plate_length):
    print(plate_length)
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        return False

# Checks for periods, spaces and punctuation in the input
def sign_detection(plate_input):
    for signs in plate_input:
        # punctuation() detects: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        signs = signs.punctuation()
        # whitespace detects: characters space, tab, linefeed, return, formfeed, and vertical tab
        signs = signs.whitespace()
        if signs != True:
            return True
        else:
            return False


main()
