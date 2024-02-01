# "All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” CHECK
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # filtering length between 2 and 6 characters
    if 2 <= len(s) <= 6:
        print("länge pass")
    plate_split = seperator(s)
    plate_split = plate_raw.split(" ")

# Seperates first letter block and number block
def seperator(plate_raw):
    for letters in plate_raw:
        l = letters.isalpha()
        if l == False:
            plate_raw = plate_raw.replace(str(letters)," " + str(letters), 1)
            #print(plate_raw)
            break
    return plate_raw


    for numbers in s:
        n = numbers.isdigit()
        print(n)



main()
