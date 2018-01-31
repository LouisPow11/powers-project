#Louis_powers
#2017
#guessing game

print ("_" * 35)
print ("NORWEGIAN BLUE GUESSING GAME")
print ("~" * 35)

instructions = """You walk into a Bolton pet shop and need to guess the age of the norwegain blue parrot
in order to take it home.
/oo\
\   >
 \/
|  |"""

print (instructions)
# Make up parrots age
parrot_age = 12

#Set guesses to 0
number_of_guesses = 0

# Get a guess from user
guess = input ("Guess the age of the parrot [1 to 21]:")

guess = int(guess)#Converts a string to an interger and stores it back into guess


if guess == parrot_age:
    print("CONGRATS YOU WIN!")

else:
    print("CONGRATS ITS NOT CORRECT! ")
    print("That was a horible guess, people have been better then you.")
    
    

