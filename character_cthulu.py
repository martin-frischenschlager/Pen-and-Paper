# =============================================================================
# Call of Cthulu - Caracter designer
# =============================================================================
#this should be a step by step guid through the character design process
#the process shall be broken down into sections
#everything should be well narrated and easily understood
import cthulu

def agemodify(shareminus,app_minus,edu_bonus):
    sharesum = sum((player.stats['STR'],player.stats['CON'],player.stats['DEX']))
    if shareminus > sharesum: shareminus = sharesum
    if app_minus > player.stats['APP']: app_minus = player.stats['APP']
    print("Alright, then we need to remove a total of",shareminus,"points from STR and CON and DEX as well as",app_minus,"points from APP.")
    print("But you get",edu_bonus,"chances at a better EDU stat.")
    minus1 = int(input("How many points do you want me to remove from STR? (0-"+str(shareminus)+") "))
    player.stats['STR'] -= minus1
    minus2 = int(input("How many points from CON? (0-"+str(shareminus-minus1)+") "))
    player.stats['CON'] -= minus2
    player.stats['DEX'] -= shareminus-minus1-minus2
    player.stats['APP'] -= app_minus
    print("The new values are:")
    for key, value in player.stats.items():
        if key not in {'STR','CON','DEX','APP'}: continue
        print(key+": ",value)


print("########  Welcome to the \"Call of Cthulu\"-Character-Designer!  ########")

playedBy = input("First up, tell me YOUR NAME: ")

print("Hi "+playedBy+"! Let's begin setting up your new character!")

name = input("Now, what NAME do you give your new character?: ")
player = cthulu.Character(name, playedBy)

print("Alright,",playedBy+"! Let's start by determining",name+"'s stats!")
print("First up, do you want to roll dice yourself?")
loop = True
while loop:
    roll = input("[Y/N] ")
    if roll == 'Y':
        roll = True
        loop = False
        print("Alright, get your dice ready, here we go!")
    elif roll == 'N':
        roll = False
        loop = False
        print("Alright, here we go!")
    else:
        print("Sorry, I didn't recognize that, try again.")

if roll:
    pass
else:
    player.init_stats()
    print("Here are",name+"'s preliminary stats.")
    for key, value in player.stats.items():
        if key == 'MOV': continue
        print(key+":",value)

age = int(input("Now, what AGE is "+name+"? (15-90): "))

luckBonus = False
eduBonus = 0
if roll:
    pass
else:
    if 15 <= age and age < 20:
        print("Alright, then we need to remove a total of 5 points from STR and SIZ as well as 5 points from EDU.")
        print("But you get a bonus throw for luck afterwards.")
        luckBonus = True
        minus = int(input("How many do you want me to remove from STR? (0-5) "))
        player.stats['STR'] -= minus
        player.stats['SIZ'] -= 5-minus
        player.stats['EDU'] -= 5
        print("The new values are:")
        for key, value in player.stats.items():
            if key not in {'STR','SIZ','EDU'}: continue
            print(key+": ",value)
    elif 20 <= age and age < 40:
        print("You get one chance at a better EDU stat")
        eduBonus = 1
    elif 40 <= age and age < 50:
        eduBonus = 2
        agemodify(5,5,eduBonus)
    elif 50 <= age and age < 60:
        eduBonus = 3
        agemodify(10,10,eduBonus)
    elif 60 <= age and age < 70:
        eduBonus = 4
        agemodify(20,15,eduBonus)
    elif 70 <= age and age < 80:
        eduBonus = 4
        agemodify(40,20,eduBonus)
    elif 80 <= age and age <= 90:
        eduBonus = 4
        agemodify(80,25,eduBonus)
        
    