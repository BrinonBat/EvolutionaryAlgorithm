from statistics import mean
import fitness,csv,datetime
import matplotlib.pyplot as plt
import numpy as np
import os

#create the CSV of the current try
def createCSV(selection_name,crossover_name,mutation_name,insertion_name,cross_proba,mutate_proba,seeds):
    path="V2.0.0/results/"+selection_name+"/"+crossover_name+"/"+mutation_name+"/"+insertion_name
    if not os.path.exists(path): os.makedirs(path)
    csv_path=path+"/c"+str(cross_proba)+"_m"+str(mutate_proba)+"_datas.csv"
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["selection","crossover","mutation","insertion","crossover_proba","mutation_proba"])
        csv_writer.writerow([selection_name,crossover_name,mutation_name,insertion_name,cross_proba,mutate_proba])
        csv_writer.writerow("")
        csv_writer.writerow(["generation","min","mean","max","stddev"]+seeds)
    return csv_path

#update the local CSV of the current try
#CSV format line is {cycle_number;min;mean;max;std_deviation}
def register(csv_path,nb_iter,iter_step,results):
    score=nb_iter+1
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        for rep_num in range(0,nb_iter+1,iter_step):
            fitnesses_at_step=(results[:,int(rep_num/iter_step)]).tolist()
            line=[rep_num]+fitness.evaluation(fitnesses_at_step)+fitnesses_at_step
            if line[2]==1.0 and score==nb_iter+1 : score=line[0] # if mean is 1.0, then score is the current generation
            csv_writer.writerow(line)
    return score
        


def show(path):
    #gather the datas
    with open(path, 'r+', newline='') as csv_file:
        reader = list(csv.reader(csv_file,delimiter=";"))
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
    means=np.array(means)
    stddevs=np.array(stddevs)
    plt.plot(cycles,mins,label="min")
    plt.plot(cycles,means,label="mean")
    plt.plot(cycles,maxs,label="max")
    plt.fill_between(cycles,means-stddevs,means+stddevs,alpha=.3)
    plt.axis([0,cycles[-1],0,1])
    plt.xlabel("generation")
    plt.xticks(cycles[1::500])
    plt.ylabel("value")
    plt.grid()
    plt.legend()
    plt.savefig("V2.0.0/results/"+str(datetime.datetime.now())+".png")