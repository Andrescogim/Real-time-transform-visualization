from kafka import KafkaConsumer, KafkaProducer
import json


consumer = KafkaConsumer('aviones_pr2', bootstrap_servers='localhost:9092')

# producer = KafkaProducer('av_pr_transformed' ,bootstrap_servers='localhost:9092')
# producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for msg in consumer:
    print (msg.value)
    producer.send('av_pr_transformed', msg.value)

