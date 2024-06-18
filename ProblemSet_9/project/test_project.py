import pytest



def test_serial_data():
    sPort = "/dev/cu.usbmodem101"
    Baud = 9600
    assert serial_data(sPort, Baud) == 


