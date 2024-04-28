import random
import time
import matplotlib.pyplot as plt
import numpy as np

def main():
    get_data()
    plot_data()

# first, use random data... later arduino
def get_data():
    #while True:
    for _ in range(10):
        temp = random.randrange(15, 25,)
        print(temp)
        time.sleep(1)


def create_window_for_data_plot():
    ...

def plot_data():
 ...


if __name__ == "__main__":
    main()
