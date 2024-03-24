from um import count

def test_um_with_surroundings():
    assert count("test um, returns um 2") == 2

def test_um_included_in_words():
    assert count("test yummy, returns um 1") == 1

def test_um_in_uppercase():
    assert count("test UM, returns Um 2") == 2
