import board
import digitalio
import time
import busio
import microcontroller


# import board
uart = board.UART()   # Uses pins 4 and 3 for TX and TX, baudrate 9600.
i2c = board.I2C()     # Uses pins 2 and 0 for SCL and SDA.


led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=9600)

syncInfo = 0

# list1 = ["abc", 34, True, 40, "male"]
# for x in list1:
#  print(x)
#
#  const char str[] = "My very long string";
#  Serial.print("Address of str $");
#  Serial.println((int)&str, HEX);
on = 'on'
off = 'off'

def uartCom(boolean, number, onOff):
    led.value = boolean
    syncInfo == number
    uart.write(onOff)

while True:
    data = uart.read(32)  # read up to 32 bytes
    # data_string manipulated on phone during testing

    # determine if data is in need to be synced before turning on data send?
    if data is not None:
        data_string = ''.join([chr(b) for b in data])
        # converts bytearray to string, standard parameter
        if data_string == '1':
            uartCom(True, 1, on)
            # led.value = True
            # syncInfo=='1' # mine
            # uart.write('on')

        if data_string == '0':
            uartCom(False, 3, off)
            # led.value = False
            # syncInfo=='3' #mine
            # uart.write('off')
