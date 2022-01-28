import crossovers,mutations,selections,fitness,UI,time
import random,csv,numpy

li_select=[selections.bestFirst]
li_cross=[crossovers.crossAtHalf]
li_mutate=[mutations.bitFlip,mutations.oneFlip,mutations.threeFlip,mutations.fiveFlip] 
li_insert=[selections.highFitnessFirst,selections.bestOfAFourth]
li_proba=[10,50,90]

#execute one generation
#   parameters: numbers corresponding to the functions applied and the mutation&crossovers probabilities
#   population: individuals list to be treated
def iterate(parameters,population):
    select=parameters[0]
    cross=parameters[1]
    mutate=parameters[2]
    insert=parameters[3]
    cross_proba=parameters[4]
    mutate_proba=parameters[5]

    modified=False
    #crossover
    if(random.randint(1,100)<=cross_proba): 
        modified=True
        offspring=cross(population,select)
        #mutation
        if(random.randint(1,100)<=mutate_proba):mutate(offspring)
    
    #other mutation case
    elif(random.randint(1,100)<=mutate_proba):
        modified=True
        offspring=select(population)
        mutate(offspring)

   
    #insertion
    if modified : insert(population,offspring)

#function starting a simulation
#   vector_size: size of each individual
#   population_size: quantity of individuals in the population
#   nb_cycle: quantity of maximum generations  
#   nb_cycle_register: quantity of cycles between each registration of the population
def launch(vector_size,population_size,nb_cycle,nb_cycle_register):
    parameters=[None,None,None,None,None,None]
    best_parameters=[[selections.randomSelection,crossovers.randomCross,mutations.bitFlip,selections.randomInsertion,50,50],nb_cycle+1] # by default, the best is the full random
    
    #generate parameters and launch the algorithm
    for parameters[0] in li_select:
        for parameters[1] in li_cross :
            for parameters[2] in li_mutate :
                for parameters[3] in li_insert :
                    for parameters[4] in li_proba :
                        for parameters[5] in li_proba :
                            print("test for parameters : "+str(parameters))

                            #get the seeds
                            with open ('seeds.csv','r') as csv_file:
                                reader = list(csv.reader(csv_file,delimiter=" "))
                                seeds=reader[0]
                            results=numpy.full((len(seeds),int(nb_cycle/nb_cycle_register)+1),1.0)
                            results[:,0]=0
                            #generate CSV
                            csv_name=UI.createCSV(parameters[0].__name__,parameters[1].__name__,parameters[2].__name__,parameters[3].__name__,parameters[4],parameters[5],seeds)

                            #chrono initialization
                            start=time.time()
                            end=start

                            #iterate for each seed
                            for seed_num in range(0,len(seeds)):
                                
                                #initialize
                                seed=seeds[seed_num]
                                random.seed(seed)    
                                
                                #generate population
                                population=[([0]*vector_size)]*population_size

                                #start the algorithm
                                for i in range(1,nb_cycle+1):
                                    iterate(parameters,population)

                                    #save the results every X generation so we can prompt it on a graph
                                    max=fitness.maxFit(population)
                                    if(max==1.0) : break
                                    if(i%nb_cycle_register==0): results[seed_num][int(i/nb_cycle_register)]=max
                                        
                                #show the time spent and time remaining
                                duration=(time.time()-end)
                                end=time.time()
                                print("seed "+str(seed_num+1)+"/"+str(len(seeds))+" finished in %.2f s " %duration)

                            #once finished, we save the results
                            print(str(parameters)+"finished in %.2f s" %(time.time()-start))
                            score=UI.register(csv_name,nb_cycle,nb_cycle_register,results)
                            print(score)
                            #UI.show(csv_name)
                            if(score<best_parameters[1]):
                                best_parameters[0]=parameters.copy()
                                best_parameters[1]=score
    
    #show the best parameters
    print("the best parameter configuration is ")
    print(best_parameters[0])
    print(" with a score of "+str(best_parameters[1]))
    


nb_cycle_step=5 #step bewteen each registration in the local data file
vector_size=300 # between 100 and 1000
population_size=20
nb_cycle=20000
launch(vector_size,population_size,nb_cycle,nb_cycle_step)