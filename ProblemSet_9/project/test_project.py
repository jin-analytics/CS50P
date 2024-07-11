from project import use_serialport
import pytest

def main():
    test_use_serialport()

def test_use_serialport():
    with pytest.raises(ConnectionError):
        use_serialport()
def test_animation(frame):
       assert frame = 4:
       
       ax1.set_xlim(left=frame - 3, right=frame + 1)


if __name__ == "__main__":
    main()
