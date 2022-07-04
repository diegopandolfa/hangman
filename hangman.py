"""
Hangman implementation based on version of Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 

@editedBy: Diego Pandolfa
@updateAt: 01-07-2022
@course: TICS100
@section: 3
@university: UAI
@brief: TICS100 Final Project where we added a realtime graphic visualization to Hangman game of Kylie Ying using OpenCV.
        Also we changed the hangman default visual and we added one lives more.
        The images used in this custom hangman was taken to google images and then these were edited with paint.net
@video: https://youtu.be/xk-Q-H0B-Ws
@github: https://github.com/diegopandolfa/hangman.git
"""

import random
from words import words
from hangman_visual import lives_visual_dict
import string
import cv2 as cv # importing opencv with cv alias

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper() # return one word with only mayus characters

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 8 # game start with 8 lives

    img = cv.imread(f'start.jpg') # loading initial image to show as game presentation
    cv.imshow("hangman game", img) # showing initial image with window name as "hangman game" 
    cv.waitKey(5000) # waiting for 5 seconds with game presentation

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])

        #loading corresponding image according to lives left. Also we add printed messeges from terminal to image in the position (15, 600) in color black (0,0,0)
        img = cv.imread(f'{lives}.jpg')
        cv.putText(img, f"You have {lives} lives left and you have used these letters:", (15,600), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
        cv.putText(img, f"{' '.join(used_letters)}", (15,615), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,125,40), 1, cv.LINE_AA)
        cv.putText(img, f"{' '.join(word_list)}", (15,650), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)
        cv.imshow("hangman game", img)
        cv.waitKey(1)
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter [press enter]: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                # We add printed messeges from terminal to image
                cv.putText(img, f'Your letter, {user_letter} is not in the word', (15,550), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv.LINE_AA)
                cv.imshow("hangman game", img)
                cv.waitKey(1250)
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            # We add printed messeges from terminal to image
            cv.putText(img, f'You have already used that letter. Guess another letter.', (15,550), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv.LINE_AA)
            cv.imshow("hangman game", img)
            cv.waitKey(1250)
            print('\nYou have already used that letter. Guess another letter.')

        else:
            # We add printed messeges from terminal to image
            cv.putText(img, f'That is not a valid letter.', (15,550), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv.LINE_AA)
            cv.imshow("hangman game", img)
            cv.waitKey(1250)
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        # We add printed messeges from terminal to image, in this case you died
        img = cv.imread(f'{lives}.jpg')
        cv.putText(img, f'You died, sorry. The word was {word}', (15,650), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv.LINE_AA)
        cv.imshow("hangman game", img)
        cv.waitKey(5000)
        print('You died, sorry. The word was', word)
    else:
        # We add printed messeges from terminal to image, in this case you win
        img = cv.imread(f'winner.jpg')
        cv.putText(img, f'YAY! You guessed the word {word}!!', (15,650), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv.LINE_AA)
        cv.imshow("hangman game", img)
        cv.waitKey(5000)
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
