# Write your code here :-)
import time
import board
import digitalio
import microcontroller

# For most CircuitPython boards:
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

try:
    with open("/braxtonworstpmNA.txt", "a") as fp:
        while True:
            # temp = microcontroller.cpu.temperature
            # do the C-to-F conversion here if you would like
            for x in range(6):
                temp = x
                fp.write("{0:f}\n".format(temp))
            fp.flush()
            led.value = not led.value
            time.sleep(1)
except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.5  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.25  # ...blink the LED faster!
    while True:
        led.value = not led.value
        time.sleep(delay)
