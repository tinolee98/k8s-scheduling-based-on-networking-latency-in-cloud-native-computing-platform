import os
import json
from time import sleep

print('start to measure network latency from nodes')

# initialize client.txt
os.system("echo $(kubectl get pods -n iperf3 -l app=iperf3-client -o name | cut -d'/' -f2) > client.txt")

clientFile = open('./client.txt')
clientsString = clientFile.readline()
clientFile.close()

clients = clientsString.split()

latency = [0,0,0]

i = 1
while(1):
    print(i,"times...")
    os.system("./steps/run.sh")
    print("if you want to stop this process, press \'ctrl + C\'")
    i += 1

    for j in range(len(clients)):
        client = clients[j]
        fileName = "./latency/"+client+"_latency.json"
        jsonFile = open(fileName)
        iperf3File = json.load(jsonFile)
        jsonFile.close()
        end = iperf3File.get("end")
        stream = end.get("streams")
        senderBytes = stream[0].get("sender").get("bytes")
        latency[j] = int(senderBytes)
    print("latency: ", latency, "\n\n")
    sleep(5)
