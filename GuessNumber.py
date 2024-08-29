import random  # import the random module to generate a random number
import time  # import the time module to add delays in the game

def intro():
    """
    Introduction function to ask for the player's name and explain the game
    """
    print("May I ask you for your name?")
    name = input()  # ask for the player's name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)  # add a short delay
    print("Go ahead. Guess!")
    return name  # return the player's name

def pick(name, number):
    """
    Main game function to handle the player's guesses
    """
    guessesTaken = 0  # initialize the number of guesses taken
    while guessesTaken < 6:  # loop until the player has made 6 guesses or less
        time.sleep(0.25)  # add a short delay
        enter = input("Guess: ")  # ask for the player's guess
        try:
            # try to convert the input to an integer
            guess = int(enter)
            if guess <= 200 and guess >= 1:  # check if the guess is within the range
                guessesTaken += 1  # increment the number of guesses taken
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    else:
                        break  # exit the loop if the guess is correct
                    if guess != number:
                        time.sleep(0.5)  # add a short delay
                        print("Try Again!")
                else:
                    if guess == number:
                        break  # exit the loop if the guess is correct
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)  # add a short delay
                print("Please enter a number between 1 and 200")
        except ValueError:
            # handle the case where the input is not a number
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"
while playagain.lower() in ["yes", "y"]:  # loop until the player wants to quit
    name = intro()  # get the player's name
    number = random.randint(1, 200)  # generate a random number
    pick(name, number)  # pass the name and number to the pick function
    print("Do you want to play again?")
    playagain = input().lower()  # ask if the player wants to play again
