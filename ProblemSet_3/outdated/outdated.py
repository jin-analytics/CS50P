def main():
    date = get_date("What is the date? ")
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            return (int(input(prompt)))
        except ValueError:
            pass

main()
