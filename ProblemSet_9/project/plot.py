import matplotlib.pyplot as plt
import random

def main():
    get_data()
    #plot_data()

# first, use random data... later arduino
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
    

main()
