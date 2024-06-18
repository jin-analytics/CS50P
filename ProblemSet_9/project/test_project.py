from project import serial_data
import pytest

def main():
    test_serial_data()


def test_serial_data():
    sPort = "/dev/cu.usbmodem101"
    Baud = 9600
    with pytest.raises(ImportError):
        serial_data(sPort, Baud)

if __name__ == "__main__":
    main()
