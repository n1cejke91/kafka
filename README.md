# kafka

## 1. Запустить Kafka с помощью Docker Compose

Создать файл docker-compose.yml:

```yml
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

Запустить Kafka:

```bash
docker-compose up -d
```

Проверить, что Kafka работает:

```bash
docker ps
```

## 2.Отправить сообщения с помощью утилиты kafka-producer

Войти в контейнер Kafka:

```bash
docker exec -it <container_name> bash
```

Создать топик:

```bash
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Отправить сообщение:

```bash
kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```

## 3. Прочитать сообщения с помощью kafka-consumer

```bash
kafka-console-consumer --topic test-topic --from-beginning --bootstrap-server localhost:9092
```

Убедиться, что ранее отправленные сообщения получены  

## 4. Отправка и чтение сообщений с помощью Python

Установить зависимости:

```bash
pip install kafka-python
```

Отправка сообщений (producer.py):

```python
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(5):
    msg = f'Сообщение {i}'
    producer.send('test-topic', msg.encode('utf-8'))
    print(f'Отправлено: {msg}')

producer.flush()
```

Чтение сообщений (consumer.py):

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group')

for message in consumer:
    print(f"Получено: {message.value.decode('utf-8')}")
```

```bash
python producer.py
python consumer.py
```
