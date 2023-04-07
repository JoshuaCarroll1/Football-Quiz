import gspread
import os
import time
import random
from colors import colorama
from questions import QUESTIONS


def opening_logo():
    """
    Logo for opening of game 
    """ 
    print(Back.RED+ "========  ========  ========  ========  ========      ===     ==       ==") 
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||     ==    || ||    ||       ||")
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||     ===  ||   ||   ||       ||")
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")
    print(Back.RED+ "========  ||    ||  ||    ||     ||     ========    =======   ||       ||")
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||      ==  ||   ||   ||       ||")
    print(Back.RED+ "||        ||    ||  ||    ||     ||     ||     ==   ||   ||   ||       ||")
    print(Back.RED+ "==        ========  ========     ==     ========    ==   ==   =======  =======/n")
    print(Back.RED+ "========   ==    ==  ======  =======")
    print(Back.RED+ "||    ||   ||    ||    ||         ||")
    print(Back.RED+ "||    ||   ||    ||    ||        ||")
    print(Back.RED+ "||    ||   ||    ||    ||       ||")
    print(Back.RED+ "||    ||   ||    ||    ||      ||")
    print(Back.RED+ "||    ||   ||    ||    ||     ||")
    print(Back.RED+ "=========  ========  ======  =======/n")   


def clear():
    """
    Clear function to make terminal look cleaner.
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_setup():
    """
    Game start up prior to entering name.
    """
    print(Fore.GREEN+ "Welcome to the Football Quiz!")
    print(Fore.GREEN+ "Please add your username below!")


def username_setup():
    """
    Add username here.
    """
    username = input("Type name here and click return: ")
    print(Fore.GREEN+ "Hello" + username + ", lets test your ball knowledge!")
    

def validator_username(username_setup):
    """
    Used to validate name has under a certain amount of characters and only uses alphabet
    """    
    if username_setup == '':
        print(Fore.RED+ "No usersname given, please try again/n")
        return False
    elif len(username_setup) > 15:
        print(Fore.RED+ "Usersname given is too long, please try again/n")
        return False
    elif len(username_setup) < 4:
        print(Fore.RED+ "Usersname given is too short, please try again/n")
        return False
    elif username_setup.isalpha():
        print(Fore.RED+ "Usersname given cannot contain letters only!/n")
        return False
      
    else:
        return True


def questions_validator():
    """
    Questions validator to show questions and answers
    """
    print(QUESTIONS)


from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('football_quiz')


def main():
    """
    Main function to run program 
    """
    opening_logo()
    clear()
    game_setup()
    username_setup()
    questions_validator()
    