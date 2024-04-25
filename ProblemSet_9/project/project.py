import random
import time
import matplotlib.pyplot as plt
import numpy as np

def main():
    plot_data()
    get_data()

# first, use random data... later arduino
def get_data():
    while True:
        temp = random.randrange(15, 25,)
        print(temp)
        time.sleep(1)


def create_window_for_data_plot():
    ...

def plot_data():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
