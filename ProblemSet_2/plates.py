def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length(s)
    sign_detection



# Check if the string Length of the input is in the allowed range from between 2 to 6
    def length(plate_length):
        if 2 <= len(plate_length) <= 6:
            return True
        else:
            exit("Invalid")

    # Checks for signs, spaces and punctuation in the input
    def sign_detection(plate_input):
        for signs in plate_input:
            if " " or "."
