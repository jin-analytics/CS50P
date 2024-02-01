def main():
    tweet = input("Input: ")
    omitter(tweet)
   # print("Output")

def omitter(twt):
    for vowels in twt:
        print("1",vowels)
        vowels += vowels
        print("2",vowels)



# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()
