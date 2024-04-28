import random
import time
import matplotlib.pyplot as plt
import numpy as np

def main():
    get_data()
    plot_data()

# first, use random data... later arduino
def get_data():
    while _ in range(10):
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
    #plt.show()
    with open('plot.png', 'w') as file:
        file.write(plt.show())


if __name__ == "__main__":
    main()
