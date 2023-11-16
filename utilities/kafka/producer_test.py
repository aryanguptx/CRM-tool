from kafka import KafkaProducer

# Define the Kafka broker connection details
broker_hosts = ["aryan-Swift-SF314-55G:9092"]

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=broker_hosts)

def send_messages():
    while True:
        message = input("Enter message to send: ")
        topic = "testtopic"

        producer.send(topic, message.encode())
        print(f"Sent message: {message}")

if __name__ == "__main__":
    send_messages()
