def main():
    tweet = input("Input: ")
    # print out what the function gives as return, in this case "twt"
    print("Output:", omitter(tweet))

# funtion which removes vowels (Vokale)
def omitter(twt):
    # Checks each letter in "twt" string
    for vowels in twt:
        # checks if any vowel is inside the "twt" and removes it
        match vowels:
            case "a" | "e" | "i" | "o" | "u":
                twt = twt.replace(vowels,"")
    return twt


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
