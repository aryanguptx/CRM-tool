from kafka import KafkaConsumer
from json import loads
broker_hosts = ["localhost:9092"]

# Create a Kafka consumer instance
consumer = KafkaConsumer(bootstrap_servers=broker_hosts, group_id = None, auto_offset_reset="earliest", value_deserializer = lambda x : loads(x.decode('utf-8'))  )
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

                    print(f"Received message: {message_value}")


if __name__ == "__main__":
    consume_messages()

