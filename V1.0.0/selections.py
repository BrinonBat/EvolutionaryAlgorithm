import fitness

#parent selection functions
def parent1(population):
    return population[-4:]

#survivor selection functions
def survivor1(population,offspring):
    for member in offspring:
        fitness.insert(member,population)
        population.pop(0)