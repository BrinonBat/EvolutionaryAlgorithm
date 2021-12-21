import random as rand
import csv
with open('seeds.csv','a',newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=' ',dialect='unix',quoting=csv.QUOTE_NONE)
    seeds=[]
    for i in range(30):
        seeds.append(rand.randint(0,9999999))
    csv_writer.writerow(seeds)

