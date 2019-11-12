# =============================================================================
# Call of Cthulu - Caracter designer
# =============================================================================
# this should be a step by step guid through the character design process
# the process shall be broken down into sections
# everything should be well narrated and easily understood
from cthulu import Character, intInput, agemodify, W


def padding():
    print('_' * 79)


# Greeting and initialize new Character
greeting = ("############# WELCOME TO THE \"CALL OF CTHULU\" CHARACTER"
            "-DESIGNER ##############")
print('#' * 79)
print(greeting)
print('#' * 79)

playedBy = input("First up, tell me YOUR NAME: ")
padding()
print(f"Hi {playedBy}! Let's begin setting up your new character!")

name = input("Now, what NAME do you give your new character?: ")
padding()
player = Character(name, playedBy)
print(f"Alright, {playedBy}! Let's start by determining {name}'s stats!")
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

padding()

# initialize stats
if roll:
    pass
else:
    player.init_stats()
    print(f"Here are {name}'s preliminary stats.")
    for key, value in player.stats.items():
        if key == 'MOV':
            continue
        print(f"{key}: {value}")

age = intInput(15, 90, "Age", f"Now, what AGE is {name}? (15-90): ")
padding()

luckBonus = False
eduBonus = 0
if roll:
    pass
else:
    if 15 <= age < 20:
        msg = ("Alright, then we need to remove a total of 5 points from "
               "STR and SIZ as well as 5 points from EDU.")
        print(msg)
        print("But you get a bonus throw for luck afterwards.")
        luckBonus = True
        minus = intInput(0, 5, "Value",
                         "How many do you want me to remove from STR? (0-5) ")
        padding()
        player.stats['STR'] -= minus
        player.stats['SIZ'] -= 5 - minus
        player.stats['EDU'] -= 5
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'SIZ', 'EDU'}:
                continue
            print(key + ": ", value)
    elif 20 <= age < 40:
        print("You get one chance at a better EDU stat")
        eduBonus = 1
    elif 40 <= age < 50:
        eduBonus = 2
        agemodify(player, 5, 5, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 50 <= age < 60:
        eduBonus = 3
        agemodify(player, 10, 10, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 60 <= age < 70:
        eduBonus = 4
        agemodify(player, 20, 15, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 70 <= age < 80:
        eduBonus = 4
        agemodify(player, 40, 20, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)
    elif 80 <= age <= 90:
        eduBonus = 4
        agemodify(player, 80, 25, eduBonus)
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR', 'CON', 'DEX', 'APP'}:
                continue
            print(key + ": ", value)

padding()

# do a test for bonus on EDU stat
if roll:
    pass
elif eduBonus != 0:
    if eduBonus == 1:
        ch = "chance"
        t = "once"
    else:
        if eduBonus == 2:
            t = "twice"
        else:
            t = f"{eduBonus} times"
        ch = "chances"
    print(f"You now get {eduBonus} {ch} at a better EDU stat")
    print(f"I will roll W100 {t}. If I roll a better score than your EDU stat, "
          "you get 1W10 added to EDU.")

    print(f"Your EDU stat is: {player.stats['EDU']}")
    rolls = [W() for n in range(eduBonus)]
    high_roll = max(rolls)
    print(f"rolls: {rolls}")

    if high_roll > player.stats['EDU']:
        print(f"{high_roll} > {player.stats['EDU']}")
        print("Success!")
        wten = W(10)
        print(f"I rolled {wten}")
        player.stats['EDU'] += wten
        if player.stats['EDU'] > 99:
            wten = player.stats['EDU'] - 99
            player.stats['EDU'] = 99
        print(f"Your EDU-score has been improved by {wten} and is now "
              f"{player.stats['EDU']}")
    else:
        print("No higher roll")

padding()

# initialize derived attributes
player.der_stats['sanity'] = player.stats['POW']
player.der_stats['MP'] = player.stats['POW'] // 5
player.der_stats['luck'] = W(6, 3, 5)
player.der_stats['HP'] = (player.stats['CON'] + player.stats['SIZ']) // 10

print("Your derived stats are:")
for key, value in player.der_stats.items():
    print(f"{key}: {value}")

if luckBonus != 0:
    print("Doing an extra roll for luck.")
    roll = W(6, 3, 5)
    print(roll)
    if roll > player.der_stats['luck']:
        player.der_stats['luck'] = roll

# determine move rate
Dex = player.stats['DEX']
Str = player.stats['STR']
Siz = player.stats['SIZ']

if Dex < Siz and Str < Siz:
    player.stats['MOV'] = 7
elif Dex > Siz and Str > Siz:
    player.stats['MOV'] = 9
else:
    player.stats['MOV'] = 8

if 40 <= age < 50:
    player.stats['MOV'] -= 1
elif 50 <= age < 60:
    player.stats['MOV'] -= 2
elif 60 <= age < 70:
    player.stats['MOV'] -= 3
elif 70 <= age < 80:
    player.stats['MOV'] -= 4
elif 80 <= age < 90:
    player.stats['MOV'] -= 5

print(f"Your move rate is {player.stats['MOV']}")

print("DONE!")
