from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.mymongodb    #Select the database
LOL_WC = db.todo #Select the collection name

def insert_db(name, country, pool=1, used=1):
    LOL_WC.insert({ "name": name, "country": country, "pool": pool, "used": used})

if __name__ == "__main__":
    print('?')

