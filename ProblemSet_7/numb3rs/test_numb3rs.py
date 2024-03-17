from numb3rs import validate

def main():
    test_format_in_dot_decimal()

def test_format_in_dot_decimal():
    #ip = ip.split('.')
    #print(ip)
    assert validate("cat") == True


if __name__ == "__main__":
    main()
