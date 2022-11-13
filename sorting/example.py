# This is an example of the usage of the sorting.py file

from sorting import *
import os

def askInt(name):
    cont = True
    while cont:
        value = input(f"New {name}: ")
        try:
            value = int(value)
            cont = False
        except:
            print("Value must be an integer, try again.")
    return value
            

def displayHelp():
    help = """
            H   --> Display help
            S   --> Leave programm
            P   --> Edit default values
            B   --> Execute bubble sort
            S   --> Execute selection sort
            D   --> Execute double selection sort
            C   --> Execute cycle sort
            cls --> Clear console
            """
    print(help)

length = 10
min = 0
max = 100

os.system("cls")
isContinuer = True
while isContinuer:
    usrInput = input("Insert command here, 'H' to display help : ").lower()
    array = generateArray(length, min, max)
    
    if usrInput == "h":
        displayHelp()
    elif usrInput == "q":
        isContinuer = False
    elif usrInput == "b":
        print(f"Unsorted array: {array}\nSorted array:   {bubbleSort(array)}")
    elif usrInput == "s":
        print(f"Unsorted array: {array}\nSorted array:   {selectionSort(array)}")
    elif usrInput == "d":
        print(f"Unsorted array: {array}\nSorted array:   {doubleSelectionSort(array)}")
    elif usrInput == "c":
        print(f"Unsorted array: {array}\nSorted array:   {cycleSort(array)}")
    elif usrInput == "p":
        length = askInt("length")
        max = askInt("max")
        min = askInt("min")
    elif usrInput == "cls":
        os.system("cls")
    else:
        print("Unknown command, type 'H' for help : ")