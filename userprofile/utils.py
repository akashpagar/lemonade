from pymongo import MongoClient
from bson import json_util
import json


MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
DB_NAME = 'lemonade_10001'
COLLECTION_NAME = 'userprofile_user'


def connect():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    return connection

def close_conn(conn):
    if isinstance(conn, MongoClient):
        print('conn is object of MongoClient')
        conn.close()
    else:
        print('conn is not object of MongoClient')


def get_user_details(user_id):
    conn = connect()
    collection = conn[DB_NAME][COLLECTION_NAME]
    #{'_id':'5bd6f63ca2156207c6d9c888'}
    data = collection.find({'_id':json_util.ObjectId(user_id)})
    json_projects = []
    for project in data:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    conn.close()
    return json.loads(json_projects)
