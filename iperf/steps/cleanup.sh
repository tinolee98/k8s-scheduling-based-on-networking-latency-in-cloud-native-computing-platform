#!/usr/bin/env bash
set -eu

kubectl delete --cascade -f test_iperf3.yaml
