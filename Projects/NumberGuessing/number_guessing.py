from art import print_art
import sys
import random

def generate_number():
    return random.randint(1,100)


print_art()

number = generate_number()

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
'''while(difficulty:=input("")!=easy or difficulty!=hard)'''
while(difficulty!="easy" and difficulty!="hard"):
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if(difficulty=="easy"):
    attempts=10
elif(difficulty=="hard"):
    attempts=5

while(attempts>0):
    print(f"You have {attempts} attemps remaining to guess the number.")
    guess=input("Make a guess: ")
    while (not guess.isnumeric()):
        guess=input("Make a guess: ")
    guess = int(guess)    
    if(guess==number):
        print("You win")
        break
    elif(guess>number):
        print("Too high.")
    elif(guess<number):
        print("Too low.")
    if(attempts!=1):
        print("Guess again.")
    attempts-=1
if(attempts==0):
    print("You've run out of guesses. You lose")
    print(f"The number you had to find was{number}")
