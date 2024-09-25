from sense_hat import SenseHat
import time

# create an object from sensehat class
sense = SenseHat()

# good idea to clear your pi
sense.clear()

# set colors
R=[255, 0, 0]
O=[255,140,0]
Y=[255,255,0]
G=[0,255,0]
B=[30,144,255]
I=[0, 0, 139]
V=[138,43,226]
X=[0,0,0]
W=[255,255,255]

# Hard coded values for testing
# temp = 30
# temp = -10
# temp = 18
# humidity = 82
# humidity = 60
# humidity = 100

# Read temp and humidity CONTINUOUSLY
while True:
    # wait 2 seconds between each display!
    time.sleep(1)
    temp = sense.get_temperature()
    print("Temperature: %.2f C" % temp)

    humidity = sense.get_humidity()
    print("Humidity: %.2f %%rH" % humidity)

# Display a rainbow when temp ^ 20degC, humidity ^ 80%
    rainbow=[
        R,R,R,R,R,R,R,R,
        R,O,O,O,O,O,O,O,
        R,O,Y,Y,Y,Y,Y,Y,
        R,O,Y,G,G,G,G,G,
        R,O,Y,G,B,B,B,B,
        R,O,Y,G,B,I,I,I,
        R,O,Y,G,B,I,V,V,
        R,O,Y,G,B,I,V,X
    ]
    if (temp>20 and humidity>80):
        sense.set_pixels(rainbow)
    else:
        sense.clear()

# Display a sun when temp^20C and humidity below 80%
    sun=[
        X,X,X,X,X,X,X,X,
        X,X,X,Y,Y,X,X,X,
        X,X,Y,Y,Y,Y,X,X,
        X,Y,Y,Y,Y,Y,Y,X,
        X,Y,Y,Y,Y,Y,Y,X,
        X,X,Y,Y,Y,Y,X,X,
        X,X,X,Y,Y,X,X,X,
        X,X,X,X,X,X,X,X
    ]

    if(temp>20 and humidity<80):
        sense.set_pixels(sun)
    else:
        sense.clear()

# Display snow when temp below 0C and humidity ^ 80%
    snow1=[
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W
    ]

    snow2=[
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X,
        X,W,X,W,X,W,X,W,
        W,X,W,X,W,X,W,X
    ]

    if (temp<0 and humidity>80):
        sense.set_pixels(snow1)
        time.sleep(1)
        sense.set_pixels(snow2)

    else :
        sense.clear()

# Display Rain when temp^0C and humidity=100%
    rain1=[
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B
    ]

    rain2=[
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X,
        X,B,X,B,X,B,X,B,
        B,X,B,X,B,X,B,X
    ]

    if (temp>0 and humidity==100):
        sense.set_pixels(rain1)
        time.sleep(1)
        sense.set_pixels(rain2)

    else :
        sense.clear()

