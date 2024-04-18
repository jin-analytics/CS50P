# https://docs.python.org/3/library/unittest.mock.html

from jar import Jar


def test_init():
    ...


def test_str():
    jar = Jar(size=0, deposit=5, withdraw=1)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    ...


def test_withdraw():
    ...
