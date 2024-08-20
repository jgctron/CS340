from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelterCRUD:
    def __init__(self, username, password, host='nv-desktop-services.apporto.com', port=32681):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return False

    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return []

    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return 0
