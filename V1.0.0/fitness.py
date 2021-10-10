from statistics import pstdev,mean

#generate statistics on the population
#   population: list of bit vectors
#   return a list as follow [mean,standard deviation,min,max]
def evaluation(population):
    #evaluate the fitness of each member to calculate statistics on it
    pop_fit=[]
    for i in range(len(population)):
        pop_fit.append(fitness(population[i]))

    print(pop_fit)
    #calculate statistics
    fit_mean=mean(pop_fit)
    std_dev=pstdev(pop_fit,mu=fit_mean)

    return([fit_mean,std_dev,min(pop_fit),max(pop_fit)])

#evaluate x depending on the quantity of "1" it has
#   x: bit vector to be tested
#   return a float in [0,1]
def fitness(x):
    return float(mean(x))
    