import fitness,csv,datetime

#generate a name for the CSV of the current try
def generateCSVName():
    return str(datetime.datetime.now())

#create the CSV of the current try
def createCSV(crossover_name,mutation_name,survivor_selection_name,parent_selection_name):
    csv_name=generateCSVName()
    with open("V1.0.0/"+csv_name+".csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["crossover","mutation","survivor_selection","parent_selection"])
        csv_writer.writerow([crossover_name,mutation_name,survivor_selection_name,parent_selection_name])
        csv_writer.writerow("")
        csv_writer.writerow(["cycle_number","min","mean","max","std_deviation"])
    return csv_name

#update the CSV of the current try
#CSV format line is {cycle_number;min;mean;max;std_deviation}
def updateCSV(cycle_number,population,csv_name):
     with open("V1.0.0/"+csv_name+".csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow([cycle_number]+fitness.evaluation(population))


#save the results in the global CSV to compare with other configurations
#CSV's first line: {Version;vector_size;population_size;nb_cycle;crossover;mutation;survivor_selection;parents_selection;min;mean;max;std_deviation}
def saveResults(vector_size,population_size,nb_cycle,crossover_name,mutation_name,survivor_selection_name,parent_selection_name,final_stats):
    print(final_stats)
    with open('global.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["1.0.0",str(vector_size),str(population_size),str(nb_cycle),crossover_name,mutation_name,survivor_selection_name,parent_selection_name]+final_stats)
        print("sauvegarde du résultat effectuée")