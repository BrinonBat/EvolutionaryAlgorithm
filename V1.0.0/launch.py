import crossovers,mutations,selections,fitness,UI

#choosed 16 bits at first, but can switch to 
# 100 iteration, a print every 5 iteration

#function starting a simulation
#   population: starting population
#   nb_cycle: quantity of generations
#   cross: crossover function
#   mutate: mutation function
#   selectSurvivors: survivor selection function
def launch(vector_size,population_size,nb_cycle,nb_cycle_register,cross,mutate,selectSurvivors,selectParents):
    
    #generate population
    population=[([0]*vector_size)]*population_size
    print("pop size at first:"+str(len(population)))
    #generate CSV
    csv_name=UI.createCSV(cross.__name__,mutate.__name__,selectSurvivors.__name__,selectParents.__name__)
  
    #start the algorithm
    for i in range(nb_cycle):
        #crossover
        offspring=cross(population,parent_selection)
        #mutation
        mutate(offspring)
        #survivor selection
        selectSurvivors(population,offspring)

        #save the results every 5 generation so we can prompt it on a graph
        if((i+1)%nb_cycle_register==0):
            max=UI.updateCSV(i+1,population,csv_name)
            if(max==1.0):break 
    #once finished, we save the results of this try and we show it
    UI.saveResults(vector_size,population_size,nb_cycle,cross.__name__,mutate.__name__,selectSurvivors.__name__,selectParents.__name__,fitness.evaluation(population))
    UI.show(csv_name)

nb_cycle_step=5 #step bewteen each registration in the local data file
vector_size=16
population_size=12
nb_cycle=200
crossover=crossovers.crossover1
mutation=mutations.mutation1
survivor_selection=selections.survivor1
parent_selection=selections.parent1

launch(vector_size,population_size,nb_cycle,nb_cycle_step,crossover,mutation,survivor_selection,parent_selection)