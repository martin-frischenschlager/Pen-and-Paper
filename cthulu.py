import random

class Character:
    """
    An investigator-charakter in the "Call of Cthulu"-Universe
    """
    
    #INFO
    info = {'occupation':'', 'age':'', 'birthday':'', 'sex':'', 'residence':'', 'birthplace':''}
    
    #ATTRIBUTES
    stats =  {'STR':0, 'DEX':0, 'POW':0, 'CON':0, 'APP':0, 'EDU':0, 'SIZ':0, 'INT':0, 'MOV':0}
    
    #DERIVED ATTRIBUTES
    der_stats = {'HP':0, 'sanity':0, 'MP':0, 'luck':0}
    
    def __init__(self, name, playedBy):
        self.info['name'] = name
        self.info['playedBy'] = playedBy
        
    def init_stats(self):
        print("setting attributes")
        for key, value in self.stats.items():
            if key not in {'SIZ', 'INT', 'EDU', 'MOV'}:
                self.stats[key] = W(6,3,5)
            elif key != 'MOV':
                self.stats[key] = W(6,2,5,6)

        print("stats \\MOV are set")
        print(self.stats)
    
        
def W(faces=100,throws=1, mult=1, add=0):
    list = []
    for i in range(throws):
        list.append(random.randint(1,faces))
    return (sum(list)+add)*mult