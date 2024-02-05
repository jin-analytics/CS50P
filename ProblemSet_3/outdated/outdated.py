def main():
    # input will be MM/DD/YYYY
    date = get_date("What is the date? ")
    # output will be YY/MM/DD
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            # Split the date string wherever "/" is
            date_split = input(prompt).split("/")
            # check if all inputs beside "/" are integer
            if date_split[0].isdigit() and date_split[1].isdigit() and date_split[2].isdigit() == True:
                # add 0 if MM has only one character
                if len(date_split[0]) == 1:
                    date_split[0] = date_split[0].replace(date_split[0], "0" + date_split[0])
                    print (date_split[0])
                # add 0 if DD has only one character
                if len(date_split[1]) == 1:
                    date_split[1] = date_split[1].replace(date_split[1], "0" + date_split[1])
                    print (date_split[1])
                # change format MM.DD.YYYY to YYYY.MM.DD
                myorder = [3, 2, 1]
                date_split = [date_split[i] for i in myorder]
                print(date_split)

                return date_split
        except ValueError:
            pass
        except IndexError:
            pass

main()
