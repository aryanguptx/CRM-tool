from kafka import KafkaConsumer

# Define the Kafka broker connection details
broker_hosts = ["aryan-Swift-SF314-55G:9092"]

# Create a Kafka consumer instance
consumer = KafkaConsumer(bootstrap_servers=broker_hosts,  auto_offset_reset="latest")
consumer.subscribe(["testtopic"])

def consume_messages():
    while True:
        event = consumer.poll()
        if event:
            for topic_partition, records in event.items():
                for msg in records:
                    # Extract the message value from the ConsumerRecord
                    message_value = msg.value

                    # Decode the message value based on the encoding used
                    message = message_value.decode()
                    print(f"Received message: {message} and event is {event}")

if __name__ == "__main__":
    consume_messages()

