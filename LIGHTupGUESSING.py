#Guess the number, shows blue if too low, red if too high, green if correct.
#1/3/2018
#Louis Powers
import random
import time
import RPi.GPIO as GPIO

play_again = "Y"

def game_over():
    print ("GAME OVER YOU RAN OUT OF GUESSES")

def blink_led(pin):
    for i in range(5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(.2)
        

GPIO.setmode(GPIO.BCM)

led_pin_red = 21
led_pin_green = 22
led_pin_blue = 23

GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)



print ("." * 80)
print ("Light up guessing Game!!!")
print ("^" * 80)
print ("""
You have five guesses to guess a number between 1 and 20
Too Low ---> Blue
Too High ----> Red
Just right -----> Green"""
       )

while play_again == "Y":
    
    #Get random number 1 to 20
    num = random.randint(1,20)
    #Start loop
    guesses = 0

    while guesses < 5:
        guess = input ("Guess a number from 1 to 20: ")
        guess = int(guess)
        guesses += 1
        if guess == num:
            print ("You are correct!!")
            blink_led (led_pin_green)
            break
        elif guess < num:
            print ("Too low!")
            blink_led (led_pin_blue)
        elif guess == 0:
            print ("""You found an easter egg congrats
    
                 ____ \__ \
                 \__ \__/ / __
                 __/ ____ \ \ \    ____
                / __ \__ \ \/ / __ \__ \
           ____ \ \ \__/ / __ \/ / __/ / __
      ____ \__ \ \/ ____ \/ / __/ / __ \ \ \
      \__ \__/ / __ \__ \__/ / __ \ \ \ \/
      __/ ____ \ \ \__/ ____ \ \ \ \/ / __
     / __ \__ \ \/ ____ \__ \ \/ / __ \/ /
     \ \ \__/ / __ \__ \__/ / __ \ \ \__/
      \/ ____ \/ / __/ ____ \ \ \ \/ ____
         \__ \__/ / __ \__ \ \/ / __ \__ \
         __/ ____ \ \ \__/ / __ \/ / __/ / __
        / __ \__ \ \/ ____ \/ / __/ / __ \/ /
        \/ / __/ / __ \__ \__/ / __ \/ / __/
        __/ / __ \ \ \__/ ____ \ \ \__/ / __
       / __ \ \ \ \/ ____ \__ \ \/ ____ \/ /
       \ \ \ \/ / __ \__ \__/ / __ \__ \__/
        \/ / __ \/ / __/ ____ \ \ \__/
           \ \ \__/ / __ \__ \ \/
            \/      \ \ \__/ / __
                     \/ ____ \/ /
                        \__ \__/
                        __/

    """)
        
        else:
            print ("Too High")
            blink_led (led_pin_red)
    else:
        game_over()
    play_again = input ("Do you want to play again Y/N").upper()
print("Thank you for playing")



  
