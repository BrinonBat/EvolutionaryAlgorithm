import random as rand
#crossover function
#   popultion : current population
#   parentSelect : parent selection function
#   RETURN : offspring
def crossoverAtFour(population,parentSelect):
    parents=parentSelect(4,population)
    offspring=[]
    new1=parents[0][0:4]+parents[1][4:]
    new2=parents[2][0:4]+parents[3][4:]
    offspring.append(new1)
    offspring.append(new2)
    return offspring

def randomCross(population,parentSelect):
    parents=parentSelect(2,population)
    pos=rand.randint(0,len(parents[0])-1)
    print("pos is "+str(pos))
    new=parents[0][:pos]+parents[1][pos:]
    return [new] #offspring

def crossAtHalf(population,parentSelect):
    parents=parentSelect(2,population)
    pos=len(parents[0])/2
    new=parents[0][:pos]+parents[1][pos:]
    return [new] #offspring