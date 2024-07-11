from project import use_serialport
import pytest

def main():
    test_use_serialport()

def test_use_serialport():
    with pytest.raises(ConnectionError):
        sPort = "default"

if __name__ == "__main__":
    main()
