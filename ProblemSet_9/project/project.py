import re
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import serial
import serial.tools.list_ports

# * - - - Define USB Modem and Baudrate for the connected Arduino
sPort = "/dev/cu.usbmodem101"
Baud = 9600

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
    serial_data(use_serialport(), Baud)
    csv_header(fieldnames)
    # FuncAnimation is used to create the animation:
    ani1 = FuncAnimation(
        fig=fig,  # fig is the figure to animate
        func=animation,  # update is the function to call at each frame
        frames=1000,  # frames specifies the number of frames in the animation.
        save_count=None,  # then there is no error message
        interval=1000,  # interval is the delay between frames in milliseconds.
    )
    plt.show()


# * - - - Animated plot
def animation(frame):
    # Get data from Serial Device and safe it into two variables
    temp, humid = serial_data("/dev/cu.usbmodem101", 9600)

    # Set the moving x-axis through interval
    ax1.set_xlim(left=frame - 3, right=frame + 1)

    # Append data for x-axis and y-axis for both plots
    x_values.append(frame)
    yTemp_values.append(temp)
    yHumid_values.append(humid)

    # Update plot data
    animated_plot_C.set_data(x_values[1:], yTemp_values[1:])
    animated_plot_F.set_data(x_values[1:], yHumid_values[1:])

    # Gets current date and time
    currentDateAndTime = datetime.now()
    # Gets current date... for example 2024-06-11
    currentDate = currentDateAndTime.date()
    # Gets current time in hours:minute:seconds... for example: 18:22:52
    currentTime = currentDateAndTime.strftime("%H:%M:%S")

    # Safe Data To CSV-File
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


# * - - - Get serial data from the arduino and return temperature and humidity
def serial_data(s, b):
    aSerialData = serial.Serial(s, b)
    time.sleep(0.5)
    if aSerialData.inWaiting():
        sData = str(aSerialData.readline())
        # RegEx pattern to remove the unwanted signs and letters from databyte
        pattern = r"b'|\\r|\\n'"
        sData = re.sub(pattern, "", sData)
        sData = sData.split(",")
        return int(sData[0]), int(sData[1])

def use_serialport():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    sPort = str("default")  # Mac - find usb connections using >ls /dev/cu.usb*
    portsList = []

    for _ in ports:
        portsList.append(str(_))

    for i in range(len(portsList)):
        if portsList[i].startswith(str("/dev/cu.usbmodem")):
            sPort = str("/dev/cu.usbmodem")  # On Mac - find this using >ls /dev/cu.usb*
            break
        else:
            sPort = str("default")  # Mac - find usb connections using >ls /dev/cu.usb*

    if sPort == "default":
        raise ConnectionError("No USB Port connected")
        # sys.exit("No USB Port connected")
    else:
        return sPort

# * - - - Start
if __name__ == "__main__":
    main()
