# breakfast  time [07:00;08:00]
# lunch      time [12:00;13:00]
# dinner     time [18:00;19:00]



def main():
    #print("TEST MAIN")

    # Gives the variable "t" to the convert funciton
    t=input("What time is it? ")
    print("Before convert function ",t)
    convert(t)
    print("After convert function ",t)




def convert(time):
    #print(time)
    time = time.split
    #time = float(time)
    print(time)
    return time


# if __name__ == "__main__": - helps to prevent errors due to not defined
# global variables yet of we call main() inside there
if __name__ == "__main__":
    main()
    print("TEST function")

