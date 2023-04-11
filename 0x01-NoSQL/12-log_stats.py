#!/usr/bin/env python3
"""log nginx stats"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for methodN in methods:
        print(f"\tmethod {methodN}:\
            {nginx.count_documents({'method': methodN})}")
    print(f'{nginx.count_documents({"method": "GET", "path": "/status"})} \
        status check')
