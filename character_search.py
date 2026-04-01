#WG_CP2 character search for group
#The code for searching though the characters
#from character creator import character return
import matplotlib
import pandas
import faker
#define check character
def check_char(characters):
    while True:
        search_val = input("Do you want to search for? This can be a name, a race, a class, or having a certain number in any attribute. ").strip().lower()

        matched_char = []
        for name, data in characters.items():
            # check name match
            if search_val in name.lower():
                matched_char.append(name)
                continue

            # helper to search nested structures
            def search_in(obj):
                if isinstance(obj, dict):
                    return any(search_in(v) for v in obj.values())
                if isinstance(obj, (list, set, tuple)):
                    return any(search_in(v) for v in obj)
                if isinstance(obj, (int, float)):
                    return search_val == str(obj).lower()
                if isinstance(obj, str):
                    return search_val in obj.lower()
                return False

            if search_in(data):
                matched_char.append(name)

        if not matched_char:
            print(f"No characters found matching '{search_val}'. Try again.")
            continue

        print("Matches:")
        for i, name in enumerate(matched_char, 1):
            print(f"{i}. {name}")

        choice = input("Which character do you want to look at? (type name or number) ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(matched_char):
                return matched_char[idx]
        else:
            if choice in matched_char:
                return choice

        print(f"{choice} is not an option; try again.")

#character search function
def char_search(characters):
    #call check_char with characters argunment, & search value
    check = check_char(characters)
    dict_display(check, characters)
    #ask if they want to exit
    exit = input("Do you want to exit the searching? do not answer until you are done looking over the character. y/n ").strip().lower()
    #if exit is no

    if exit == "n":
        #continue
        char_search(characters)

    #else   
    else:
        #break
        return

#character display function
def _format_item_display(item):
    # item can be dict with 'name' and 'stats', a string, or other dict/list
    if isinstance(item, dict) and 'name' in item and 'stats' in item:
        stats = ", ".join(f"{k}: {v}" for k, v in item['stats'].items())
        return f"{item['name']} — {stats}" if stats else f"{item['name']}"
    if isinstance(item, dict):
        # fallback format
        return ", ".join(f"{k}: {v}" for k, v in item.items())
    return str(item)


def dict_display(key, dic_name):
    # print the dictionary key (e.g., character name)
    print(f"{key}:")
    dic = dic_name[key]
    for i in dic:
        if isinstance(dic[i], dict):
            print(f"{i.capitalize()}:")
            for j in dic[i]:
                value = dic[i][j]
                # Inventory-style entries: item dict, list, or nested dict (attributes)
                if isinstance(value, dict) and 'name' in value and 'stats' in value:
                    print(f"  {j.capitalize()}: {_format_item_display(value)}")
                elif isinstance(value, list):
                    # list of strings or list of item-dicts
                    if value and isinstance(value[0], dict) and 'name' in value[0]:
                        print(f"  {j.capitalize()}: {', '.join(_format_item_display(v) for v in value)}")
                    else:
                        print(f"  {j.capitalize()}: {', '.join(str(v) for v in value) if value else 'None'}")
                elif isinstance(value, dict):
                    # nested attributes dictionary
                    print(f"  {j.capitalize()}:")
                    for k in value:
                        print(f"    {k.capitalize()}: {value[k]}")
                else:
                    print(f"  {j.capitalize()}: {value}")
        elif isinstance(dic[i], list):
            print(f"{i.capitalize()}: {', '.join(str(x) for x in dic[i]) if dic[i] else 'None'}")
        elif isinstance(dic[i], set):
            print(f"{i.capitalize()}: {', '.join(dic[i]) if dic[i] else 'None'}")
        else:
            print(f"{i.capitalize()}: {dic[i]}")

def key_from_value(characters, key_desired):
    for key, value in characters.items():
        if value == key_desired:
            return key

if __name__ == "__main__":
    pass
