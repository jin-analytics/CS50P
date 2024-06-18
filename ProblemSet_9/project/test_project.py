import pytest
from project import serial_data

def main():
    test_serial_data()


def test_serial_data():
    sPort = "/dev/cu.usbmodem101_???"
    Baud = 9600
    with pytest.raises(ModuleNotFoundError):
        serial_data(sPort, Baud)

if __name__ == "__main__":
    main()
