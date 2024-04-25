import random
def main():
    get_data()

# first, use random data... later arduino
def get_data():
    try:
        while True:
            temp = random.randrange(15, 25,)
            #if temp == 18:
             #   return False
            print(temp)
    except EOFError:
        exit()

def create_window_for_data_plot():
    ...

def plot_data():
    ...


if __name__ == "__main__":
    main()
