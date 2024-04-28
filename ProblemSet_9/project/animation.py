import random
from itertools import count
#import pandas as pd
import matplotlib.pyplot as plt
import time
from matplotlib import animation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.cla()
plt.plot(x_vals, y_vals)


index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 20))

ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.savefig('pic.png')

