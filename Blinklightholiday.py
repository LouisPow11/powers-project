# BLINK LIGHT FOR HOLIDAY
#12-19-2017
import RPi.GPIO as GPIO
import time

LED_pin_green = 21

LED_pin_red = 22

LED_pin_blue = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)

GPIO.setwarnings (False)

while True:
    GPIO.output(LED_pin_red, GPIO.HIGH)
    print ("ON")
    time.sleep(.01)
    
    GPIO.output(LED_pin_red, GPIO.LOW)
    print("OFF")
    time.sleep(.01)
    
    GPIO.output(LED_pin_green, GPIO.HIGH)
    print ("ON")
    time.sleep(.01)
    
    GPIO.output(LED_pin_green, GPIO.LOW)
    print("OFF")
    time.sleep(.01)
    
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    print ("ON")
    time.sleep(.01)
    
    GPIO.output(LED_pin_blue, GPIO.LOW)
    print("OFF")
    time.sleep(.01)

    GPIO.output(LED_pin_green, GPIO.HIGH)
    print ("ON")
    time.sleep(.01)
    
    GPIO.output(LED_pin_green, GPIO.LOW)
    print("OFF")
    time.sleep(.01)
    
    
