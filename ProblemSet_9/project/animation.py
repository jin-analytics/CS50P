import matplotlib.pyplot as plt
import random
from matplotlib import animation
import itertools

x = []
y = []

index = itertools.count() ## count(2.5, 0.5) → 2.5 3.0 3.5 ...

def plot_animated_data(i):
    x.append(next(index))
    y.append(random.randrange(17, 22))

    plt.cla()
    plt.plot(x,y)


ani = animation.FuncAnimation(plt.gcf(), plot_animated_data, interval=1000)
#ani.savefig('data.png', bbox_inches='tight') #fits figure with less whitespace around the image
