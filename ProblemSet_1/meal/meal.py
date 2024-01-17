# breakfast  time [07:00;08:00]
# lunch      time [12:00;13:00]
# dinner     time [18:00;19:00]



def main():
    #print("TEST MAIN")

    # Gives the variable "t" to the convert funciton
    t=input("What time is it? ")
   # print("Before convert function ",t)
    convert(t)
    #print("After convert function ",t)




def convert(time):
    #print(time)
    time = time.replace(':',' ')
    time = time.split()
    time[0] = int(time[0])
    time[1] = float(time[1])
    time[1] = round(time[1]*1.666)
    time = ' '.join(time)

    # 1 minute = 1.66666... %
    #time = float(time)
    print("Check: ",time)
    return time


# if __name__ == "__main__": - helps to prevent errors due to not defined
# global variables yet of we call main() inside there
if __name__ == "__main__":
    main()
    #print("TEST function")

