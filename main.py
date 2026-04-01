#Import other files for functions
from char_manager import create_character, edit_character
from character_search import char_search
import matplotlib
import pandas
import faker
# tuple of races
    # tuple that contians all available races
race_options = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")

# tuple of classes
    # tuple containing all available classes
class_options = ("Black Mage", "Warrior", "Thief", "White Mage")

# dictionary to contain all characters
characters = {
    # FOR ALL CHARACTERS
    # race and class stored in tuple
    # skills stored a set
    # atributtes in nested dictionary
    # inventory in list
    "example_char" : {
        "race" : ("Dragonborn"),
        "class" : ("White Mage"),
        "level" : 10,
        "atributtes" : {
            "MP" : 1,
            "HP" : 2,
            "Str" : 3,
            "Atk" : 4,
            "Def" : 5,
            "Mag" : 6,
            "Spr" : 7,
            "Acc" : 8,
            "Spd" : 9,
            "Evs" : 10
        },
        "skills" : {"Cure", "Esuna"},
        "inventory" : {
            "weapon" : ["Wand"],
            "armor" : ["Robes"],
            "equipment one" : ["Classic Italian Pizza"],
            "equipment two" : ["Pot of Petunias"],
            "equipment three" : ["Bowling Pin"],
            "equipment four" : ["Sticky Hand"]
        }
    }
}

import sys
#Define main
def main():
    characters_local = characters
    print("Welcome to the RPG Character Manager. You can create, edit, and search for characters here.")
    while True:
        choice = input("What would you like to do?\n1.Create a new character\n2.Edit an already made character\n3.Search through characters\n4.Exit\n")
        if choice == '1':
            characters_local = create_character(characters_local, race_options, class_options)
        elif choice == '2':
            characters_local = edit_character(characters_local)
        elif choice == '3':  
            char_search(characters_local)
        elif choice == '4':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid choice, try again")

#define a function to return characters
def char_return(characters):
    return characters

#Run Main
if __name__ == "__main__":
    main()
