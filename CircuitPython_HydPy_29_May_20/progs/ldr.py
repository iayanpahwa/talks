import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Light:", cpx.light)
    print((cpx.light,))
    time.sleep(1)
