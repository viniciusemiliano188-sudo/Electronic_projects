#LED blinking script
from machine import Pin
import time

led =  Pin(12 , Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
