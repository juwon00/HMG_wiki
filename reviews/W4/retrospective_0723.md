# 정리
~~~bash
#Spark 다운로드 및 설치
RUN mkdir -p /tmp && \
    cd /tmp && \
    wget https://dlcdn.apache.org/spark/spark-3.4.3/spark-3.4.3-bin-hadoop3.tgz && \
    tar -xvzf spark-3.4.3-bin-hadoop3.tgz -C /opt && \
    mkdir -p /opt/spark && \
    mv /opt/spark-3.4.3-bin-hadoop3/* /opt/spark && \
    chown -R sparkuser:sparkuser /opt/spark
~~~
<br>
<br>

## keep
미로찾기 길을 따라 들어갔다.<br>
스파크를 하나하나 설치해 보고 있는 중이다.<br>
길을 찾아 나가면 도커 파일을 작성할 것이다.

남아서 공부를 더 했다.<br>
집에서 하는것보다 집중이 잘 된다.<br>
더 재미도 있는것 같다.
<br>
<br>

## problem
프로젝트 주제에 대해 조금 더 데이터를 찾아보고, 가능한 프로토타입 형태를 생각해 봐야할 것 같다.
<br>
<br>

## try
딱히 없는것 같다.
<br>
<br>
