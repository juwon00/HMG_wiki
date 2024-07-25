## Docker image build

```bash
docker-compose build
```

<br>
<br>

## Docker container run

```bash
docker-compose up -d
```

<br>
<br>

## Data Operations

- 파이썬 파일 실행

```bash
/opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark/scripts/pi.py
```

<br>

## Error

- 아래와 같이 쓰면 로컬에서 돌아감 - worker 노드를 쓰지 않음, Web에 완료되었다고 뜨지 않음

```bash
/opt/spark/bin/spark-submit /opt/spark/scripts/pi.py
```

<br>
