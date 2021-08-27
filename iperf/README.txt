이를 쓰고 싶으면 다음과 같이 해야합니다.

1. kubectl apply -f iperf3.yaml
// 당연히 kubernetes cluster는 구성하셨겠죠?

2. python3 measure.py
// 실행하면 자동적으로 latency 디렉토리에 노드 개수만큼 latency.json 파일이 생성됩니다. 계속 읽고 지웠다가 반복합니다.

3. 알아서 잘 사용하면 됩니다!
// 저는 이 값을 이용해서 kubernetes customized cluster를 만들 생각인데, kafka를 이용해서 실시간으로 받을 수 있게끔 만들어줘야겠군요.
