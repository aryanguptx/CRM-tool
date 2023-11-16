# #'aryan-Swift-SF314-55G:9092'
#
# from kafka import KafkaProducer, KafkaConsumer
#
# # Create a Kafka producer
# producer = KafkaProducer(bootstrap_servers=['aryan-Swift-SF314-55G:9092'
# ])
#
# # Produce a message to the topic 'testtopic'
# producer.send('testtopic', b'Hello, Kafka!')
#
# # Create a Kafka consumer
# consumer = KafkaConsumer(bootstrap_servers=['aryan-Swift-SF314-55G:9092'
# ], auto_offset_reset='latest', group_id='my-consumer-group')
#
# # Subscribe to the topic 'testtopic'
# consumer.subscribe(['testtopic'])
#
# # Consume messages from the topic
# while True:
#     message = consumer.poll(timeout_ms=100)
#
#     if message:
#         for m in message:
#             print(m.value.decode())

import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

async def main():
    # Define the Kafka broker connection details
    broker_hosts = ['aryan-Swift-SF314-55G:9092']

    # Create a Kafka producer instance within the async function
    async with AIOKafkaProducer(bootstrap_servers=broker_hosts) as producer:
        message = "Hello, Kafka!".encode()
        topic = "testtopic"

        await producer.send_and_wait(topic, message)
        print(f"Sent message: {message}")

    # Create a Kafka consumer instance within the async function
    async with AIOKafkaConsumer(bootstrap_servers=broker_hosts, group_id='my-consumer-group', auto_offset_reset="latest") as consumer:
        consumer.subscribe(["testtopic"])

        while True:
            event = await consumer.poll()
            message = event['value']
            print(f"Received message: {message}")

# Start the main function
asyncio.run(main())

