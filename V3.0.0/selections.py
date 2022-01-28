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

    qty_insert=0
    #insert the offspring in the population
    for member in offspring:
        fitness.insert(member,population)
        qty_insert+=1
    
    #select 1/4th of the population's position and sort it
    selecteds=random.sample(range(0, int(len(population)-1)),int(len(population)/4))
    selecteds=sorted(selecteds)[-qty_insert:]

    #pop members which position is in selected
    for i in range(qty_insert):
        population.pop(selecteds[i]-i) # -i is the update of the position, because the one stored in selecteds isn't updated when popped out of population

def randomInsertion(population,offspring):

    qty_insert=0

    #insertion
    for member in offspring:
        qty_insert+=1
        fitness.insert(member,population)
    
    #deletion
    while qty_insert>0:
        population.pop(random.randint(0,len(population)-1))
        qty_insert-=1

# parent selection ====> SELECTION
# select parents depending on their fitness
def bestFirst(population):
    return population[-2:]

# select parents randomly
def randomSelection(population):
    return random.choices(population,k=2)