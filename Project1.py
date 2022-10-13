import numpy as np
import pandas as pd

#global data



def inputNumber(prompt):
# INPUTNUMBER Prompts user to input a number
#
# Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))  
            break
        except ValueError:
            pass
    return num

def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
#
# Usage: choice = displayMenu(options)
#
# Input options Menu options (array of strings)
# Output choice Chosen option (integer)
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
# Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice


def load_data(dataname):
    global data

    try:
        data = pd.read_csv(dataname)
        print("File loaded succesfully!")
    except OSError as e:
        print("\n404 FILE NOT FOUND! TRY ANOTHER FILENAME\n")



def menu():
    menuItems = np.array(["Enter txt file", "Display First line", "Quit"])
    name = ""

    while True:
        # Display menu options and ask user to choose a menu item
        print("MENU")
        choice = displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Enter name
        if choice == 1:
        # Ask user to input name and save it in variable
            name = input("Please enter name of file: ")
            load_data(name)
        # ------------------------------------------------------------------
        # 2. Display greeting
        elif choice == 2:
        # Is name empty?
            if data is None:
        # Display error message
                print("Error: empty file")
            else:
        # Display greeting
                print(data)
        # ------------------------------------------------------------------
        # 3. Quit
        elif choice == 3:
        # End
            break

menu()