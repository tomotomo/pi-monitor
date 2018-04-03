import datetime
import random
import os
import pprint
# import serial
import time


# ser = serial.Serial('/dev/ttyS1', 9600)
pp = pprint.PrettyPrinter(indent=2)


def get_temp():
    return random.randint(0, 50)

def get_humid():
    return random.randint(0, 50)

def get_current():
    return random.randint(-100, 100)


if __name__ == '__main__':

    while True:
        timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
        data = {
            "mac": "aa:bb:cc:dd:ee",
            "time": timestamp, 
#            "current": get_current(),
#            "humid": get_humid(),
            "temp": get_temp()
        }

        pp.pprint(data)
        time.sleep(5)
