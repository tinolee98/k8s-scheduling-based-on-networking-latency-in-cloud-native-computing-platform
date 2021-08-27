#!/usr/bin/env bash
set -eu

CLIENTS=$(kubectl get pods -n iperf3 -l app=iperf3-client -o name | cut -d'/' -f2)
echo ${CLIENTS} > client.txt

for POD in ${CLIENTS}; do
    until $(kubectl get -n iperf3 pod ${POD} -o jsonpath='{.status.containerStatuses[0].ready}'); do
        echo "Waiting for ${POD} to start..."
        sleep 5
    done
    NODE=$(kubectl get -n iperf3 pod ${POD} -o jsonpath='{.spec.nodeName}')
    echo "measure the network latency from ${NODE} to masterNode..."
    kubectl exec -it ${POD} -n iperf3 -- iperf3 -c iperf3-server -J -T"Client on ${NODE}" $@ > ./latency/${NODE}_latency.json
done
