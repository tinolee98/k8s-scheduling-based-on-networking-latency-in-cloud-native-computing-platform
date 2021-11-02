# k8s-scheduling-based-on-networking-latency-in-cloud-native-computing-platform

## Kubernetes?

쿠버네티스는 클러스터 내에서 컨테이너의 집합체인 파드의 배치와 유지 및 보수를 책임지는 컨테이너 오케스트레이션 서비스입니다.

쿠버네티스는 사용자의 kubectl 명령에 의해 파드를 적절한 노드에 배치하고 관리를 하는 역할로 많이 사용되고 있습니다.

그중 파드를 배치하는 과정에서 **쿠버네티스의 스케쥴러**가 이용됩니다.



----

### Kubernetes Scheduler?

쿠버네티스 스케쥴러는 파드의 목적에 알맞은 적절한 노드를 찾아내어 배치합니다.

이때, 스케쥴러는 Filtering(필터링), Scoring(스코어링) 과정을 거칩니다.



----

#### Filtering

Taint(테인트)와 Toleration(톨러레이션), Affinity(어피니티)를 고려하여 파드에 어울리지 못하는 노드를 걸러내는 과정입니다.

- 어피니티: 노드가 어떤 파드를 원하는지 나타냅니다.
- 테인트: 노드가 어떤 파드를 싫어하는지 나타냅니다.
- 톨러레이션: 파드가 테인트를 수용할 수 있는지(무시할 수 있는지) 나타냅니다.

필터링 과정을 통해 사용 가능한 노드를 추려낸 후, 스코어링을 거칩니다.


----

#### Scoring

가능한 노드들에 점수를 부과하여 파드와 가장 어울리는 노드를 선택하는 과정입니다.

최적의 노드를 선택한 이후 바인딩 과정을 거쳐 파드가 배치됩니다.



----

## Iperf3

Server - Client 간의 네트워크 대역폭을 측정할 수 있는 툴입니다.

### Bandwidth

네트워크 측면에서의 대역폭은 **일정한 시간 내에 데이터 연결을 도와줄 수 있는 정보량의 척도**입니다.

-----

## What I want to do

쿠버네티스 스케쥴러의 필터링 및 스코어링 과정에서 네트워크 요소는 사용되지 않고 있습니다.

클러스터 내 노드에 iperf3 파드를 배치하여 노드 간의 네트워크 지연시간을 측정합니다.

측정한 네트워크 지연시간을 기반으로 파드를 배치할 수 있는 커스터마이즈드 스케쥴러를 파이썬으로 구성하였습니다.



-----

## Overview

![Overview](https://user-images.githubusercontent.com/77374551/139871782-5b8ba578-1a2d-49ef-919c-6e82691811bd.png)

- 3대의 노드로 클러스터 구성하였습니다. (master, worker1, worker2)
- iperf3 파드를 배치하여 주기적으로 네트워크 지연시간 데이터 수집합니다.
- 수집한 데이터를 토대로 master 노드에서 가장 가까운 노드에 파드를 모두 배치됩니다.



----

## Result

![Result](https://user-images.githubusercontent.com/77374551/139873280-c3489108-977c-4eca-a91e-205d684fef41.png)

- sb1 (worker1)이 master 노드와 네트워크 지연시간이 더 짧습니다.
- 이 정보에 맞춰 파이썬 기반 커스터마이즈드 스케쥴러가 작동되어 bookinfo 파드 샘플을 모두 sb1에 배치한 모습입니다.
