import re

month = {
    "January":  1,
    "February": 2,
    "March":    3,
    "April":    4,
    "May":      5,
    "June":     6,
    "July":     7,
    "August":   8,
    "September":9,
    "October":  10,
    "November": 11,
    "December": 12
}


def main():
    # input will be MM/DD/YYYY
    print(get_date("Date: ")) # output will be YY/MM/DD


def get_date(prompt):
    while True:
        try:
            date = input(prompt)

            # First will be checked if its "September 9, 1999" or "9/9/1999", because these are the only valid inputs
            if sign_detection_comma(date) == True:
                # Split the date string wherever "/"
                date_split = re.split('[ ,]', date)
                # remove every whitespace
                date_split = remove_spaces(date_split)
                # check if the month is fully written, for example: "September 9, 1999"
                if date_split[0].isalpha() and date_split[1].isdigit() and date_split[2].isdigit() == True:
                    # changes the fully written month in entree data_split[0] to the number from the list "month"
                    for month_name in month:
                        if month_name == date_split[0]:
                            date_split[0] = str(month[month_name])
                            if int(date_split[0]) <= 12 and int(date_split[1]) <= 31: # Checks if the month and day is legit:
                                outdated = date_convert(date_split)
                                return outdated

            # First will be checked if its "September 9, 1999" or "9/9/1999", because these are the only valid inputs
            if sign_detection_slash(date) == True:
                # Split the date string wherever "/", " " is
                date_split = re.split('[ /]', date)
                date_split = remove_spaces(date_split)
                # check if all inputs beside "/" are numbers
                if date_split[0].isdigit() and date_split[1].isdigit() and date_split[2].isdigit() == True:
                    if int(date_split[0]) <= 12 and int(date_split[1]) <= 31: # Checks if the month and day is legit
                        outdated = date_convert(date_split)
                        return outdated

        except ValueError:
            pass
        except IndexError:
            pass

# converts the date_split variable to YYYY-MM-DD
def date_convert(date_split):
    # add 0 if MM has only one character
    if len(date_split[0]) == 1:
        date_split[0] = date_split[0].replace(date_split[0], "0" + date_split[0])
    # add 0 if DD has only one character
    if len(date_split[1]) == 1:
        date_split[1] = date_split[1].replace(date_split[1], "0" + date_split[1])
    # change format MM.DD.YYYY to YYYY.MM.DD
    date_split[0], date_split[1] = date_split[1], date_split[0] # Changes MM #1 to MM #2 and DD #2 to DD #1
    date_split[0], date_split[2] = date_split[2], date_split[0] # Changes DD #1 to DD #3 and YYYY #3 to YYYY #1
    # joins the list to a string joined wir "-"
    date_split = '-'.join(date_split)
    return date_split

# Checks for ","
def sign_detection_comma(d):
    for signs in d:
        if signs  == ",":
            #print("detected")
            return True

# Checks for "/"
def sign_detection_slash(d):
    for signs in d:
        if signs  == "/":
            return True

# Create a new list without the ("")-tuple
def remove_spaces(d):
    tuple_to_remove = ("")
    new_list = []
    for item in d:
        if item != tuple_to_remove:
            new_list.append(item)
            # Update the original list with the modified list
            d = new_list
    return d

main()
