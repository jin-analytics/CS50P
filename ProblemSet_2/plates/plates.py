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
    print(length(s))

    # seperates the first letter block and uses the "plate_order" function
    # to see if there is a letter in the number block via function "plate_order", if not - returns True
    plate_split = seperator(s)
    print(plate_order(plate_split))
    # check if there is a "0" as the first number, if not - returns True
    print(plate_order_zero(plate_split))

    print(sign_alarm(s))



def length(plate_length):
    if 2 <= len(plate_length) <= 6:
        return True

# Seperates first letter block and number block
def seperator(plate_raw):
    for letters in plate_raw:
        l = letters.isalpha()
        if l == False:
            plate_raw = plate_raw.replace(str(letters)," " + str(letters), 1)
            plate_split = plate_raw.split(" ")
            break
    return plate_split

def plate_order(split):
    test = split[1]
    if test.isdigit() == True:
        return True

def plate_order_zero(split):
    test = split[1]
    if test[0] != "0":
        return True

def sign_alarm(split):
    letter_split = split[0]
    number_split = split[1]
    # checks if there is not a number or letter, does not - return True


    for sign_detection in number_split:
        if sign_detection.isaplha() == True:
            

    return True





main()
