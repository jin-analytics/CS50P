from bank import value

def test_gives_100_for_hello():
    greeting = ("hello")
    val = value(greeting)
    assert val == 0
    greeting = ("Hello")
    val = value(greeting)
    assert val == 0
    greeting = ("Hello,")
    val = value(greeting)
    assert val == 0

def test_gives_20_for_h_at_beginning():
    greeting = ("Hello,")
    val = value(greeting)
    assert val == 0
