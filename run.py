import gspread
import os
import time
import random
import colorama
from colorama import Fore, Back
from google.oauth2.service_account import Credentials
from questions import QUESTIONS
colorama.init(autoreset=True)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('football_quiz')


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
    print(QUESTIONS)


if __name__ == "__main__":
    """
    Main function to run program
    """
    clear()
    opening_logo()
    game_setup()
    username_setup()
    questions_validator()
