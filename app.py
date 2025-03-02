#import libraries

import random
from words import word_list
from art import logo, stages

end_of_game = False
chosen_word = random.choice(word_list)   #for choosing random word from word_list
lives = 6




print(logo)



#creating blanks
display=[]
for _ in range(len(chosen_word)):
    display+="_"

#either user wins, user looses the game
while not end_of_game:
    #user make a guess
    guess=input("Guess a letter. ").lower()
    if guess in display:
        print("you have already guessed this letter")

    #guess n , funny 