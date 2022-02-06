from statistics import mean
import fitness,csv,datetime
import matplotlib.pyplot as plt
import numpy as np
#generate a name for the CSV of the current try
def generateCSVName():
    return str(datetime.datetime.now())

#create the CSV of the current try
def createCSV(selection_name,crossover_name,insertion_name,cross_proba,mutate_proba,seeds):
    csv_name=generateCSVName()
    with open("V3.0.0/results/fit_"+csv_name+".csv", 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["selection","crossover","insertion","crossover_proba","mutation_proba"])
        csv_writer.writerow([selection_name,crossover_name,insertion_name,cross_proba,mutate_proba])
        csv_writer.writerow("")
        csv_writer.writerow(["generation","min","mean","max","stddev"]+seeds)
    return csv_name

#update the local CSV of the current try
#CSV format line is {cycle_number;min;mean;max;std_deviation}
def register(nb_iter,iter_step,results,csv_name):
    with open("V3.0.0/results/fit_"+csv_name+".csv", 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        for rep_num in range(0,nb_iter+1,iter_step):
            fitnesses_at_step=(results[:,int(rep_num/iter_step)]).tolist()
            line=[rep_num]+fitness.evaluation(fitnesses_at_step)+fitnesses_at_step
            csv_writer.writerow(line)
        


def show(csv_name):
    #gather the datas
    with open("V3.0.0/results/fit_"+csv_name+".csv", 'r+', newline='') as csv_file:
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
    plt.savefig("V3.0.0/results/"+csv_name+".png")
    plt.clf()

def createFunctionTracer(li_mutations,csv_name):
    with open("V3.0.0/results/func_"+csv_name+".csv", 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';',dialect='unix',quoting=csv.QUOTE_NONE)
        csv_writer.writerow(["list, for each seed, of the wheel's probabilities"])
        csv_writer.writerow("")
        line=[]
        for elem in li_mutations:
            line.append(elem.__name__)
        csv_writer.writerow(line)

def generateWheelsGraph(wheels_records,max_gen):
    name="wheels_record"
    gen=range(0,max_gen)
    bitflip_curve=[]
    noflip_curve=[]
    oneflip_curve=[]
    threeflip_curve=[]
    fiveflip_curve=[]
    for g in gen: # for each generation (our X axis)
        bitflip_sum=0
        noflip_sum=0
        oneflip_sum=0
        threeflip_sum=0
        fiveflip_sum=0

        #save the mean of each mutation function probability
        for s in range(0,30):
            bitflip_sum+=wheels_records[s][g][0]
            noflip_sum+=wheels_records[s][g][1]
            oneflip_sum+=wheels_records[s][g][2]
            threeflip_sum+=wheels_records[s][g][3]
            fiveflip_sum+=wheels_records[s][g][4]
        bitflip_curve.append(bitflip_sum/30)
        noflip_curve.append(noflip_sum/30)
        oneflip_curve.append(oneflip_sum/30)
        threeflip_curve.append(threeflip_sum/30)
        fiveflip_curve.append(fiveflip_sum/30)

    bitflip=np.array(bitflip_curve)
    noflip=np.array(noflip_curve)
    oneflip=np.array(oneflip_curve)
    threeflip=np.array(threeflip_curve)
    fiveflip=np.array(fiveflip_curve)
    
    plt.plot(gen,bitflip,label="bitflip")
    plt.plot(gen,noflip,label="noflip")
    plt.plot(gen,oneflip,label="oneflip")
    plt.plot(gen,threeflip,label="threeflip")
    plt.plot(gen,fiveflip,label="fiveflip")
    plt.axis([0,gen[-1],0,100])
    plt.xlabel("generations")
    plt.xticks(gen[1::500])
    plt.ylabel("probability")
    plt.grid()
    plt.legend()
    plt.savefig("V3.0.0/results/"+name+".png")

        





