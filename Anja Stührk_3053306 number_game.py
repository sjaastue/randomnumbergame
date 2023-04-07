
import random # imports the random module
import time # imports the time module

from winsound import Beep # imports the winsound module and from the winsound the beep sound
sounds = {"A": 500,
         "B": 750,
         "C": 1000,
         "D": 1250} # assigns a number in the unit hertz to the variable A, B, C and D

randomnumber = random.randint(1, 100) #generates a random number between 1 and 100 inclusive

guesses = 0 # the variable for counting the guesses
aktiv = True # sets the variable aktiv as True
start_time = time.time() # calculates the current time in seconds and saves it as the start_time

name_user = input("Please enter your name: ")
print("Hello " + name_user + ". Welcome to the random number game!")

while aktiv:
    guesses += 1 # adds a guess to the count
    
    while True: # This while loop checks if the user has entered a number, if not then the user is asked again until a number is entered
        try:
            guessnumber = int(input("Please guess the random number (Enter 0 to quit the game): ")) # asks the user to enter a number and gives the infomation about quitting the game
            break # ends the while loop
        except ValueError: # the Error for incorrect value
            print("Please enter a number.")
        
    if guessnumber == 0: # the if statement for ending the game 
        sound_end = "DCBA" # defines the order of the variables
        for sound in sound_end:
            Beep(sounds[sound], 100) # for loop that iterats through sounds and searchs for the right one in sound_end and with 1000 milliseconds
        print("End of game")
        break

    if randomnumber == guessnumber: # the if statement for guessing the random number 
        print("You guessd the right number!")
        aktiv = False # breaks up the while loop
        time_dif = time.time()-start_time #calculates the current time in seconds and subtracts it from the start time
        
        sound_rigth_guess = "ABCD"
        for sound in sound_rigth_guess:
            Beep(sounds[sound], 100)

        print("The random number was: " + str(randomnumber) + ". You got it in "+ str(guesses) + " guesses and it took you " + str(round(time_dif, 2)) + " seconds.")
        break

    elif randomnumber < guessnumber: # the if statement for an entry of a number that is too high 
        print("Your guessed number was too high.")

    elif randomnumber > guessnumber: # the if statement for an entry of a number that is too low 
        print("Your guessed number was too low.")





