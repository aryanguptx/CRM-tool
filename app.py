from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)


"""
./zookeeper-server-start.sh ../config/zookeeper.properties
./kafka_dependency-server-start.sh ../config/server.properties
 ./kafka_dependency-topics.sh --bootstrap-server aryan-Swift-SF314-55G:9092 --create --topic testtopic --partitions 1 --replication-factor 1
"""
