from pymongo.mongo_client import MongoClient # type: ignore
import pandas as pd
import json

#url
uri="mongodb+srv://jatinbansal52846:12345@cluster0.4e6v5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="sensor_faut_detection"
COLLECTION_NAME='waferfault'

df=pd.read_csv("E:\4 Data Science\12 Project\Sensor Fault Detection\notebook\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)