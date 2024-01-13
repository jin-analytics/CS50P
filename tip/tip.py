def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # string input which has to remove the "$"
    d=d.replace('$','')
    # string input which has to be converted to a float number
    d=float(d)
    # return the value "d" which is a float number now
    return d


def percent_to_float(p):
    # string input which has to remove the "%"
    p=p.replace('%','')
    # string input which has to be converted to a float number and divided to
    p=float(p)/100
    # return the value "d" which is a float number now
    return p


main()

