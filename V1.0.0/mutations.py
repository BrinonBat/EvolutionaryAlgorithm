import random as rand

#used for some testing
def mutation1(population,seed):
    rand.seed(seed)
    member=population[rand.randint(0,len(population)-1)]
    print(member)
    pos=rand.randint(0,len(member)-1)
    member[pos]=int(not(member[pos]))

    member=population[rand.randint(0,len(population)-1)]
    pos=rand.randint(0,len(member)-1)
    member[pos]=int(not(member[pos]))

#Change the value of one of the bit
def oneFlip(population,seed):
    rand.seed(seed)
    member=population[rand.randint(0,len(population)-1)]
    pos=rand.randint(0,len(member)-1)
    member[pos]=int(not(member[pos]))

#Change the value of three bits
def threeFlip(population,seed):
    rand.seed(seed)
    member=population[rand.randint(0,len(population)-1)]
    for i in range(3):
        pos=rand.randint(0,len(member)-1)
        member[pos]=int(not(member[pos]))

#Change the value of five bits
def fiveFlip(population,seed):
    rand.seed(seed)
    member=population[rand.randint(0,len(population)-1)]
    for i in range(5):
        pos=rand.randint(0,len(member)-1)
        member[pos]=int(not(member[pos]))

#each bit have 1/nbBit chances to be flipped
def bitFlip(population,seed):
    rand.seed(seed)
    member=population[rand.randint(0,len(population)-1)]
    for i in member:
        if rand.randint(0,len(member)-1)==i : member[i]==int(not(member[i]))
    