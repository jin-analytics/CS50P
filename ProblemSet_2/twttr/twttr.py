def main():
    tweet = input("Input: ")
    # print out what the function gives as return, in this case "twt"
    print("Output:", omitter(tweet))

def omitter(twt):
    for vowels in twt:
        match vowels:
            case "a" | "e" | "i" | "o" | "u":
                twt = twt.replace(vowels,"")
    return twt


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
