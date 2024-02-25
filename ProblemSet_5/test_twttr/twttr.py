def main():
    tweet = input("Input: ")
    print("Output:", shorten(tweet))

# checks if any vowel is inside the "tweet" and removes it, then gives it ("word") back
def shorten(word):
    for vowels in word:
        match vowels:
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                word = word.replace(vowels,"")
    return word

# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
