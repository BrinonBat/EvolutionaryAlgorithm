import crossovers,mutations,selections,fitness,UI,time
import random,csv

#choosed 16 bits at first, but can switch to 
# 100 iteration, a print every 5 iteration

li_select=[selections.bestFirst,selections.randomSelection]
li_cross=[crossovers.crossAtHalf, crossovers.randomCross]
li_mutate=[mutations.oneFlip,mutations.threeFlip,mutations.fiveFlip,mutations.bitFlip] 
li_insert=[selections.highFitnessFirst,selections.bestOfAFourth,selections.randomInsertion]
parameters=[0,0,1,0,100,100] #[select_function_number, crossover_function_number, mutation_function_number, insertion_function_number,crossover_probability,mutation_probability]

#execute one generation
#   verbose: True to print things, False to only get the results
#   parameters: numbers corresponding to the functions applied and the mutation&crossovers probabilities
#   population: individuals list to be treated
def iterate(verbose,parameters,population):
    select=li_select[parameters[0]]
    cross=li_cross[parameters[1]]
    mutate=li_mutate[parameters[2]]
    insert=li_insert[parameters[3]]
    cross_proba=parameters[4]
    mutate_proba=parameters[5]

    #crossover
    if(random.randint(1,100)<=cross_proba): offspring=cross(population,select)
    #mutation
    if(random.randint(1,100)<=mutate_proba):mutate(offspring)
    if verbose : print("after mutation, offspring is "+str(offspring))
    #insertion
    insert(population,offspring)

#function starting a simulation
#   verbose: True to print things, False to only get the results
#   population_size: quantity of individuals in the population
#   nb_cycle: quantity of maximum generations  
#   nb_cycle_register: quantity of cycles between each registration of the population
#   parameters: numbers corresponding to the functions applied and the mutation&crossovers probabilities
def launch(verbose,vector_size,population_size,nb_cycle,nb_cycle_register,parameters):
    
    results=[]

    #get the seeds
    with open ('seeds.csv','r') as csv_file:
        reader = list(csv.reader(csv_file,delimiter=" "))
        seeds=reader[0]

    #generate CSV
    csv_name=UI.createCSV(li_select[parameters[0]].__name__,li_cross[parameters[1]].__name__,li_mutate[parameters[2]].__name__,li_insert[parameters[3]].__name__,parameters[4],parameters[5],seeds)

    #chrono initialization
    start=time.time()
    end=start

    #iterate for each seed
    for seed_num in range(0,len(seeds)):
        if verbose: print("seed is "+seed)
        
        #initialize
        results.append([])
        seed=seeds[seed_num]
        random.seed(seed)    
        
        #generate population
        population=[([0]*vector_size)]*population_size
        #if verbose: print("pop size at first:"+str(len(population)))

        #start the algorithm
        for i in range(nb_cycle):
            iterate(verbose,parameters,population)
            if verbose: print("seed "+str(seed_num+1)+"/"+str(len(seeds))+"; iteration "+str(i)+" done")

            #save the results every X generation so we can prompt it on a graph
            if((i+1)%nb_cycle_register==0):
                results[seed_num].append(fitness.maxFit(population))
                
        #show the time spent and time remaining
        duration=(time.time()-end)
        end=time.time()
        remaining=((time.time()-start)*(len(seeds)-(seed_num+1)))/(seed_num+1)
        print("seed "+str(seed_num+1)+"/"+str(len(seeds))+" finished in %.2f s " %duration +" approximately %.2f s remaining" %remaining)

    #once finished, we save the results
    print("finished in %.2f s" %(time.time()-start))
    UI.register(nb_cycle,nb_cycle_register,results,csv_name)
    UI.show(csv_name)
nb_cycle_step=5 #step bewteen each registration in the local data file
vector_size=100 # between 100 and 1000
population_size=20
nb_cycle=20001
verbose=False
launch(verbose,vector_size,population_size,nb_cycle,nb_cycle_step,parameters)