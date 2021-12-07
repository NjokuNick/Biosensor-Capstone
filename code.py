# Write your code here :-)
import MAX30102
from machine import sleep
from utime import ticks_diff, ticks_ms
import logging
import board
import digitalio
import time
import busio
import microcontroller

# initializations for LED and storage boolean value
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()
valT = True
UART_True = True
# UART initializations
uart = board.UART()   # Uses pins 4 and 3 for TX and TX, baudrate 9600.

on = 'on'
off = 'off'

def uartCom(boolean, number, onOff):
    led.value = boolean
    syncInfo == number
    uart.write(onOff)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

# configures the instance of the heart rate sensor
    sensor = MAX30102()

    print("Setting up sensor with default configuration.", '\n')
    sensor.setup_sensor()
    # Set the sample rate to 80 samples/s are collected by the sensor
    sensor.setSampleRate(80)
    # Set the number of samples to be averaged per each reading
    sensor.setFIFOAverage(8)

    sleep(1)

    # The getGreen() method allows to extract the temperature from the green sensor
    print("Reading bpm", '\n')
    print(sensor.getRed())

    # Select wether to compute the acquisition frequency or not
    compute_frequency = False

    print("Starting data acquisition from Red & IR registers...", '\n')
    sleep(1)

    t_start = ticks_ms()    # Starting time of the acquisition
    samples_n = 0           # Number of samples that has been collected

    while(True):
        # pulls for sensor data on every line run
        sensor.check()

        # Check if the storage contains available samples
        if(sensor.available()):
            # Access the storage FIFO and gather the readings (integers)
            red_reading = sensor.popRedFromStorage()
            IR_reading = sensor.popIRFromStorage()

        try:
            with open("/measurements.txt", "a") as fp:
                while valT:
                    # temp = microcontroller.cpu.sensor reading
                    for x in range(1):
                        temp = red_reading  # stores value of bpm reading
                        fp.write("{0:f}\n".format(temp))
                        temp = IR_reading
                        fp.write("{0:f}\n".format(temp))
                    fp.flush()
                    led.value = not led.value
                    time.sleep(1)
                    valT = False

        except OSError as e:  # Typically when the filesystem isn't writeable...
            delay = 0.5  # ...blink the LED every half second.
            if e.args[0] == 28:  # If the file system is full...
                delay = 0.25  # ...blink the LED faster!
            while True:
                led.value = not led.value
                time.sleep(delay)

        # Using readlines()
        file1 = open('measurements.txt', 'r')
        Lines = file1.readlines()  # stores each line by line product into Lines
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))  # serial print confirmation
            UART_True = True
            while UART_True:
                data = uart.read(32)  # read up to 32 bytes
                # data_string manipulated on phone during testing
                # determine if data is in need to be synced before turning on data send?
                if data is not None:
                    led.value = True
                    # convert bytearray to string
                    data_string = Lines.join([chr(b) for b in data])
                    uart.write(data_string)  # Sends data to receiver/ smartphone terminal
                    print(data_string, end="")
                    UART_True = False
