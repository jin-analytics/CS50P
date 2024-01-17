def main():
    # Gives the variable "t" to the convert funciton
    t=input("What time is it? ")
    # defines the t variable with the returned variable (time) from the convert() function
    t = convert(t)
    #print("After convert function ",t)

    if 7 <= t <= 8:          # breakfasttime [07:00;08:00]
        print("Breakfast time")
    elif 12 <= t <= 13:        # lunchtime [12:00;13:00]
        print("lunch time")
    elif 18 <= t <= 19:        # dinnertime [18:00;19:00]
        print("dinner time")



def convert(time):
    # replaces the ":" to a " " space for the split function
    time = time.replace(':',' ')
    # splits the time variable
    time = time.split()
    # frist column to an integer
    time[0] = int(time[0])
    # second cloumn to a float, so that we can later compare the number and not the time
    time[1] = float(time[1])
    # multiplies the minutes (1 minute = 1.666...%) to get the percentage of a full hour
    time[1] = round(time[1]*1.666)
    # Adds both colums into a string
    time[0] = str(time[0])
    time[1] = str(time[1])
    # Join the string back together
    time = '.'.join(time)
    # convert it back to a float number as a single number now with the estimated percentage per hour
    time = float(time)
    #print("Check: ",time)
    return time


# if __name__ == "__main__": - helps to prevent errors due to not defined global variables yet of we call main() inside there
if __name__ == "__main__":
    main()
