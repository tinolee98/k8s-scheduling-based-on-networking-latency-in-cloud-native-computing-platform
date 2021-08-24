import json

clientFile = open('./client.txt')
clientsString = clientFile.readline()
clientFile.close()

clients = clientsString.split()

for client in clients:
    print(client)
    fileName = "./latency/"+client+"_latency.json"
    jsonFile = open(fileName)
    iperf3File = json.load(jsonFile)
    jsonFile.close()
    end = iperf3File.get("end")
    stream = end.get("streams")
    senderBytes = stream[0].get("sender").get("bytes")
    print(senderBytes)
