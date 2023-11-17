from kafka import KafkaProducer
from json import dumps


my_producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda x: dumps(x).encode('utf-8')
    )


def send_messages(message):

    topic = "testtopic"
    data = {'value': message}
    my_producer.send(topic, data)
    print(f"Sent message: {data}")
    my_producer.flush()


if __name__ == "__main__":
    send_messages("sdf")
