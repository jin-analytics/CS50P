from project import use_serialport
import pytest

def main():
    test_use_serialport()

def test_use_serialport():
    with pytest.raises(ConnectionError):
        use_serialport()

def test_animation():
    ...

def test_csv_header():
    ...

def test_csv_file():
     ...

def test_serial_data():
     ...



if __name__ == "__main__":
    main()
