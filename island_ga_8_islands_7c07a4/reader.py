import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

run_data_file = sys.argv[1]
energy_data_file = sys.argv[2]

fo = open(run_data_file, "rw+")

timestamps = [None]*16
generations = [None]*15
line = fo.readline()
timestamps[0] = int(line.rstrip())
for i in range(0,15):
    line = fo.readline()
    generations[i] = int(line.split(" ")[2].rstrip())
    line = fo.readline()
    timestamps[i+1] = int(line.rstrip())
fo.close()

raw_data = []

with open(energy_data_file) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        raw_data.append([None]*13)
        raw_data[len(raw_data)-1][0] = int(row[0])
        for i in range(1,13):
            raw_data[len(raw_data)-1][i] = float(row[i])

raw_data = filter(lambda x: timestamps[0] <= x[0] <= timestamps[15], raw_data)

average_data = [0]*12
for row in raw_data:
    for i in range(0,12):
        average_data[i] += row[i+1]

for i in range(0,12):
    average_data[i] = average_data[i]/len(raw_data)

total_generations = 0
for i in range(15):
    total_generations += generations[i]


print "Average execution time"
print (timestamps[15]-timestamps[0])/15
print "Average generations"
print (total_generations)/15

print "Average energy data for components:"
print "A15 Volt, A15 Amps, A15 Watt, A7  Volt, A7  Amps, A7  Watt, GPU Volt, GPU Amps, GPU Watt, Mem Volt, Mem Amps, Mem Watt"
for data in average_data:
    print str(data) + ",",
print

