from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(5):
    msg = f'Сообщение {i}'
    producer.send('test-topic', msg.encode('utf-8'))
    print(f'Отправлено: {msg}')

producer.flush()
