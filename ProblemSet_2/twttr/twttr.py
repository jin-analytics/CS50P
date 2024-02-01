def main():
    tweet = input("Input: ")
    omitter(tweet)
   # print("Output")

def omitter(twt):
    for vowels in twt:
        match twt:
            case "a" | "e" | "i" | "o" | "u":
                print("case",vowels)
                twt = twt.replace(vowels,"")
                print("case2",twt)
    print("case3",twt)




# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
