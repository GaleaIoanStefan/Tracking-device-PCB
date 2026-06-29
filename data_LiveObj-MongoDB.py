import json
from paho.mqtt import client as mqtt
from pymongo import MongoClient
from fastapi import FastAPI

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("fifo/Tracking_Device_FIFO")

def on_message(client, userdata, msg):
    # these commands convert message to dictionary and send to mongodb
    data = json.loads(msg.payload)
    collection.insert_one(data)
    
    
    grafana_data = {
        "latitude": data["value"]["latitude"],
        "lat_indicator": data["value"]["lat_indicator"],
        "longitude": data["value"]["longitude"],
        "lon_indicator": data["value"]["lon_indicator"],
        "timestamp": data["timestamp"]
    }

    collection_grafana.insert_one(grafana_data)

    print(msg.topic+" "+str(msg.payload))

#  connection to the live objects server, for lora dummy data
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set("application", "21fc8b0d447a47469fe92701b71dacf0")
mqttc.tls_set()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("liveobjects.orange-business.com", 8883, 60)

# mongodb client and data routing
client = MongoClient("mongodb+srv://galeaioanstefan_db_user:pATV9eNo8xIHhFv3@loracluster.xme5q68.mongodb.net/?appName=LoRaCluster")
db = client['coordinates_db']
collection = db['full_message']
collection_grafana = db['lat_lon_data']

# runs indefinitly to it receives messages
mqttc.loop_forever()
