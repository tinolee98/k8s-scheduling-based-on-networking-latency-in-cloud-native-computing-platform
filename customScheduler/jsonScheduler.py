#!/usr/bin/env python

import time
import random
import json

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException

config.load_kube_config()
v1 = client.CoreV1Api()

scheduler_name = "testScheduler"

def nearest_node():
    nodeFile = open('../iperf/nodes.txt')
    nodeString = nodeFile.readline()
    nodeFile.close()
    nodes = nodeString.split()
    print(nodes)
    latencyFile = open("../iperf/latency/latency.txt",'r')
    latencyString = latencyFile.readline()
    latency = list(map(int, latencyString.split()))
    print(latency)
    latencyFile.close()
    
    for i in range(len(nodes)):
        if i == 0:
            nearest = latency[i]
            nearestNode = nodes[i]
        else:
            if nearest < latency[i]:
                nearest = latency[i]
                nearestNode = nodes[i]
    print(nearestNode)
    return nearestNode

def scheduler(name, node, namespace="default"):
    target = client.V1ObjectReference()
    target.kind = "Node"
    target.apiVersion = "v1"
    target.name = node

    meta = client.V1ObjectMeta()
    meta.name = name

    body=client.V1Binding(target = target, metadata = meta)

    body.target = target
    body.metadata = meta

    return v1.create_namespaced_binding(namespace, body)

def main():
    w = watch.Watch()
    for event in w.stream(v1.list_pod_for_all_namespaces):
        if event['object'].status.phase == "Pending" and event['object'].spec.scheduler_name == scheduler_name:
            try:
                res = scheduler(event['object'].metadata.name, nearest_node())
                print("Success Scheduling!")
            except ApiException as e:
                print(json.lods(e.body)['message'])

if __name__ == '__main__':
    print("Scheduling starts...")
    main()
