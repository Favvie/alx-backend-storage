#!/usr/bin/env python3
<<<<<<< HEAD
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    # get number of documents in collection
    docs_num = nginx_logs.count_documents({})
    get_num = nginx_logs.count_documents({'method': 'GET'})
    post_num = nginx_logs.count_documents({'method': 'POST'})
    put_num = nginx_logs.count_documents({'method': 'PUT'})
    patch_num = nginx_logs.count_documents({'method': 'PATCH'})
    delete_num = nginx_logs.count_documents({'method': 'DELETE'})
    get_status = nginx_logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    print("{} logs".format(docs_num))
    print("Methods:")
    print("\tmethod GET: {}".format(get_num))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))
    
=======
""" 12-log_stats.py """
from pymongo import MongoClient


def main():
    """Python script that provides some stats about
    Nginx logs stored in MongoDB
    Database: logs
    Collection: nginx

    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    (see example below - warning: it’s a tabulation before each line)

    one line with the number of documents with:
        method=GET
        path=/status"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"""\tmethod {method}: {nginx.count_documents(
                {"method": method})}"""
              )
    print(f"""{nginx.count_documents({
            "method": "GET", "path": "/status"})} status check"""
          )


if __name__ == "__main__":
    main()
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222
