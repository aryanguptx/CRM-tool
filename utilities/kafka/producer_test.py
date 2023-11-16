from kafka import KafkaProducer

broker_hosts = ["aryan-Swift-SF314-55G:9092"]
producer = KafkaProducer(bootstrap_servers=broker_hosts)


def send_messages(data):

    topic = "testtopic"
    producer.send(topic, data.encode())
    print(f"Sent message: {data}")


if __name__ == "__main__":
    send_messages("apple")
