from time import sleep_ms, ticks_ms, ticks_diff
import Stepper
from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
from dth import DTH
import utime
import pycom
import machine
# main.py -- put your code here!
from mqtt import MQTTClient
# from mqtt import MQTTClient_lib as MQTTClient
from network import WLAN
import time



# Wireless network
WIFI_SSID = "Mi"
WIFI_PASS = "65yryr"


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "ea224"
AIO_KEY = "aio_LJRv03mGN8hG4GtaEJMs0kHQwKiG"
AIO_CONTROL_FEED = "ea224/feeds/button"
AIO_TEMP_FEED = "ea224/feeds/temperature"
AIO_RANGING_FEED = "ea224/feeds/ranging"
AIO_MOTOR_FEED = "ea224/feeds/motor"
# RGBLED
# Disable the on-board heartbeat (blue flash every 4 seconds)
# We'll use the LED to respond to messages from Adafruit IO
pycom.heartbeat(False)
time.sleep(0.1) # Workaround for a bug.
                # Above line is not actioned if another
                # process occurs immediately afterwards
pycom.rgbled(0xff0000)  # Status red = not working

# WIFI
# We need to have a connection to WiFi for Internet access
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html

wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)

while not wlan.isconnected():    # Code waits here until WiFi connects
    machine.idle()

print("Connected to Wifi")
pycom.rgbled(0xffd7000) # Status orange: partially working
time.sleep(3)

pycom.heartbeat(False)






RANDOMS_INTERVAL = 5000 # milliseconds
last_random_sent_ticks = 0  # milliseconds





def sub_cb(topic, msg):
    print(msg)
    if msg == b"1":             
        client.publish(topic="ea224/feeds/motor", msg="Motor are spinning")
        mashine()
    



def send_temp():
    global last_random_sent_ticks
    global RANDOMS_INTERVAL
    global x
    if ((time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL):
        return; # Too soon since last one sent.
    else:
        print("Publishing: {0} to {1} ... ".format(x, AIO_TEMP_FEED), end='')
        try:
            client.publish(topic=AIO_TEMP_FEED, msg=str(x))
            client.publish(topic=AIO_RANGING_FEED, msg=str(diss))
            print("DONE")
        except Exception as e:
            print("FAILED")
        finally:
            last_random_sent_ticks = time.ticks_ms()


def spined():
    client.publish(topic=AIO_MOTOR_FEED, msg="Motor spinned")




s1 = Stepper.create(Pin("P23", mode=Pin.OUT),Pin("P22", mode=Pin.OUT),Pin("P21", mode=Pin.OUT),Pin("P20", mode=Pin.OUT), delay=3)
last_time = ticks_ms() # save current time
delay = 2 # 2 sec
x = 0 # temp value
displayed_value = 0
diss = 0

# initialise Ultrasonic Sensor pins
echo = Pin("P18", mode=Pin.IN)
trigger = Pin("P19", mode=Pin.OUT)
trigger(0)


# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2
    pos_distance = abs(distance)

    return pos_distance


def distance_median():

    # initialise the list
    distance_samples = []
    # take 10 samples and append them into the list
    for count in range(10):
        distance_samples.append(int(distance_measure()))
    # sort the list
    distance_samples = sorted(distance_samples)
    # take the center list row value (median average)
    distance_median = distance_samples[int(len(distance_samples)/2)]
    # apply the function to scale to volts
    return int(distance_median)

def tempo():
    global x
    th = DTH(Pin('P3', mode=Pin.OPEN_DRAIN),0)
    result = th.read()
    if result.is_valid():
        x= result.temperature
    print("x",x)


#lcd
# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def LCD():
    global displayed_value
    i2c = I2C()
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.putstr("The Temperature is\n \t "+ str(x))
    displayed_value = x

#if __name__ == "__main__":
def mashine():
    global x
    global displayed_value
    global diss
    global last_time
    global delay
    while True:
        if(ticks_diff(ticks_ms(), last_time) > delay):
            print("step...",end=" ")
            s1.step(125) # or s1.step(-100)
            print("stepped")
            last_time = ticks_ms()
            tempo() # send th
            diss = distance_median()  
            send_temp()
            spined()
            if displayed_value != x :
                LCD()
        else:
            tempo()
            send_temp()
            diss = distance_median()
            if displayed_value != x :
                LCD()
client = MQTTClient("ea224pn", AIO_SERVER,user = AIO_USER,password= AIO_KEY, port = AIO_PORT)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic=AIO_CONTROL_FEED)

while True:
    client.check_msg()
    time.sleep(2)
#     time.sleep(2) cant use that cuse the phone charger stop outputing
#s1.step(100)
    
#s1.angle(180)
#s1.angle(360,-1) # or s1.angle(-360)
