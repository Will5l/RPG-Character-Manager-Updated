#BB 1st RPG Character Manager Project
# char_return will be imported inside setup_char_value to avoid circular import
import matplotlib
import pandas
import faker
# Characters starting stats are in nested dictionary and available module-wide
CHAR_TABLE = {

    'Black Mage': {
        'Stats': {
            'MP': 15, 'HP': 50, 'Str': 0, 'Atk': 0, 'Def': 5,
            'Mag': 10, 'Spr': 9, 'Acc': 0, 'Spd': 25, 'Evs': 30, 'Lvl': 1
        },

        'Atributes': {
            # Fire line
            'Fire':      [1, 4],
            'Fira':      [15, 10],
            'Firaga':    [30, 20],

            # Blizzard line
            'Blizzard':  [1, 4],
            'Blizzara':  [17, 10],
            'Blizzarga': [35, 20],

            # Thunder line
            'Thunder':   [1, 4],
            'Thundera':  [18, 10],
            'Thunderga': [40, 20],

            # Status spells
            'Poison':    [5, 10],
            'Blind':     [6, 12],
            'Silence':   [7, 10],

            # General skills
            'Item':      [1, 0],
            'Defend':    [1, 0]
        }
    },

    'Warrior': {
        'Stats': {
            'MP': 10, 'HP': 80, 'Str': 10, 'Atk': 7, 'Def': 10,
            'Mag': 0, 'Spr': 3, 'Acc': 70, 'Spd': 15, 'Evs': 15, 'Lvl': 1
        },

        'Atributes': {
            'Jump':     [21, 10],
            'Defender': [1, 0],

            # General skills
            'Attack':   [1, 0],
            'Item':     [1, 0],
            'Defend':   [1, 0]
        }
    },

    'Thief': {
        'Stats': {
            'MP': 5, 'HP': 60, 'Str': 5, 'Atk': 9, 'Def': 7,
            'Mag': 0, 'Spr': 6, 'Acc': 65, 'Spd': 25, 'Evs': 25, 'Lvl': 1
        },

        'Atributes': {
            'Steal': [1, 0],
            'Mug':   [30, 0],
            'Taunt': [15, 0],
            'Cheer': [21, 0],

            # General skills
            'Attack': [1, 0],
            'Item':   [1, 0],
            'Defend': [1, 0]
        }
    },

    'White Mage': {
        'Stats': {
            'MP': 15, 'HP': 50, 'Str': 5, 'Atk': 5, 'Def': 5,
            'Mag': 10, 'Spr': 9, 'Acc': 40, 'Spd': 25, 'Evs': 30, 'Lvl': 1
        },

        'Atributes': {
            # Cure line
            'Cure':    [7, 6],
            'Cura':    [20, 12],
            'Curaga':  [40, 25],

            # Life line
            'Life':      [25, 15],
            'Full Life': [50, 35],

            # Status heal
            'Esuna':   [15, 10],

            # General skills
            'Attack': [1, 0],
            'Item':   [1, 0],
            'Defend': [1, 0]
        }
    }
}


def get_stats_for_class(clas, level=1):
    """Return a dict of stats adjusted for level for class `clas`."""
    base = CHAR_TABLE[clas]['Stats']
    # compute level increases similarly to original logic
    final = {}
    for stat, value in base.items():
        if stat == 'Lvl':
            final['Lvl'] = base['Lvl'] + (int(level) - 1)
        else:
            increase = int(value * 0.1 * (int(level) - 1))
            final[stat] = value + increase
    return final


def make_stat_modifier(bonuses):
    """Closure factory that returns a function applying `bonuses` to a stats dict.

    The returned function takes a stats dict and returns a new dict where each stat
    in `bonuses` is added to the corresponding value (missing stats are treated as 0).
    The bonuses are captured (copied) when the closure is created so later changes to
    the original `bonuses` object do not affect the modifier.
    """
    # copy to freeze captured values
    captured = dict(bonuses)

    def apply_modifier(stats):
        new = dict(stats)
        for k, v in captured.items():
            new[k] = new.get(k, 0) + v
        return new

    return apply_modifier


def setup_char_value(characters, target_name=None):

    # Stores manual stat edits
    added_dic = {
        'Stats': {'MP': 0, 'HP': 0, 'Str': 0, 'Atk': 0, 'Def': 0,
                  'Mag': 0, 'Spr': 0, 'Acc': 0, 'Spd': 0, 'Evs': 0, 'Lvl': 0}
    }

    # Stores level‑based stat increases
    level_dic = {
        'Stats': {'MP': 0, 'HP': 0, 'Str': 0, 'Atk': 0, 'Def': 0,
                  'Mag': 0, 'Spr': 0, 'Acc': 0, 'Spd': 0, 'Evs': 0}
    }

    #While editing
    while True:

        char = characters

        if target_name:
            name = target_name
            if name not in char:
                print("Character not found.")
                return char
        else:
            name = input('Who are you editing? \n>')
            if name not in char:
                print("Character not found.")
                continue

        clas = char[name]['class']

        #Player chooses single or all stat editor
        choice = input('Do you want to: \n1. Edit single stat\n2. Edit level\n3. Edit attributes\n> ')

        #Multiply by level function:
        def mult_level(): 
            new_level = int(input("What is the character Level?\n> "))
            base_stats = CHAR_TABLE[clas]['Stats']

            # calculate level-based increases
            for stat, value in base_stats.items():
                if stat == "Lvl":
                    continue
                increase = int(value * 0.1 * (new_level - 1))
                level_dic['Stats'][stat] = increase

            # store new level difference
            added_dic['Stats']['Lvl'] = new_level - base_stats['Lvl']

            # unlock skills
            print("\nChecking for new skills...")
            for skill, data in CHAR_TABLE[clas]['Atributes'].items():
                required_level = data[0]
                if new_level >= required_level:
                    print(f"Unlocked: {skill} (requires Lvl {required_level})")

        #Single stat Function: 
        def add_single():
            stat_chose = input('What stat will you edit?\n> ')

            if stat_chose not in added_dic['Stats']:
                print("Invalid stat.")
                return

            while True: 
                amount = input('How much?\n> ')
                try:
                    amount = int(amount)
                    break
                except ValueError: 
                    print('try again')

            added_dic['Stats'][stat_chose] += amount

        #Choice to add/remove character skills
        def edit_attributes():
            print("Current skills:")
            for skill in CHAR_TABLE[clas]['Atributes']:
                print("-", skill)

            action = input("Add or remove?\n> ").lower()

            if action == "add":
                new_skill = input("Skill name?\n> ")
                req = int(input("Required level?\n> "))
                mp = int(input("MP cost?\n> "))
                CHAR_TABLE[clas]['Atributes'][new_skill] = [req, mp]

            elif action == "remove":
                remove_skill = input("Which skill?\n> ")
                if remove_skill in CHAR_TABLE[clas]['Atributes']:
                    del CHAR_TABLE[clas]['Atributes'][remove_skill]

        # Run chosen option
        if choice == "1":
            add_single()
        elif choice == "2":
            mult_level()
        elif choice == "3":
            edit_attributes()

        # Combine base + level + added stats using modifiers (demonstrates closure usage)
        base = CHAR_TABLE[clas]['Stats']
        # make modifiers (closures) that apply level and manual additions
        level_modifier = make_stat_modifier(level_dic['Stats'])
        manual_modifier = make_stat_modifier(added_dic['Stats'])

        # apply modifiers sequentially and handle 'Lvl' specially
        intermediate = level_modifier(base)
        final_stats = manual_modifier(intermediate)
        # ensure Lvl reflects manual added level (added_dic stores Lvl diff)
        final_stats['Lvl'] = base['Lvl'] + added_dic['Stats']['Lvl']

        # Save final stats back to character (use existing 'atributtes' key used elsewhere)
        char[name]['atributtes'] = final_stats

        editing = input("Still editing? (y/n)\n> ").lower()
        if editing != "y":
            break

    return char