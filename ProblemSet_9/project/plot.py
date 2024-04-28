import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    get_data()
    plot_data()

# first, use random data... later arduino data
def get_data():
    #while True:
    templist = []
    for _ in range(10):
        temp = random.randrange(15, 25,)
        templist.append(temp)
        #print(templs)
        #time.sleep(1)
    return templist

def plot_data():
    # evenly spaced values with given stepwidth (default stepwidth: 1)
    y = np.arange(0, 10)
    # evenly spaced values with given a number of steps
    y_float = np.linspace(0, 10, 11)
    print(y)

main()
