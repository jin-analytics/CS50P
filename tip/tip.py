def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # string input which has to be converted to a float number
    dollars = d
    # string input which has to replace the "$"
    dollars=dollars.replace('$','')
    # string input which has to be converted to a float number
    dollars=float(dollars)
    print (dollars)
    d=dollars


def percent_to_float(p):
    print(p)
    percent=p
    percent=float(p)
    percent=percent/100
    print (percent)
    p=percent



main()

