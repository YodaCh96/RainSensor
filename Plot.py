import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit

def plot():
    plt.title("Rainsensor")
    plt.grid(True)
    plt.ylabel("Values")
    plt.plot(SensorValues, label="values")
    plt.legend(loc="upper right")


def doatexit():
    serialArduino.close()


SensorValues = []

plt.ion()

RainSensor = serial.Serial("COM3", 9600)

atexit.register(doatexit)

for i in range(0, 26):
    SensorValues.append(0)

while True:
    while RainSensor.inWaiting() == 0:
        pass

    RainSensorRead = RainSensor.readline(500)

    try:
        RainSensorRead = int(RainSensorRead)
        if RainSensorRead <= 1024:
            if RainSensorRead >= 0:
                SensorValues.append(RainSensorRead)
                SensorValues.pop(0)
                drawnow(plot)
            else:
                print("Invalid negative number.")
        else:
            print("Invalid too large number.")
    except ValueError:
        print("Cannot cast")
