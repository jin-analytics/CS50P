from numb3rs import validate

def main():
    format_only_accepts_4_numberblocks()

def format_only_accepts_4_numberblocks():
    ip = "cat"
    #ip = ip.split('.')
    #print(ip)
    assert validate(ip) == True


if __name__ == "__main__":
    main()
