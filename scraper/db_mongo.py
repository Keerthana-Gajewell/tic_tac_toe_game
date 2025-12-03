from pymongo import MongoClient #
from config import settings 

def save_to_mongo(data):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]
    coll = db[settings.MONGO_COLLECTION]
    # insert many
    if data:
        coll.insert_many(data)
    print(f"Saved {len(data)} records to MongoDB collection {settings.MONGO_COLLECTION}")
    client.close()
