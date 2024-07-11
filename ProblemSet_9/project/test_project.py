from project import csv_header
import pytest

def main():
    test_csv_header()

def test_csv_header():
    fieldnames = ["Date", "Time", "Datapoint [No.]", "Temperature [˚C]", "Humidity [%]"]


if __name__ == "__main__":
    main()
