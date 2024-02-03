import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

# Check if the string Length of the input is in the allowed range from between 2 to 6
    if length(s) == False:
        return False

# Checks for periods, spaces and punctuation in the input, if nothing found - return True
    if sign_detection(s) == False:
        return False

# Checks for numbers in the input - if no number detected, function returns True else the proove of validation continues
    if number_detection(s) == False:
        exit(True)


# If no functions used exit(), then the plate input is valid and return a "True"
    return True



# Check if the string Length of the input is in the allowed range from between 2 to 6 and if in range - return False
def length(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        return False

# Checks for periods, spaces and punctuation in the input, if nothing found - return True
def sign_detection(plate_input):
    for signs in plate_input:
        # detects: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        # isspace() detects: characters space and tab
        print(signs)
        if signs in "!#$%&' ()*+,-./:;<=>?@[\]^_`{|}~" or signs.isspace() == True:
            #print("detected")
            return False
            break
    else:
        return True


main()
