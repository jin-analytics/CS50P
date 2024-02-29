from test_bank import value

#def main():
#    greeting = str(input("Greeting: "))
#    test_hello(greeting)

#def test_hello():
#    assert value() == 100
#______________________________________

def test_gives_100_for_hello(greeting = "hello"):
    #greeting = ("hello")
    val = value(greeting)
    assert val == 100


#if __name__ == "__main__":
#    main()
