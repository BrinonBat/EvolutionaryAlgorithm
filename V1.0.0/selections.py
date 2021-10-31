import fitness
import random
#parent selection functions
#testing function
def parent1(population):
    return population[-4:]

#survivor selection functions
def survivor1(population,offspring):
    for member in offspring:
        fitness.insert(member,population)
        population.pop(0)

#random choice of 1/4th of the population
#then pop out the worsts of them
def bestOfAFourth(population,offspring):
    out=len(offspring)
    for member in offspring:
        fitness.insert(member,population)
    
    print(population)

    selecteds=random.sample(range(0, int(len(population)-1)),int(len(population)/4))
    print(selecteds)
    selecteds=sorted(selecteds)[-out:]
    print(selecteds)
    for mem in selecteds:
        population.pop(mem)

    print(population)