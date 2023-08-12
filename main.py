from wordle import *

wantsToPlay = True
print_msg_box("Welcome to the wordle game!")

while wantsToPlay:
    hasWon = False
    correct_word = random_word()
    round_num = 0
    while not hasWon and round_num < MAX_ROUNDS:
        guess_word = input(f'✏  Guess Word ({round_num+1}/{MAX_ROUNDS}): ').upper()
        if len(guess_word) != WORD_LENGTH or not guess_word.isalpha():
            print('Please enter a 5 letter word.\n')
            continue
        else:
            word(guess_word, correct_word)
            if guess_word == correct_word:
                print_won_msg()
                hasWon = True
            else:
                round_num += 1   
    if not hasWon:
        print_lose_msg(correct_word)
        exit()
    else:
        wantsToPlay = False