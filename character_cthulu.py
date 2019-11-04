# =============================================================================
# Call of Cthulu - Caracter designer
# =============================================================================
# this should be a step by step guid through the character design process
# the process shall be broken down into sections
# everything should be well narrated and easily understood
from cthulu import Character, intInput, agemodify

greeting = (
    "########  Welcome to the \"Call of Cthulu\"-"
    "Character-Designer!  ########")
print(greeting)

playedBy = input("First up, tell me YOUR NAME: ")

print("Hi " + playedBy + "! Let's begin setting up your new character!")

name = input("Now, what NAME do you give your new character?: ")
player = Character(name, playedBy)

print("Alright,", playedBy +
      "! Let's start by determining", name + "'s stats!")
print("First up, do you want to roll dice yourself?")

# self or automatic dice throwing?
while True:
    roll = input("[Y/N] ")
    if roll == 'Y':
        roll = True
        print("Alright, get your dice ready, here we go!")
        break
    elif roll == 'N':
        roll = False
        print("Alright, here we go!")
        break
    else:
        print("Sorry, I didn't recognize that, try again.")

# initialize stats
if roll:
    pass
else:
    player.init_stats()
    print("Here are", name + "'s preliminary stats.")
    for key, value in player.stats.items():
        if key == 'MOV':
            continue
        print(key + ":", value)

age = intInput(15, 90, "Age", "Now, what AGE is " + name + "? (15-90): ")

luckBonus = False
eduBonus = 0
if roll:
    pass
else:
    if 15 <= age and age < 20:
        msg = ("Alright, then we need to remove a total of 5 points from "
               "STR and SIZ as well as 5 points from EDU.")
        print(msg)
        print("But you get a bonus throw for luck afterwards.")
        luckBonus = True
        minus = intInput(0, 5, "Value",
                         "How many do you want me to remove from STR? (0-5) ")
        player.stats['STR'] -= minus
        player.stats['SIZ'] -= 5 - minus
        player.stats['EDU'] -= 5
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'SIZ', 'EDU'}:
                continue
            print(key + ": ", value)
    elif 20 <= age and age < 40:
        print("You get one chance at a better EDU stat")
        eduBonus = 1
    elif 40 <= age and age < 50:
        eduBonus = 2
        agemodify(player, 5, 5, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 50 <= age and age < 60:
        eduBonus = 3
        agemodify(player, 10, 10, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 60 <= age and age < 70:
        eduBonus = 4
        agemodify(player, 20, 15, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 70 <= age and age < 80:
        eduBonus = 4
        agemodify(player, 40, 20, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 80 <= age and age <= 90:
        eduBonus = 4
        agemodify(player, 80, 25, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
