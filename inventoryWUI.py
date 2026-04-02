# WM 1st pseudocode
import matplotlib
import pandas
import faker
#UI
    #Create a function for the main interface, just named main()
    #Have it greet them to the program.
    #Start a while true loop that will keep the code going until the user chooses to exit.
    #They will be asked what they want to do, 1.Make a character 2.Edit a character 3.Search for a character 4.Exit
    #Each option will call a different funtion



#Inventory
    #Make a dictionary for the items in the game, split into several pieces.
    #It would start with a split between weapons, equipment, and armor.
        #The weapons would then seperate based on class restrictions
            #Then each weapon would have its own stats
        #The equipment would be split into ones with one stat increased, two stats, and three stats.
            #There will be one for each of the one stat, but the two and three stats would only be with ones that make sense.
        #Armor would also be class restricted, based on what was choosen in creator.
            #There would be a few options for each class, with them affecting defense, evasion, speed, and spirit differently
    #Make a function for creating a character inventory.

items = {
    'Warrior':{
        'Armor':{
            'Chainmail':{
                'Defence':20,
                'Speed':0,
            },
            'Platemail':{
                'Defence':40,
                'Speed':-2,

            },
            'Platemail and Chainmail':{
                'Defence':60,
                'Speed':-3,

            }
        },
        'Weapons':{
            'Shortsword':{
                'Attack':20,
                'Accuracy':5,
                'Speed':2,

            },
            'Longsword':{
                'Attack':25,
                'Accuracy':0,
                'Speed':0,

            },
            'Greatsword':{
                'Attack':50,
                'Accuracy':-5,
                'Speed':-4,


            }
        }
    },
    'Thief':{
        'Armor':{
            'Cloth':{
                'Defence':5,
                'Speed':10,
            },
            'Leather':{
                'Defence':10,
                'Speed':6,
            },
            'Padded Leather':{
                'Defence':15,
                'Speed':4,
            }

        },
        'Weapons':{
            'Knife':{
                'Attack':15,
                'Accuracy':10,
                'Speed':2,


            },
            'Blowgun':{
                'Attack':10,
                'Accuracy':15,
                'Speed':4,
                'Evasion':5


            },
            'Shuriken':{
                'Attack':5,
                'Accuracy':20,
                'Speed':5,
                'Evasion':15


            }
        }
    },
    'Mage':{
        'Armor':{
            'Robes':{
                'Spirit':20,
                'Speed':2,
            },
            'Padded Robes':{
                'Defence':10,
                'Spririt':15,
                'Speed':0,
            },
            'Enhanced Robes':{
                'Spirit':30,
                'Speed':0,
            }
        },
        'Weapons':{
            'Shortstaff':{
                'Magic':20,
                'Speed':2,
            },
            'Wand':{
                'Magic':10,
                'Speed':4,
                'Evasion':5
            },
            'Longstaff':{
                'Magic':40,
                'Speed':-3,

            },
            
        }
    },
    'Equipment':{
        #Each be a 30 increase
        'One':{
            'Mana Ring':{
                'Mana':30
            },
            'Life Earring':{
                'Health':30
            },
            'Strength Armlet':{
                'Strength':30
            },
            'Attack Glove':{
                'Attack':30
            }, 
            'Defence Pauldron':{
                'Defence':30
            },
            'Magical Catalyst':{
                'Magic':30
            },
            'Spiritual Runes':{
                'Spiritual':30
            },
            'Focus Ring':{
                'Accuracy':30
            },
            'Falcon Feather':{
                'Speed':30
            },
            'Rabbits Foot':{
                'Evasion':30
            },
        },
        #each be a 20 increase
        'Two':{
            'Mana Tome':{
                'Mana':20,
                'Magic':20
            },
            'Mana Glove':{
                #Magic and spirit
                'Spirit':20,
                'Mana':20
            },
            'Healthy Armlet':{
                #Strength and life
                'Strength':20,
                'Life':20
            },
            'Life Bracer':{
                #Life and defence
                'Life':20,
                'Defence':20
            },
            'Titans Glove':{
                #Strength and attack
                'Strength':20,
                'Attack':20
            },
            'Strength Bracer':{
                #Strength and defence
                'Strength':20,
                'Defence':20
            },
            'Spiritual Pauldron':{
                #Defence and spirit
                'Defence':20,
                'Spirit':20
            },
            'Spiritual Tome':{
                #Magic and spirit
                'Spirit':20,
                'Magic':20
            },
            'Focus Feather':{
                #Accuracy and speed
                'Accuracy':20,
                'Speed':20
            },
            'Jackalope Foot':{
                'Speed':20,
                'Evasion':20
            },

        },
        #Each be a 15 increase
        'Three':{
             'Titans Bracer':{
                  #atk str hp
                  'Attack':15,
                  'Strength':15,
                  'Health':15
             },
             'Ancient Tome':{
                  #mp magic spirit
                  'Mana':15,
                  'Magic':15,
                  'Spirit':15
             },
             "Theifs Charm":{
                  #spd evasion acc
                  'Speed':15,
                  'Evasion':15,
                  'Accuracy':15
             }

        }
    }
}

def _format_stats(stats):
    if not stats:
        return ""
    return ", ".join(f"{k}: {v}" for k, v in stats.items())


def _format_item_line(name, stats):
    formatted = _format_stats(stats)
    return f"{name} — {formatted}" if formatted else name


def _print_menu(items_dict):
    for idx, name in enumerate(items_dict.keys(), start=1):
        print(f"{idx}. {_format_item_line(name, items_dict[name])}")


def _choose_item_from(items_dict, prompt="Choose an item (number, 's' to search, 'c' to cancel, or exact name):\n"):
    names = list(items_dict.keys())
    if not names:
        print("No items available to choose from.")
        return None
    attempts = 0
    max_attempts = 6
    while attempts < max_attempts:
        _print_menu(items_dict)
        choice = input(prompt).strip()
        if not choice:
            print("Enter a number, 's' to search, 'c' to cancel, or exact name.")
            attempts += 1
            continue
        if choice.lower() == 'c':
            return None
        # number selection
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(names):
                return names[idx]
            print("That number is not an option.")
            attempts += 1
            continue
        # search helper
        if choice.lower() == 's':
            term = input("Search term:\n").strip().lower()
            matches = [n for n in names if term in n.lower()]
            if not matches:
                print("No matches.")
                attempts += 1
                continue
            for i, nm in enumerate(matches, 1):
                print(f"{i}. {_format_item_line(nm, items_dict[nm])}")
            sel = input("Enter number to choose, 'c' to cancel, or press Enter to cancel:\n").strip()
            if sel.lower() == 'c' or sel == '':
                attempts += 1
                continue
            if sel.isdigit() and 1 <= int(sel) <= len(matches):
                return matches[int(sel) - 1]
            print("Invalid selection.")
            attempts += 1
            continue
        # exact name (case insensitive)
        for nm in names:
            if choice.lower() == nm.lower():
                return nm
        print("Invalid choice. Enter a number, 's' to search, 'c' to cancel, or exact name.")
        attempts += 1
    print("Too many invalid attempts. Cancelled.")
    return None


_num_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


def find_item_by_name(name):
    """Return {'name', 'stats'} for a matching item name (case-insensitive), or None if not found."""
    if not name or not isinstance(name, str):
        return None
    target = name.strip().lower()
    # check weapons and armor per class
    for cls in ('Warrior', 'Thief', 'Mage'):
        for k, v in items[cls]['Weapons'].items():
            if k.lower() == target:
                return {'name': k, 'stats': v}
        for k, v in items[cls]['Armor'].items():
            if k.lower() == target:
                return {'name': k, 'stats': v}
    # equipment categories
    for cat in ('One', 'Two', 'Three'):
        for k, v in items['Equipment'][cat].items():
            if k.lower() == target:
                return {'name': k, 'stats': v}
    return None


def migrate_inventories(characters):
    """Migrate inventory entries stored as lists/strings into structured format {'name','stats'}.
    Unknown items are preserved as {'name': <name>, 'stats': {}} so they still print nicely.
    """
    changed = 0
    for cname, cdata in characters.items():
        inv = cdata.setdefault('inventory', {})
        for slot, val in list(inv.items()):
            # skip already structured items
            if isinstance(val, dict) and 'name' in val and 'stats' in val:
                continue
            # skip explicit None
            if val is None:
                continue
            item_name = None
            if isinstance(val, (list, tuple)) and val:
                # take first element
                item_name = val[0]
            elif isinstance(val, str):
                item_name = val
            else:
                # unexpected structure: skip
                continue
            if not item_name:
                inv[slot] = None
                changed += 1
                continue
            found = find_item_by_name(item_name)
            if found:
                inv[slot] = {'name': found['name'], 'stats': found['stats']}
            else:
                # preserve unknown item name with empty stats so it prints
                inv[slot] = {'name': item_name, 'stats': {}}
            changed += 1
    if changed:
        print(f"Migrated {changed} inventory entries to structured format.")
    return characters


def new_inven(char_class, char_name):
    # Normalize incoming class name to our item categories
    if char_class in ("Black Mage", "White Mage"):
        internal_class = 'Mage'
    elif char_class == 'Thief':
        internal_class = 'Thief'
    else:
        internal_class = 'Warrior'

    print("\n--- Inventory Setup ---\n")

    # Weapon
    print("Choose your weapon:")
    while True:
        weapon = _choose_item_from(items[internal_class]['Weapons'], "Choose a weapon (number, 's' to search, 'c' to cancel, or exact name):\n")
        if weapon is None:
            again = input("No selection made. Retry choosing weapon? (y/n)\n").strip().lower()
            if again == 'y':
                continue
            else:
                print("Weapon selection skipped.")
                weapon_select = None
                break
        # valid selection
        weapon_select = {'name': weapon, 'stats': items[internal_class]['Weapons'][weapon]}
        print(f"Selected: {_format_item_line(weapon, items[internal_class]['Weapons'][weapon])}\n")
        break

    # Armor
    print("Choose your armor:")
    while True:
        armor = _choose_item_from(items[internal_class]['Armor'], "Choose armor (number, 's' to search, 'c' to cancel, or exact name):\n")
        if armor is None:
            again = input("No selection made. Retry choosing armor? (y/n)\n").strip().lower()
            if again == 'y':
                continue
            else:
                print("Armor selection skipped.")
                armor_selection = None
                break
        armor_selection = {'name': armor, 'stats': items[internal_class]['Armor'][armor]}
        print(f"Selected: {_format_item_line(armor, items[internal_class]['Armor'][armor])}\n")
        break

    # Equipment - 4 slots
    equipment = {}
    for slot_idx in range(1, 5):
        print(f"Choose equipment slot {slot_idx} (choose category) or enter 's' to skip slot:")
        while True:
            print("1. One stat\n2. Two stats\n3. Three stats\n")
            slot_level = input("Enter 1/2/3 (or 's' to skip this slot):\n").strip()
            if slot_level.lower() == 's':
                slot_name = f"equipment {_num_to_word[slot_idx]}"
                equipment[slot_name] = None
                print(f"Skipped {slot_name}.\n")
                break
            if slot_level not in ('1', '2', '3'):
                print("Invalid choice; enter 1, 2, 3, or 's' to skip.")
                continue
            slot_key = 'One' if slot_level== '1' else ('Two' if slot_level == '2' else 'Three')
            chosen = _choose_item_from(items['Equipment'][slot_key], "Choose equipment (number, 's' to search, 'c' to cancel, or exact name):\n")
            if chosen is None:
                skip = input("No selection made. Skip this equipment slot? (y/n)\n").strip().lower()
                if skip == 'y':
                    slot_name = f"equipment {_num_to_word[slot_idx]}"
                    equipment[slot_name] = None
                    print(f"Skipped {slot_name}.\n")
                    break
                else:
                    print("Retrying equipment selection.")
                    continue
            slot_name = f"equipment {_num_to_word[slot_idx]}"
            equipment[slot_name] = {'name': chosen, 'stats': items['Equipment'][slot_key][chosen]}
            print(f"Selected: {_format_item_line(chosen, items['Equipment'][slot_key][chosen])}\n")
            break

    print("Your inventory has been completed.\n")
    return weapon_select, armor_selection, equipment


def edit_inven(char_dict, char_name, char_class):
    # Normalize incoming class name to our item categories
    if char_class in ("Black Mage", "White Mage"):
        internal_class = 'Mage'
    elif char_class == 'Thief':
        internal_class = 'Thief'
    else:
        internal_class = 'Warrior'

    while True:
        choice = input('What slot would you like to edit?\n1. Weapon\n2. Armor\n3. Equipment\n4. Exit\n')
        if choice == '1':
            print("Choose a new weapon:")
            weapon = _choose_item_from(items[internal_class]['Weapons'], "Choose a weapon (number, 's' to search, 'c' to cancel, or exact name):\n")
            if weapon is None:
                print("No changes made to weapon.")
            else:
                char_dict.setdefault(char_name, {}).setdefault('inventory', {})['weapon'] = {'name': weapon, 'stats': items[internal_class]['Weapons'][weapon]}
                print(f"Weapon set to: {_format_item_line(weapon, items[internal_class]['Weapons'][weapon])}\n")
            again = input("Would you like to change more? (y/n)\n").strip().lower()
            if again == 'y':
                continue
            return char_dict
        elif choice == '2':
            print("Choose a new armor:")
            armor = _choose_item_from(items[internal_class]['Armor'], "Choose armor (number, 's' to search, 'c' to cancel, or exact name):\n")
            if armor is None:
                print("No changes made to armor.")
            else:
                char_dict.setdefault(char_name, {}).setdefault('inventory', {})['armor'] = {'name': armor, 'stats': items[internal_class]['Armor'][armor]}
                print(f"Armor set to: {_format_item_line(armor, items[internal_class]['Armor'][armor])}\n")
            again = input("Would you like to change more? (y/n)\n").strip().lower()
            if again == 'y':
                continue
            return char_dict
        elif choice == '3':
            while True:
                slot = input("Which slot? One, Two, Three, Four\n").strip().lower().capitalize()
                if slot not in ('One', 'Two', 'Three', 'Four'):
                    print("Invalid slot name. Use One/Two/Three/Four.")
                    continue
                cat_choice = input("1 stat, 2 stats, or 3 stats? (or 's' to clear slot)\n").strip()
                if cat_choice.lower() == 's':
                    slot_key = f"equipment {slot.lower()}"
                    char_dict.setdefault(char_name, {}).setdefault('inventory', {})[slot_key] = None
                    print(f"{slot_key} cleared.")
                    again = input("Would you like to change more? (y/n)\n").strip().lower()
                    if again == 'y':
                        break
                    else:
                        return char_dict
                if cat_choice not in ('1', '2', '3'):
                    print("Invalid choice; enter 1, 2 or 3.")
                    continue
                cat_key = 'One' if cat_choice == '1' else ('Two' if cat_choice == '2' else 'Three')
                print(f"Choosing from category: {cat_key}")
                chosen = _choose_item_from(items['Equipment'][cat_key], "Choose equipment (number, 's' to search, 'c' to cancel, or exact name):\n")
                slot_key = f"equipment {slot.lower()}"
                if chosen is None:
                    cont = input("No selection made. Retry or clear this slot? (retry/clear)\n").strip().lower()
                    if cont == 'clear':
                        char_dict.setdefault(char_name, {}).setdefault('inventory', {})[slot_key] = None
                        print(f"{slot_key} cleared.")
                        again = input("Would you like to change more? (y/n)\n").strip().lower()
                        if again == 'y':
                            break
                        else:
                            return char_dict
                    else:
                        continue
                # chosen valid
                char_dict.setdefault(char_name, {}).setdefault('inventory', {})[slot_key] = {'name': chosen, 'stats': items['Equipment'][cat_key][chosen]}
                print(f"{slot_key} set to: {_format_item_line(chosen, items['Equipment'][cat_key][chosen])}\n")
                again = input("Would you like to change more? (y/n)\n").strip().lower()
                if again == 'y':
                    break
                else:
                    return char_dict
        elif choice == '4':
            return char_dict
        else:
            print("Not an option.")

        #It will search for keywords like warrior or mage in their class and mark variables as true where needed.
        #It will print all the valid items for them
        #It would start with weapons and the armor, and then finally do equipment. a variable would keep track of how many equipment they choose, so it will end when they get all 4.
        #All of these would loop until a variable for each becomes true, and lets it move on.
        #It would finally return the character dictionary at the end.
        #When they choose an item, it will use that to search for the item, and if it exists, it will append it to the character dictionaray.
    #Make a fucntion for editing an already made character
