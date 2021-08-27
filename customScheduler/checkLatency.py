import json
from time import sleep

nodeFile = open('../iperf/nodes.txt')
nodeString = nodeFile.readline()
nodeFile.close()

nodes = nodeString.split()

latency = [0 for _ in range(len(nodes))]

#writeFile = open('./2.txt', 'w')
print(nodes)
while(1):
    sleep(5)
    file = open("../iperf/latency/latency.txt",'r')
    latency = file.readline()
    print(latency)
    file.close()
