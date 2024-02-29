from bank import value

def test_gives_100_for_hello():
    greeting = ("hello")
    assert value(greeting) == 0
    greeting = ("Hello")
    assert value(greeting) == 0
    greeting = ("Hello,")
    assert value(greeting) == 0

def test_gives_20_for_h_at_beginning():
    greeting = ("hi Sir")
    assert value(greeting[0]) == 20
    greeting = ("Hi Sir")
    assert value(greeting[0]) == 20
    greeting = ("Hi, Sir")
    assert value(greeting[0]) == 20

def test_gives_0_for_when_h_is_not_at_beginning():
    alphabet = [a:z]
    for _ in
