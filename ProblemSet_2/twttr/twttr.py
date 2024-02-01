def main():
    tweet = input("Input: ")

    tweet = omitter(tweet)
    print(tweet)

def omitter(twt):
    for vowels in twt:
        match vowels:
            case "a" | "e" | "i" | "o" | "u":
                twt = twt.replace(vowels,"")
    


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
