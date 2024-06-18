import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from datetime import datetime

# * - - - Creates the headername for the file 'data.csv'
fieldnames = ["Date", "Time", "Datapoint [No.]", "Temperature [˚C]", "Humidity [%]"]

# * - - - Creates parameter for the animated plot with empty list
x_values = []
yTemp_values = []
yHumid_values = []

# * - - - Defines the figure and for the nimated Plot
fig, ax1 = plt.subplots()

# * - - - Plot data on the first y-axis (left y-axis)
ax1.plot(x_values, yTemp_values, "r-", label="Temperature [˚C]")
ax1.set_xlabel("Datapoint [No.]")
ax1.set_ylabel("Temperature [˚C]", color="r")
ax1.tick_params(axis="y", labelcolor="r")

# * - - - Create a second y-axis (right y-axis)
ax2 = ax1.twinx()
ax2.plot(x_values, yHumid_values, "b-", label="Humidity [%]")
ax2.set_ylabel("Humidity [%]", color="b")
ax2.tick_params(axis="y", labelcolor="b")

# * - - - Set limit for x-axis, y-axis left, y-axis right
ax1.set_xlim([-5, 5])
ax1.set_ylim([15, 25])  # y-axis left
ax2.set_ylim([35, 65])  # y-axis left
plt.grid()

# * - - -  Adding legends to the animated plot
lines = ax1.get_lines() + ax2.get_lines()
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper right")

# * - - - Create the plot for temperature (C) and humidity (F)
(animated_plot_C,) = ax1.plot([], [], "ro-", markersize=4)
(animated_plot_F,) = ax2.plot([], [], "bo-", markersize=4)


def main():
    csv_header(fieldnames)
    # FuncAnimation is used to create the animation:
    ani = FuncAnimation(
        fig=fig,  # fig is the figure to animate
        func=animation_random,  # update is the function to call at each frame
        frames=1000,  # frames specifies the number of frames in the animation.
        save_count=None,  # then there is no error message
        interval=1000,  # interval is the delay between frames in milliseconds.
    )
    plt.show()


# * - - - Animated plot
def animation_random(frame):

    # Set the moving x-axis through interval
    ax1.set_xlim(left=frame - 3, right=frame + 1)

    # Append data for x-axis and y-axis for both plots
    x_values.append(frame)
    yTemp_values.append(random.randint(15, 25))  # Example random y value for plot C
    yHumid_values.append(random.randint(40, 60))  # Example random y value for plot F

    # Update plot data
    animated_plot_C.set_data(x_values[1:], yTemp_values[1:])  # Update plot C
    animated_plot_F.set_data(x_values[1:], yHumid_values[1:])

    ##### Safe Data To CSV-File #####
    # Gets current date and time... for example: 2024-06-11 18:06:31.689454
    currentDateAndTime = datetime.now()
    # Gets current date... for example 2024-06-11
    currentDate = currentDateAndTime.date()
    # Gets current time in hours:minute:seconds... for example: 18:22:52
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    # Opens function which safes the data in the csv-file
    csv_file(
        fieldnames,
        currentDate,
        currentTime,
        x_values[frame],
        yTemp_values[frame],
        yHumid_values[frame],
    )

    return animated_plot_C, animated_plot_F


# * - - - Creates the header for the file 'data.csv'
def csv_header(fieldnames):
    with open("data.csv", "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_file.close()
    return csv_file


# * - - - Writes data to the file 'data.csv'
def csv_file(fieldnames, currentDate, currentTime, datapoint, temperature, humidity):
    with open("data.csv", "a") as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )

        csv_writer.writerow(
            {
                fieldnames[0]: currentDate,
                fieldnames[1]: currentTime,
                fieldnames[2]: datapoint,
                fieldnames[3]: temperature,
                fieldnames[4]: humidity,
            }
        )
        csv_file.close()
        return csv_file


# * - - - Start
if __name__ == "__main__":
    main()

