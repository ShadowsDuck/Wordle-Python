import random
import pathlib

MAX_ROUNDS = 6
WORD_LENGTH = 5

def random_word():
    WORDLIST = pathlib.Path("words.txt")
    words = [word.upper() for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")]
    return random.choice(words)

def display_positions(guess_word, positions):
    guess_word_positions = ' | '.join(['', *guess_word, '']).strip()
    right_position = ' | '.join(['', *positions, '']).strip()
    return guess_word_positions+"\n―――――――――――――――――――――\n"+right_position

def display_game_status(correct_letters, misplaced_letters, wrong_letters):
    print("• Right letters in the correct position:", sorted(correct_letters))
    print("• Right letters in the wrong position:", sorted(misplaced_letters))
    print("• Letters not present in the word:", sorted(wrong_letters))
    print()
    
def add_misplaced_letters(guess_word, correct_word, correct_letters):
    new_misplaced_letters = []
    for char in guess_word:
        count = correct_letters.count(char) + new_misplaced_letters.count(char)
        if (char in correct_word and count < correct_word.count(char)
                and count < guess_word.count(char)):
            new_misplaced_letters.append(char)
    return new_misplaced_letters
    
def update_positions(guess_word, correct_word):
    new_positions = []
    for letter, correct in zip(guess_word, correct_word):
        if letter == correct:
            new_positions.append(letter)
        else:
            new_positions.append('_')
    return new_positions

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
        box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
        if title:
            box += f'║{space}{title:<{width}}{space}║\n'  # title
            box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
        box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
        box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
        print(box)

def print_won_msg():
    print('✅ GOOD, You Win! 😃')
    
def print_lose_msg(correct_word):
    print('❎ Sorry, You Lose! 😢')
    print('Correct Answer is ' + correct_word)
    
wrong_letters = []
def word(guess_word, correct_word):
    positions = ['_' for _ in range(WORD_LENGTH)]
    correct_letters = []
    misplaced_letters = []
    global wrong_letters

    correct_letters = [letter for letter, correct in zip(guess_word, correct_word) if letter == correct]
    misplaced_letters = add_misplaced_letters(guess_word, correct_word, correct_letters)
    wrong_letters += set(guess_word) - set(correct_word)

    positions = update_positions(guess_word, correct_word)
    print_msg_box(display_positions(guess_word, positions))
        
    display_game_status(correct_letters, misplaced_letters, set(wrong_letters))
