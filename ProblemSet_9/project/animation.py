import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib
from matplotlib import FuncAnimation


x = []
y = []

index = count()

def get_data(i):
    templist = []
    for _ in range(int(i)):
        temp = random.randrange(17, 22)
        templist.append(temp)
        #time.sleep(1)
    return templist

def plot_animated_data(i, tempdata):
    # evenly spaced values with given stepwidth (default stepwidth: 1)
    x = np.arange(0, int(i))

    #Figure settings
    fig, ax = plt.subplots(figsize=(5, 3))
    fig.subplots_adjust(bottom=0.15, left=0.2)
    ax.plot(x, tempdata)
    ax.set_xlabel('Datapoint [Nr.]')
    ax.set_ylabel('Temprature [°C]')
    ax.set_title('Temperature data from Arduino', loc='center')

    plt.savefig('data.png', bbox_inches='tight') #fits figure with less whitespace around the image

