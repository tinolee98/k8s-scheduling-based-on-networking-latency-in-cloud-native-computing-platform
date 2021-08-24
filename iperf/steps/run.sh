#!/usr/bin/env bash
set -eu

CLIENTS=$(kubectl get pods -n iperf3 -l app=iperf3-client -o name | cut -d'/' -f2)
echo ${CLIENTS} > client.txt

for POD in ${CLIENTS}; do
    until $(kubectl get -n iperf3 pod ${POD} -o jsonpath='{.status.containerStatuses[0].ready}'); do
        echo "Waiting for ${POD} to start..."
        sleep 5
    done
    echo "measure the network latency from ${POD}..."
    HOST=$(kubectl get -n iperf3 pod ${POD} -o jsonpath='{.status.hostIP}')
    kubectl exec -it ${POD} -n iperf3 -- iperf3 -c iperf3-server -J -T"Client on ${HOST}" $@ > ./latency/${POD}_latency.json
done
