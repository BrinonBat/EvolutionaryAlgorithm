from statistics import pstdev,mean

#generate statistics on the population
#   list: list of elements to get stats on
#   return a list as follow [mean,standard deviation,min,max]
def evaluation(list):
    #calculate statistics
    fit_mean=mean(list)
    std_dev=pstdev(list,mu=fit_mean)

    return([min(list),fit_mean,max(list),std_dev])

#evaluate x depending on the quantity of "1" it has
#   x: bit vector to be tested
#   return a float in [0,1]
def fitness(x):
    return float(mean(x))

#return de maximum fitness the population has
def maxFit(population):
    #evaluate the fitness of each member to calculate statistics on it
    pop_fit=[]
    for i in range(len(population)):
        pop_fit.append(fitness(population[i]))
    return max(pop_fit)

#insert the new member in the population according to his fitness
#   member: bit vector to be placed
#   population: array of bit vector where it has to be inserted
def insert(member,population):
    for i in range(len(population)):
        if(fitness(member)<=fitness(population[i])): 
            population.insert(i,member)
            return
    population.append(member)
