import fitness,csv,datetime
import matplotlib.pyplot as plt
#generate a name for the CSV of the current try
def generateCSVName():
    return str(datetime.datetime.now())

#create the CSV of the current try
def createCSV(crossover_name,mutation_name,survivor_selection_name,parent_selection_name):
    csv_name=generateCSVName()
    with open("V1.0.0/results/"+csv_name+".csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["crossover","mutation","survivor_selection","parent_selection"])
        csv_writer.writerow([crossover_name,mutation_name,survivor_selection_name,parent_selection_name])
        csv_writer.writerow("")
        csv_writer.writerow(["cycle_number","min","mean","max","std_deviation"])
    return csv_name

#update the local CSV of the current try
#CSV format line is {cycle_number;min;mean;max;std_deviation}
def updateCSV(cycle_number,population,csv_name):
    stats=fitness.evaluation(population)
    with open("V1.0.0/results/"+csv_name+".csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow([cycle_number]+stats)
    return stats[2]


#save the results in the global CSV to compare with other configurations
#CSV's first line: {Version;vector_size;population_size;nb_cycle;crossover;mutation;survivor_selection;parents_selection;min;mean;max;std_deviation}
def saveResults(vector_size,population_size,nb_cycle,crossover_name,mutation_name,survivor_selection_name,parent_selection_name,final_stats):
    print(final_stats)
    with open('global.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["1.0.0",str(vector_size),str(population_size),str(nb_cycle),crossover_name,mutation_name,survivor_selection_name,parent_selection_name]+final_stats)
        print("sauvegarde du résultat effectuée")


def show(csv_name):
    #gather the datas
    with open("V1.0.0/results/"+csv_name+".csv", 'r+', newline='') as csvfile:
        reader = list(csv.reader(csvfile,delimiter=";"))
        mins=[0]
        cycles=[0]
        maxs=[0]
        means=[0]
        stddevs=[0]
        for row in reader[4:]:
            cycles.append(float(row[0]))
            mins.append(float(row[1]))
            means.append(float(row[2]))
            maxs.append(float(row[3]))
            stddevs.append(float(row[4]))

    #generate associated plot
    plt.plot(cycles,mins,label="min")
    plt.plot(cycles,means,label="mean")
    plt.plot(cycles,maxs,label="max")
    plt.plot(cycles,stddevs,label="stddev")
    plt.axis([0,cycles[-1],0,1])
    plt.xlabel("cycles")
    plt.xticks(cycles)
    plt.ylabel("value")
    plt.grid()
    plt.legend()
    plt.savefig("V1.0.0/results/"+csv_name+".png")