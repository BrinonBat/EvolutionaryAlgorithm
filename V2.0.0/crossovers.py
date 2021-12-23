import random as rand
#crossover function
#   popultion : current population
#   parentSelect : parent selection function
#   RETURN : offspring
def crossoverAtFour(population,parentSelect):
    parents=parentSelect(population)
    offspring=[]
    new_1=parents[0][:4]+parents[1][4:]
    new_2=parents[1][:4]+parents[0][4:]
    offspring.append(new_1)
    offspring.append(new_2)
    return offspring

def randomCross(population,parentSelect):
    parents=parentSelect(population)
    pos=rand.randint(0,len(parents[0])-1)
    offspring=[]
    new_1=parents[0][:pos]+parents[1][pos:]
    new_2=parents[1][:pos]+parents[0][pos:]
    offspring.append(new_1)
    offspring.append(new_2)
    return offspring #offspring

def crossAtHalf(population,parentSelect):
    parents=parentSelect(population)
    pos=int(len(parents[0])/2)
    offspring=[]
    new_1=parents[0][:pos]+parents[1][pos:]
    new_2=parents[1][:pos]+parents[0][pos:]
    offspring.append(new_1)
    offspring.append(new_2)
    return offspring #offspring