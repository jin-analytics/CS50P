from bank import value

def test_gives_100_for_hello():
    greeting = ("hello")
    assert value(greeting) == 0
    greeting = ("Hello")
    assert value(greeting) == 0
    greeting = ("Hello,")
    assert value(greeting) == 0

def test_gives_20_for_h_at_beginning():
    greeting = ("H")
    assert value(greeting[1]) == 0
