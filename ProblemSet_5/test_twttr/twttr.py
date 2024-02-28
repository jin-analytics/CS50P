def main():
    tweet = str(input("Input: "))
    print("Output:", shorten(tweet))

# checks if any vowel is inside the "tweet" and removes it, then gives it ("word") back
#def shorten(word = "twitter123#"):
def shorten(word):
    for _ in word:
        match _: #vowels
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            #case "a" | "e" | "o" | "u" | "A" | "E" | "I" | "O" | "U": # modified without i
                word = word.replace(_,"")
            #case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                #word = word.replace(_,"")
        if _.isalpha() == False:
             #print(_.isalpha())
             word = word.replace(_,"")

    return word

# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
