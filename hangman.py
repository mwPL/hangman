# Write your code here
import random


def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(words)
    print('H A N G M A N')
    lifes = 8
    progress = list(len(answer) * '-')
    guesses = set()
    while lifes > 0:

        print()
        print(''.join(progress))
        print('Input a letter:', end="")
        letter = input()

        if len(letter) != 1:
            print('You should input a single letter')
        elif not letter.islower():
            print('Please enter a lowercase English letter')
        else:
            if letter in progress:
                print('You\'ve already guessed this letter.')
            elif letter in answer:
                for x, y in enumerate(answer):
                    if y == letter:
                        progress[x] = letter
                guesses.add(letter)
                if '-' not in progress:
                    print('You guessed the word')
                    print('You survived!')
                    exit()
            else:
                if letter in guesses:
                    print("You've already guessed this letter")
                else:
                    print('That letter doesn\'t appear in the word')
                    lifes -= 1
                    guesses.add(letter)
    print('You lost!')


choices =['play', 'exit']
choice = None
while choice not in choices:
    print('Type "play" to play the game, "exit" to quit: ')
    choice = input()
    if choice == 'play':
        game()
    elif choice == 'exit':
        exit()
