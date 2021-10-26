import keyboard
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def select_game_mode():

    print("--------------------------------------------")
    print("|                                          |")
    print("|************SELECT GAME MODE**************|")
    print("|                                          |")
    print("|                                          |")
    print("|    A. Player1    vs.    Computer         |")
    print("|                                          |")
    print("|                                          |")
    print("|    B. Player1    vs.    Player2          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|            [PLEASE SELECT]               |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A or B: ")

def welcome_screen():
    print("--------------------------------------------")
    print("|                                          |")
    print("|    W  E  L  C  O  M  E                   |")
    print("|                                          |")
    print("|       T O                                |")
    print("|                                          |")
    print("|          P  Y  T  H  O  N                |")
    print("|                                          |")
    print("|              C  H  E  C  K  E  R  S !    |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|         [PRESS ENTER TO BEGIN]           |")
    print("|                                          |")
    print("|                                          |")
    print("--------------------------------------------")
    


welcome_screen()
input("")
clear()


def setup_screen():
    
    print("--------------------------------------------")
    print("|                                          |")
    print("|************GAME SETUP MENU:**************|")
    print("|                                          |")
    print("|    A. GAME MODE            [NOT DONE]    |")
    print("|                                          |")
    print("|    B. BOARD SIZE           [NOT DONE]    |")
    print("|                                          |")
    print("|    C. SIDE SELECTION       [NOT DONE]    |")
    print("|                                          |")
    print("|    D. VIEW RULES           [OPTIONAL]    |")
    print("|                                          |")
    print("|    E. PLAY CHECKERS!       [LOCKED]      |")
    print("|                                          |")
    print("|         [PLEASE COMPLETE SETUP]          |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A to E: ")

    if setup.upper() == "A":
        clear()
        sleep(0.5)
        select_game_mode()
    else:
        print("Please make a valid choice")

setup_screen()


def create_board_normal():

    print("                                      ")
    print("--------------------------------------------")
    print("You have chosen Board Size: Standard (8 x 8)")
    print("--------------------------------------------")
    print("                                      ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H")
    print("                                 ")
    print("      0    O  -  &  -  O  -  0  -")
    print("      1    -  O  -  O  -  @  -  O")
    print("      2    O  -  O  -  O  -  O  -")
    print("      3    -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -")
    print("      5    X  -  X  -  X  -  X  -")
    print("      6    -  X  -  X  -  X  -  X")
    print("      7    #  -  X  -  X  -  X  -")
    print("                                      ")


# create_board_normal()


def create_board_large():

    print("                                      ")
    print("-----------------------------------------")
    print("You have chosen Board Size: Large (9 x 9)")
    print("-----------------------------------------")
    print("                                      ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H  I")
    print("                            ")
    print("      0    O  -  O  -  O  -  O  -  O")
    print("      1    -  O  -  O  -  O  -  O  -")
    print("      2    O  -  O  -  O  -  O  -  O")
    print("      3    -  -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -  -")
    print("      5    -  -  -  -  -  -  -  -  -")
    print("      6    -  X  -  X  -  X  -  X  -")
    print("      7    X  -  X  -  X  -  X  -  X")
    print("      8    -  X  -  X  -  X  -  X  -")
    print("                                      ")


# create_board_large()


def create_board_extra_large():

    print("                                         ")
    print("-------------------------------------------------")
    print("You have chosen Board Size: Extra-Large (10 x 10)")
    print("-------------------------------------------------")
    print("                                         ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H  I  J")
    print("                                 ")
    print("      0    O  -  O  -  O  -  O  -  O  -")
    print("      1    -  O  -  O  -  O  -  O  -  O")
    print("      2    O  -  O  -  O  -  O  -  O  -")
    print("      3    -  -  -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -  -  -")
    print("      5    -  -  -  -  -  -  -  -  -  -")
    print("      6    -  -  -  -  -  -  -  -  -  -")
    print("      7    X  -  X  -  X  -  X  -  X  -")
    print("      8    -  X  -  X  -  X  -  X  -  X")
    print("      9    X  -  X  -  X  -  X  -  X  -")
    print("                                      ")


# create_board_extra_large()


