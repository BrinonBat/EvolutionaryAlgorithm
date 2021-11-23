import fitness
import random

#survivor selection functions ===> INSERTION
def highFitnessFirst(population,offspring):
    for member in offspring:
        fitness.insert(member,population)
        population.pop(0)

#random choice of 1/4th of the population
#then pop out the worsts of them
def bestOfAFourth(population,offspring):
    out=len(offspring)
    for member in offspring:
        fitness.insert(member,population)
    
    selecteds=random.sample(range(0, int(len(population)-1)),int(len(population)/4))
    selecteds=sorted(selecteds)[-out:]
    for i in range (out):
        population.pop(selecteds[i]-i)

def randomInsertion(population,offspring):

    out=len(population)

    for member in offspring:
        fitness.insert(member,population)
    

    while len(population<out):
        population.pop(random.randint(0,len(population)-1))

# parent selection ====> SELECTION
# select parents depending on their fitness
def bestFirst(qty,population):
    return population[-qty:]

# select parents randomly
def randomSelection(qty,population):
    return random.choice(population,k=qty)