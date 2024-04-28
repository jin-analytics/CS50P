import matplotlib.pyplot as plt
def main():
    print('ww')
    get_data()
    #plot_data()

# first, use random data... later arduino
def get_data():
    #while True:
    templs = []
    for _ in range(10):
        temp = random.randrange(15, 25,)
        templs.append(temp)
        print(templs)
        #time.sleep(1)
