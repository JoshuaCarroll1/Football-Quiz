import os
import time
import random
import colorama
from colorama import Fore, Back
from questions import QUESTIONS
colorama.init(autoreset=True)


QUESTIONS_CORRECT = 0
QUESTIONS_INCORRECT = 0


def opening_logo():
    """
    Logo for opening of game
    """
    print(Back.RED + "========  ========  ========  ========  ========      ===     ==       ==")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||     ==    || ||    ||       ||")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||     ===  ||   ||   ||       ||")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")  # noqa
    print(Back.RED + "========  ||    ||  ||    ||     ||     ========    =======   ||       ||")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||      ==  ||   ||   ||       ||")  # noqa
    print(Back.RED + "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")  # noqa
    print(Back.RED + "==        ========  ========     ==     ========    ==   ==   =======  =======")  # noqa
    print("")
    print(Back.RED + "========   ==    ==  ======  =======")
    print(Back.RED + "||    ||   ||    ||    ||         ||")
    print(Back.RED + "||    ||   ||    ||    ||        ||")
    print(Back.RED + "||    ||   ||    ||    ||       ||")
    print(Back.RED + "||    ||   ||    ||    ||      ||")
    print(Back.RED + "||    ||   ||    ||    ||     ||")
    print(Back.RED + "=========  ========  ======  =======")


def clear():
    """
    Clear function to make terminal look cleaner.
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_setup():
    """
    Game start up prior to entering name.
    """
    print(Fore.GREEN + "Welcome to the Football Quiz!")
    print(Fore.GREEN + "Please add your username below!")


def username_setup():
    """
    Add username here.
    """
    while True:
        username = input("Type name here and click return: ")
        if validator_username(username):
            break
    clear()
    print(Fore.GREEN + "Hello" + username + ", lets test your ball knowledge!")


def validator_username(username):
    """
    Used to validate name has under a certain
    amount of characters and only uses alphabet
    """
    if username == '':
        print(Fore.RED + "No usersname given, please try again/n")
        return False
    elif len(username) > 15:
        print(Fore.RED + "Usersname given is too long, please try again/n")
        return False
    elif len(username) < 3:
        print(Fore.RED + "Usersname given is too short, please try again/n")
        return False
    elif not username.isalpha():
        print(Fore.RED + "Usersname given cannot contain letters only!/n")
        return False
    else:
        return True


def questions_validator():
    """
    Questions validator to show questions and answers
    """
    global QUESTIONS_CORRECT
    global QUESTIONS_INCORRECT

    random.shuffle(QUESTIONS)
    questions = QUESTIONS[:10]
    for question in questions:
        print("")
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        print("")
        user_answer = input(f"Select your answer:\n").upper()
        options = ["A", "B", "C", "D"]
        if user_answer not in options:
            print(Fore.RED + "That is not a valid option, try again!")
        if user_answer == question["correct_answer"]:
            QUESTIONS_CORRECT += 1
            print(Fore.GREEN + "That is Correct!")
        else:
            QUESTIONS_INCORRECT += 1
            print(Fore.RED + "That is Incorrect!")
        print("")
        input("Press enter to continue")
        clear()


def end_game():
    """
    End of game text with result
    """
    print(Fore.GREEN + f"Great job {USERNAME}, you got a score of {QUESTIONS_CORRECT}!")
    print(Fore.RED + f"You got {QUESTIONS_INCORRECT} incorrect.\n")
    print(Fore.GREEN + "Would you like to play again?")


def replay_game()
    """
    Yes or No on whether the user wouldl ike to play again
    """


if __name__ == "__main__":
    """
    Main function to run program
    """
    clear()
    opening_logo()
    game_setup()
    username_setup()
    questions_validator()
    final_score()
    end_game()
    replay_game()