import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

# Check if the string Length of the input is in the allowed range from between 2 to 6
    if length(s) == False: # Function #1
        return False

# Checks for periods, spaces and punctuation in the input, if nothing found - return True
    if sign_detection(s) == False: # Function #2
        return False

# Checks for numbers in the input - if no number detected, function returns True else the proove of validation continues
    if number_detection(s) == False: # Function #3
        return True
# Splits the plate input to a letter (#1) and number (#2) block to continue the proove of validation
    else:
        plate_split = splitter(s) # Function #4
        #print(plate_split)

# checks if there is a "0" as first number in the number block, returns if not - True
    if first_number_zero(plate_split) == False: # Function #5
        return False

# check if the length of the letter block is atleast 2 character, and then - returns True
    if letterblock_atleast_two_char(plate_split) == False: # Function #6
        return False

# Checks if there are only numbers in the number block (#2)
    if first_number_zero(plate_split) == False: # Function #6
        return False

# If no functions used exit(), then the plate input is valid and return a "True"
    else:
        return True



#_______________________________________________Function #1_____________________________________________________________
# Check if the string Length of the input is in the allowed range from between 2 to 6 and if in range - return False
def length(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        return False

#_______________________________________________Function #2_____________________________________________________________
# Checks for periods, spaces and punctuation in the input, if nothing found - return True
def sign_detection(plate_input):
    for signs in plate_input:
        # detects: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ in the input
        # isspace() detects: characters space and tab
        if signs in "!#$%&' ()*+,-./:;<=>?@[\]^_`{|}~" or signs.isspace() == True:
            #print("detected")
            return False
            break
    else:
        return True

#_______________________________________________Function #3_____________________________________________________________
# Checks for numbers in the input - if a number is detected, function returns True... else returns False
def number_detection(plate_input):
    for numbers in plate_input:
        if numbers.isdigit() == True:
            return True
            break
    else:
        return False

#_______________________________________________Function #4_____________________________________________________________
# Seperates first letter block and number block and returns variable "plate_split"
def splitter(plate_input):
    # checks each character from the plate_input
    for number in plate_input:
        # gives "n" a boolean type
        n = number.isdigit()
        # when the first number is detected, then will be a whitespace added in front of it
        if n == True:
            plate_input = plate_input.replace(str(number)," " + str(number), 1)
            plate_split = plate_input.split(" ")
            return plate_split

#_______________________________________________Function #5_____________________________________________________________
# checks if there is a "0" as first number in the number block, returns if not - returns True
def first_number_zero(plate_split):
    number_block = plate_split[1]
    if number_block[0] == "0":
        return False
    else:
        return True

#_______________________________________________Function #6_____________________________________________________________
# check if the length of the letter block is atleast 2 character, and then - returns True
def letterblock_atleast_two_char(plate_split):
    letter_block = plate_split[0]
    if  len(letter_block) >= 2:
        return True
    else:
        return False

#_______________________________________________Function #7_____________________________________________________________
# Checks if there are only numbers in the number block (#2), if yes - returns True
def numberblock_only_number(plate_split):
        number_block = plate_split[1]
        print("bool",number_block.isdigit())
        if number_block.isdigit() != True:
            return False
        else:
            return True


main()
