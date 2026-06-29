from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient(
    "mongodb+srv://galeaioanstefan_db_user:pATV9eNo8xIHhFv3@loracluster.xme5q68.mongodb.net/?appName=LoRaCluster"
)

db = client["coordinates_db"]

collection = db["lat_lon_data"]
    
@app.get("/coordinate_data")
def data_link():

    data = list(
        collection.find(
            {},
            {"_id": 0}
        )
    )

    return data

