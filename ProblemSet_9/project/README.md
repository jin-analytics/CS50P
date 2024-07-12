# Plot serial data dynamicly from an serial device and safe it into an csv-file
    #### Video Demo:  <https://youtu.be/E77XgQzNAdQ>
    #### Description:

    My final project has the purpose to plot sensor data in realtime from an Arduino and safe it
    into an csv-file. The Data comes from a Sensor DHT11, this sensor is cappable of measuring the
    temperature and the humidity. The Arduino Portenta H7 reads the data from the sensor and writes
    it to the serial connection (USB cable to the computer). The program will use this data to plot
    it live and safes each datapoint to the csv-file. Both parameters (temperature, humidity) will be stored inside my
    python programm. The parameters will be used to be plotted in an animated plot. The x-axis moves
    for each datapoint to the right. The y-axis on the left is for the temperature in Celsius [˚C],
    the y-axis on the right is for the humidity in Percent [%]. The animated plot will pop up in an
    seperated window. Parallel to the animation, the data will also be stored inside an csv-file.
    Each second comes a new row in this file. The header structure is like this (with one example
    row):
    Date,Time,Datapoint [No.],Temperature [˚C],Humidity [%]
    2024-06-15,20:28:11,0,25,44
    If the window gets closed, the program will stop plotting and safing data to the csv-file.
    Since the data comes in an Byte format, there is some data cleaning through regular expressions
    implemented. With this, there will be just the value of temperature and humidity returned to the
    plot function.
    In the beginning of the program "program.py", there will be defined how the axis should look like,
    and the general figure setup.
    The Arduino has the program "SensorData.ino" installed.
    - Setup: |sensor|->|arduino|->|computer|->|data visualization|

    In case you dont have the exact setup with an Arduino and the installed sensor, you can use the
    default version "project_default.py". This doesnt need an serial connection and just prints random
    data withing defined intervals. With this, you can simulate the original setup.
    - Setup: |computer|->|random data visualization|

    In case you dont have the sensor but an arduino, you can use the arduino program "RandomNumber.ino".
    This will print random data which can be read through the python program "project.py".
    - Setup: |arduino|->|computer|->|random data visualization|

