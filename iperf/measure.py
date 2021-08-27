import os
from subprocess import check_output
import json
from time import sleep

print('start to measure network latency from nodes')

# initialize client.txt
os.system("echo $(kubectl get pods -n iperf3 -l app=iperf3-client -o name | cut -d'/' -f2) > client.txt")

clientFile = open('./client.txt')
clientsString = clientFile.readline()
clientFile.close()

clients = clientsString.split()

nodes = []
for client in clients:
    node = check_output(['kubectl', 'get', '-n', 'iperf3', 'po', client, '-o', 'jsonpath=\'{.spec.nodeName}\'']).decode('utf-8')
    node = node.replace("'", "")
    nodes.append(node)

print (nodes)
nodeFile = open("./nodes.txt","w")
nodeFile.write(" ".join(nodes))
nodeFile.close()


latency = ['0' for _ in range(len(nodes))]

writeFile = open('./latency/latency.txt', 'w')
writeFile.write("0 0 0")
writeFile.close()

i = 1

while(1):
    print(i,"times...")
    os.system("./steps/run.sh")
    print("if you want to stop this process, press \'ctrl + C\'")
    i += 1

    for j in range(len(nodes)):
        node = nodes[j]
        fileName = "./latency/"+node+"_latency.json"
        jsonFile = open(fileName)
        iperf3File = json.load(jsonFile)
        jsonFile.close()
        end = iperf3File.get("end")
        stream = end.get("streams")
        senderBytes = stream[0].get("sender").get("bytes")
        latency[j] = str(senderBytes)
    print("latency: ", latency, "\n")
    writeFile = open('./latency/latency.txt', 'w')
    writeFile.write(" ".join(latency))
    writeFile.close()
    sleep(5)
