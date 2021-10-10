from statistics import pstdev,mean

#generate statistics on the population
#   population: list of bit vectors
#   return a list as follow [mean,standard deviation,min,max]
def evaluation(population):
    #evaluate the fitness of each member to calculate statistics on it
    pop_fit=[]
    print("population is ")
    print(population)
    for i in range(len(population)):
        pop_fit.append(fitness(population[i]))

    #calculate statistics
    fit_mean=mean(pop_fit)
    std_dev=pstdev(pop_fit,mu=fit_mean)

    return([min(pop_fit),fit_mean,max(pop_fit),std_dev])

#evaluate x depending on the quantity of "1" it has
#   x: bit vector to be tested
#   return a float in [0,1]
def fitness(x):
    print(" x is")
    print(x)
    return float(mean(x))
    