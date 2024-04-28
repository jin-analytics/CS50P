import matplotlib.pyplot as plt
import random
from matplotlib import animation
import count
from itertools import count

x = []
y = []

index = count() ## count(2.5, 0.5) → 2.5 3.0 3.5 ...

def plot_animated_data(i, tempdata):
    x.append(next(index))
    y.append(random.randrange(17, 22))

    #Figure settings
    fig, ax = plt.subplots(figsize=(5, 3))
    fig.subplots_adjust(bottom=0.15, left=0.2)
    ax.plot(x, tempdata)
    ax.set_xlabel('Datapoint [Nr.]')
    ax.set_ylabel('Temprature [°C]')
    ax.set_title('Temperature data from Arduino', loc='center')

    plt.savefig('data.png', bbox_inches='tight') #fits figure with less whitespace around the image

ani = animation.FuncAnimation(plt.gcf(), plot_animated_data, interval=1000)
