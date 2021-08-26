#!/usr/bin/env python

import time
import random
import json

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException

config.load_kube_config()
v1 = client.CoreV1Api()

scheduler_name = "testScheduler"

def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
        for status in n.status.conditions:
            if status.status == "True" and status.type == "Ready":
                ready_nodes.append(n.metadata.name)
    return ready_nodes

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
                res = scheduler(event['object'].metadata.name, random.choice(nodes_available()))
                print("Success Scheduling!")
            except ApiException as e:
                print(json.lods(e.body)['message'])

if __name__ == '__main__':
    print("Scheduling starts...")
    main()
