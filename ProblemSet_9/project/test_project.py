from project import use_serialport
import pytest

def main():
    test_use_serialport()

def test_use_serialport():
    with pytest.raises(ConnectionError):
        use_serialport()

if __name__ == "__main__":
    main()
