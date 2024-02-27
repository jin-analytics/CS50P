from twttr import shorten

def main():
    tweet = input("Input: ")
    #print("Output:", shorten(tweet))
    test_lower(tweet)

# compare the selected vowes with the one removed
def test_lower(tw):
    assert shorten(tw) == 


#def test_upper():


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet, if we call main() inside there
if __name__ == "__main__":
    main()

