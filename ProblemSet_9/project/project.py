import random
import time

def main():
    get_data()

# first, use random data... later arduino
def get_data():
    while True:
        temp = random.randrange(15, 25,)
        print(temp)
        time.sleep(1)
        exit()


def create_window_for_data_plot():
    ...

def plot_data():
    plt.plot(df['sepal_length'])


if __name__ == "__main__":
    main()
