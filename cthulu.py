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
    """ default returns a 100-sided dicethrow-result, 
    options include No. of faces, No. of summmed throws,
    multiplicator of result, offset addition to the result """
    list = []
    for i in range(throws):
        list.append(random.randint(1,faces))
    return (sum(list)+add)*mult

def intInput(a,b):
    """ asks for an Integer-input in [a,b], returns input once correctly entered """
    while True:
        inp = input()
        try:
            inp_int = int(inp)
            if not a <= inp_int <= b: print("Input must be between",a,"and",b); raise ValueError 
            break
        except: print("Please try again!")
    return inp_int