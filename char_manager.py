# MH 1st character management
import matplotlib.pyplot as plt
import numpy as np
import pandas
import faker
import csv
from skill_stat_manager import setup_char_value, get_stats_for_class
from inventoryWUI import new_inven, edit_inven, migrate_inventories, find_item_by_name
from character_search import check_char, dict_display
from ast import literal_eval

class DataVisulataion:
    def __init__(self):
        pass


    def bar_graph(data):
        name = list(data.keys())
        values = list(data.values())
        fig, axs = plt.subplots(1, figsize=(18, 6), sharey=True)
        axs.bar(name,values)
        plt.show()






class Character:
    def __init__(self, Name, Class, Level, attributes, skills, weapon, armor, equipment):
        self.name = Name
        self.charclass = Class
        self.lvl = Level
        self.attributes = dict(attributes)
        self.skills = skills
        self.weapon = weapon
        self.armor = armor
        self.equipment = equipment

    def attributesep(self):
        for key, value in self.attributes.items():
            print(f"{key} = {value}")


    def display(self):


        print(f"Name: {self.name}\nClass: {self.charclass}\nLevel: {self.lvl}")
        print(f"{self.attributesep()}\nSkills: {self.skills}\nWeapon: {self.weapon}\nArmor: {self.armor}\nEquipment: {self.equipment}\n")


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
            # structured format: {'name': <str>, 'stats': {..}} or None
            "weapon" : find_item_by_name("Wand") or {"name": "Wand", "stats": {}},
            "armor" : find_item_by_name("Robes") or {"name": "Robes", "stats": {}},
            "equipment one" : {"name": "Classic Italian Pizza", "stats": {}},
            "equipment two" : {"name": "Pot of Petunias", "stats": {}},
            "equipment three" : {"name": "Bowling Pin", "stats": {}},
            "equipment four" : {"name": "Sticky Hand", "stats": {}}
        }
    }
}

# ensure older character inventories migrate to new structured format on load
try:
    migrate_inventories(characters)
except Exception as e:
    print(f"Inventory migration failed: {e}")


# tuple of races
    # tuple that contians all available races
race_options = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")

# tuple of classes
    # tuple containing all available classes
class_options = ("Black Mage", "Warrior", "Thief", "White Mage")

# return characters function,takes in character dictionary:
def char_return(characters):
    # returns character dictionary for easy access
    return characters

# Create character function, takes in character dictionary, race tuple, class tuple:
def create_character(races, classes):
    # ask character name (non-empty & unique)
    while True:
        name = input("What is your character's name?\n").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        #if name in character_dictionary:
            print("That name already exists. Choose another.")
            continue
        break
    # choose class
    while True:
        for idx, cls in enumerate(classes, start=1):
            print(f"{idx}. {cls}")
        class_choice = input("Choose a class (enter number)\n")
        if class_choice.isdigit() and 1 <= int(class_choice) <= len(classes):
            class_choice = classes[int(class_choice) - 1]
            break
        print("That is not an option.")

    # choose race
    while True:
        print("\n")
        for idx, rc in enumerate(races, start=1):
            print(f"{idx}. {rc}")
        race_choice = input("Choose a race (enter number)\n")
        if race_choice.isdigit() and 1 <= int(race_choice) <= len(races):
            race_choice = races[int(race_choice) - 1]
            break
        print("That is not an option.")

    # choose level
    while True:
        level = input("What level is your character? (integer >= 1)\n").strip()
        if not level.isdigit():
            print("That is not an option.")
            continue
        level = int(level)
        if level < 1:
            print("Level must be at least 1.")
            continue
        break

    # set base atributtes using skill_stat_manager helper
    attributtes = get_stats_for_class(class_choice, level)
    # start with empty skills set
    skills = set()

    # allow adding starting skills
    print("\nEnter starting skills (one per line). Press Enter on an empty line to finish.")
    while True:
        skill = input('Skill name (or press Enter to finish):\n').strip()
        if not skill:
            break
        skills.add(skill)
        print(f"Added skill: {skill}")

    # set new character inventory with Wills new inventory function and display the character
    weapon, armor, equipment = new_inven(class_choice, name)
    # returns updated character dictionary
    return Character(name, class_choice, level, attributtes, skills, weapon, armor, equipment)

# character editing function, takes in character dictionary:
def edit_character(character_dictionary):
    while True:
        # User chooses character to edit with Warrens search function
        character = check_char(character_dictionary)
        dict_display(character, character_dictionary)
        # ask what they want to edit (inventory, skills, attributes, name)
        to_edit = input("What do you want to edit?\n1. Inventory\n2. Skills\n3. Atributtes\n")
        if to_edit == "1":
            # edit inventory for that character
            character_dictionary = edit_inven(character_dictionary, character, character_dictionary[character]["class"])
        elif to_edit == "2":
            # simple skills add/remove handler
            action = input("Add or remove skill? (add/remove)\n").strip().lower()
            if action == 'add':
                new_skill = input("Skill name?\n")
                character_dictionary[character].setdefault('skills', set()).add(new_skill)
            elif action == 'remove':
                rem = input("Skill name to remove?\n")
                character_dictionary[character].setdefault('skills', set()).discard(rem)
        elif to_edit == "3":
            # edit attributes for that character
            character_dictionary = setup_char_value(character_dictionary, target_name=character)
        else:
            print("Not an option.")

        # ask if they want to keep editing
        while True:
            keep_editing = input("Do you want to keep editing? (Y/N)\n").lower().strip()
            if keep_editing in ("y", "n"):
                break
            else:
                continue
        if keep_editing == "y":
            continue
        else:
            break
    # return the updated dictionary
    return character_dictionary
