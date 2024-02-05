def main():
    # input will be MM/DD/YYYY
    date = get_date("What is the date? ")
    # output will be YY/MM/DD
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            date_split = input(prompt).split("/")
            # check if all inputs beside "/" are integer
            if date_split[0].isdigit() or date_split[1].isdigit() or date_split[2].isdigit() == True:
                # add 0 if MM has only one character
                if len(date_split[0]) == 1:
                    date_split[0] = date_split[0].replace(date_split[0], "0" + date_split[0])
                    print (date_split[0])
                # add 0 if DD has only one character
                if len(date_split[1]) == 1:
                    date_split[1] = date_split[1].replace(date_split[1], "0" + date_split[1])
                    print (date_split[1])
                print(date_split)

            # Split the date string wherever "/" is


            return prompt
        except ValueError:
            pass

main()
