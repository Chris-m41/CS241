import random
from random import randint

rand_num = randint(1, 100)

print("Welcome to the number guessing game!")
my_seed = input("Enter random seed: ")
random.seed(my_seed)
my_seed = rand_num
guessAgain = bool(True)
count = 0
playAgain = "yes"

#Will run so long as the number has not been guessed.
while playAgain == "yes":
    while guessAgain == True:  #Runs until the correct number is guessed
        guess = int(input("Please enter a guess: "))
        count += 1  #Increments by everytime a new guess is made.
        if guess == my_seed:  #If user wins
            guessAgain = bool(False)
            print("Congratulations! You guessed it! ")
            print("It took you {} guesses".format(count))

            playAgain = input("Would you like to play again? (yes/no)\n")
            if playAgain == "yes":  #If user wants to play again
                count = 0
                rand_num = randint(1, 100)  #Creates new random number
                my_seed = rand_num  #Sets seed to new number
                guessAgain = bool(True)  #Will start new game.

       #if number is not guessed correctly, will tell user if the number is higher or lower
        elif guess > my_seed:
            print("Lower\n")
        elif guess < my_seed:
            print("Higher\n")

#if playAgain is answered as "no"
if playAgain == "no":
    print("Thank you. Goodbye.")