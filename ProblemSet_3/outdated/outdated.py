def main():
    date = get_date("What's the date?")
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            return (int(prompt))
        except ValueError:
            pass

main()
