import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin_red = 21
led_pin_green = 22
led_pin_blue = 23

GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)

pwm_red = GPIO.PWM (led_pin_red,100)
pwm_green = GPIO.PWM (led_pin_green,100)
pwm_blue = GPIO.PWM (led_pin_blue,100)

pwm_red.start(20)
pwm_green.start(50)
pwm_blue.start(10)
time.sleep(3)

pwm_red.stop()
pwm_blue.stop()
pwm_green.stop()
GPIO.cleanup()
