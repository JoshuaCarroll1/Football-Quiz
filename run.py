import gspread
import os
import time
import random
from colors import colorama


def opening_logo():
    """
    Logo for opening of game 
    """ 
    print(Back.RED+ "========  ========  ========  ========  ========      ===     ==       ==") 
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==     ==    == ==    ==       ==")
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==     ===  ==   ==   ==       ==")
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==     ==   ==   ==   ==       ==")
    print(Back.RED+ "========  ==    ==  ==    ==     ==     ========    =======   ==       ==")
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==     ==   ==   ==   ==       ==")
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==      ==  ==   ==   ==       ==")
    print(Back.RED+ "==        ==    ==  ==    ==     ==     ==     ==   ==   ==   ==       ==")
    print(Back.RED+ "==        ========  ========     ==     ========    ==   ==   =======  =======/n")
    print(Back.RED+ "========   ==    ==  ======  =======")
    print(Back.RED+ "==    ==   ==    ==    ==         =")
    print(Back.RED+ "==    ==   ==    ==    ==        =")
    print(Back.RED+ "==    ==   ==    ==    ==       =")
    print(Back.RED+ "==    ==   ==    ==    ==      =")
    print(Back.RED+ "==    ==   ==    ==    ==     =")
    print(Back.RED+ "=========  ========  ======  =======/n")   


def clear():
    """
    Clear function to make terminal look cleaner.
    """
    os.system("cls" if os.name == "nt" else "clear")

def game_setup():
    """
    Game start up prior to enetering name.
    """


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