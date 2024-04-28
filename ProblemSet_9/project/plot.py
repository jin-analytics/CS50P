import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    i = input("number of data points")
    get_data(i)
    plot_data(i)

# first, use random data... later arduino data
def get_data(i):
    #while True:
    templist = []
    for _ in range(int(i)):
        temp = random.randrange(15, 25,)
        templist.append(temp)
        #print(templs)
        #time.sleep(1)
    return templist

def plot_data(i):
    # evenly spaced values with given stepwidth (default stepwidth: 1)
    y = np.arange(0, int(i))
    # evenly spaced values with given a number of steps
    y_float = np.linspace(0, int(i), int(i)+1)
    print(y)
    print(y_float)

main()
