def main():
    date = get_date("What is the date? ")
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            date_split = input(prompt).split("/")
            print(date_split)
            # add 0 if 
            if len(date_split[0]) == 1:
                date_split[0] = date_split[0].replace(date_split[0], "0" + date_split[0])
                print (date_split[0])

            # Split the date string wherever "/" is


            return prompt
        except ValueError:
            pass

main()
