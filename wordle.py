import random
import pathlib
from colorama import init, Fore
init(autoreset=True)

MAX_ROUNDS = 6
WORD_LENGTH = 5

def random_word():
    WORDLIST = pathlib.Path("words.txt")
    words = [word.upper() for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")]
    return random.choice(words)

new_guess_word = []
def display_positions(guess_word, correct_letters, misplaced_letters):
    txt = ''
    for i in range(len(guess_word)):
        if correct_letters[i] != '*':
            txt += f"{Fore.GREEN}{correct_letters[i]} "
        elif misplaced_letters[i] != '*':
            txt += f"{Fore.YELLOW}{misplaced_letters[i]} "
        else:
            txt += f"{Fore.RED}{guess_word[i]} "
    new_guess_word.append(txt)
    
    # Create BOX
    print(Fore.LIGHTMAGENTA_EX + "}==========={")
    for i in range(len(new_guess_word)):
        print(Fore.LIGHTMAGENTA_EX + f"| {Fore.RESET + new_guess_word[i] + Fore.LIGHTMAGENTA_EX}|")
    print(Fore.LIGHTMAGENTA_EX + "}==========={")
    
def add_correct_letters(guess_word, correct_word):
    new_correct_letters = []
    for guess_letter, correct_letter in zip(guess_word, correct_word):
        if guess_letter == correct_letter:
            new_correct_letters.append(guess_letter)
        else:
            new_correct_letters.append('*')
    return new_correct_letters

def add_misplaced_letters(guess_word, correct_word, correct_letters):
    new_misplaced_letters = []
    for i, char in enumerate(guess_word):
        count = correct_letters.count(char) + new_misplaced_letters.count(char)
        if (char in correct_word and count < min(correct_word.count(char),guess_word.count(char))
                and correct_letters[i] != char):
            new_misplaced_letters.append(char)
        else:
            new_misplaced_letters.append('*')
    return new_misplaced_letters

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
    print('Correct Answer is ' + Fore.GREEN + correct_word)
    
wrong_letters = []
def word(guess_word, correct_word):
    correct_letters = []
    misplaced_letters = []
    global wrong_letters

    correct_letters = add_correct_letters(guess_word, correct_word)
    misplaced_letters = add_misplaced_letters(guess_word, correct_word, correct_letters)
    wrong_letters += set(guess_word) - set(correct_word)

    display_positions(guess_word, correct_letters, misplaced_letters)