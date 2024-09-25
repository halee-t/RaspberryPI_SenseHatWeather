from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()

while True:
    time.sleep(1)
    # use the compass sensor
    north = sense.get_compass()
    print("North: %s" % north)

    # Maybe we can display the direction we are currently facing?