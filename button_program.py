#Louis Powers
#1 - 16 - 2018 also flames birthday
#Button DJ Raspi

import RPi.GPIO as GPIO

import time

import random

import os


path_music = "/usr/share/scratch/Media/Sounds/Music Loops"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals"
path_effects = "/usr/share/scratch/Media/Sounds/Effects"
def get_MP3_sounds(sound_path):
    sound_file = os.listdir(sound_path)
    sound_file = [sound_file for sound_file in sound_file if sound_file.endswith('.mp3')]
    return sound_file
def play_random_sound(sound_path, sound_file):
    sound_file = random.choice(sound_file)
    os.system("omxplayer -o local '" + sound_path +
              "/" + sound_file + "' &")

sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
path_effects = get_MP3_sounds(path_vocals)
# Variables for buttons


button_pin1 = 6

button_pin2 = 19

GPIO.setmode(GPIO.BCM)


GPIO.setup(button_pin1, GPIO.IN)

GPIO.setup(button_pin2, GPIO.IN)


print(sounds_music)
print(sounds_vocals)

os.system("clear")

print("""The best DJ
         press button 1 for music sounds
         press button 2 for vocal sounds
         press ctrl + C to exit
               ^
             <(_)>
          ___(___)___
         |  (_____)  |
           (_______)
          (_________)
         (___________)""")
while True:
    if GPIO.input (button_pin1):
        print("You pressed #1 ")
        play_random_sound(path_music, sounds_music)
        time.sleep(.1)
    if GPIO.input(button_pin2):
        print ("You pressed #2")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(.1)
    if GPIO.input(button_pin2) and GPIO.input (button_pin1):
        print ("You pressed #3")
        play_random_sound(path_effects,sounds_effects)
        time.sleep(.1)
    time.sleep(.1)
