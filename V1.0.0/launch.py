import crossovers,mutations,selections,fitness,UI

#function starting a simulation
#   population: starting population
#   nb_cycle: quantity of generations
#   cross: crossover function
#   mutate: mutation function
#   selectSurvivors: survivor selection function
def launch(population,nb_cycle,cross,mutate,selectSurvivors):
    UI.createCSV(cross.__name__,mutate.__name__,selectSurvivors.__name__)
    for i in range(nb_cycle):
        #crossover
        offspring=cross(population)
        #mutation
        mutate(offspring)
        #survivor selection
        selectSurvivors(population,offspring)
