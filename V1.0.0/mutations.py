import random as rand
import fitness
def mutation1(population):
    member=population[rand.randint(0,len(population)-1)]
    pos=rand.randint(0,15)
    member[pos]=int(not(member[pos]))

    member=population[rand.randint(0,len(population)-1)]
    pos=rand.randint(0,15)
    member[pos]=int(not(member[pos]))