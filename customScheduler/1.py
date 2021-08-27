import json
from time import sleep

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException

config.load_kube_config()
v1 = client,CoreV1Api()

scheduler_name = "testScheduler"

def nodes_available():
    ready_nodes = []
    return ready_nodes

def scheduler(name, node, namespace="default"):
    target = client.V1ObjectReference()
    target.kind = "Node"
    target.apiVersion = "v1"
    target.name = node

    meta = client.V1ObjectMeta()
    meta.name = name

    body = client.V1Binding(target = target, metadata = meta)
    body.metadata = meta

    return v1.create_namespaced_binding(namespace, body)

clientFile = open('../iperf/client.txt')
clientsString = clientFile.readline()
clientFile.close()

clients = clientsString.split()

latency = [0 for _ in range(len(clients))]

def main():
    latency = [0 for _ in range(len(clients))]
    print(latency)


if __name__ == '__main__':
    print("call main")
    main()


# json 파일을 읽어서 scheduling을 할 수 있는 친구를 만드는 중
