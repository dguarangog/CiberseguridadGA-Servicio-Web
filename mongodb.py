from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

class MongoDriver:
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        hostname = os.getenv('MONGO_HOSTNAME')
        uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

    def insert_record(self, record: dict, username: str):
        self.client.get_database('pry_test_fin_tratam_datos').get_collection(f'{username}_TEST-FINAL').insert_one(record)
    def consulta_record(self,username: str):
        registros = self.client.get_database('pry_test_fin_tratam_datos').get_collection(f'{username}_TEST-FINAL').find({})
        return registros
    def consulta_record_one(self,record: dict, username: str):
        registros = self.client.get_database('pry_test_fin_tratam_datos').get_collection(f'{username}_TEST-FINAL').find_one(record)
        return registros

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Te conectaste exitosamente a MongoDB!")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    mi_base_de_datos = MongoDriver()

    num_reg=mi_base_de_datos.consulta_record(username="REGISTROS")
    print(num_reg)

