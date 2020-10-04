from pymongo import MongoClient

DB_NOBEL_PRIZE = 'nobel_prize'

COUNTRIES_COLLECTION = 'country_data'

def get_mongo_db(db_name=DB_NOBEL_PRIZE, host='localhost', port=27017, username=None, password=None):
    """Connect to MongoDB with or without authentication"""
    if username and password:
        return MongoClient(f'mongodb://{username}:{password}@{host}/{port}').get_database(db_name)
    return MongoClient(host=host, port=port).get_database(db_name)