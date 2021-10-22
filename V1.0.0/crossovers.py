#crossover function
#   popultion : current population
#   parentSelect : parent selection function
#   RETURN : offspring
def crossover1(population,parentSelect):
    parents=parentSelect(population)
    offspring=[]
    new1=parents[0][0:4]+parents[1][4:]
    new2=parents[2][0:4]+parents[3][4:]
    offspring.append(new1)
    offspring.append(new2)
    return offspring