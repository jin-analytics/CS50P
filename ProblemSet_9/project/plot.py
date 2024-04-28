import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib

def main():
    i = input("Number of data points: ")
    plot_data(i, get_data(i))

# first, use random data... later arduino data
def get_data(i):
    templist = []
    for _ in range(int(i)):
        temp = random.randrange(15, 25,)
        templist.append(temp)
        #time.sleep(1)
    return templist

def plot_data(i, tempdata):
    # evenly spaced values with given stepwidth (default stepwidth: 1)
    x = np.arange(0, int(i))
    # evenly spaced values with given a number of steps
    x_float = np.linspace(0, int(i), int(i)+1)

    #Figure settings
    fig, ax = plt.subplots(figsize=(5, 3))
    fig.subplots_adjust(bottom=0.15, left=0.2)
    ax.plot(x, tempdata)
    ax.set_xlabel('Datapoints [Nr.]')
    ax.set_ylabel('Temprature [°C]')


    plt.savefig('data.png', bbox_inches='tight') #fits figure with less whitespace around the image

main()
