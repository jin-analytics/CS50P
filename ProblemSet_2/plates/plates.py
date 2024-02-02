# "All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” CHECK
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
# vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.” CHECK
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # filtering length between 2 and 6 characters, if so - return True
    length(s)

    # seperates the plate string from main() to a letter block (#1) and a number block (#2) through the variable "plate_split"
    plate_split = seperator(s)

    # Looks up if there is a letter in the number block via function "plate_order", if not - returns True
    plate_order(plate_split)

    # check if there is a "0" as the first number in Block #2, if not - returns True
    plate_order_zero(plate_split)

    # checks if there is a sign in the first list entree of "plate_split"
    sign_alarm_letter(plate_split)

    # checks if there is a sign in the second list entree of "plate_split"
    sign_alarm_number(plate_split)

    # checks if the letter block (#1) has atleast two characters
    length_letter(plate_split)


    print(length(s))
    print(plate_order(plate_split))
    print(plate_order_zero(plate_split))
    print(sign_alarm_letter(plate_split))
    print(sign_alarm_number(plate_split))
    print(length_letter(plate_split))

    print(len(plate_split))
    if len(plate_split) == 2:
        if (
        length(s) == True and
        length_letter(plate_split) == True and
        sign_alarm_number(plate_split) == True and
        sign_alarm_letter(plate_split) == True and
        plate_order_zero(plate_split) == True and
        plate_order(plate_split) == True
        ):
            return True

    if len(plate_split) == 1:
        if (
        length(s) == True and
        length_letter(plate_split) == None and
        sign_alarm_number(plate_split) == True and
        sign_alarm_letter(plate_split) == True and
        plate_order_zero(plate_split) == None and
        plate_order(plate_split) == None
        ):
            return True
    else:
        return False



# check if the length of the plate is between [2;6]
def length(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True
    else:
        exit("Invalid")

# Seperates first letter block and number block and returns variable "plate_split"
def seperator(plate_raw):
    plate_split = plate_raw.split()
    plate_split = plate_split.append("")
    print(plate_split)
    for letters in plate_raw:

        l = letters.isalpha()
        if l == False:
            plate_raw = plate_raw.replace(str(letters)," " + str(letters), 1)
            plate_split = plate_raw.split(" ")
            break
    return plate_split

# Checks if there are only numbers in the number block (#2) and returns True
def plate_order(split):
    test = split[1]
    if test.isdigit() == True:
        return True

# checks if there is a "0" as first number in the number block, returns if not - True
def plate_order_zero(split):
    number_block = split[1]
    if number_block[0] != "0":
        return True

# Checks for signs, spaces, punctuation in the number block #2
def sign_alarm_number(split):
    sign_detection = split[1]
    for signs in sign_detection:
        signs = sign_detection.isdigit()
        if signs != False:
            return True

# Checks for signs, spaces, punctuation in the letter block #1
def sign_alarm_letter(split):
    sign_detection = split[0]
    for signs in sign_detection:
        signs = sign_detection.isalpha()
        if signs != False:
            return True

# check if the length of the plate is between [2;6]
def length_letter(split):
    letter_block = split[0]
    if  len(letter_block) >= 2:
        #print(len(letter_block))
        return True


main()
