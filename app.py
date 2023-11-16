from flask import *
import requests, json
from utilities.kafka.producer_test import send_messages

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('/home/aryan/Desktop/CRM2/anon-ecommerce-website/index.html')


@app.route("/pushtotopic")
def push_to_topic():
    data = 5
    #data = request.json['data']
    send_messages(data)


if __name__ == "__main__":
    app.run(debug=True)





"""
./zookeeper-server-start.sh ../config/zookeeper.properties
./kafka_dependency-server-start.sh ../config/server.properties
 ./kafka_dependency-topics.sh --bootstrap-server aryan-Swift-SF314-55G:9092 --create --topic testtopic --partitions 1 --replication-factor 1
"""
