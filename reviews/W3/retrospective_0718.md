# 오전 스크럼

### 어제는 무얼 했나 ?

- 태규님: 잠만 잤음. 하반기 원서
- 주원님: M1 완료 M2막혀서 막힌채로 왔습니다

### 오늘은 무엇을 할 것인가?

- 11시 반부터 주제 이야기

# 점심 세션

### 이번 주 계획이 어떻게 되나 ?

- 미션…

# 저녁 회고

### 오늘은 무얼 했나 ?

- 태규님: W3M2a를 마무리하고 갈겁니다. 그래야 내일 2b까지 마무리
- 주원님: W3M2a 마무리하고 W3M2b로 넘어가려고 합니다. 근데 어떻게 접근해야 할지 잘 모르겠어서 살펴보는 중이에요

### 내일은 어떻게 ?

- W3M2b까지 마무리
- 아침 스크럼 때 2가지 주제에 대한 구체화를 마칩시다.

<br>
<br>
<br>

# 정리

- `start-dfs.sh`
    - `hdfs-site.xml` 파일에 따라
    - DataNode, NameNode, SecondaryNameNode가 생김
    - 따로 생기게 하려면 아래처럼 각각 실행
    - `hdfs --daemon start namenode
    hdfs --daemon start secondarynamenode`
    - `hdfs --daemon start datanode`
- `start-yarn.sh`
    - ResourceManager, NodeManager가 생김
    - 따로 생기게 하려면 아래처럼 각각 실행
    - `yarn --daemon start resourcemanager`
    - `yarn --daemon start nodemanager`

- `cat /usr/local/hadoop/logs/hadoop-hadoopuser-namenode-hadoop-master.log`
    - 로그로 어디서 에러가 생겼는지 확인 가능

<br>
<br>

## keep
삽질을 잘했다.<br>
정리도 노션에 했다.<br>
싸워서 점점 이기는 중이다.
<br>
<br>
W3M2a를 마무리하고 W3M2b를 하려고 하는데 어떻게 접근할지 아직 감이 안잡히네요
## problem
비즈니스 가치를 생각하다가 돌고돌아 처음으로 돌아왔다.<br>
어떤 웹툰, 유튜버등을 선택할 수 있게 리스트를 뽑는 것을 도와주자.<br>
근데 위와같이 말하면 Dano님에게 피드백 받을게 눈에 보인다.<br>
근데 회의를 하다보니 무한굴레에 빠져서 위와 같은 결론으로 돌아온다.<br>
그럼 문제 자체가 그냥 문제인건가?<br>
Dano님의 피드백으로 해결할 예정 !
<br>
<br>

## try
딱히 없는것 같다.
<br>
<br>
