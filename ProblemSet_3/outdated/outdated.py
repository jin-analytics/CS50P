def main():
    date = get_date(
    print(f"The date is {date}")

def get_date(prompt):
    while True:
        try:
            return (int(prompt))
        except ValueError:
            pass

main()
